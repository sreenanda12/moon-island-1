# Search style.css for display: none rules and see what they apply to
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
matches = re.finditer(r'display\s*:\s*none', css, re.IGNORECASE)
for m in matches:
    pos = m.start()
    # Print the selector before the display: none
    # Let's find the preceding 100 characters to see the selector
    print(f"Match at pos {pos}:")
    print(css[pos-120:pos+50])
    print("-" * 50)
