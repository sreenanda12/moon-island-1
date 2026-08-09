with open('style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if '.hero-premium' in line or '.hero-video-overlay' in line or '.hero-left' in line or '.hero-content-premium' in line:
        print(f"Line {i+1}: {line.strip()[:150]}")
