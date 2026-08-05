from PIL import Image
import numpy as np

img = Image.open('p4.png')
print("Image size:", img.size)
print("Image mode:", img.mode)

if img.mode == 'RGBA':
    data = np.array(img)
    alpha = data[:, :, 3]
    # Find bounding box of non-transparent area
    non_transparent = np.where(alpha > 0)
    if len(non_transparent[0]) > 0:
        ymin, ymax = np.min(non_transparent[0]), np.max(non_transparent[0])
        xmin, xmax = np.min(non_transparent[1]), np.max(non_transparent[1])
        print(f"Non-transparent bounding box: x={xmin} to {xmax}, y={ymin} to {ymax}")
        print(f"Borders of transparency: Left={xmin}, Right={img.size[0]-1-xmax}, Top={ymin}, Bottom={img.size[1]-1-ymax}")
        
        # Check if there is any transparency inside the image
        total_transparent_pixels = np.sum(alpha == 0)
        print("Total transparent pixels:", total_transparent_pixels)
    else:
        print("Image is completely transparent!")
else:
    print("No alpha channel present in the image.")
