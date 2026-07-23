import os
import cv2
import numpy as np

def find_matching_resort_image():
    # Load base image (p9.JPG is the day resort image)
    base_path = 'p9.JPG'
    if not os.path.exists(base_path):
        print("Base image p9.JPG not found.")
        return
    
    img1 = cv2.imread(base_path, cv2.IMREAD_GRAYSCALE)
    # Resize for faster feature matching
    img1 = cv2.resize(img1, (800, int(800 * img1.shape[0] / img1.shape[1])))
    
    orb = cv2.ORB_create(nfeatures=1000)
    kp1, des1 = orb.detectAndCompute(img1, None)
    
    if des1 is None:
        print("No descriptors found in base image.")
        return

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    
    candidates = []
    # Root JPG files (p1-p15, except p9)
    for f in os.listdir('.'):
        if f.lower().endswith(('.jpg', '.jpeg', '.png')) and f != 'p9.JPG' and not f.startswith('p9'):
            candidates.append(f)
            
    # Assets files
    assets_dir = 'assets'
    if os.path.exists(assets_dir):
        for f in os.listdir(assets_dir):
            if f.lower().endswith(('.jpg', '.jpeg', '.png')):
                candidates.append(os.path.join(assets_dir, f))
                
    results = []
    for cand in candidates:
        try:
            img2 = cv2.imread(cand, cv2.IMREAD_GRAYSCALE)
            if img2 is None:
                continue
            img2 = cv2.resize(img2, (800, int(800 * img2.shape[0] / img2.shape[1])))
            kp2, des2 = orb.detectAndCompute(img2, None)
            if des2 is None:
                continue
            matches = bf.match(des1, des2)
            # Filter good matches
            matches = sorted(matches, key=lambda x: x.distance)
            good_matches = [m for m in matches if m.distance < 50]
            results.append((cand, len(good_matches)))
        except Exception as e:
            # print(f"Error processing {cand}: {e}")
            pass
            
    results.sort(key=lambda x: x[1], reverse=True)
    print("Top matched images (highest matching features with p9.JPG first):")
    for path, matches_count in results[:10]:
        print(f"{path}: {matches_count} matches")

if __name__ == '__main__':
    find_matching_resort_image()
