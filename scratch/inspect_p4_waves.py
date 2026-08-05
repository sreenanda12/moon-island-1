from PIL import Image
import numpy as np

img = Image.open('p4.png')
w, h = img.size
alpha = np.array(img)[:, :, 3]

# For each row, find the left-most and right-most non-transparent pixel
left_insets = []
right_insets = []
for y in range(h):
    row = alpha[y, :]
    non_zero = np.where(row > 0)[0]
    if len(non_zero) > 0:
        left_insets.append(non_zero[0])
        right_insets.append(w - 1 - non_zero[-1])

# For each col, find the top-most and bottom-most non-transparent pixel
top_insets = []
bottom_insets = []
for x in range(w):
    col = alpha[:, x]
    non_zero = np.where(col > 0)[0]
    if len(non_zero) > 0:
        top_insets.append(non_zero[0])
        bottom_insets.append(h - 1 - non_zero[-1])

print(f"Max Left transparency inset: {np.max(left_insets)} px ({np.max(left_insets)/w*100:.2f}%)")
print(f"Max Right transparency inset: {np.max(right_insets)} px ({np.max(right_insets)/w*100:.2f}%)")
print(f"Max Top transparency inset: {np.max(top_insets)} px ({np.max(top_insets)/h*100:.2f}%)")
print(f"Max Bottom transparency inset: {np.max(bottom_insets)} px ({np.max(bottom_insets)/h*100:.2f}%)")
