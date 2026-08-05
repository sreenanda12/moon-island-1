from PIL import Image
import numpy as np

img = Image.open('p4_backup.png')
w, h = img.size
print("Image size:", w, h)
data = np.array(img)

# Let's inspect the bounding box of non-transparent pixels again
alpha = data[:, :, 3]
non_transparent = np.where(alpha > 0)
print(f"Non-transparent box: y from {np.min(non_transparent[0])} to {np.max(non_transparent[0])}, x from {np.min(non_transparent[1])} to {np.max(non_transparent[1])}")

# Let's inspect the colors along the edge of the non-transparent box
# Left edge (x = 94)
left_edge_colors = data[13:666, 94, :3]
# Let's print unique colors on the left edge or some sample colors
print("Sample colors along left edge:")
for y in range(13, 50):
    print(f"y={y}: {data[y, 94, :]}")
