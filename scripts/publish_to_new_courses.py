"""
Script para publicar el Ecosistema Completo de 4 Nuevos Cursos en el repositorio de GitHub:
rovalle-kinal/new-courses
y activar / actualizar GitHub Pages para su visualización pública en la web.
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

# Token retrieval (environment variable)
TOKEN = os.environ.get("GITHUB_TOKEN", os.environ.get("GH_TOKEN", ""))
REPO_URL = f"https://rovalle-kinal:{TOKEN}@github.com/rovalle-kinal/new-courses.git" if TOKEN else "https://github.com/rovalle-kinal/new-courses.git"
CLONE_DIR = os.path.join(os.environ.get("TEMP", "C:/Temp"), "new-courses-repo")

print("1. Limpiando y preparando directorio de clonación...")
if os.path.exists(CLONE_DIR):
    subprocess.run(f'cmd /c if exist "{CLONE_DIR}" rd /s /q "{CLONE_DIR}"', shell=True)

print("2. Clonando repositorio de GitHub...")
subprocess.run([GIT_EXE, "clone", REPO_URL, CLONE_DIR], check=True)

# Configurar identidad de git en el clon
subprocess.run([GIT_EXE, "config", "user.name", "rovalle-kinal"], cwd=CLONE_DIR, check=True)
subprocess.run([GIT_EXE, "config", "user.email", "rovalle@kinal.edu.gt"], cwd=CLONE_DIR, check=True)

print("3. Copiando y adaptando documentos Word de los 4 cursos...")
course_folders = ["Mecatrónica", "Ciberseguridad", "Automatización", "Cableado_Estructurado"]
for cfolder in course_folders:
    src_folder = os.path.join(CURSOS_DIR, cfolder)
    dst_folder = os.path.join(CLONE_DIR, cfolder)
    os.makedirs(dst_folder, exist_ok=True)
    if os.path.exists(src_folder):
        for f in os.listdir(src_folder):
            if f.endswith(".docx"):
                shutil.copy2(os.path.join(src_folder, f), os.path.join(dst_folder, f))

print("4. Adaptando y copiando páginas HTML para la raíz del repositorio...")
html_files = ["index.html", "mecatronica.html", "ciberseguridad.html", "automatizacion.html", "cableado_estructurado.html"]

for hfile in html_files:
    src_path = os.path.join(WEB_DIR, hfile)
    with open(src_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Adaptar enlaces al Portal Maestro y TSU / Revisión
    content = content.replace('../../index.html', 'https://rovalle-kinal.github.io/curricula-2026/')
    content = content.replace('../../TSU/index.html', 'https://rovalle-kinal.github.io/curricula-2026/TSU/index.html')
    content = content.replace('../../Revision_Temarios/index.html', 'https://rovalle-kinal.github.io/curricula-2026/Revision_Temarios/index.html')
    
    # Enlaces relativos a Word desde la raíz del repo
    content = content.replace('../Mecatrónica/', 'Mecatrónica/')
    content = content.replace('../Ciberseguridad/', 'Ciberseguridad/')
    content = content.replace('../Automatización/', 'Automatización/')
    content = content.replace('../Cableado_Estructurado/', 'Cableado_Estructurado/')

    dst_path = os.path.join(CLONE_DIR, hfile)
    with open(dst_path, "w", encoding="utf-8") as f:
        f.write(content)

# Crear .nojekyll
with open(os.path.join(CLONE_DIR, ".nojekyll"), "w", encoding="utf-8") as f:
    f.write("")

# Crear README.md para GitHub
readme_content = """# 🚀 Ecosistema de Nuevos Cursos en Desarrollo — Fundación Kinal 2026

Repositorio oficial y portal interactivo para los nuevos programas formativos diseñados para la formación continua, especialización industrial y reconversión técnica laboral bajo los estándares del **Marco Alemán de Cualificaciones (DQR Nivel 4 - 5)** y el **Sistema Dual de Formación en Alternancia**.

