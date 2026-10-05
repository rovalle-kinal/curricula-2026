#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador del Artefacto HTML y Markdown de Auditoría Curricular y Dosificación:
LÍNEA DE FORMACIÓN HUMANA, ÉTICA Y CIUDADANA (4 Cursos / 40 Sesiones)
Grounded en el plan de clase de Vinicio Donis y el Ideario de Fundación Kinal.
"""

import os
import shutil

def generate_etica_html():
    html_content = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Auditoría Curricular y Dosificación: Ética Profesional TSU 2026 | Fundación Kinal</title>
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
                <div class="w-9 h-9 rounded-xl bg-blue-600 flex items-center justify-center font-black text-white text-lg shadow-inner">
                    K
                </div>
                <div>
                    <span class="text-xs uppercase tracking-wider text-amber-400 font-extrabold block">Fundación Kinal • TSU 2026</span>
                    <h1 class="text-sm font-bold text-slate-100 flex items-center gap-2">
                        Auditoría Curricular: Línea de Formación Humana y Ética
                    </h1>
                </div>
            </div>
            <div class="flex items-center gap-3 text-xs no-print">
                <a href="index.html#linea-etica" class="px-3 py-1.5 rounded-lg bg-slate-800 text-slate-200 hover:bg-slate-700 transition flex items-center gap-1.5 font-semibold">
                    <i data-lucide="arrow-left" class="w-3.5 h-3.5 text-amber-400"></i> Pensum TSU
                </a>
                <button onclick="window.print()" class="px-3 py-1.5 rounded-lg bg-blue-600 hover:bg-blue-500 text-white font-bold transition flex items-center gap-1.5 shadow-sm">
                    <i data-lucide="printer" class="w-3.5 h-3.5"></i> Imprimir / PDF
                </button>
            </div>
        </div>
    </header>

    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-10 flex-1 w-full">

        <!-- Encabezado Principal y Contexto -->
        <section class="bg-gradient-to-br from-slate-900 via-blue-950 to-slate-900 rounded-3xl p-6 sm:p-10 text-white shadow-xl relative overflow-hidden border border-slate-800">
            <div class="absolute -right-16 -top-16 w-80 h-80 bg-blue-500/10 rounded-full blur-3xl pointer-events-none"></div>
            <div class="max-w-3xl space-y-4 relative z-10">
                <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-500/20 text-blue-300 text-xs font-bold border border-blue-400/30">
                    <i data-lucide="scale" class="w-3.5 h-3.5 text-amber-400"></i> Diagnóstico Pedagógico y Metodológico 2026
                </div>
                <h2 class="text-2xl sm:text-4xl font-extrabold tracking-tight text-white leading-tight">
                    Auditoría Curricular Cuatricolor: Curso de Ética Profesional
                </h2>
                <p class="text-slate-300 text-sm sm:text-base leading-relaxed">
                    Evaluación sistemática del programa de <strong>Ética Profesional</strong> impartido por el <strong>Prof. Vinicio Donis</strong>. Se contrastan los 38 temas de su plan actual con los requerimientos del mando medio en la <strong>Industria 4.0</strong>, los compromisos de la <strong>UNIS</strong> y los principios inmutables del <strong>Ideario de Fundación Kinal</strong>.
                </p>
                <div class="pt-2 flex flex-wrap gap-4 text-xs text-slate-300">
                    <div class="flex items-center gap-1.5 bg-slate-800/80 px-3 py-1.5 rounded-lg border border-slate-700">
                        <i data-lucide="user-check" class="w-4 h-4 text-amber-400"></i> <strong>Docente Analizado:</strong> Prof. Vinicio Donis
                    </div>
                    <div class="flex items-center gap-1.5 bg-slate-800/80 px-3 py-1.5 rounded-lg border border-slate-700">
                        <i data-lucide="book-open" class="w-4 h-4 text-emerald-400"></i> <strong>Carga Anual:</strong> 4 Bimestres • 40 Sesiones (50 min) • 54 Horas
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
                    <div class="text-2xl font-black text-slate-900">20</div>
                    <div class="text-xs text-slate-500 font-medium">Temas Clásicos a Mantener</div>
                </div>
            </div>
            <div class="bg-white p-4 rounded-xl border border-amber-200 shadow-sm flex items-center gap-3">
                <div class="w-10 h-10 rounded-lg bg-amber-100 text-amber-800 flex items-center justify-center font-bold text-lg">🟡</div>
                <div>
                    <div class="text-2xl font-black text-slate-900">12</div>
                    <div class="text-xs text-slate-500 font-medium">Temas a Actualizar</div>
                </div>
            </div>
            <div class="bg-white p-4 rounded-xl border border-blue-200 shadow-sm flex items-center gap-3">
                <div class="w-10 h-10 rounded-lg bg-blue-100 text-blue-700 flex items-center justify-center font-bold text-lg">🔵</div>
                <div>
                    <div class="text-2xl font-black text-slate-900">14</div>
                    <div class="text-xs text-slate-500 font-medium">Temas Nuevos a Agregar</div>
                </div>
            </div>
            <div class="bg-white p-4 rounded-xl border border-red-200 shadow-sm flex items-center gap-3">
                <div class="w-10 h-10 rounded-lg bg-red-100 text-red-700 flex items-center justify-center font-bold text-lg">🔴</div>
                <div>
                    <div class="text-2xl font-black text-slate-900">6</div>
                    <div class="text-xs text-slate-500 font-medium">Temas a Eliminar (Desviación)</div>
                </div>
            </div>
        </div>

        <!-- Barra de Control: Filtros y Acceso Rápido a Bimestres -->
        <div class="p-5 rounded-2xl bg-white border border-slate-200 shadow-sm space-y-4 sticky top-16 z-40 bg-white/95 backdrop-blur-sm">
            <div class="flex flex-wrap items-center justify-between gap-4">
                <div>
                    <h3 class="text-xs font-bold text-slate-500 uppercase tracking-wider flex items-center gap-2">
                        <i data-lucide="filter" class="w-4 h-4 text-blue-600"></i> Filtro Global de Auditoría (Aplica a los 4 Bimestres)
                    </h3>
                    <p class="text-xs text-slate-500 mt-0.5">Filtra simultáneamente los 52 elementos evaluados en toda la página:</p>
                </div>
                <!-- Botones de Filtro -->
                <div class="flex flex-wrap items-center gap-2 text-xs font-semibold no-print">
                    <button onclick="filterAuditItems('all')" id="btn-filter-all" class="px-3 py-1.5 rounded-lg bg-slate-900 text-white shadow-sm transition">Todos (52)</button>
                    <button onclick="filterAuditItems('keep')" id="btn-filter-keep" class="px-3 py-1.5 rounded-lg bg-emerald-100 text-emerald-800 hover:bg-emerald-200 transition">🟢 Mantener (20)</button>
                    <button onclick="filterAuditItems('update')" id="btn-filter-update" class="px-3 py-1.5 rounded-lg bg-amber-100 text-amber-800 hover:bg-amber-200 transition">🟡 Actualizar (12)</button>
                    <button onclick="filterAuditItems('new')" id="btn-filter-new" class="px-3 py-1.5 rounded-lg bg-blue-100 text-blue-700 hover:bg-blue-200 transition">🔵 Agregar (14)</button>
                    <button onclick="filterAuditItems('delete')" id="btn-filter-delete" class="px-3 py-1.5 rounded-lg bg-red-100 text-red-700 hover:bg-red-200 transition">🔴 Eliminar (6)</button>
                </div>
            </div>

            <!-- Acceso Rápido a Bimestres -->
            <div class="pt-3 border-t border-slate-100 flex items-center gap-2 overflow-x-auto text-xs no-print pb-1">
                <span class="text-slate-500 font-bold shrink-0 flex items-center gap-1">
                    <i data-lucide="compass" class="w-3.5 h-3.5"></i> Ir a Bimestre:
                </span>
                <a href="#bimestre-1" class="px-2.5 py-1 rounded bg-slate-100 text-slate-700 hover:bg-blue-900 hover:text-white shrink-0 transition font-medium">B1: Antropología y Sentido del Trabajo (B1-C1)</a>
                <a href="#bimestre-2" class="px-2.5 py-1 rounded bg-slate-100 text-slate-700 hover:bg-blue-900 hover:text-white shrink-0 transition font-medium">B2: Libertad, Firmas y Compliance (B2-C1)</a>
                <a href="#bimestre-3" class="px-2.5 py-1 rounded bg-slate-100 text-slate-700 hover:bg-blue-900 hover:text-white shrink-0 transition font-medium">B3: Deontología e Industria 4.0 (B3-C1)</a>
                <a href="#bimestre-4" class="px-2.5 py-1 rounded bg-slate-100 text-slate-700 hover:bg-blue-900 hover:text-white shrink-0 transition font-medium">B4: Bioética, HITL y Custodia Ambiental (B4-C1)</a>
            </div>
        </div>

        <!-- ========================================================================= -->
        <!-- CUADRÍCULA CONTINUA DE LOS 4 BIMESTRES (TODOS VISIBLES EN LA MISMA PÁGINA) -->
        <!-- ========================================================================= -->
        <section class="space-y-6">
            <div class="flex items-center justify-between">
                <div>
                    <h2 class="text-2xl font-extrabold text-slate-900 flex items-center gap-2">
                        <i data-lucide="layers" class="w-6 h-6 text-blue-600"></i>
                        Estructura Curricular Auditada por Bimestre Lectivo
                    </h2>
                    <p class="text-xs text-slate-500 mt-1">Análisis detallado tema por tema que fundamenta la propuesta dosificada de 40 sesiones.</p>
                </div>
            </div>

            <!-- Grid de 2 Columnas con los 4 Bloques Bimestrales -->
            <div class="grid lg:grid-cols-2 gap-8 pt-2">

                <!-- ==================== BIMESTRE 1 ==================== -->
                <div id="bimestre-1" class="bg-white rounded-xl border border-slate-300 shadow-sm overflow-hidden flex flex-col scroll-mt-36">
                    <div class="bg-slate-900 text-white p-4 border-b border-slate-800">
                        <div class="flex justify-between items-center text-xs text-amber-400 font-semibold mb-1">
                            <span>BIMESTRE 1 • Período 1 (50 min)</span>
                            <span>Código: B1-C1 • 13.5 Horas</span>
                        </div>
                        <h4 class="text-lg font-bold">B1: Ética General 1 — Antropología y Sentido del Trabajo</h4>
                        <p class="text-xs text-slate-300 mt-1">
                            <strong>Correspondencia en Donis:</strong> I Trimestre (Temas 1 al 10).
                        </p>
                        <p class="text-xs text-slate-300 mt-0.5">
                            <strong>Logro esperado:</strong> Comprender la dignidad inalienable de la persona, los actos humanos y convertir el trabajo bien hecho en medio de realización y servicio social bajo el Ideario de Kinal.
                        </p>
                    </div>
                    <div class="p-5 divide-y divide-slate-100 flex-1 space-y-2">

                        <div class="audit-item item-keep p-3 rounded text-xs space-y-1" data-category="keep">
                            <div class="flex justify-between items-center font-bold">
                                <span>1. Fundamentos de la Ética y Relación con Otras Ciencias</span>
                                <span class="px-2 py-0.5 rounded bg-emerald-200 text-emerald-900 text-[10px] font-extrabold uppercase">🟢 Mantener</span>
                            </div>
                            <p class="text-slate-700">Diferencia cardinal entre ética (filosofía moral normativa) y moral vivida. Su relación con el derecho y la técnica.</p>
                        </div>

                        <div class="audit-item item-keep p-3 rounded text-xs space-y-1" data-category="keep">
                            <div class="flex justify-between items-center font-bold">
                                <span>2. El Bien Moral como Fin Natural del Hombre</span>
                                <span class="px-2 py-0.5 rounded bg-emerald-200 text-emerald-900 text-[10px] font-extrabold uppercase">🟢 Mantener</span>
                            </div>
                            <p class="text-slate-700">El bien como objeto de la voluntad y fin de la acción humana. Distinción entre bien honesto, bien útil y bien placentero.</p>
                        </div>

                        <div class="audit-item item-keep p-3 rounded text-xs space-y-1" data-category="keep">
                            <div class="flex justify-between items-center font-bold">
                                <span>3. Los Actos Humanos: Advertencia y Consentimiento</span>
                                <span class="px-2 py-0.5 rounded bg-emerald-200 text-emerald-900 text-[10px] font-extrabold uppercase">🟢 Mantener</span>
                            </div>
                            <p class="text-slate-700">Diferencia entre 'actos del hombre' (involuntarios) y 'actos humanos' (con advertencia de la razón y consentimiento de la voluntad).</p>
                        </div>

                        <div class="audit-item item-keep p-3 rounded text-xs space-y-1" data-category="keep">
                            <div class="flex justify-between items-center font-bold">
                                <span>4. La Ley Moral Natural y su Universalidad</span>
                                <span class="px-2 py-0.5 rounded bg-emerald-200 text-emerald-900 text-[10px] font-extrabold uppercase">🟢 Mantener</span>
                            </div>
                            <p class="text-slate-700">Universalidad e inmutabilidad de los primeros principios morales: "hacer el bien y evitar el mal", superando el relativismo moral en planta.</p>
                        </div>

                        <div class="audit-item item-update p-3 rounded text-xs space-y-1" data-category="update">
                            <div class="flex justify-between items-center font-bold">
                                <span>5. La Naturaleza Humana frente a la Despersonalización Industrial</span>
                                <span class="px-2 py-0.5 rounded bg-yellow-200 text-yellow-900 text-[10px] font-extrabold uppercase">🟡 Actualizar</span>
                            </div>
                            <p class="text-slate-700"><strong>Actualización:</strong> Reorientar de la metafísica teórica abstracta hacia el reconocimiento práctico del operario como fin y nunca como mero engranaje productivo.</p>
                        </div>

                        <div class="audit-item item-keep p-3 rounded text-xs space-y-1" data-category="keep">
                            <div class="flex justify-between items-center font-bold">
                                <span>6. El Trabajo como Vocación y Perfeccionamiento (Ideario Kinal)</span>
                                <span class="px-2 py-0.5 rounded bg-emerald-200 text-emerald-900 text-[10px] font-extrabold uppercase">🟢 Mantener</span>
                            </div>
                            <p class="text-slate-700">El trabajo como medio de realización personal, perfeccionamiento moral y santificación en las tareas ordinarias.</p>
                        </div>

                        <div class="audit-item item-keep p-3 rounded text-xs space-y-1" data-category="keep">
                            <div class="flex justify-between items-center font-bold">
                                <span>7. La Generosidad y el Espíritu de Servicio</span>
                                <span class="px-2 py-0.5 rounded bg-emerald-200 text-emerald-900 text-[10px] font-extrabold uppercase">🟢 Mantener</span>
                            </div>
                            <p class="text-slate-700">Entrega profesional más allá de la obligación contractual mínima: apoyar al compañero y servir con alegría.</p>
                        </div>

                        <div class="audit-item item-new p-3 rounded text-xs space-y-1" data-category="new">
                            <div class="flex justify-between items-center font-bold">
                                <span>8. El "Trabajo Bien Hecho": Pulcritud y Rigor en los Detalles</span>
                                <span class="px-2 py-0.5 rounded bg-blue-200 text-blue-900 text-[10px] font-extrabold uppercase">🔵 Agregar</span>
                            </div>
                            <p class="text-blue-950 font-medium">Principio institucional de Kinal: cuidado minucioso de herramientas, orden, puntualidad y rechazo a la chapuza o mediocridad técnica.</p>
                        </div>

                        <div class="audit-item item-new p-3 rounded text-xs space-y-1" data-category="new">
                            <div class="flex justify-between items-center font-bold">
                                <span>9. Inteligencia Emocional y Autodominio en la Cuadrilla</span>
                                <span class="px-2 py-0.5 rounded bg-blue-200 text-blue-900 text-[10px] font-extrabold uppercase">🔵 Agregar</span>
                            </div>
                            <p class="text-blue-950 font-medium">Gestión del estrés bajo presión de entregas; erradicación del autoritarismo, gritos y trato despectivo hacia operarios.</p>
                        </div>

                        <div class="audit-item item-new p-3 rounded text-xs space-y-1" data-category="new">
                            <div class="flex justify-between items-center font-bold">
                                <span>10. Comunicación Asertiva y Resolución Pacífica de Conflictos</span>
                                <span class="px-2 py-0.5 rounded bg-blue-200 text-blue-900 text-[10px] font-extrabold uppercase">🔵 Agregar</span>
                            </div>
                            <p class="text-blue-950 font-medium">Técnicas para corregir el error técnico en taller preservando intacta la dignidad de la persona humana.</p>
                        </div>

                        <div class="audit-item item-delete p-3 rounded text-xs space-y-1" data-category="delete">
                            <div class="flex justify-between items-center font-bold">
                                <span>11. Exámenes Teóricos Múltiples de Memorización (Parciales 1, 2 y Final)</span>
                                <span class="px-2 py-0.5 rounded bg-red-200 text-red-900 text-[10px] font-extrabold uppercase">🔴 Eliminar</span>
                            </div>
                            <p class="text-red-950 font-medium"><strong>Motivo:</strong> Dedicar 3 de 10 sesiones a pruebas escritas memorísticas reduce el tiempo formativo. Se reemplazan por talleres prácticos de deliberación moral.</p>
                        </div>

                    </div>
                </div>

                <!-- ==================== BIMESTRE 2 ==================== -->
                <div id="bimestre-2" class="bg-white rounded-xl border border-slate-300 shadow-sm overflow-hidden flex flex-col scroll-mt-36">
                    <div class="bg-slate-900 text-white p-4 border-b border-slate-800">
                        <div class="flex justify-between items-center text-xs text-amber-400 font-semibold mb-1">
                            <span>BIMESTRE 2 • Período 1 (50 min)</span>
                            <span>Código: B2-C1 • 13.5 Horas</span>
                        </div>
                        <h4 class="text-lg font-bold">B2: Ética General 2 — Libertad Responsable, Firmas y Compliance</h4>
                        <p class="text-xs text-slate-300 mt-1">
                            <strong>Correspondencia en Donis:</strong> II Trimestre (Temas 11 al 19).
                        </p>
                        <p class="text-xs text-slate-300 mt-0.5">
                            <strong>Logro esperado:</strong> Asumir la libertad personal responsable, comprender el alcance civil y penal de las firmas técnicas y aplicar protocolos de compliance industrial contra la corrupción.
                        </p>
                    </div>
                    <div class="p-5 divide-y divide-slate-100 flex-1 space-y-2">

                        <div class="audit-item item-keep p-3 rounded text-xs space-y-1" data-category="keep">
                            <div class="flex justify-between items-center font-bold">
                                <span>1. La Inteligencia y la Búsqueda de la Verdad Científica</span>
                                <span class="px-2 py-0.5 rounded bg-emerald-200 text-emerald-900 text-[10px] font-extrabold uppercase">🟢 Mantener</span>
                            </div>
                            <p class="text-slate-700">Función de la razón en la aprehensión de la realidad objetiva y honestidad ante los datos técnicos reales.</p>
                        </div>

                        <div class="audit-item item-update p-3 rounded text-xs space-y-1" data-category="update">
                            <div class="flex justify-between items-center font-bold">
                                <span>2. La Voluntad y la Libertad Responsable en Decisiones de Planta</span>
                                <span class="px-2 py-0.5 rounded bg-yellow-200 text-yellow-900 text-[10px] font-extrabold uppercase">🟡 Actualizar</span>
                            </div>
                            <p class="text-slate-700"><strong>Actualización:</strong> Vincular la libertad a la responsabilidad inexcusable: toda decisión de campo genera impacto en personas, equipos y costos.</p>
                        </div>

                        <div class="audit-item item-keep p-3 rounded text-xs space-y-1" data-category="keep">
                            <div class="flex justify-between items-center font-bold">
                                <span>3. El Fin Último: Felicidad, Integridad y Familia</span>
                                <span class="px-2 py-0.5 rounded bg-emerald-200 text-emerald-900 text-[10px] font-extrabold uppercase">🟢 Mantener</span>
                            </div>
                            <p class="text-slate-700">El sentido trascendente de la vida humana y la conciliación equilibrada entre jornada de trabajo y estabilidad familiar.</p>
                        </div>

                        <div class="audit-item item-keep p-3 rounded text-xs space-y-1" data-category="keep">
                            <div class="flex justify-between items-center font-bold">
                                <span>4. La Solidaridad y el Sentido del Bien Común</span>
                                <span class="px-2 py-0.5 rounded bg-emerald-200 text-emerald-900 text-[10px] font-extrabold uppercase">🟢 Mantener</span>
                            </div>
                            <p class="text-slate-700">Apoyo mutuo entre áreas operativas y compromiso cívico de la empresa con la comunidad circundante en Guatemala.</p>
                        </div>

                        <div class="audit-item item-update p-3 rounded text-xs space-y-1" data-category="update">
                            <div class="flex justify-between items-center font-bold">
                                <span>5. La Prudencia como Recto Juicio en la Operación Técnica</span>
                                <span class="px-2 py-0.5 rounded bg-yellow-200 text-yellow-900 text-[10px] font-extrabold uppercase">🟡 Actualizar</span>
                            </div>
                            <p class="text-slate-700"><strong>Actualización:</strong> Aplicar la prudencia al discernimiento operativo de mandos medios: sopesar riesgos antes de autorizar maniobras peligrosas.</p>
                        </div>

                        <div class="audit-item item-keep p-3 rounded text-xs space-y-1" data-category="keep">
                            <div class="flex justify-between items-center font-bold">
                                <span>6. Metodología Sistemática de Análisis de Dilemas Morales</span>
                                <span class="px-2 py-0.5 rounded bg-emerald-200 text-emerald-900 text-[10px] font-extrabold uppercase">🟢 Mantener</span>
                            </div>
                            <p class="text-slate-700">Pasos formales: clarificación de hechos, identificación de principios éticos en conflicto, alternativas y juicio de conciencia.</p>
                        </div>

                        <div class="audit-item item-new p-3 rounded text-xs space-y-1" data-category="new">
                            <div class="flex justify-between items-center font-bold">
                                <span>7. Alcance Legal y Penal de las Firmas Técnicas (Código Penal GT)</span>
                                <span class="px-2 py-0.5 rounded bg-blue-200 text-blue-900 text-[10px] font-extrabold uppercase">🔵 Agregar</span>
                            </div>
                            <p class="text-blue-950 font-medium">Responsabilidad civil y penal al firmar bitácoras de obra, peritajes mecánicos, planos eléctricos y memorias de cálculo. Imprudencia e impericia.</p>
                        </div>

                        <div class="audit-item item-new p-3 rounded text-xs space-y-1" data-category="new">
                            <div class="flex justify-between items-center font-bold">
                                <span>8. Veracidad Absoluta en Ensayos de Calidad y Reportes</span>
                                <span class="px-2 py-0.5 rounded bg-blue-200 text-blue-900 text-[10px] font-extrabold uppercase">🔵 Agregar</span>
                            </div>
                            <p class="text-blue-950 font-medium">Prohibición de maquillar lecturas de resistencia de concreto, frenos o aislamiento eléctrico; consecuencias catastróficas de la falsedad.</p>
                        </div>

                        <div class="audit-item item-new p-3 rounded text-xs space-y-1" data-category="new">
                            <div class="flex justify-between items-center font-bold">
                                <span>9. Compliance Industrial: Prevención de Sobornos y Dádivas</span>
                                <span class="px-2 py-0.5 rounded bg-blue-200 text-blue-900 text-[10px] font-extrabold uppercase">🔵 Agregar</span>
                            </div>
                            <p class="text-blue-950 font-medium">Conflicto de intereses en compras técnicas, rechazo a comisiones ilícitas (kickbacks) de proveedores y repuestos adulterados.</p>
                        </div>

                        <div class="audit-item item-new p-3 rounded text-xs space-y-1" data-category="new">
                            <div class="flex justify-between items-center font-bold">
                                <span>10. Canales de Denuncia Ética (Whistleblowing) y Seguridad Psicológica</span>
                                <span class="px-2 py-0.5 rounded bg-blue-200 text-blue-900 text-[10px] font-extrabold uppercase">🔵 Agregar</span>
                            </div>
                            <p class="text-blue-950 font-medium">Protocolos para alertar prácticas ilícitas o riesgos inminentes sin temor a represalias laborales.</p>
                        </div>

                    </div>
                </div>

                <!-- ==================== BIMESTRE 3 ==================== -->
                <div id="bimestre-3" class="bg-white rounded-xl border border-slate-300 shadow-sm overflow-hidden flex flex-col scroll-mt-36">
                    <div class="bg-slate-900 text-white p-4 border-b border-slate-800">
                        <div class="flex justify-between items-center text-xs text-amber-400 font-semibold mb-1">
                            <span>BIMESTRE 3 • Período 1 (50 min)</span>
                            <span>Código: B3-C1 • 13.5 Horas</span>
                        </div>
                        <h4 class="text-lg font-bold">B3: Ética Profesional 1 — Deontología, Automatización e IA</h4>
                        <p class="text-xs text-slate-300 mt-1">
                            <strong>Correspondencia en Donis:</strong> III Trimestre (Temas 20 al 28).
                        </p>
                        <p class="text-xs text-slate-300 mt-0.5">
                            <strong>Logro esperado:</strong> Dominar la deontología técnica, liderar con justicia la transición ante la automatización (reskilling vs. despido) y gobernar la IA preservando secretos industriales.
                        </p>
                    </div>
                    <div class="p-5 divide-y divide-slate-100 flex-1 space-y-2">

                        <div class="audit-item item-keep p-3 rounded text-xs space-y-1" data-category="keep">
                            <div class="flex justify-between items-center font-bold">
                                <span>1. Código Deontológico de Ingeniería y Asociaciones Técnicas</span>
                                <span class="px-2 py-0.5 rounded bg-emerald-200 text-emerald-900 text-[10px] font-extrabold uppercase">🟢 Mantener</span>
                            </div>
                            <p class="text-slate-700">Deberes fiduciarios, honestidad intelectual, lealtad contractual con el empleador y primacía de la seguridad pública.</p>
                        </div>

                        <div class="audit-item item-delete p-3 rounded text-xs space-y-1" data-category="delete">
                            <div class="flex justify-between items-center font-bold">
                                <span>2. Código Deontológico Periodístico</span>
                                <span class="px-2 py-0.5 rounded bg-red-200 text-red-900 text-[10px] font-extrabold uppercase">🔴 Eliminar</span>
                            </div>
                            <p class="text-red-950 font-medium"><strong>Motivo:</strong> Contenido ajeno a los perfiles de egreso técnicos e industriales del TSU Kinal.</p>
                        </div>

                        <div class="audit-item item-delete p-3 rounded text-xs space-y-1" data-category="delete">
                            <div class="flex justify-between items-center font-bold">
                                <span>3. Código Deontológico Jurídico</span>
                                <span class="px-2 py-0.5 rounded bg-red-200 text-red-900 text-[10px] font-extrabold uppercase">🔴 Eliminar</span>
                            </div>
                            <p class="text-red-950 font-medium"><strong>Motivo:</strong> Enfocado en litigios forenses de abogados; se sustituye por deontología de supervisión industrial.</p>
                        </div>

                        <div class="audit-item item-delete p-3 rounded text-xs space-y-1" data-category="delete">
                            <div class="flex justify-between items-center font-bold">
                                <span>4. Código Deontológico Médico</span>
                                <span class="px-2 py-0.5 rounded bg-red-200 text-red-900 text-[10px] font-extrabold uppercase">🔴 Eliminar</span>
                            </div>
                            <p class="text-red-950 font-medium"><strong>Motivo:</strong> Relación médico-paciente clínica; se reemplaza por ética de la seguridad industrial y prevención de riesgos.</p>
                        </div>

                        <div class="audit-item item-update p-3 rounded text-xs space-y-1" data-category="update">
                            <div class="flex justify-between items-center font-bold">
                                <span>5. Análisis de Casos Complejos de Fallas Catastróficas en Ingeniería</span>
                                <span class="px-2 py-0.5 rounded bg-yellow-200 text-yellow-900 text-[10px] font-extrabold uppercase">🟡 Actualizar</span>
                            </div>
                            <p class="text-slate-700"><strong>Actualización:</strong> Casos reales de negligencia: colapso del Puente Cambray, fallas de calderas y software defectuoso.</p>
                        </div>

                        <div class="audit-item item-new p-3 rounded text-xs space-y-1" data-category="new">
                            <div class="flex justify-between items-center font-bold">
                                <span>6. Automatización y el Principio de la Transición Justa</span>
                                <span class="px-2 py-0.5 rounded bg-blue-200 text-blue-900 text-[10px] font-extrabold uppercase">🔵 Agregar</span>
                            </div>
                            <p class="text-blue-950 font-medium">La primacía del trabajo humano sobre el capital. Evaluación del impacto laboral antes de introducir robótica o automatización.</p>
                        </div>

                        <div class="audit-item item-new p-3 rounded text-xs space-y-1" data-category="new">
                            <div class="flex justify-between items-center font-bold">
                                <span>7. Reskilling y Upskilling como Deber Moral del Supervisor</span>
                                <span class="px-2 py-0.5 rounded bg-blue-200 text-blue-900 text-[10px] font-extrabold uppercase">🔵 Agregar</span>
                            </div>
                            <p class="text-blue-950 font-medium">Reentrenar y capacitar a los operarios en nuevas herramientas tecnológicas antes de optar por despidos masivos.</p>
                        </div>

                        <div class="audit-item item-new p-3 rounded text-xs space-y-1" data-category="new">
                            <div class="flex justify-between items-center font-bold">
                                <span>8. Límites Éticos del Monitoreo Digital y Cámaras en Planta</span>
                                <span class="px-2 py-0.5 rounded bg-blue-200 text-blue-900 text-[10px] font-extrabold uppercase">🔵 Agregar</span>
                            </div>
                            <p class="text-blue-950 font-medium">Respeto a la intimidad, prohibición de vigilancia invasiva desmedida y derecho a la desconexión laboral del trabajador.</p>
                        </div>

                        <div class="audit-item item-new p-3 rounded text-xs space-y-1" data-category="new">
                            <div class="flex justify-between items-center font-bold">
                                <span>9. Protección de Secretos Industriales y Fuga de Datos con IA</span>
                                <span class="px-2 py-0.5 rounded bg-blue-200 text-blue-900 text-[10px] font-extrabold uppercase">🔵 Agregar</span>
                            </div>
                            <p class="text-blue-950 font-medium">Riesgo legal y ético de subir planos, códigos o fórmulas patentadas a modelos públicos de IA (ChatGPT, Claude).</p>
                        </div>

                    </div>
                </div>

                <!-- ==================== BIMESTRE 4 ==================== -->
                <div id="bimestre-4" class="bg-white rounded-xl border border-slate-300 shadow-sm overflow-hidden flex flex-col scroll-mt-36">
                    <div class="bg-slate-900 text-white p-4 border-b border-slate-800">
                        <div class="flex justify-between items-center text-xs text-amber-400 font-semibold mb-1">
                            <span>BIMESTRE 4 • Período 1 (50 min)</span>
                            <span>Código: B4-C1 • 13.5 Horas</span>
                        </div>
                        <h4 class="text-lg font-bold">B4: Ética Profesional 2 — Bioética, HITL y Custodia Ambiental</h4>
                        <p class="text-xs text-slate-300 mt-1">
                            <strong>Correspondencia en Donis:</strong> IV Trimestre (Temas 29 al 38).
                        </p>
                        <p class="text-xs text-slate-300 mt-0.5">
                            <strong>Logro esperado:</strong> Aplicar los principios de la bioética integral, consagrar el principio Human-in-the-Loop ante sistemas autónomos y custodiar el medio ambiente con economía circular.
                        </p>
                    </div>
                    <div class="p-5 divide-y divide-slate-100 flex-1 space-y-2">

                        <div class="audit-item item-keep p-3 rounded text-xs space-y-1" data-category="keep">
                            <div class="flex justify-between items-center font-bold">
                                <span>1. Fundamentos Históricos de la Bioética (Potter y Núremberg)</span>
                                <span class="px-2 py-0.5 rounded bg-emerald-200 text-emerald-900 text-[10px] font-extrabold uppercase">🟢 Mantener</span>
                            </div>
                            <p class="text-slate-700">El nacimiento de la bioética como puente entre la ciencia experimental y las humanidades para proteger la vida.</p>
                        </div>

                        <div class="audit-item item-keep p-3 rounded text-xs space-y-1" data-category="keep">
                            <div class="flex justify-between items-center font-bold">
                                <span>2. Los 4 Principios de la Bioética: Beneficencia, No Maleficencia, Autonomía y Justicia</span>
                                <span class="px-2 py-0.5 rounded bg-emerald-200 text-emerald-900 text-[10px] font-extrabold uppercase">🟢 Mantener</span>
                            </div>
                            <p class="text-slate-700">Marco bioético de Georgetown aplicable a la experimentación científica y el impacto de la tecnología en la salud humana.</p>
                        </div>

                        <div class="audit-item item-keep p-3 rounded text-xs space-y-1" data-category="keep">
                            <div class="flex justify-between items-center font-bold">
                                <span>3. La Dignidad Inviolable de la Vida Humana desde su Inicio</span>
                                <span class="px-2 py-0.5 rounded bg-emerald-200 text-emerald-900 text-[10px] font-extrabold uppercase">🟢 Mantener</span>
                            </div>
                            <p class="text-slate-700">Defensa incondicional del derecho a la vida en todas sus etapas conforme a la antropología cristiana de Fundación Kinal.</p>
                        </div>

                        <div class="audit-item item-update p-3 rounded text-xs space-y-1" data-category="update">
                            <div class="flex justify-between items-center font-bold">
                                <span>4. Cuidados Paliativos vs. Eutanasia y Encarnizamiento Terapéutico</span>
                                <span class="px-2 py-0.5 rounded bg-yellow-200 text-yellow-900 text-[10px] font-extrabold uppercase">🟡 Actualizar</span>
                            </div>
                            <p class="text-slate-700"><strong>Actualización:</strong> Acompañamiento humano, alivio integral del sufrimiento y respeto a la muerte natural sin acelerar ni prolongar artificialmente la agonía.</p>
                        </div>

                        <div class="audit-item item-delete p-3 rounded text-xs space-y-1" data-category="delete">
                            <div class="flex justify-between items-center font-bold">
                                <span>5. Casuística Médica Ginecológica Hiper-Especializada</span>
                                <span class="px-2 py-0.5 rounded bg-red-200 text-red-900 text-[10px] font-extrabold uppercase">🔴 Eliminar</span>
                            </div>
                            <p class="text-red-950 font-medium"><strong>Motivo:</strong> Se aligera el temario clínico hospitalario (protocolos de reproducción asistida) para abrir espacio a la bioética tecnológica y ambiental.</p>
                        </div>

                        <div class="audit-item item-new p-3 rounded text-xs space-y-1" data-category="new">
                            <div class="flex justify-between items-center font-bold">
                                <span>6. El Principio Human-in-the-Loop (HITL) en Operaciones Críticas</span>
                                <span class="px-2 py-0.5 rounded bg-blue-200 text-blue-900 text-[10px] font-extrabold uppercase">🔵 Agregar</span>
                            </div>
                            <p class="text-blue-950 font-medium">Supervisión humana obligatoria e indelegable: un algoritmo o robot nunca puede asumir la responsabilidad moral o penal por vidas.</p>
                        </div>

                        <div class="audit-item item-new p-3 rounded text-xs space-y-1" data-category="new">
                            <div class="flex justify-between items-center font-bold">
                                <span>7. Superación del Sesgo de Automatización (Automation Bias)</span>
                                <span class="px-2 py-0.5 rounded bg-blue-200 text-blue-900 text-[10px] font-extrabold uppercase">🔵 Agregar</span>
                            </div>
                            <p class="text-blue-950 font-medium">Juicio crítico técnico: contrastar las sugerencias de la IA con la inspección física en campo y las leyes de la física real.</p>
                        </div>

                        <div class="audit-item item-new p-3 rounded text-xs space-y-1" data-category="new">
                            <div class="flex justify-between items-center font-bold">
                                <span>8. Honestidad Académica y Profesional Kinal frente al "Copy-Paste"</span>
                                <span class="px-2 py-0.5 rounded bg-blue-200 text-blue-900 text-[10px] font-extrabold uppercase">🔵 Agregar</span>
                            </div>
                            <p class="text-blue-950 font-medium">Rechazo al facilismo del plagio digital; propiedad moral del esfuerzo y comprobación personal de cada cálculo.</p>
                        </div>

                        <div class="audit-item item-new p-3 rounded text-xs space-y-1" data-category="new">
                            <div class="flex justify-between items-center font-bold">
                                <span>9. Bioética Ambiental, Economía Circular y Residuos Peligrosos</span>
                                <span class="px-2 py-0.5 rounded bg-blue-200 text-blue-900 text-[10px] font-extrabold uppercase">🔵 Agregar</span>
                            </div>
                            <p class="text-blue-950 font-medium">Custodia de la creación: manejo certificado de aceites usados, refrigerantes, baterías de litio y chatarra RAEE bajo normas MARN.</p>
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
                <span class="text-xs uppercase tracking-wider text-blue-600 font-extrabold">Estructura Didáctica Oficial 2026</span>
                <h3 class="text-2xl font-black text-slate-900 mt-1 flex items-center gap-2">
                    <i data-lucide="calendar-check" class="w-6 h-6 text-emerald-600"></i>
                    Nuevo Temario Dosificado: 40 Sesiones Anuales de Formación Humana y Ética
                </h3>
                <p class="text-xs text-slate-500 mt-1">
                    Dosificación continua de 10 sesiones por bimestre (Período 1 de 50 minutos) totalmente articuladas con el Pensum del TSU.
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
                            <th class="p-3 font-bold w-60">Enfoque Metodológico / Entregable</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-200 text-slate-700">

                        <!-- BIMESTRE 1 -->
                        <tr class="hover:bg-slate-50">
                            <td class="p-3 font-bold text-center text-blue-900 bg-blue-50/50" rowspan="10">B1</td>
                            <td class="p-3 font-semibold text-center bg-slate-50">1</td>
                            <td class="p-3 font-bold text-blue-900" rowspan="10">
                                B1-C1 • Ética General 1
                                <div class="text-[10px] text-slate-500 font-normal">Antropología y Sentido Trascendente del Trabajo (13.5h)</div>
                            </td>
                            <td class="p-3"><strong>Fundamentos de la Ética y Antropología Filosófica:</strong> La persona en el centro de la operación técnica frente a la despersonalización.</td>
                            <td class="p-3"><span class="px-2 py-0.5 rounded bg-slate-100 text-slate-800 font-semibold">Debate: Técnica vs. Humanismo</span></td>
                        </tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">2</td><td class="p-3"><strong>El Bien Moral:</strong> El bien como fin natural y objeto de la voluntad; bien honesto, útil y deleitable.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-slate-100 text-slate-800 font-semibold">Plenaria dirigida</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">3</td><td class="p-3"><strong>Los Actos Humanos:</strong> Advertencia del entendimiento y consentimiento de la voluntad; responsabilidad moral.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-emerald-100 text-emerald-800 font-semibold">Análisis de casos de advertencia</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">4</td><td class="p-3"><strong>La Ley Moral Natural:</strong> Principios universales inmutables, la voz de la conciencia recta y superación del relativismo.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-slate-100 text-slate-800 font-semibold">Guía de discernimiento moral</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">5</td><td class="p-3"><strong>El Ideario de Kinal:</strong> El trabajo como vocación humana, medio de perfeccionamiento y santificación ordinaria.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-amber-100 text-amber-900 font-semibold">Reflexión Ideario Kinal</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">6</td><td class="p-3"><strong>El "Trabajo Bien Hecho":</strong> Pulcritud en los detalles, custodia de herramientas, puntualidad y superación de la mediocridad.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-amber-100 text-amber-900 font-semibold">Matriz de Excelencia en Taller</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">7</td><td class="p-3"><strong>La Generosidad y Espíritu de Servicio:</strong> Transformar la jornada en aporte social más allá del mínimo exigido.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-slate-100 text-slate-800 font-semibold">Foro de vivencias de servicio</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">8</td><td class="p-3"><strong>Autodominio y Templanza en el Mando Medio:</strong> Erradicación del autoritarismo, gritos y maltrato en cuadrillas.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-blue-100 text-blue-800 font-semibold">Protocolo de Autodominio</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">9</td><td class="p-3"><strong>Comunicación Asertiva y Empatía Operativa:</strong> Cómo corregir el error técnico preservando intacta la dignidad humana.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-blue-100 text-blue-800 font-semibold">Role-playing de Corrección</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">10</td><td class="p-3"><strong>Taller Integrador B1:</strong> Deliberación de casos reales de convivencia y trato humano en cuadrillas de Kinal.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-purple-100 text-purple-900 font-bold">Dictamen Ético Integrador B1</span></td></tr>

                        <!-- BIMESTRE 2 -->
                        <tr class="hover:bg-slate-50">
                            <td class="p-3 font-bold text-center text-emerald-900 bg-emerald-50/50" rowspan="10">B2</td>
                            <td class="p-3 font-semibold text-center bg-slate-50">11</td>
                            <td class="p-3 font-bold text-blue-900" rowspan="10">
                                B2-C1 • Ética General 2
                                <div class="text-[10px] text-slate-500 font-normal">Libertad Responsable, Compliance e Integridad Industrial (13.5h)</div>
                            </td>
                            <td class="p-3"><strong>La Inteligencia y la Verdad:</strong> El deber ineludible del rigor técnico y científico; honestidad con la realidad.</td>
                            <td class="p-3"><span class="px-2 py-0.5 rounded bg-slate-100 text-slate-800 font-semibold">Ensayo breve de rigor técnico</span></td>
                        </tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">12</td><td class="p-3"><strong>La Voluntad y la Libertad Responsable:</strong> Toda decisión u omisión técnica genera consecuencias directas.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-slate-100 text-slate-800 font-semibold">Árbol de Consecuencias de Campo</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">13</td><td class="p-3"><strong>El Fin Último y Balance de Vida:</strong> La felicidad como realización integral; balance ético trabajo-familia.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-slate-100 text-slate-800 font-semibold">Plan Personal de Equilibrio</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">14</td><td class="p-3"><strong>La Solidaridad y el Bien Común:</strong> Cooperación interfuncional entre departamentos y compromiso social en Guatemala.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-slate-100 text-slate-800 font-semibold">Propuesta de Bien Común Local</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">15</td><td class="p-3"><strong>La Prudencia en la Operación:</strong> Recto juicio para sopesar riesgos ante presiones económicas o prisas del cliente.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-amber-100 text-amber-900 font-semibold">Matriz de Decisión Prudencial</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">16</td><td class="p-3"><strong>Alcance Legal de las Firmas Técnicas:</strong> Responsabilidad civil y penal en bitácoras de obra, planos y memorias de cálculo.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-red-100 text-red-900 font-bold">Análisis del Código Penal GT</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">17</td><td class="p-3"><strong>Veracidad en Informes Técnicos:</strong> Prohibición de adulterar ensayos de resistencia, frenos o aislamiento; trazabilidad.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-emerald-100 text-emerald-800 font-semibold">Auditoría de Bitácoras Foliadas</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">18</td><td class="p-3"><strong>Compliance Industrial:</strong> Prevención de sobornos, dádivas, comisiones ilícitas (kickbacks) y repuestos fraudulentos.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-blue-100 text-blue-800 font-semibold">Manual de Política Anti-Soborno</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">19</td><td class="p-3"><strong>Whistleblowing y Seguridad Psicológica:</strong> Canales éticos de denuncia interna ante prácticas ilícitas sin represalias.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-blue-100 text-blue-800 font-semibold">Protocolo de Alerta Temprana</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">20</td><td class="p-3"><strong>Taller Integrador B2:</strong> Simulación de juicio ético por firma de orden de trabajo defectuosa bajo presión jerárquica.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-purple-100 text-purple-900 font-bold">Caso Práctico: Dilema de la Firma</span></td></tr>

                        <!-- BIMESTRE 3 -->
                        <tr class="hover:bg-slate-50">
                            <td class="p-3 font-bold text-center text-amber-900 bg-amber-50/50" rowspan="10">B3</td>
                            <td class="p-3 font-semibold text-center bg-slate-50">21</td>
                            <td class="p-3 font-bold text-blue-900" rowspan="10">
                                B3-C1 • Ética Profesional 1
                                <div class="text-[10px] text-slate-500 font-normal">Automatización, Inteligencia Artificial y la Transición Justa (13.5h)</div>
                            </td>
                            <td class="p-3"><strong>Deontología Técnica Aplicada:</strong> Código ético de ingeniería; deberes fiduciarios y seguridad colectiva.</td>
                            <td class="p-3"><span class="px-2 py-0.5 rounded bg-slate-100 text-slate-800 font-semibold">Estudio de Código Deontológico</span></td>
                        </tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">22</td><td class="p-3"><strong>Secreto Profesional y Confidencialidad:</strong> Custodia de información técnica del cliente y lealtad laboral.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-slate-100 text-slate-800 font-semibold">Acuerdo de Confidencialidad (NDA)</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">23</td><td class="p-3"><strong>Metodología de Resolución de Dilemas Éticos Complejos:</strong> Árbol de decisiones fiduciarias y juicio de prudencia.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-emerald-100 text-emerald-800 font-semibold">Plantilla de Deliberación</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">24</td><td class="p-3"><strong>La Industria 4.0 y la Transición Justa:</strong> Impacto de robótica e IA en el empleo formal guatemalteco.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-blue-100 text-blue-800 font-semibold">Matriz de Impacto Social</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">25</td><td class="p-3"><strong>Primacía del Trabajo sobre el Capital:</strong> La persona como sujeto del desarrollo; tecnología al servicio del hombre.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-amber-100 text-amber-900 font-semibold">Doctrina Social: Laborem Exercens</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">26</td><td class="p-3"><strong>Reskilling y Upskilling Obligatorio:</strong> El supervisor como educador técnico; reentrenar antes de despedir.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-blue-100 text-blue-800 font-semibold">Plan de Reentrenamiento Técnico</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">27</td><td class="p-3"><strong>Sesgos Algorítmicos en Operaciones:</strong> Discriminación en sistemas automáticos de asignación de turnos y méritos.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-blue-100 text-blue-800 font-semibold">Auditoría Ética de Algoritmos</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">28</td><td class="p-3"><strong>Límites del Monitoreo Digital en Planta:</strong> Cámaras inteligentes, biometría y derecho a la desconexión.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-blue-100 text-blue-800 font-semibold">Política de Privacidad de Planta</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">29</td><td class="p-3"><strong>Secretos Industriales y Fuga de Datos con IA:</strong> Riesgos de exponer planos o recetas patentadas a modelos públicos.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-red-100 text-red-900 font-bold">Guía de Uso Seguro de LLMs</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">30</td><td class="p-3"><strong>Taller Integrador B3:</strong> Diseño de un plan ético de modernización y automatización de una línea de producción.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-purple-100 text-purple-900 font-bold">Proyecto Transición Justa Kinal</span></td></tr>

                        <!-- BIMESTRE 4 -->
                        <tr class="hover:bg-slate-50">
                            <td class="p-3 font-bold text-center text-purple-900 bg-purple-50/50" rowspan="10">B4</td>
                            <td class="p-3 font-semibold text-center bg-slate-50">31</td>
                            <td class="p-3 font-bold text-blue-900" rowspan="10">
                                B4-C1 • Ética Profesional 2
                                <div class="text-[10px] text-slate-500 font-normal">Principio Human-in-the-Loop, Juicio Crítico y el Trabajo Bien Hecho (13.5h)</div>
                            </td>
                            <td class="p-3"><strong>Fundamentos de la Bioética:</strong> Nacimiento histórico (Potter, Núremberg); la técnica al servicio de la vida.</td>
                            <td class="p-3"><span class="px-2 py-0.5 rounded bg-slate-100 text-slate-800 font-semibold">Línea de Tiempo Bioética</span></td>
                        </tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">32</td><td class="p-3"><strong>Los 4 Principios Bioéticos Universales:</strong> Beneficencia, No Maleficencia, Autonomía y Justicia distributiva.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-slate-100 text-slate-800 font-semibold">Matriz de Principios Bioéticos</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">33</td><td class="p-3"><strong>Dignidad Inviolable de la Vida Humana:</strong> Defensa de la vida desde la concepción; rechazo al utilitarismo.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-emerald-100 text-emerald-800 font-semibold">Debate: La Vida como Valor Supremo</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">34</td><td class="p-3"><strong>Ética ante el Sufrimiento Humano:</strong> Cuidados paliativos vs. eutanasia; dignidad en la etapa final de la existencia.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-slate-100 text-slate-800 font-semibold">Análisis de Caso: Acompañamiento</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">35</td><td class="p-3"><strong>El Principio Human-in-the-Loop (HITL):</strong> Supervisión humana obligatoria en sistemas autónomos y robots.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-blue-100 text-blue-800 font-semibold">Protocolo HITL de Planta</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">36</td><td class="p-3"><strong>Superación del Sesgo de Automatización:</strong> Juicio crítico; contrastar la IA con la inspección física y el sentido común.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-blue-100 text-blue-800 font-semibold">Taller Anti-Automation Bias</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">37</td><td class="p-3"><strong>Honestidad Académica y Profesional Kinal:</strong> Rechazo al fraude del 'copiar y pegar' de IA generativa en memorias.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-amber-100 text-amber-900 font-semibold">Declaración de Autoría Moral</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">38</td><td class="p-3"><strong>Bioética Ambiental y Custodia de la Creación:</strong> Impacto ecológico de talleres, obras y subestaciones.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-emerald-100 text-emerald-800 font-semibold">Auditoría Ambiental de Taller</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">39</td><td class="p-3"><strong>Economía Circular y Residuos Peligrosos:</strong> Manejo certificado de aceites usados, refrigerantes, baterías y RAEE (MARN).</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-emerald-100 text-emerald-800 font-semibold">Plan de Gestión de Residuos MARN</span></td></tr>
                        <tr class="hover:bg-slate-50"><td class="p-3 font-semibold text-center bg-slate-50">40</td><td class="p-3"><strong>Clausura Anual y Compromiso Deontológico:</strong> Juramento ético del egresado TSU Kinal y decálogo de integridad profesional.</td><td class="p-3"><span class="px-2 py-0.5 rounded bg-purple-100 text-purple-900 font-bold">Juramento Deontológico TSU Kinal</span></td></tr>

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
                El plan original del <strong>Prof. Vinicio Donis</strong> posee una sólida arquitectura antropológica clásica, plenamente compatible con el <strong>Ideario de Kinal</strong>. La presente modernización no desvirtúa sus fundamentos morales, sino que:
            </p>
            <div class="grid md:grid-cols-3 gap-4 pt-2 text-xs text-slate-300">
                <div class="p-4 rounded-xl bg-slate-800/80 border border-slate-700 space-y-1">
                    <strong class="text-white block font-semibold">1. Elimina Desviaciones Vocacionales</strong>
                    <p class="text-slate-400">Suprime códigos deontológicos de periodismo, abogacía y medicina clínica que no corresponden a técnicos universitarios.</p>
                </div>
                <div class="p-4 rounded-xl bg-slate-800/80 border border-slate-700 space-y-1">
                    <strong class="text-white block font-semibold">2. Incorpora Compliance y Firmas</strong>
                    <p class="text-slate-400">Dota al alumno de conocimientos sobre responsabilidad civil y penal en bitácoras, y prevención de sobornos y conflicto de intereses.</p>
                </div>
                <div class="p-4 rounded-xl bg-slate-800/80 border border-slate-700 space-y-1">
                    <strong class="text-white block font-semibold">3. Integra Ética 4.0 y Medio Ambiente</strong>
                    <p class="text-slate-400">Introduce la transición justa ante la automatización, gobernanza de IA (Human-in-the-Loop) y manejo de residuos peligrosos (MARN).</p>
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
                    btn.classList.remove('ring-2', 'ring-offset-2', 'ring-blue-600', 'font-black');
                }
            });

            const activeBtn = document.getElementById('btn-filter-' + category);
            if (activeBtn) {
                activeBtn.classList.add('ring-2', 'ring-offset-2', 'ring-blue-600', 'font-black');
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
    with open("TSU/etica_auditoria.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("TSU/etica_auditoria.html generado con éxito.")

def generate_etica_markdown():
    md_content = """# Auditoría Curricular y Propuesta de Temario Dosificado: Formación Humana y Ética Profesional (TSU 2026)

