from PIL import Image
import numpy as np

paths = ['assets/moonlit_backwater_hero.png', 'assets/moonlit_backwaters_hero.png', 'assets/kerala_backwater_hero.png']
for path in paths:
    try:
        with Image.open(path) as img:
            print(f"\nImage {path} size: {img.size}, mode: {img.mode}")
            img_rgba = img.convert('RGBA')
            pixels = np.array(img_rgba)
            alpha = pixels[:, :, 3]
            num_transparent = np.sum(alpha < 255)
            print(f"Number of non-opaque pixels: {num_transparent} out of {img.size[0] * img.size[1]} ({num_transparent / (img.size[0] * img.size[1]) * 100:.2f}%)")
            
            # Find bounding box of opaque pixels
            opaque_mask = alpha == 255
            y_indices, x_indices = np.where(opaque_mask)
            if len(y_indices) > 0 and len(x_indices) > 0:
                print(f"Opaque Bounding Box: Left={np.min(x_indices)}, Right={np.max(x_indices)}, Top={np.min(y_indices)}, Bottom={np.max(y_indices)}")
            else:
                print("Entirely transparent!")
    except Exception as e:
        print(f"Error inspecting image {path}: {e}")
