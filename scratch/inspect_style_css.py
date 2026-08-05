# Check the encoding and search for strings in style.css
with open('style.css', 'rb') as f:
    content_bytes = f.read()

print("File size in bytes:", len(content_bytes))
# Try to decode as utf-8 and utf-16
try:
    text = content_bytes.decode('utf-8')
    print("Decoded successfully as UTF-8")
except UnicodeDecodeError:
    try:
        text = content_bytes.decode('utf-16')
        print("Decoded successfully as UTF-16")
    except UnicodeDecodeError:
        text = content_bytes.decode('latin-1')
        print("Decoded as Latin-1 fallback")

# Search for some terms
terms = ['desktop-moon-bg', 'hero-premium', 'welcome-about-section', 'cinematic-bg-wrapper']
for term in terms:
    pos = text.find(term)
    if pos != -1:
        print(f"Term '{term}' found at character position {pos}")
        # Print a small snippet around the term
        start = max(0, pos - 50)
        end = min(len(text), pos + 150)
        print(f"Snippet: {text[start:end]}\n")
    else:
        print(f"Term '{term}' NOT found")
