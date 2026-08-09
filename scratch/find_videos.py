with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
matches = list(re.finditer(r'<video[^>]*>', html, re.IGNORECASE))
print(f"Found {len(matches)} video elements in index.html:")
for m in matches:
    print(m.group(0))