**Institución:** Fundación Kinal  
**Programa:** Técnico Superior Universitario (TSU) — Año Académico Común (3er Año UNIS)  
**Línea de Estudio:** Formación Humana, Ética Profesional y Gobernanza IA  
**Docente Base Analizado:** Prof. Vinicio Donis  
**Carga Horaria Anual:** 4 Bimestres • 40 Sesiones (50 min) • 54 Horas Presenciales  
**Umbral Aprobatorio:** $\\ge 75/100$ puntos  

---

## 1. Resumen Ejecutivo del Diagnóstico Curricular

El programa original de **Ética Profesional** impartido por el **Prof. Vinicio Donis** (estructurado en 4 trimestres lectivos) cuenta con una sólida raíz antropológica y filosófica clásica (tomista), plenamente convergente con el **Ideario de Fundación Kinal** (*"Visión cristiana de la vida. Respeto a la dignidad de la persona. Espíritu de servicio. Trabajo bien hecho. Libertad personal responsable"*).

Sin embargo, tras la auditoría técnica exhaustiva orientada al perfil de egreso del **Mando Medio en la Industria 4.0** en las 7 especialidades técnicas de Kinal, se identificaron tres áreas de mejora crítica:
1. **Desviaciones Vocacionales:** El bloque III dedicaba sesiones enteras a códigos deontológicos ajenos al ámbito técnico (periodístico, jurídico de abogados y médico clínico hospitalario).
2. **Vacíos Normativos y Legales:** Ausencia de contenidos sobre la **responsabilidad civil y penal de las firmas técnicas** (bitácoras de obra, peritajes, memorias de cálculo), **compliance industrial**, prevención de sobornos en compras de repuestos y canales de denuncia (*whistleblowing*).
3. **Desafíos Tecnológicos Contemporáneos:** Ausencia de lineamientos ante la **automatización y transición justa** (reskilling vs. despido masivo), **gobernanza de la Inteligencia Artificial (Principio Human-in-the-Loop)**, privacidad de secretos industriales y **bioética ambiental** (residuos peligrosos, baterías de litio y normativas MARN).

