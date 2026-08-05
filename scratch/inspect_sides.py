from PIL import Image
import numpy as np

img = Image.open('p4.JPG')
w, h = img.size
pixels = np.array(img)

# Print col means for left 50 cols
print("LEFT 50 COLS:")
for x in range(50):
    col_mean = np.mean(pixels[:, x, :], axis=0)
    if all(val < 15 for val in col_mean):
        print(f"Col {x:02d} mean RGB: {col_mean} (DARK)")
    else:
        print(f"Col {x:02d} mean RGB: {col_mean} (CONTENT STARTS)")
        break

# Print col means for right 50 cols
print("\nRIGHT 50 COLS:")
for x in range(w - 1, w - 51, -1):
    col_mean = np.mean(pixels[:, x, :], axis=0)
    if all(val < 15 for val in col_mean):
        print(f"Col {x:02d} mean RGB: {col_mean} (DARK)")
    else:
        print(f"Col {x:02d} mean RGB: {col_mean} (CONTENT STARTS)")
        break
