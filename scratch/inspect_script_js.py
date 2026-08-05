# Search for terms in script.js
with open('script.js', 'r', encoding='utf-8') as f:
    text = f.read()

terms = ['updateScrollParallax', 'parallax', 'Scroll', 'hero-premium', 'desktop-moon-bg']
for term in terms:
    pos = text.find(term)
    if pos != -1:
        print(f"Term '{term}' found at character position {pos}")
        print(f"Snippet: {text[pos-50:pos+150]}\n")
    else:
        print(f"Term '{term}' NOT found")
