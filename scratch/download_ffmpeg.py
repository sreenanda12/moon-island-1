import urllib.request
import zipfile
import os

url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
zip_path = r"c:\Users\sreenanda\Desktop\moon islands\scratch\ffmpeg.zip"
dest_dir = r"c:\Users\sreenanda\Desktop\moon islands\scratch"

print("Downloading FFmpeg from:", url)

def report_progress(block_num, block_size, total_size):
    read_so_far = block_num * block_size
    if total_size > 0:
        percent = (read_so_far / total_size) * 100
        print(f"Downloaded {read_so_far / (1024*1024):.2f} MB of {total_size / (1024*1024):.2f} MB ({percent:.1f}%)", end="\r")
    else:
        print(f"Downloaded {read_so_far / (1024*1024):.2f} MB", end="\r")

try:
    urllib.request.urlretrieve(url, zip_path, report_progress)
    print("\nDownload completed. Extracting ffmpeg.exe and ffprobe.exe...")
    
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for file_info in zip_ref.infolist():
            filename = os.path.basename(file_info.filename)
            if filename in ['ffmpeg.exe', 'ffprobe.exe']:
                # Extract file to dest_dir
                target_path = os.path.join(dest_dir, filename)
                with zip_ref.open(file_info) as source, open(target_path, 'wb') as target:
                    target.write(source.read())
                print(f"Extracted: {filename}")
                
    print("Extraction done. Cleaning up zip file...")
    os.remove(zip_path)
    print("Cleanup completed.")
except Exception as e:
    print(f"\nError occurred: {e}")
    if os.path.exists(zip_path):
        os.remove(zip_path)
