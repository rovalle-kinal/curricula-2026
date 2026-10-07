"""
Script para desplegar la optimización móvil en producción:
1. Reemplaza los archivos en Cursos/Web/ y curricula-2026 (root, Revision_Temarios, TSU)
2. Adapta enlaces relativos para cada ubicación de producción
3. Elimina la carpeta 'optimización movil'
4. Hace commit y push en curricula-2026
5. Publica en el repositorio rovalle-kinal/new-courses
"""

import os
import shutil
import subprocess
import re

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GIT_EXE = r"C:\Users\arqov\AppData\Local\Programs\Git\cmd\git.exe"
OPT_DIR = os.path.join(WORKSPACE_DIR, "optimización movil")
NEW_COURSES_SRC = os.path.join(OPT_DIR, "new-courses")
CURRICULA_SRC = os.path.join(OPT_DIR, "curricula-2026")
CURSOS_WEB_DST = os.path.join(WORKSPACE_DIR, "Cursos", "Web")

print("=== PASO 1: MIGRANDO NUEVOS CURSOS A Cursos/Web/ ===")
for fname in os.listdir(NEW_COURSES_SRC):
    if fname.endswith(".html"):
        src = os.path.join(NEW_COURSES_SRC, fname)
        dst = os.path.join(CURSOS_WEB_DST, fname)
        with open(src, "r", encoding="utf-8") as f:
            content = f.read()

        # Ajustar enlaces para la ubicación Cursos/Web/
        content = content.replace('../curricula-2026/index.html', '../../index.html')
        content = content.replace('../curricula-2026/TSU/index.html', '../../TSU/index.html')
        content = content.replace('../curricula-2026/Revision_Temarios/index.html', '../../Revision_Temarios/index.html')

        with open(dst, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"  -> Reemplazado en producción: Cursos/Web/{fname}")

print("\n=== PASO 2: MIGRANDO CURRICULA-2026 A SUS CARPETAS DEFINITIVAS ===")
# Root index.html
with open(os.path.join(CURRICULA_SRC, "index.html"), "r", encoding="utf-8") as f:
    root_content = f.read()
root_content = root_content.replace('../new-courses/index.html', 'Cursos/Web/index.html')
with open(os.path.join(WORKSPACE_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(root_content)
print("  -> Reemplazado en producción: index.html (Portal Maestro)")

# Revision_Temarios
rev_src = os.path.join(CURRICULA_SRC, "Revision_Temarios")
rev_dst = os.path.join(WORKSPACE_DIR, "Revision_Temarios")
for fname in os.listdir(rev_src):
    if fname.endswith(".html"):
        with open(os.path.join(rev_src, fname), "r", encoding="utf-8") as f:
            c = f.read()
        c = c.replace('../../new-courses/index.html', '../Cursos/Web/index.html')
        with open(os.path.join(rev_dst, fname), "w", encoding="utf-8") as f:
            f.write(c)
        print(f"  -> Reemplazado en producción: Revision_Temarios/{fname}")

# TSU
tsu_src = os.path.join(CURRICULA_SRC, "TSU")
tsu_dst = os.path.join(WORKSPACE_DIR, "TSU")
for fname in os.listdir(tsu_src):
    if fname.endswith(".html"):
        with open(os.path.join(tsu_src, fname), "r", encoding="utf-8") as f:
            c = f.read()
        c = c.replace('../../new-courses/index.html', '../Cursos/Web/index.html')
        with open(os.path.join(tsu_dst, fname), "w", encoding="utf-8") as f:
            f.write(c)
        print(f"  -> Reemplazado en producción: TSU/{fname}")

print("\n=== PASO 3: ELIMINANDO CARPETA optimización movil ===")
if os.path.exists(OPT_DIR):
    shutil.rmtree(OPT_DIR)
    print("  -> Carpeta 'optimización movil' eliminada exitosamente.")
else:
    print("  -> Carpeta 'optimización movil' ya no existe.")

print("\n=== PASO 4: ACTUALIZANDO REPOSITORIO rovalle-kinal/curricula-2026 ===")
subprocess.run([GIT_EXE, "add", "-A"], cwd=WORKSPACE_DIR, check=True)
commit_msg = "feat(responsive): optimización móvil integral para Portal Maestro, TSU, Especialidades y Nuevos Cursos"
subprocess.run([GIT_EXE, "commit", "-m", commit_msg], cwd=WORKSPACE_DIR)
subprocess.run([GIT_EXE, "push", "origin", "main"], cwd=WORKSPACE_DIR, check=True)
print("  -> curricula-2026 actualizado y publicado en GitHub Pages.")

print("\n=== PASO 5: PUBLICANDO EN REPOSITORIO rovalle-kinal/new-courses ===")
pub_script = os.path.join(WORKSPACE_DIR, "scripts", "publish_to_new_courses.py")
subprocess.run(["python", pub_script], cwd=WORKSPACE_DIR, check=True)
print("  -> new-courses actualizado y publicado en GitHub Pages.")

print("\n=== TODO COMPLETADO CON ÉXITO ===")
