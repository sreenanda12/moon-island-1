import os
from PIL import Image
import numpy as np

def check_borders(image_path):
    try:
        with Image.open(image_path) as img:
            w, h = img.size
            
            # Convert to RGBA for PNG to check transparency, or RGB for JPEG to check black
            img_rgba = img.convert('RGBA')
            pixels = np.array(img_rgba)
            
            # Check transparency (alpha == 0) and black (RGB < 15)
            # A pixel is "empty" if it's transparent or black
            alpha = pixels[:, :, 3]
            rgb = pixels[:, :, :3]
            
            # Mask of empty pixels (either fully transparent or very dark black)
            empty_mask = (alpha == 0) | np.all(rgb < 15, axis=2)
            
            # Content mask (pixels that are NOT empty)
            content_mask = ~empty_mask
            
            y_indices, x_indices = np.where(content_mask)
            
            if len(y_indices) > 0 and len(x_indices) > 0:
                min_y, max_y = np.min(y_indices), np.max(y_indices)
                min_x, max_x = np.min(x_indices), np.max(x_indices)
                
                left_border = min_x
                right_border = w - 1 - max_x
                top_border = min_y
                bottom_border = h - 1 - max_y
                
                if left_border > 5 or right_border > 5 or top_border > 5 or bottom_border > 5:
                    print(f"\n[BORDER FOUND] {image_path}: size {w}x{h}")
                    print(f"  Empty Insets: Left={left_border}px, Right={right_border}px, Top={top_border}px, Bottom={bottom_border}px")
            else:
                print(f"Image {image_path} is entirely empty.")
    except Exception as e:
        print(f"Error checking {image_path}: {e}")

def main():
    print("Checking root directory images...")
    for f in os.listdir('.'):
        if f.lower().endswith(('.jpg', '.jpeg', '.png')) and not f.startswith('p4_backup') and not f.startswith('WhatsApp'):
            check_borders(f)
            
    print("\nChecking assets directory images...")
    assets_dir = 'assets'
    if os.path.exists(assets_dir):
        for f in os.listdir(assets_dir):
            if f.lower().endswith(('.jpg', '.jpeg', '.png')):
                check_borders(os.path.join(assets_dir, f))

if __name__ == '__main__':
    main()
