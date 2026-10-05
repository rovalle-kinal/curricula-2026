"""
Script para publicar el Ecosistema de Nuevos Cursos en el repositorio de GitHub:
rovalle-kinal/new-courses
y activar GitHub Pages para su visualización pública en la web.
"""

import os
import shutil
import subprocess
import urllib.request
import json

GIT_EXE = r"C:\Users\arqov\AppData\Local\Programs\Git\cmd\git.exe"
WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CURSOS_DIR = os.path.join(WORKSPACE_DIR, "Cursos")
WEB_DIR = os.path.join(CURSOS_DIR, "Web")

TOKEN = os.environ.get("GITHUB_TOKEN", os.environ.get("GH_TOKEN", ""))
REPO_URL = f"https://rovalle-kinal:{TOKEN}@github.com/rovalle-kinal/new-courses.git" if TOKEN else "https://github.com/rovalle-kinal/new-courses.git"
CLONE_DIR = os.path.join(os.environ.get("TEMP", "C:/Temp"), "new-courses-repo")

print("1. Limpiando y preparando directorio de clonación...")
if os.path.exists(CLONE_DIR):
    shutil.rmtree(CLONE_DIR, ignore_errors=True)

print("2. Clonando repositorio vacío de GitHub...")
subprocess.run([GIT_EXE, "clone", REPO_URL, CLONE_DIR], check=True)

# Configurar identidad de git en el clon
subprocess.run([GIT_EXE, "config", "user.name", "rovalle-kinal"], cwd=CLONE_DIR, check=True)
subprocess.run([GIT_EXE, "config", "user.email", "rovalle@kinal.edu.gt"], cwd=CLONE_DIR, check=True)

print("3. Copiando y adaptando archivos para la raíz del repositorio...")
# Copiar carpetas de Word
os.makedirs(os.path.join(CLONE_DIR, "Mecatrónica"), exist_ok=True)
for f in os.listdir(os.path.join(CURSOS_DIR, "Mecatrónica")):
    if f.endswith(".docx"):
        shutil.copy2(os.path.join(CURSOS_DIR, "Mecatrónica", f), os.path.join(CLONE_DIR, "Mecatrónica", f))

os.makedirs(os.path.join(CLONE_DIR, "Ciberseguridad"), exist_ok=True)
for f in os.listdir(os.path.join(CURSOS_DIR, "Ciberseguridad")):
    if f.endswith(".docx"):
        shutil.copy2(os.path.join(CURSOS_DIR, "Ciberseguridad", f), os.path.join(CLONE_DIR, "Ciberseguridad", f))

# Leer y adaptar index.html
with open(os.path.join(WEB_DIR, "index.html"), "r", encoding="utf-8") as f:
    idx_content = f.read()

# En index.html para new-courses, adaptar rutas a curricula-2026 para los enlaces externos
idx_content = idx_content.replace('../../index.html', 'https://rovalle-kinal.github.io/curricula-2026/')
idx_content = idx_content.replace('../../TSU/index.html', 'https://rovalle-kinal.github.io/curricula-2026/TSU/index.html')
idx_content = idx_content.replace('../../Revision_Temarios/index.html', 'https://rovalle-kinal.github.io/curricula-2026/Revision_Temarios/index.html')
# Enlaces a Word desde la raíz
idx_content = idx_content.replace('../Mecatrónica/', 'Mecatrónica/')
idx_content = idx_content.replace('../Ciberseguridad/', 'Ciberseguridad/')

