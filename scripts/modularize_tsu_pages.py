#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Modularizador del Currículo TSU:
1. Genera TSU/temarios_por_linea.html con las 4 líneas de estudio (20 cursos).
2. Genera TSU/auditoria_curricular.html con la matriz general de 20 cursos y barra de subnivel para las auditorías individuales (Admón, Ética, Matemática).
3. Adelgaza TSU/index.html reemplazando los bloques extensos con tarjetas portales hacia las páginas modulares y limpiando la barra de navegación.
4. Actualiza index.html raíz.
"""

import re
import os

INDEX_PATH = "TSU/index.html"
TEMARIOS_PATH = "TSU/temarios_por_linea.html"
AUDITORIA_PATH = "TSU/auditoria_curricular.html"
ROOT_INDEX_PATH = "index.html"

with open(INDEX_PATH, "r", encoding="utf-8") as f:
    lines = f.readlines()

s3_idx = None
s4_idx = None
s5_idx = None

for i, l in enumerate(lines):
    if "<!-- SECCIÓN 3: TEMARIOS" in l:
        s3_idx = i - 1  # banner separator
    elif "<!-- SECCIÓN 4: AUDITORÍA" in l:
        s4_idx = i - 1
    elif "<!-- SECCIÓN 5: DISTRIBUCIÓN" in l:
        s5_idx = i - 1

# Extract lines
temarios_lines = lines[s3_idx:s4_idx]
temarios_raw = "".join(temarios_lines)

auditoria_lines = lines[s4_idx:s5_idx]
auditoria_raw = "".join(auditoria_lines)

# Fix links in temarios: #audit- to auditoria_curricular.html#audit-
temarios_clean = re.sub(r'href="#audit-', r'href="auditoria_curricular.html#audit-', temarios_raw)
temarios_clean = re.sub(r'href="#seccion-mapa"', r'href="index.html#seccion-mapa"', temarios_clean)

# Fix links in auditoria: #temario- to temarios_por_linea.html#temario-
auditoria_clean = re.sub(r'href="#temario-', r'href="temarios_por_linea.html#temario-', auditoria_raw)

# Extract CSS stylesheet from index.html (lines 1 to 940)
head_lines = lines[:940]
css_head = "".join(head_lines)

# -------------------------------------------------------------
# 1. CONSTRUIR TSU/temarios_por_linea.html
# -------------------------------------------------------------
temarios_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Temarios por Línea de Estudio (20 Cursos) | TSU Kinal 2026</title>
{css_head[css_head.find('<style>'):css_head.find('</style>')+8]}
</head>
<body>

<div class="app-container">

    <!-- HERO HEADER -->
    <header class="main-header">
        <div class="hero-top">
            <span class="badge-hero">Currículo Oficial 2026 • 20 Asignaturas</span>
            <span class="badge-accent">DQR Nivel 6 • Sistema Dual</span>
        </div>
        <h1><span>📚</span> Temarios Modernizados por Línea de Estudio</h1>
        <p class="hero-subtitle">
            Desglose exhaustivo de las 4 unidades temáticas por asignatura, vinculación práctica con Inteligencia Artificial (Human-in-the-Loop), herramientas industriales y entregables verificables para las 4 líneas formativas del TSU.
        </p>
    </header>

    <!-- STICKY NAVBAR -->
    <nav class="sticky-nav">
        <a href="index.html" style="color: #f59e0b; font-weight: 700; background: rgba(217, 119, 6, 0.15); border-radius: 8px;"><span>←</span> Portal TSU (Mapa & Red)</a>
        <a href="../index.html"><span>🏠</span> Portal Maestro</a>
        <a href="temarios_por_linea.html" class="active"><span>📚</span> Temarios por Línea</a>
        <a href="auditoria_curricular.html" style="color: #67e8f9; font-weight: 700;"><span>⚖️</span> Auditoría & Dictamen</a>
        <a href="index.html#seccion-bimestres"><span>🗓️</span> Distribución Bimestral</a>
    </nav>

    <main class="main-content">
{temarios_clean}
    </main>

    <footer style="background: #0b1f3a; color: #94a3b8; padding: 24px 40px; text-align: center; font-size: 0.85rem; border-top: 3px solid var(--kinal-accent);">
        <p><strong>Fundación Kinal</strong> • Dirección Académica / Coordinación TSU 2026 • Formación Dual DQR 6</p>
    </footer>

</div>

<script>
    function filterByLinea(lineaId, btn) {{
        document.querySelectorAll('.linea-tabs .tab-btn').forEach(b => b.classList.remove('active'));
        if (btn) btn.classList.add('active');

        document.querySelectorAll('.linea-section').forEach(sec => {{
            sec.style.display = (lineaId === 'all' || sec.id === lineaId) ? 'block' : 'none';
        }});
    }}

    function filterTemarios() {{
        const query = document.getElementById('searchInput').value.toLowerCase().trim();
        document.querySelectorAll('.temario-card').forEach(card => {{
            card.style.display = card.innerText.toLowerCase().includes(query) ? 'block' : 'none';
        }});
    }}

    function toggleUnidades(id) {{
        const content = document.getElementById('unidades-' + id);
        if (content) {{
            content.style.display = (content.style.display === 'none') ? 'grid' : 'none';
        }}
    }}

    function toggleAllUnidades(expand) {{
        document.querySelectorAll('.unidades-content').forEach(content => {{
            content.style.display = expand ? 'grid' : 'none';
        }});
    }}
</script>

</body>
</html>
"""

