# Check average colors at the bottom of each candidate image (lower 30%)
from PIL import Image
import numpy as np

images = [
    'assets/moonlit_backwaters_hero.png',
    'assets/moonlit_backwater_hero.png',
    'assets/kerala_backwater_hero.png',
    'assets/bg-boat.png'
]

for path in images:
    try:
        with Image.open(path) as img:
            pixels = np.array(img.convert('RGB'))
            h, w, _ = pixels.shape
            # Bottom 30%
            bottom_part = pixels[int(h*0.7):, :, :]
            mean_color = np.mean(bottom_part, axis=(0, 1))
            print(f"{path}: bottom 30% mean RGB={mean_color.astype(int)}")
    except Exception as e:
        print(f"Error checking {path}: {e}")
