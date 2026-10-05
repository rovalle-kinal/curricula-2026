#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import os

AUDITORIA_PATH = "TSU/auditoria_curricular.html"
ADMIN_PATH = "TSU/administracion_auditoria.html"
ETICA_PATH = "TSU/etica_auditoria.html"
MAT_PATH = "TSU/matematica_auditoria.html"

# ==============================================================================
# 1. ACTUALIZAR HEADER Y BOTONES EN ETICA Y MATEMATICA
# ==============================================================================
with open(ETICA_PATH, "r", encoding="utf-8") as f:
    etica_html = f.read()

# Estandarizar botón volver en header
etica_html = re.sub(
    r'<a href="auditoria_curricular\.html"[^>]*>.*?Auditoría General.*?</a>',
    '<a href="auditoria_curricular.html" class="px-3.5 py-1.5 rounded-lg bg-amber-500 hover:bg-amber-400 text-slate-950 transition flex items-center gap-1.5 font-bold shadow-sm text-xs"><i data-lucide="arrow-left" class="w-3.5 h-3.5"></i> Volver a Auditoría General (20 Cursos)</a>',
    etica_html,
    flags=re.DOTALL
)

# Agregar botón inferior si no existe
if "Volver a Auditoría General (20 Cursos)" not in etica_html[etica_html.rfind('</section>'):]:
    bottom_btn = """
        <div class="text-center py-8 no-print border-t border-slate-200 mt-10">
            <a href="auditoria_curricular.html" class="inline-flex items-center gap-2 px-6 py-3 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-extrabold text-sm shadow-md transition">
                <i data-lucide="arrow-left" class="w-4 h-4"></i> Volver a Auditoría General (20 Cursos)
            </a>
        </div>
    """
    etica_html = re.sub(r'(</main>)', bottom_btn + r'\1', etica_html)

with open(ETICA_PATH, "w", encoding="utf-8") as f:
    f.write(etica_html)
print(f"Actualizado {ETICA_PATH}")

# MATEMATICA
with open(MAT_PATH, "r", encoding="utf-8") as f:
    mat_html = f.read()

mat_html = re.sub(
    r'<a href="auditoria_curricular\.html"[^>]*>.*?Auditoría General.*?</a>',
    '<a href="auditoria_curricular.html" class="px-3.5 py-1.5 rounded-lg bg-amber-500 hover:bg-amber-400 text-slate-950 transition flex items-center gap-1.5 font-bold shadow-sm text-xs"><i data-lucide="arrow-left" class="w-3.5 h-3.5"></i> Volver a Auditoría General (20 Cursos)</a>',
    mat_html,
    flags=re.DOTALL
)

if "Volver a Auditoría General (20 Cursos)" not in mat_html[mat_html.rfind('</section>'):]:
    bottom_btn = """
        <div class="text-center py-8 no-print border-t border-slate-200 mt-10">
            <a href="auditoria_curricular.html" class="inline-flex items-center gap-2 px-6 py-3 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-extrabold text-sm shadow-md transition">
                <i data-lucide="arrow-left" class="w-4 h-4"></i> Volver a Auditoría General (20 Cursos)
            </a>
        </div>
    """
    mat_html = re.sub(r'(</main>)', bottom_btn + r'\1', mat_html)

with open(MAT_PATH, "w", encoding="utf-8") as f:
    f.write(mat_html)
print(f"Actualizado {MAT_PATH}")

# ==============================================================================
# 2. ACTUALIZAR ADMINISTRACION PARA HOMOLOGAR AL 100%
# ==============================================================================
with open(ADMIN_PATH, "r", encoding="utf-8") as f:
    admin_html = f.read()

# Homologar Top Header
admin_top_header = """    <!-- Top Navigation Bar -->
    <header class="bg-slate-900 text-white sticky top-0 z-50 border-b border-slate-800 shadow-md">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
            <div class="flex items-center gap-3">
                <div class="w-9 h-9 rounded-xl bg-blue-600/30 border border-blue-500/40 flex items-center justify-center text-amber-400 shadow-inner">
                    <i data-lucide="briefcase" class="w-5 h-5"></i>
                </div>
                <div>
                    <span class="text-xs uppercase tracking-wider text-amber-400 font-extrabold block">Fundación Kinal • TSU 2026</span>
                    <h1 class="text-sm font-bold text-slate-100 flex items-center gap-2">
                        Auditoría Curricular: Línea de Gestión y Supervisión Industrial
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
    </header>"""

