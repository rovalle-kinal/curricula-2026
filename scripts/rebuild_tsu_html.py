# -*- coding: utf-8 -*-
import json
import os

# Cargar cursos_data
with open("cursos_data.json", "r", encoding="utf-8") as f:
    cursos_data = json.load(f)

# Configuración de las 4 líneas
lines_config = [
    {
        "id": "linea-etica",
        "name": "Formación Humana y Ética",
        "sub": "4 Cursos • Deontología y Gobernanza IA",
        "icon": "🛡️",
        "color": "#0284c7",
        "b1": ["b1_etica_general_1"],
        "b2": ["b2_etica_general_2"],
        "b3": ["b3_etica_profesional_1"],
        "b4": ["b4_etica_profesional_2"]
    },
    {
        "id": "linea-gestion",
        "name": "Gestión y Supervisión Industrial",
        "sub": "8 Cursos • Lean, SSO, Costos y Calidad",
        "icon": "📋",
        "color": "#d97706",
        "b1": ["b1_fundamentos_administracion", "b1_planeacion_control_trabajo"],
        "b2": ["b2_herramientas_contables", "b2_administracion_rrhh_sso"],
        "b3": ["b3_metodos_produccion", "b3_servicio_cliente"],
        "b4": ["b4_control_calidad", "b4_fundamentos_marketing"]
    },
    {
        "id": "linea-matematica",
        "name": "Ciencias Matemáticas y Analítica",
        "sub": "4 Cursos • Modelado, Finanzas y Estadística",
        "icon": "📐",
        "color": "#16a34a",
        "b1": ["b1_matematica_basica_1"],
        "b2": ["b2_matematica_basica_2"],
        "b3": ["b3_matematica_aplicada_1"],
        "b4": ["b4_matematica_aplicada_2"]
    },
    {
        "id": "linea-fisica",
        "name": "Física y Tecnología Industrial 4.0",
        "sub": "4 Cursos • Materiales, Energía y Sensores Python",
        "icon": "⚡",
        "color": "#7c3aed",
        "b1": ["b1_fisica_basica_1"],
        "b2": ["b2_fisica_aplicada_1"],
        "b3": ["b3_fisica_aplicada_2"],
        "b4": ["b4_fisica_aplicada_3"]
    }
]

def render_compact_card(cid):
    c = cursos_data[cid]
    in_count = len(c["prerequisitos"])
    out_count = len(c["habilita"])
    
    return f"""
        <div class="node-card p-2 sm:p-2.5 rounded-xl border border-slate-200 bg-white shadow-xs hover:border-[#22376D] transition relative"
             data-id="{c['id']}" data-linea="{c['linea_id']}"
             onclick="selectCourseNode('{c['id']}')"
             onmouseenter="highlightNodeRuta('{c['id']}')"
             onmouseleave="clearHighlightNode()">
            
            <div class="flex items-center justify-between gap-1 mb-1">
                <span class="text-[9px] font-extrabold px-1.5 py-0.5 rounded bg-slate-100 text-slate-700 tracking-wider">
                    {c['codigo']}
                </span>
                <span class="text-[9px] font-semibold text-slate-500">
                    {c['horas']}
                </span>
            </div>

            <div class="flex items-start gap-1 mb-1">
                <span class="text-xs leading-none select-none">{c['icono']}</span>
                <strong class="text-[11px] font-bold text-[#22376D] leading-tight block">
                    {c['nombre']}
                </strong>
            </div>

            <p class="text-[9.5px] text-slate-500 line-clamp-2 leading-snug mb-1.5">
                {c['subtitulo']}
            </p>

            <div class="flex items-center gap-1 pt-1 border-t border-slate-100 text-[8.5px] font-bold">
                <span class="px-1 py-0.5 rounded {'bg-emerald-50 text-emerald-700' if in_count > 0 else 'bg-slate-50 text-slate-400'}">
                    IN: {in_count}
                </span>
                <span class="px-1 py-0.5 rounded {'bg-amber-50 text-amber-700' if out_count > 0 else 'bg-slate-50 text-slate-400'}">
                    OUT: {out_count}
                </span>
            </div>
        </div>
    """

