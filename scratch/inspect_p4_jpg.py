from PIL import Image
import numpy as np

img = Image.open('p4.JPG')
w, h = img.size
pixels = np.array(img)

# Print image shape
print(f"p4.JPG size: {w}x{h}")

# Check the first few rows (top 50 rows) for black/dark pixels
# Let's check the mean RGB value of the top 30 rows
for y in range(30):
    row_mean = np.mean(pixels[y, :, :], axis=0)
    print(f"Row {y:02d} mean RGB: {row_mean}")
