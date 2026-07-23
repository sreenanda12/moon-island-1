import os
from PIL import Image
from PIL.ExifTags import TAGS

def get_exif(path):
    try:
        with Image.open(path) as img:
            exif_data = img._getexif()
            if not exif_data:
                return "No EXIF"
            
            exif = {}
            for tag, val in exif_data.items():
                decoded = TAGS.get(tag, tag)
                if decoded in ['DateTimeOriginal', 'DateTime', 'Model', 'ExposureTime', 'FNumber', 'ISOSpeedRatings']:
                    exif[decoded] = val
            return exif
    except Exception as e:
        return str(e)

def main():
    for f in ['p9.JPG', 'p13.JPG', 'p10.JPG', 'p11.JPG']:
        if os.path.exists(f):
            print(f"{f}: {get_exif(f)}")

if __name__ == '__main__':
    main()