---

## 2. Métricas Cuatricolores de la Auditoría

Se evaluaron **52 elementos curriculares** a lo largo de los 4 bimestres lectivos:

* 🟢 **20 Temas a Mantener (38.5%):** Los fundamentos inmutables de la ética filosófica: el bien moral, actos humanos (advertencia y consentimiento), ley moral natural, el trabajo como vocación y perfeccionamiento personal (Ideario Kinal), generosidad, virtudes de prudencia y solidaridad, deontología de ingeniería y defensa irrestricta de la dignidad de la vida humana.
* 🟡 **12 Temas a Actualizar (23.1%):** Transición de la metafísica teórica abstracta hacia la acción de planta: toma de decisiones de campo, prudencia aplicada a evaluar riesgos operacionales bajo presión de tiempos, deliberación moral ante fallas técnicas reales, y bioética ante el sufrimiento humano centrada en el alivio integral (cuidados paliativos).
* 🔵 **14 Temas Nuevos a Agregar (26.9%):** Competencias indispensables para el supervisor técnico moderno:
  * El "Trabajo Bien Hecho" de Kinal contra la mediocridad y el plagio de IA.
  * Inteligencia emocional, autodominio y erradicación del maltrato en cuadrillas.
  * Alcance legal y penal de las firmas técnicas (Código Penal de Guatemala).
  * Veracidad absoluta en bitácoras foliadas y ensayos de laboratorio/calidad.
  * Compliance industrial: prevención de sobornos y comisiones ilícitas (*kickbacks*).
  * Canales éticos de denuncia interna (*whistleblowing*) y seguridad psicológica.
  * Automatización industrial y el principio de la Transición Justa (primacía del trabajo sobre el capital).
  * Reskilling y Upskilling técnico como deber moral del supervisor antes de despedir.
  * Protección de secretos industriales y propiedad intelectual al usar IA corporativa.
  * Principio *Human-in-the-Loop* (HITL): supervisión humana indelegable sobre sistemas autónomos y robots.
  * Superación del sesgo de automatización (*automation bias*) y fomento del juicio crítico.
  * Bioética ambiental, economía circular y disposición certificada de residuos peligrosos (aceites, baterías, RAEE bajo normas MARN).
