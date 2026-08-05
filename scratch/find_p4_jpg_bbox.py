from PIL import Image
import numpy as np

img = Image.open('p4.JPG')
w, h = img.size
pixels = np.array(img)

# We define non-black as any pixel where at least one channel is > 15
non_black_mask = np.any(pixels > 15, axis=2)

# Find coordinates where non_black_mask is True
y_indices, x_indices = np.where(non_black_mask)

if len(y_indices) > 0 and len(x_indices) > 0:
    min_y, max_y = np.min(y_indices), np.max(y_indices)
    min_x, max_x = np.min(x_indices), np.max(x_indices)
    print(f"Content Bounding Box in p4.JPG:")
    print(f"Left: {min_x} px (Inset: {min_x})")
    print(f"Right: {max_x} px (Inset from right: {w - 1 - max_x})")
    print(f"Top: {min_y} px (Inset: {min_y})")
    print(f"Bottom: {max_y} px (Inset from bottom: {h - 1 - max_y})")
    print(f"Opaque content width: {max_x - min_x + 1} px")
    print(f"Opaque content height: {max_y - min_y + 1} px")
else:
    print("No non-black content found in p4.JPG!")
