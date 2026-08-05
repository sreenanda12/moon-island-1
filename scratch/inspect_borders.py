from PIL import Image
import numpy as np

img = Image.open('p4.JPG')
w, h = img.size
pixels = np.array(img)

# Print row means for top 100 rows
print("TOP 100 ROWS:")
for y in range(100):
    row_mean = np.mean(pixels[y, :, :], axis=0)
    # Check if this row is mostly dark (threshold < 15 in all channels)
    if all(val < 15 for val in row_mean):
        print(f"Row {y:02d} mean RGB: {row_mean} (DARK)")
    else:
        print(f"Row {y:02d} mean RGB: {row_mean} (CONTENT STARTS)")
        break

# Print row means for bottom 100 rows
print("\nBOTTOM 100 ROWS:")
for y in range(h - 1, h - 101, -1):
    row_mean = np.mean(pixels[y, :, :], axis=0)
    # Check if this row is mostly dark
    if all(val < 15 for val in row_mean):
        print(f"Row {y:02d} mean RGB: {row_mean} (DARK)")
    else:
        print(f"Row {y:02d} mean RGB: {row_mean} (CONTENT STARTS)")
        break