* 🔴 **6 Temas a Eliminar (11.5%):**
  * Código Deontológico Periodístico (ajeno a especialidades técnicas).
  * Código Deontológico Jurídico (enfocado en litigios de derecho).
  * Código Deontológico Médico clínico (ajeno al ámbito de planta/obra).
  * Casuística ginecológica hiper-especializada hospitalaria (reproducción asistida).
  * Tres baterías de exámenes teóricos memorísticos que consumían 30% del tiempo de clase (reemplazados por talleres prácticos de deliberación ética).

---

## 3. Matriz de Correspondencia 1 a 1: Módulos Auditados vs. Pensum TSU

| Bimestre | Módulo en Plan Donis | Asignatura en Pensum TSU (Línea Ética) | Código | Horas / Carga | Logro Curricular Clave |
| :---: | :--- | :--- | :---: | :---: | :--- |
| **B1** | I Trimestre: Fundamentos, Actos Humanos y Trabajo | **Ética General 1: Antropología y Sentido del Trabajo** | `B1-C1` | P1 • 13.5h | Dignidad humana, actos humanos, trabajo bien hecho e inteligencia emocional en cuadrillas. |
| **B2** | II Trimestre: Inteligencia, Voluntad, Prudencia y Casos | **Ética General 2: Libertad, Firmas y Compliance** | `B2-C1` | P1 • 13.5h | Libertad responsable, responsabilidad civil/penal de firmas técnicas y compliance anti-soborno. |
| **B3** | III Trimestre: Análisis de Casos y Códigos Deontológicos | **Ética Profesional 1: Deontología e Industria 4.0** | `B3-C1` | P1 • 13.5h | Deontología técnica, automatización y transición justa (reskilling vs. despido) y secretos en IA. |
| **B4** | IV Trimestre: Bioética y Respeto a la Vida | **Ética Profesional 2: Bioética, HITL y Medio Ambiente** | `B4-C1` | P1 • 13.5h | Principios bioéticos, principio Human-in-the-Loop, juicio crítico y custodia ambiental MARN. |

