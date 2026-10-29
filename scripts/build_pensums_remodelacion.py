"""
Script para generar las 4 páginas de pensum y actualizar index.html
con la identidad gráfica oficial de Fundación Kinal y la Escuela Técnica Superior (ETS):
- Favicon oficial con el escudo de Kinal (assets/escudo_kinal.png).
- Fondo azul en degradado limpio (sin marca de agua ni imagen de llama).
- Botones en la esquina superior:
  - 'Inicio': fondo azul Kinal (#22376D)
  - 'Construcción', 'Electricidad', 'Industrial' (antes Mecánica) y 'Mecánica' (antes Automotriz): fondo blanco
- Encabezado: SOLO logo de Escuela Técnica Superior (assets/escuela_tecnica_superior.png).
- Pie de página: SOLO logo blanco de Fundación Kinal (assets/fundacion_kinal_blanco.png).
"""

import os
import re

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SOURCE_DIR = os.path.join(WORKSPACE_DIR, "curricula-2026", "Revision_Temarios")
TARGET_DIR = os.path.join(WORKSPACE_DIR, "rovalle-kinal.git", "remodelacion_revision_temarios")

AREAS = [
    {
        "filename": "construccion.html",
        "slug": "construccion",
        "title": "Área de Construcción, Topografía y Modelado BIM",
        "hours": "720 Horas",
        "courses_count": "6 Programas de Taller",
        "normas": "AGIES NSE-4 • SSO 229-2014 • BIM Forum GT • DGC Guatemala",
        "icon": "hard-hat",
        "desc": "Modernización curricular orientada a la ingeniería estructural sísmica (AGIES NSE-4), administración y supervisión de obras (Plan SSO 229-2014, Carta Gantt, APU), adopción del estándar BIM Forum Guatemala, interoperabilidad CAD-BIM, Navisworks clash detection y diseño vial con Autodesk Civil 3D y fotogrametría LiDAR de drones."
    },
    {
        "filename": "electricidad.html",
        "slug": "electricidad",
        "title": "Área de Electricidad Industrial, Electrónica y Automatización",
        "hours": "900 Horas",
        "courses_count": "5 Programas de Taller",
        "normas": "CNEE 186-2008 • NFPA 70E • Siemens TIA Portal • IEEE 142",
        "icon": "zap",
        "desc": "Formación técnica alineada a los pliegos tarifarios de EEGSA y Energuate, medición de resistividad de puesta a tierra con telurómetro, generación solar fotovoltaica On-Grid (CNEE-186-2008), control electromecánico con variadores de frecuencia VFD, PLC Siemens S7-1200 en TIA Portal, redes Profinet y electrónica de potencia aplicada."
    },
    {
        "filename": "mecanica.html",
        "slug": "mecanica",
        "title": "Área de Mecánica Industrial, Soldadura y Calderas de Vapor",
        "hours": "540 Horas",
        "courses_count": "3 Programas de Taller",
        "normas": "AWS D1.1 • ASME Sección IX • Reglamento General de Calderas (MinTrab)",
        "icon": "wrench",
        "desc": "Mantenimiento predictivo industrial con alineación láser de ejes y análisis de vibraciones IoT, calificación de procedimientos y soldadores según códigos internacionales AWS D1.1 y ASME Sección IX (procesos GMAW, FCAW, TIG inoxidable) y operación segura de calderas pirotubulares bajo la normativa de seguridad de recipientes a presión."
    },
    {
        "filename": "automotriz.html",
        "slug": "automotriz",
        "title": "Área de Mecánica Automotriz y Motocicletas",
        "hours": "1,080 Horas",
        "courses_count": "6 Programas de Taller",
        "normas": "SAE J1939 • Protocolos OBD-II / CAN-Bus ISO 14229 • EPA 609",
        "icon": "car",
        "desc": "Diagnóstico automotriz computarizado de alta gama en protocolos CAN-Bus e ISO 14229, inyección directa GDI y Common Rail Diésel, análisis de señales con osciloscopio digital automotriz, mecánica y diagnóstico de motocicletas 4T/2T con inyección electrónica EFI y servicio a sistemas R-134a/R-1234yf de climatización."
    }
]

