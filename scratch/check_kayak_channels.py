import os
from PIL import Image

def check_kayak_channels():
    c = 'kayak.png'
    if not os.path.exists(c):
        print(f"File {c} not found.")
        return
    try:
        with Image.open(c) as img:
            print(f"kayak.png format: {img.format}, size: {img.size}, mode: {img.mode}")
            if img.mode == 'RGBA':
                # Check if there is non-trivial transparency
                alpha = img.split()[-1]
                extrema = alpha.getextrema()
                print(f"Alpha channel extrema: {extrema}")
            else:
                print("No alpha channel.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    check_kayak_channels()
