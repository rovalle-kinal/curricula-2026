import os
import re
import glob

workspace = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
html_files = glob.glob(os.path.join(workspace, "*.html"))

# Regex to match any link rel icon
pattern = re.compile(r'<link\s+[^>]*rel=["\'](?:shortcut\s+)?icon["\'][^>]*>', re.IGNORECASE)
replacement = '<link rel="icon" type="image/png" href="assets/escudo_kinal_cuadrado.png">'

for f in html_files:
    fname = os.path.basename(f)
    with open(f, 'r', encoding='utf-8') as fl:
        content = fl.read()
    if pattern.search(content):
        new_content = pattern.sub(replacement, content)
        with open(f, 'w', encoding='utf-8') as out:
            out.write(new_content)
        print(f"Updated icon in {fname}")
    else:
        # If not present, insert before </head>
        if "</head>" in content:
            new_content = content.replace("</head>", f"    {replacement}\n</head>")
            with open(f, 'w', encoding='utf-8') as out:
                out.write(new_content)
            print(f"Inserted icon in {fname}")

print("Favicons updated successfully!")
