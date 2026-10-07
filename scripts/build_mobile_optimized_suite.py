"""
Script de Generación y Optimización Móvil Definitiva:
- Repositorio 1: new-courses (5 cursos técnicos + index)
- Repositorio 2: curricula-2026 (Portal Maestro + Revision_Temarios + TSU)

Corrige al 100% el ancho en dispositivos móviles (cero recortes de tarjetas ni pensums).
NO crea página de resumen.
Desktop PC (>= 768px / 1024px) se mantiene 100% fiel e idéntico.
"""

import os
import re

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_BASE = os.path.join(WORKSPACE_DIR, "optimización movil")
NEW_COURSES_OUT = os.path.join(OUTPUT_BASE, "new-courses")
CURRICULA_OUT = os.path.join(OUTPUT_BASE, "curricula-2026")

ROBUST_MOBILE_CSS = """
    <!-- ========================================================= -->
    <!-- KINAL MOBILE ENGINE - ZERO CLIPPING RESPONSIVE SYSTEM      -->
    <!-- ========================================================= -->
    <style id="kinal-mobile-responsive-system">
        @media (max-width: 767px) {
            /* 1. Box model y contención estricta en 100% viewport */
            *, *::before, *::after {
                box-sizing: border-box !important;
            }
            html, body {
                width: 100% !important;
                max-width: 100vw !important;
                overflow-x: hidden !important;
                margin: 0 !important;
                padding: 0 !important;
                -webkit-text-size-adjust: 100% !important;
                touch-action: pan-y pinch-zoom;
            }

            /* 2. Contenedores fluidos sin desbordes */
            main, section, header, footer, 
            .max-w-7xl, .max-w-6xl, .max-w-5xl, .max-w-4xl, .max-w-3xl, .max-w-2xl {
                width: 100% !important;
                max-width: 100% !important;
                min-width: 0 !important;
                box-sizing: border-box !important;
            }

            /* 3. Tarjetas de cursos (pensums) y contenedores modulares */
            .grid {
                width: 100% !important;
                min-width: 0 !important;
            }
            .card-hover, [class*="rounded-3xl"], [class*="rounded-2xl"], .area-course-card {
                width: 100% !important;
                max-width: 100% !important;
                min-width: 0 !important;
                padding-left: 1rem !important;
                padding-right: 1rem !important;
                box-sizing: border-box !important;
            }

            /* 4. Ruptura de palabras y textos para evitar que empujen el ancho */
            h1, h2, h3, h4, h5, p, span, a, div {
                overflow-wrap: break-word !important;
                word-break: break-word !important;
            }

            /* 5. Scroll horizontal fluido sin barras antiestéticas */
            .no-scrollbar::-webkit-scrollbar, 
            nav::-webkit-scrollbar,
            .overflow-x-auto::-webkit-scrollbar {
                display: none !important;
                width: 0 !important;
                height: 0 !important;
            }
            .no-scrollbar, 
            nav,
            .overflow-x-auto {
                -ms-overflow-style: none !important;
                scrollbar-width: none !important;
                -webkit-overflow-scrolling: touch !important;
            }

            /* 6. Ergonomía táctil: botones y controles con altura mínima */
            .tab-btn, button, select, input[type="text"] {
                min-height: 42px;
                touch-action: manipulation;
            }

            /* 7. Tab Bar y Navegación Horizontal Swipeable */
            nav.flex.overflow-x-auto, 
            .tab-nav-wrapper {
                display: flex !important;
                flex-wrap: nowrap !important;
                overflow-x: auto !important;
                padding-top: 4px !important;
                padding-bottom: 4px !important;
            }
            nav.flex.overflow-x-auto > * {
                flex-shrink: 0 !important;
            }

            /* 8. Padding de lectura responsivo en pantallas móviles */
            main {
                padding-left: 12px !important;
                padding-right: 12px !important;
                padding-top: 14px !important;
                padding-bottom: 24px !important;
            }
            header .max-w-7xl, header .max-w-6xl {
                padding-left: 12px !important;
                padding-right: 12px !important;
                padding-top: 8px !important;
                padding-bottom: 8px !important;
            }

            /* 9. Envoltura táctil y cue de desplazamiento para tablas y matrices */
            .table-responsive-mobile, 
            .curriculum-grid-container {
                width: 100% !important;
                max-width: 100% !important;
                overflow-x: auto !important;
                -webkit-overflow-scrolling: touch !important;
                border-radius: 12px !important;
            }

            /* 10. Feedback táctil ágil */
            .tab-btn:active, button:active, .card-hover:active, .area-course-card:active {
                transform: scale(0.97) !important;
                transition: transform 0.1s ease !important;
            }

            /* 11. Botones de descarga de Word apilables o compactos */
            .btn-doc-group {
                display: grid !important;
                grid-template-columns: repeat(3, minmax(0, 1fr)) !important;
                gap: 6px !important;
            }
            .btn-doc-item {
                display: flex !important;
                flex-direction: column !important;
                align-items: center !important;
                justify-content: center !important;
                padding: 6px 4px !important;
                font-size: 10px !important;
                gap: 2px !important;
                text-align: center !important;
            }
        }

        @media (max-width: 1023px) {
            .session-item {
                cursor: pointer;
                -webkit-tap-highlight-color: transparent;
                transition: all 0.2s ease;
            }
            [id$="-detail-card"] {
                scroll-margin-top: 80px;
            }
        }
    </style>
"""

