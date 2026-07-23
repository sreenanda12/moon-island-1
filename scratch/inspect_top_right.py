import os
import cv2
import numpy as np

def inspect_top_right():
    c = 'assets/bg-kayak.png'
    if not os.path.exists(c):
        print(f"File {c} not found.")
        return
    try:
        img = cv2.imread(c)
        h, w, _ = img.shape
        # Crop top right quarter
        tr_crop = img[:int(h*0.5), int(w*0.5):]
        # Convert to gray
        gray = cv2.cvtColor(tr_crop, cv2.COLOR_BGR2GRAY)
        avg_val = np.mean(gray)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(gray)
        print(f"{c}: TR average={avg_val:.2f}, TR min={min_val:.2f}, TR max={max_val:.2f}")
        
        # Check if there is a large bright circular region
        # Threshold to find bright areas
        _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
        white_pixels = np.sum(thresh > 0)
        print(f"{c}: TR white pixels (val > 200)={white_pixels} out of {gray.size}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    inspect_top_right()
