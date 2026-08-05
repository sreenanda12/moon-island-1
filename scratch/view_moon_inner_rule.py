# Find and print the exact .desktop-moon-inner CSS rule in style.css
import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

match = re.search(r'\.desktop-moon-inner\s*\{[^}]*\}', css)
if match:
    print(match.group(0))
else:
    print(".desktop-moon-inner rule NOT found")