---

## 4. Nuevo Temario Dosificado: 40 Sesiones Anuales (10 por Bimestre)

### BIMESTRE 1: Ética General 1 — Antropología y Sentido Trascendente del Trabajo (B1-C1)
* **Sesión 1:** Fundamentos de la Ética y Antropología Filosófica: La Persona en el Centro de la Empresa Técnica.
* **Sesión 2:** El Bien Moral: El Bien como Fin Natural y Objeto de la Voluntad (Bien Honesto vs. Útil).
* **Sesión 3:** Los Actos Humanos: Discernimiento, Advertencia y Consentimiento en el Ámbito Laboral.
* **Sesión 4:** La Ley Moral Natural: Principios Universales Inmutables frente al Relativismo Moral.
* **Sesión 5:** El Ideario de Kinal: El Trabajo como Vocación Humana, Perfeccionamiento y Escuela de Virtudes.
* **Sesión 6:** El "Trabajo Bien Hecho": Pulcritud en los Detalles, Custodia de Herramientas y Excelencia Diaria.
* **Sesión 7:** La Generosidad y el Espíritu de Servicio: Trascender el Cumplimiento Mínimo Contractual.
* **Sesión 8:** Inteligencia Emocional y Autodominio del Mando Medio: Erradicación del Maltrato en Taller y Obra.
* **Sesión 9:** Comunicación Asertiva, Diálogo Empático y Resolución Pacífica de Conflictos Operativos.
* **Sesión 10:** Taller Integrador B1: Deliberación de Casos Reales de Convivencia y Trato Humano en Cuadrillas Técnicas.

