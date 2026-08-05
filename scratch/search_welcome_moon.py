# Search welcome-section-moon in style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
matches = re.finditer(r'\.welcome-section-moon', css)
for m in matches:
    pos = m.start()
    print(f"Occurrence of welcome-section-moon:")
    print(css[pos:pos+300])
    print("-" * 50)