rows_html = ""
for line in lines_config:
    b1_html = "".join([render_compact_card(cid) for cid in line["b1"]])
    b2_html = "".join([render_compact_card(cid) for cid in line["b2"]])
    b3_html = "".join([render_compact_card(cid) for cid in line["b3"]])
    b4_html = "".join([render_compact_card(cid) for cid in line["b4"]])

    rows_html += f"""
    <!-- Fila de Línea: {line['name']} -->
    <div class="grid-linea-row grid grid-cols-[180px_repeat(4,minmax(170px,1fr))] border-b border-slate-200" id="row-{line['id']}">
        <!-- Etiqueta de la Línea -->
        <div class="p-3 bg-slate-50/90 border-r border-slate-200 flex flex-col justify-center border-l-4" style="border-left-color: {line['color']};">
            <div class="flex items-center gap-1.5 mb-1">
                <span class="text-lg">{line['icon']}</span>
                <strong class="text-xs font-bold text-[#22376D] leading-tight">{line['name']}</strong>
            </div>
            <span class="text-[10px] text-slate-500 font-medium leading-tight">{line['sub']}</span>
        </div>

        <!-- Bimestre 1 -->
        <div class="p-2 bg-white border-r border-slate-200 flex flex-col gap-2">
            {b1_html}
        </div>

        <!-- Bimestre 2 -->
        <div class="p-2 bg-slate-50/40 border-r border-slate-200 flex flex-col gap-2">
            {b2_html}
        </div>

        <!-- Bimestre 3 -->
        <div class="p-2 bg-white border-r border-slate-200 flex flex-col gap-2">
            {b3_html}
        </div>

        <!-- Bimestre 4 -->
        <div class="p-2 bg-slate-50/40 flex flex-col gap-2">
            {b4_html}
        </div>
    </div>
    """

