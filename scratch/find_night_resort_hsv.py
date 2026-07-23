import os
import cv2
import numpy as np

def find_night_resort_candidate():
    # p9.JPG is the day resort shot. We want to find the night version.
    # The night version should be dark overall, but have bright yellow/orange lights in the middle.
    candidates = [f"p{i}.JPG" for i in range(1, 16) if os.path.exists(f"p{i}.JPG")]
    
    # Also add assets images
    assets_dir = 'assets'
    if os.path.exists(assets_dir):
        for f in os.listdir(assets_dir):
            if f.lower().endswith(('.jpg', '.jpeg', '.png')):
                candidates.append(os.path.join(assets_dir, f))
                
    results = []
    for path in candidates:
        try:
            img = cv2.imread(path)
            if img is None:
                continue
            h, w, _ = img.shape
            
            # Convert to gray
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            avg_brightness = np.mean(gray)
            
            # If the image is too bright, it's not a night shot
            if avg_brightness > 80:
                continue
                
            # Night shot of resort has bright yellow/orange lights.
            # Convert to HSV to find yellow/orange colors.
            hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            
            # Define range for yellow/orange light glow
            lower_glow = np.array([10, 50, 150])
            upper_glow = np.array([30, 255, 255])
            
            mask = cv2.inRange(hsv, lower_glow, upper_glow)
            glow_pixels = np.sum(mask > 0)
            
            results.append((path, avg_brightness, glow_pixels))
        except Exception as e:
            pass
            
    results.sort(key=lambda x: x[2], reverse=True)
    print("Candidates sorted by amount of warm light glow pixels (night shots with lights):")
    for path, b, glow in results[:10]:
        print(f"{path}: brightness={b:.2f}, glow_pixels={glow}")

if __name__ == '__main__':
    find_night_resort_candidate()
