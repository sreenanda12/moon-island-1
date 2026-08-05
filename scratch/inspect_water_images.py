# Check dimensions and check if there are moonlit backwaters image assets
from PIL import Image

images = [
    'assets/moonlit_backwaters_hero.png',
    'assets/moonlit_backwater_hero.png',
    'assets/kerala_backwater_hero.png',
    'assets/bg-boat.png'
]

for img_path in images:
    try:
        with Image.open(img_path) as img:
            print(f"{img_path}: size={img.size}, mode={img.mode}")
    except Exception as e:
        print(f"Error opening {img_path}: {e}")
