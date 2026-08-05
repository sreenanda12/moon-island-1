# Search style.css for welcome-about-section styles
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
matches = re.finditer(r'\.welcome-about-section', css)
for m in matches:
    pos = m.start()
    print(f"Occurrence at pos {pos}:")
    print(css[pos:pos+400])
    print("-" * 50)