with open(os.path.join(CLONE_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(idx_content)

# Leer y adaptar mecatronica.html
with open(os.path.join(WEB_DIR, "mecatronica.html"), "r", encoding="utf-8") as f:
    meca_content = f.read()

meca_content = meca_content.replace('../../index.html', 'https://rovalle-kinal.github.io/curricula-2026/')
meca_content = meca_content.replace('../Mecatrónica/', 'Mecatrónica/')
meca_content = meca_content.replace('../Ciberseguridad/', 'Ciberseguridad/')

with open(os.path.join(CLONE_DIR, "mecatronica.html"), "w", encoding="utf-8") as f:
    f.write(meca_content)

# Leer y adaptar ciberseguridad.html
with open(os.path.join(WEB_DIR, "ciberseguridad.html"), "r", encoding="utf-8") as f:
    ciber_content = f.read()

ciber_content = ciber_content.replace('../../index.html', 'https://rovalle-kinal.github.io/curricula-2026/')
ciber_content = ciber_content.replace('../Mecatrónica/', 'Mecatrónica/')
ciber_content = ciber_content.replace('../Ciberseguridad/', 'Ciberseguridad/')

with open(os.path.join(CLONE_DIR, "ciberseguridad.html"), "w", encoding="utf-8") as f:
    f.write(ciber_content)

# Crear .nojekyll
with open(os.path.join(CLONE_DIR, ".nojekyll"), "w", encoding="utf-8") as f:
    f.write("")

# Crear README.md para GitHub
readme_content = """# 🚀 Ecosistema de Nuevos Cursos en Desarrollo — Fundación Kinal 2026

Repositorio oficial y portal interactivo para los nuevos programas formativos diseñados para la formación continua, especialización industrial y reconversión técnica laboral bajo los estándares del **Marco Alemán de Cualificaciones (DQR Nivel 4 - 5)** y el **Sistema Dual de Formación en Alternancia**.

🔗 **Sitio Web Público (GitHub Pages):** [https://rovalle-kinal.github.io/new-courses/](https://rovalle-kinal.github.io/new-courses/)

---

## 📚 Cursos Disponibles

### 1. ⚙️ Mecatrónica Industrial y Fabricación Digital Aplicada
* **Modalidad:** 100% Presencial en Talleres de Fabricación Digital y Automatización Kinal
* **Duración:** 90 horas pedagógicas (20 sábados de 4.5 horas • 8:00 a 12:30 hrs • Febrero a Junio)
* **Nivel:** Equivalencia DQR Nivel 4 - 5
* **Ejes:** CAD paramétrico 3D, corte láser CO2, manufactura aditiva FDM, fresado CNC, sensórica PNP/NPN, electroneumática Festo y PLC Siemens S7-1200.
* **Proyecto Terminal:** Celda Mecatrónica Integrada + Bitácora de Taller (*Berichtsheft*).
* **Explorar Web:** [mecatronica.html](https://rovalle-kinal.github.io/new-courses/mecatronica.html)
* **Documentos Word Oficiales:**
  * [Propuesta Formativa Institucional](Mecatrónica/Propuesta_Curso_Mecatronica_Kinal.docx)
  * [Temario Modular Completo](Mecatrónica/Temario_Curso_Mecatronica_Kinal.docx)
  * [Dosificación y Secuencia Didáctica Sesión a Sesión](Mecatrónica/Dosificacion_y_Secuencia_Didactica_Mecatronica_Kinal.docx)

### 2. 🛡️ Ciberseguridad y Fundamentos de Seguridad de la Información
* **Modalidad:** Híbrida (80% Virtual Síncrona / 20% Presencial en Sede Kinal)
* **Duración:** 80 horas pedagógicas (20 sesiones de 4 horas • 10 semanas)
* **Nivel:** Equivalencia DQR Nivel 4 - 5
* **Ejes:** Tríada CIA, soporte ITIL, identidad y acceso (IAM/MFA/RBAC), criptografía y PKI/TLS, monitoreo en SOC/SIEM, gestión de vulnerabilidades CVE/CVSS y normativas (ISO 27001, SOC 2, HIPAA, PCI-DSS).
* **Proyecto Terminal:** Expediente de Seguridad del Caso Práctico Transversal de Empresa Ficticia.
* **Explorar Web:** [ciberseguridad.html](https://rovalle-kinal.github.io/new-courses/ciberseguridad.html)
* **Documentos Word Oficiales:**
  * [Propuesta Formativa Institucional](Ciberseguridad/Propuesta_Curso_Ciberseguridad_Kinal.docx)
  * [Temario Modular Completo](Ciberseguridad/Temario_Curso_Ciberseguridad_Kinal.docx)
  * [Dosificación y Secuencia Didáctica Sesión a Sesión](Ciberseguridad/Dosificacion_y_Secuencia_Didactica_Ciberseguridad.docx)

---

## 🏛️ Ideario Institucional de Fundación Kinal

> *«Formar a jóvenes y adultos a través de una educación integral, con énfasis en las áreas técnicas y tecnológicas, influyendo positivamente en su trabajo, su familia y la sociedad».*

* **Valores:** Visión cristiana de la vida. Respeto a la dignidad de la persona. Espíritu de servicio. Trabajo bien hecho. Libertad personal responsable.
* **Nota Mínima Aprobatoria:** **75 puntos sobre 100** en todas las evaluaciones técnicas y prácticas.

---

## 🌐 Enlace al Portal Maestro Curricular
* Portal Curricular General Kinal 2026: [https://rovalle-kinal.github.io/curricula-2026/](https://rovalle-kinal.github.io/curricula-2026/)
"""

with open(os.path.join(CLONE_DIR, "README.md"), "w", encoding="utf-8") as f:
    f.write(readme_content)

print("4. Realizando commit y push a la rama main de new-courses...")
subprocess.run([GIT_EXE, "add", "."], cwd=CLONE_DIR, check=True)
subprocess.run([GIT_EXE, "commit", "-m", "Publicación inicial: Ecosistema Web interactivo y documentos Word de Nuevos Cursos en Desarrollo"], cwd=CLONE_DIR, check=True)
subprocess.run([GIT_EXE, "branch", "-M", "main"], cwd=CLONE_DIR, check=True)
subprocess.run([GIT_EXE, "push", "-u", "origin", "main"], cwd=CLONE_DIR, check=True)

print("5. Activando / Verificando GitHub Pages en el repositorio...")
api_url = "https://api.github.com/repos/rovalle-kinal/new-courses/pages"
req = urllib.request.Request(
    api_url,
    data=json.dumps({"source": {"branch": "main", "path": "/"}}).encode("utf-8"),
    headers={
        "Authorization": f"token {TOKEN}",
        "Accept": "application/vnd.github.v3+json",
        "Content-Type": "application/json",
        "User-Agent": "Python"
    },
    method="POST"
)

try:
    with urllib.request.urlopen(req) as resp:
        res_data = json.loads(resp.read().decode())
        print("GitHub Pages activado exitosamente:", res_data.get("html_url"))
except urllib.error.HTTPError as e:
    err_body = e.read().decode()
    if "already" in err_body.lower():
        print("GitHub Pages ya se encuentra activado.")
    else:
        print(f"Nota en la API de GitHub Pages ({e.code}): {err_body}")

print("\n¡Publicación completada!")
print("Repositorio: https://github.com/rovalle-kinal/new-courses")
print("Sitio Web en vivo: https://rovalle-kinal.github.io/new-courses/")
