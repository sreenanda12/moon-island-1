from PIL import Image
import numpy as np

img = Image.open('p4_backup.png')
w, h = img.size
data = np.array(img)
alpha = data[:, :, 3]

# Print some stats about alpha values
print("Alpha min:", np.min(alpha))
print("Alpha max:", np.max(alpha))
print("Unique alpha values:", np.unique(alpha))

# Let's find the bounding box where alpha == 255 (completely opaque)
opaque_indices = np.where(alpha == 255)
if len(opaque_indices[0]) > 0:
    ymin, ymax = np.min(opaque_indices[0]), np.max(opaque_indices[0])
    xmin, xmax = np.min(opaque_indices[1]), np.max(opaque_indices[1])
    print(f"Opaque content box (alpha == 255): x={xmin} to {xmax}, y={ymin} to {ymax}")
    
    # Check the colors at the four corners of this opaque box
    print("Opaque corners colors:")
    print(f"Top-Left ({xmin}, {ymin}):", data[ymin, xmin, :])
    print(f"Top-Right ({xmax}, {ymin}):", data[ymin, xmax, :])
    print(f"Bottom-Left ({xmin}, {ymax}):", data[ymax, xmin, :])
    print(f"Bottom-Right ({xmax}, {ymax}):", data[ymax, xmax, :])
    
    # Check a few rows down from ymin
    print("Opaque colors at xmin + 10 for first few rows:")
    for y in range(ymin, ymin + 15):
        print(f"y={y}:", data[y, xmin + 10, :])
else:
    print("No opaque pixels found!")