### BIMESTRE 2: Ética General 2 — Libertad Responsable, Firmas y Compliance (B2-C1)
* **Sesión 11:** La Inteligencia Orientada a la Verdad: El Deber del Rigor Técnico y Científico en la Empresa.
* **Sesión 12:** La Voluntad y la Libertad Responsable: Toda Decisión Técnica Genera Consecuencias Directas.
* **Sesión 13:** El Fin Último del Hombre: Felicidad, Integridad y Conciliación Trabajo-Familia.
* **Sesión 14:** La Solidaridad y el Bien Común: Cooperación Interdepartamental y Responsabilidad Comunitaria.
* **Sesión 15:** La Prudencia (Recto Juicio): Evaluación de Riesgos y Criterio Técnico ante la Presión de Tiempos.
* **Sesión 16:** Alcance Legal y Penal de las Firmas Técnicas en Guatemala: Bitácoras, Memorias y Planos.
* **Sesión 17:** Veracidad e Integridad en Informes Técnicos: Prohibición de Alterar Ensayos y Lecturas de Calidad.
* **Sesión 18:** Compliance Industrial: Prevención de Sobornos, Dádivas y Conflicto de Intereses en Compras.
* **Sesión 19:** Seguridad Psicológica y Canales de Denuncia Ética (*Whistleblowing*) ante Prácticas Ilícitas.
* **Sesión 20:** Taller Integrador B2: Simulación de Juicio Ético por Firma de Orden de Trabajo Defectuosa bajo Presión.