def generate_header_nav(current_slug):
    buttons = [
        {"name": "Inicio", "url": "index.html", "icon": "home", "slug": "inicio"},
        {"name": "Construcción", "url": "construccion.html", "icon": "hard-hat", "slug": "construccion"},
        {"name": "Electricidad", "url": "electricidad.html", "icon": "zap", "slug": "electricidad"},
        {"name": "Industrial", "url": "mecanica.html", "icon": "wrench", "slug": "mecanica"},
        {"name": "Mecánica", "url": "automotriz.html", "icon": "car", "slug": "automotriz"},
    ]
    
    nav_html = []
    for btn in buttons:
        is_active = (btn["slug"] == current_slug)
        if btn["slug"] == "inicio":
            active_ring = " ring-2 ring-[#EC9123]" if is_active else ""
            nav_html.append(f'''                <a href="{btn["url"]}" class="px-3.5 py-2 rounded-lg bg-[#22376D] hover:bg-[#152244] text-white transition flex items-center gap-1.5 shadow-sm whitespace-nowrap font-bold{active_ring}">
                    <i data-lucide="{btn["icon"]}" class="w-4 h-4 text-[#EC9123]"></i> {btn["name"]}
                </a>''')
        else:
            active_cls = " ring-2 ring-[#EC9123] border-[#EC9123] font-black" if is_active else " border-slate-200 hover:border-[#22376D] font-bold"
            nav_html.append(f'''                <a href="{btn["url"]}" class="px-3.5 py-2 rounded-lg bg-white hover:bg-slate-50 border text-[#22376D] transition flex items-center gap-1.5 shadow-sm whitespace-nowrap{active_cls}">
                    <i data-lucide="{btn["icon"]}" class="w-4 h-4 text-[#EC9123]"></i> {btn["name"]}
                </a>''')
    
    return "\n".join(nav_html)