tsu_html = f"""<!DOCTYPE html>
<html lang="es" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
    <title>Técnico Superior Universitario (TSU) — Malla Curricular 2026 | Fundación Kinal</title>
    
    <!-- Favicon Oficial: Escudo de Kinal -->
    <link rel="icon" type="image/png" href="assets/escudo_kinal.png">
    
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    
    <!-- Lucide Icons -->
    <script src="https://unpkg.com/lucide@latest"></script>

    <!-- Fuentes Oficiales Fundación Kinal -->
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700;800&family=Montserrat:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Playfair+Display:ital,wght@0,600;0,700;1,400&display=swap');

        :root {{
            --kinal-navy: #22376D;
            --kinal-flame: #EC9123;
            --kinal-navy-dark: #152244;
            --kinal-night: #0D162C;
            --kinal-gray-bg: #F8FAFC;
        }}

        body {{
            font-family: Arial, Helvetica, sans-serif;
            color: #1E293B;
            background-color: var(--kinal-gray-bg);
        }}

        .brand-serif {{
            font-family: 'Times New Roman', Times, 'Playfair Display', serif;
        }}

        .bg-kinal-navy {{ background-color: var(--kinal-navy); }}
        .text-kinal-navy {{ color: var(--kinal-navy); }}
        .border-kinal-navy {{ border-color: var(--kinal-navy); }}

        .bg-kinal-flame {{ background-color: var(--kinal-flame); }}
        .text-kinal-flame {{ color: var(--kinal-flame); }}
        .border-kinal-flame {{ border-color: var(--kinal-flame); }}

        .hero-kinal-gradient {{
            background: linear-gradient(135deg, #0D162C 0%, #152244 45%, #22376D 100%);
        }}

        /* Estilos Malla Curricular Interactiva */
        .node-card {{
            transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            cursor: pointer;
            border: 1.5px solid #E2E8F0;
            background-color: #FFFFFF;
        }}
        .node-card:hover {{
            transform: translateY(-2px);
            border-color: #22376D;
            box-shadow: 0 4px 10px rgba(34, 55, 109, 0.08);
        }}
        .node-card.selected {{
            border-color: #22376D !important;
            background-color: #EFF6FF !important;
            box-shadow: 0 0 0 3px rgba(34, 55, 109, 0.3) !important;
            transform: scale(1.02);
            z-index: 20;
        }}
        .node-card.selected::after {{
            content: "SELECCIONADO";
            position: absolute;
            top: -8px;
            right: 6px;
            background: #22376D;
            color: #FFFFFF;
            font-size: 0.58rem;
            font-weight: 800;
            padding: 1px 5px;
            border-radius: 3px;
            letter-spacing: 0.3px;
        }}
        .node-card.prereq-active {{
            border-color: #16A34A !important;
            background-color: #F0FDF4 !important;
            box-shadow: 0 0 0 2px rgba(22, 163, 74, 0.4) !important;
            z-index: 10;
        }}
        .node-card.prereq-active::after {{
            content: "⬅️ PRERREQUISITO";
            position: absolute;
            top: -8px;
            right: 6px;
            background: #16A34A;
            color: #FFFFFF;
            font-size: 0.58rem;
            font-weight: 800;
            padding: 1px 5px;
            border-radius: 3px;
            letter-spacing: 0.3px;
        }}
        .node-card.habilita-active {{
            border-color: #EC9123 !important;
            background-color: #FEFCE8 !important;
            box-shadow: 0 0 0 2px rgba(236, 145, 35, 0.4) !important;
            z-index: 10;
        }}
        .node-card.habilita-active::after {{
            content: "➡️ HABILITA A";
            position: absolute;
            top: -8px;
            right: 6px;
            background: #EC9123;
            color: #FFFFFF;
            font-size: 0.58rem;
            font-weight: 800;
            padding: 1px 5px;
            border-radius: 3px;
            letter-spacing: 0.3px;
        }}
        .node-card.dimmed {{
            opacity: 0.32;
            filter: grayscale(40%);
        }}

        @media (max-width: 767px) {{
            *, *::before, *::after {{ box-sizing: border-box !important; }}
            html, body {{ overflow-x: hidden !important; max-width: 100vw !important; }}
            .no-scrollbar::-webkit-scrollbar {{ display: none !important; }}
            .no-scrollbar {{ -ms-overflow-style: none !important; scrollbar-width: none !important; }}
        }}
    </style>
</head>
<body class="min-h-screen flex flex-col antialiased pt-[115px] sm:pt-[125px]">

    <!-- ========================================================= -->
    <!-- ENCABEZADO FIJO PERMANENTE (SIEMPRE VISIBLE)              -->
    <!-- ========================================================= -->
    <div class="fixed top-0 left-0 right-0 z-50 bg-white shadow-md border-b border-slate-200">
        
        <!-- BARRA INSTITUCIONAL SUPERIOR -->
        <div class="bg-[#152244] text-white text-xs border-b-2 border-[#EC9123]">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-1.5 flex flex-wrap justify-between items-center gap-2">
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

        <!-- HEADER CORPORATIVO (SOLO LOGO ETS & BOTONES TODOS BLANCOS) -->
        <header class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-2.5 sm:py-3 flex flex-wrap justify-between items-center gap-3">
            <div class="flex items-center">
                <a href="index.html" class="flex items-center group">
                    <img src="assets/escuela_tecnica_superior.png" alt="Escuela Técnica Superior" class="h-8 sm:h-10 w-auto object-contain transition group-hover:opacity-90">
                </a>
            </div>

            <!-- Botones de Navegación: TODOS BLANCOS -->
            <nav class="flex items-center gap-2 sm:gap-3 text-xs overflow-x-auto no-scrollbar py-1">
                <a href="index.html" class="px-3.5 py-2 rounded-lg bg-white hover:bg-slate-50 text-[#22376D] transition flex items-center gap-1.5 shadow-sm whitespace-nowrap font-bold border border-slate-200">
                    <i data-lucide="home" class="w-4 h-4 text-[#EC9123]"></i> Inicio
                </a>
                <a href="#malla" class="px-3.5 py-2 rounded-lg bg-white hover:bg-slate-50 text-[#22376D] transition flex items-center gap-1.5 shadow-sm whitespace-nowrap font-bold border border-slate-200">
                    <i data-lucide="layers" class="w-4 h-4 text-[#EC9123]"></i> Malla
                </a>
                <a href="#lineas" class="px-3.5 py-2 rounded-lg bg-white hover:bg-slate-50 text-[#22376D] transition flex items-center gap-1.5 shadow-sm whitespace-nowrap font-bold border border-slate-200">
                    <i data-lucide="git-branch" class="w-4 h-4 text-[#EC9123]"></i> Líneas
                </a>
                <a href="tsu_auditoria.html" class="px-3.5 py-2 rounded-lg bg-white hover:bg-slate-50 text-[#22376D] transition flex items-center gap-1.5 shadow-sm whitespace-nowrap font-bold border border-slate-200">
                    <i data-lucide="check-square" class="w-4 h-4 text-[#EC9123]"></i> Revisión
                </a>
            </nav>
        </header>

    </div>

    <!-- ========================================================= -->
    <!-- HERO PRINCIPAL DE TSU (FONDO AZUL DEGRADADO LIMPIO)       -->
    <!-- ========================================================= -->
    <section class="hero-kinal-gradient text-white py-12 sm:py-16 px-4 sm:px-6 lg:px-8 relative overflow-hidden">
        
        <div class="max-w-7xl mx-auto space-y-6 relative z-10">
            
            <!-- Badge institucional superior -->
            <div class="inline-flex items-center px-3.5 py-1.5 rounded-full bg-white/10 border border-white/20 text-[#EC9123] text-xs font-bold tracking-wide uppercase">
                <span>Escuela Técnica Superior (ETS) • Ciclo Lectivo 2026 • Aval UNIS</span>
            </div>

            <!-- Título Institucional con tipografía oficial Times -->
            <h1 class="text-3xl sm:text-5xl font-bold tracking-tight leading-tight brand-serif text-white">
                Técnico Superior Universitario (TSU) — 3er Año
            </h1>

            <p class="text-slate-200 text-sm sm:text-base lg:text-lg max-w-4xl leading-relaxed">
                Malla curricular interactiva, mapa de correlatividades y competencias del 3er Año de Técnico Superior Universitario, avalado por la <strong>Universidad del Istmo (UNIS)</strong> y <strong>Fundación Kinal</strong>. Estructurado en 4 bimestres académicos modulares que integran la gestión de operaciones, ciencias exactas aplicadas y deontología profesional en régimen dual.
            </p>

            <!-- Cita Doctrinal y Formativa -->
            <div class="pt-1 text-xs text-slate-300">
                <span>Formación doctrinal y espiritual a cargo de la Prelatura del Opus Dei</span>
            </div>

            <!-- Métricas Clave Consolidadas del TSU -->
            <div class="grid grid-cols-2 md:grid-cols-4 gap-3 sm:gap-4 pt-4 text-left">
                <div class="bg-white/10 backdrop-blur rounded-2xl p-4 border border-white/15 space-y-1">
                    <div class="text-[11px] uppercase tracking-wider text-slate-300 font-bold">Asignaturas</div>
                    <div class="text-2xl sm:text-3xl font-bold brand-serif text-white">20 Cursos</div>
                    <div class="text-[11px] text-[#EC9123] font-medium">4 Bimestres Modulares</div>
                </div>
                <div class="bg-white/10 backdrop-blur rounded-2xl p-4 border border-white/15 space-y-1">
                    <div class="text-[11px] uppercase tracking-wider text-slate-300 font-bold">Líneas Formativas</div>
                    <div class="text-2xl sm:text-3xl font-bold brand-serif text-white">4 Líneas</div>
                    <div class="text-[11px] text-emerald-400 font-medium">Gestión, Matemáticas, Física, Ética</div>
                </div>
                <div class="bg-white/10 backdrop-blur rounded-2xl p-4 border border-white/15 space-y-1">
                    <div class="text-[11px] uppercase tracking-wider text-slate-300 font-bold">Acreditación</div>
                    <div class="text-sm font-bold brand-serif text-white">Universidad del Istmo</div>
                    <div class="text-[11px] text-amber-300 font-medium">Aval UNIS-Kinal</div>
                </div>
                <div class="bg-white/10 backdrop-blur rounded-2xl p-4 border border-white/15 space-y-1">
                    <div class="text-[11px] uppercase tracking-wider text-slate-300 font-bold">Aprobación Mínima</div>
                    <div class="text-2xl sm:text-3xl font-bold brand-serif text-amber-400">≥ 75 Pts</div>
                    <div class="text-[11px] text-slate-300 font-medium">Exigencia Kinal sobre 100</div>
                </div>
            </div>

        </div>
    </section>

    <!-- ========================================================= -->
    <!-- CONTENIDO PRINCIPAL DEL PORTAL TSU                        -->
    <!-- ========================================================= -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 space-y-14 flex-1">

        <!-- ===================================================== -->
        <!-- SECCIÓN 1: MALLA CURRICULAR INTERACTIVA CON DEPENDENCIAS -->
        <!-- ===================================================== -->
        <section id="malla" class="space-y-6 scroll-mt-36">
            
            <div class="flex flex-col sm:flex-row justify-between items-start sm:items-end gap-3 border-b-2 border-slate-200 pb-4">
                <div>
                    <span class="text-xs font-bold text-[#EC9123] tracking-widest uppercase">Malla Académica Oficial e Interactiva</span>
                    <h2 class="text-2xl sm:text-3xl font-bold brand-serif text-[#22376D] mt-1">
                        Red Curricular y Mapa de Prerrequisitos
                    </h2>
                    <p class="text-slate-600 text-xs sm:text-sm mt-1 max-w-3xl leading-relaxed">
                        Explora la red relacional del pensum universitario. Haz clic en cualquier asignatura para resaltar en verde sus <strong>prerrequisitos requeridos</strong> y en naranja los cursos que <strong>habilita</strong> en los siguientes bimestres.
                    </p>
                </div>
                <span class="px-3 py-1 rounded-full bg-[#22376D]/10 text-[#22376D] font-bold text-xs border border-[#22376D]/20 whitespace-nowrap">
                    Ciclo 2026 • 3er Año TSU
                </span>
            </div>

            <!-- Barra de Instrucciones y Leyenda de Colores Kinal -->
            <div class="bg-amber-50/70 border-l-4 border-[#EC9123] p-4 rounded-r-2xl flex flex-col md:flex-row justify-between items-start md:items-center gap-4 text-xs">
                <div class="space-y-0.5">
                    <strong class="text-amber-900 block font-bold">💡 Navegación Dinámica de la Red Curricular:</strong>
                    <span class="text-amber-800">
                        Selecciona o pasa el cursor sobre una materia para activar su Ruta Crítica. La ficha lateral actualizará la descripción, horas e integración con Inteligencia Artificial.
                    </span>
                </div>
                <div class="flex flex-wrap items-center gap-2 text-xs font-bold bg-white px-3 py-2 rounded-xl border border-amber-200 shadow-sm shrink-0">
                    <span class="inline-flex items-center gap-1.5 text-[#22376D]">
                        <span class="w-3 h-3 rounded-full bg-[#22376D]"></span> Seleccionado
                    </span>
                    <span class="text-slate-300">|</span>
                    <span class="inline-flex items-center gap-1.5 text-emerald-700">
                        <span class="w-3 h-3 rounded-full bg-[#16A34A]"></span> Prerrequisito
                    </span>
                    <span class="text-slate-300">|</span>
                    <span class="inline-flex items-center gap-1.5 text-amber-700">
                        <span class="w-3 h-3 rounded-full bg-[#EC9123]"></span> Habilita
                    </span>
                </div>
            </div>

            <!-- Selector de Filtro por Línea Formativa -->
            <div class="flex flex-wrap items-center justify-between gap-3 bg-white p-3.5 rounded-2xl border border-slate-200 shadow-sm">
                <div class="flex items-center gap-2 text-xs font-bold text-slate-700">
                    <i data-lucide="filter" class="w-4 h-4 text-[#EC9123]"></i>
                    <span>Filtrar por Línea de Estudio:</span>
                </div>
                <select id="lineaFilterSelect" onchange="filterMapByLinea(this.value)" class="text-xs font-semibold px-3 py-1.5 rounded-xl border border-slate-200 bg-slate-50 text-[#22376D] focus:ring-2 focus:ring-[#22376D] outline-none">
                    <option value="all">Ver Todas las 4 Líneas Curriculares</option>
                    <option value="linea-etica">🛡️ Formación Humana y Ética</option>
                    <option value="linea-gestion">📋 Gestión y Supervisión Industrial</option>
                    <option value="linea-matematica">📐 Ciencias Matemáticas y Analítica</option>
                    <option value="linea-fisica">⚡ Física y Tecnología Industrial 4.0</option>
                </select>
            </div>

            <!-- LAYOUT PRINCIPAL: MATRIZ CURRICULAR + PANEL DETALLE LATERAL -->
            <div class="grid grid-cols-1 xl:grid-cols-[1fr_320px] gap-5 items-start">
                
                <!-- VISTA MATRIZ REJILLA CURRICULAR COMPACTA (SCROLL HORIZONTAL RESPONSIVO) -->
                <div class="bg-white rounded-2xl border border-slate-200 shadow-sm overflow-x-auto no-scrollbar">
                    
                    <!-- Encabezado de Bimestres: CADA CELDA CON SU FONDO OFICIAL AZUL OSCURO -->
                    <div class="grid grid-cols-[180px_repeat(4,minmax(170px,1fr))] bg-[#152244] text-white text-xs font-bold border-b-2 border-[#EC9123] min-w-[860px]">
                        <div class="p-3 text-left flex items-center bg-[#152244]">
                            <span>Línea Formativa / Eje</span>
                        </div>
                        <div class="p-3 text-center border-l border-white/10 bg-[#152244]">
                            <div class="text-[#EC9123]">Bimestre 1</div>
                            <span class="text-[10px] text-slate-300 font-normal">Fundamentos y Estática</span>
                        </div>
                        <div class="p-3 text-center border-l border-white/10 bg-[#152244]">
                            <div class="text-[#EC9123]">Bimestre 2</div>
                            <span class="text-[10px] text-slate-300 font-normal">Costos, SSO y Materiales</span>
                        </div>
                        <div class="p-3 text-center border-l border-white/10 bg-[#152244]">
                            <div class="text-[#EC9123]">Bimestre 3</div>
                            <span class="text-[10px] text-slate-300 font-normal">Lean, SLAs y Analítica</span>
                        </div>
                        <div class="p-3 text-center border-l border-white/10 bg-[#152244]">
                            <div class="text-[#EC9123]">Bimestre 4</div>
                            <span class="text-[10px] text-slate-300 font-normal">Calidad, BI, Finanzas y Python</span>
                        </div>
                    </div>

                    <!-- Filas Dinámicas de las 4 Líneas de Estudio -->
                    <div class="min-w-[860px] divide-y divide-slate-100">
                        {rows_html}
                    </div>

                </div>

                <!-- PANEL LATERAL DE DETALLE TÉCNICO (STICKY COMPACTO) -->
                <aside id="sideDetailPanel" class="bg-white rounded-2xl border border-slate-200 p-5 shadow-sm sticky top-[135px] space-y-4">
                    
                    <div class="border-b border-slate-100 pb-2.5">
                        <div class="flex items-center justify-between gap-2 mb-1">
                            <span id="sideBadge" class="text-[10px] font-extrabold px-2 py-0.5 rounded-full bg-[#22376D] text-white">
                                B1-C2 • Bimestre 1
                            </span>
                            <span class="text-[10px] font-bold text-[#EC9123]" id="sideHoras">
                                30 Horas
                            </span>
                        </div>
                        <h3 id="sideTitle" class="text-base font-bold brand-serif text-[#22376D] flex items-center gap-1.5">
                            📋 Fundamentos de la Administración
                        </h3>
                        <p id="sideSub" class="text-[11px] text-slate-500 mt-0.5 leading-snug">
                            Liderazgo Ágil de Mandos Medios y Coordinación de Equipos
                        </p>
                    </div>

                    <!-- Prerrequisitos de Entrada -->
                    <div class="space-y-1">
                        <span class="text-[10px] font-bold uppercase tracking-wider text-slate-400 block">
                            ⬅️ Prerrequisitos de Entrada:
                        </span>
                        <ul id="sidePrereqList" class="space-y-1 text-xs">
                            <!-- Inyectado vía JS -->
                        </ul>
                    </div>

                    <!-- Materias que Habilita -->
                    <div class="space-y-1">
                        <span class="text-[10px] font-bold uppercase tracking-wider text-slate-400 block">
                            ➡️ Asignaturas que Habilita:
                        </span>
                        <ul id="sideHabilitaList" class="space-y-1 text-xs">
                            <!-- Inyectado vía JS -->
                        </ul>
                    </div>

                    <!-- Objetivo Formativo -->
                    <div class="space-y-0.5 bg-slate-50 p-2.5 rounded-xl border border-slate-100">
                        <span class="text-[10px] font-bold text-[#22376D] block">
                            🎯 Competencia Clave:
                        </span>
                        <p id="sideObjetivo" class="text-[11px] text-slate-600 leading-relaxed">
                            Dotar al técnico de competencias de supervisión moderna y liderazgo ágil para articular el puente operativo entre la alta gerencia y el personal de piso.
                        </p>
                    </div>

                    <!-- Inteligencia Artificial Aplicada -->
                    <div class="space-y-0.5 bg-purple-50 p-2.5 rounded-xl border border-purple-100">
                        <span class="text-[10px] font-bold text-purple-900 flex items-center gap-1">
                            <i data-lucide="sparkles" class="w-3 h-3 text-purple-600"></i> Integración con IA Aplicada:
                        </span>
                        <p id="sideIA" class="text-[11px] text-purple-950 leading-relaxed">
                            Uso de asistentes de IA generativa (Copilots) para redacción ejecutiva de descriptores de puestos y actas técnicas de reunión.
                        </p>
                    </div>

                    <!-- Herramientas y Metodología -->
                    <div class="space-y-0.5 bg-amber-50/60 p-2.5 rounded-xl border border-amber-100">
                        <span class="text-[10px] font-bold text-amber-900 block">
                            🛠️ Herramientas de Taller & Entorno:
                        </span>
                        <p id="sideHerramientas" class="text-[11px] text-amber-950 leading-relaxed">
                            Matrices RACI, plataformas de documentación (Notion / Confluence), plantillas de feedback 1-on-1, tableros de objetivos SMART.
                        </p>
                    </div>

                </aside>

            </div>

        </section>

        <!-- ===================================================== -->
        <!-- SECCIÓN 2: LAS 4 LÍNEAS CURRICULARES                  -->
        <!-- ===================================================== -->
        <section id="lineas" class="space-y-6 scroll-mt-36">
            
            <div class="border-b-2 border-slate-200 pb-4">
                <span class="text-xs font-bold text-[#EC9123] tracking-widest uppercase">Ejes Transversales Universitarios</span>
                <h2 class="text-2xl sm:text-3xl font-bold brand-serif text-[#22376D] mt-1">
                    Líneas Formativas y Competencias Clave
                </h2>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 gap-5">
                
                <div class="bg-white rounded-2xl border border-slate-200 p-5 shadow-sm space-y-2.5">
                    <div class="flex items-center gap-3">
                        <div class="w-10 h-10 rounded-xl bg-blue-50 text-[#22376D] flex items-center justify-center font-bold">
                            <i data-lucide="briefcase" class="w-5 h-5"></i>
                        </div>
                        <div>
                            <h3 class="font-bold text-base brand-serif text-[#22376D]">Gestión Empresarial y Operaciones</h3>
                            <span class="text-xs text-[#EC9123] font-bold">8 Materias • 240 Horas de Formación</span>
                        </div>
                    </div>
                    <p class="text-xs text-slate-600 leading-relaxed">
                        Desarrolla habilidades directivas, planeación y control de proyectos, cumplimiento de normas de Salud y Seguridad Ocupacional (SSO Acuerdo Gubernativo 229-2014), control de costos, gestión de recursos humanos y calidad ISO 9001.
                    </p>
                </div>

                <div class="bg-white rounded-2xl border border-slate-200 p-5 shadow-sm space-y-2.5">
                    <div class="flex items-center gap-3">
                        <div class="w-10 h-10 rounded-xl bg-emerald-50 text-emerald-700 flex items-center justify-center font-bold">
                            <i data-lucide="calculator" class="w-5 h-5"></i>
                        </div>
                        <div>
                            <h3 class="font-bold text-base brand-serif text-[#22376D]">Ciencias Matemáticas Aplicadas</h3>
                            <span class="text-xs text-[#EC9123] font-bold">4 Materias • 120 Horas de Formación</span>
                        </div>
                    </div>
                    <p class="text-xs text-slate-600 leading-relaxed">
                        Modelado cuantitativo, trigonometría técnica, cálculo diferencial e integral enfocado a la resolución de problemas en ingeniería y procesos de manufactura industrial.
                    </p>
                </div>

                <div class="bg-white rounded-2xl border border-slate-200 p-5 shadow-sm space-y-2.5">
                    <div class="flex items-center gap-3">
                        <div class="w-10 h-10 rounded-xl bg-amber-50 text-amber-700 flex items-center justify-center font-bold">
                            <i data-lucide="activity" class="w-5 h-5"></i>
                        </div>
                        <div>
                            <h3 class="font-bold text-base brand-serif text-[#22376D]">Física Técnica e Industrial</h3>
                            <span class="text-xs text-[#EC9123] font-bold">4 Materias • 120 Horas de Formación</span>
                        </div>
                    </div>
                    <p class="text-xs text-slate-600 leading-relaxed">
                        Análisis estático y dinámico, cinemática de mecanismos, termodinámica de fluidos y recipientes de presión, y fundamentos de electromagnetismo aplicados a la automatización.
                    </p>
                </div>

                <div class="bg-white rounded-2xl border border-slate-200 p-5 shadow-sm space-y-2.5">
                    <div class="flex items-center gap-3">
                        <div class="w-10 h-10 rounded-xl bg-purple-50 text-purple-700 flex items-center justify-center font-bold">
                            <i data-lucide="scale" class="w-5 h-5"></i>
                        </div>
                        <div>
                            <h3 class="font-bold text-base brand-serif text-[#22376D]">Ética y Deontología Profesional</h3>
                            <span class="text-xs text-[#EC9123] font-bold">4 Materias • 120 Horas de Formación</span>
                        </div>
                    </div>
                    <p class="text-xs text-slate-600 leading-relaxed">
                        Formación antropológica, discernimiento moral cristiano, ética en los negocios, lealtad profesional, servicio a la sociedad y el principio institucional del <em>«Trabajo bien hecho»</em>.
                    </p>
                </div>

            </div>

        </section>

    </main>

    <!-- ========================================================= -->
    <!-- FOOTER INSTITUCIONAL (SOLO LOGO BLANCO FUNDACIÓN KINAL)   -->
    <!-- ========================================================= -->
    <footer class="bg-[#0D162C] text-white border-t-4 border-[#EC9123] py-12 px-4 sm:px-6 lg:px-8 mt-12">
        <div class="max-w-7xl mx-auto space-y-8">
            <div class="flex flex-col md:flex-row justify-between items-start md:items-center gap-6 border-b border-slate-800 pb-8">
                <div class="flex items-center gap-4">
                    <img src="assets/fundacion_kinal_blanco.png" alt="Fundación Kinal" class="h-10 sm:h-12 w-auto object-contain">
                </div>
                <div class="text-xs text-slate-400 max-w-md text-left md:text-right">
                    <strong class="text-white block mb-0.5">Fundación Kinal — Escuela Técnica Superior (ETS)</strong>
                    Programa de Técnico Superior Universitario (TSU) con aval de la Universidad del Istmo (UNIS).
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

    <!-- Lógica Interactiva de Resaltado de Prerrequisitos y Dependencias -->
    <script>
        lucide.createIcons();

        const cursosData = {json.dumps(cursos_data, ensure_ascii=False)};
        let selectedCourseId = "b1_fundamentos_administracion";

        function filterMapByLinea(lineaId) {{
            const rows = document.querySelectorAll('.grid-linea-row');
            rows.forEach(r => {{
                if (lineaId === 'all' || r.id === 'row-' + lineaId) {{
                    r.style.display = 'grid';
                }} else {{
                    r.style.display = 'none';
                }}
            }});
        }}

        function selectCourseNode(courseId) {{
            selectedCourseId = courseId;
            renderActiveRuta(courseId);
            updateSidePanel(courseId);
        }}

        function highlightNodeRuta(courseId) {{
            renderActiveRuta(courseId);
        }}

        function clearHighlightNode() {{
            renderActiveRuta(selectedCourseId);
        }}

        function renderActiveRuta(courseId) {{
            const course = cursosData[courseId];
            if (!course) return;

            const allNodes = document.querySelectorAll('.node-card');
            allNodes.forEach(node => {{
                node.classList.remove('selected', 'prereq-active', 'habilita-active', 'dimmed');
                const nId = node.getAttribute('data-id');
                if (nId === courseId) {{
                    node.classList.add('selected');
                }} else if (course.prerequisitos.includes(nId)) {{
                    node.classList.add('prereq-active');
                }} else if (course.habilita.includes(nId)) {{
                    node.classList.add('habilita-active');
                }} else {{
                    node.classList.add('dimmed');
                }}
            }});
        }}

        function updateSidePanel(courseId) {{
            const course = cursosData[courseId];
            if (!course) return;

            document.getElementById('sideBadge').innerText = course.codigo + ' • ' + course.bimestre;
            document.getElementById('sideHoras').innerText = course.horas;
            document.getElementById('sideTitle').innerHTML = course.icono + ' ' + course.nombre;
            document.getElementById('sideSub').innerText = course.subtitulo;
            document.getElementById('sideObjetivo').innerText = course.objetivo;
            document.getElementById('sideIA').innerText = course.subtema_ia;
            document.getElementById('sideHerramientas').innerText = course.herramientas;

            // Prerrequisitos list
            const prereqList = document.getElementById('sidePrereqList');
            prereqList.innerHTML = '';
            if (course.prerequisitos.length > 0) {{
                course.prerequisitos.forEach(pId => {{
                    const pInfo = cursosData[pId];
                    const li = document.createElement('li');
                    li.className = 'p-1.5 rounded-lg bg-emerald-50 text-emerald-800 border border-emerald-200 cursor-pointer hover:bg-emerald-100 transition flex items-center justify-between text-[11px]';
                    li.innerHTML = '<span>⬅️ ' + pInfo.codigo + ' • ' + pInfo.nombre + '</span><span class="text-[9px] text-emerald-600 font-bold">Ver</span>';
                    li.onclick = () => selectCourseNode(pId);
                    prereqList.appendChild(li);
                }});
            }} else {{
                const li = document.createElement('li');
                li.className = 'p-1.5 rounded-lg bg-slate-50 text-slate-500 border border-slate-200 text-[11px]';
                li.innerText = 'Ingreso al 3er Año TSU (Sin prerrequisito previo)';
                prereqList.appendChild(li);
            }}

            // Habilita list
            const habilitaList = document.getElementById('sideHabilitaList');
            habilitaList.innerHTML = '';
            if (course.habilita.length > 0) {{
                course.habilita.forEach(hId => {{
                    const hInfo = cursosData[hId];
                    const li = document.createElement('li');
                    li.className = 'p-1.5 rounded-lg bg-amber-50 text-amber-800 border border-amber-200 cursor-pointer hover:bg-amber-100 transition flex items-center justify-between text-[11px]';
                    li.innerHTML = '<span>➡️ ' + hInfo.codigo + ' • ' + hInfo.nombre + '</span><span class="text-[9px] text-amber-600 font-bold">Ver</span>';
                    li.onclick = () => selectCourseNode(hId);
                    habilitaList.appendChild(li);
                }});
            }} else {{
                const li = document.createElement('li');
                li.className = 'p-1.5 rounded-lg bg-amber-50/70 text-amber-900 border border-amber-200 font-semibold text-[11px]';
                li.innerText = 'Culminación del Plan / Graduación TSU';
                habilitaList.appendChild(li);
            }}
        }}

        document.addEventListener('DOMContentLoaded', () => {{
            selectCourseNode('b1_fundamentos_administracion');
        }});
    </script>
</body>
</html>
"""

with open("tsu.html", "w", encoding="utf-8") as f:
    f.write(tsu_html)

print("tsu.html regenerated successfully.")