with open(TEMARIOS_PATH, "w", encoding="utf-8") as f:
    f.write(temarios_html)
print(f"Generado {TEMARIOS_PATH} ({len(temarios_html)} bytes)")

# -------------------------------------------------------------
# 2. CONSTRUIR TSU/auditoria_curricular.html
# -------------------------------------------------------------
auditoria_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Auditoría Curricular y Matriz de Dictamen (20 Cursos) | TSU Kinal 2026</title>
{css_head[css_head.find('<style>'):css_head.find('</style>')+8]}
    <style>
        .subnav-auditorias {{
            background: #0f172a;
            padding: 14px 32px;
            border-bottom: 2px solid #334155;
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 14px;
        }}
        .subnav-badge {{
            background: #1e293b;
            color: #f59e0b;
            border: 1px solid #d97706;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.75rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        .subnav-label {{
            color: #cbd5e1;
            font-size: 0.88rem;
            font-weight: 600;
        }}
        .subnav-links {{
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }}
        .subnav-btn {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 8px 16px;
            border-radius: 8px;
            font-size: 0.84rem;
            font-weight: 700;
            text-decoration: none;
            transition: all 0.2s;
            box-shadow: 0 2px 4px rgba(0,0,0,0.2);
        }}
        .subnav-btn-admon {{
            background: #1e3a8a;
            color: #dbeafe;
            border: 1px solid #3b82f6;
        }}
        .subnav-btn-admon:hover {{
            background: #2563eb;
            color: #ffffff;
            transform: translateY(-1px);
        }}
        .subnav-btn-etica {{
            background: #0c4a6e;
            color: #e0f2fe;
            border: 1px solid #0284c7;
        }}
        .subnav-btn-etica:hover {{
            background: #0284c7;
            color: #ffffff;
            transform: translateY(-1px);
        }}
        .subnav-btn-matematica {{
            background: #064e3b;
            color: #d1fae5;
            border: 1px solid #10b981;
        }}
        .subnav-btn-matematica:hover {{
            background: #059669;
            color: #ffffff;
            transform: translateY(-1px);
        }}

        .audit-filter-panel {{
            background: #ffffff;
            border: 1px solid var(--border-color);
            border-radius: 10px;
            padding: 20px 24px;
            margin-bottom: 28px;
            display: flex;
            flex-direction: column;
            gap: 14px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.03);
        }}
        .audit-filter-row {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 12px;
        }}
        .filter-btn-group {{
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
        }}
        .audit-filter-btn {{
            background: #f8fafc;
            border: 1px solid var(--border-color);
            padding: 6px 14px;
            border-radius: 6px;
            font-size: 0.84rem;
            font-weight: 600;
            color: var(--text-dark);
            cursor: pointer;
            transition: all 0.2s;
        }}
        .audit-filter-btn.active {{
            background: var(--kinal-blue);
            color: #ffffff;
            border-color: var(--kinal-blue);
        }}
    </style>
