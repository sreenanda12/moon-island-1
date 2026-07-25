from PIL import Image
import os

img = Image.open(r"c:\Users\sreenanda\Desktop\moon islands\moon_island_logoh.png-removebg-preview.png")
width, height = img.size

# Region 0 is the circular icon
# Let's crop it with a small, balanced padding or exactly crop the circle.
# Looking at the coordinates: x: 185-426, y: 27-246.
# Let's crop x: 185 to 426, y: 27 to 246.
icon = img.crop((185, 27, 427, 247))

# Let's ensure the output directory exists
os.makedirs(r"c:\Users\sreenanda\Desktop\moon islands\assets", exist_ok=True)

# Save the cropped icon
icon.save(r"c:\Users\sreenanda\Desktop\moon islands\assets\logo-icon.png")
print("Saved logo-icon.png to assets/logo-icon.png")
print("Icon dimensions:", icon.size)
