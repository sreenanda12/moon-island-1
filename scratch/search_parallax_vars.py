# Search script.js for targetScale and currentScale
with open('script.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
for term in ['targetScale', 'currentScale', 'targetX', 'targetY']:
    matches = list(re.finditer(re.escape(term), text))
    print(f"Term '{term}' matches found: {len(matches)}")
    for m in matches:
        pos = m.start()
        print(f"  Line snippet: {text[pos-40:pos+80]}")
