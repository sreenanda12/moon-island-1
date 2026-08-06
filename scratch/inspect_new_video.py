import cv2
import os

video_path = r"c:\Users\sreenanda\Desktop\moon islands\hero section vedio.mp4"
if not os.path.exists(video_path):
    print("Video file not found at path:", video_path)
    exit(1)

cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print("Error: Could not open video file.")
    exit(1)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
duration = frame_count / fps if fps > 0 else 0

print(f"Video Path: {video_path}")
print(f"File Size: {os.path.getsize(video_path) / (1024*1024):.2f} MB")
print(f"Resolution: {width}x{height}")
print(f"FPS: {fps}")
print(f"Frame Count: {frame_count}")
print(f"Duration: {duration:.2f} seconds")

cap.release()
