import os
import cv2
import numpy as np

def inspect_bottom_right():
    candidates = [
        'assets/bg-kayak.png',
        'assets/about_kayak_hero.png',
        'assets/bg-boat.png',
        'assets/bg-stay.png',
        'assets/bg-nature.png',
        'assets/kerala_backwater_hero.png',
        'assets/moonlit_backwater_hero.png'
    ]
    
    for c in candidates:
        if not os.path.exists(c):
            continue
        try:
            img = cv2.imread(c)
            h, w, _ = img.shape
            # Crop bottom right quarter
            br_crop = img[int(h*0.5):, int(w*0.5):]
            # Convert to gray
            gray = cv2.cvtColor(br_crop, cv2.COLOR_BGR2GRAY)
            # Find minimum brightness (potential silhouette) and maximum (water reflection)
            min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(gray)
            avg_val = np.mean(gray)
            print(f"{c}: size={w}x{h}, BR average={avg_val:.2f}, BR min={min_val:.2f}, BR max={max_val:.2f}")
        except Exception as e:
            print(f"Error {c}: {e}")

if __name__ == '__main__':
    inspect_bottom_right()
