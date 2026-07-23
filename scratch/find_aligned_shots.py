import os
import cv2
import numpy as np

def find_aligned_shots():
    base_path = 'p9.JPG'
    if not os.path.exists(base_path):
        print("Base image p9.JPG not found.")
        return
        
    img1 = cv2.imread(base_path, cv2.IMREAD_GRAYSCALE)
    img1 = cv2.resize(img1, (600, 400))
    edges1 = cv2.Canny(img1, 50, 150)
    
    candidates = [f"p{i}.JPG" for i in range(1, 16) if i != 9 and os.path.exists(f"p{i}.JPG")]
    
    results = []
    for cand in candidates:
        img2 = cv2.imread(cand, cv2.IMREAD_GRAYSCALE)
        if img2 is None:
            continue
        img2 = cv2.resize(img2, (600, 400))
        edges2 = cv2.Canny(img2, 50, 150)
        
        # Compute correlation coefficient of edge images
        correlation = np.corrcoef(edges1.flat, edges2.flat)[0, 1]
        results.append((cand, correlation))
        
    results.sort(key=lambda x: x[1], reverse=True)
    print("Edge correlation with p9.JPG (highest first):")
    for path, corr in results:
        print(f"{path}: correlation={corr:.4f}")

if __name__ == '__main__':
    find_aligned_shots()
