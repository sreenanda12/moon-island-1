# Let's find and print all occurrences of desktop-moon-bg in style.css
import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Let's search for all matches of .desktop-moon-bg and print around them
for match in re.finditer(r'\.desktop-moon-bg', css):
    pos = match.start()
    print(f"Occurrence at pos {pos}:")
    print(css[pos:pos+300])
    print("-" * 50)
