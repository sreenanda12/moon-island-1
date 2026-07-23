import os
import shutil
from PIL import Image

def resize_and_copy(src, dest_dir, width=600):
    try:
        filename = os.path.basename(src)
        dest_path = os.path.join(dest_dir, filename)
        with Image.open(src) as img:
            # maintain aspect ratio
            w, h = img.size
            height = int(h * (width / w))
            resized = img.resize((width, height), Image.Resampling.LANCZOS)
            # save as PNG or JPEG depending on extension
            resized.save(dest_path)
            print(f"Copied & resized {src} to {dest_path}")
    except Exception as e:
        print(f"Error copying {src}: {e}")

def main():
    dest_dir = r"C:\Users\sreenanda\.gemini\antigravity-ide\brain\1f6317df-f1fe-4527-991f-30ea40681df6"
    os.makedirs(dest_dir, exist_ok=True)
    
    # Candidates in assets
    candidates = [
        'assets/moonlit_backwater_hero.png',
        'assets/moonlit_backwaters_hero.png',
        'assets/kerala_backwater_hero.png',
        'assets/hero.png',
        'assets/hero-bg.png',
        'assets/moon_bg.png'
    ]
    
    # Check if any p*.JPG is a night shot. We noticed p13.JPG was dark, let's add it
    for i in range(1, 16):
        p_path = f"p{i}.JPG"
        if os.path.exists(p_path):
            candidates.append(p_path)
            
    for c in candidates:
        if os.path.exists(c):
            resize_and_copy(c, dest_dir)

if __name__ == '__main__':
    main()
