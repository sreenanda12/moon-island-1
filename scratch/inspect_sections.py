# Let's inspect the sections in index.html
import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's search for <section ...> tags and print them
sections = re.findall(r'<section\s+[^>]*>', html)
print("Sections in index.html:")
for sec in sections:
    print("  ", sec)
