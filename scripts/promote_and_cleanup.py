import os
import shutil
import re

ROOT_DIR = r"D:\OneDrive\Software\Antigravity\Diseño Instruccional"
SCRIPTS_DIR = os.path.join(ROOT_DIR, "scripts")
SCRATCH_DIR = os.path.join(ROOT_DIR, "scratch")

os.makedirs(SCRIPTS_DIR, exist_ok=True)
os.makedirs(SCRATCH_DIR, exist_ok=True)

# 1. Promote mecanica_temporal.html -> mecanica.html
mecanica_temp = os.path.join(ROOT_DIR, "mecanica_temporal.html")
mecanica_target = os.path.join(ROOT_DIR, "mecanica.html")

if os.path.exists(mecanica_temp):
    with open(mecanica_temp, "r", encoding="utf-8") as f:
        content = f.read()
    # Normalize links
    content = content.replace("automotriz_temporal.html", "automotriz.html")
    content = content.replace("mecanica_temporal.html", "mecanica.html")
    with open(mecanica_target, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[OK] Promoted {mecanica_temp} -> {mecanica_target}")
    os.remove(mecanica_temp)
    print(f"[OK] Removed temporary {mecanica_temp}")

# 2. Promote automotriz_temporal.html -> automotriz.html
automotriz_temp = os.path.join(ROOT_DIR, "automotriz_temporal.html")
automotriz_target = os.path.join(ROOT_DIR, "automotriz.html")

if os.path.exists(automotriz_temp):
    with open(automotriz_temp, "r", encoding="utf-8") as f:
        content = f.read()
    # Normalize links
    content = content.replace("mecanica_temporal.html", "mecanica.html")
    content = content.replace("automotriz_temporal.html", "automotriz.html")
    with open(automotriz_target, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[OK] Promoted {automotriz_temp} -> {automotriz_target}")
    os.remove(automotriz_temp)
    print(f"[OK] Removed temporary {automotriz_temp}")

# 3. Move root python scripts to scripts/
root_files = os.listdir(ROOT_DIR)
for fname in root_files:
    fpath = os.path.join(ROOT_DIR, fname)
    if os.path.isfile(fpath) and fname.endswith(".py"):
        dest = os.path.join(SCRIPTS_DIR, fname)
        shutil.move(fpath, dest)
        print(f"[OK] Moved script {fname} -> scripts/{fname}")

# 4. Move temporary operational JSONs to scratch/
temp_jsons = ["batch_slides.json", "cleanup_ops.json", "del_p_ops.json", "visual_ops.json"]
for jname in temp_jsons:
    jpath = os.path.join(ROOT_DIR, jname)
    if os.path.exists(jpath):
        dest = os.path.join(SCRATCH_DIR, jname)
        shutil.move(jpath, dest)
        print(f"[OK] Moved temp json {jname} -> scratch/{jname}")

print("\n[ÉXITO] Promoción y limpieza local completadas.")
