import re

# Read style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

classes = [
    'cinematic-bg-wrapper',
    'sky-gradient',
    'desktop-moon-bg',
    'desktop-moon-inner',
    'mobile-moon-bg',
    'mobile-moon-inner',
    'stars-container',
    'clouds-container',
    'hero-premium',
    'hero-video-bg',
    'hero-bg-video',
    'hero-video-overlay',
    'welcome-about-section',
    'featured-image-frame',
    'welcome-heading',
    'welcome-description',
    'experience-icons-row',
    'btn-discover-story',
    'navbar'
]

# Find block of CSS rules for each class
for cls in classes:
    # Match something like .class_name { ... } including nested braces (optional, simple match first)
    # Since CSS can be complex, let's find the start of the selector and grab 400 chars
    pattern = rf'\.{cls}\s*\{{[^}}]*\}}'
    match = re.search(pattern, css)
    if match:
        print(f"--- MATCH FOR .{cls} ---")
        print(match.group(0))
        print()
    else:
        # Fallback: search for the selector name and print around it
        idx = css.find(f".{cls}")
        if idx != -1:
            print(f"--- FOUND .{cls} (fallback) ---")
            print(css[idx:idx+400])
            print()
        else:
            print(f"--- .{cls} NOT FOUND ---")