</head>
<body>

<div class="app-container">

    <!-- HERO HEADER -->
    <header class="main-header">
        <div class="hero-top">
            <span class="badge-hero">Evaluación Diagnóstica Curricular • 20 Asignaturas</span>
            <span class="badge-accent">DQR Nivel 6 • Sistema Dual</span>
        </div>
        <h1><span>⚖️</span> Auditoría Curricular y Matriz de Dictamen</h1>
        <p class="hero-subtitle">
            Diagnóstico formal comparativo del pensum: análisis riguroso de contenidos anulados por obsolescencia, actualizaciones metodológicas a la Industria 4.0 y nuevas competencias técnicas incorporadas para el mando medio.
        </p>
    </header>

    <!-- STICKY NAVBAR NIVEL 1 -->
    <nav class="sticky-nav">
        <a href="index.html" style="color: #f59e0b; font-weight: 700; background: rgba(217, 119, 6, 0.15); border-radius: 8px;"><span>←</span> Portal TSU (Mapa & Red)</a>
        <a href="../index.html"><span>🏠</span> Portal Maestro</a>
        <a href="temarios_por_linea.html" style="color: #fef08a; font-weight: 700;"><span>📚</span> Temarios por Línea</a>
        <a href="auditoria_curricular.html" class="active"><span>⚖️</span> Auditoría General (20 Cursos)</a>
        <a href="index.html#seccion-bimestres"><span>🗓️</span> Distribución Bimestral</a>
    </nav>

    <!-- SUBNAV NIVEL 2: AUDITORÍAS INDIVIDUALES POR ASIGNATURA -->
    <div class="subnav-auditorias">
        <div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap;">
            <span class="subnav-badge">Nivel de Detalle Quirúrgico</span>
            <span class="subnav-label">Auditorías Específicas por Asignatura:</span>
        </div>
        <div class="subnav-links">
            <a href="administracion_auditoria.html" class="subnav-btn subnav-btn-admon">
                <span>💼</span> Auditoría Administración
            </a>
            <a href="etica_auditoria.html" class="subnav-btn subnav-btn-etica">
                <span>🛡️</span> Auditoría Ética Profesional
            </a>
            <a href="matematica_auditoria.html" class="subnav-btn subnav-btn-matematica">
                <span>📐</span> Auditoría Matemáticas
            </a>
        </div>
    </div>

    <main class="main-content">

        <!-- Panel de Filtros para la Auditoría -->
        <div class="audit-filter-panel">
            <div class="audit-filter-row">
                <div style="display: flex; align-items: center; gap: 8px;">
                    <span style="font-weight: 700; font-size: 0.88rem; color: var(--kinal-blue);">Filtrar por Línea:</span>
                    <div class="filter-btn-group">
                        <button class="audit-filter-btn active" onclick="filterAuditByLinea('all', this)">Todas (20)</button>
                        <button class="audit-filter-btn" onclick="filterAuditByLinea('linea-etica', this)">🛡️ Ética (4)</button>
                        <button class="audit-filter-btn" onclick="filterAuditByLinea('linea-gestion', this)">📋 Gestión (8)</button>
                        <button class="audit-filter-btn" onclick="filterAuditByLinea('linea-matematica', this)">📐 Exactas (4)</button>
                        <button class="audit-filter-btn" onclick="filterAuditByLinea('linea-fisica', this)">⚡ Física (4)</button>
                    </div>
                </div>
                <div style="display: flex; align-items: center; gap: 8px;">
                    <span style="font-weight: 700; font-size: 0.88rem; color: var(--kinal-blue);">Bimestre:</span>
                    <div class="filter-btn-group">
                        <button class="audit-filter-btn active" onclick="filterAuditByBimestre('all', this)">Todos</button>
                        <button class="audit-filter-btn" onclick="filterAuditByBimestre('1', this)">B1</button>
                        <button class="audit-filter-btn" onclick="filterAuditByBimestre('2', this)">B2</button>
                        <button class="audit-filter-btn" onclick="filterAuditByBimestre('3', this)">B3</button>
                        <button class="audit-filter-btn" onclick="filterAuditByBimestre('4', this)">B4</button>
                    </div>
                </div>
            </div>
        </div>