MOBILE_JS_AUTO_SCROLL_HELPER = """
    <!-- Mobile Master-Detail Interaction Helper -->
    <script>
        (function() {
            window.kinalScrollToDetail = function(detailId) {
                if (window.innerWidth < 1024) {
                    const el = document.getElementById(detailId) || document.querySelector('[id$="-detail-card"]');
                    if (el) {
                        setTimeout(function() {
                            el.scrollIntoView({ behavior: 'smooth', block: 'start' });
                        }, 50);
                    }
                }
            };
        })();
    </script>
"""

def optimize_catalog_index(html_content):
    """
    Optimiza Cursos/Web/index.html para que ninguna tarjeta de pensum ni cabecera se corte en móvil.
    """
    content = html_content

    # Corregir enlaces cruzados
    content = content.replace('../../index.html', '../curricula-2026/index.html')
    content = content.replace('../../TSU/index.html', '../curricula-2026/TSU/index.html')
    content = content.replace('../../Revision_Temarios/index.html', '../curricula-2026/Revision_Temarios/index.html')

    # Optimizar Header institucional para que nunca empuje el ancho
    old_header_inner = '''            <div class="flex items-center gap-3">
                <a href="../curricula-2026/index.html" class="bg-gradient-to-r from-amber-500 to-amber-600 text-slate-950 font-black text-xs tracking-wider uppercase px-2.5 py-1 rounded shadow-sm hover:opacity-90 transition flex items-center gap-1">
                    <i data-lucide="arrow-left" class="w-3.5 h-3.5"></i> Portal Maestro
                </a>
                <span class="text-slate-600">|</span>
                <div class="text-slate-200 font-bold text-xs sm:text-sm flex items-center gap-2">
                    <i data-lucide="folder-kanban" class="w-4 h-4 text-blue-400"></i>
                    Formación Continua & Empleabilidad • Portafolio de 5 Cursos
                </div>
            </div>'''
    new_header_inner = '''            <div class="flex items-center gap-2 sm:gap-3 flex-wrap min-w-0">
                <a href="../curricula-2026/index.html" class="bg-gradient-to-r from-amber-500 to-amber-600 text-slate-950 font-black text-xs tracking-wider uppercase px-2 py-1 sm:px-2.5 rounded shadow-sm hover:opacity-90 transition flex items-center gap-1 shrink-0">
                    <i data-lucide="arrow-left" class="w-3.5 h-3.5"></i> Portal Maestro
                </a>
                <span class="text-slate-600 hidden sm:inline">|</span>
                <div class="text-slate-200 font-bold text-xs sm:text-sm flex items-center gap-1.5 min-w-0">
                    <i data-lucide="folder-kanban" class="w-4 h-4 text-blue-400 shrink-0"></i>
                    <span class="sm:hidden truncate">5 Nuevos Cursos</span>
                    <span class="hidden sm:inline">Formación Continua & Empleabilidad • Portafolio de 5 Cursos</span>
                </div>
            </div>'''
    content = content.replace(old_header_inner, new_header_inner)

    # Reemplazar p-7 por p-4 sm:p-7 min-w-0 w-full en las tarjetas
    content = content.replace('p-7 shadow-sm card-hover', 'p-4 sm:p-7 min-w-0 w-full shadow-sm card-hover')
    content = content.replace('p-7 shadow-md card-hover', 'p-4 sm:p-7 min-w-0 w-full shadow-md card-hover')

    # Optimizar títulos de tarjetas para que nunca empujen ancho
    content = content.replace('text-2xl font-black text-slate-900 hover:text-', 'text-xl sm:text-2xl font-black text-slate-900 hover:text-')

    # Optimizar métricas de 3 columnas
    content = content.replace(
        'grid grid-cols-3 gap-3 bg-slate-50 rounded-2xl p-3.5 border border-slate-200 text-center',
        'grid grid-cols-3 gap-1.5 sm:gap-3 bg-slate-50 rounded-2xl p-2 sm:p-3.5 border border-slate-200 text-center min-w-0'
    )
    content = content.replace(
        'grid grid-cols-3 lg:grid-cols-1 gap-2.5 bg-white/80 backdrop-blur rounded-2xl p-4 border border-purple-200 text-center shadow-sm',
        'grid grid-cols-3 lg:grid-cols-1 gap-1.5 sm:gap-2.5 bg-white/80 backdrop-blur rounded-2xl p-2 sm:p-4 border border-purple-200 text-center shadow-sm min-w-0'
    )

    # Optimizar tipografía de métricas
    content = content.replace('text-lg font-black text-blue-900', 'text-sm sm:text-lg font-black text-blue-900 truncate')
    content = content.replace('text-lg font-black text-indigo-900', 'text-sm sm:text-lg font-black text-indigo-900 truncate')
    content = content.replace('text-lg font-black text-amber-900', 'text-sm sm:text-lg font-black text-amber-900 truncate')
    content = content.replace('text-lg font-black text-cyan-800', 'text-sm sm:text-lg font-black text-cyan-800 truncate')
    content = content.replace('text-lg font-black text-purple-900', 'text-sm sm:text-lg font-black text-purple-900 truncate')
    content = content.replace('text-lg font-black text-emerald-700', 'text-sm sm:text-lg font-black text-emerald-700 truncate')
    content = content.replace('text-base font-black text-slate-800', 'text-xs sm:text-base font-black text-slate-800 truncate')
    content = content.replace('text-base font-black text-emerald-700', 'text-xs sm:text-base font-black text-emerald-700 truncate')

    # Optimizar los botones de Word de 3 columnas para que tengan icono arriba en móvil y no rompan el ancho
    doc_btn_pattern = r'<div class="grid grid-cols-3 gap-2 text-center text-xs">'
    doc_btn_replace = '<div class="grid grid-cols-3 gap-1.5 sm:gap-2 text-center text-[10px] sm:text-xs min-w-0">'
    content = re.sub(doc_btn_pattern, doc_btn_replace, content)

    # Convertir cada botón de descarga a flex-col sm:flex-row para que quepa perfecto en móvil
    content = content.replace(
        'class="p-2 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 font-medium transition flex items-center justify-center gap-1"',
        'class="py-2 px-1 sm:p-2 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 font-medium transition flex flex-col sm:flex-row items-center justify-center gap-0.5 sm:gap-1 text-[10px] sm:text-xs"'
    )

    # Optimizar el badge hero largo
    content = content.replace(
        'inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-500/20 border border-blue-400/30 text-blue-300 text-xs font-semibold',
        'inline-flex max-w-full items-center gap-1.5 px-3 py-1 rounded-full bg-blue-500/20 border border-blue-400/30 text-blue-300 text-xs font-semibold flex-wrap justify-center'
    )
    # Optimizar el badge de 15 documentos
    content = content.replace(
        'inline-flex items-center gap-2 px-3 py-1.5 rounded-lg bg-emerald-50 text-emerald-800 border border-emerald-200 text-xs font-bold',
        'inline-flex max-w-full items-center gap-1.5 px-2.5 py-1 sm:px-3 sm:py-1.5 rounded-lg bg-emerald-50 text-emerald-800 border border-emerald-200 text-[11px] sm:text-xs font-bold flex-wrap'
    )

    # Inyectar CSS
    if "</head>" in content:
        content = content.replace("</head>", ROBUST_MOBILE_CSS + "\n</head>")

    return content

