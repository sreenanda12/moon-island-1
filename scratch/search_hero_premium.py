# Search for hero-premium in style.css to see if it is hidden or styled differently
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
matches = re.finditer(r'\.hero-premium', css)
for m in matches:
    pos = m.start()
    print(f"Occurrence at pos {pos}:")
    print(css[pos:pos+300])
    print("-" * 50)
