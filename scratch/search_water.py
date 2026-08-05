# Search style.css for water, reflect, wave, ripple, etc.
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
terms = ['water', 'reflect', 'wave', 'ripple', 'shimmer', 'sea', 'lake', 'backwater']
for term in terms:
    matches = list(re.finditer(re.escape(term), css, re.IGNORECASE))
    print(f"Term '{term}' matches found: {len(matches)}")
    for m in matches[:3]:  # print first 3 matches
        pos = m.start()
        print(f"  Pos {pos}: {css[pos-40:pos+100]}")
