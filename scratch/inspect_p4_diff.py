from PIL import Image
import numpy as np

img_png = Image.open('p4.png')
img_jpg = Image.open('p4.JPG')

print("PNG size:", img_png.size)
print("JPG size:", img_jpg.size)

# Convert both to RGBA numpy arrays
png_arr = np.array(img_png)
jpg_arr = np.array(img_jpg)

# Check if the RGB channels of png_arr (where alpha > 0) are the same as jpg_arr
alpha = png_arr[:, :, 3]
mask = alpha > 0

rgb_png = png_arr[:, :, :3][mask]
rgb_jpg = jpg_arr[mask]

difference = np.abs(rgb_png.astype(float) - rgb_jpg.astype(float))
mean_diff = np.mean(difference)
max_diff = np.max(difference)

print("Mean RGB difference in non-transparent area:", mean_diff)
print("Max RGB difference in non-transparent area:", max_diff)
