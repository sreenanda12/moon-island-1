from PIL import Image

img = Image.open(r"c:\Users\sreenanda\Desktop\moon islands\moon_island_logoh.png-removebg-preview.png")
width, height = img.size
alpha = img.split()[-1]

# Find non-zero regions
ranges = []
in_range = False
start = None

for x in range(width):
    has_pixels = any(alpha.getpixel((x, y)) > 0 for y in range(height))
    if has_pixels and not in_range:
        start = x
        in_range = True
    elif not has_pixels and in_range:
        ranges.append((start, x - 1))
        in_range = False
if in_range:
    ranges.append((start, width - 1))

print("Non-zero regions in x-coordinate:", ranges)

# Let's save the non-zero sub-images to see what they are!
for i, (x1, x2) in enumerate(ranges):
    # Find y boundaries for this region
    y_pixels = [y for y in range(height) for x in range(x1, x2 + 1) if alpha.getpixel((x, y)) > 0]
    y1, y2 = min(y_pixels), max(y_pixels)
    # Crop with a tiny margin
    cropped = img.crop((x1, y1, x2 + 1, y2 + 1))
    cropped.save(f"c:\\Users\\sreenanda\\Desktop\\moon islands\\scratch\\region_{i}.png")
    print(f"Region {i} (x: {x1}-{x2}, y: {y1}-{y2}) saved to scratch/region_{i}.png")
