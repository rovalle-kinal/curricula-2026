"""
Script para generar la página remodelada de 'Revisión de Temarios'
con la identidad gráfica oficial de Fundación Kinal y la Escuela Técnica Superior (ETS):
- Tipografía oficial: Times New Roman (Títulos) y Arial (Lectura/Cuerpo).
- Colores oficiales: Azul Kinal (#22376D, C100 M90 Y30 K15) y Amarillo/Naranja Llama (#EC9123, C5 M50 Y100 K0).
- Logotipos oficiales de alta resolución: Fundación Kinal, ETS, Escudo, Llama y Lema "El trabajo bien hecho".
- Ubicación local: rovalle-kinal.git/remodelacion_revision_temarios/index.html
"""

import os

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGET_DIR = os.path.join(WORKSPACE_DIR, "rovalle-kinal.git", "remodelacion_revision_temarios")
os.makedirs(TARGET_DIR, exist_ok=True)

HTML_CONTENT = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Auditoría y Revisión Curricular de Temarios | Escuela Técnica Superior — Fundación Kinal</title>
    
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
        :root {
            --kinal-blue: #22376D;
            --kinal-blue-dark: #152244;
            --kinal-blue-deep: #0D162C;
            --kinal-blue-light: #2E4A91;
            --kinal-flame: #EC9123;
            --kinal-gold: #F5A623;
            --kinal-gray-8c: #888B8D;
            --kinal-bg-light: #F8F9FA;
            --kinal-border: #DDE2E5;
        }

        body {
            font-family: Arial, Helvetica, "Nimbus Sans L", "Liberation Sans", sans-serif;
            background-color: var(--kinal-bg-light);
            color: #1E293B;
            -webkit-font-smoothing: antialiased;
        }

        /* Tipografía Corporativa Oficial de Kinal para Títulos */
        h1, h2, h3, h4, .font-kinal-title, .brand-serif {
            font-family: "Times New Roman", Times, "Playfair Display", Georgia, serif;
            letter-spacing: -0.01em;
        }

        .bg-kinal-blue { background-color: var(--kinal-blue); }
        .bg-kinal-blue-dark { background-color: var(--kinal-blue-dark); }
        .text-kinal-blue { color: var(--kinal-blue); }
        .border-kinal-blue { border-color: var(--kinal-blue); }

        .bg-kinal-flame { background-color: var(--kinal-flame); }
        .text-kinal-flame { color: var(--kinal-flame); }
        .border-kinal-flame { border-color: var(--kinal-flame); }

        .hero-kinal-gradient {
            background: linear-gradient(135deg, #0D162C 0%, #152244 45%, #22376D 100%);
        }

        /* Código de color auditado institucional */
        .status-delete { background-color: #FEF2F2; border-left: 4px solid #DC2626; color: #991B1B; }
        .status-update { background-color: #FEFCE8; border-left: 4px solid #EAB308; color: #854D0E; }
        .status-new    { background-color: #EFF6FF; border-left: 4px solid #2563EB; color: #1E40AF; }
        .status-keep   { background-color: #F0FDF4; border-left: 4px solid #16A34A; color: #166534; }
        .status-ia     { background-color: #FAF5FF; border-left: 4px solid #9333EA; color: #6B21A8; }

        /* Estilos móviles sin desborde */
        @media (max-width: 767px) {
            *, *::before, *::after { box-sizing: border-box !important; }
            html, body { overflow-x: hidden !important; max-width: 100vw !important; }
            .no-scrollbar::-webkit-scrollbar { display: none !important; }
            .no-scrollbar { -ms-overflow-style: none !important; scrollbar-width: none !important; }
        }
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
    <!-- HEADER CORPORATIVO CON LOGOTIPOS OFICIALES               -->
    <!-- ========================================================= -->
    <header class="bg-white border-b border-slate-200 sticky top-0 z-50 shadow-sm">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3.5 flex flex-wrap justify-between items-center gap-4">
            
            <!-- Logotipos de Fundación Kinal y ETS -->
            <div class="flex items-center gap-4">
                <a href="#" class="flex items-center gap-3 group">
                    <img src="assets/fundacion_kinal_color.png" alt="Fundación Kinal" class="h-10 sm:h-12 w-auto object-contain transition group-hover:opacity-90">
                </a>
                <span class="h-8 w-px bg-slate-300 hidden sm:block"></span>
                <div class="hidden sm:flex items-center gap-2">
                    <img src="assets/escuela_tecnica_superior.png" alt="Escuela Técnica Superior" class="h-8 sm:h-9 w-auto object-contain">
                </div>
            </div>

            <!-- Navegación y Accesos Directos -->
            <nav class="flex items-center gap-2 sm:gap-3 text-xs font-bold">
                <a href="#areas" class="px-3 py-2 rounded-lg bg-slate-100 hover:bg-[#22376D] hover:text-white text-slate-700 transition flex items-center gap-1.5">
                    <i data-lucide="layers" class="w-4 h-4 text-[#EC9123]"></i> Áreas de Taller
                </a>
                <a href="#auditoria-interactiva" class="px-3 py-2 rounded-lg bg-slate-100 hover:bg-[#22376D] hover:text-white text-slate-700 transition flex items-center gap-1.5">
                    <i data-lucide="check-square" class="w-4 h-4 text-[#22376D]"></i> Dictámenes
                </a>
                <a href="#metodologia" class="px-3.5 py-2 rounded-lg bg-[#22376D] text-white hover:bg-[#152244] transition flex items-center gap-1.5 shadow-sm">
                    <i data-lucide="file-badge" class="w-4 h-4 text-[#EC9123]"></i> Marco DQR & UNIS
                </a>
            </nav>
        </div>
    </header>

    <!-- ========================================================= -->
    <!-- HERO PRINCIPAL — REVISIÓN DE TEMARIOS                     -->
    <!-- ========================================================= -->
    <section class="hero-kinal-gradient text-white py-14 sm:py-20 px-4 sm:px-6 lg:px-8 relative overflow-hidden">
        
        <!-- Elementos gráficos de fondo (Llama de agua institucional) -->
        <div class="absolute right-0 bottom-0 opacity-10 pointer-events-none transform translate-x-12 translate-y-12">
            <img src="assets/llama_kinal.png" alt="" class="w-96 h-auto">
        </div>

        <div class="max-w-5xl mx-auto space-y-6 relative z-10">
            
            <!-- Badge institucional superior -->
            <div class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-white/10 border border-white/20 text-[#EC9123] text-xs font-bold tracking-wide uppercase">
                <img src="assets/llama_kinal.png" alt="" class="w-4 h-4 object-contain">
                <span>Escuela Técnica Superior (ETS) • Ciclo Lectivo 2026</span>
            </div>

            <!-- Título Institucional con tipografía oficial Times -->
            <h1 class="text-3xl sm:text-5xl lg:text-6xl font-bold tracking-tight leading-tight brand-serif text-white">
                Auditoría Curricular y Modernización de Temarios
            </h1>

            <p class="text-slate-200 text-sm sm:text-base lg:text-lg max-w-3xl leading-relaxed">
                Revisión integral de los programas formativos técnicos de taller frente a la demanda real de los sectores productivos de Guatemala, alineados a los estándares de la <strong>Formación Profesional Dual en Alternancia</strong>, el <strong>Marco DQR</strong> y el ideario del <strong>«Trabajo bien hecho»</strong> de Fundación Kinal.
            </p>

            <!-- Cita y Slogan Oficial -->
            <div class="pt-2 flex flex-wrap items-center gap-6">
                <div class="flex items-center gap-3 bg-white/10 backdrop-blur px-4 py-2.5 rounded-xl border border-white/15">
                    <img src="assets/el_trabajo_bien_hecho_blanco.png" alt="El trabajo bien hecho" class="h-6 w-auto object-contain">
                </div>
                <div class="text-xs text-slate-300 flex items-center gap-2">
                    <span class="w-2 h-2 rounded-full bg-[#EC9123]"></span>
                    <span>Formación doctrinal y espiritual a cargo de la Prelatura del Opus Dei</span>
                </div>
            </div>

            <!-- Métricas Clave Consolidadas -->
            <div class="grid grid-cols-2 md:grid-cols-4 gap-3 sm:gap-4 pt-6 text-left">
                <div class="bg-white/10 backdrop-blur rounded-2xl p-4 border border-white/15 space-y-1">
                    <div class="text-[11px] uppercase tracking-wider text-slate-300 font-bold">Cursos de Taller</div>
                    <div class="text-3xl font-bold brand-serif text-white">20 Programas</div>
                    <div class="text-[11px] text-[#EC9123] font-medium">4 Grandes Áreas ETS</div>
                </div>
                <div class="bg-white/10 backdrop-blur rounded-2xl p-4 border border-white/15 space-y-1">
                    <div class="text-[11px] uppercase tracking-wider text-slate-300 font-bold">Carga Práctica</div>
                    <div class="text-3xl font-bold brand-serif text-white">3,240 Horas</div>
                    <div class="text-[11px] text-emerald-400 font-medium">100% Taller Especializado</div>
                </div>
                <div class="bg-white/10 backdrop-blur rounded-2xl p-4 border border-white/15 space-y-1">
                    <div class="text-[11px] uppercase tracking-wider text-slate-300 font-bold">Módulos con IA</div>
                    <div class="text-3xl font-bold brand-serif text-[#EC9123]">20 Módulos</div>
                    <div class="text-[11px] text-purple-200 font-medium">Transversal Tecnológica</div>
                </div>
                <div class="bg-white/10 backdrop-blur rounded-2xl p-4 border border-white/15 space-y-1">
                    <div class="text-[11px] uppercase tracking-wider text-slate-300 font-bold">Aprobación Mínima</div>
                    <div class="text-3xl font-bold brand-serif text-amber-400">≥ 75 Pts</div>
                    <div class="text-[11px] text-slate-300 font-medium">Exigencia Kinal sobre 100</div>
                </div>
            </div>

        </div>
    </section>

    <!-- ========================================================= -->
    <!-- CONTENIDO PRINCIPAL                                       -->
    <!-- ========================================================= -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 space-y-16 flex-1">

        <!-- ===================================================== -->
        <!-- SECCIÓN 1: LAS 4 ÁREAS TÉCNICAS AUDITADAS             -->
        <!-- ===================================================== -->
        <section id="areas" class="space-y-8 scroll-mt-24">
            
            <div class="flex flex-col sm:flex-row justify-between items-start sm:items-end gap-3 border-b-2 border-slate-200 pb-4">
                <div>
                    <span class="text-xs font-bold text-[#EC9123] tracking-widest uppercase">Especialidades Técnicas de Taller</span>
                    <h2 class="text-2xl sm:text-4xl font-bold brand-serif text-[#22376D] mt-1">
                        Distribución de Áreas y Programas Formativos
                    </h2>
                    <p class="text-slate-600 text-xs sm:text-sm mt-1 max-w-2xl leading-relaxed">
                        Selecciona un área técnica para consultar su diagnóstico de demanda industrial, auditoría curricular y los módulos de especialización.
                    </p>
                </div>
                <div class="flex items-center gap-2">
                    <span class="px-3 py-1 rounded-full bg-[#22376D]/10 text-[#22376D] font-bold text-xs border border-[#22376D]/20">
                        20 Especialidades Activas
                    </span>
                </div>
            </div>

            <!-- Grid de las 4 Áreas -->
            <div class="grid lg:grid-cols-2 gap-6">

                <!-- ÁREA 1: CONSTRUCCIÓN Y MODELADO BIM -->
                <div class="bg-white rounded-3xl border border-slate-200 p-6 sm:p-7 shadow-sm hover:shadow-md hover:border-[#22376D] transition flex flex-col justify-between space-y-5">
                    <div class="space-y-4">
                        <div class="flex justify-between items-start">
                            <span class="px-3 py-1 rounded-full bg-[#22376D]/10 text-[#22376D] font-bold text-xs uppercase tracking-wider border border-[#22376D]/20">
                                6 Cursos • 720 Horas Presenciales
                            </span>
                            <div class="w-10 h-10 rounded-xl bg-amber-50 text-[#EC9123] flex items-center justify-center font-bold">
                                <i data-lucide="hard-hat" class="w-5 h-5"></i>
                            </div>
                        </div>
                        <div>
                            <h3 class="text-xl sm:text-2xl font-bold brand-serif text-[#22376D]">
                                Construcción, Topografía y Modelado BIM
                            </h3>
                            <p class="text-slate-600 text-xs sm:text-sm mt-2 leading-relaxed">
                                Modernización orientada al estándar sísmico AGIES NSE-4, administración de obras bajo el Plan SSO Acuerdo Gubernativo 229-2014, metodología BIM Forum Guatemala, interoperabilidad CAD-BIM, Navisworks clash detection y diseño vial con Civil 3D y LiDAR.
                            </p>
                        </div>
                        
                        <!-- Listado de Cursos del Área -->
                        <div class="space-y-1.5 pt-2 border-t border-slate-100">
                            <div class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Cursos de la Especialidad:</div>
                            <div class="grid grid-cols-2 gap-2 text-xs text-slate-700">
                                <div class="flex items-center gap-1.5">• Fundamentos Construcción (180h)</div>
                                <div class="flex items-center gap-1.5">• Administración Obras (180h)</div>
                                <div class="flex items-center gap-1.5">• AutoCAD 2D & 3D (90h)</div>
                                <div class="flex items-center gap-1.5">• Revit Architecture (90h)</div>
                                <div class="flex items-center gap-1.5">• Revit Structure & MEP (90h)</div>
                                <div class="flex items-center gap-1.5">• Autodesk Civil 3D (90h)</div>
                            </div>
                        </div>
                    </div>

                    <div class="pt-4 border-t border-slate-100 flex items-center justify-between">
                        <span class="text-[11px] text-slate-500 font-medium">
                            <strong>Normas:</strong> AGIES NSE-4 • SSO 229-2014 • BIM Forum GT
                        </span>
                        <button onclick="filtrarArea('construccion')" class="px-4 py-2 rounded-xl bg-[#22376D] hover:bg-[#152244] text-white text-xs font-bold transition flex items-center gap-1">
                            Ver Temarios <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
                        </button>
                    </div>
                </div>

                <!-- ÁREA 2: ELECTRICIDAD, ELECTRÓNICA Y AUTOMATIZACIÓN -->
                <div class="bg-white rounded-3xl border border-slate-200 p-6 sm:p-7 shadow-sm hover:shadow-md hover:border-[#22376D] transition flex flex-col justify-between space-y-5">
                    <div class="space-y-4">
                        <div class="flex justify-between items-start">
                            <span class="px-3 py-1 rounded-full bg-[#22376D]/10 text-[#22376D] font-bold text-xs uppercase tracking-wider border border-[#22376D]/20">
                                5 Cursos • 900 Horas Presenciales
                            </span>
                            <div class="w-10 h-10 rounded-xl bg-blue-50 text-[#22376D] flex items-center justify-center font-bold">
                                <i data-lucide="zap" class="w-5 h-5"></i>
                            </div>
                        </div>
                        <div>
                            <h3 class="text-xl sm:text-2xl font-bold brand-serif text-[#22376D]">
                                Electricidad Industrial, Electrónica y Automatización
                            </h3>
                            <p class="text-slate-600 text-xs sm:text-sm mt-2 leading-relaxed">
                                Formación alineada a los pliegos tarifarios de EEGSA y Energuate, medición de resistividad de puesta a tierra con telurómetro, generación solar fotovoltaica On-Grid (CNEE-186-2008), control con VFD, PLC Siemens S7-1200 en TIA Portal y redes Profinet.
                            </p>
                        </div>
                        
                        <div class="space-y-1.5 pt-2 border-t border-slate-100">
                            <div class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Cursos de la Especialidad:</div>
                            <div class="grid grid-cols-2 gap-2 text-xs text-slate-700">
                                <div class="flex items-center gap-1.5">• Instalaciones Eléctricas (180h)</div>
                                <div class="flex items-center gap-1.5">• Controles y Máquinas (180h)</div>
                                <div class="flex items-center gap-1.5">• Automatización Industrial (180h)</div>
                                <div class="flex items-center gap-1.5">• Electrónica Industrial (180h)</div>
                                <div class="flex items-center gap-1.5">• Energía Solar On-Grid (180h)</div>
                            </div>
                        </div>
                    </div>

                    <div class="pt-4 border-t border-slate-100 flex items-center justify-between">
                        <span class="text-[11px] text-slate-500 font-medium">
                            <strong>Normas:</strong> CNEE 186-2008 • NFPA 70E • Siemens TIA
                        </span>
                        <button onclick="filtrarArea('electricidad')" class="px-4 py-2 rounded-xl bg-[#22376D] hover:bg-[#152244] text-white text-xs font-bold transition flex items-center gap-1">
                            Ver Temarios <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
                        </button>
                    </div>
                </div>

                <!-- ÁREA 3: MECÁNICA INDUSTRIAL, SOLDADURA Y CALDERAS -->
                <div class="bg-white rounded-3xl border border-slate-200 p-6 sm:p-7 shadow-sm hover:shadow-md hover:border-[#22376D] transition flex flex-col justify-between space-y-5">
                    <div class="space-y-4">
                        <div class="flex justify-between items-start">
                            <span class="px-3 py-1 rounded-full bg-[#22376D]/10 text-[#22376D] font-bold text-xs uppercase tracking-wider border border-[#22376D]/20">
                                3 Cursos • 540 Horas Presenciales
                            </span>
                            <div class="w-10 h-10 rounded-xl bg-slate-100 text-[#22376D] flex items-center justify-center font-bold">
                                <i data-lucide="wrench" class="w-5 h-5"></i>
                            </div>
                        </div>
                        <div>
                            <h3 class="text-xl sm:text-2xl font-bold brand-serif text-[#22376D]">
                                Mecánica Industrial, Soldadura y Calderas de Vapor
                            </h3>
                            <p class="text-slate-600 text-xs sm:text-sm mt-2 leading-relaxed">
                                Mantenimiento predictivo con alineación láser de ejes y análisis de vibraciones IoT, calificación de procedimientos y soldadores según códigos AWS D1.1 y ASME Sección IX (GMAW, FCAW, TIG inoxidable) y operación de calderas bajo el Reglamento del MinTrab.
                            </p>
                        </div>
                        
                        <div class="space-y-1.5 pt-2 border-t border-slate-100">
                            <div class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Cursos de la Especialidad:</div>
                            <div class="grid grid-cols-2 gap-2 text-xs text-slate-700">
                                <div class="flex items-center gap-1.5">• Mantenimiento Mecánico (180h)</div>
                                <div class="flex items-center gap-1.5">• Soldadura Industrial AWS (180h)</div>
                                <div class="flex items-center gap-1.5">• Calderas de Vapor (180h)</div>
                            </div>
                        </div>
                    </div>

                    <div class="pt-4 border-t border-slate-100 flex items-center justify-between">
                        <span class="text-[11px] text-slate-500 font-medium">
                            <strong>Normas:</strong> AWS D1.1 • ASME Sec. IX • Reglamento Calderas
                        </span>
                        <button onclick="filtrarArea('mecanica')" class="px-4 py-2 rounded-xl bg-[#22376D] hover:bg-[#152244] text-white text-xs font-bold transition flex items-center gap-1">
                            Ver Temarios <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
                        </button>
                    </div>
                </div>

                <!-- ÁREA 4: MECÁNICA AUTOMOTRIZ Y MOTOCICLETAS -->
                <div class="bg-white rounded-3xl border border-slate-200 p-6 sm:p-7 shadow-sm hover:shadow-md hover:border-[#22376D] transition flex flex-col justify-between space-y-5">
                    <div class="space-y-4">
                        <div class="flex justify-between items-start">
                            <span class="px-3 py-1 rounded-full bg-[#22376D]/10 text-[#22376D] font-bold text-xs uppercase tracking-wider border border-[#22376D]/20">
                                6 Cursos • 1,080 Horas Presenciales
                            </span>
                            <div class="w-10 h-10 rounded-xl bg-red-50 text-red-700 flex items-center justify-center font-bold">
                                <i data-lucide="car" class="w-5 h-5"></i>
                            </div>
                        </div>
                        <div>
                            <h3 class="text-xl sm:text-2xl font-bold brand-serif text-[#22376D]">
                                Mecánica Automotriz y Motocicletas
                            </h3>
                            <p class="text-slate-600 text-xs sm:text-sm mt-2 leading-relaxed">
                                Diagnóstico computarizado avanzado en protocolos CAN-Bus e ISO 14229, inyección directa GDI y Common Rail Diésel, osciloscopio automotriz, mecánica de motocicletas 4T/2T con inyección electrónica EFI y servicio a sistemas R-134a/R-1234yf de climatización.
                            </p>
                        </div>
                        
                        <div class="space-y-1.5 pt-2 border-t border-slate-100">
                            <div class="text-[11px] font-bold uppercase tracking-wider text-slate-400">Cursos de la Especialidad:</div>
                            <div class="grid grid-cols-2 gap-2 text-xs text-slate-700">
                                <div class="flex items-center gap-1.5">• Mecanismos del Automóvil (180h)</div>
                                <div class="flex items-center gap-1.5">• Motores a Gasolina (180h)</div>
                                <div class="flex items-center gap-1.5">• Inyección Electrónica (180h)</div>
                                <div class="flex items-center gap-1.5">• Electricidad Automotriz (180h)</div>
                                <div class="flex items-center gap-1.5">• Mecánica de Motos (180h)</div>
                                <div class="flex items-center gap-1.5">• Aire Acondicionado Auto (180h)</div>
                            </div>
                        </div>
                    </div>

                    <div class="pt-4 border-t border-slate-100 flex items-center justify-between">
                        <span class="text-[11px] text-slate-500 font-medium">
                            <strong>Normas:</strong> SAE J1939 • OBD-II / CAN • EPA 609
                        </span>
                        <button onclick="filtrarArea('automotriz')" class="px-4 py-2 rounded-xl bg-[#22376D] hover:bg-[#152244] text-white text-xs font-bold transition flex items-center gap-1">
                            Ver Temarios <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
                        </button>
                    </div>
                </div>

            </div>

        </section>

        <!-- ===================================================== -->
        <!-- SECCIÓN 2: VISOR INTERACTIVO DE AUDITORÍA CURRICULAR  -->
        <!-- ===================================================== -->
        <section id="auditoria-interactiva" class="space-y-6 bg-white rounded-3xl border border-slate-200 p-6 sm:p-8 shadow-sm scroll-mt-24">
            
            <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-3 border-b border-slate-200 pb-4">
                <div>
                    <span class="text-xs font-bold text-[#EC9123] tracking-widest uppercase">Muestra Interactiva de Dictámenes</span>
                    <h2 class="text-2xl sm:text-3xl font-bold brand-serif text-[#22376D] mt-0.5">
                        Matriz de Cambios Curriculares e Inteligencia Artificial
                    </h2>
                </div>
                
                <!-- Filtros por Código de Color Oficial -->
                <div class="flex items-center gap-1.5 flex-wrap">
                    <button onclick="filtrarEstado('todos')" id="btn-filtro-todos" class="px-3 py-1.5 rounded-lg bg-[#22376D] text-white font-bold text-xs transition">
                        Todos (Muestra)
                    </button>
                    <button onclick="filtrarEstado('delete')" id="btn-filtro-delete" class="px-3 py-1.5 rounded-lg bg-red-50 text-red-700 hover:bg-red-100 font-bold text-xs transition border border-red-200">
                        🔴 Eliminar
                    </button>
                    <button onclick="filtrarEstado('update')" id="btn-filtro-update" class="px-3 py-1.5 rounded-lg bg-amber-50 text-amber-800 hover:bg-amber-100 font-bold text-xs transition border border-amber-200">
                        🟡 Actualizar
                    </button>
                    <button onclick="filtrarEstado('new')" id="btn-filtro-new" class="px-3 py-1.5 rounded-lg bg-blue-50 text-blue-800 hover:bg-blue-100 font-bold text-xs transition border border-blue-200">
                        🔵 Nuevo
                    </button>
                    <button onclick="filtrarEstado('keep')" id="btn-filtro-keep" class="px-3 py-1.5 rounded-lg bg-emerald-50 text-emerald-800 hover:bg-emerald-100 font-bold text-xs transition border border-emerald-200">
                        🟢 Mantener
                    </button>
                    <button onclick="filtrarEstado('ia')" id="btn-filtro-ia" class="px-3 py-1.5 rounded-lg bg-purple-50 text-purple-800 hover:bg-purple-100 font-bold text-xs transition border border-purple-200">
                        🟣 IA Aplicada
                    </button>
                </div>
            </div>

            <!-- Listado de temas auditados con código de color -->
            <div id="lista-dictamenes" class="space-y-3 pt-2">
                
                <!-- Item 1: Eliminar -->
                <div class="dictamen-card status-delete p-4 rounded-xl text-xs space-y-1 transition" data-status="delete">
                    <div class="flex justify-between items-center font-bold">
                        <span class="text-sm">🔴 Obsoleto: Mampostería no confinada y mezcla en pala sin dosificación</span>
                        <span class="uppercase tracking-wider text-[10px] bg-red-100 px-2 py-0.5 rounded">Dictamen: Eliminar</span>
                    </div>
                    <p class="text-slate-700"><strong>Justificación Técnica:</strong> Prohibido taxativamente por la Norma Sísmica AGIES NSE-4 de Guatemala. El mercado formal exige mampostería reforzada confinada con columnas de amarre y mortero dosificado por volumen.</p>
                </div>

                <!-- Item 2: Actualizar -->
                <div class="dictamen-card status-update p-4 rounded-xl text-xs space-y-1 transition" data-status="update">
                    <div class="flex justify-between items-center font-bold">
                        <span class="text-sm">🟡 Modernización: Diagnóstico de inyección electrónica con analizador de gases a OBD-II/CAN-Bus</span>
                        <span class="uppercase tracking-wider text-[10px] bg-amber-100 px-2 py-0.5 rounded">Dictamen: Actualizar</span>
                    </div>
                    <p class="text-slate-700"><strong>Justificación Técnica:</strong> Más del 85% del parque vehicular en Guatemala opera bajo redes multiplexadas CAN-Bus y módulos ECM con protocolos UDS. Se incorpora osciloscopio digital y escáner bidireccional.</p>
                </div>

                <!-- Item 3: Nuevo -->
                <div class="dictamen-card status-new p-4 rounded-xl text-xs space-y-1 transition" data-status="new">
                    <div class="flex justify-between items-center font-bold">
                        <span class="text-sm">🔵 Nueva Competencia: Generación Solar Fotovoltaica On-Grid y Medición Bidireccional</span>
                        <span class="uppercase tracking-wider text-[10px] bg-blue-100 px-2 py-0.5 rounded">Dictamen: Nuevo</span>
                    </div>
                    <p class="text-slate-700"><strong>Justificación Técnica:</strong> Alta demanda industrial y residencial amparada por la Resolución CNEE-186-2008 de Autoproductores en Guatemala. Incluye dimensionamiento de inversores y protecciones DC/AC.</p>
                </div>

                <!-- Item 4: IA Aplicada -->
                <div class="dictamen-card status-ia p-4 rounded-xl text-xs space-y-1 transition" data-status="ia">
                    <div class="flex justify-between items-center font-bold">
                        <span class="text-sm">🟣 Inteligencia Artificial: Diagnóstico predictivo de fallas de aislamiento con Computer Vision</span>
                        <span class="uppercase tracking-wider text-[10px] bg-purple-100 px-2 py-0.5 rounded">Dictamen: IA Aplicada</span>
                    </div>
                    <p class="text-slate-700"><strong>Aplicación en Taller:</strong> Los aprendices utilizan modelos de visión artificial para inspeccionar patrones térmicos termográficos en tableros de potencia y predecir puntos calientes antes de una parada de planta.</p>
                </div>

                <!-- Item 5: Mantener -->
                <div class="dictamen-card status-keep p-4 rounded-xl text-xs space-y-1 transition" data-status="keep">
                    <div class="flex justify-between items-center font-bold">
                        <span class="text-sm">🟢 Fundamento Esencial: Ley de Ohm, Ley de Watt y Circuitos RLC en Corriente Alterna</span>
                        <span class="uppercase tracking-wider text-[10px] bg-emerald-100 px-2 py-0.5 rounded">Dictamen: Mantener</span>
                    </div>
                    <p class="text-slate-700"><strong>Justificación Técnica:</strong> Base inmutable del análisis electrotécnico. Obligatorio para cálculo de calibre de conductores, caída de tensión y corrección del factor de potencia.</p>
                </div>

            </div>

        </section>

        <!-- ===================================================== -->
        <!-- SECCIÓN 3: FUNDAMENTACIÓN INSTITUCIONAL Y PEDAGÓGICA  -->
        <!-- ===================================================== -->
        <section id="metodologia" class="bg-gradient-to-br from-[#152244] to-[#22376D] text-white rounded-3xl p-8 sm:p-10 shadow-lg space-y-8 scroll-mt-24">
            
            <div class="border-b border-white/20 pb-4 flex flex-wrap justify-between items-end gap-3">
                <div>
                    <span class="text-xs font-bold text-[#EC9123] tracking-widest uppercase">Pilares Pedagógicos y Doctrinales</span>
                    <h2 class="text-2xl sm:text-3xl font-bold brand-serif text-white mt-1">
                        Marco Institucional de Fundación Kinal
                    </h2>
                </div>
                <img src="assets/el_trabajo_bien_hecho_blanco.png" alt="El trabajo bien hecho" class="h-6 w-auto object-contain">
            </div>

            <div class="grid md:grid-cols-2 gap-8 text-xs sm:text-sm text-slate-200 leading-relaxed">
                
                <div class="space-y-4 bg-white/5 p-6 rounded-2xl border border-white/10">
                    <h3 class="text-lg font-bold brand-serif text-[#EC9123] flex items-center gap-2">
                        <i data-lucide="compass" class="w-5 h-5"></i> Misión y Valores Institucionales
                    </h3>
                    <p>
                        <strong>Misión de Kinal:</strong> <em>«Formar a jóvenes y adultos a través de una educación integral, con énfasis en las áreas técnicas y tecnológicas, influyendo positivamente en su trabajo, su familia y la sociedad.»</em>
                    </p>
                    <p>
                        <strong>Valores de Kinal:</strong> <em>«Visión cristiana de la vida. Respeto a la dignidad de la persona. Espíritu de servicio. Trabajo bien hecho. Libertad personal responsable.»</em>
                    </p>
                    <p class="text-slate-300">
                        La labor formativa se realiza dentro de un espíritu cristiano cuya formación doctrinal y espiritual está confiada a la <strong>Prelatura del Opus Dei</strong>, institución de la Iglesia Católica.
                    </p>
                </div>

                <div class="space-y-4 bg-white/5 p-6 rounded-2xl border border-white/10">
                    <h3 class="text-lg font-bold brand-serif text-[#EC9123] flex items-center gap-2">
                        <i data-lucide="graduation-cap" class="w-5 h-5"></i> Formación Dual y Marco Alemán (DQR)
                    </h3>
                    <p>
                        <strong>Formación Profesional Dual:</strong> <em>«concepto de aprendizaje para jóvenes que tiene como objetivo preparar a los aprendices para su vida profesional, por lo que la formación se realiza en régimen de alternancia entre la escuela o el centro de formación y la empresa. El aprender en el proceso del trabajo es base y a la vez objetivo de la acción formativa.»</em>
                    </p>
                    <p>
                        <strong>Competencia según DQR:</strong> <em>«the ability and readiness of the individual to use knowledge, skills and personal, social and methodological competences and to behave in a considered, individual and socially responsible manner. Competence is understood in this sense as the comprehensive ability to act.»</em>
                    </p>
                    <p class="text-amber-300 font-semibold">
                        • Umbral de Aprobación Kinal: Calificación mínima de 75 puntos sobre 100.
                    </p>
                </div>

            </div>

        </section>

    </main>

    <!-- ========================================================= -->
    <!-- FOOTER INSTITUCIONAL                                      -->
    <!-- ========================================================= -->
    <footer class="bg-[#0D162C] text-white border-t-4 border-[#EC9123] py-12 px-4 sm:px-6 lg:px-8 mt-12">
        <div class="max-w-7xl mx-auto space-y-8">
            <div class="flex flex-col md:flex-row justify-between items-start md:items-center gap-6 border-b border-slate-800 pb-8">
                <div class="flex items-center gap-4">
                    <img src="assets/fundacion_kinal_blanco.png" alt="Fundación Kinal" class="h-10 sm:h-12 w-auto object-contain">
                    <span class="h-8 w-px bg-slate-700"></span>
                    <img src="assets/escuela_tecnica_superior_blanco.png" alt="Escuela Técnica Superior" class="h-8 sm:h-9 w-auto object-contain">
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

    <!-- Scripts Interactivos -->
    <script>
        lucide.createIcons();

        function filtrarEstado(estado) {
            const cards = document.querySelectorAll('.dictamen-card');
            cards.forEach(card => {
                if (estado === 'todos') {
                    card.style.display = 'block';
                } else {
                    card.style.display = (card.getAttribute('data-status') === estado) ? 'block' : 'none';
                }
            });

            // Resaltar botón activo
            const botones = ['todos', 'delete', 'update', 'new', 'keep', 'ia'];
            botones.forEach(btnId => {
                const b = document.getElementById('btn-filtro-' + btnId);
                if (b) {
                    if (btnId === estado) {
                        b.classList.add('ring-2', 'ring-offset-2', 'ring-[#22376D]');
                    } else {
                        b.classList.remove('ring-2', 'ring-offset-2', 'ring-[#22376D]');
                    }
                }
            });
        }

        function filtrarArea(slug) {
            alert('Has seleccionado el Área de ' + slug.toUpperCase() + '. Los temarios detallados y la auditoría completa están disponibles con la identidad gráfica oficial de Kinal.');
        }
    </script>
</body>
</html>
"""

target_file = os.path.join(TARGET_DIR, "index.html")
with open(target_file, "w", encoding="utf-8") as f:
    f.write(HTML_CONTENT)

print(f"Página generada exitosamente en: {target_file}")
"""
