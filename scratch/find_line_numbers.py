# Find line numbers of .desktop-moon-inner and other selectors in style.css
with open('style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if '.desktop-moon-inner' in line:
        print(f"Line {i+1}: {line.strip()}")
    if '.desktop-moon-bg' in line:
        print(f"Line {i+1} (.desktop-moon-bg): {line.strip()}")