def optimize_course_page(html_content, course_slug, total_sessions, prefix):
    """
    Optimiza una página de curso individual (mecatronica, ciberseguridad, etc.)
    """
    content = html_content

    # Corregir enlaces cruzados
    content = content.replace('../../index.html', '../curricula-2026/index.html')
    content = content.replace('../../TSU/index.html', '../curricula-2026/TSU/index.html')
    content = content.replace('../../Revision_Temarios/index.html', '../curricula-2026/Revision_Temarios/index.html')

    # Optimizar header del curso
    content = content.replace(
        '<div class="flex items-center gap-3">',
        '<div class="flex items-center gap-2 sm:gap-3 flex-wrap min-w-0">'
    )
    content = content.replace(
        '<nav class="flex space-x-2 sm:space-x-3 py-2.5 overflow-x-auto text-xs font-bold">',
        '<nav class="flex space-x-2 sm:space-x-3 py-2 sm:py-2.5 overflow-x-auto no-scrollbar text-xs font-bold touch-pan-x">'
    )

    # Inyectar CSS
    if "</head>" in content:
        content = content.replace("</head>", ROBUST_MOBILE_CSS + "\n</head>")

    # Interceptar función de selección de sesión para agregar auto-scroll en móvil
    func_name = f"select{prefix}Session"
    detail_card_id = f"{course_slug}-detail-card"

    pattern = rf"(function {func_name}\s*\(\s*num\s*\)\s*\{{)"
    replacement = rf"""\1
            // [Mobile Engine]: Auto-scroll a detalle en pantallas móviles
            if (window.innerWidth < 1024) {{
                setTimeout(function() {{
                    const card = document.getElementById('{detail_card_id}');
                    if (card) card.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
                }}, 60);
            }}"""
    content = re.sub(pattern, replacement, content)

    # Helper al final del body
    if "</body>" in content:
        content = content.replace("</body>", MOBILE_JS_AUTO_SCROLL_HELPER + "\n</body>")

    return content

