from PIL import Image
import numpy as np

def check_for_bright_moon(image_path):
    try:
        with Image.open(image_path) as img:
            w, h = img.size
            pixels = np.array(img.convert('RGB'))
            
            # The moon is usually a very bright circle (RGB values close to 255)
            # Let's count how many pixels are extremely bright (R > 220, G > 200, B > 180)
            bright_pixels = (pixels[:, :, 0] > 220) & (pixels[:, :, 1] > 200) & (pixels[:, :, 2] > 150)
            num_bright = np.sum(bright_pixels)
            
            # Find the center of these bright pixels
            y_indices, x_indices = np.where(bright_pixels)
            if len(y_indices) > 50:
                center_y = int(np.mean(y_indices))
                center_x = int(np.mean(x_indices))
                print(f"{image_path} contains a bright object (moon?) of size {len(y_indices)} px centered at ({center_x}, {center_y})")
            else:
                print(f"{image_path} does NOT contain a bright moon object (only {num_bright} bright pixels).")
    except Exception as e:
        print(f"Error checking {image_path}: {e}")

check_for_bright_moon('assets/moonlit_backwater_hero.png')
check_for_bright_moon('assets/moonlit_backwaters_hero.png')
check_for_bright_moon('assets/moon_bg.png')