### BIMESTRE 3: Ética Profesional 1 — Deontología Técnica, Automatización e Industria 4.0 (B3-C1)
* **Sesión 21:** Deontología Aplicada: Códigos de Ética de la Ingeniería y Asociaciones Técnicas Internacionales.
* **Sesión 22:** El Deber Fiduciario con el Cliente y la Empresa: Custodia de Recursos y Secreto Profesional.
* **Sesión 23:** Metodología Sistemática para la Resolución de Dilemas Éticos Complejos en Ingeniería.
* **Sesión 24:** La Cuarta Revolución Industrial y el Empleo en Guatemala: Principio de la Transición Justa.
* **Sesión 25:** Primacía de la Persona sobre el Capital y la Tecnología: Humanizar los Procesos Automatizados.
* **Sesión 26:** El Deber Formativo del Supervisor: Planes de Reentrenamiento (*Reskilling* y *Upskilling*) de Operarios.
* **Sesión 27:** Sesgos Algorítmicos en Operaciones: Discriminación en Sistemas de Asignación de Turnos y Méritos.
* **Sesión 28:** Vigilancia Digital, Cámaras Inteligentes y Privacidad: Límites del Monitoreo y Derecho a Desconexión.
* **Sesión 29:** Protección de Secretos Industriales y Propiedad Intelectual: Riesgos de Subir Datos Técnicos a IA Pública.
* **Sesión 30:** Taller Integrador B3: Diseño de un Plan Ético de Modernización y Automatización en una Línea de Planta.