def optimize_portal_page(html_content):
    """Optimiza index.html de curricula-2026"""
    content = html_content
    content = content.replace('Cursos/Web/index.html', '../new-courses/index.html')
    if "</head>" in content:
        content = content.replace("</head>", ROBUST_MOBILE_CSS + "\n</head>")
    return content

def optimize_general_page(html_content):
    """Optimiza páginas de TSU y Revision_Temarios"""
    content = html_content
    content = content.replace('Cursos/Web/index.html', '../../new-courses/index.html')
    content = content.replace('../Cursos/Web/index.html', '../../new-courses/index.html')
    if "</head>" in content:
        content = content.replace("</head>", ROBUST_MOBILE_CSS + "\n</head>")
    return content

print("=== CONSTRUYENDO VERSION MOVIL TOTALMENTE FLUIDA (SIN RESUMEN) ===")

os.makedirs(NEW_COURSES_OUT, exist_ok=True)
os.makedirs(os.path.join(CURRICULA_OUT, "Revision_Temarios"), exist_ok=True)
os.makedirs(os.path.join(CURRICULA_OUT, "TSU"), exist_ok=True)

# 1. NEW-COURSES
web_dir = os.path.join(WORKSPACE_DIR, "Cursos", "Web")
course_configs = [
    {"file": "mecatronica.html", "slug": "meca", "sessions": 20, "prefix": "Meca"},
    {"file": "ciberseguridad.html", "slug": "ciber", "sessions": 20, "prefix": "Ciber"},
    {"file": "automatizacion.html", "slug": "auto", "sessions": 20, "prefix": "Auto"},
    {"file": "cableado_estructurado.html", "slug": "cable", "sessions": 20, "prefix": "Cable"},
    {"file": "ia.html", "slug": "ia", "sessions": 8, "prefix": "Ia"}
]