{auditoria_clean}
    </main>

    <footer style="background: #0b1f3a; color: #94a3b8; padding: 24px 40px; text-align: center; font-size: 0.85rem; border-top: 3px solid var(--kinal-accent);">
        <p><strong>Fundación Kinal</strong> • Dirección Académica / Coordinación TSU 2026 • Formación Dual DQR 6</p>
    </footer>

</div>

<script>
    let currentLinea = 'all';
    let currentBimestre = 'all';

    function filterAuditByLinea(linea, btn) {{
        currentLinea = linea;
        btn.parentElement.querySelectorAll('.audit-filter-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        applyAuditFilters();
    }}

    function filterAuditByBimestre(bimestre, btn) {{
        currentBimestre = bimestre;
        btn.parentElement.querySelectorAll('.audit-filter-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        applyAuditFilters();
    }}

    function applyAuditFilters() {{
        document.querySelectorAll('.audit-card').forEach(card => {{
            const cardLinea = card.getAttribute('data-linea');
            const cardBimestre = card.getAttribute('data-bimestre');

            const matchLinea = (currentLinea === 'all' || cardLinea === currentLinea);
            const matchBimestre = (currentBimestre === 'all' || cardBimestre === currentBimestre);

            card.style.display = (matchLinea && matchBimestre) ? 'block' : 'none';
        }});
    }}
</script>

</body>
</html>
"""

with open(AUDITORIA_PATH, "w", encoding="utf-8") as f:
    f.write(auditoria_html)
print(f"Generado {AUDITORIA_PATH} ({len(auditoria_html)} bytes)")

# -------------------------------------------------------------
# 3. ACTUALIZAR TSU/index.html
# -------------------------------------------------------------
# Tarjetas resumen en lugar de los 3,500 renglones
replacement_portal_cards = """        <!-- ======================================================== -->
        <!-- SECCIÓN 3: TEMARIOS MODERNIZADOS POR LÍNEA DE ESTUDIO   -->
        <!-- ======================================================== -->
        <section class="portal-section" id="seccion-temarios" style="background: linear-gradient(135deg, #f8fafc 0%, #edf2f7 100%); border: 1px solid var(--border-color); border-radius: 12px; padding: 32px 36px; margin-bottom: 40px;">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 20px;">
                <div style="max-width: 820px;">
                    <span style="display: inline-block; background: #e0f2fe; color: #0369a1; border: 1px solid #bae6fd; padding: 4px 12px; border-radius: 20px; font-size: 0.78rem; font-weight: 700; text-transform: uppercase; margin-bottom: 12px;">
                        Plan Temático Oficial • 20 Asignaturas
                    </span>
                    <h2 style="font-size: 1.6rem; color: var(--kinal-blue); margin-bottom: 10px; display: flex; align-items: center; gap: 10px;">
                        <span>📚</span> Temarios Modernizados por Línea de Estudio
                    </h2>
                    <p style="color: var(--text-dark); font-size: 0.95rem; line-height: 1.6; margin-bottom: 16px;">
                        Desglose exhaustivo de las 4 unidades temáticas por curso, vinculación práctica con Inteligencia Artificial (Human-in-the-Loop), herramientas industriales y entregables verificables en las 4 líneas formativas:
                    </p>
                    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 12px; margin-bottom: 20px;">
                        <div style="background: #ffffff; border: 1px solid var(--border-light); padding: 12px 14px; border-radius: 8px;">
                            <div style="font-size: 0.82rem; font-weight: 700; color: #0284c7;">🛡️ Formación Humana y Ética</div>
                            <div style="font-size: 0.76rem; color: var(--text-muted);">4 Asignaturas • 54.0 Horas</div>
                        </div>
                        <div style="background: #ffffff; border: 1px solid var(--border-light); padding: 12px 14px; border-radius: 8px;">
                            <div style="font-size: 0.82rem; font-weight: 700; color: #d97706;">📋 Gestión & Supervisión</div>
                            <div style="font-size: 0.76rem; color: var(--text-muted);">8 Asignaturas • 108.0 Horas</div>
                        </div>
                        <div style="background: #ffffff; border: 1px solid var(--border-light); padding: 12px 14px; border-radius: 8px;">
                            <div style="font-size: 0.82rem; font-weight: 700; color: #16a34a;">📐 Ciencias Exactas y Analítica</div>
                            <div style="font-size: 0.76rem; color: var(--text-muted);">4 Asignaturas • 54.0 Horas</div>
                        </div>
                        <div style="background: #ffffff; border: 1px solid var(--border-light); padding: 12px 14px; border-radius: 8px;">
                            <div style="font-size: 0.82rem; font-weight: 700; color: #7c3aed;">⚡ Física & Industria 4.0</div>
                            <div style="font-size: 0.76rem; color: var(--text-muted);">4 Asignaturas • 54.0 Horas</div>
                        </div>
                    </div>
                </div>
                <div style="align-self: center;">
                    <a href="temarios_por_linea.html" style="display: inline-flex; align-items: center; gap: 8px; background: var(--kinal-blue); color: #ffffff; padding: 14px 26px; border-radius: 10px; font-weight: 700; text-decoration: none; font-size: 0.95rem; box-shadow: 0 4px 14px rgba(15,45,89,0.25); transition: all 0.2s;">
                        <span>📚</span> Ver Temarios Detallados por Línea →
                    </a>
                </div>
            </div>
        </section>

        <!-- ======================================================== -->
        <!-- SECCIÓN 4: AUDITORÍA CURRICULAR Y MATRIZ DE DICTAMEN     -->
        <!-- ======================================================== -->
        <section class="portal-section" id="seccion-auditoria" style="background: linear-gradient(135deg, #0b1f3a 0%, #0f2d59 100%); color: #ffffff; border-radius: 12px; padding: 32px 36px; margin-bottom: 40px; box-shadow: 0 4px 20px rgba(0,0,0,0.12);">
            <div style="display: flex; justify-content: space-between; align-items: flex-start; flex-wrap: wrap; gap: 20px;">
                <div style="max-width: 820px;">
                    <span style="display: inline-block; background: rgba(217,119,6,0.2); color: #fef08a; border: 1px solid rgba(217,119,6,0.4); padding: 4px 12px; border-radius: 20px; font-size: 0.78rem; font-weight: 700; text-transform: uppercase; margin-bottom: 12px;">
                        Auditoría Integral • Dictámenes y Transformación
                    </span>
                    <h2 style="font-size: 1.6rem; color: #ffffff; margin-bottom: 10px; display: flex; align-items: center; gap: 10px;">
                        <span>⚖️</span> Auditoría Curricular y Matriz de Dictamen
                    </h2>
                    <p style="color: #cbd5e1; font-size: 0.95rem; line-height: 1.6; margin-bottom: 16px;">
                        Diagnóstico formal comparativo para las 20 asignaturas del pensum: identificación de temas obsoletos a anular, modernizaciones metodológicas requeridas e inserción de nuevas competencias técnicas demandadas por la industria guatemalteca e internacional.
                    </p>
                    <div style="display: flex; gap: 14px; flex-wrap: wrap; margin-bottom: 8px;">
                        <div style="background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.15); padding: 10px 16px; border-radius: 8px;">
                            <span style="color: #f87171; font-weight: 800; font-size: 0.88rem;">🔴 Anulaciones</span>
                            <div style="color: #94a3b8; font-size: 0.75rem;">Teoría abstracta sin aplicación en planta</div>
                        </div>
                        <div style="background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.15); padding: 10px 16px; border-radius: 8px;">
                            <span style="color: #facc15; font-weight: 800; font-size: 0.88rem;">🟡 Actualizaciones</span>
                            <div style="color: #94a3b8; font-size: 0.75rem;">Migración a estándares Industria 4.0</div>
                        </div>
                        <div style="background: rgba(255,255,255,0.08); border: 1px solid rgba(255,255,255,0.15); padding: 10px 16px; border-radius: 8px;">
                            <span style="color: #60a5fa; font-weight: 800; font-size: 0.88rem;">🔵 Nuevos Contenidos</span>
                            <div style="color: #94a3b8; font-size: 0.75rem;">IA, SPC, Normas ISO/SAT/DQR 6</div>
                        </div>
                    </div>
                </div>
                <div style="align-self: center;">
                    <a href="auditoria_curricular.html" style="display: inline-flex; align-items: center; gap: 8px; background: #d97706; color: #ffffff; padding: 14px 26px; border-radius: 10px; font-weight: 700; text-decoration: none; font-size: 0.95rem; box-shadow: 0 4px 14px rgba(217,119,6,0.3); transition: all 0.2s;">
                        <span>⚖️</span> Explorar Auditoría y Matriz de Dictamen →
                    </a>
                </div>
            </div>
        </section>
"""

new_index_lines = lines[:s3_idx] + [replacement_portal_cards] + lines[s5_idx:]
new_index_content = "".join(new_index_lines)

# Limpiar navbar en TSU/index.html (quitar botones individuales de auditoría)
new_nav = """    <!-- STICKY NAVBAR -->
    <nav class="sticky-nav">
        <a href="../index.html" style="color: #f59e0b; font-weight: 700; background: rgba(217, 119, 6, 0.15); border-radius: 8px;"><span>←</span> Portal Maestro</a>
        <a href="#seccion-resumen" class="active"><span>📋</span> Resumen & Especialidades</a>
        <a href="#seccion-mapa"><span>🗺️</span> Mapa Curricular & Red</a>
        <a href="temarios_por_linea.html" style="color: #fef08a; font-weight: 700;"><span>📚</span> Temarios por Línea</a>
        <a href="auditoria_curricular.html" style="color: #67e8f9; font-weight: 700;"><span>⚖️</span> Auditoría & Dictamen</a>
        <a href="#seccion-bimestres"><span>🗓️</span> Distribución Bimestral</a>
    </nav>"""

new_index_content = re.sub(r'<!-- STICKY NAVBAR -->\s*<nav class="sticky-nav">.*?</nav>', new_nav, new_index_content, flags=re.DOTALL)

# Actualizar enlaces del panel lateral del mapa interactivo
new_index_content = re.sub(
    r"document\.getElementById\('sideLinkTemario'\)\.href = '#temario-' \+ course\.id;",
    "document.getElementById('sideLinkTemario').href = 'temarios_por_linea.html#temario-' + course.id;",
    new_index_content
)
new_index_content = re.sub(
    r"document\.getElementById\('sideLinkAudit'\)\.href = '#audit-' \+ course\.id;",
    "document.getElementById('sideLinkAudit').href = 'auditoria_curricular.html#audit-' + course.id;",
    new_index_content
)

with open(INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(new_index_content)
print(f"Actualizado {INDEX_PATH} ({len(new_index_content)} bytes)")

# -------------------------------------------------------------
# 4. ACTUALIZAR index.html RAÍZ
# -------------------------------------------------------------
with open(ROOT_INDEX_PATH, "r", encoding="utf-8") as f:
    root_content = f.read()

# Actualizar grid del TSU para tener botones secundarios limpios (Temarios por Línea y Auditoría & Matriz)
root_tsu_grid = """                    <div class="grid grid-cols-1 sm:grid-cols-2 gap-2 pt-1">
                        <a href="TSU/temarios_por_linea.html" class="py-2.5 px-3 rounded-xl bg-blue-50 hover:bg-blue-100 text-blue-900 font-bold text-xs transition flex items-center justify-center gap-1.5 border border-blue-200 text-center">
                            <i data-lucide="book-open" class="w-4 h-4 text-blue-600"></i> Temarios por Línea
                        </a>
                        <a href="TSU/auditoria_curricular.html" class="py-2.5 px-3 rounded-xl bg-amber-50 hover:bg-amber-100 text-amber-900 font-bold text-xs transition flex items-center justify-center gap-1.5 border border-amber-200 text-center">
                            <i data-lucide="scale" class="w-4 h-4 text-amber-600"></i> Auditoría & Matriz
                        </a>
                    </div>"""

root_content = re.sub(
    r'<div class="grid grid-cols-1 sm:grid-cols-[23] gap-2 pt-1">.*?</div>\s*</div>\s*</div>\s*<!-- PILAR 2',
    root_tsu_grid + '\n                </div>\n            </div>\n\n            <!-- PILAR 2',
    root_content,
    flags=re.DOTALL
)

with open(ROOT_INDEX_PATH, "w", encoding="utf-8") as f:
    f.write(root_content)
print(f"Actualizado {ROOT_INDEX_PATH}")
