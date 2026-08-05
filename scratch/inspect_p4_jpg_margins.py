from PIL import Image
import numpy as np

img = Image.open('p4_backup.JPG')
w, h = img.size
data = np.array(img)

# Print average color of margins (e.g., top-left corner, x=10, y=10)
print("Top-left margin color (x=10, y=10):", data[10, 10, :])
print("Left margin color (x=40, y=300):", data[300, 40, :])
print("Right margin color (x=980, y=300):", data[300, 980, :])
print("Top margin color (x=500, y=5):", data[5, 500, :])
print("Bottom margin color (x=500, y=675):", data[675, 500, :])
