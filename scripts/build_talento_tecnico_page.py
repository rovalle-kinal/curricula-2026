import os
import re
import html
import docx
import json

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CURSOS_DIR = os.path.join(WORKSPACE_DIR, "Cursos")
TALENTO_DIR = os.path.join(CURSOS_DIR, "Talento_Tecnico")

def clean_html(text):
    if not text:
        return ""
    return html.escape(text).replace('\n', '<br>')

# 1. Parsear los 3 archivos Word
prop_doc = docx.Document(os.path.join(TALENTO_DIR, "Propuesta_Diplomado_Talento_Tecnico_Kinal.docx"))
tem_doc = docx.Document(os.path.join(TALENTO_DIR, "Temario_Diplomado_Talento_Tecnico_Kinal.docx"))
dos_doc = docx.Document(os.path.join(TALENTO_DIR, "Dosificacion_y_Secuencia_Didactica_Talento_Tecnico_Kinal.docx"))

# Ficha técnica
ficha_rows = []
for r in prop_doc.tables[0].rows:
    ficha_rows.append([c.text.strip() for c in r.cells])

# Módulos de la propuesta
modulos_prop_rows = []
for r in prop_doc.tables[5].rows[1:]:
    modulos_prop_rows.append([c.text.strip() for c in r.cells])

# Componentes de evaluación
eval_prop_rows = []
for r in prop_doc.tables[7].rows[1:]:
    eval_prop_rows.append([c.text.strip() for c in r.cells])

# Dosificación cronológica (Tabla 1)
cron_rows = []
for r in dos_doc.tables[1].rows[1:]:
    cron_rows.append([c.text.strip() for c in r.cells])

