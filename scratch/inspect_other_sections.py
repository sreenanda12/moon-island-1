# Let's inspect sections in other html files
import re

for filename in ['about.html', 'services.html', 'contact.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()
    sections = re.findall(r'<section\s+[^>]*>', html)
    print(f"Sections in {filename}:")
    for sec in sections:
        print("  ", sec)