def build_pensum_page(area):
    source_path = os.path.join(SOURCE_DIR, area["filename"])
    target_path = os.path.join(TARGET_DIR, area["filename"])
    
    with open(source_path, "r", encoding="utf-8") as f:
        src = f.read()
        
    # Extraer el contenido de cursos (desde <!-- Selector de Cursos hasta </main>)
    sel_idx = src.find("<!-- Selector de Cursos")
    if sel_idx == -1:
        sel_idx = src.find("id=\"course-selector-anchor\"")
        if sel_idx != -1:
            div_prev = src.rfind("<div", 0, sel_idx)
            sel_idx = div_prev if div_prev != -1 else sel_idx
            
    main_end = src.find("</main>")
    if sel_idx == -1 or main_end == -1:
        raise ValueError(f"No se pudo delimitar el contenido de cursos en {area['filename']}")
        
    course_content = src[sel_idx:main_end]
    
    # Extraer scripts originales después de </footer>
    footer_idx = src.find("<footer")
    script_idx = src.find("<script>", footer_idx)
    scripts_content = src[script_idx:] if script_idx != -1 else ""
    
    nav_buttons_html = generate_header_nav(area["slug"])
    
    full_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{area["title"]} | Escuela Técnica Superior — Fundación Kinal</title>
    
    <!-- Favicon Oficial: Escudo de Fundación Kinal -->
    <link rel="icon" type="image/png" href="assets/escudo_kinal.png">
    
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Lucide Icons -->
    <script src="https://unpkg.com/lucide@latest"></script>
    
    <!-- Google Fonts complementarias para renderizado web fiel a Times y Arial -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Playfair+Display:ital,wght@0,600;0,700;0,800;0,900;1,600&display=swap" rel="stylesheet">

    <style>
        /* =========================================================
           IDENTIDAD GRÁFICA OFICIAL — FUNDACIÓN KINAL
           Manual de Identidad Corporativa:
           - Títulos: Times New Roman / Times Bold
           - Complementaria / Lectura: Arial (Regular, Italic, Bold)
           - Color Azul Kinal: C:100 M:90 Y:30 K:15 -> RGB(34, 55, 109) -> #22376D
           - Color Llama Kinal: C:5 M:50 Y:100 K:0  -> RGB(236, 145, 35) -> #EC9123
           ========================================================= */
        :root {{
            --kinal-blue: #22376D;
            --kinal-blue-dark: #152244;
            --kinal-blue-deep: #0D162C;
            --kinal-blue-light: #2E4A91;
            --kinal-flame: #EC9123;
            --kinal-gold: #F5A623;
            --kinal-gray-8c: #888B8D;
            --kinal-bg-light: #F8F9FA;
            --kinal-border: #DDE2E5;
        }}

        body {{
            font-family: Arial, Helvetica, "Nimbus Sans L", "Liberation Sans", sans-serif;
            background-color: var(--kinal-bg-light);
            color: #1E293B;
            -webkit-font-smoothing: antialiased;
        }}

        /* Tipografía Corporativa Oficial de Kinal para Títulos */
        h1, h2, h3, h4, .font-kinal-title, .brand-serif, .font-heading {{
            font-family: "Times New Roman", Times, "Playfair Display", Georgia, serif;
            letter-spacing: -0.01em;
        }}

        .bg-kinal-blue {{ background-color: var(--kinal-blue); }}
        .bg-kinal-blue-dark {{ background-color: var(--kinal-blue-dark); }}
        .text-kinal-blue {{ color: var(--kinal-blue); }}
        .border-kinal-blue {{ border-color: var(--kinal-blue); }}

        .bg-kinal-flame {{ background-color: var(--kinal-flame); }}
        .text-kinal-flame {{ color: var(--kinal-flame); }}
        .border-kinal-flame {{ border-color: var(--kinal-flame); }}

        .hero-kinal-gradient {{
            background: linear-gradient(135deg, #0D162C 0%, #152244 45%, #22376D 100%);
        }}

        /* Código de color auditado institucional */
        .item-delete, .status-delete {{ background-color: #FEF2F2; border-left: 4px solid #DC2626; color: #991B1B; }}
        .item-update, .status-update {{ background-color: #FEFCE8; border-left: 4px solid #EAB308; color: #854D0E; }}
        .item-new, .status-new       {{ background-color: #EFF6FF; border-left: 4px solid #2563EB; color: #1E40AF; }}
        .item-keep, .status-keep     {{ background-color: #F0FDF4; border-left: 4px solid #16A34A; color: #166534; }}
        .status-ia                   {{ background-color: #FAF5FF; border-left: 4px solid #9333EA; color: #6B21A8; }}

        @media print {{ .no-print {{ display: none !important; }} }}

        /* Estilos móviles sin desborde */
        @media (max-width: 767px) {{
            *, *::before, *::after {{ box-sizing: border-box !important; }}
            html, body {{ overflow-x: hidden !important; max-width: 100vw !important; }}
            .no-scrollbar::-webkit-scrollbar {{ display: none !important; }}
            .no-scrollbar {{ -ms-overflow-style: none !important; scrollbar-width: none !important; }}
            
            main, section, header, footer, 
            .max-w-7xl, .max-w-6xl, .max-w-5xl, .max-w-4xl, .max-w-3xl, .max-w-2xl {{
                width: 100% !important;
                max-width: 100% !important;
                min-width: 0 !important;
                box-sizing: border-box !important;
            }}
            .card-hover, [class*="rounded-3xl"], [class*="rounded-2xl"], .area-course-card {{
                width: 100% !important;
                max-width: 100% !important;
                min-width: 0 !important;
                padding-left: 1rem !important;
                padding-right: 1rem !important;
                box-sizing: border-box !important;
            }}
            h1, h2, h3, h4, h5, p, span, a, div {{
                overflow-wrap: break-word !important;
                word-break: break-word !important;
            }}
            .tab-btn, button, select, input[type="text"] {{
                min-height: 42px;
                touch-action: manipulation;
            }}
        }}

        @media (max-width: 1023px) {{
            .session-item {{
                cursor: pointer;
                -webkit-tap-highlight-color: transparent;
                transition: all 0.2s ease;
            }}
            [id$="-detail-card"] {{
                scroll-margin-top: 80px;
            }}
        }}
    </style>
</head>
<body class="min-h-screen flex flex-col antialiased">

    <!-- ========================================================= -->
    <!-- BARRA INSTITUCIONAL SUPERIOR                              -->
    <!-- ========================================================= -->
    <div class="bg-[#152244] text-white text-xs border-b-2 border-[#EC9123]">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-2 flex flex-wrap justify-between items-center gap-2">
            <div class="flex items-center gap-3">
                <span class="inline-flex items-center gap-1.5 font-bold tracking-wider uppercase text-[#EC9123]">
                    <i data-lucide="award" class="w-3.5 h-3.5"></i> Fundación Kinal
                </span>
                <span class="text-slate-500">|</span>
                <span class="text-slate-300 font-medium hidden sm:inline">
                    Ideario Institucional: <em>«El trabajo bien hecho»</em>
                </span>
            </div>
            <div class="flex items-center gap-4 text-slate-300 font-medium">
                <span class="flex items-center gap-1.5">
                    <i data-lucide="calendar" class="w-3.5 h-3.5 text-[#EC9123]"></i> Ciclo Académico 2026
                </span>
                <span class="text-slate-600">|</span>
                <span class="text-emerald-400 font-bold flex items-center gap-1">
                    <i data-lucide="shield-check" class="w-3.5 h-3.5"></i> Aval UNIS-Kinal
                </span>
            </div>
        </div>
    </div>

    <!-- ========================================================= -->
    <!-- HEADER CORPORATIVO (SOLO LOGO ETS & BOTONES SUPERIORES)   -->
    <!-- ========================================================= -->
    <header class="bg-white border-b border-slate-200 sticky top-0 z-50 shadow-sm">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3.5 flex flex-wrap justify-between items-center gap-4">
            
            <!-- Logotipo de Escuela Técnica Superior (ETS) -->
            <div class="flex items-center">
                <a href="index.html" class="flex items-center group">
                    <img src="assets/escuela_tecnica_superior.png" alt="Escuela Técnica Superior" class="h-8 sm:h-10 w-auto object-contain transition group-hover:opacity-90">
                </a>
            </div>

            <!-- Navegación: Botones de 1 palabra con fondo blanco (excepto Inicio) -->
            <nav class="flex items-center gap-2 sm:gap-3 text-xs overflow-x-auto no-scrollbar py-1">
{nav_buttons_html}
            </nav>
        </div>
    </header>

    <!-- ========================================================= -->
    <!-- HERO PRINCIPAL DEL ÁREA (FONDO AZUL DEGRADADO LIMPIO)     -->
    <!-- ========================================================= -->
    <section class="hero-kinal-gradient text-white py-12 sm:py-16 px-4 sm:px-6 lg:px-8 relative overflow-hidden">
        
        <div class="max-w-7xl mx-auto space-y-6 relative z-10">
            
            <!-- Badge institucional superior -->
            <div class="inline-flex items-center px-3.5 py-1.5 rounded-full bg-white/10 border border-white/20 text-[#EC9123] text-xs font-bold tracking-wide uppercase">
                <span>Escuela Técnica Superior (ETS) • Ciclo Lectivo 2026</span>
            </div>

            <!-- Título Institucional Times Bold SIN LLAMA -->
            <h1 class="text-3xl sm:text-5xl font-bold tracking-tight leading-tight brand-serif text-white">
                {area["title"]}
            </h1>

            <p class="text-slate-200 text-sm sm:text-base lg:text-lg max-w-4xl leading-relaxed">
                {area["desc"]}
            </p>

            <!-- Cita Doctrinal y Formativa Limpia -->
            <div class="pt-1 text-xs text-slate-300">
                <span>Formación doctrinal y espiritual a cargo de la Prelatura del Opus Dei</span>
            </div>

            <!-- Métricas Clave Consolidadas -->
            <div class="grid grid-cols-2 md:grid-cols-4 gap-3 sm:gap-4 pt-4 text-left">
                <div class="bg-white/10 backdrop-blur rounded-2xl p-4 border border-white/15 space-y-1">
                    <div class="text-[11px] uppercase tracking-wider text-slate-300 font-bold">Carga Práctica</div>
                    <div class="text-2xl sm:text-3xl font-bold brand-serif text-white">{area["hours"]}</div>
                    <div class="text-[11px] text-emerald-400 font-medium">100% Taller Especializado</div>
                </div>
                <div class="bg-white/10 backdrop-blur rounded-2xl p-4 border border-white/15 space-y-1">
                    <div class="text-[11px] uppercase tracking-wider text-slate-300 font-bold">Especialidades</div>
                    <div class="text-2xl sm:text-3xl font-bold brand-serif text-white">{area["courses_count"]}</div>
                    <div class="text-[11px] text-[#EC9123] font-medium">Currícula Actualizada</div>
                </div>
                <div class="bg-white/10 backdrop-blur rounded-2xl p-4 border border-white/15 space-y-1">
                    <div class="text-[11px] uppercase tracking-wider text-slate-300 font-bold">Normativas</div>
                    <div class="text-sm font-bold brand-serif text-white line-clamp-2">{area["normas"].split('•')[0]}</div>
                    <div class="text-[11px] text-amber-300 font-medium">Estándar Industrial</div>
                </div>
                <div class="bg-white/10 backdrop-blur rounded-2xl p-4 border border-white/15 space-y-1">
                    <div class="text-[11px] uppercase tracking-wider text-slate-300 font-bold">Aprobación Mínima</div>
                    <div class="text-2xl sm:text-3xl font-bold brand-serif text-amber-400">≥ 75 Pts</div>
                    <div class="text-[11px] text-slate-300 font-medium">Exigencia Kinal / 100</div>
                </div>
            </div>

        </div>
    </section>

    <!-- ========================================================= -->
    <!-- CONTENIDO PRINCIPAL: METODOLOGÍA & CURSOS DEL PENSUM       -->
    <!-- ========================================================= -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8 flex-1">

        <!-- Metodología de Código de Color Institucional -->
        <div class="p-5 rounded-2xl bg-white border border-slate-200 shadow-sm space-y-3">
            <h3 class="text-xs font-bold text-slate-500 uppercase tracking-wider flex items-center gap-2">
                <i data-lucide="info" class="w-4 h-4 text-[#22376D]"></i> Metodología de Auditoría Curricular Kinal
            </h3>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3 text-xs">
                <div class="p-3 rounded-xl bg-red-50 border border-red-200 text-red-900">
                    <strong class="text-red-700 block mb-1">🔴 ROJO (Eliminar)</strong>
                    Contenidos obsoletos retirados para optimizar el tiempo de taller.
                </div>
                <div class="p-3 rounded-xl bg-amber-50 border border-amber-200 text-amber-900">
                    <strong class="text-amber-700 block mb-1">🟡 AMARILLO (Actualizar)</strong>
                    Temas existentes modernizados según las normas técnicas vigentes.
                </div>
                <div class="p-3 rounded-xl bg-blue-50 border border-blue-200 text-blue-900">
                    <strong class="text-blue-700 block mb-1">🔵 AZUL (Propuesta Nueva)</strong>
                    Nuevas competencias prioritarias demandadas por la industria en Guatemala.
                </div>
                <div class="p-3 rounded-xl bg-purple-50 border border-purple-200 text-purple-900">
                    <strong class="text-purple-700 block mb-1">🟣 PÚRPURA (Innovación IA)</strong>
                    Módulos aplicados de Inteligencia Artificial incorporados en cada programa.
                </div>
            </div>
        </div>

{course_content}
    </main>

    <!-- ========================================================= -->
    <!-- FOOTER INSTITUCIONAL (SOLO FUNDACIÓN KINAL EN BLANCO)     -->
    <!-- ========================================================= -->
    <footer class="bg-[#0D162C] text-white border-t-4 border-[#EC9123] py-12 px-4 sm:px-6 lg:px-8 mt-12">
        <div class="max-w-7xl mx-auto space-y-8">
            <div class="flex flex-col md:flex-row justify-between items-start md:items-center gap-6 border-b border-slate-800 pb-8">
                <div class="flex items-center gap-4">
                    <img src="assets/fundacion_kinal_blanco.png" alt="Fundación Kinal" class="h-10 sm:h-12 w-auto object-contain">
                </div>
                <div class="text-xs text-slate-400 max-w-md text-left md:text-right">
                    <strong class="text-white block mb-0.5">Fundación Kinal — Escuela Técnica Superior (ETS)</strong>
                    Servicios de capacitación técnica y tecnológica dirigidos a empresas y personas individuales para desarrollar competencias laborales al mejor nivel.
                </div>
            </div>

            <div class="flex flex-col sm:flex-row justify-between items-center text-xs text-slate-500 gap-4">
                <div>
                    © 2026 Fundación Kinal. Todos los derechos reservados. Ciudad de Guatemala.
                </div>
                <div class="flex items-center gap-4">
                    <span class="text-slate-400">Ideario: <em>«El trabajo bien hecho»</em></span>
                    <span>•</span>
                    <span class="text-[#EC9123]">Aval UNIS-Kinal</span>
                </div>
            </div>
        </div>
    </footer>

{scripts_content}
"""

    with open(target_path, "w", encoding="utf-8") as f:
        f.write(full_html)
        
    print(f"[OK] Generado exitosamente: {target_path} ({len(full_html)} bytes)")

def update_index_page():
    index_path = os.path.join(TARGET_DIR, "index.html")
    with open(index_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Agregar favicon si no está presente
    if "escudo_kinal.png" not in content:
        favicon_tag = '\n    <!-- Favicon Oficial: Escudo de Fundación Kinal -->\n    <link rel="icon" type="image/png" href="assets/escudo_kinal.png">'
        content = content.replace('<head>', '<head>' + favicon_tag)

    # 2. Reemplazar la barra de navegación de index.html con los mismos 5 botones
    nav_html = generate_header_nav("inicio")
    # Buscar el nav en header
    nav_pattern = re.compile(r'<nav class="flex items-center gap-2 sm:gap-3 text-xs.*?</nav>', re.DOTALL)
    new_nav = f'<nav class="flex items-center gap-2 sm:gap-3 text-xs overflow-x-auto no-scrollbar py-1">\n{nav_html}\n            </nav>'
    content = nav_pattern.sub(new_nav, content)

    # 3. Eliminar marca de agua de la llama en el hero si existe
    watermark_pattern = re.compile(r'<!-- Elementos gráficos de fondo.*?<div class="absolute right-0 bottom-0 opacity-10.*?</div>\s*</div>', re.DOTALL)
    content = watermark_pattern.sub('', content)

    # Caso alternativo de regex si la etiqueta difiere levemente
    watermark_simple = re.compile(r'<div class="absolute right-0 bottom-0 opacity-10 pointer-events-none transform translate-x-12 translate-y-12">\s*<img src="assets/llama_kinal\.png"[^>]*>\s*</div>', re.DOTALL)
    content = watermark_simple.sub('', content)

    with open(index_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"[OK] Actualizado exitosamente: {index_path} ({len(content)} bytes)")

if __name__ == "__main__":
    for area in AREAS:
        build_pensum_page(area)
    update_index_page()
    print("Todas las páginas han sido actualizadas con favicon, fondo degradado limpio y botones renovados.")
