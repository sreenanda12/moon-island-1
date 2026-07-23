import os
from PIL import Image
import numpy as np

def get_brightness(image_path):
    try:
        with Image.open(image_path) as img:
            img_gray = img.convert('L')
            arr = np.array(img_gray)
            return np.mean(arr)
    except Exception as e:
        return None

def main():
    images = []
    for f in os.listdir('.'):
        if f.lower().endswith(('.jpg', '.jpeg', '.png')):
            b = get_brightness(f)
            if b is not None:
                images.append((f, b))
                
    assets_dir = 'assets'
    if os.path.exists(assets_dir):
        for f in os.listdir(assets_dir):
            if f.lower().endswith(('.jpg', '.jpeg', '.png')):
                path = os.path.join(assets_dir, f)
                b = get_brightness(path)
                if b is not None:
                    images.append((path, b))
                    
    images.sort(key=lambda x: x[1])
    print("Images sorted by average brightness (darkest first):")
    for path, b in images:
         print(f"{path}: brightness={b:.2f}")

if __name__ == '__main__':
    main()
