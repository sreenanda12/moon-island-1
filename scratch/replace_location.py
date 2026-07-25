import os

files = ["index.html", "about.html", "services.html", "contact.html"]
workspace_dir = r"c:\Users\sreenanda\Desktop\moon islands"

for filename in files:
    path = os.path.join(workspace_dir, filename)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()
        
        # Replace Alappuzha with Pottotta
        new_content = content.replace("Alappuzha", "Pottotta")
        
        with open(path, "w", encoding="utf-8") as file:
            file.write(new_content)
        print(f"Updated {filename}")
    else:
        print(f"File not found: {filename}")
