# Check background properties of other sections in style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
sections = [
    'experiences-section',
    'why-us-section',
    'editorial-culture-section',
    'packages-preview',
    'final-cta',
    'premium-cta'
]

for sec in sections:
    matches = list(re.finditer(rf'\.{sec}\s*\{{[^}}]*\}}', css))
    if matches:
        print(f"--- Matches for .{sec} ---")
        for m in matches:
            print(m.group(0))
        print()
    else:
        # fallback
        idx = css.find(f".{sec}")
        if idx != -1:
            print(f"--- Found .{sec} (fallback) ---")
            print(css[idx:idx+250])
            print()
