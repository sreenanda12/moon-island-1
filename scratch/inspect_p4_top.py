from PIL import Image
import numpy as np

img = Image.open('p4_backup.png')
w, h = img.size
data = np.array(img)
alpha = data[:, :, 3]

# Let's find all opaque pixels in the top row that contains any opaque pixel (ymin)
opaque_indices = np.where(alpha == 255)
ymin = np.min(opaque_indices[0])
xmin_at_ymin = np.min(opaque_indices[1][opaque_indices[0] == ymin])
xmax_at_ymin = np.max(opaque_indices[1][opaque_indices[0] == ymin])
print(f"At ymin={ymin}, opaque pixels range from x={xmin_at_ymin} to {xmax_at_ymin}")
print("Colors of these opaque pixels:")
for x in range(xmin_at_ymin, min(xmin_at_ymin + 10, xmax_at_ymin + 1)):
    print(f"x={x}:", data[ymin, x, :])
