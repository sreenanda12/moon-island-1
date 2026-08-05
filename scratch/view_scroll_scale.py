# Print updateScrollState context
with open('script.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
pos = text.find('updateScrollState = () => {')
if pos != -1:
    print(text[pos:pos+700])