🔗 **Sitio Web Público (GitHub Pages):** [https://rovalle-kinal.github.io/new-courses/](https://rovalle-kinal.github.io/new-courses/)

---

## 📚 Portafolio de Cursos Disponibles

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

### 3. ⚡ Automatización y Control Eléctrico Industrial con PLC y Variadores de Frecuencia (VFD)
* **Modalidad:** Híbrida Asimétrica (80% Práctica en Bancos Reales / 20% Plataforma Virtual LMS)
* **Duración:** 120 horas formativas (20 sesiones de 6 horas • 110h de actividad neta de laboratorio)
* **Nivel:** Equivalencia DQR Nivel 4 - 5
* **Ejes:** Seguridad eléctrica NFPA 70E / LOTO, control electromagnético con contactores AC-3, variadores de frecuencia comerciales, programación Ladder en TIA Portal (Siemens S7-1200), red PROFINET, pantallas HMI y diagnóstico sistemático de averías.
* **Proyecto Terminal:** Puesta en Marcha Autónoma de Celda de Embotellado Continuo y Resolución de Averías Inducidas.
* **Explorar Web:** [automatizacion.html](https://rovalle-kinal.github.io/new-courses/automatizacion.html)
* **Documentos Word Oficiales:**
  * [Propuesta Formativa Institucional](Automatización/Propuesta_Curso_Automatizacion_Kinal.docx)
  * [Temario Modular Completo](Automatización/Temario_Curso_Automatizacion_Kinal.docx)
  * [Dosificación y Secuencia Didáctica Sesión a Sesión](Automatización/Dosificacion_y_Secuencia_Didactica_Automatizacion_Kinal.docx)

### 4. 🌐 Cableado Estructurado y Redes de Cobre y Fibra Óptica
* **Modalidad:** Presencial en Laboratorios de Redes de Kinal con apoyo digital en Google Classroom (80% Taller / 20% Plataforma)
* **Duración:** 80 horas pedagógicas (20 sesiones de 4 horas • 10 semanas • Martes y Jueves)
* **Nivel:** Equivalencia DQR Nivel 4 - 5
* **Ejes:** Estándares ANSI/TIA (568, 569, 606, 607), diseño de cuartos de telecomunicaciones TR/ER, curvado de tubería EMT, charolas portacables, montaje y anclaje de racks de 19'' (42U), remate Cat 6A, empalme de fibra óptica por fusión (< 0.05 dB), certificación instrumental Tier 1 con Fluke Networks y elaboración de planos As-Built.
* **Proyecto Terminal:** Certificación Integral de Rack Departamental, Rotulado TIA-606 y Dossier As-Built.
* **Explorar Web:** [cableado_estructurado.html](https://rovalle-kinal.github.io/new-courses/cableado_estructurado.html)
* **Documentos Word Oficiales:**
  * [Propuesta Formativa Institucional](Cableado_Estructurado/Propuesta_Curso_Cableado_Estructurado_Kinal.docx)
  * [Temario Modular Completo](Cableado_Estructurado/Temario_Curso_Cableado_Estructurado_Kinal.docx)
  * [Dosificación y Secuencia Didáctica Sesión a Sesión](Cableado_Estructurado/Dosificacion_y_Secuencia_Didactica_Cableado_Estructurado_Kinal.docx)

---

## 🏛️ Ideario Institucional de Fundación Kinal

> *«Formar a jóvenes y adultos a través de una educación integral, con énfasis en las áreas técnicas y tecnológicas, influyendo positivamente en su trabajo, su familia y la sociedad».*

* **Valores:** Visión cristiana de la vida. Respeto a la dignidad de la persona. Espíritu de servicio. Trabajo bien hecho. Libertad personal responsable.
* **Nota Mínima Aprobatoria:** **75 puntos sobre 100** en todas las comprobaciones técnicas y prácticas.

---

## 🌐 Enlace al Portal Maestro Curricular
* Portal Curricular General Kinal 2026: [https://rovalle-kinal.github.io/curricula-2026/](https://rovalle-kinal.github.io/curricula-2026/)
"""

with open(os.path.join(CLONE_DIR, "README.md"), "w", encoding="utf-8") as f:
    f.write(readme_content)

print("5. Realizando commit y push a la rama main de new-courses...")
subprocess.run([GIT_EXE, "add", "."], cwd=CLONE_DIR, check=True)
subprocess.run([GIT_EXE, "commit", "-m", "feat(courses): agregar páginas web interactivas y documentos de Automatización y Cableado Estructurado"], cwd=CLONE_DIR, check=True)
subprocess.run([GIT_EXE, "push", "origin", "main"], cwd=CLONE_DIR, check=True)

print("\n¡Publicación completada exitosamente!")
print("Repositorio: https://github.com/rovalle-kinal/new-courses")
print("Portal en vivo: https://rovalle-kinal.github.io/new-courses/")
print("  - Mecatrónica: https://rovalle-kinal.github.io/new-courses/mecatronica.html")
print("  - Ciberseguridad: https://rovalle-kinal.github.io/new-courses/ciberseguridad.html")
print("  - Automatización: https://rovalle-kinal.github.io/new-courses/automatizacion.html")
print("  - Cableado Estructurado: https://rovalle-kinal.github.io/new-courses/cableado_estructurado.html")
