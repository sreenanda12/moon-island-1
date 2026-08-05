from PIL import Image
import numpy as np

# Load git version of p4.png using inspect_git_images method
import subprocess, io

def get_git_image(path):
    proc = subprocess.run(['git', 'show', f'HEAD:{path}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode == 0:
        return Image.open(io.BytesIO(proc.stdout))
    return None

img = get_git_image('p4.png')
if img:
    w, h = img.size
    data = np.array(img)
    
    # Gold border color is roughly [216, 165, 82] (CSS gold is #D8A552)
    # Let's search for pixels close to [216, 165, 82] or [218, 165, 32]
    # Let's find all pixels where R > 150, G > 120, B < 120
    r, g, b = data[:, :, 0], data[:, :, 1], data[:, :, 2]
    alpha = data[:, :, 3]
    gold_mask = (r > 150) & (g > 120) & (b < 120) & (alpha == 255)
    
    y_idx, x_idx = np.where(gold_mask)
    print("Number of gold-ish pixels found:", len(y_idx))
    if len(y_idx) > 0:
        print("Gold-ish pixel range: x from", np.min(x_idx), "to", np.max(x_idx), ", y from", np.min(y_idx), "to", np.max(y_idx))
        # Print a few sample coordinates and colors
        for i in range(min(10, len(y_idx))):
            y, x = y_idx[i], x_idx[i]
            print(f"({x}, {y}):", data[y, x, :3])
    else:
        print("No gold-ish pixels found.")
else:
    print("Could not load git image.")
