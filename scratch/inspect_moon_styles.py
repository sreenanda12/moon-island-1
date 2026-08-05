import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Let's extract any blocks of rules containing desktop-moon or mobile-moon
# We can search for selectors matching `.desktop-moon...` or `.mobile-moon...` and print their rules
matches = re.finditer(r'\.(desktop|mobile)-moon[a-zA-Z-]*\s*\{[^}]*\}', css)
for m in matches:
    print(m.group(0))
    print("-" * 30)

# Also let's extract animations related to them, e.g. @keyframes floatMoon, keyframes mobileMoonFloatSimple
keyframes = re.finditer(r'@keyframes\s+[a-zA-Z0-9_-]+\s*\{[^}]*\}', css)
for k in keyframes:
    name = k.group(0)
    if 'Moon' in name or 'moon' in name:
        print(name)
        print("-" * 30)
