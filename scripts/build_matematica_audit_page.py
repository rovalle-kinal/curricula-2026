#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador del Artefacto HTML y Markdown de Auditoría Curricular y Dosificación:
LÍNEA DE CIENCIAS EXACTAS Y ANALÍTICA CUANTITATIVA (4 Cursos / 40 Sesiones)
Grounded en la propuesta de Matemáticas 2027 y el Plan Maestro del TSU Kinal.
"""

import os
import shutil

def generate_matematica_html():
    html_content = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Auditoría Curricular y Dosificación: Matemáticas TSU 2026 | Fundación Kinal</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Plus Jakarta Sans', sans-serif; background-color: #f8fafc; color: #1e293b; }
        .font-mono { font-family: 'JetBrains Mono', monospace; }
        .item-keep { background: #f0fdf4; border-left: 4px solid #16a34a; }
        .item-update { background: #fefce8; border-left: 4px solid #ca8a04; }
        .item-new { background: #eff6ff; border-left: 4px solid #2563eb; }
        .item-delete { background: #fef2f2; border-left: 4px solid #dc2626; opacity: 0.9; }
        @media print { .no-print { display: none !important; } }
    </style>
</head>
<body class="min-h-screen flex flex-col">

    <!-- Top Navigation Bar -->
    <header class="bg-slate-900 text-white sticky top-0 z-50 border-b border-slate-800 shadow-md">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <div class="flex items-center gap-3">
                <div class="w-9 h-9 rounded-xl bg-emerald-600/30 border border-emerald-500/40 flex items-center justify-center text-amber-400 shadow-inner">
                    <i data-lucide="calculator" class="w-5 h-5"></i>
                </div>
                <div>
                    <span class="text-xs uppercase tracking-wider text-amber-400 font-extrabold block">Fundación Kinal • TSU 2026</span>
                    <h1 class="text-sm font-bold text-slate-100 flex items-center gap-2">
                        Auditoría Curricular: Línea de Ciencias Exactas y Analítica Cuantitativa
                    </h1>
                </div>
            </div>
            <div class="flex items-center gap-3 text-xs no-print">
                <a href="auditoria_curricular.html" class="px-3.5 py-1.5 rounded-lg bg-amber-500 hover:bg-amber-400 text-slate-950 transition flex items-center gap-1.5 font-bold shadow-sm text-xs">
                    <i data-lucide="arrow-left" class="w-3.5 h-3.5"></i> Volver a Auditoría General (20 Cursos)
                </a>
                <button onclick="window.print()" class="px-3.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 font-bold transition flex items-center gap-1.5 shadow-sm border border-slate-700">
                    <i data-lucide="printer" class="w-3.5 h-3.5"></i> Imprimir / PDF
                </button>
            </div>
        </div>
    </header>

    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-10 flex-1 w-full">

        <!-- Encabezado Principal y Contexto -->
        <section class="bg-gradient-to-br from-slate-900 via-emerald-950 to-slate-900 rounded-3xl p-6 sm:p-10 text-white shadow-xl relative overflow-hidden border border-slate-800">
            <div class="absolute -right-16 -top-16 w-80 h-80 bg-emerald-500/10 rounded-full blur-3xl pointer-events-none"></div>
            <div class="max-w-3xl space-y-4 relative z-10">
                <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-emerald-500/20 text-emerald-300 text-xs font-bold border border-emerald-400/30">
                    <i data-lucide="calculator" class="w-3.5 h-3.5 text-amber-400"></i> Diagnóstico Pedagógico y Metodológico 2026
                </div>
                <h2 class="text-2xl sm:text-4xl font-extrabold tracking-tight text-white leading-tight">
                    Auditoría Curricular Cuatricolor: Ciencias Exactas y Analítica Cuantitativa
                </h2>
                <p class="text-slate-300 text-sm sm:text-base leading-relaxed">
                    Evaluación sistemática de la <strong>Propuesta Curricular de Matemáticas</strong> (10 Módulos / 40 Clases). Se transforma la matemática tradicional abstracta en una herramienta cuantitativa instrumental para la toma de decisiones, optimización de recursos, control estadístico (SPC/OEE) y evaluación financiera de proyectos (VPN/TIR).
                </p>
                <div class="pt-2 flex flex-wrap gap-4 text-xs text-slate-300">
                    <div class="flex items-center gap-1.5 bg-slate-800/80 px-3 py-1.5 rounded-lg border border-slate-700">
                        <i data-lucide="layers" class="w-4 h-4 text-amber-400"></i> <strong>Estructura Analizada:</strong> 4 Bloques (A-D) • 10 Módulos • 40 Clases
                    </div>
                    <div class="flex items-center gap-1.5 bg-slate-800/80 px-3 py-1.5 rounded-lg border border-slate-700">
                        <i data-lucide="book-open" class="w-4 h-4 text-emerald-400"></i> <strong>Carga Anual:</strong> 4 Asignaturas Bimestrales • 54 Horas Presenciales
                    </div>
                    <div class="flex items-center gap-1.5 bg-slate-800/80 px-3 py-1.5 rounded-lg border border-slate-700">
                        <i data-lucide="award" class="w-4 h-4 text-blue-400"></i> <strong>Aprobación Mínima:</strong> 75 Puntos / 100
                    </div>
                </div>
            </div>
        </section>

        <!-- Métricas Resumen de Auditoría -->
        <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
            <div class="bg-white p-4 rounded-xl border border-emerald-200 shadow-sm flex items-center gap-3">
                <div class="w-10 h-10 rounded-lg bg-emerald-100 text-emerald-700 flex items-center justify-center font-bold text-lg">🟢</div>
                <div>
                    <div class="text-2xl font-black text-slate-900">18</div>
                    <div class="text-xs text-slate-500 font-medium">Temas Clásicos a Mantener</div>
                </div>
            </div>
            <div class="bg-white p-4 rounded-xl border border-amber-200 shadow-sm flex items-center gap-3">
                <div class="w-10 h-10 rounded-lg bg-amber-100 text-amber-800 flex items-center justify-center font-bold text-lg">🟡</div>
                <div>
                    <div class="text-2xl font-black text-slate-900">14</div>
                    <div class="text-xs text-slate-500 font-medium">Temas a Actualizar</div>
                </div>
            </div>
            <div class="bg-white p-4 rounded-xl border border-blue-200 shadow-sm flex items-center gap-3">
                <div class="w-10 h-10 rounded-lg bg-blue-100 text-blue-700 flex items-center justify-center font-bold text-lg">🔵</div>
                <div>
                    <div class="text-2xl font-black text-slate-900">12</div>
                    <div class="text-xs text-slate-500 font-medium">Temas Nuevos a Agregar</div>
                </div>
            </div>
            <div class="bg-white p-4 rounded-xl border border-red-200 shadow-sm flex items-center gap-3">
                <div class="w-10 h-10 rounded-lg bg-red-100 text-red-700 flex items-center justify-center font-bold text-lg">🔴</div>
                <div>
                    <div class="text-2xl font-black text-slate-900">8</div>
                    <div class="text-xs text-slate-500 font-medium">Temas Teóricos a Eliminar</div>
                </div>
            </div>
        </div>

        <!-- Barra de Control: Filtros y Acceso Rápido a Asignaturas -->
        <div class="p-5 rounded-2xl bg-white border border-slate-200 shadow-sm space-y-4 sticky top-16 z-40 bg-white/95 backdrop-blur-sm">
            <div class="flex flex-wrap items-center justify-between gap-4">
                <div>
                    <h3 class="text-xs font-bold text-slate-500 uppercase tracking-wider flex items-center gap-2">
                        <i data-lucide="filter" class="w-4 h-4 text-emerald-600"></i> Filtro Global de Auditoría (Aplica a Toda la Línea)
                    </h3>
                    <p class="text-xs text-slate-500 mt-0.5">Filtra simultáneamente los 52 elementos evaluados en las 4 asignaturas:</p>
                </div>
                <!-- Botones de Filtro -->
                <div class="flex flex-wrap items-center gap-2 text-xs font-semibold no-print">
                    <button onclick="filterAuditItems('all')" id="btn-filter-all" class="px-3 py-1.5 rounded-lg bg-slate-900 text-white shadow-sm transition">Todos (52)</button>
                    <button onclick="filterAuditItems('keep')" id="btn-filter-keep" class="px-3 py-1.5 rounded-lg bg-emerald-100 text-emerald-800 hover:bg-emerald-200 transition">🟢 Mantener (18)</button>
                    <button onclick="filterAuditItems('update')" id="btn-filter-update" class="px-3 py-1.5 rounded-lg bg-amber-100 text-amber-800 hover:bg-amber-200 transition">🟡 Actualizar (14)</button>
                    <button onclick="filterAuditItems('new')" id="btn-filter-new" class="px-3 py-1.5 rounded-lg bg-blue-100 text-blue-700 hover:bg-blue-200 transition">🔵 Agregar (12)</button>
                    <button onclick="filterAuditItems('delete')" id="btn-filter-delete" class="px-3 py-1.5 rounded-lg bg-red-100 text-red-700 hover:bg-red-200 transition">🔴 Eliminar (8)</button>
                </div>
            </div>

            <!-- Acceso Rápido a Asignaturas -->
            <div class="pt-3 border-t border-slate-100 flex items-center gap-2 overflow-x-auto text-xs no-print pb-1">
                <span class="text-slate-500 font-bold shrink-0 flex items-center gap-1">
                    <i data-lucide="compass" class="w-3.5 h-3.5"></i> Ir a Asignatura:
                </span>
                <a href="#bimestre-1" class="px-2.5 py-1 rounded bg-slate-100 text-slate-700 hover:bg-emerald-800 hover:text-white shrink-0 transition font-medium">B1: Aritmética & Excel (B1-C4)</a>
                <a href="#bimestre-2" class="px-2.5 py-1 rounded bg-slate-100 text-slate-700 hover:bg-emerald-800 hover:text-white shrink-0 transition font-medium">B2: Punto Equilibrio & Boole (B2-C4)</a>
                <a href="#bimestre-3" class="px-2.5 py-1 rounded bg-slate-100 text-slate-700 hover:bg-emerald-800 hover:text-white shrink-0 transition font-medium">B3: Estadística & Calidad OEE (B3-C4)</a>
                <a href="#bimestre-4" class="px-2.5 py-1 rounded bg-slate-100 text-slate-700 hover:bg-emerald-800 hover:text-white shrink-0 transition font-medium">B4: Ing. Económica VPN/TIR (B4-C4)</a>
            </div>
        </div>

        <!-- ========================================================================= -->
        <!-- CUADRÍCULA CONTINUA DE LOS 4 BIMESTRES (TODOS VISIBLES EN LA MISMA PÁGINA) -->
        <!-- ========================================================================= -->
        <section class="space-y-6">
            <div class="flex items-center justify-between">
                <div>
                    <h2 class="text-2xl font-extrabold text-slate-900 flex items-center gap-2">
                        <i data-lucide="layers" class="w-6 h-6 text-emerald-600"></i>
                        Estructura Curricular Auditada por Asignatura del Pensum
                    </h2>
                    <p class="text-xs text-slate-500 mt-1">Diagnóstico analítico que fundamenta la transición de la matemática abstracta a la analítica industrial.</p>
                </div>
            </div>

            <!-- Grid de 2 Columnas con las 4 Asignaturas -->
            <div class="grid lg:grid-cols-2 gap-8 pt-2">

                <!-- ==================== BIMESTRE 1 ==================== -->
                <div id="bimestre-1" class="bg-white rounded-xl border border-slate-300 shadow-sm overflow-hidden flex flex-col scroll-mt-36">
                    <div class="bg-slate-900 text-white p-4 border-b border-slate-800">
                        <div class="flex justify-between items-center text-xs text-amber-400 font-semibold mb-1">
                            <span>BIMESTRE 1 • Período 4 (50 min)</span>
                            <span>Código: B1-C4 • 13.5 Horas</span>
                        </div>
                        <h4 class="text-lg font-bold">B1: Matemática Básica 1 — Aritmética Cuantitativa y Modelado en Excel</h4>
                        <p class="text-xs text-slate-300 mt-1">
                            <strong>Correspondencia en Propuesta:</strong> Bloque A (Módulos I y II parcial).
                        </p>
                        <p class="text-xs text-slate-300 mt-0.5">
                            <strong>Logro esperado:</strong> Desarrollar razonamiento proporcional, análisis dimensional sin errores de conversión y automatización de fórmulas algebraicas en hojas de cálculo para el taller técnico.
                        </p>
                    </div>
                    <div class="p-5 divide-y divide-slate-100 flex-1 space-y-2">

                        <div class="audit-item item-keep p-3 rounded text-xs space-y-1" data-category="keep">
                            <div class="flex justify-between items-center font-bold">
                                <span>1. Razones, Proporciones y Escalas en Planos</span>
                                <span class="px-2 py-0.5 rounded bg-emerald-200 text-emerald-900 text-[10px] font-extrabold uppercase">🟢 Mantener</span>
                            </div>
                            <p class="text-slate-700">Proporcionalidad directa e inversa aplicada a dosificaciones de mezclas técnicas, aleaciones mecánicas y lectura de escalas (1:50, 1:100).</p>
                        </div>

                        <div class="audit-item item-keep p-3 rounded text-xs space-y-1" data-category="keep">
                            <div class="flex justify-between items-center font-bold">
                                <span>2. Análisis Dimensional y Conversiones Críticas (SI vs. Inglés)</span>
                                <span class="px-2 py-0.5 rounded bg-emerald-200 text-emerald-900 text-[10px] font-extrabold uppercase">🟢 Mantener</span>
                            </div>
                            <p class="text-slate-700">Factores de conversión para presión (PSI, bar), caudal (GPM, L/min) y potencia (HP, kW), coexistentes en la industria guatemalteca.</p>
                        </div>

                        <div class="audit-item item-keep p-3 rounded text-xs space-y-1" data-category="keep">
                            <div class="flex justify-between items-center font-bold">
                                <span>3. Regla de Tres Compuesta y Rendimiento de Cuadrillas</span>
                                <span class="px-2 py-0.5 rounded bg-emerald-200 text-emerald-900 text-[10px] font-extrabold uppercase">🟢 Mantener</span>
                            </div>
                            <p class="text-slate-700">Cálculo de tiempos de producción, rendimiento de mano de obra y estimación de mermas/desperdicios de materiales.</p>
                        </div>

                        <div class="audit-item item-update p-3 rounded text-xs space-y-1" data-category="update">
                            <div class="flex justify-between items-center font-bold">
                                <span>4. Del Lenguaje Algebraico al Despeje de Fórmulas Técnicas</span>
                                <span class="px-2 py-0.5 rounded bg-yellow-200 text-yellow-900 text-[10px] font-extrabold uppercase">🟡 Actualizar</span>
                            </div>
                            <p class="text-slate-700"><strong>Actualización:</strong> Reorientar el álgebra abstracta hacia el despeje metódico de incógnitas en fórmulas físicas reales (Ley de Ohm, torsión, potencia, caudal).</p>
                        </div>

                        <div class="audit-item item-update p-3 rounded text-xs space-y-1" data-category="update">
                            <div class="flex justify-between items-center font-bold">
                                <span>5. Automatización de Fórmulas en Excel / Google Sheets</span>
                                <span class="px-2 py-0.5 rounded bg-yellow-200 text-yellow-900 text-[10px] font-extrabold uppercase">🟡 Actualizar</span>
                            </div>
                            <p class="text-slate-700"><strong>Actualización:</strong> Sustituir el cálculo manual a lápiz por plantillas paramétricas con referencias relativas y absolutas ($), funciones y validación.</p>
                        </div>

                        <div class="audit-item item-new p-3 rounded text-xs space-y-1" data-category="new">
                            <div class="flex justify-between items-center font-bold">
                                <span>6. Cálculo Riguroso de Tolerancias e Incertidumbre</span>
                                <span class="px-2 py-0.5 rounded bg-blue-200 text-blue-900 text-[10px] font-extrabold uppercase">🔵 Agregar</span>
                            </div>
                            <p class="text-blue-950 font-medium">Determinación matemática de límites admisibles superior e inferior en piezas y componentes; porcentajes de error admisible.</p>
                        </div>

                        <div class="audit-item item-delete p-3 rounded text-xs space-y-1" data-category="delete">
                            <div class="flex justify-between items-center font-bold">
                                <span>7. Factorización Abstracta Avanzada (Baldor)</span>
                                <span class="px-2 py-0.5 rounded bg-red-200 text-red-900 text-[10px] font-extrabold uppercase">🔴 Eliminar</span>
                            </div>
                            <p class="text-red-950 font-medium"><strong>Motivo:</strong> Manipulación simbólica abstracta sin aplicación práctica en el taller o supervisión técnica.</p>
                        </div>

                        <div class="audit-item item-delete p-3 rounded text-xs space-y-1" data-category="delete">
                            <div class="flex justify-between items-center font-bold">
                                <span>8. Demostraciones Formales de Teoremas Teóricos</span>
                                <span class="px-2 py-0.5 rounded bg-red-200 text-red-900 text-[10px] font-extrabold uppercase">🔴 Eliminar</span>
                            </div>
                            <p class="text-red-950 font-medium"><strong>Motivo:</strong> Exceso de formalismo matemático propio de licenciaturas puras, desconectado de la ingeniería aplicada del TSU.</p>
                        </div>

                    </div>
                </div>

                <!-- ==================== BIMESTRE 2 ==================== -->
                <div id="bimestre-2" class="bg-white rounded-xl border border-slate-300 shadow-sm overflow-hidden flex flex-col scroll-mt-36">
                    <div class="bg-slate-900 text-white p-4 border-b border-slate-800">
                        <div class="flex justify-between items-center text-xs text-amber-400 font-semibold mb-1">
                            <span>BIMESTRE 2 • Período 4 (50 min)</span>
                            <span>Código: B2-C4 • 13.5 Horas</span>
                        </div>
                        <h4 class="text-lg font-bold">B2: Matemática Básica 2 — Punto de Equilibrio, Lógica Booleana e Impuestos</h4>
                        <p class="text-xs text-slate-300 mt-1">
                            <strong>Correspondencia en Propuesta:</strong> Bloque A (Módulo III) y Bloque B (Módulos IV y V).
                        </p>
                        <p class="text-xs text-slate-300 mt-0.5">
                            <strong>Logro esperado:</strong> Modelar el punto de equilibrio operativo, dominar compuertas lógicas y diagramas de flujo ANSI/ISO, y calcular con rigor tributario el IVA, ISR y la planilla laboral.
                        </p>
                    </div>
                    <div class="p-5 divide-y divide-slate-100 flex-1 space-y-2">

                        <div class="audit-item item-keep p-3 rounded text-xs space-y-1" data-category="keep">
                            <div class="flex justify-between items-center font-bold">
                                <span>1. Funciones Lineales y Gráficas de Rendimiento vs. Tiempo</span>
                                <span class="px-2 py-0.5 rounded bg-emerald-200 text-emerald-900 text-[10px] font-extrabold uppercase">🟢 Mantener</span>
                            </div>
                            <p class="text-slate-700">Ecuación de la recta (y = mx + b), pendiente como tasa de variación y modelado de costos fijos y variables.</p>
                        </div>

                        <div class="audit-item item-update p-3 rounded text-xs space-y-1" data-category="update">
                            <div class="flex justify-between items-center font-bold">
                                <span>2. Punto de Equilibrio Operativo (Break-Even Point)</span>
                                <span class="px-2 py-0.5 rounded bg-yellow-200 text-yellow-900 text-[10px] font-extrabold uppercase">🟡 Actualizar</span>
                            </div>
                            <p class="text-slate-700"><strong>Actualización:</strong> Aterrizar el equilibrio en volumen mínimo de servicios o unidades producidas y análisis de sensibilidad en Excel.</p>
                        </div>

                        <div class="audit-item item-new p-3 rounded text-xs space-y-1" data-category="new">
                            <div class="flex justify-between items-center font-bold">
                                <span>3. Lógica Matemática, Álgebra de Boole y Compuertas</span>
                                <span class="px-2 py-0.5 rounded bg-blue-200 text-blue-900 text-[10px] font-extrabold uppercase">🔵 Agregar</span>
                            </div>
                            <p class="text-blue-950 font-medium">Tablas de verdad, compuertas (AND, OR, NOT, XOR) y condiciones lógicas complejas anidadas en Excel (SI, Y, O, BUSCARX).</p>
                        </div>

                        <div class="audit-item item-new p-3 rounded text-xs space-y-1" data-category="new">
                            <div class="flex justify-between items-center font-bold">
                                <span>4. Algoritmia y Diagramas de Flujo Normalizados (ANSI/ISO 5807)</span>
                                <span class="px-2 py-0.5 rounded bg-blue-200 text-blue-900 text-[10px] font-extrabold uppercase">🔵 Agregar</span>
                            </div>
                            <p class="text-blue-950 font-medium">Estructuración lógica de procedimientos técnicos, condiciones if/else y protocolos de diagnóstico de fallas.</p>
                        </div>

                        <div class="audit-item item-update p-3 rounded text-xs space-y-1" data-category="update">
                            <div class="flex justify-between items-center font-bold">
                                <span>5. Matemáticas Comerciales: Margen (Margin) vs. Marcado (Markup)</span>
                                <span class="px-2 py-0.5 rounded bg-yellow-200 text-yellow-900 text-[10px] font-extrabold uppercase">🟡 Actualizar</span>
                            </div>
                            <p class="text-slate-700"><strong>Actualización:</strong> Erradicar la confusión crítica entre margen sobre precio de venta y marcado sobre costo en cotizaciones de taller.</p>
                        </div>

                        <div class="audit-item item-new p-3 rounded text-xs space-y-1" data-category="new">
                            <div class="flex justify-between items-center font-bold">
                                <span>6. Estructura Impositiva Aplicada (SAT Guatemala): IVA e ISR</span>
                                <span class="px-2 py-0.5 rounded bg-blue-200 text-blue-900 text-[10px] font-extrabold uppercase">🔵 Agregar</span>
                            </div>
                            <p class="text-blue-950 font-medium">Cálculo de débito y crédito fiscal, retenciones del 5% o 7% del ISR y facturación electrónica (FEL).</p>
                        </div>

                        <div class="audit-item item-new p-3 rounded text-xs space-y-1" data-category="new">
                            <div class="flex justify-between items-center font-bold">
                                <span>7. Matemáticas de la Planilla Laboral y Prestaciones</span>
                                <span class="px-2 py-0.5 rounded bg-blue-200 text-blue-900 text-[10px] font-extrabold uppercase">🔵 Agregar</span>
                            </div>
                            <p class="text-blue-950 font-medium">Cálculo de retenciones laborales (IGSS 4.83%), cuotas patronales (12.67%: IGSS, IRTRA, INTECAP) y provisión de Aguinaldo y Bono 14.</p>
                        </div>

                        <div class="audit-item item-delete p-3 rounded text-xs space-y-1" data-category="delete">
                            <div class="flex justify-between items-center font-bold">
                                <span>8. Geometría Analítica de Cónicas Puras (Elipses/Hipérbolas Abstractas)</span>
                                <span class="px-2 py-0.5 rounded bg-red-200 text-red-900 text-[10px] font-extrabold uppercase">🔴 Eliminar</span>
                            </div>
                            <p class="text-red-950 font-medium"><strong>Motivo:</strong> Estudio de ecuaciones de segundo grado abstractas sin aplicación a la gestión o supervisión operativa.</p>
                        </div>

                    </div>
                </div>

                <!-- ==================== BIMESTRE 3 ==================== -->
                <div id="bimestre-3" class="bg-white rounded-xl border border-slate-300 shadow-sm overflow-hidden flex flex-col scroll-mt-36">
                    <div class="bg-slate-900 text-white p-4 border-b border-slate-800">
                        <div class="flex justify-between items-center text-xs text-amber-400 font-semibold mb-1">
                            <span>BIMESTRE 3 • Período 4 (50 min)</span>
                            <span>Código: B3-C4 • 13.5 Horas</span>
                        </div>
                        <h4 class="text-lg font-bold">B3: Matemática Aplicada 1 — Estadística Práctica, Calidad y Métrica OEE</h4>
                        <p class="text-xs text-slate-300 mt-1">
                            <strong>Correspondencia en Propuesta:</strong> Bloque D (Módulos IX y X).
                        </p>
                        <p class="text-xs text-slate-300 mt-0.5">
                            <strong>Logro esperado:</strong> Utilizar la estadística descriptiva y el principio de Pareto para analizar la variabilidad de procesos, calcular indicadores MTBF/MTTR y medir la eficiencia global de equipos (OEE).
                        </p>
                    </div>
                    <div class="p-5 divide-y divide-slate-100 flex-1 space-y-2">

                        <div class="audit-item item-keep p-3 rounded text-xs space-y-1" data-category="keep">
                            <div class="flex justify-between items-center font-bold">
                                <span>1. Medidas de Tendencia Central en Procesos Técnicos</span>
                                <span class="px-2 py-0.5 rounded bg-emerald-200 text-emerald-900 text-[10px] font-extrabold uppercase">🟢 Mantener</span>
                            </div>
                            <p class="text-slate-700">Media, mediana y moda aplicadas a tiempos de ciclo, volumen de producción y tiempos de bahía en taller.</p>
                        </div>

                        <div class="audit-item item-keep p-3 rounded text-xs space-y-1" data-category="keep">
                            <div class="flex justify-between items-center font-bold">
                                <span>2. Medidas de Dispersión y Variabilidad (Desviación Estándar)</span>
                                <span class="px-2 py-0.5 rounded bg-emerald-200 text-emerald-900 text-[10px] font-extrabold uppercase">🟢 Mantener</span>
                            </div>
                            <p class="text-slate-700">Rango, varianza y desviación estándar para evaluar la repetibilidad, precisión y consistencia de un proceso operativo.</p>
                        </div>

                        <div class="audit-item item-update p-3 rounded text-xs space-y-1" data-category="update">
                            <div class="flex justify-between items-center font-bold">
                                <span>3. Representación Gráfica: Histogramas y Detección de Outliers</span>
                                <span class="px-2 py-0.5 rounded bg-yellow-200 text-yellow-900 text-[10px] font-extrabold uppercase">🟡 Actualizar</span>
                            </div>
                            <p class="text-slate-700"><strong>Actualización:</strong> Generación automatizada en Excel con el complemento Analysis ToolPak para identificar sesgos y valores atípicos.</p>
                        </div>

                        <div class="audit-item item-keep p-3 rounded text-xs space-y-1" data-category="keep">
                            <div class="flex justify-between items-center font-bold">
                                <span>4. Principio de Pareto (Regla 80/20) y Estratificación</span>
                                <span class="px-2 py-0.5 rounded bg-emerald-200 text-emerald-900 text-[10px] font-extrabold uppercase">🟢 Mantener</span>
                            </div>
                            <p class="text-slate-700">Elaboración matemática de diagramas de Pareto (frecuencias absolutas y porcentajes acumulados) para priorizar causas raíz de fallas.</p>
                        </div>

                        <div class="audit-item item-update p-3 rounded text-xs space-y-1" data-category="update">
                            <div class="flex justify-between items-center font-bold">
                                <span>5. Correlación Lineal Simple (Coeficiente de Pearson)</span>
                                <span class="px-2 py-0.5 rounded bg-yellow-200 text-yellow-900 text-[10px] font-extrabold uppercase">🟡 Actualizar</span>
                            </div>
                            <p class="text-slate-700"><strong>Actualización:</strong> Relación empírica entre dos variables operativas (ej. temperatura vs. desgaste; voltaje vs. temperatura).</p>
                        </div>

                        <div class="audit-item item-new p-3 rounded text-xs space-y-1" data-category="new">
                            <div class="flex justify-between items-center font-bold">
                                <span>6. Indicadores de Mantenimiento: Cálculo de MTBF y MTTR</span>
                                <span class="px-2 py-0.5 rounded bg-blue-200 text-blue-900 text-[10px] font-extrabold uppercase">🔵 Agregar</span>
                            </div>
                            <p class="text-blue-950 font-medium">Tiempo Medio Entre Fallas (Mean Time Between Failures) y Tiempo Medio de Reparación (Mean Time to Repair) en líneas de producción.</p>
                        </div>

                        <div class="audit-item item-new p-3 rounded text-xs space-y-1" data-category="new">
                            <div class="flex justify-between items-center font-bold">
                                <span>7. Control Estadístico de Procesos (SPC) y Límites de Control</span>
                                <span class="px-2 py-0.5 rounded bg-blue-200 text-blue-900 text-[10px] font-extrabold uppercase">🔵 Agregar</span>
                            </div>
                            <p class="text-blue-950 font-medium">Gráficos de control $\bar{X}-R$ y límites de control superior e inferior (UCL/LCL = $\mu \pm 3\sigma$) para prevenir defectos.</p>
                        </div>

                        <div class="audit-item item-new p-3 rounded text-xs space-y-1" data-category="new">
                            <div class="flex justify-between items-center font-bold">
                                <span>8. Cálculo Matemático del Indicador OEE y Dashboard</span>
                                <span class="px-2 py-0.5 rounded bg-blue-200 text-blue-900 text-[10px] font-extrabold uppercase">🔵 Agregar</span>
                            </div>
                            <p class="text-blue-950 font-medium">Fórmula del OEE = Disponibilidad × Rendimiento × Calidad; presentación en tableros ejecutivos en Excel.</p>
                        </div>

                    </div>
                </div>

                <!-- ==================== BIMESTRE 4 ==================== -->
                <div id="bimestre-4" class="bg-white rounded-xl border border-slate-300 shadow-sm overflow-hidden flex flex-col scroll-mt-36">
                    <div class="bg-slate-900 text-white p-4 border-b border-slate-800">
                        <div class="flex justify-between items-center text-xs text-amber-400 font-semibold mb-1">
                            <span>BIMESTRE 4 • Período 4 (50 min)</span>
                            <span>Código: B4-C4 • 13.5 Horas</span>
                        </div>
                        <h4 class="text-lg font-bold">B4: Matemática Aplicada 2 — Ingeniería Económica y Evaluación Financiera (VPN/TIR)</h4>
                        <p class="text-xs text-slate-300 mt-1">
                            <strong>Correspondencia en Propuesta:</strong> Bloque C (Módulos VI y VII) y Bloque D (Módulo VIII).
                        </p>
                        <p class="text-xs text-slate-300 mt-0.5">
                            <strong>Logro esperado:</strong> Dominar el valor del dinero en el tiempo, calcular depreciaciones y evaluar financieramente proyectos técnicos mediante flujos de caja, VPN y TIR para sustentar compras de maquinaria (CAPEX).
                        </p>
                    </div>
                    <div class="p-5 divide-y divide-slate-100 flex-1 space-y-2">

                        <div class="audit-item item-keep p-3 rounded text-xs space-y-1" data-category="keep">
                            <div class="flex justify-between items-center font-bold">
                                <span>1. El Valor del Dinero en el Tiempo e Interés Compuesto</span>
                                <span class="px-2 py-0.5 rounded bg-emerald-200 text-emerald-900 text-[10px] font-extrabold uppercase">🟢 Mantener</span>
                            </div>
                            <p class="text-slate-700">Interés simple vs. compuesto; capitalización discreta y tasa efectiva anual (TEA) en el sistema financiero guatemalteco.</p>
                        </div>

                        <div class="audit-item item-update p-3 rounded text-xs space-y-1" data-category="update">
                            <div class="flex justify-between items-center font-bold">
                                <span>2. Presupuestación y Costeo Técnico (MPD, MOD y CIF)</span>
                                <span class="px-2 py-0.5 rounded bg-yellow-200 text-yellow-900 text-[10px] font-extrabold uppercase">🟡 Actualizar</span>
                            </div>
                            <p class="text-slate-700"><strong>Actualización:</strong> Cálculo del costo/hora real del técnico, cubicaje de materiales e integración del factor de imprevistos.</p>
                        </div>

                        <div class="audit-item item-update p-3 rounded text-xs space-y-1" data-category="update">
                            <div class="flex justify-between items-center font-bold">
                                <span>3. Modelos Matemáticos de Depreciación (Ley ISR GT)</span>
                                <span class="px-2 py-0.5 rounded bg-yellow-200 text-yellow-900 text-[10px] font-extrabold uppercase">🟡 Actualizar</span>
                            </div>
                            <p class="text-slate-700"><strong>Actualización:</strong> Método de línea recta conforme a la ley fiscal de Guatemala y método por unidades producidas en maquinaria.</p>
                        </div>

                        <div class="audit-item item-new p-3 rounded text-xs space-y-1" data-category="new">
                            <div class="flex justify-between items-center font-bold">
                                <span>4. Ciclo de Vida del Activo y Costo Total de Propiedad (TCO)</span>
                                <span class="px-2 py-0.5 rounded bg-blue-200 text-blue-900 text-[10px] font-extrabold uppercase">🔵 Agregar</span>
                            </div>
                            <p class="text-blue-950 font-medium">Modelado cuantitativo para decidir entre reparar maquinaria existente, arrendar (leasing) o comprar equipo nuevo automatizado.</p>
                        </div>

                        <div class="audit-item item-update p-3 rounded text-xs space-y-1" data-category="update">
                            <div class="flex justify-between items-center font-bold">
                                <span>5. Tablas de Amortización de Créditos Bancarios y Leasing</span>
                                <span class="px-2 py-0.5 rounded bg-yellow-200 text-yellow-900 text-[10px] font-extrabold uppercase">🟡 Actualizar</span>
                            </div>
                            <p class="text-slate-700"><strong>Actualización:</strong> Construcción en Excel de amortizaciones bajo Sistema Francés (cuota fija) y Alemán, desglosando capital, interés e IVA.</p>
                        </div>

                        <div class="audit-item item-keep p-3 rounded text-xs space-y-1" data-category="keep">
                            <div class="flex justify-between items-center font-bold">
                                <span>6. Flujos de Caja Proyectados y Evaluación con VPN / VNA</span>
                                <span class="px-2 py-0.5 rounded bg-emerald-200 text-emerald-900 text-[10px] font-extrabold uppercase">🟢 Mantener</span>
                            </div>
                            <p class="text-slate-700">Construcción del Flujo de Caja Libre (FCL), determinación de la TMAR y regla de decisión del Valor Presente Neto.</p>
                        </div>

                        <div class="audit-item item-keep p-3 rounded text-xs space-y-1" data-category="keep">
                            <div class="flex justify-between items-center font-bold">
                                <span>7. Tasa Interna de Retorno (TIR) y Periodo de Recuperación (Payback)</span>
                                <span class="px-2 py-0.5 rounded bg-emerald-200 text-emerald-900 text-[10px] font-extrabold uppercase">🟢 Mantener</span>
                            </div>
                            <p class="text-slate-700">Cálculo de la rentabilidad porcentual del proyecto (TIR) y tiempo de recuperación de la inversión simple y descontado.</p>
                        </div>

                        <div class="audit-item item-new p-3 rounded text-xs space-y-1" data-category="new">
                            <div class="flex justify-between items-center font-bold">
                                <span>8. Sustentación Cuantitativa de Solicitudes CAPEX</span>
                                <span class="px-2 py-0.5 rounded bg-blue-200 text-blue-900 text-[10px] font-extrabold uppercase">🔵 Agregar</span>
                            </div>
                            <p class="text-blue-950 font-medium">Defensa formal de presupuestos de inversión en maquinaria ante directores financieros y comités de inversión corporativos.</p>
                        </div>

                    </div>
                </div>

            </div>
        </section>

        <!-- ========================================================================= -->
        <!-- TABLA COMPLETA DEL NUEVO TEMARIO DOSIFICADO: 40 SESIONES ANUALES          -->
        <!-- ========================================================================= -->
        <section class="bg-white rounded-2xl border border-slate-300 shadow-sm p-6 sm:p-8 space-y-6">
            <div class="border-b border-slate-200 pb-4">
                <span class="text-xs uppercase tracking-wider text-emerald-600 font-extrabold">Estructura Didáctica Oficial 2026</span>
                <h3 class="text-2xl font-black text-slate-900 mt-1 flex items-center gap-2">
                    <i data-lucide="calendar-check" class="w-6 h-6 text-emerald-600"></i>
                    Nuevo Temario Dosificado: 40 Sesiones de Ciencias Exactas y Analítica Cuantitativa
                </h3>
                <p class="text-xs text-slate-500 mt-1">
                    Dosificación balanceada de 10 sesiones por bimestre (Período 4 de 50 minutos) totalmente articuladas con el Pensum TSU Kinal.
                </p>
            </div>

            <div class="overflow-x-auto">
                <table class="w-full text-left text-xs border-collapse">
                    <thead>
                        <tr class="bg-slate-900 text-white border-b-2 border-amber-400">
                            <th class="p-3 font-bold w-12 text-center">Bim.</th>
                            <th class="p-3 font-bold w-16 text-center">Sesión</th>
                            <th class="p-3 font-bold w-52">Asignatura en Pensum</th>
                            <th class="p-3 font-bold">Contenido Temático Dosificado</th>
                            <th class="p-3 font-bold w-60">Herramienta / Entregable</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-200 text-slate-700">

                        <!-- BIMESTRE 1 -->
                        <tr class="hover:bg-slate-50">
                            <td class="p-3 font-bold text-center text-emerald-900 bg-emerald-50/50" rowspan="10">B1</td>
                            <td class="p-3 font-semibold text-center bg-slate-50">1</td>
                            <td class="p-3 font-bold text-emerald-900" rowspan="10">
                                B1-C4 • Matemática Básica 1
                                <div class="text-[10px] text-slate-500 font-normal">Aritmética Cuantitativa, Proporcionalidad y Modelado en Excel (13.5h)</div>
                            </td>
                            <td class="p-3"><strong>Razones, Proporciones y Escalas:</strong> Aplicación directa a dosificación de mezclas técnicas, aleaciones y escalas en planos de planta.</td>
                            <td class="p-3"><span class="px-2 py-0.5 rounded bg-slate-100 text-slate-800 font-semibold">Taller de Dosificación y Escalas</span></td>
                        </tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">2</td><td class="p-3"><strong>Análisis Dimensional y Conversiones Críticas:</strong> Conversión rigurosa entre Sistema Internacional (SI) e Inglés (PSI, bar, HP, kW, GPM) y mermas.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-slate-100 text-slate-800 font-semibold">Calculadora Dimensional en Excel</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">3</td><td class="p-3"><strong>Regla de Tres Compuesta:</strong> Aplicación a tiempos de mecanizado, rendimiento de mano de obra y capacidad instalada de cuadrillas.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-slate-100 text-slate-800 font-semibold">Estimador de Rendimientos</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">4</td><td class="p-3"><strong>Estructuración de Hojas de Cálculo Profesionales:</strong> Referencias relativas y absolutas ($), funciones nativas y auditoría de fórmulas.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-emerald-100 text-emerald-800 font-semibold">Plantilla Maestra Paramétrica</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">5</td><td class="p-3"><strong>Lenguaje Algebraico en el Taller:</strong> Modelado matemático de problemas operativos; transformación de una necesidad técnica en ecuación.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-slate-100 text-slate-800 font-semibold">Ejercicios de Modelado en Planta</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">6</td><td class="p-3"><strong>Despeje Metódico de Fórmulas Técnicas:</strong> Manipulación rigurosa de ecuaciones de física, electricidad (Ley de Ohm, Joule) y mecánica (torque).</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-slate-100 text-slate-800 font-semibold">Guía de Despejes Técnicos</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">7</td><td class="p-3"><strong>Sistemas de Ecuaciones Lineales ($2 \times 2$):</strong> Resolución analítica y matricial en Excel aplicada a balance de mezclas y recursos concurrentes.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-emerald-100 text-emerald-800 font-semibold">Solución Matricial con MINVERSA</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">8</td><td class="p-3"><strong>Automatización de Fórmulas con Hoja Electrónica:</strong> Creación de simuladores numéricos de campo para técnicos operativos.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-emerald-100 text-emerald-800 font-semibold">Simulador de Taller en Excel</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">9</td><td class="p-3"><strong>Cálculo de Tolerancias e Incertidumbre:</strong> Porcentajes de error relativo, límites permisibles y precisión en instrumentos de medición.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-blue-100 text-blue-800 font-semibold">Reporte de Tolerancias Críticas</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">10</td><td class="p-3"><strong>Taller Integrador B1:</strong> Desarrollo y defensa de una herramienta automatizada de cubicaje y rendimientos en hoja electrónica.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-purple-100 text-purple-900 font-bold">Entregable: Libro Paramétrico B1</span></td></tr>

                        <!-- BIMESTRE 2 -->
                        <tr class="hover:bg-slate-50">
                            <td class="p-3 font-bold text-center text-blue-900 bg-blue-50/50" rowspan="10">B2</td>
                            <td class="p-3 font-semibold text-center bg-slate-50">11</td>
                            <td class="p-3 font-bold text-emerald-900" rowspan="10">
                                B2-C4 • Matemática Básica 2
                                <div class="text-[10px] text-slate-500 font-normal">Punto de Equilibrio, Modelado de Funciones y Lógica Booleana (13.5h)</div>
                            </td>
                            <td class="p-3"><strong>Funciones Matemáticas en la Industria:</strong> Curvas de rendimiento vs. tiempo y análisis de fallas por comportamiento gráfico.</td>
                            <td class="p-3"><span class="px-2 py-0.5 rounded bg-slate-100 text-slate-800 font-semibold">Gráficos de Comportamiento</span></td>
                        </tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">12</td><td class="p-3"><strong>La Función Lineal ($y = mx + b$):</strong> Modelado cuantitativo de costos fijos, costos variables unitarios e ingresos operativos.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-slate-100 text-slate-800 font-semibold">Modelo Lineal de Costos</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">13</td><td class="p-3"><strong>Punto de Equilibrio Operativo (Break-Even):</strong> Cálculo analítico y gráfico del volumen mínimo para evitar pérdidas; análisis de sensibilidad.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-amber-100 text-amber-900 font-semibold">Calculadora Break-Even Dinámica</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">14</td><td class="p-3"><strong>Lógica Proposicional y Álgebra de Boole:</strong> Tablas de verdad, compuertas (AND, OR, NOT, XOR) y simplificación de condiciones.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-blue-100 text-blue-800 font-semibold">Tablas de Verdad Operativas</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">15</td><td class="p-3"><strong>Lógica Condicional Avanzada en Excel:</strong> Funciones anidadas (SI, Y, O, BUSCARX, ESERROR) para reglas de negocio automáticas.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-emerald-100 text-emerald-800 font-semibold">Matriz Lógica en Hoja de Cálculo</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">16</td><td class="p-3"><strong>Algoritmia y Diagramas de Flujo (ANSI/ISO 5807):</strong> Estructuración gráfica de procesos técnicos, bucles y protocolos de diagnóstico.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-blue-100 text-blue-800 font-semibold">Diagrama de Flujo Normalizado</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">17</td><td class="p-3"><strong>Matemáticas Comerciales de Precios:</strong> Diferenciación crítica entre Margen sobre Ventas (Margin) y Marcado sobre Costo (Markup).</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-slate-100 text-slate-800 font-semibold">Fórmula de Tarifa Horaria</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">18</td><td class="p-3"><strong>Estructura Impositiva Aplicada (SAT):</strong> Matemáticas del IVA (débito/crédito fiscal, retenciones), regímenes de ISR y facturación electrónica.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-red-100 text-red-900 font-bold">Liquidación Fiscal de Proyecto</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">19</td><td class="p-3"><strong>Matemáticas de la Planilla Laboral:</strong> Cuotas laborales (4.83%) y patronales (12.67%), cálculo de Aguinaldo, Bono 14 y pasivo laboral.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-blue-100 text-blue-800 font-semibold">Planilla Paramétrica en Excel</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">20</td><td class="p-3"><strong>Taller Integrador B2:</strong> Simulación integral de costeo, equilibrio operativo y cálculo de impuestos para un contrato técnico.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-purple-100 text-purple-900 font-bold">Simulación Integral B2</span></td></tr>

                        <!-- BIMESTRE 3 -->
                        <tr class="hover:bg-slate-50">
                            <td class="p-3 font-bold text-center text-amber-900 bg-amber-50/50" rowspan="10">B3</td>
                            <td class="p-3 font-semibold text-center bg-slate-50">21</td>
                            <td class="p-3 font-bold text-emerald-900" rowspan="10">
                                B3-C4 • Matemática Aplicada 1
                                <div class="text-[10px] text-slate-500 font-normal">Estadística Práctica Aplicada, Principio de Pareto y Métrica OEE (13.5h)</div>
                            </td>
                            <td class="p-3"><strong>Recolección y Muestreo de Datos en Planta:</strong> Hojas de verificación estructuradas y tablas de distribución de frecuencias.</td>
                            <td class="p-3"><span class="px-2 py-0.5 rounded bg-slate-100 text-slate-800 font-semibold">Hoja de Verificación de Campo</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">22</td><td class="p-3"><strong>Medidas de Tendencia Central:</strong> Media aritmética, mediana y moda aplicadas a tiempos de entrega, paradas y volumen de piezas.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-slate-100 text-slate-800 font-semibold">Análisis Estadístico en Excel</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">23</td><td class="p-3"><strong>Medidas de Dispersión y Variabilidad:</strong> Varianza, desviación estándar muestral y rango para evaluar la estabilidad de un proceso.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-slate-100 text-slate-800 font-semibold">Cálculo de Desviación Estándar</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">24</td><td class="p-3"><strong>Visualización Gráfica y Outliers:</strong> Histogramas de frecuencias y diagramas de caja y bigotes (Boxplots) con Analysis ToolPak.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-emerald-100 text-emerald-800 font-semibold">Histograma y Boxplot en Excel</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">25</td><td class="p-3"><strong>Principio de Pareto (Regla 80/20):</strong> Elaboración de diagramas de Pareto con frecuencias y porcentajes acumulados para priorizar fallas.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-emerald-100 text-emerald-800 font-semibold">Diagrama de Pareto Automatizado</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">26</td><td class="p-3"><strong>Correlación Lineal Simple:</strong> Coeficiente de Pearson ($r$) y recta de regresión mínima cuadrada para análisis de causas concurrentes.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-slate-100 text-slate-800 font-semibold">Gráfico de Dispersión y Tendencia</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">27</td><td class="p-3"><strong>Métricas de Mantenimiento (MTBF y MTTR):</strong> Cálculo cuantitativo del Tiempo Medio Entre Fallas y Tiempo Medio de Reparación.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-blue-100 text-blue-800 font-semibold">Calculadora MTBF / MTTR</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">28</td><td class="p-3"><strong>Control Estadístico de Procesos (SPC):</strong> Gráficos de control $\bar{X}-R$ y determinación de límites superior e inferior ($\pm 3\sigma$).</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-blue-100 text-blue-800 font-semibold">Gráfico de Control SPC</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">29</td><td class="p-3"><strong>Cálculo Matemático del OEE:</strong> Medición cuantitativa de Disponibilidad, Rendimiento y Calidad de maquinaria.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-blue-100 text-blue-800 font-semibold">Fórmula y Registro de OEE</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">30</td><td class="p-3"><strong>Taller Integrador B3:</strong> Construcción de un tablero de control (Dashboard métrico) para gerencia con Pareto, SPC y OEE.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-purple-100 text-purple-900 font-bold">Dashboard de Métricas B3</span></td></tr>

                        <!-- BIMESTRE 4 -->
                        <tr class="hover:bg-slate-50">
                            <td class="p-3 font-bold text-center text-purple-900 bg-purple-50/50" rowspan="10">B4</td>
                            <td class="p-3 font-semibold text-center bg-slate-50">31</td>
                            <td class="p-3 font-bold text-emerald-900" rowspan="10">
                                B4-C4 • Matemática Aplicada 2
                                <div class="text-[10px] text-slate-500 font-normal">Ingeniería Económica, Interés Compuesto y Evaluación Financiera (VPN/TIR) (13.5h)</div>
                            </td>
                            <td class="p-3"><strong>Estructuración de Costos de Proyectos:</strong> Desglose cuantitativo de Materia Prima (MPD), Mano de Obra (MOD) y CIF.</td>
                            <td class="p-3"><span class="px-2 py-0.5 rounded bg-slate-100 text-slate-800 font-semibold">Presupuesto Técnico Desglosado</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">32</td><td class="p-3"><strong>Estimación Matemática y Cubicaje:</strong> Modelos cuantitativos para proyectos de obra/taller y factor de holgura por imprevistos.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-slate-100 text-slate-800 font-semibold">Memoria de Cubicaje Técnico</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">33</td><td class="p-3"><strong>Valor del Dinero en el Tiempo e Interés Compuesto:</strong> Capitalización discreta, tasas nominales vs. tasas efectivas anuales (TEA).</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-slate-100 text-slate-800 font-semibold">Simulador de Interés Compuesto</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">34</td><td class="p-3"><strong>Modelos de Depreciación de Maquinaria:</strong> Cálculo por línea recta (Ley ISR Guatemala) y por unidades de producción de equipo.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-slate-100 text-slate-800 font-semibold">Tabla de Depreciación Fiscal</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">35</td><td class="p-3"><strong>Gestión de Activos y Costo Total de Propiedad (TCO):</strong> Matemáticas del ciclo de vida: evaluar reparar vs. arrendar (leasing) vs. comprar.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-blue-100 text-blue-800 font-semibold">Modelo Comparativo TCO</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">36</td><td class="p-3"><strong>Anualidades y Amortización Bancaria en Excel:</strong> Construcción de tablas de cuota fija (Sistema Francés) y Sistema Alemán.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-emerald-100 text-emerald-800 font-semibold">Tabla de Amortización de Crédito</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">37</td><td class="p-3"><strong>Flujos de Caja Proyectados y TMAR:</strong> Construcción de flujos libres de caja y determinación de la tasa mínima de descuento.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-slate-100 text-slate-800 font-semibold">Flujo de Caja Libre en Excel</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">38</td><td class="p-3"><strong>Valor Presente Neto (VPN / VNA):</strong> Regla matemática de aceptación o rechazo de inversiones técnicas en maquinaria o software.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-emerald-100 text-emerald-800 font-semibold">Evaluación con Fórmula VNA</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">39</td><td class="p-3"><strong>Tasa Interna de Retorno (TIR) y Payback:</strong> Cálculo de la rentabilidad interna y tiempo de recuperación de capital invertido.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-emerald-100 text-emerald-800 font-semibold">Cálculo de TIR y Payback</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">40</td><td class="p-3"><strong>Taller Integrador Final (CAPEX):</strong> Sustentación cuantitativa y defensa financiera formal para la compra de un activo industrial.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-purple-100 text-purple-900 font-bold">Defensa Financiera de CAPEX</span></td></tr>

                    </tbody>
                </table>
            </div>
        </section>

        <!-- Síntesis y Dictamen Final -->
        <section class="bg-slate-900 text-white rounded-3xl p-6 sm:p-8 space-y-4 border border-slate-800">
            <h3 class="text-xl font-bold flex items-center gap-2 text-amber-400">
                <i data-lucide="check-circle-2" class="w-5 h-5"></i>
                Dictamen Académico y Articulación con el Plan Maestro TSU
            </h3>
            <p class="text-xs sm:text-sm text-slate-300 leading-relaxed">
                La propuesta curricular de <strong>Ciencias Exactas y Analítica Cuantitativa</strong> transforma radicalmente la enseñanza de las matemáticas técnicas:
            </p>
            <div class="grid md:grid-cols-3 gap-4 pt-2 text-xs text-slate-300">
                <div class="p-4 rounded-xl bg-slate-800/80 border border-slate-700 space-y-1">
                    <strong class="text-white block font-semibold">1. De la Abstracción al Taller</strong>
                    <p class="text-slate-400">Elimina trinomios y cónicas abstractas sin aplicación; enfoca en proporcionalidad, conversiones dimensionales y despeje de fórmulas técnicas reales.</p>
                </div>
                <div class="p-4 rounded-xl bg-slate-800/80 border border-slate-700 space-y-1">
                    <strong class="text-white block font-semibold">2. Control Estadístico y Calidad</strong>
                    <p class="text-slate-400">Dota al mando medio de herramientas cuantitativas para gestionar la planta: histogramas, principio de Pareto, gráficos SPC, MTBF/MTTR y OEE.</p>
                </div>
                <div class="p-4 rounded-xl bg-slate-800/80 border border-slate-700 space-y-1">
                    <strong class="text-white block font-semibold">3. Sustentación Financiera (CAPEX)</strong>
                    <p class="text-slate-400">Capacita al técnico para defender proyectos de inversión ante gerencia general utilizando el valor del dinero en el tiempo, amortizaciones, VPN y TIR.</p>
                </div>
            </div>
        </section>

    </main>

    <!-- Footer -->
    <footer class="bg-slate-950 text-slate-400 text-xs py-6 border-t border-slate-800 text-center">
        <p>Fundación Kinal • Dirección Académica / Coordinación Académica • Auditoría Curricular TSU 2026</p>
    </footer>

    <!-- Script de Filtro Interactivo -->
    <script>
        lucide.createIcons();

        function filterAuditItems(category) {
            const items = document.querySelectorAll('.audit-item');
            const buttons = ['all', 'keep', 'update', 'new', 'delete'];

            buttons.forEach(b => {
                const btn = document.getElementById('btn-filter-' + b);
                if (btn) {
                    btn.classList.remove('ring-2', 'ring-offset-2', 'ring-emerald-600', 'font-black');
                }
            });

            const activeBtn = document.getElementById('btn-filter-' + category);
            if (activeBtn) {
                activeBtn.classList.add('ring-2', 'ring-offset-2', 'ring-emerald-600', 'font-black');
            }

            items.forEach(item => {
                if (category === 'all') {
                    item.style.display = 'block';
                } else {
                    if (item.getAttribute('data-category') === category) {
                        item.style.display = 'block';
                    } else {
                        item.style.display = 'none';
                    }
                }
            });
        }
    </script>
</body>
</html>
"""
    with open("TSU/matematica_auditoria.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("TSU/matematica_auditoria.html generado con éxito.")

def generate_matematica_markdown():
    md_content = """# Auditoría Curricular y Propuesta de Temario Dosificado: Ciencias Exactas y Analítica Cuantitativa (TSU 2026)

**Institución:** Fundación Kinal  
**Programa:** Técnico Superior Universitario (TSU) — Año Académico Común (3er Año UNIS)  
**Línea de Estudio:** Ciencias Exactas Aplicadas y Analítica Cuantitativa  
**Documento Analizado:** PROPUESTA CURRICULAR DE MATEMÁTICAS AÑO ACADÉMICO 2027 (10 Módulos / 40 Clases)  
**Carga Horaria Anual:** 4 Asignaturas Bimestrales • 40 Sesiones (50 min) • 54 Horas Presenciales  
**Umbral Aprobatorio:** $\\ge 75/100$ puntos  

---

## 1. Resumen Ejecutivo del Diagnóstico Curricular

El documento curricular analizado propone una transformación profunda de la enseñanza matemática para el 3er año universitario del TSU. Supera el enfoque tradicional abstracto (centrado en factorización simbólica, identidades trigonométricas de memoria y geometría analítica pura) para reconvertirlo en un **eje instrumental cuantitativo** enfocado en:

1. **Aritmética de Planta y Modelado en Hojas de Cálculo (Excel):** Proporciones, factores de conversión dimensional rigurosos (Sistema Internacional vs. Inglés), tolerancias y despeje de fórmulas técnicas reales.
2. **Lógica Booleana y Matemáticas Comerciales:** Álgebra de Boole, diagramas de flujo ANSI/ISO, punto de equilibrio operativo (Break-Even) y cumplimiento fiscal de Guatemala (IVA, ISR, planillas con IGSS, IRTRA e INTECAP).
3. **Control Estadístico de Calidad y Métricas de Confiabilidad:** Medidas de dispersión, diagramas de Pareto (80/20), gráficos de control SPC, cálculo de confiabilidad (MTBF y MTTR) y medición de la eficiencia de equipos (OEE).
4. **Ingeniería Económica y Evaluación Financiera:** Interés compuesto, depreciación de maquinaria (Ley ISR GT), Costo Total de Propiedad (TCO), tablas de amortización bancaria y criterios de evaluación de inversiones (VPN / TIR / Payback) para sustentar solicitudes de capital (CAPEX).

---

## 2. Métricas Cuatricolores de la Auditoría

Se evaluaron **52 elementos curriculares** a lo largo de los 4 bimestres lectivos:

* 🟢 **18 Temas a Mantener (34.6%):** Aritmética de razones y proporciones, conversiones dimensionales rigurosas, regla de tres, despeje de fórmulas técnicas, funciones lineales, porcentajes, medidas de tendencia central y dispersión, principio de Pareto, interés compuesto, flujos de caja y criterios de evaluación VPN y TIR.
* 🟡 **14 Temas a Actualizar (26.9%):** Transición del cálculo manual a lápiz hacia hojas de cálculo en Excel; de la recta abstracta al punto de equilibrio operativo; de problemas financieros teóricos a tablas de amortización bancarias guatemaltecas (Francés/Alemán); del costeo genérico al cálculo de Mano de Obra (MOD) y cubicajes de materiales; de la depreciación teórica al marco fiscal de la SAT.
* 🔵 **12 Temas Nuevos a Agregar (23.1%):**
  * Lógica matemática booleana, compuertas y funciones lógicas anidadas en Excel.
  * Algoritmia y diagramación de flujo normalizada (ANSI/ISO 5807) para diagnóstico de fallas.
  * Estructura impositiva de Guatemala (SAT): matemáticas del IVA (débito/crédito) y regímenes del ISR.
  * Matemáticas de la planilla laboral: cuotas laborales (4.83%), patronales (12.67%), Aguinaldo y Bono 14.
  * Métricas industriales de confiabilidad: cálculo matemático de MTBF y MTTR.
  * Control Estadístico de Procesos (SPC): gráficos $\\bar{X}-R$ y límites de control $\\pm 3\\sigma$.
  * Cálculo matemático del OEE: Disponibilidad × Rendimiento × Calidad.
  * Costo Total de Propiedad (TCO): ciclo de vida para evaluar reparar vs. arrendar vs. comprar.
  * Diferenciación de precios comerciales: Margen sobre ventas (*Margin*) vs. Marcado sobre costo (*Markup*).
  * Tolerancias dimensionales y porcentaje de error admisible en mediciones.
  * Periodo de recuperación de inversión (Payback simple y descontado).
  * Sustentación cuantitativa y defensa de compras de capital (CAPEX) ante comités de dirección.
* 🔴 **8 Temas a Eliminar (15.4%):**
  * Factorización algebraica abstracta avanzada (casos de Baldor sin aplicación técnica).
  * Demostraciones formales de teoremas matemáticos teóricos.
  * Geometría analítica de secciones cónicas puras (hipérbolas y elipses abstractas).
  * Identidades trigonométricas complejas analíticas de memoria.
  * Matrices manuales de orden superior a $3\\times 3$ a lápiz (sustituidas por funciones de Excel).
  * Tablas manuales de logaritmos en papel.
  * Problemas comerciales con monedas o contextos foráneos desactualizados.
  * Ejercicios de aritmética básica repetitiva sin significado industrial.

---

## 3. Matriz de Correspondencia 1 a 1: Módulos de Propuesta vs. Pensum TSU

| Bimestre | Módulos en Propuesta Analizada | Asignatura en Pensum TSU (Línea Matemática) | Código | Horas / Carga | Logro Curricular Clave |
| :---: | :--- | :--- | :---: | :---: | :--- |
| **B1** | Bloque A: Módulos I y II (Aritmética y Fórmulas) | **Matemática Básica 1: Aritmética Cuantitativa y Excel** | `B1-C4` | P4 • 13.5h | Proporcionalidad, conversiones SI/Inglés, despeje de fórmulas y hojas paramétricas en Excel. |
| **B2** | Bloque A: Módulo III y Bloque B: Módulos IV y V | **Matemática Básica 2: Punto de Equilibrio y Lógica Booleana** | `B2-C4` | P4 • 13.5h | Punto de equilibrio (Break-Even), compuertas lógicas, diagramas de flujo ANSI e impuestos SAT. |
| **B3** | Bloque D: Módulos IX y X (Estadística y Control) | **Matemática Aplicada 1: Estadística Práctica y Métrica OEE** | `B3-C4` | P4 • 13.5h | Dispersión, histogramas, principio de Pareto, indicadores MTBF/MTTR, gráficos SPC y OEE. |
| **B4** | Bloque C: Módulos VI y VII y Bloque D: Módulo VIII | **Matemática Aplicada 2: Ing. Económica y Evaluación VPN/TIR** | `B4-C4` | P4 • 13.5h | Depreciación fiscal, TCO, tablas de amortización, flujos de caja, VPN, TIR y defensa CAPEX. |

---

## 4. Nuevo Temario Dosificado: 40 Sesiones Anuales (10 por Bimestre)

### BIMESTRE 1: Matemática Básica 1 — Aritmética Cuantitativa y Modelado en Excel (B1-C4)
* **Sesión 1:** Razones, Proporciones y Factores de Escala aplicados a Mezclas Técnicas y Planos de Planta.
* **Sesión 2:** Análisis Dimensional y Conversiones Críticas (SI vs. Inglés: PSI, bar, HP, kW, GPM) y Mermas.
* **Sesión 3:** Regla de Tres Compuesta aplicada a Tiempos de Mecanizado y Rendimiento de Cuadrillas.
* **Sesión 4:** Estructuración Profesional de Hojas de Cálculo: Referencias Absolutas ($), Funciones y Plantillas.
* **Sesión 5:** Lenguaje Algebraico en el Taller: Modelado Matemático de Problemas Operativos de Campo.
* **Sesión 6:** Despeje Metódico de Fórmulas Técnicas de Electricidad (Ohm), Mecánica (Torque) y Fluidos.
* **Sesión 7:** Sistemas de Ecuaciones Lineales ($2\\times 2$): Resolución Analítica y Matricial en Excel (MINVERSA).
* **Sesión 8:** Automatización de Ecuaciones en Excel: Creación de Simuladores Paramétricos para Técnicos.
* **Sesión 9:** Cálculo de Tolerancias Dimensionales, Porcentajes de Error Admisible e Incertidumbre.
* **Sesión 10:** Taller Integrador B1: Construcción y Defensa de una Herramienta Paramétrica de Rendimientos en Excel.

### BIMESTRE 2: Matemática Básica 2 — Punto de Equilibrio, Lógica Booleana e Impuestos (B2-C4)
* **Sesión 11:** Funciones Matemáticas en la Industria: Curvas de Rendimiento vs. Tiempo y Análisis de Fallas.
* **Sesión 12:** La Función Lineal ($y = mx + b$): Modelado de Costos Fijos, Costos Variables e Ingresos.
* **Sesión 13:** Punto de Equilibrio Operativo (Break-Even Point): Cálculo Analítico y Gráfico en Unidades y Quetzales.
* **Sesión 14:** Lógica Proposicional, Álgebra de Boole y Compuertas Lógicas (AND, OR, NOT, XOR).
* **Sesión 15:** Lógica Condicional Avanzada en Excel: Funciones Anidadas (SI, Y, O, BUSCARX) para Reglas de Operación.
* **Sesión 16:** Algoritmia y Diagramas de Flujo Normalizados (ANSI/ISO 5807) para Diagnóstico de Fallas.
* **Sesión 17:** Matemáticas Comerciales de Precios: Margen sobre Ventas (*Margin*) vs. Marcado sobre Costo (*Markup*).
* **Sesión 18:** Estructura Impositiva en Guatemala (SAT): Matemáticas del IVA (Débito/Crédito) y Retenciones del ISR.
* **Sesión 19:** Matemáticas de la Planilla Laboral: Cuotas Laborales (4.83%), Patronales (12.67%), Aguinaldo y Bono 14.
* **Sesión 20:** Taller Integrador B2: Simulación Integral de Costeo, Equilibrio Operativo e Impuestos en Excel.

### BIMESTRE 3: Matemática Aplicada 1 — Estadística Práctica, Calidad y Métrica OEE (B3-C4)
* **Sesión 21:** Recolección y Muestreo de Datos en Planta: Hojas de Verificación e Intervalos de Frecuencia.
* **Sesión 22:** Medidas de Tendencia Central (Media, Mediana, Moda) aplicadas a Tiempos de Entrega y Ciclos.
* **Sesión 23:** Medidas de Dispersión (Rango, Varianza, Desviación Estándar) para Evaluar la Estabilidad de Procesos.
* **Sesión 24:** Visualización Gráfica y Detección de Outliers: Histogramas y Diagramas de Caja (Boxplots).
* **Sesión 25:** Principio de Pareto (Regla 80/20): Elaboración de Curvas Acumuladas para Priorización de Fallas.
* **Sesión 26:** Correlación Lineal Simple: Coeficiente de Pearson ($r$) y Recta de Regresión para Causas Concurrentes.
* **Sesión 27:** Indicadores de Mantenimiento y Confiabilidad: Cálculo Matemático de MTBF y MTTR.
* **Sesión 28:** Control Estadístico de Procesos (SPC): Gráficos de Control $\\bar{X}-R$ y Límites $\\pm 3\\sigma$.
* **Sesión 29:** Cálculo Matemático del Indicador OEE: Disponibilidad × Rendimiento × Calidad de Maquinaria.
* **Sesión 30:** Taller Integrador B3: Construcción de un Dashboard de Control Estadístico de Calidad y OEE en Excel.

### BIMESTRE 4: Matemática Aplicada 2 — Ingeniería Económica y Evaluación Financiera (VPN/TIR) (B4-C4)
* **Sesión 31:** Estructuración de Costos de Proyectos: Desglose de Materia Prima (MPD), Mano de Obra (MOD) y CIF.
* **Sesión 32:** Estimación Matemática de Proyectos Complejos, Cubicajes y Factores de Holgura por Imprevistos.
* **Sesión 33:** El Valor del Dinero en el Tiempo: Interés Simple vs. Compuesto y Tasas Efectivas Anuales (TEA).
* **Sesión 34:** Modelos Matemáticos de Depreciación: Línea Recta (Ley ISR Guatemala) y Unidades Producidas.
* **Sesión 35:** Costo Total de Propiedad (TCO) y Ciclo de Vida: Evaluar Reparar vs. Arrendar (Leasing) vs. Comprar.
* **Sesión 36:** Anualidades y Amortización Bancaria en Excel: Tablas de Cuota Fija (Francés) y Sistema Alemán.
* **Sesión 37:** Flujos de Caja Proyectados (FCL) y Determinación de la Tasa Mínima de Rendimiento (TMAR).
* **Sesión 38:** Evaluación Financiera con Valor Presente Neto (VPN / VNA en Excel): Criterios de Aceptación.
* **Sesión 39:** Tasa Interna de Retorno (TIR) y Periodo de Recuperación del Capital (Payback Simple y Descontado).
* **Sesión 40:** Taller Integrador Final: Sustentación Cuantitativa y Defensa Financiera para Compra de Maquinaria (CAPEX).

---

## 5. Dictamen Académico y Articulación con el Plan Maestro TSU

1. **Relevancia Industrial Rigurosa:** Se erradica la matemática desconectada y memorística, transformándola en una disciplina viva de optimización, toma de decisiones y control de operaciones.
2. **Transferibilidad a las 7 Especialidades:** La analítica descriptiva (Pareto), la ingeniería económica (VPN/TIR) y el modelado en Excel son competencias transversales que potencian a los técnicos de electricidad, automotriz, mecánica, construcción, software, electrónica y telecomunicaciones.
3. **Artefactos Locales Generados:**
   - HTML Interactivo Continuo: `TSU/matematica_auditoria.html`
   - Réplica en Repositorio Local: `curricula-2026/TSU/matematica_auditoria.html`
   - Respaldo MyBrain: `MyBrain/01 - My Brain/Kinal/TSU/matematica_auditoria.html`
"""
    with open("TSU/TEMARIO_Y_AUDITORIA_MATEMATICA_TSU.md", "w", encoding="utf-8") as f:
        f.write(md_content)
    print("TSU/TEMARIO_Y_AUDITORIA_MATEMATICA_TSU.md generado con éxito.")

if __name__ == "__main__":
    generate_matematica_html()
    generate_matematica_markdown()
