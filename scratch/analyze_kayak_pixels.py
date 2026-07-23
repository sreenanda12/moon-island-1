import os
from PIL import Image
import numpy as np

def analyze_kayak_pixels():
    c = 'kayak.png'
    if not os.path.exists(c):
        print(f"File {c} not found.")
        return
    try:
        with Image.open(c) as img:
            arr = np.array(img)
            # Find average of R, G, B channels where alpha > 0
            if arr.shape[2] == 4:
                mask = arr[:, :, 3] > 0
                if np.sum(mask) > 0:
                    r_avg = np.mean(arr[:, :, 0][mask])
                    g_avg = np.mean(arr[:, :, 1][mask])
                    b_avg = np.mean(arr[:, :, 2][mask])
                    print(f"kayak.png (non-transparent pixels): R_avg={r_avg:.2f}, G_avg={g_avg:.2f}, B_avg={b_avg:.2f}")
                else:
                    print("kayak.png is entirely transparent.")
            else:
                print("kayak.png has no alpha channel.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    analyze_kayak_pixels()
