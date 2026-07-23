import os
from PIL import Image

def resize_and_copy(src, dest_dir, width=600):
    try:
        filename = os.path.basename(src)
        dest_path = os.path.join(dest_dir, filename)
        with Image.open(src) as img:
            w, h = img.size
            height = int(h * (width / w))
            resized = img.resize((width, height), Image.Resampling.LANCZOS)
            resized.save(dest_path)
            print(f"Copied & resized {src} to {dest_path}")
    except Exception as e:
        print(f"Error copying {src}: {e}")

def main():
    dest_dir = r"C:\Users\sreenanda\Desktop\moon islands\scratch"
    os.makedirs(dest_dir, exist_ok=True)
    
    candidates = [
        'assets/bg-kayak.png',
        'assets/bg-stay.png',
        'assets/bg-nature.png',
        'assets/bg-boat.png'
    ]
    
    for c in candidates:
        if os.path.exists(c):
            resize_and_copy(c, dest_dir)

if __name__ == '__main__':
    main()
