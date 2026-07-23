import os
from PIL import Image

def inspect_images():
    print("=== ROOT IMAGES ===")
    for f in os.listdir('.'):
        if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
            try:
                with Image.open(f) as img:
                    print(f"{f}: {img.format}, {img.size}, {os.path.getsize(f)} bytes")
            except Exception as e:
                print(f"{f}: Error opening - {e}")
                
    print("\n=== ASSETS IMAGES ===")
    assets_dir = 'assets'
    if os.path.exists(assets_dir):
        for f in os.listdir(assets_dir):
            if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.webp')):
                path = os.path.join(assets_dir, f)
                try:
                    with Image.open(path) as img:
                        print(f"{f}: {img.format}, {img.size}, {os.path.getsize(path)} bytes")
                except Exception as e:
                    print(f"{f}: Error opening - {e}")

if __name__ == '__main__':
    inspect_images()
