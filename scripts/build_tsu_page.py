"""
Script para generar la página completa de TSU (tsu.html) y actualizar index.html
con la identidad gráfica oficial de Fundación Kinal y la Escuela Técnica Superior:
- Encabezado SIEMPRE VISIBLE (fixed top-0) para cambiar entre botones sin escrollear.
- Todos los botones del encabezado en color AZUL KINAL (#22376D).
- Inclusión de la sección de TSU en index.html.
- Creación de tsu.html con la malla curricular, líneas de formación, auditoría y bimestres.
- Favicon con el escudo de Kinal.
- Pie de página exclusivamente con el logo de Fundación Kinal en blanco.
"""

import os
import re

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGET_DIR = os.path.join(WORKSPACE_DIR, "rovalle-kinal.git", "remodelacion_revision_temarios")

TSU_HTML_CONTENT = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Técnico Superior Universitario (TSU) 3er Año | Escuela Técnica Superior — Fundación Kinal</title>
    
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

        h1, h2, h3, h4, .font-kinal-title, .brand-serif {
            font-family: "Times New Roman", Times, "Playfair Display", Georgia, serif;
            letter-spacing: -0.01em;
        }

        .hero-kinal-gradient {
            background: linear-gradient(135deg, #0D162C 0%, #152244 45%, #22376D 100%);
        }

        .status-delete { background-color: #FEF2F2; border-left: 4px solid #DC2626; color: #991B1B; }
        .status-update { background-color: #FEFCE8; border-left: 4px solid #EAB308; color: #854D0E; }
        .status-new    { background-color: #EFF6FF; border-left: 4px solid #2563EB; color: #1E40AF; }
        .status-keep   { background-color: #F0FDF4; border-left: 4px solid #16A34A; color: #166534; }
        .status-ia     { background-color: #FAF5FF; border-left: 4px solid #9333EA; color: #6B21A8; }

        @media (max-width: 767px) {
            *, *::before, *::after { box-sizing: border-box !important; }
            html, body { overflow-x: hidden !important; max-width: 100vw !important; }
            .no-scrollbar::-webkit-scrollbar { display: none !important; }
            .no-scrollbar { -ms-overflow-style: none !important; scrollbar-width: none !important; }
        }
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

        <!-- HEADER CORPORATIVO (SOLO LOGO ETS & BOTONES AZULES DE 1 PALABRA) -->
        <header class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-2.5 sm:py-3 flex flex-wrap justify-between items-center gap-3">
            <div class="flex items-center">
                <a href="index.html" class="flex items-center group">
                    <img src="assets/escuela_tecnica_superior.png" alt="Escuela Técnica Superior" class="h-8 sm:h-10 w-auto object-contain transition group-hover:opacity-90">
                </a>
            </div>

            <!-- Botones de Navegación Todos Azules de 1 Palabra -->
            <nav class="flex items-center gap-2 sm:gap-3 text-xs overflow-x-auto no-scrollbar py-1">
                <a href="index.html" class="px-3.5 py-2 rounded-lg bg-[#22376D] hover:bg-[#152244] text-white transition flex items-center gap-1.5 shadow-sm whitespace-nowrap font-bold">
                    <i data-lucide="home" class="w-4 h-4 text-[#EC9123]"></i> Inicio
                </a>
                <a href="#malla" class="px-3.5 py-2 rounded-lg bg-[#22376D] hover:bg-[#152244] text-white transition flex items-center gap-1.5 shadow-sm whitespace-nowrap font-bold ring-2 ring-[#EC9123]">
                    <i data-lucide="layers" class="w-4 h-4 text-[#EC9123]"></i> Malla
                </a>
                <a href="#lineas" class="px-3.5 py-2 rounded-lg bg-[#22376D] hover:bg-[#152244] text-white transition flex items-center gap-1.5 shadow-sm whitespace-nowrap font-bold">
                    <i data-lucide="git-branch" class="w-4 h-4 text-[#EC9123]"></i> Líneas
                </a>
                <a href="#bimestres" class="px-3.5 py-2 rounded-lg bg-[#22376D] hover:bg-[#152244] text-white transition flex items-center gap-1.5 shadow-sm whitespace-nowrap font-bold">
                    <i data-lucide="calendar" class="w-4 h-4 text-[#EC9123]"></i> Bimestres
                </a>
                <a href="#auditoria" class="px-3.5 py-2 rounded-lg bg-[#22376D] hover:bg-[#152244] text-white transition flex items-center gap-1.5 shadow-sm whitespace-nowrap font-bold">
                    <i data-lucide="check-square" class="w-4 h-4 text-[#EC9123]"></i> Auditoría
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
                Malla curricular oficial, dosificación modular y auditoría curricular del 3er Año de Técnico Superior Universitario, avalado por la <strong>Universidad del Istmo (UNIS)</strong> y <strong>Fundación Kinal</strong>. Estructurado en 4 bimestres académicos modulares que integran la gestión de operaciones, ciencias exactas aplicadas y deontología profesional en régimen dual.
            </p>

            <!-- Cita Doctrinal y Formativa -->
            <div class="pt-1 text-xs text-slate-300">
                <span>Formación doctrinal y espiritual a cargo de la Prelatura del Opus Dei</span>
            </div>

            <!-- Métricas Clave Consolidadas del TSU -->
            <div class="grid grid-cols-2 md:grid-cols-4 gap-3 sm:gap-4 pt-4 text-left">
                <div class="bg-white/10 backdrop-blur rounded-2xl p-4 border border-white/15 space-y-1">
                    <div class="text-[11px] uppercase tracking-wider text-slate-300 font-bold">Asignaturas</div>
                    <div class="text-2xl sm:text-3xl font-bold brand-serif text-white">16 Cursos</div>
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
        <!-- SECCIÓN 1: MALLA CURRICULAR Y MAPA DE ASIGNATURAS     -->
        <!-- ===================================================== -->
        <section id="malla" class="space-y-6 scroll-mt-36">
            
            <div class="flex flex-col sm:flex-row justify-between items-start sm:items-end gap-3 border-b-2 border-slate-200 pb-4">
                <div>
                    <span class="text-xs font-bold text-[#EC9123] tracking-widest uppercase">Malla Académica Oficial</span>
                    <h2 class="text-2xl sm:text-3xl font-bold brand-serif text-[#22376D] mt-1">
                        Distribución Curricular en 4 Bimestres Modulares
                    </h2>
                    <p class="text-slate-600 text-xs sm:text-sm mt-1 max-w-3xl leading-relaxed">
                        Estructura secuencial de las 16 materias universitarias del 3er año, organizadas por periodo lectivo con carga horaria y líneas de especialidad.
                    </p>
                </div>
                <span class="px-3 py-1 rounded-full bg-[#22376D]/10 text-[#22376D] font-bold text-xs border border-[#22376D]/20">
                    Ciclo 2026 • 3er Año Universitario
                </span>
            </div>

            <!-- Grilla Visual de los 4 Bimestres -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-5">
                
                <!-- Bimestre 1 -->
                <div class="bg-white rounded-2xl border border-slate-200 p-5 shadow-sm space-y-4 hover:border-[#22376D] transition">
                    <div class="border-b border-slate-100 pb-2 flex justify-between items-center">
                        <span class="font-bold text-[#22376D] brand-serif text-lg">Bimestre 1</span>
                        <span class="text-[11px] font-bold px-2 py-0.5 rounded-full bg-blue-100 text-blue-800">Ene - Mar</span>
                    </div>
                    <div class="space-y-2 text-xs">
                        <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-100 space-y-1">
                            <div class="font-bold text-slate-800">Fundamentos de Administración</div>
                            <div class="text-[11px] text-slate-500">Línea Gestión • 30 Horas</div>
                        </div>
                        <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-100 space-y-1">
                            <div class="font-bold text-slate-800">Planeación y Control del Trabajo</div>
                            <div class="text-[11px] text-slate-500">Línea Gestión • 30 Horas</div>
                        </div>
                        <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-100 space-y-1">
                            <div class="font-bold text-slate-800">Matemática Básica 1</div>
                            <div class="text-[11px] text-slate-500">Línea Matemáticas • 30 Horas</div>
                        </div>
                        <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-100 space-y-1">
                            <div class="font-bold text-slate-800">Física Básica 1</div>
                            <div class="text-[11px] text-slate-500">Línea Física • 30 Horas</div>
                        </div>
                        <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-100 space-y-1">
                            <div class="font-bold text-slate-800">Ética General 1</div>
                            <div class="text-[11px] text-slate-500">Línea Ética • 30 Horas</div>
                        </div>
                    </div>
                </div>

                <!-- Bimestre 2 -->
                <div class="bg-white rounded-2xl border border-slate-200 p-5 shadow-sm space-y-4 hover:border-[#22376D] transition">
                    <div class="border-b border-slate-100 pb-2 flex justify-between items-center">
                        <span class="font-bold text-[#22376D] brand-serif text-lg">Bimestre 2</span>
                        <span class="text-[11px] font-bold px-2 py-0.5 rounded-full bg-blue-100 text-blue-800">Mar - May</span>
                    </div>
                    <div class="space-y-2 text-xs">
                        <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-100 space-y-1">
                            <div class="font-bold text-slate-800">Administración de RRHH y SSO</div>
                            <div class="text-[11px] text-slate-500">Línea Gestión • 30 Horas</div>
                        </div>
                        <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-100 space-y-1">
                            <div class="font-bold text-slate-800">Herramientas Contables</div>
                            <div class="text-[11px] text-slate-500">Línea Gestión • 30 Horas</div>
                        </div>
                        <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-100 space-y-1">
                            <div class="font-bold text-slate-800">Matemática Básica 2</div>
                            <div class="text-[11px] text-slate-500">Línea Matemáticas • 30 Horas</div>
                        </div>
                        <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-100 space-y-1">
                            <div class="font-bold text-slate-800">Física Aplicada 1</div>
                            <div class="text-[11px] text-slate-500">Línea Física • 30 Horas</div>
                        </div>
                        <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-100 space-y-1">
                            <div class="font-bold text-slate-800">Ética General 2</div>
                            <div class="text-[11px] text-slate-500">Línea Ética • 30 Horas</div>
                        </div>
                    </div>
                </div>

                <!-- Bimestre 3 -->
                <div class="bg-white rounded-2xl border border-slate-200 p-5 shadow-sm space-y-4 hover:border-[#22376D] transition">
                    <div class="border-b border-slate-100 pb-2 flex justify-between items-center">
                        <span class="font-bold text-[#22376D] brand-serif text-lg">Bimestre 3</span>
                        <span class="text-[11px] font-bold px-2 py-0.5 rounded-full bg-blue-100 text-blue-800">Jun - Ago</span>
                    </div>
                    <div class="space-y-2 text-xs">
                        <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-100 space-y-1">
                            <div class="font-bold text-slate-800">Métodos de Producción</div>
                            <div class="text-[11px] text-slate-500">Línea Gestión • 30 Horas</div>
                        </div>
                        <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-100 space-y-1">
                            <div class="font-bold text-slate-800">Servicio al Cliente</div>
                            <div class="text-[11px] text-slate-500">Línea Gestión • 30 Horas</div>
                        </div>
                        <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-100 space-y-1">
                            <div class="font-bold text-slate-800">Matemática Aplicada 1</div>
                            <div class="text-[11px] text-slate-500">Línea Matemáticas • 30 Horas</div>
                        </div>
                        <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-100 space-y-1">
                            <div class="font-bold text-slate-800">Física Aplicada 2</div>
                            <div class="text-[11px] text-slate-500">Línea Física • 30 Horas</div>
                        </div>
                        <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-100 space-y-1">
                            <div class="font-bold text-slate-800">Ética Profesional 1</div>
                            <div class="text-[11px] text-slate-500">Línea Ética • 30 Horas</div>
                        </div>
                    </div>
                </div>

                <!-- Bimestre 4 -->
                <div class="bg-white rounded-2xl border border-slate-200 p-5 shadow-sm space-y-4 hover:border-[#22376D] transition">
                    <div class="border-b border-slate-100 pb-2 flex justify-between items-center">
                        <span class="font-bold text-[#22376D] brand-serif text-lg">Bimestre 4</span>
                        <span class="text-[11px] font-bold px-2 py-0.5 rounded-full bg-blue-100 text-blue-800">Ago - Oct</span>
                    </div>
                    <div class="space-y-2 text-xs">
                        <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-100 space-y-1">
                            <div class="font-bold text-slate-800">Control de Calidad</div>
                            <div class="text-[11px] text-slate-500">Línea Gestión • 30 Horas</div>
                        </div>
                        <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-100 space-y-1">
                            <div class="font-bold text-slate-800">Fundamentos de Marketing</div>
                            <div class="text-[11px] text-slate-500">Línea Gestión • 30 Horas</div>
                        </div>
                        <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-100 space-y-1">
                            <div class="font-bold text-slate-800">Matemática Aplicada 2</div>
                            <div class="text-[11px] text-slate-500">Línea Matemáticas • 30 Horas</div>
                        </div>
                        <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-100 space-y-1">
                            <div class="font-bold text-slate-800">Física Aplicada 3</div>
                            <div class="text-[11px] text-slate-500">Línea Física • 30 Horas</div>
                        </div>
                        <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-100 space-y-1">
                            <div class="font-bold text-slate-800">Ética Profesional 2</div>
                            <div class="text-[11px] text-slate-500">Línea Ética • 30 Horas</div>
                        </div>
                    </div>
                </div>

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

            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                
                <div class="bg-white rounded-3xl border border-slate-200 p-6 shadow-sm space-y-3">
                    <div class="flex items-center gap-3">
                        <div class="w-10 h-10 rounded-xl bg-blue-50 text-[#22376D] flex items-center justify-center font-bold">
                            <i data-lucide="briefcase" class="w-5 h-5"></i>
                        </div>
                        <div>
                            <h3 class="font-bold text-lg brand-serif text-[#22376D]">Gestión Empresarial y Operaciones</h3>
                            <span class="text-xs text-[#EC9123] font-bold">8 Materias • 240 Horas de Formación</span>
                        </div>
                    </div>
                    <p class="text-xs sm:text-sm text-slate-600 leading-relaxed">
                        Desarrolla habilidades directivas, planeación y control de proyectos, cumplimiento de normas de Salud y Seguridad Ocupacional (SSO Acuerdo Gubernativo 229-2014), control de costos, gestión de recursos humanos y calidad ISO 9001.
                    </p>
                </div>

                <div class="bg-white rounded-3xl border border-slate-200 p-6 shadow-sm space-y-3">
                    <div class="flex items-center gap-3">
                        <div class="w-10 h-10 rounded-xl bg-emerald-50 text-emerald-700 flex items-center justify-center font-bold">
                            <i data-lucide="calculator" class="w-5 h-5"></i>
                        </div>
                        <div>
                            <h3 class="font-bold text-lg brand-serif text-[#22376D]">Ciencias Matemáticas Aplicadas</h3>
                            <span class="text-xs text-[#EC9123] font-bold">4 Materias • 120 Horas de Formación</span>
                        </div>
                    </div>
                    <p class="text-xs sm:text-sm text-slate-600 leading-relaxed">
                        Modelado cuantitativo, trigonometría técnica, cálculo diferencial e integral enfocado a la resolución de problemas en ingeniería y procesos de manufactura industrial.
                    </p>
                </div>

                <div class="bg-white rounded-3xl border border-slate-200 p-6 shadow-sm space-y-3">
                    <div class="flex items-center gap-3">
                        <div class="w-10 h-10 rounded-xl bg-amber-50 text-amber-700 flex items-center justify-center font-bold">
                            <i data-lucide="activity" class="w-5 h-5"></i>
                        </div>
                        <div>
                            <h3 class="font-bold text-lg brand-serif text-[#22376D]">Física Técnica e Industrial</h3>
                            <span class="text-xs text-[#EC9123] font-bold">4 Materias • 120 Horas de Formación</span>
                        </div>
                    </div>
                    <p class="text-xs sm:text-sm text-slate-600 leading-relaxed">
                        Análisis estático y dinámico, cinemática de mecanismos, termodinámica de fluidos y recipientes de presión, y fundamentos de electromagnetismo aplicados a la automatización.
                    </p>
                </div>

                <div class="bg-white rounded-3xl border border-slate-200 p-6 shadow-sm space-y-3">
                    <div class="flex items-center gap-3">
                        <div class="w-10 h-10 rounded-xl bg-purple-50 text-purple-700 flex items-center justify-center font-bold">
                            <i data-lucide="scale" class="w-5 h-5"></i>
                        </div>
                        <div>
                            <h3 class="font-bold text-lg brand-serif text-[#22376D]">Ética y Deontología Profesional</h3>
                            <span class="text-xs text-[#EC9123] font-bold">4 Materias • 120 Horas de Formación</span>
                        </div>
                    </div>
                    <p class="text-xs sm:text-sm text-slate-600 leading-relaxed">
                        Formación antropológica, discernimiento moral cristiano, ética en los negocios, lealtad profesional, servicio a la sociedad y el principio institucional del <em>«Trabajo bien hecho»</em>.
                    </p>
                </div>

            </div>

        </section>

        <!-- ===================================================== -->
        <!-- SECCIÓN 3: AUDITORÍA CURRICULAR TRANSVERSAL           -->
        <!-- ===================================================== -->
        <section id="auditoria" class="space-y-6 bg-white rounded-3xl border border-slate-200 p-6 sm:p-8 shadow-sm scroll-mt-36">
            
            <div class="border-b border-slate-200 pb-4">
                <span class="text-xs font-bold text-[#EC9123] tracking-widest uppercase">Diagnóstico y Modernización Curricular</span>
                <h2 class="text-2xl sm:text-3xl font-bold brand-serif text-[#22376D] mt-1">
                    Dictámenes Curriculares del Programa TSU 2026
                </h2>
                <p class="text-xs sm:text-sm text-slate-600 mt-1">
                    Evaluación de actualización de contenidos para asegurar relevancia universitaria y rigor técnico.
                </p>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4 pt-2">
                <div class="status-update p-4 rounded-2xl border transition">
                    <span class="font-bold text-xs uppercase text-amber-700">🟡 Actualizar</span>
                    <h4 class="font-bold text-sm text-slate-900 mt-1">Normativa SSO Acuerdo 229-2014</h4>
                    <p class="text-xs text-slate-600 mt-1">Se actualiza con el protocolo de auditorías del Ministerio de Trabajo y Comités Bipartitos de Salud.</p>
                </div>
                <div class="status-new p-4 rounded-2xl border transition">
                    <span class="font-bold text-xs uppercase text-blue-700">🔵 Nuevo</span>
                    <h4 class="font-bold text-sm text-slate-900 mt-1">Herramientas Digitales y ERP</h4>
                    <p class="text-xs text-slate-600 mt-1">Inclusión de software contable moderno y tableros de control KPI en gestión de operaciones.</p>
                </div>
                <div class="status-ia p-4 rounded-2xl border transition">
                    <span class="font-bold text-xs uppercase text-purple-700">🟣 IA Aplicada</span>
                    <h4 class="font-bold text-sm text-slate-900 mt-1">Inteligencia Artificial en Calidad</h4>
                    <p class="text-xs text-slate-600 mt-1">Modelos de visión artificial para control estadístico de procesos y detección de no conformidades.</p>
                </div>
                <div class="status-keep p-4 rounded-2xl border transition">
                    <span class="font-bold text-xs uppercase text-green-700">🟢 Mantener</span>
                    <h4 class="font-bold text-sm text-slate-900 mt-1">Deontología Profesional Cristiana</h4>
                    <p class="text-xs text-slate-600 mt-1">Se conserva la base moral y doctrinal a cargo de la Prelatura del Opus Dei con enfoque ético universal.</p>
                </div>
                <div class="status-update p-4 rounded-2xl border transition">
                    <span class="font-bold text-xs uppercase text-amber-700">🟡 Actualizar</span>
                    <h4 class="font-bold text-sm text-slate-900 mt-1">Cálculo Diferencial e Integral Aplicado</h4>
                    <p class="text-xs text-slate-600 mt-1">Orientación práctica a curvas de carga, transferencia de calor y optimización de materiales.</p>
                </div>
                <div class="status-keep p-4 rounded-2xl border transition">
                    <span class="font-bold text-xs uppercase text-green-700">🟢 Mantener</span>
                    <h4 class="font-bold text-sm text-slate-900 mt-1">Umbral Aprobatorio de 75 Puntos</h4>
                    <p class="text-xs text-slate-600 mt-1">Estándar inmutable de excelencia de Fundación Kinal para cursos y exámenes por suficiencia.</p>
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

    <script>
        lucide.createIcons();
    </script>
</body>
</html>
"""

def generate_tsu_page():
    target_path = os.path.join(TARGET_DIR, "tsu.html")
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(TSU_HTML_CONTENT)
    print(f"[OK] tsu.html generado exitosamente: {target_path} ({len(TSU_HTML_CONTENT)} bytes)")

def update_index_with_fixed_header_and_tsu():
    target_index = os.path.join(TARGET_DIR, "index.html")
    with open(target_index, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Asegurar padding-top en el body para que el encabezado fijo no tape el contenido
    content = re.sub(r'<body class="([^"]*)"', r'<body class="\1 pt-[115px] sm:pt-[125px]"', content)
    # Limpiar duplicados si hubiere
    content = content.replace('pt-[115px] sm:pt-[125px] pt-[115px] sm:pt-[125px]', 'pt-[115px] sm:pt-[125px]')

    # 2. Hacer el encabezado fixed permanente
    # Reemplazar la barra superior y header por un contenedor fijo
    header_block_regex = re.compile(r'<!-- =+\s*BARRA INSTITUCIONAL SUPERIOR.*?<!-- =+\s*HERO PRINCIPAL', re.DOTALL)
    
    new_fixed_header = """<!-- ========================================================= -->
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

        <!-- HEADER CORPORATIVO (SOLO LOGO ETS & BOTONES AZULES DE 1 PALABRA) -->
        <header class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-2.5 sm:py-3 flex flex-wrap justify-between items-center gap-3">
            <div class="flex items-center">
                <a href="index.html" class="flex items-center group">
                    <img src="assets/escuela_tecnica_superior.png" alt="Escuela Técnica Superior" class="h-8 sm:h-10 w-auto object-contain transition group-hover:opacity-90">
                </a>
            </div>

            <!-- Navegación: Todos los botones azules de 1 palabra -->
            <nav class="flex items-center gap-2 sm:gap-3 text-xs overflow-x-auto no-scrollbar py-1">
                <a href="#areas" class="px-3.5 py-2 rounded-lg bg-[#22376D] hover:bg-[#152244] text-white transition flex items-center gap-1.5 shadow-sm whitespace-nowrap font-bold">
                    <i data-lucide="layers" class="w-4 h-4 text-[#EC9123]"></i> Áreas
                </a>
                <a href="#tsu" class="px-3.5 py-2 rounded-lg bg-[#22376D] hover:bg-[#152244] text-white transition flex items-center gap-1.5 shadow-sm whitespace-nowrap font-bold">
                    <i data-lucide="graduation-cap" class="w-4 h-4 text-[#EC9123]"></i> TSU
                </a>
                <a href="#auditoria-interactiva" class="px-3.5 py-2 rounded-lg bg-[#22376D] hover:bg-[#152244] text-white transition flex items-center gap-1.5 shadow-sm whitespace-nowrap font-bold">
                    <i data-lucide="check-square" class="w-4 h-4 text-[#EC9123]"></i> Dictámenes
                </a>
                <a href="#metodologia" class="px-3.5 py-2 rounded-lg bg-[#22376D] hover:bg-[#152244] text-white transition flex items-center gap-1.5 shadow-sm whitespace-nowrap font-bold">
                    <i data-lucide="file-badge" class="w-4 h-4 text-[#EC9123]"></i> DQR
                </a>
            </nav>
        </header>

    </div>

    <!-- ========================================================= -->
    <!-- HERO PRINCIPAL"""

    content = header_block_regex.sub(new_fixed_header, content)

    # 3. Insertar la sección de TSU antes de la SECCIÓN 2: AUDITORÍA INTERACTIVA si no está presente
    if 'id="tsu"' not in content:
        tsu_section_html = """
        <!-- ===================================================== -->
        <!-- SECCIÓN TSU: TÉCNICO SUPERIOR UNIVERSITARIO 3ER AÑO   -->
        <!-- ===================================================== -->
        <section id="tsu" class="space-y-8 scroll-mt-36">
            
            <div class="flex flex-col sm:flex-row justify-between items-start sm:items-end gap-3 border-b-2 border-slate-200 pb-4">
                <div>
                    <span class="text-xs font-bold text-[#EC9123] tracking-widest uppercase">Educación Superior Técnica • Aval UNIS</span>
                    <h2 class="text-2xl sm:text-4xl font-bold brand-serif text-[#22376D] mt-1">
                        Técnico Superior Universitario (TSU) — 3er Año
                    </h2>
                    <p class="text-slate-600 text-xs sm:text-sm mt-1 max-w-3xl leading-relaxed">
                        Programa de tercer año universitario avalado por la <strong>Universidad del Istmo (UNIS)</strong> y <strong>Fundación Kinal</strong>. Estructurado en 4 bimestres intensivos con 16 asignaturas modulares que combinan gestión operativa, ciencias aplicadas, ética profesional y formación dual en alternancia.
                    </p>
                </div>
                <a href="tsu.html" class="px-5 py-2.5 rounded-xl bg-[#22376D] hover:bg-[#152244] text-white text-xs font-bold transition flex items-center gap-2 shadow-sm whitespace-nowrap">
                    Portal TSU Completo <i data-lucide="arrow-right" class="w-4 h-4 text-[#EC9123]"></i>
                </a>
            </div>

            <!-- 4 Tarjetas de Líneas Curriculares del TSU -->
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
                
                <div class="bg-white rounded-2xl border border-slate-200 p-5 shadow-sm hover:border-[#22376D] transition flex flex-col justify-between space-y-3">
                    <div class="space-y-2">
                        <div class="w-9 h-9 rounded-lg bg-blue-50 text-[#22376D] flex items-center justify-center font-bold">
                            <i data-lucide="briefcase" class="w-5 h-5"></i>
                        </div>
                        <h3 class="font-bold text-base brand-serif text-[#22376D]">Gestión y Administración</h3>
                        <p class="text-xs text-slate-600 leading-relaxed">
                            Fundamentos de administración, SSO Acuerdo 229-2014, costos contables, calidad total y marketing industrial.
                        </p>
                    </div>
                    <div class="pt-2 border-t border-slate-100 text-[11px] text-[#EC9123] font-bold">
                        8 Asignaturas Modulares
                    </div>
                </div>

                <div class="bg-white rounded-2xl border border-slate-200 p-5 shadow-sm hover:border-[#22376D] transition flex flex-col justify-between space-y-3">
                    <div class="space-y-2">
                        <div class="w-9 h-9 rounded-lg bg-emerald-50 text-emerald-700 flex items-center justify-center font-bold">
                            <i data-lucide="calculator" class="w-5 h-5"></i>
                        </div>
                        <h3 class="font-bold text-base brand-serif text-[#22376D]">Matemáticas Aplicadas</h3>
                        <p class="text-xs text-slate-600 leading-relaxed">
                            Álgebra lineal, trigonometría técnica, cálculo diferencial e integral aplicado al modelado de ingeniería.
                        </p>
                    </div>
                    <div class="pt-2 border-t border-slate-100 text-[11px] text-[#EC9123] font-bold">
                        4 Asignaturas Modulares
                    </div>
                </div>

                <div class="bg-white rounded-2xl border border-slate-200 p-5 shadow-sm hover:border-[#22376D] transition flex flex-col justify-between space-y-3">
                    <div class="space-y-2">
                        <div class="w-9 h-9 rounded-lg bg-amber-50 text-amber-700 flex items-center justify-center font-bold">
                            <i data-lucide="activity" class="w-5 h-5"></i>
                        </div>
                        <h3 class="font-bold text-base brand-serif text-[#22376D]">Física Técnica</h3>
                        <p class="text-xs text-slate-600 leading-relaxed">
                            Mecánica vectorial, cinemática, termodinámica de procesos industriales, electromagnetismo y ondas.
                        </p>
                    </div>
                    <div class="pt-2 border-t border-slate-100 text-[11px] text-[#EC9123] font-bold">
                        4 Asignaturas Modulares
                    </div>
                </div>

                <div class="bg-white rounded-2xl border border-slate-200 p-5 shadow-sm hover:border-[#22376D] transition flex flex-col justify-between space-y-3">
                    <div class="space-y-2">
                        <div class="w-9 h-9 rounded-lg bg-purple-50 text-purple-700 flex items-center justify-center font-bold">
                            <i data-lucide="scale" class="w-5 h-5"></i>
                        </div>
                        <h3 class="font-bold text-base brand-serif text-[#22376D]">Ética y Deontología</h3>
                        <p class="text-xs text-slate-600 leading-relaxed">
                            Antropología, bioética, responsabilidad social corporativa y toma de decisiones éticas profesionales.
                        </p>
                    </div>
                    <div class="pt-2 border-t border-slate-100 text-[11px] text-[#EC9123] font-bold">
                        4 Asignaturas Modulares
                    </div>
                </div>

            </div>

            <!-- Malla Resumen de los 4 Bimestres -->
            <div class="bg-white rounded-3xl border border-slate-200 p-6 sm:p-8 shadow-sm space-y-6">
                <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2 border-b border-slate-200 pb-3">
                    <h3 class="text-lg sm:text-xl font-bold brand-serif text-[#22376D] flex items-center gap-2">
                        <i data-lucide="calendar-days" class="w-5 h-5 text-[#EC9123]"></i> Distribución Bimestral del 3er Año
                    </h3>
                    <span class="text-xs text-slate-500 font-semibold">Exigencia de Aprobación Kinal: ≥ 75 Pts / 100</span>
                </div>

                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 text-xs">
                    <div class="bg-slate-50 p-4 rounded-2xl border border-slate-200 space-y-2.5">
                        <div class="flex justify-between items-center font-bold text-[#22376D] border-b border-slate-200 pb-1.5">
                            <span>Bimestre 1</span>
                            <span class="text-[10px] bg-blue-100 text-blue-800 px-2 py-0.5 rounded-full">Enero - Marzo</span>
                        </div>
                        <ul class="space-y-1.5 text-slate-700">
                            <li>• Fundamentos de Administración</li>
                            <li>• Planeación y Control del Trabajo</li>
                            <li>• Matemática Básica 1</li>
                            <li>• Física Básica 1</li>
                            <li>• Ética General 1</li>
                        </ul>
                    </div>

                    <div class="bg-slate-50 p-4 rounded-2xl border border-slate-200 space-y-2.5">
                        <div class="flex justify-between items-center font-bold text-[#22376D] border-b border-slate-200 pb-1.5">
                            <span>Bimestre 2</span>
                            <span class="text-[10px] bg-blue-100 text-blue-800 px-2 py-0.5 rounded-full">Marzo - Mayo</span>
                        </div>
                        <ul class="space-y-1.5 text-slate-700">
                            <li>• Administración de RRHH y SSO</li>
                            <li>• Herramientas Contables</li>
                            <li>• Matemática Básica 2</li>
                            <li>• Física Aplicada 1</li>
                            <li>• Ética General 2</li>
                        </ul>
                    </div>

                    <div class="bg-slate-50 p-4 rounded-2xl border border-slate-200 space-y-2.5">
                        <div class="flex justify-between items-center font-bold text-[#22376D] border-b border-slate-200 pb-1.5">
                            <span>Bimestre 3</span>
                            <span class="text-[10px] bg-blue-100 text-blue-800 px-2 py-0.5 rounded-full">Junio - Agosto</span>
                        </div>
                        <ul class="space-y-1.5 text-slate-700">
                            <li>• Métodos de Producción</li>
                            <li>• Servicio al Cliente</li>
                            <li>• Matemática Aplicada 1</li>
                            <li>• Física Aplicada 2</li>
                            <li>• Ética Profesional 1</li>
                        </ul>
                    </div>

                    <div class="bg-slate-50 p-4 rounded-2xl border border-slate-200 space-y-2.5">
                        <div class="flex justify-between items-center font-bold text-[#22376D] border-b border-slate-200 pb-1.5">
                            <span>Bimestre 4</span>
                            <span class="text-[10px] bg-blue-100 text-blue-800 px-2 py-0.5 rounded-full">Agosto - Octubre</span>
                        </div>
                        <ul class="space-y-1.5 text-slate-700">
                            <li>• Control de Calidad</li>
                            <li>• Fundamentos de Marketing</li>
                            <li>• Matemática Aplicada 2</li>
                            <li>• Física Aplicada 3</li>
                            <li>• Ética Profesional 2</li>
                        </ul>
                    </div>
                </div>

                <div class="pt-3 border-t border-slate-200 flex flex-wrap justify-between items-center gap-3">
                    <div class="text-xs text-slate-500">
                        <strong>Título Otorgado:</strong> Técnico Superior Universitario con mención de especialidad • <strong>Aval Académico:</strong> Universidad del Istmo (UNIS)
                    </div>
                    <a href="tsu.html" class="px-4 py-2 rounded-xl bg-[#22376D] hover:bg-[#152244] text-white text-xs font-bold transition flex items-center gap-1.5 shadow-sm">
                        Ver Malla Curricular y Auditoría TSU <i data-lucide="arrow-right" class="w-3.5 h-3.5 text-[#EC9123]"></i>
                    </a>
                </div>
            </div>

        </section>
        """
        # Insertar antes de SECCIÓN 2: VISOR INTERACTIVO
        sec2_idx = content.find('<!-- ===================================================== -->\n        <!-- SECCIÓN 2: VISOR INTERACTIVO')
        if sec2_idx != -1:
            content = content[:sec2_idx] + tsu_section_html + "\n\n        " + content[sec2_idx:]
        else:
            # Si el comentario exacto difiere, buscar por id="auditoria-interactiva"
            aud_idx = content.find('id="auditoria-interactiva"')
            sec_start = content.rfind('<section', 0, aud_idx)
            content = content[:sec_start] + tsu_section_html + "\n\n        " + content[sec_start:]

    with open(target_index, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"[OK] index.html actualizado con encabezado fixed permanente y seccion TSU ({len(content)} bytes)")

if __name__ == "__main__":
    generate_tsu_page()
    update_index_with_fixed_header_and_tsu()
    print("Completado exitosamente.")
