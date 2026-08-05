import subprocess

# Run git diff index.html
proc = subprocess.run(['git', 'diff', 'index.html'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
diff_text = proc.stdout.decode('utf-8', errors='ignore')

print("Diff length:", len(diff_text))
print(diff_text)
