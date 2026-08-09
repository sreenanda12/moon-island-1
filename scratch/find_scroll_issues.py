import re

with open('style.css', 'r', encoding='utf-8') as f:
    style_css = f.read()

with open('script.js', 'r', encoding='utf-8') as f:
    script_js = f.read()

print("=== SEARCH IN STYLE.CSS ===")
for match in re.finditer(r'(overflow|touch-action|scroll-lock|pointer-events|fixed|100vh|100dvh)', style_css, re.IGNORECASE):
    start = max(0, match.start() - 50)
    end = min(len(style_css), match.end() + 100)
    print(f"Match '{match.group(0)}':\n{style_css[start:end]}\n" + "-"*40)

print("\n=== SEARCH IN SCRIPT.JS ===")
for match in re.finditer(r'(prevent|scroll|wheel|touch|overflow|pointer)', script_js, re.IGNORECASE):
    start = max(0, match.start() - 50)
    end = min(len(script_js), match.end() + 100)
    print(f"Match '{match.group(0)}':\n{script_js[start:end]}\n" + "-"*40)