### BIMESTRE 4: Ética Profesional 2 — Bioética Integral, Human-in-the-Loop y Custodia Ambiental (B4-C1)
* **Sesión 31:** Fundamentos de la Bioética: Origen Histórico (Potter, Núremberg); la Técnica al Servicio de la Vida.
* **Sesión 32:** Los 4 Principios Bioéticos Universales: Beneficencia, No Maleficencia, Autonomía y Justicia Distributiva.
* **Sesión 33:** La Dignidad Inviolable de la Vida Humana en Todo su Ciclo: Defensa de la Vida desde la Concepción.
* **Sesión 34:** Ética Frente al Sufrimiento Humano: Cuidados Paliativos vs. Eutanasia y Encarnizamiento Terapéutico.
* **Sesión 35:** El Principio *Human-in-the-Loop* (HITL): Supervisión Humana Obligatoria en Decisiones Críticas de Planta.
* **Sesión 36:** Superación del Sesgo de Automatización (*Automation Bias*): Contraste Crítico con la Física Real.
* **Sesión 37:** Honestidad Académica y Profesional Kinal: Rechazo al Facilismo del "Copiar y Pegar" de IA en Memorias.
* **Sesión 38:** Bioética Ambiental y Custodia de la Creación: Impacto Ecológico de Talleres, Obras y Subestaciones.
* **Sesión 39:** Economía Circular y Manejo Certificado de Residuos Peligrosos: Aceites, Baterías y RAEE (MARN).
* **Sesión 40:** Clausura Anual: Juramento Deontológico del Egresado TSU Kinal y Decálogo de Integridad Profesional.

---

## 5. Dictamen Académico y Articulación con el Plan Maestro TSU

1. **Plena Continuidad Antropológica:** Se preserva el 100% de la doctrina moral y virtudes del programa del Prof. Donis, asegurando que el alumno cultive la inteligencia, voluntad, libertad, prudencia, laboriosidad y generosidad.
2. **Pertinencia Industrial en Guatemala:** Se corrigen las desviaciones vocacionales sustituyendo normativas de medicina y periodismo por las verdaderas responsabilidades del supervisor técnico: firmas de bitácoras, prevención de sobornos y seguridad de cuadrillas.
3. **Vanguardia en IA y Medio Ambiente:** Se incorporan los debates contemporáneos más urgentes de la supervisión técnica: gobernanza HITL de sistemas autónomos y responsabilidad ecológica certificada.
4. **Artefactos Locales Generados:**
   - HTML Interactivo Continuo: `TSU/etica_auditoria.html`
   - Réplica en Repositorio Local: `curricula-2026/TSU/etica_auditoria.html`
   - Respaldo MyBrain: `MyBrain/01 - My Brain/Kinal/TSU/etica_auditoria.html`
"""
    with open("TSU/TEMARIO_Y_AUDITORIA_ETICA_TSU.md", "w", encoding="utf-8") as f:
        f.write(md_content)
    print("TSU/TEMARIO_Y_AUDITORIA_ETICA_TSU.md generado con éxito.")

if __name__ == "__main__":
    generate_etica_html()
    generate_etica_markdown()
