import cv2
import os

input_path = r"c:\Users\sreenanda\Desktop\moon islands\hero section vedio.mp4"
output_path_mp4v = r"c:\Users\sreenanda\Desktop\moon islands\scratch\test_mp4v.mp4"
output_path_avc1 = r"c:\Users\sreenanda\Desktop\moon islands\scratch\test_avc1.mp4"

cap = cv2.VideoCapture(input_path)
if not cap.isOpened():
    print("Could not open input video")
    exit(1)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)

print(f"Input: {width}x{height} at {fps} fps")

# Test mp4v
fourcc_mp4v = cv2.VideoWriter_fourcc(*'mp4v')
out_mp4v = cv2.VideoWriter(output_path_mp4v, fourcc_mp4v, fps, (width, height))
print("mp4v writer opened:", out_mp4v.isOpened())

# Test avc1
fourcc_avc1 = cv2.VideoWriter_fourcc(*'avc1')
out_avc1 = cv2.VideoWriter(output_path_avc1, fourcc_avc1, fps, (width, height))
print("avc1 writer opened:", out_avc1.isOpened())

# Write 50 frames
count = 0
while count < 50:
    ret, frame = cap.read()
    if not ret:
        break
    if out_mp4v.isOpened():
        out_mp4v.write(frame)
    if out_avc1.isOpened():
        out_avc1.write(frame)
    count += 1

cap.release()
if out_mp4v.isOpened():
    out_mp4v.release()
if out_avc1.isOpened():
    out_avc1.release()

print("Done. File sizes:")
if os.path.exists(output_path_mp4v):
    print(f"mp4v size: {os.path.getsize(output_path_mp4v) / 1024:.2f} KB")
if os.path.exists(output_path_avc1):
    print(f"avc1 size: {os.path.getsize(output_path_avc1) / 1024:.2f} KB")