admin_html = re.sub(r'<header class="bg-slate-900.*?</header>', admin_top_header, admin_html, flags=re.DOTALL)

# Homologar Hero a Dark Gradient
admin_hero = """        <!-- Encabezado Principal y Contexto -->
        <section class="bg-gradient-to-br from-slate-900 via-blue-950 to-slate-900 rounded-3xl p-6 sm:p-10 text-white shadow-xl relative overflow-hidden border border-slate-800">
            <div class="absolute -right-16 -top-16 w-80 h-80 bg-blue-500/10 rounded-full blur-3xl pointer-events-none"></div>
            <div class="max-w-3xl space-y-4 relative z-10">
                <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-500/20 text-blue-300 text-xs font-bold border border-blue-400/30">
                    <i data-lucide="scale" class="w-3.5 h-3.5 text-amber-400"></i> Diagnóstico Pedagógico y Metodológico 2026
                </div>
                <h2 class="text-2xl sm:text-4xl font-extrabold tracking-tight text-white leading-tight">
                    Auditoría Curricular Cuatricolor: Curso de Administración
                </h2>
                <p class="text-slate-300 text-sm sm:text-base leading-relaxed">
                    Evaluación sistemática de los 8 planes de clase (40 sesiones anuales) desarrollados por el instructor <strong>Sergio J. Ávalos Austria</strong>. Metodología cuatricolor aplicada para la gestión operativa, liderazgo técnico, productividad Lean y cumplimiento laboral en Guatemala.
                </p>
                <div class="pt-2 flex flex-wrap gap-4 text-xs text-slate-300">
                    <div class="flex items-center gap-1.5 bg-slate-800/80 px-3 py-1.5 rounded-lg border border-slate-700">
                        <i data-lucide="user-check" class="w-4 h-4 text-amber-400"></i> <strong>Instructor Analizado:</strong> Sergio J. Ávalos Austria
                    </div>
                    <div class="flex items-center gap-1.5 bg-slate-800/80 px-3 py-1.5 rounded-lg border border-slate-700">
                        <i data-lucide="book-open" class="w-4 h-4 text-emerald-400"></i> <strong>Carga Anual:</strong> 8 Módulos • 40 Sesiones (50 min) • 108 Horas
                    </div>
                    <div class="flex items-center gap-1.5 bg-slate-800/80 px-3 py-1.5 rounded-lg border border-slate-700">
                        <i data-lucide="award" class="w-4 h-4 text-blue-400"></i> <strong>Aprobación Mínima:</strong> 75 Puntos / 100
                    </div>
                </div>
            </div>
        </section>"""

admin_html = re.sub(r'<!-- Hero del Curso -->\s*<div class="bg-white rounded-2xl border.*?</div>\s*</div>\s*<!-- Tarjetas de Métricas', admin_hero + '\n\n        <!-- Tarjetas de Métricas', admin_html, flags=re.DOTALL)

# Botón de retorno al final
if "Volver a Auditoría General (20 Cursos)" not in admin_html[admin_html.rfind('</section>'):]:
    bottom_btn = """
        <div class="text-center py-8 no-print border-t border-slate-200 mt-10">
            <a href="auditoria_curricular.html" class="inline-flex items-center gap-2 px-6 py-3 rounded-xl bg-amber-500 hover:bg-amber-400 text-slate-950 font-extrabold text-sm shadow-md transition">
                <i data-lucide="arrow-left" class="w-4 h-4"></i> Volver a Auditoría General (20 Cursos)
            </a>
        </div>
    """
    admin_html = re.sub(r'(</main>)', bottom_btn + r'\1', admin_html)

with open(ADMIN_PATH, "w", encoding="utf-8") as f:
    f.write(admin_html)
print(f"Actualizado {ADMIN_PATH}")

