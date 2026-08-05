from PIL import Image
import numpy as np

path = 'assets/moon_bg.png'
try:
    with Image.open(path) as img:
        print(f"Image {path} size: {img.size}, mode: {img.mode}")
        img_rgba = img.convert('RGBA')
        pixels = np.array(img_rgba)
        alpha = pixels[:, :, 3]
        
        # Check if there are non-transparent pixels on the left side (cols 0 to 100)
        # and print their average color and opacity
        left_alpha = alpha[:, :100]
        num_non_transparent = np.sum(left_alpha > 0)
        print(f"Number of non-transparent pixels in the left-most 100 columns: {num_non_transparent}")
        
        if num_non_transparent > 0:
            avg_alpha = np.mean(left_alpha[left_alpha > 0])
            avg_color = np.mean(pixels[:, :100, :3][left_alpha > 0], axis=0)
            print(f"Average opacity of those pixels: {avg_alpha:.2f}/255")
            print(f"Average color of those pixels: {avg_color}")
            
        # Find the overall bounding box of non-transparent pixels (alpha > 0)
        content_mask = alpha > 0
        y_indices, x_indices = np.where(content_mask)
        if len(y_indices) > 0 and len(x_indices) > 0:
            print(f"Content Bounding Box: Left={np.min(x_indices)}, Right={np.max(x_indices)}, Top={np.min(y_indices)}, Bottom={np.max(y_indices)}")
            
            # Let's inspect the left boundary columns. Are they soft or sharp?
            left_col = np.min(x_indices)
            print(f"Content starts at column {left_col}")
            # Check the average alpha of the column where content starts
            col_alpha = alpha[:, left_col]
            print(f"Average alpha at column {left_col}: {np.mean(col_alpha[col_alpha > 0]):.2f}")
        else:
            print("Image is entirely transparent!")
except Exception as e:
    print(f"Error inspecting image: {e}")