# 12 Sesiones didácticas (Tablas 2 a 13)
sessions = []
for idx in range(2, 14):
    t = dos_doc.tables[idx]
    s_num = idx - 1
    t1_row = cron_rows[s_num - 1] if (s_num - 1) < len(cron_rows) else ["", "", "", ""]
    
    # Rows in session table:
    # R0: Módulo y Duración
    # R1: Objetivo Específico
    # R2: Apertura
    # R3: Desarrollo
    # R4: Cierre
    # R5: Recursos y Plataformas
    # R6: Entregable y Evidencia
    mod_dur = t.rows[0].cells[1].text.strip()
    obj = t.rows[1].cells[1].text.strip()
    ap = t.rows[2].cells[1].text.strip()
    des = t.rows[3].cells[1].text.strip()
    cie = t.rows[4].cells[1].text.strip()
    eq = t.rows[5].cells[1].text.strip()
    evi = t.rows[6].cells[1].text.strip()
    
    mod_name = t1_row[1] if len(t1_row) > 1 else f"Módulo {((s_num-1)//3)+1}"
    title_short = t1_row[2] if len(t1_row) > 2 else f"Sesión {s_num}"
    prod_obs = t1_row[3] if len(t1_row) > 3 else evi
    
    mod_num = ((s_num - 1) // 3) + 1
    ses_in_mod = ((s_num - 1) % 3) + 1
    
    semana_str = f"Semana {mod_num}"
    if ses_in_mod == 1:
        tipo_str = "Virtual Teams (Martes 19:00 - 21:00)"
        dur_str = "2 Horas (120 min)"
    elif ses_in_mod == 2:
        tipo_str = "Virtual Teams (Jueves 19:00 - 21:00)"
        dur_str = "2 Horas (120 min)"
    else:
        tipo_str = f"Presencial Campus Kinal (Sábado {mod_num} Consecutivo 8:00 - 12:00)"
        dur_str = "4 Horas (240 min)"

    sessions.append({
        "num": s_num,
        "code": f"S-{s_num:02d}",
        "mod_num": mod_num,
        "module": mod_name,
        "title": title_short,
        "duration": dur_str,
        "tipo": tipo_str,
        "semana": semana_str,
        "objective": obj,
        "apertura": ap,
        "desarrollo": des,
        "cierre": cie,
        "evidencias": evi,
        "equipamiento": eq,
        "producto_obs": prod_obs
    })

# Rúbrica analítica (Tabla 15 de dosificación)
rubrica_rows = []
for r in dos_doc.tables[15].rows[1:]:
    rubrica_rows.append([c.text.strip() for c in r.cells])

# Temario analítico detallado
temario_modules = [
    {
        "num": 1,
        "semana": "Semana 1",
        "title": "La Brecha del Talento Operativo y el Retorno de Inversión del TSU",
        "hours": "8 Horas Directas (4h Virtual Teams + 4h Sábado 1 Kinal)",
        "logro": "Analizar la estructura del empleo técnico industrial guatemalteco, contrastar la baja productividad del operario empírico frente a la solvencia del Técnico Superior Universitario (TSU) y formular un caso de negocio de retorno de inversión (ROI) que justifique la profesionalización de cuadrillas técnicas.",
        "topics": [
            {
                "num": 1,
                "title": "Radiografía del Empleo Técnico en Guatemala y el 'Síndrome del Operador Empírico'",
                "cat": "diagnostico",
                "cat_name": "📊 Diagnóstico & Brechas",
                "cat_badge": "bg-blue-100 text-blue-900 border border-blue-200",
                "desc": "Causas estructurales de la escasez de técnicos calificados en la industria manufacturera, automotriz, eléctrica y constructiva en Guatemala. La trampa del 'aprender sobre la marcha' sin fundamentación técnica: sobrecostos por reprocesos, rotura de maquinaria, accidentes de trabajo y dependencia crítica de mandos medios no formados."
            },
            {
                "num": 2,
                "title": "El Técnico Superior Universitario (TSU) y el Marco Alemán DQR (Nivel 5 - 6)",
                "cat": "competencias",
                "cat_name": "🎯 Competencias DQR",
                "cat_badge": "bg-purple-100 text-purple-900 border border-purple-200",
                "desc": "Definición oficial DQR: capacidad y disposición para actuar integralmente con solvencia técnica, social y metodológica. Mapeo del perfil del TSU egresado de Kinal: rigor matemático aplicado, metrología de precisión, lectura de planos normalizados, normativas internacionales y disciplina operativa frente a la intuición empírica."
            },
            {
                "num": 3,
                "title": "Taller Vivencial e Inmersión de Planta: El Contraste de Competencias (Sábado 1)",
                "cat": "inmersion",
                "cat_name": "🏭 Inmersión Presencial Kinal",
                "cat_badge": "bg-amber-100 text-amber-900 border border-amber-200",
                "desc": "Visita ejecutiva a talleres y laboratorios de alta tecnología de Fundación Kinal (CNC, Automatización Siemens, Redes, Sistemas Automotrices y Construcción). Observación directa de proyectos reales de graduación de aprendices de TSU. Taller de cálculo financiero: Costos Ocultos de la No Calidad (CONC) y modelo cuantitativo de Retorno de Inversión (ROI)."
            }
        ]
    },
    {
        "num": 2,
        "semana": "Semana 2",
        "title": "Reclutamiento por Competencias Técnicas y Sistemas de Formación Dual",
        "hours": "8 Horas Directas (4h Virtual Teams + 4h Sábado 2 Kinal)",
        "logro": "Diseñar e implementar procesos de selección técnica basados en evidencias prácticas y entrevistas conductuales (STAR), y formular un esquema de Semillero de Formación Dual en alternancia empresa-escuela que garantice el relevo generacional y reduzca la curva de aprendizaje en planta.",
        "topics": [
            {
                "num": 4,
                "title": "Reingeniería del Perfil de Puesto Técnico hacia Competencias Demostrables",
                "cat": "seleccion",
                "cat_name": "📋 Selección Técnica",
                "cat_badge": "bg-emerald-100 text-emerald-900 border border-emerald-200",
                "desc": "Superación de los perfiles genéricos tradicionales. Definición de la Matriz de Competencias Operativas: Conocimientos Técnicos DQR, Habilidades Manuales y Metrológicas, y Competencias Metodológicas. Criterios de evaluación técnica objetiva en taller sin sesgos subjetivos."
            },
            {
                "num": 5,
                "title": "Entrevistas Situacionales (STAR) y el Sistema Dual en Alternancia",
                "cat": "dual",
                "cat_name": "🔄 Sistema Dual en Alternancia",
                "cat_badge": "bg-blue-100 text-blue-900 border border-blue-200",
                "desc": "Estructuración de preguntas técnicas basadas en el método STAR (Situación, Tarea, Acción, Resultado). El modelo dual de alternancia Kinal: el aprender en el proceso del trabajo como base y objetivo de la acción formativa. Roles del Tutor de Empresa y Mentor Técnico de Taller."
            },
            {
                "num": 6,
                "title": "Laboratorio de Selección Técnica y Evaluación Práctica en Taller Kinal (Sábado 2)",
                "cat": "inmersion",
                "cat_name": "🏭 Inmersión Presencial Kinal",
                "cat_badge": "bg-amber-100 text-amber-900 border border-amber-200",
                "desc": "Simulación en vivo de entrevistas técnicas a aprendices de TSU de último año en el campus Kinal. Aplicación de pruebas de habilidad en laboratorio con uso de instrumentos de medición y rúbricas de calibración. Diseño del Plan Corporativo de Semillero Dual adaptado a las plantas de los gerentes."
            }
        ]
    },
    {
        "num": 3,
        "semana": "Semana 3",
        "title": "Cultura del 'Factor Humano': Valores Laicos, Dignidad y Clima Operativo",
        "hours": "8 Horas Directas (4h Virtual Teams + 4h Sábado 3 Kinal)",
        "logro": "Desplegar el modelo del Factor Humano de Fundación Kinal como un sistema formativo basado en valores laicos universales, erradicando el maltrato en planta, previniendo la rotación prematura y fomentando el orgullo del oficio y el estándar del «trabajo bien hecho».",
        "topics": [
            {
                "num": 7,
                "title": "Antropología del Factor Humano en Kinal y los Cuatro Pilares del Clima Operativo",
                "cat": "factor_humano",
                "cat_name": "⭐ Factor Humano Kinal",
                "cat_badge": "bg-amber-100 text-amber-900 border border-amber-200",
                "desc": "El Factor Humano en Kinal como formación de virtudes humanas en el trabajo. Traducción empresarial: Respeto estricto a la dignidad del operario, Espíritu de servicio hacia el compañero de cuadrilla, Libertad personal responsable y El trabajo bien hecho como realización personal y fuente de prestigio laboral."
            },
            {
                "num": 8,
                "title": "Liderazgo en Cuadrillas, Seguridad Psicológica y Comunicación Directa",
                "cat": "liderazgo",
                "cat_name": "👥 Liderazgo Operativo",
                "cat_badge": "bg-indigo-100 text-indigo-900 border border-indigo-200",
                "desc": "Desmontando la cultura del capataz intimidatorio y el maltrato verbal en planta. Creación de entornos de seguridad psicológica para reportar errores técnicos y casi-accidentes sin temor a represalias destructivas. Canales formales de escucha y resolución ética de controversias operativas."
            },
            {
                "num": 9,
                "title": "Clínica Vivencial: Dinámicas de Piso de Planta y el «Trabajo Bien Hecho» (Sábado 3)",
                "cat": "inmersion",
                "cat_name": "🏭 Inmersión Presencial Kinal",
                "cat_badge": "bg-amber-100 text-amber-900 border border-amber-200",
                "desc": "Taller interactivo de resolución de dilemas éticos y operativos en planta mediante role-playing directivo. Conversatorio con instructores y capataces experimentados de Kinal sobre disciplina positiva y mentoría. Diseño del Protocolo Corporativo de Cero Tolerancia al Maltrato y Charla de Factor Humano de 10 Minutos."
            }
        ]
    },
    {
        "num": 4,
        "semana": "Semana 4",
        "title": "Taller Directivo Capstone: Creación y Defensa del Programa Corporativo",
        "hours": "8 Horas Directas (4h Virtual Teams + 4h Sábado 4 Kinal)",
        "logro": "Formular, estructurar y defender ante un tribunal evaluador directivo un Plan Integral de Gestión Estratégica del Talento Técnico y Factor Humano, articulando el caso de negocio del TSU, la estrategia de atracción dual y el protocolo de cultura de planta con métricas de retorno de inversión.",
        "topics": [
            {
                "num": 10,
                "title": "Metodología de Despliegue Corporativo e Integración del Factor Humano",
                "cat": "capstone",
                "cat_name": "🚀 Proyecto Capstone",
                "cat_badge": "bg-purple-100 text-purple-900 border border-purple-200",
                "desc": "Estructura del Proyecto Directivo Capstone: Diagnóstico de la Brecha Operativa en la Empresa, Matriz de Selección por Competencias Demostrables, Plan de Alianza Dual con Kinal y Protocolo de Despliegue del Factor Humano. Cronograma de implantación a 90 y 180 días con matriz de gestión del cambio."
            },
            {
                "num": 11,
                "title": "Cuadro de Mando Integral (KPIs), Alianzas Kinal y Preparación de la Defensa",
                "cat": "metricas",
                "cat_name": "📈 Métricas de Retorno (KPIs)",
                "cat_badge": "bg-emerald-100 text-emerald-900 border border-emerald-200",
                "desc": "Definición de indicadores de impacto operativo: reducción de tasa de rotación en cuadrillas (Turnover), incremento de OEE (Overall Equipment Effectiveness), disminución de costos por garantías y reprocesos, e índice de clima laboral en planta. Simulación de defensa ejecutiva con retroalimentación personalizada."
            },
            {
                "num": 12,
                "title": "Defensa Directiva Capstone ante el Tribunal de Kinal y Clausura (Sábado 4)",
                "cat": "inmersion",
                "cat_name": "🎓 Defensa & Certificación Kinal",
                "cat_badge": "bg-amber-100 text-amber-900 border border-amber-200",
                "desc": "Sustentación formal de 15 minutos por participante del Plan Integral ante el Tribunal Directivo de la Escuela Técnica Superior de Fundación Kinal. Deliberación, evaluación bajo rúbrica institucional (aprobación >= 75 puntos) y entrega formal de Certificados Ejecutivos en acto de clausura."
            }
        ]
    }
]

# Construir el HTML
sessions_json = json.dumps(sessions, ensure_ascii=False)

html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Diplomado Gerencial en Gestión del Talento Técnico | Escuela Técnica Superior Kinal</title>
    
    <!-- Favicon Oficial Escudo Proporcional Cuadrado -->
    <link rel="icon" type="image/png" href="assets/escudo_kinal_cuadrado.png">
    
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        body {{
            font-family: Arial, Helvetica, sans-serif;
            background-color: #F8FAFC;
            color: #0F172A;
        }}
        h1, h2, h3, h4, h5, .brand-serif {{
            font-family: 'Times New Roman', Times, serif;
        }}
        .hero-kinal-gradient {{
            background: linear-gradient(135deg, #0D162C 0%, #152244 45%, #22376D 100%);
        }}
        .card-hover {{
            transition: all 0.25s ease-in-out;
        }}
        .card-hover:hover {{
            transform: translateY(-4px);
            box-shadow: 0 16px 28px -6px rgba(34, 55, 109, 0.15), 0 8px 12px -4px rgba(34, 55, 109, 0.08);
        }}
        .tab-btn.active {{
            background-color: #22376D !important;
            color: #FFFFFF !important;
            border-color: #22376D !important;
            box-shadow: 0 4px 6px -1px rgba(34, 55, 109, 0.2);
        }}
        .session-item.active {{
            border-left: 4px solid #EC9123 !important;
            background-color: #F0FDF4 !important;
        }}
        @media (max-width: 767px) {{
            *, *::before, *::after {{ box-sizing: border-box !important; }}
            html, body {{ overflow-x: hidden !important; max-width: 100vw !important; }}
            .no-scrollbar::-webkit-scrollbar {{ display: none !important; }}
            .no-scrollbar {{ -ms-overflow-style: none !important; scrollbar-width: none !important; }}
        }}
    </style>
    <script src="assets/auth_gatekeeper.js"></script>
</head>
<body class="min-h-screen flex flex-col antialiased pt-[115px] sm:pt-[125px]">

    <!-- ========================================================= -->
    <!-- ENCABEZADO FIJO PERMANENTE UNIFICADO                      -->
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

        <!-- HEADER CORPORATIVO (LOGO ETS & BOTONES DE NAVEGACIÓN PRINCIPAL) -->
        <header class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-2 sm:py-2.5 flex flex-wrap justify-between items-center gap-3 border-b border-slate-100">
            <div class="flex items-center">
                <a href="index.html" class="flex items-center group">
                    <img src="assets/escuela_tecnica_superior.png" alt="Escuela Técnica Superior" class="h-8 sm:h-9 w-auto object-contain transition group-hover:opacity-90">
                </a>
            </div>

            <!-- Botones Principales: Inicio y Vuelta a Cursos Nuevos -->
            <nav class="flex items-center gap-2 sm:gap-3 text-xs font-bold">
                <a href="cursos_nuevos.html" class="px-3.5 py-2 rounded-lg bg-white hover:bg-slate-50 text-[#22376D] transition flex items-center gap-1.5 shadow-sm whitespace-nowrap border border-slate-200" title="Volver al catálogo de cursos nuevos">
                    <i data-lucide="arrow-left" class="w-4 h-4 text-[#EC9123]"></i> Nuevos
                </a>
                <a href="index.html" class="px-3.5 py-2 rounded-lg bg-white hover:bg-slate-50 text-[#22376D] transition flex items-center gap-1.5 shadow-sm whitespace-nowrap border border-slate-200">
                    <i data-lucide="home" class="w-4 h-4 text-[#EC9123]"></i>
                </a>
            </nav>
        </header>

        <!-- SUB-BARRA INTEGRADA DE PESTAÑAS DEL CURSO (UNIFICADA CON EL ENCABEZADO) -->
        <div class="bg-slate-50 border-t border-slate-200">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                <nav class="flex space-x-2 py-2 overflow-x-auto no-scrollbar text-xs font-bold">
                    <button onclick="switchTab('propuesta')" id="btn-propuesta" class="tab-btn active px-3.5 py-1.5 rounded-lg transition flex items-center gap-1.5 shrink-0">
                        <i data-lucide="file-text" class="w-3.5 h-3.5"></i> Propuesta
                    </button>
                    <button onclick="switchTab('temario')" id="btn-temario" class="tab-btn px-3.5 py-1.5 rounded-lg bg-white hover:bg-slate-100 text-slate-700 border border-slate-200 transition flex items-center gap-1.5 shrink-0">
                        <i data-lucide="list-tree" class="w-3.5 h-3.5"></i> Temario
                    </button>
                    <button onclick="switchTab('calendario')" id="btn-calendario" class="tab-btn px-3.5 py-1.5 rounded-lg bg-white hover:bg-slate-100 text-slate-700 border border-slate-200 transition flex items-center gap-1.5 shrink-0">
                        <i data-lucide="calendar" class="w-3.5 h-3.5"></i> Calendario
                    </button>
                    <button onclick="switchTab('secuencias')" id="btn-secuencias" class="tab-btn px-3.5 py-1.5 rounded-lg bg-white hover:bg-slate-100 text-slate-700 border border-slate-200 transition flex items-center gap-1.5 shrink-0">
                        <i data-lucide="layers" class="w-3.5 h-3.5"></i> Secuencias
                    </button>
                    <button onclick="switchTab('evaluacion')" id="btn-evaluacion" class="tab-btn px-3.5 py-1.5 rounded-lg bg-white hover:bg-slate-100 text-slate-700 border border-slate-200 transition flex items-center gap-1.5 shrink-0">
                        <i data-lucide="award" class="w-3.5 h-3.5"></i> Evaluación
                    </button>
                </nav>
            </div>
        </div>

    </div>

    <!-- Hero Course Banner -->
    <section class="hero-kinal-gradient relative overflow-hidden text-white py-10 px-4 sm:px-6 lg:px-8">
        <div class="max-w-7xl mx-auto space-y-3">
            <div class="flex flex-wrap items-center gap-2">
                <span class="px-3 py-1 rounded-full bg-amber-500/20 border border-amber-400/30 text-amber-300 text-xs font-bold tracking-wide uppercase">
                    ⭐ Programa Ejecutivo Híbrido (4 Semanas Intensivas)
                </span>
                <span class="px-3 py-1 rounded-full bg-blue-500/20 border border-blue-400/30 text-blue-300 text-xs font-bold">
                    DQR Nivel 6 - 7
                </span>
                <span class="px-3 py-1 rounded-full bg-emerald-500/20 border border-emerald-400/30 text-emerald-300 text-xs font-bold">
                    Aprobación: ≥ 75 Pts
                </span>
            </div>
            <h1 class="text-2xl sm:text-4xl font-black tracking-tight leading-tight brand-serif">
                Diplomado de Certificación Gerencial en Gestión Estratégica del Talento Técnico
            </h1>
            <p class="text-slate-300 text-xs sm:text-sm max-w-4xl leading-relaxed">
                Capitalizando el Valor del Técnico Superior Universitario (TSU), la Formación Dual en Alternancia Empresa-Escuela y la Cultura del Factor Humano en la Industria Guatemalteca.
            </p>
            <div class="pt-2 flex flex-wrap gap-4 text-xs text-slate-200">
                <span class="flex items-center gap-1.5">
                    <i data-lucide="clock" class="w-4 h-4 text-[#EC9123]"></i> 32 Horas Directas + 8h Proyecto Capstone
                </span>
                <span class="flex items-center gap-1.5">
                    <i data-lucide="video" class="w-4 h-4 text-[#EC9123]"></i> 8 Sesiones Virtuales (Teams)
                </span>
                <span class="flex items-center gap-1.5">
                    <i data-lucide="map-pin" class="w-4 h-4 text-[#EC9123]"></i> 4 Talleres de Sábado en Campus Kinal
                </span>
            </div>
        </div>
    </section>

    <!-- Main Container -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 flex-1 space-y-8">

        <!-- ================================================================== -->
        <!-- PESTAÑA 1: PROPUESTA -->
        <!-- ================================================================== -->
        <div id="tab-propuesta" class="tab-content space-y-8">
            
            <!-- Ficha Técnica -->
            <div class="bg-white rounded-3xl border border-slate-200 p-6 sm:p-8 shadow-sm space-y-5">
                <div class="flex flex-wrap items-center justify-between border-b border-slate-200 pb-4 gap-2">
                    <div class="flex items-center gap-2">
                        <span class="w-8 h-8 rounded-lg bg-amber-50 text-amber-900 flex items-center justify-center font-black">
                            <i data-lucide="file-badge" class="w-4 h-4 text-[#EC9123]"></i>
                        </span>
                        <h3 class="text-xl font-black text-slate-900">
                            Ficha Técnica Oficial del Programa
                        </h3>
                    </div>
                    <span class="px-3 py-1 rounded-full bg-amber-50 text-amber-900 text-xs font-bold border border-amber-200">
                        Código: TALENTO-GERENCIAL-2026
                    </span>
                </div>
                <div class="divide-y divide-slate-100">
                    <div class="py-3 sm:grid sm:grid-cols-3 sm:gap-4 flex flex-col">
                        <dt class="font-bold text-slate-900 text-xs sm:col-span-1">Nivel Formativo de Referencia:</dt>
                        <dd class="text-slate-700 text-xs sm:col-span-2 mt-0.5 sm:mt-0 leading-relaxed">Equivalencia DQR Nivel 6 - 7 (Dirección estratégica de talento, diseño organizacional y liderazgo)</dd>
                    </div>
                    <div class="py-3 sm:grid sm:grid-cols-3 sm:gap-4 flex flex-col">
                        <dt class="font-bold text-slate-900 text-xs sm:col-span-1">Población Destinataria:</dt>
                        <dd class="text-slate-700 text-xs sm:col-span-2 mt-0.5 sm:mt-0 leading-relaxed">Gerentes Generales, Gerentes de Talento Humano / RRHH, Reclutadores Técnicos y Gerentes de Operaciones / Planta.</dd>
                    </div>
                    <div class="py-3 sm:grid sm:grid-cols-3 sm:gap-4 flex flex-col">
                        <dt class="font-bold text-slate-900 text-xs sm:col-span-1">Duración Total:</dt>
                        <dd class="text-slate-700 text-xs sm:col-span-2 mt-0.5 sm:mt-0 leading-relaxed">32 horas directas sincrónicas/presenciales (40 horas formativas totales en 4 semanas continuas con Proyecto Capstone)</dd>
                    </div>
                    <div class="py-3 sm:grid sm:grid-cols-3 sm:gap-4 flex flex-col">
                        <dt class="font-bold text-slate-900 text-xs sm:col-span-1">Modalidad Híbrida Ejecutiva:</dt>
                        <dd class="text-slate-700 text-xs sm:col-span-2 mt-0.5 sm:mt-0 leading-relaxed">16h Virtual Sincrónico (Microsoft Teams) + 16h Presencial Inmersivo (4 Sábados consecutivos en Campus Kinal)</dd>
                    </div>
                    <div class="py-3 sm:grid sm:grid-cols-3 sm:gap-4 flex flex-col">
                        <dt class="font-bold text-slate-900 text-xs sm:col-span-1">Estructura de Horarios:</dt>
                        <dd class="text-slate-700 text-xs sm:col-span-2 mt-0.5 sm:mt-0 leading-relaxed">Martes y Jueves (19:00 a 21:00 hrs en Teams) y 4 Sábados consecutivos (8:00 a 12:00 hrs en Kinal)</dd>
                    </div>
                    <div class="py-3 sm:grid sm:grid-cols-3 sm:gap-4 flex flex-col">
                        <dt class="font-bold text-slate-900 text-xs sm:col-span-1">Nota Mínima Aprobatoria:</dt>
                        <dd class="text-slate-700 text-xs sm:col-span-2 mt-0.5 sm:mt-0 leading-relaxed">75 puntos sobre 100 en análisis de casos, auditoría de competencias y Proyecto Directivo Capstone</dd>
                    </div>
                    <div class="py-3 sm:grid sm:grid-cols-3 sm:gap-4 flex flex-col">
                        <dt class="font-bold text-slate-900 text-xs sm:col-span-1">Sede Presencial:</dt>
                        <dd class="text-slate-700 text-xs sm:col-span-2 mt-0.5 sm:mt-0 leading-relaxed">Fundación Kinal — Auditorio Ejecutivo y Complejo de Talleres y Laboratorios TSU, Zona 7, Ciudad de Guatemala</dd>
                    </div>
                </div>
            </div>

            <!-- Fundamentación y Competencia -->
            <div class="grid md:grid-cols-2 gap-8">
                <div class="bg-white rounded-3xl border border-slate-200 p-6 sm:p-8 shadow-sm space-y-4">
                    <h3 class="text-lg font-black text-slate-900 brand-serif flex items-center gap-2">
                        <i data-lucide="compass" class="w-5 h-5 text-[#EC9123]"></i> Fundamentación Estratégica: El Retorno de Inversión del TSU
                    </h3>
                    <p class="text-xs text-slate-600 leading-relaxed">
                        La industria guatemalteca gasta sumas millonarias en maquinaria de última generación pero continúa contratando operarios empíricos sin fundamentación técnica. Esto produce paradas imprevistas, mermas críticas, rotación masiva y dependencia de mandos medios.
                    </p>
                    <p class="text-xs text-slate-600 leading-relaxed">
                        El <strong>Técnico Superior Universitario (TSU)</strong> cierra esta brecha con rigor metrológico, diagnóstico estructurado y autonomía operativa DQR 5-6, generando un retorno financiero inmediato comprobable en planta.
                    </p>
                </div>

                <div class="bg-white rounded-3xl border border-slate-200 p-6 sm:p-8 shadow-sm space-y-4">
                    <h3 class="text-lg font-black text-slate-900 brand-serif flex items-center gap-2">
                        <i data-lucide="heart-handshake" class="w-5 h-5 text-[#EC9123]"></i> El Factor Humano: Cultura de Planta y «Trabajo Bien Hecho»
                    </h3>
                    <p class="text-xs text-slate-600 leading-relaxed">
                        En Kinal, el <strong>Factor Humano</strong> no es una charla pasajera: es una disciplina formativa basada en virtudes universales que erradica el capataz intimidatorio y el maltrato en planta.
                    </p>
                    <p class="text-xs text-slate-600 leading-relaxed">
                        Los gerentes aprenderán a implementar entornos de seguridad psicológica, dignidad de la persona, fidelización de cuadrillas operativas y el estándar del <em>«trabajo bien hecho»</em> como ventaja competitiva.
                    </p>
                </div>
            </div>

            <!-- Estructura Modular Resumen -->
            <div class="bg-white rounded-3xl border border-slate-200 p-6 sm:p-8 shadow-sm space-y-6">
                <h3 class="text-lg font-black text-slate-900 brand-serif flex items-center gap-2 border-b border-slate-200 pb-3">
                    <i data-lucide="layers" class="w-5 h-5 text-[#22376D]"></i> Estructura Curricular Modular (4 Semanas Consecutivas)
                </h3>
                <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-4">
                    <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
                        <span class="px-2.5 py-0.5 rounded-full bg-blue-100 text-blue-900 text-[10px] font-black uppercase">Semana 1 • 8h</span>
                        <h4 class="font-bold text-sm text-slate-900 leading-snug">Brecha del TSU y Retorno de Inversión</h4>
                        <p class="text-xs text-slate-600">Radiografía del talento técnico empírico y caso de negocio cuantitativo del TSU.</p>
                    </div>
                    <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
                        <span class="px-2.5 py-0.5 rounded-full bg-emerald-100 text-emerald-900 text-[10px] font-black uppercase">Semana 2 • 8h</span>
                        <h4 class="font-bold text-sm text-slate-900 leading-snug">Reclutamiento por Competencias & Modelo Dual</h4>
                        <p class="text-xs text-slate-600">Perfiles DQR, entrevistas STAR y diseño de semillero dual empresa-escuela.</p>
                    </div>
                    <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
                        <span class="px-2.5 py-0.5 rounded-full bg-amber-100 text-amber-900 text-[10px] font-black uppercase">Semana 3 • 8h</span>
                        <h4 class="font-bold text-sm text-slate-900 leading-snug">Cultura del Factor Humano en Planta</h4>
                        <p class="text-xs text-slate-600">Erradicación del maltrato, dignidad personal, liderazgo y charlas operativas.</p>
                    </div>
                    <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
                        <span class="px-2.5 py-0.5 rounded-full bg-purple-100 text-purple-900 text-[10px] font-black uppercase">Semana 4 • 8h</span>
                        <h4 class="font-bold text-sm text-slate-900 leading-snug">Proyecto Directivo Capstone & Certificación</h4>
                        <p class="text-xs text-slate-600">Defensa del Plan Corporativo ante el tribunal evaluador de Fundación Kinal.</p>
                    </div>
                </div>
            </div>

        </div>

        <!-- ================================================================== -->
        <!-- PESTAÑA 2: TEMARIO (DISTRIBUCIÓN MODULAR AUDITADA)                 -->
        <!-- ================================================================== -->
        <div id="tab-temario" class="tab-content hidden space-y-8">
            
            <!-- Barra Superior de Control y Filtros -->
            <div class="flex flex-col md:flex-row justify-between items-start md:items-center gap-4 bg-white rounded-3xl p-6 border border-slate-200 shadow-sm">
                <div class="space-y-1">
                    <h3 class="text-xl font-black text-slate-900 flex items-center gap-2">
                        <i data-lucide="list-tree" class="w-5 h-5 text-blue-700"></i>
                        Distribución Modular de Temarios
                    </h3>
                    <p class="text-xs text-slate-500">
                        Estructura organizada en 4 módulos y 12 temas directivos clasificados por naturaleza técnica, logros de aprendizaje e impacto en planta.
                    </p>
                </div>

                <!-- Botones de Filtro Interactivo -->
                <div class="flex flex-wrap items-center gap-2 text-xs font-semibold">
                    <button onclick="filterTalentoTemario('all')" id="btn-talento-all" class="talento-filter-btn px-3 py-1.5 rounded-lg bg-slate-900 text-white shadow-sm transition">Todos (12)</button>
                    <button onclick="filterTalentoTemario('diagnostico')" id="btn-talento-diagnostico" class="talento-filter-btn px-3 py-1.5 rounded-lg bg-blue-100 text-blue-800 hover:bg-blue-200 transition">📊 Diagnóstico & Brechas</button>
                    <button onclick="filterTalentoTemario('competencias')" id="btn-talento-competencias" class="talento-filter-btn px-3 py-1.5 rounded-lg bg-purple-100 text-purple-800 hover:bg-purple-200 transition">🎯 Competencias DQR</button>
                    <button onclick="filterTalentoTemario('factor_humano')" id="btn-talento-factor_humano" class="talento-filter-btn px-3 py-1.5 rounded-lg bg-amber-100 text-amber-800 hover:bg-amber-200 transition">⭐ Factor Humano Kinal</button>
                    <button onclick="filterTalentoTemario('inmersion')" id="btn-talento-inmersion" class="talento-filter-btn px-3 py-1.5 rounded-lg bg-emerald-100 text-emerald-800 hover:bg-emerald-200 transition">🏭 Inmersión Presencial</button>
                </div>
            </div>

            <!-- Código de Leyenda Explicativo -->
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3 text-xs">
                <div class="p-3.5 rounded-xl border border-blue-200 bg-blue-50/70 text-blue-950 flex items-start gap-2.5">
                    <span class="inline-block w-3 h-3 rounded-full bg-blue-600 mt-0.5 shrink-0"></span>
                    <div>
                        <strong class="text-blue-900">Color Azul (Diagnóstico & ROI):</strong> Radiografía laboral de Guatemala, costos de la no calidad y cálculo financiero del retorno de inversión.
                    </div>
                </div>
                <div class="p-3.5 rounded-xl border border-purple-200 bg-purple-50/70 text-purple-950 flex items-start gap-2.5">
                    <span class="inline-block w-3 h-3 rounded-full bg-purple-600 mt-0.5 shrink-0"></span>
                    <div>
                        <strong class="text-purple-900">Color Púrpura (Competencias DQR):</strong> Reingeniería de puestos hacia competencias observables y entrevistas técnicas situacionales STAR.
                    </div>
                </div>
                <div class="p-3.5 rounded-xl border border-amber-200 bg-amber-50/70 text-amber-950 flex items-start gap-2.5">
                    <span class="inline-block w-3 h-3 rounded-full bg-amber-600 mt-0.5 shrink-0"></span>
                    <div>
                        <strong class="text-amber-900">Color Ámbar (Factor Humano):</strong> Valores universales, dignidad en planta, liderazgo sin maltrato y seguridad psicológica.
                    </div>
                </div>
                <div class="p-3.5 rounded-xl border border-emerald-200 bg-emerald-50/70 text-emerald-950 flex items-start gap-2.5">
                    <span class="inline-block w-3 h-3 rounded-full bg-emerald-600 mt-0.5 shrink-0"></span>
                    <div>
                        <strong class="text-emerald-900">Color Verde (Inmersión & Alianza):</strong> Prácticas vivenciales en campus Kinal, semillero dual y defensa del Proyecto Capstone.
                    </div>
                </div>
            </div>

            <!-- Cuadrícula Modular de Temarios (Tarjetas con Módulo y Temas) -->
            <div class="grid lg:grid-cols-2 gap-8 pt-2">
"""

for mod in temario_modules:
    html_content += f"""
                <div class="bg-white rounded-2xl border border-slate-300 shadow-sm overflow-hidden flex flex-col hover:shadow-md transition">
                    <div class="bg-slate-900 text-white p-4 sm:p-5 border-b border-slate-800 space-y-1">
                        <div class="flex flex-wrap justify-between items-center text-xs text-amber-400 font-semibold mb-1 gap-2">
                            <span>MÓDULO {mod['num']} ({mod['semana']} • Sesiones {((mod['num']-1)*3)+1} a {mod['num']*3})</span>
                            <span class="px-2 py-0.5 rounded bg-blue-900/60 text-blue-200 border border-blue-400/30 text-[11px] font-bold">{mod['hours']}</span>
                        </div>
                        <h4 class="text-base sm:text-lg font-bold text-white leading-snug">{mod['title']}</h4>
                        <p class="text-xs text-slate-300 pt-1 leading-relaxed">
                            <strong class="text-amber-300">Logro esperado:</strong> {mod['logro']}
                        </p>
                    </div>
                    <div class="p-4 sm:p-5 divide-y divide-slate-100 flex-1 space-y-2.5 bg-slate-50/50">
    """
    for t in mod['topics']:
        html_content += f"""
                        <div class="content-item item-{t['cat']} p-3.5 rounded-xl text-xs space-y-1.5 transition border border-slate-200/90 bg-white hover:bg-slate-50 shadow-sm" data-category="{t['cat']}">
                            <div class="flex flex-wrap justify-between items-center gap-1.5 font-bold">
                                <span class="text-slate-900 text-sm flex items-center gap-2">
                                    <span class="w-5 h-5 rounded-full bg-slate-100 text-slate-700 text-xs font-black flex items-center justify-center shrink-0">{t['num']}</span>
                                    {t['title']}
                                </span>
                                <span class="px-2.5 py-0.5 rounded-full text-[10px] font-extrabold uppercase {t['cat_badge']}">{t['cat_name']}</span>
                            </div>
                            <p class="text-slate-600 leading-relaxed pl-7">{t['desc']}</p>
                        </div>
        """
    html_content += """
                    </div>
                </div>
    """

html_content += f"""
            </div>
        </div>

        <!-- ================================================================== -->
        <!-- PESTAÑA 3: CALENDARIO -->
        <!-- ================================================================== -->
        <div id="tab-calendario" class="tab-content hidden space-y-6">
            <div class="border-b border-slate-200 pb-4 flex flex-wrap justify-between items-end gap-2">
                <div>
                    <span class="text-xs font-bold text-[#EC9123] uppercase tracking-wider">Cronograma Ejecutivo de 4 Semanas</span>
                    <h3 class="text-2xl font-black text-slate-900 brand-serif">Dosificación Cronológica de Sesiones</h3>
                    <p class="text-slate-600 text-xs mt-1">Ritmo intensivo sin interrupciones: 2 sesiones virtuales entre semana + 1 taller presencial en Kinal los sábados.</p>
                </div>
                <div class="inline-flex items-center gap-1.5 px-3 py-1 rounded-lg bg-emerald-50 text-emerald-800 border border-emerald-200 text-xs font-bold">
                    <i data-lucide="check-circle" class="w-4 h-4 text-emerald-600"></i> 12 Sesiones Programadas
                </div>
            </div>

            <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-4">
"""

for s in sessions:
    html_content += f"""
                <div class="bg-white rounded-2xl border border-slate-200 p-4 shadow-sm hover:border-[#22376D] hover:shadow-md transition flex flex-col justify-between space-y-3">
                    <div class="space-y-1.5">
                        <div class="flex justify-between items-center text-[11px]">
                            <span class="font-black px-2 py-0.5 rounded bg-[#152244] text-[#EC9123]">{s['code']}</span>
                            <span class="font-bold text-slate-500">{s['semana']}</span>
                        </div>
                        <h5 class="font-bold text-slate-900 text-xs leading-snug line-clamp-2">{s['title']}</h5>
                        <p class="text-[11px] text-slate-500">{s['tipo']}</p>
                    </div>
                    <div class="pt-2 border-t border-slate-100 flex items-center justify-between text-[11px]">
                        <span class="text-slate-600 font-semibold">{s['duration']}</span>
                        <button onclick="goToSession({s['num']})" class="text-[#22376D] font-bold hover:underline flex items-center gap-0.5">
                            Ver Secuencia →
                        </button>
                    </div>
                </div>
    """

html_content += f"""
            </div>
        </div>

        <!-- ================================================================== -->
        <!-- PESTAÑA 4: SECUENCIAS DIDÁCTICAS INTERACTIVAS -->
        <!-- ================================================================== -->
        <div id="tab-secuencias" class="tab-content hidden space-y-6">
            <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-3 border-b border-slate-200 pb-4">
                <div>
                    <span class="text-xs font-bold text-[#EC9123] uppercase tracking-wider">Microdiseño Didáctico Andragógico</span>
                    <h3 class="text-2xl font-black text-slate-900 brand-serif flex items-center gap-2">
                        <i data-lucide="layers" class="w-5 h-5 text-[#22376D]"></i>
                        Secuencia Didáctica Sesión a Sesión
                    </h3>
                    <p class="text-slate-600 text-xs mt-0.5">
                        Selecciona una sesión en el panel lateral para revisar su desglose en 3 momentos (Apertura, Desarrollo y Cierre), recursos y entregables observables.
                    </p>
                </div>
                <div class="flex items-center gap-2 w-full sm:w-auto">
                    <div class="relative w-full sm:w-56">
                        <i data-lucide="search" class="w-3.5 h-3.5 text-slate-400 absolute left-3 top-2.5"></i>
                        <input type="text" id="talento-sec-search" oninput="filterTalentoList()" placeholder="Buscar sesión..." class="w-full pl-8 pr-3 py-1.5 text-xs rounded-xl border border-slate-200 bg-slate-50 focus:bg-white focus:outline-none focus:ring-2 focus:ring-[#22376D] transition">
                    </div>
                </div>
            </div>

            <!-- Master-Detail Container -->
            <div class="grid lg:grid-cols-12 gap-6 items-start">
                
                <!-- LISTADO LATERAL (MASTER) -->
                <div class="lg:col-span-4 bg-white rounded-3xl border border-slate-200 p-4 shadow-sm space-y-2">
                    <div class="text-[11px] font-black uppercase tracking-wider text-slate-400 px-2 pb-1 border-b border-slate-100 flex justify-between">
                        <span>Listado de Sesiones</span>
                        <span id="talento-count-badge">12 Sesiones</span>
                    </div>
                    <div id="talento-sessions-list" class="space-y-1.5 max-h-[580px] overflow-y-auto pr-1">
                        <!-- Rendered by JS -->
                    </div>
                </div>

                <!-- DETALLE DE LA SESIÓN SELECCIONADA (DETAIL) -->
                <div class="lg:col-span-8 bg-white rounded-3xl border border-slate-200 p-6 sm:p-8 shadow-sm space-y-6" id="talento-detail-card">
                    <!-- Rendered by JS -->
                </div>

            </div>
        </div>

        <!-- ================================================================== -->
        <!-- PESTAÑA 5: EVALUACIÓN Y RÚBRICA -->
        <!-- ================================================================== -->
        <div id="tab-evaluacion" class="tab-content hidden space-y-8">
            
            <!-- Esquema Resumen -->
            <div class="bg-white rounded-3xl border border-slate-200 p-8 shadow-sm space-y-6">
                <div class="flex items-center justify-between border-b border-slate-200 pb-3">
                    <h3 class="text-xl font-black text-slate-900 flex items-center gap-2">
                        <i data-lucide="check-square" class="w-5 h-5 text-[#22376D]"></i>
                        Esquema de Evaluación Institucional & Acreditación Directiva
                    </h3>
                    <span class="px-3 py-1 rounded-full bg-amber-100 text-amber-900 font-black text-xs">
                        Umbral Mínimo: 75 / 100 Puntos
                    </span>
                </div>
                <div class="grid md:grid-cols-4 gap-4 text-xs">
                    <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 text-center space-y-1">
                        <div class="text-slate-500 font-bold uppercase text-[10px]">Casos & Foros Teams</div>
                        <div class="text-3xl font-black text-[#22376D]">25%</div>
                        <div class="text-slate-600">Dilemas de Rotación & Selección</div>
                    </div>
                    <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 text-center space-y-1">
                        <div class="text-slate-500 font-bold uppercase text-[10px]">Talleres Campus Kinal</div>
                        <div class="text-3xl font-black text-emerald-700">25%</div>
                        <div class="text-slate-600">4 Sábados en Laboratorios TSU</div>
                    </div>
                    <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 text-center space-y-1">
                        <div class="text-slate-500 font-bold uppercase text-[10px]">Factor Humano & Perfiles</div>
                        <div class="text-3xl font-black text-blue-900">20%</div>
                        <div class="text-slate-600">Matrices & Charlas Operativas</div>
                    </div>
                    <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 text-center space-y-1">
                        <div class="text-slate-500 font-bold uppercase text-[10px]">Defensa Proyecto Capstone</div>
                        <div class="text-3xl font-black text-amber-700">30%</div>
                        <div class="text-slate-600">Tribunal Directivo Kinal</div>
                    </div>
                </div>
            </div>

            <!-- Rúbrica Terminal -->
            <div class="bg-white rounded-3xl border border-slate-200 p-8 shadow-sm space-y-6">
                <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2 border-b border-slate-200 pb-4">
                    <div>
                        <h3 class="text-xl font-black text-slate-900 flex items-center gap-2">
                            <i data-lucide="award" class="w-5 h-5 text-[#22376D]"></i>
                            Rúbrica Analítica Terminal de Sustentación Directiva
                        </h3>
                        <p class="text-slate-600 text-xs mt-1">
                            Evaluación objetiva del Plan Integral de Gestión Estratégica del Talento Técnico con exigencia mínima de 75 puntos sobre 100.
                        </p>
                    </div>
                    <span class="px-3 py-1.5 rounded-xl bg-amber-100 text-amber-900 font-extrabold text-xs">
                        Aprobación Mínima: ≥ 75 Pts
                    </span>
                </div>

                <div class="overflow-x-auto">
                    <table class="w-full text-xs text-left border-collapse">
                        <thead>
                            <tr class="bg-slate-100 text-slate-800 uppercase font-black border-b border-slate-200">
                                <th class="py-3 px-4 w-1/4">Criterio Evaluado</th>
                                <th class="py-3 px-4 w-24 text-center">Ponderación</th>
                                <th class="py-3 px-4 text-emerald-900">Desempeño Excelente (Estándar Kinal)</th>
                                <th class="py-3 px-4 text-rose-900">Desempeño Insuficiente (&lt; 75%)</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-100">
"""

for row in rubrica_rows:
    crit = row[0]
    pond = row[1]
    exc = row[2]
    insuf = row[3]
    html_content += f"""
                            <tr class="hover:bg-slate-50/80 transition">
                                <td class="py-3.5 px-4 font-bold text-slate-900 bg-slate-50 border-r border-slate-200 align-top">{crit}</td>
                                <td class="py-3 px-4 text-[#22376D] font-black bg-blue-50/20 border-r border-slate-200 align-top text-center">{pond}</td>
                                <td class="py-3 px-4 text-emerald-950 bg-emerald-50/30 border-r border-slate-200 align-top leading-relaxed">{exc}</td>
                                <td class="py-3 px-4 text-rose-950 bg-rose-50/30 align-top leading-relaxed">{insuf}</td>
                            </tr>
    """

html_content += f"""
                        </tbody>
                    </table>
                </div>
            </div>

        </div>

    </main>

    <!-- Footer Institucional -->
    <footer class="bg-[#0D162C] text-white border-t-4 border-[#EC9123] py-10 px-4 sm:px-6 lg:px-8 mt-12">
        <div class="max-w-7xl mx-auto space-y-6">
            <div class="flex flex-col md:flex-row justify-between items-start md:items-center gap-6 border-b border-slate-800 pb-6">
                <img src="assets/fundacion_kinal_blanco.png" alt="Fundación Kinal" class="h-10 w-auto object-contain">
                <div class="text-xs text-slate-400 max-w-md text-left md:text-right">
                    <strong class="text-white block mb-0.5">Escuela Técnica Superior — Fundación Kinal</strong>
                    Diplomado de Certificación Gerencial en Gestión Estratégica del Talento Técnico. Formación continua directiva orientada al impacto productivo real.
                </div>
            </div>
            <div class="flex flex-col sm:flex-row justify-between items-center text-xs text-slate-500 gap-4">
                <div>© 2026 Fundación Kinal. Todos los derechos reservados.</div>
                <div class="flex items-center gap-4">
                    <a href="cursos_nuevos.html" class="hover:text-[#EC9123] transition">Catálogo de Cursos</a>
                    <span>•</span>
                    <a href="tsu.html" class="hover:text-[#EC9123] transition">TSU Kinal</a>
                    <span>•</span>
                    <a href="index.html" class="hover:text-[#EC9123] transition">Inicio</a>
                </div>
            </div>
        </div>
    </footer>

    <!-- Scripts y Lógica Interactiva -->
    <script>
        const talentoSessionsData = {sessions_json};
        let currentTalentoSessionNum = 1;

        function switchTab(tabId) {{
            document.querySelectorAll('.tab-content').forEach(el => el.classList.add('hidden'));
            document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));

            const targetTab = document.getElementById('tab-' + tabId);
            const targetBtn = document.getElementById('btn-' + tabId);

            if (targetTab) targetTab.classList.remove('hidden');
            if (targetBtn) targetBtn.classList.add('active');

            if (tabId === 'secuencias') {{
                renderTalentoSessionsList(talentoSessionsData);
                renderTalentoDetail(currentTalentoSessionNum);
            }}
            lucide.createIcons();
        }}

        function renderTalentoSessionsList(list) {{
            const container = document.getElementById('talento-sessions-list');
            if (!container) return;
            container.innerHTML = '';

            list.forEach(s => {{
                const item = document.createElement('div');
                item.className = `session-item p-3 rounded-2xl border cursor-pointer transition flex items-center justify-between gap-2 ${{
                    s.num === currentTalentoSessionNum ? 'active bg-emerald-50/70 border-emerald-500' : 'bg-slate-50 border-slate-200 hover:bg-slate-100'
                }}`;
                item.onclick = () => renderTalentoDetail(s.num);
                item.innerHTML = `
                    <div class="space-y-0.5">
                        <div class="flex items-center gap-2">
                            <span class="px-2 py-0.5 rounded bg-slate-900 text-[#EC9123] text-[10px] font-black">${{s.code}}</span>
                            <span class="text-[11px] font-bold text-slate-500">${{s.semana}}</span>
                        </div>
                        <h5 class="text-xs font-bold text-slate-900 line-clamp-1">${{s.title}}</h5>
                        <p class="text-[10px] text-slate-500">${{s.duration}}</p>
                    </div>
                    <i data-lucide="chevron-right" class="w-4 h-4 text-slate-400 shrink-0"></i>
                `;
                container.appendChild(item);
            }});
            lucide.createIcons();
        }}

        function renderTalentoDetail(num) {{
            currentTalentoSessionNum = num;
            const s = talentoSessionsData.find(item => item.num === num);
            if (!s) return;

            renderTalentoSessionsList(talentoSessionsData);

            const detailContainer = document.getElementById('talento-detail-card');
            detailContainer.innerHTML = `
                <div class="border-b border-slate-200 pb-5 space-y-2">
                    <div class="flex flex-wrap justify-between items-center gap-2">
                        <div class="flex items-center gap-2">
                            <span class="px-3 py-1 rounded-xl bg-slate-950 text-[#EC9123] font-black text-xs tracking-wider">${{s.code}}</span>
                            <span class="px-2.5 py-0.5 rounded-lg bg-blue-50 text-[#22376D] font-bold text-xs border border-blue-200">${{s.module}}</span>
                        </div>
                        <span class="text-xs font-bold text-slate-500 bg-slate-100 px-3 py-1 rounded-lg">${{s.duration}}</span>
                    </div>
                    <h3 class="text-xl sm:text-2xl font-black text-slate-900 leading-snug">${{s.title}}</h3>
                    <div class="text-xs text-[#22376D] font-bold pt-1">
                        ${{s.semana}} • ${{s.tipo}}
                    </div>
                </div>

                <div class="bg-amber-50/60 rounded-2xl p-4 border border-amber-200 space-y-1">
                    <div class="text-[11px] uppercase font-black tracking-wider text-amber-900 flex items-center gap-1.5">
                        <i data-lucide="target" class="w-3.5 h-3.5 text-[#EC9123]"></i> Objetivo Específico Formativo
                    </div>
                    <p class="text-slate-800 text-xs leading-relaxed font-medium">${{s.objective}}</p>
                </div>

                <div class="space-y-4">
                    <h4 class="text-sm font-black text-slate-900 uppercase tracking-wide flex items-center gap-2 border-b border-slate-100 pb-2">
                        <i data-lucide="clock" class="w-4 h-4 text-[#22376D]"></i> Secuencia Didáctica en Tres Momentos
                    </h4>

                    <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-1.5">
                        <div class="flex items-center justify-between">
                            <span class="font-bold text-xs text-blue-950 flex items-center gap-2">
                                <span class="w-2.5 h-2.5 rounded-full bg-blue-600"></span> Fase 1: Apertura & Motivación
                            </span>
                        </div>
                        <p class="text-slate-700 text-xs leading-relaxed pl-4.5">${{s.apertura}}</p>
                    </div>

                    <div class="p-4 rounded-2xl bg-blue-50/40 border border-blue-200 space-y-1.5">
                        <div class="flex items-center justify-between">
                            <span class="font-bold text-xs text-[#152244] flex items-center gap-2">
                                <span class="w-2.5 h-2.5 rounded-full bg-emerald-600"></span> Fase 2: Desarrollo & Taller Práctico / Casos
                            </span>
                        </div>
                        <p class="text-slate-700 text-xs leading-relaxed pl-4.5">${{s.desarrollo}}</p>
                    </div>

                    <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-1.5">
                        <div class="flex items-center justify-between">
                            <span class="font-bold text-xs text-blue-950 flex items-center gap-2">
                                <span class="w-2.5 h-2.5 rounded-full bg-amber-600"></span> Fase 3: Cierre & Síntesis Directiva
                            </span>
                        </div>
                        <p class="text-slate-700 text-xs leading-relaxed pl-4.5">${{s.cierre}}</p>
                    </div>
                </div>

                <div class="grid sm:grid-cols-2 gap-4 pt-2">
                    <div class="bg-emerald-50/60 rounded-2xl p-4 border border-emerald-200 space-y-1.5">
                        <div class="text-[11px] uppercase font-black tracking-wider text-emerald-900 flex items-center gap-1.5">
                            <i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-emerald-700"></i> Entregable y Evidencia
                        </div>
                        <p class="text-slate-700 text-xs leading-relaxed">${{s.evidencias}}</p>
                    </div>

                    <div class="bg-slate-100 rounded-2xl p-4 border border-slate-200 space-y-1.5">
                        <div class="text-[11px] uppercase font-black tracking-wider text-slate-900 flex items-center gap-1.5">
                            <i data-lucide="cpu" class="w-3.5 h-3.5 text-[#22376D]"></i> Recursos y Plataformas
                        </div>
                        <p class="text-slate-700 text-xs leading-relaxed">${{s.equipamiento}}</p>
                    </div>
                </div>

                <!-- Botones de Navegación Anterior / Siguiente -->
                <div class="flex justify-between items-center pt-4 border-t border-slate-100">
                    <button onclick="navigateTalentoSession(-1)" ${{s.num === 1 ? 'disabled class="opacity-40 cursor-not-allowed"' : 'class="hover:bg-slate-100"'}} px-3.5 py-2 rounded-xl border border-slate-200 text-xs font-bold text-slate-700 flex items-center gap-1.5 transition">
                        <i data-lucide="arrow-left" class="w-4 h-4"></i> Anterior
                    </button>
                    <span class="text-xs font-bold text-slate-400">Sesión ${{s.num}} de ${{talentoSessionsData.length}}</span>
                    <button onclick="navigateTalentoSession(1)" ${{s.num === talentoSessionsData.length ? 'disabled class="opacity-40 cursor-not-allowed"' : 'class="hover:bg-slate-100"'}} px-3.5 py-2 rounded-xl border border-slate-200 text-xs font-bold text-slate-700 flex items-center gap-1.5 transition">
                        Siguiente <i data-lucide="arrow-right" class="w-4 h-4"></i>
                    </button>
                </div>
            `;
            lucide.createIcons();
        }}

        function navigateTalentoSession(delta) {{
            const newNum = currentTalentoSessionNum + delta;
            if (newNum >= 1 && newNum <= talentoSessionsData.length) {{
                renderTalentoDetail(newNum);
            }}
        }}

        function filterTalentoList() {{
            const q = document.getElementById('talento-sec-search').value.toLowerCase();
            const filtered = talentoSessionsData.filter(s => 
                s.title.toLowerCase().includes(q) || 
                s.code.toLowerCase().includes(q) ||
                s.module.toLowerCase().includes(q) ||
                s.objective.toLowerCase().includes(q)
            );
            document.getElementById('talento-count-badge').textContent = `${{filtered.length}} Sesiones`;
            renderTalentoSessionsList(filtered);
        }}

        function goToSession(num) {{
            switchTab('secuencias');
            renderTalentoDetail(num);
            document.getElementById('tab-secuencias').scrollIntoView({{ behavior: 'smooth' }});
        }}

        function filterTalentoTemario(category) {{
            const items = document.querySelectorAll('.content-item');
            items.forEach(el => {{
                if (category === 'all' || el.getAttribute('data-category') === category) {{
                    el.style.display = 'block';
                }} else {{
                    el.style.display = 'none';
                }}
            }});

            document.querySelectorAll('.talento-filter-btn').forEach(btn => {{
                btn.classList.remove('bg-slate-900', 'text-white');
                btn.classList.add('bg-slate-100', 'text-slate-700');
            }});

            const activeBtn = document.getElementById('btn-talento-' + category);
            if (activeBtn) {{
                activeBtn.classList.remove('bg-slate-100', 'text-slate-700');
                activeBtn.classList.add('bg-slate-900', 'text-white');
            }}
        }}

        document.addEventListener('DOMContentLoaded', () => {{
            lucide.createIcons();
        }});
    </script>
</body>
</html>
"""

# Guardar en raíz y en web
out_path_1 = os.path.join(WORKSPACE_DIR, "curso_diplomado_gerencial.html")
out_path_2 = os.path.join(WORKSPACE_DIR, "curso_talento_tecnico.html")

with open(out_path_1, "w", encoding="utf-8") as f:
    f.write(html_content)
with open(out_path_2, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Generated successfully: {out_path_1}")