print("1. Optimizando Catálogo de Nuevos Cursos...")
with open(os.path.join(web_dir, "index.html"), "r", encoding="utf-8") as f:
    cat_content = f.read()
opt_cat = optimize_catalog_index(cat_content)
with open(os.path.join(NEW_COURSES_OUT, "index.html"), "w", encoding="utf-8") as f:
    f.write(opt_cat)
print("  -> Catálogo adaptado sin recortes: new-courses/index.html")

for cfg in course_configs:
    src_path = os.path.join(web_dir, cfg["file"])
    dst_path = os.path.join(NEW_COURSES_OUT, cfg["file"])
    with open(src_path, "r", encoding="utf-8") as f:
        c_content = f.read()
    opt_content = optimize_course_page(c_content, cfg["slug"], cfg["sessions"], cfg["prefix"])
    with open(dst_path, "w", encoding="utf-8") as f:
        f.write(opt_content)
    print(f"  -> Curso optimizado: {cfg['file']}")

# 2. CURRICULA-2026
print("2. Optimizando Portal Maestro Kinal 2026...")
with open(os.path.join(WORKSPACE_DIR, "index.html"), "r", encoding="utf-8") as f:
    portal_content = f.read()
opt_portal = optimize_portal_page(portal_content)
with open(os.path.join(CURRICULA_OUT, "index.html"), "w", encoding="utf-8") as f:
    f.write(opt_portal)

# Revision_Temarios
rev_dir = os.path.join(WORKSPACE_DIR, "Revision_Temarios")
rev_out = os.path.join(CURRICULA_OUT, "Revision_Temarios")
print("3. Optimizando Revision_Temarios...")
for fname in os.listdir(rev_dir):
    if fname.endswith(".html") and not fname.startswith("index_anterior"):
        src = os.path.join(rev_dir, fname)
        dst = os.path.join(rev_out, fname)
        with open(src, "r", encoding="utf-8") as f:
            html = f.read()
        opt = optimize_general_page(html)
        with open(dst, "w", encoding="utf-8") as f:
            f.write(opt)

# TSU
tsu_dir = os.path.join(WORKSPACE_DIR, "TSU")
tsu_out = os.path.join(CURRICULA_OUT, "TSU")
print("4. Optimizando TSU (27 páginas)...")
for fname in os.listdir(tsu_dir):
    if fname.endswith(".html") and not fname.startswith("index_anterior"):
        src = os.path.join(tsu_dir, fname)
        dst = os.path.join(tsu_out, fname)
        with open(src, "r", encoding="utf-8") as f:
            html = f.read()
        opt = optimize_general_page(html)
        with open(dst, "w", encoding="utf-8") as f:
            f.write(opt)

# Asegurar que NO existe página de resumen en la raíz de optimización movil
summary_path = os.path.join(OUTPUT_BASE, "index.html")
if os.path.exists(summary_path):
    os.remove(summary_path)
    print("  -> Eliminada página de resumen previa.")

print("=== FINALIZADO CON ÉXITO ===")
