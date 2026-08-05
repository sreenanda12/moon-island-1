import shutil
from PIL import Image

# Backup
shutil.copyfile('p4.png', 'p4_backup.png')
print("Backed up p4.png to p4_backup.png")

# Crop
img = Image.open('p4_backup.png')
# Bounding box of non-transparent area was found to be x=94 to 907, y=13 to 665
# crop box is (left, upper, right, lower)
cropped_img = img.crop((94, 13, 908, 666))
cropped_img.save('p4.png')
print("Cropped p4.png saved successfully.")
