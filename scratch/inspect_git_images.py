import subprocess
from PIL import Image
import io

def get_git_image(path):
    proc = subprocess.run(['git', 'show', f'HEAD:{path}'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode == 0:
        return Image.open(io.BytesIO(proc.stdout))
    else:
        print(f"Error getting git file {path}: {proc.stderr.decode()}")
        return None

img_png = get_git_image('p4.png')
if img_png:
    print('Git p4.png size:', img_png.size)
    print('Git p4.png mode:', img_png.mode)
    
img_jpg = get_git_image('p4.JPG')
if img_jpg:
    print('Git p4.JPG size:', img_jpg.size)
    print('Git p4.JPG mode:', img_jpg.mode)
