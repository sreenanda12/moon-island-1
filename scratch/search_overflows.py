import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# find all selector { ... } blocks that contain "overflow" or "touch-action"
pattern = r'([^\r\n\{]+)\{[^\}]*(overflow|touch-action|scroll-lock|pointer-events|fixed)[^\}]*\}'
matches = re.finditer(pattern, css, re.IGNORECASE)

for i, m in enumerate(matches):
    print(f"Match {i+1}:\n{m.group(0).strip()}\n")
