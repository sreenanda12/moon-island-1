import shutil
from PIL import Image

# Backup
shutil.copyfile('p4.JPG', 'p4_backup.JPG')
print("Backed up p4.JPG to p4_backup.JPG")

# Crop
img = Image.open('p4_backup.JPG')
# Crop box is (left, upper, right, lower)
cropped_img = img.crop((93, 12, 910, 666))
cropped_img.save('p4.JPG')
print(f"Cropped p4.JPG saved successfully with size {cropped_img.size}")
