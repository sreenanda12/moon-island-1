from PIL import Image
import os

img_path = r"c:\Users\sreenanda\Desktop\moon islands\moon_island_logoh.png-removebg-preview.png"
if not os.path.exists(img_path):
    print("Error: Image not found at", img_path)
    exit(1)

img = Image.open(img_path)
print("Image size:", img.size)
print("Image mode:", img.mode)

# Let's inspect the alpha channel to see where the icon is and where the text starts.
# We can print the horizontal projection of alpha values.
width, height = img.size
alpha = img.split()[-1] if img.mode == 'RGBA' else None

if alpha:
    col_alpha_sums = [sum(alpha.getpixel((x, y)) for y in range(height)) for x in range(width)]
    # print columns that have content
    non_zero_cols = [x for x in range(width) if col_alpha_sums[x] > 0]
    if non_zero_cols:
        print("Non-zero alpha column range:", non_zero_cols[0], "to", non_zero_cols[-1])
        # Find the gap (where columns have zero or very low alpha sums between the icon and the text)
        # Let's print the first 100 column sums
        for x in range(min(150, width)):
            print(f"Col {x:03d}: {col_alpha_sums[x]}")
else:
    print("No alpha channel found.")
