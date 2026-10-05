#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import os

AUDITORIA_PATH = "TSU/auditoria_curricular.html"
INDEX_PATH = "TSU/index.html"

with open(AUDITORIA_PATH, "r", encoding="utf-8") as f:
    orig_html = f.read()

# Parse the 20 cards
card_pattern = re.compile(
    r'<article class="audit-card" id="([^"]+)" data-bimestre="([^"]+)" data-linea="([^"]+)">\s*'
    r'<div class="audit-card-header">\s*'
    r'<div class="audit-meta">\s*'
    r'<span class="badge-bimestre">([^<]+)</span>\s*'
    r'<span class="badge-code">([^<]+)</span>\s*'
    r'<span class="badge-eje">([^<]+)</span>\s*'
    r'</div>\s*'
    r'<h3>(.*?)</h3>\s*'
    r'<div class="audit-sub">([^<]+)</div>\s*'
    r'</div>\s*'
    r'<div class="audit-body">(.*?)</div>\s*'
    r'</article>',
    re.DOTALL
)

matches = card_pattern.findall(orig_html)
print(f"Encontradas {len(matches)} tarjetas de auditoría para procesar.")

courses_data = []
for cid, b, l, bb, code, eje, title, sub, body in matches:
    # Extraer diagnósticos
    red = re.search(r'class="audit-callout callout-red">\s*(?:<strong>[^<]+</strong>)?\s*(.*?)\s*</div>', body, re.DOTALL)
    yellow = re.search(r'class="audit-callout callout-yellow">\s*(?:<strong>[^<]+</strong>)?\s*(.*?)\s*</div>', body, re.DOTALL)
    blue = re.search(r'class="audit-callout callout-blue">\s*(?:<strong>[^<]+</strong>)?\s*(.*?)\s*</div>', body, re.DOTALL)
    orig = re.search(r'<td><strong>Contenido Original \(Pensum Previo\)</strong></td>\s*<td>.*?</td>\s*<td>(.*?)</td>', body, re.DOTALL)
    just = re.search(r'class="audit-justificacion">(.*?)</div>', body, re.DOTALL)
    temario_link = re.search(r'href="(temarios_por_linea\.html#[^"]+)"', body)
    
    # Limpiar textos para tabla ejecutiva
    def clean_text(m):
        if not m: return "—"
        txt = re.sub(r'<[^>]+>', '', m.group(1)).strip()
        txt = re.sub(r'^(Motivo de anulación|Modernización|Innovación 2026):\s*', '', txt)
        return txt

    courses_data.append({
        "cid": cid,
        "bimestre": b,
        "linea": l,
        "badge_bimestre": bb.strip(),
        "code": code.strip(),
        "eje": eje.strip(),
        "title": title.strip(),
        "sub": sub.strip(),
        "body_html": body.strip(),
        "red_text": clean_text(red),
        "yellow_text": clean_text(yellow),
        "blue_text": clean_text(blue),
        "orig_text": clean_text(orig),
        "temario_url": temario_link.group(1) if temario_link else f"temarios_por_linea.html#{cid.replace('audit-', 'temario-')}"
    })

# Extraer estilos base de index.html
with open(INDEX_PATH, "r", encoding="utf-8") as f:
    idx_content = f.read()

style_match = re.search(r'(<style>.*?</style>)', idx_content, re.DOTALL)
base_styles = style_match.group(1) if style_match else ""

# Generar filas de la Matriz Resumen Ejecutiva
matrix_rows_html = ""
for c in courses_data:
    matrix_rows_html += f"""
        <tr class="matrix-row" data-bimestre="{c['bimestre']}" data-linea="{c['linea']}" id="row-{c['cid']}">
            <td style="white-space: nowrap;">
                <span class="badge-bimestre">B{c['bimestre']}</span>
                <span class="badge-code">{c['code']}</span>
            </td>
            <td>
                <div style="font-weight: 700; color: var(--kinal-blue); font-size: 0.9rem;">{c['title']}</div>
                <div style="font-size: 0.76rem; color: var(--text-muted);">{c['sub']}</div>
            </td>
            <td style="font-size: 0.82rem; color: #991b1b; background: #fff5f5;">
                <strong style="display: block; font-size: 0.72rem; text-transform: uppercase; color: #dc2626;">🔴 Anular:</strong>
                {c['red_text'][:120]}{'...' if len(c['red_text']) > 120 else ''}
            </td>
            <td style="font-size: 0.82rem; color: #854d0e; background: #fefce8;">
                <strong style="display: block; font-size: 0.72rem; text-transform: uppercase; color: #ca8a04;">🟡 Actualizar:</strong>
                {c['yellow_text'][:120]}{'...' if len(c['yellow_text']) > 120 else ''}
            </td>
            <td style="font-size: 0.82rem; color: #1e40af; background: #eff6ff;">
                <strong style="display: block; font-size: 0.72rem; text-transform: uppercase; color: #2563eb;">🔵 Incorporar:</strong>
                {c['blue_text'][:120]}{'...' if len(c['blue_text']) > 120 else ''}
            </td>
            <td style="text-align: center; white-space: nowrap;">
                <button onclick="toggleCardDetail('{c['cid']}')" class="btn-toggle-row" style="background: var(--kinal-blue); color: #ffffff; border: none; padding: 4px 10px; border-radius: 5px; font-size: 0.75rem; font-weight: 700; cursor: pointer; transition: all 0.2s;">
                    Detalle ▾
                </button>
                <a href="{c['temario_url']}" style="display: block; margin-top: 4px; font-size: 0.72rem; color: var(--kinal-accent); font-weight: 700; text-decoration: none;">
                    Temario →
                </a>
            </td>
        </tr>
    """

# Generar tarjetas de auditoría compactas y plegables
collapsible_cards_html = ""
for c in courses_data:
    collapsible_cards_html += f"""
    <article class="audit-card compact-card" id="{c['cid']}" data-bimestre="{c['bimestre']}" data-linea="{c['linea']}" style="border: 1px solid var(--border-color); border-radius: 8px; margin-bottom: 12px; background: #ffffff; box-shadow: 0 1px 4px rgba(0,0,0,0.03);">
        <div class="audit-card-header compact-header" onclick="toggleCardDetail('{c['cid']}')" style="cursor: pointer; padding: 12px 18px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 10px; background: #f8fafc; border-bottom: 1px solid var(--border-light);">
            <div style="display: flex; align-items: center; gap: 10px; flex-wrap: wrap;">
                <span class="badge-bimestre" style="font-size: 0.72rem; padding: 2px 6px;">B{c['bimestre']}</span>
                <span class="badge-code" style="font-size: 0.72rem; padding: 2px 6px;">{c['code']}</span>
                <h3 style="font-size: 1rem; color: var(--kinal-blue); margin: 0; display: inline-flex; align-items: center; gap: 6px;">
                    {c['title']}
                </h3>
                <span style="font-size: 0.78rem; color: var(--text-muted); font-weight: 400;">— {c['sub']}</span>
            </div>
            <div style="display: flex; align-items: center; gap: 8px;">
                <a href="{c['temario_url']}" onclick="event.stopPropagation();" class="btn-card-temario" style="font-size: 0.75rem; color: var(--kinal-blue); font-weight: 700; background: #ffffff; border: 1px solid var(--border-color); padding: 4px 10px; border-radius: 5px; text-decoration: none;">
                    📚 Temario
                </a>
                <span class="toggle-indicator" id="ind-{c['cid']}" style="font-size: 0.75rem; font-weight: 700; color: #475569; background: #e2e8f0; padding: 4px 10px; border-radius: 5px;">
                    Ver Dictamen ▾
                </span>
            </div>
        </div>

        <div class="audit-body card-detail-body" id="body-{c['cid']}" style="display: none; padding: 18px 22px; border-top: 1px solid var(--border-color);">
            {c['body_html']}
        </div>
    </article>
    """

full_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Auditoría Curricular y Matriz de Dictamen (20 Cursos) | TSU Kinal 2026</title>
{base_styles}
    <style>
        /* ESTILOS ESPECÍFICOS PARA AUDITORÍA COMPACTA Y JERÁRQUICA */
        .subnav-auditorias {{
            background: #0f172a;
            padding: 12px 28px;
            border-bottom: 2px solid #334155;
            display: flex;
            align-items: center;
            justify-content: space-between;
            flex-wrap: wrap;
            gap: 12px;
        }}
        .subnav-badge {{
            background: #1e293b;
            color: #f59e0b;
            border: 1px solid #d97706;
            padding: 3px 10px;
            border-radius: 20px;
            font-size: 0.72rem;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        .subnav-label {{
            color: #cbd5e1;
            font-size: 0.84rem;
            font-weight: 600;
        }}
        .subnav-links {{
            display: flex;
            gap: 8px;
            flex-wrap: wrap;
        }}
        .subnav-btn {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            padding: 6px 14px;
            border-radius: 7px;
            font-size: 0.8rem;
            font-weight: 700;
            text-decoration: none;
            transition: all 0.2s;
            box-shadow: 0 2px 4px rgba(0,0,0,0.15);
        }}
        .subnav-btn-admon {{ background: #1e3a8a; color: #dbeafe; border: 1px solid #3b82f6; }}
        .subnav-btn-admon:hover {{ background: #2563eb; color: #ffffff; }}
        .subnav-btn-etica {{ background: #0c4a6e; color: #e0f2fe; border: 1px solid #0284c7; }}
        .subnav-btn-etica:hover {{ background: #0284c7; color: #ffffff; }}
        .subnav-btn-matematica {{ background: #064e3b; color: #d1fae5; border: 1px solid #10b981; }}
        .subnav-btn-matematica:hover {{ background: #059669; color: #ffffff; }}

        /* CONTROLES DE PESTAÑAS Y ACCIÓN RÁPIDA */
        .audit-tabs-bar {{
            background: #f8fafc;
            border: 1px solid var(--border-color);
            border-radius: 10px;
            padding: 14px 20px;
            margin-bottom: 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 12px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.02);
        }}
        .tab-btn-group {{
            display: flex;
            gap: 6px;
            flex-wrap: wrap;
        }}
        .audit-tab-btn {{
            background: #ffffff;
            border: 1px solid var(--border-color);
            padding: 7px 14px;
            border-radius: 6px;
            font-size: 0.82rem;
            font-weight: 700;
            color: var(--text-dark);
            cursor: pointer;
            transition: all 0.2s;
        }}
        .audit-tab-btn:hover {{
            background: #f1f5f9;
        }}
        .audit-tab-btn.active {{
            background: var(--kinal-blue);
            color: #ffffff;
            border-color: var(--kinal-blue);
        }}

        /* TABLA MATRIZ EJECUTIVA */
        .matrix-container {{
            background: #ffffff;
            border: 1px solid var(--border-color);
            border-radius: 10px;
            overflow-x: auto;
            margin-bottom: 28px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.03);
        }}
        .matrix-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 0.84rem;
        }}
        .matrix-table th {{
            background: #0f2d59;
            color: #ffffff;
            padding: 12px 14px;
            text-align: left;
            font-weight: 700;
            border-bottom: 2px solid var(--kinal-accent);
        }}
        .matrix-table td {{
            padding: 10px 14px;
            border-bottom: 1px solid var(--border-color);
            vertical-align: top;
        }}
        .matrix-row:hover {{
            background-color: #f8fafc;
        }}

        .compact-header:hover {{
            background: #f1f5f9 !important;
        }}
    </style>
</head>
<body>

<div class="app-container">

    <!-- HERO HEADER -->
    <header class="main-header">
        <div class="hero-top">
            <span class="badge-hero">Evaluación Curricular y Dictamen • 20 Asignaturas</span>
            <span class="badge-accent">DQR Nivel 6 • Sistema Dual</span>
        </div>
        <h1><span>⚖️</span> Auditoría Curricular y Matriz de Dictamen</h1>
        <p class="hero-subtitle">
            Diagnóstico formal comparativo del pensum: análisis sintético de contenidos anulados por obsolescencia, actualizaciones metodológicas a la Industria 4.0 y nuevas competencias técnicas incorporadas para el mando medio.
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
            <span class="subnav-badge">Auditorías Específicas Detalladas</span>
            <span class="subnav-label">Diagnósticos Quirúrgicos por Asignatura:</span>
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

        <!-- Barra de Pestañas Bimestrales y Filtros Rápidos -->
        <div class="audit-tabs-bar">
            <div style="display: flex; align-items: center; gap: 8px; flex-wrap: wrap;">
                <span style="font-weight: 800; font-size: 0.82rem; color: var(--kinal-blue); text-transform: uppercase;">Bimestre:</span>
                <div class="tab-btn-group">
                    <button class="audit-tab-btn active" onclick="switchBimestreTab('1', this)">Bimestre 1 (5)</button>
                    <button class="audit-tab-btn" onclick="switchBimestreTab('2', this)">Bimestre 2 (5)</button>
                    <button class="audit-tab-btn" onclick="switchBimestreTab('3', this)">Bimestre 3 (5)</button>
                    <button class="audit-tab-btn" onclick="switchBimestreTab('4', this)">Bimestre 4 (5)</button>
                    <button class="audit-tab-btn" onclick="switchBimestreTab('all', this)">Todos los Cursos (20)</button>
                </div>
            </div>

            <div style="display: flex; align-items: center; gap: 8px; flex-wrap: wrap;">
                <span style="font-weight: 800; font-size: 0.82rem; color: var(--kinal-blue); text-transform: uppercase;">Línea:</span>
                <select id="lineaSelect" onchange="filterByLineaSelect(this.value)" style="padding: 6px 12px; border-radius: 6px; border: 1px solid var(--border-color); font-size: 0.82rem; font-weight: 600; background: #ffffff;">
                    <option value="all">Todas las Líneas (20)</option>
                    <option value="linea-etica">🛡️ Formación Humana y Ética (4)</option>
                    <option value="linea-gestion">📋 Gestión y Supervisión (8)</option>
                    <option value="linea-matematica">📐 Ciencias Exactas y Analítica (4)</option>
                    <option value="linea-fisica">⚡ Física & Tecnología 4.0 (4)</option>
                </select>

                <button onclick="toggleAllCards(true)" style="background: #ffffff; border: 1px solid var(--border-color); padding: 6px 10px; border-radius: 6px; font-size: 0.78rem; font-weight: 700; cursor: pointer; color: var(--kinal-blue);">
                    ➕ Expandir Todo
                </button>
                <button onclick="toggleAllCards(false)" style="background: #ffffff; border: 1px solid var(--border-color); padding: 6px 10px; border-radius: 6px; font-size: 0.78rem; font-weight: 700; cursor: pointer; color: #64748b;">
                    ➖ Colapsar
                </button>
            </div>
        </div>

        <!-- 1. MATRIZ SINTÉTICA COMPARATIVA (TABLA EJECUTIVA) -->
        <div class="matrix-container">
            <table class="matrix-table">
                <thead>
                    <tr>
                        <th style="width: 10%;">Código</th>
                        <th style="width: 20%;">Asignatura y Eje</th>
                        <th style="width: 23%;">🔴 Lo que se Anula (Obsolescencia)</th>
                        <th style="width: 23%;">🟡 Lo que se Actualiza (Metodología)</th>
                        <th style="width: 24%;">🔵 Nuevas Competencias (Ind. 4.0)</th>
                        <th style="width: 10%; text-align: center;">Acciones</th>
                    </tr>
                </thead>
                <tbody>
                    {matrix_rows_html}
                </tbody>
            </table>
        </div>

        <!-- 2. FICHAS DETALLADAS PLEGABLES (ACORDEÓN COMPACTO) -->
        <div style="margin-bottom: 12px; display: flex; justify-content: space-between; align-items: center;">
            <h3 style="font-size: 1.1rem; color: var(--kinal-blue); font-weight: 800; display: flex; align-items: center; gap: 8px;">
                <span>📋</span> Fichas de Dictamen y Justificación Técnica por Asignatura
            </h3>
            <span style="font-size: 0.8rem; color: var(--text-muted);">Haz clic sobre cualquier tarjeta para ver su desglose completo</span>
        </div>

        <div class="collapsible-cards-container">
            {collapsible_cards_html}
        </div>

    </main>

    <footer style="background: #0b1f3a; color: #94a3b8; padding: 24px 40px; text-align: center; font-size: 0.85rem; border-top: 3px solid var(--kinal-accent);">
        <p><strong>Fundación Kinal</strong> • Dirección Académica / Coordinación TSU 2026 • Formación Dual DQR 6</p>
    </footer>

</div>

<script>
    let activeBimestre = '1';
    let activeLinea = 'all';

    function switchBimestreTab(bimestre, btn) {{
        activeBimestre = bimestre;
        document.querySelectorAll('.audit-tab-btn').forEach(b => b.classList.remove('active'));
        if (btn) btn.classList.add('active');
        applyFilters();
    }}

    function filterByLineaSelect(linea) {{
        activeLinea = linea;
        applyFilters();
    }}

    function applyFilters() {{
        // Filtrar filas de la matriz
        document.querySelectorAll('.matrix-row').forEach(row => {{
            const rowBim = row.getAttribute('data-bimestre');
            const rowLin = row.getAttribute('data-linea');

            const matchBim = (activeBimestre === 'all' || rowBim === activeBimestre);
            const matchLin = (activeLinea === 'all' || rowLin === activeLinea);

            row.style.display = (matchBim && matchLin) ? '' : 'none';
        }});

        // Filtrar tarjetas
        document.querySelectorAll('.compact-card').forEach(card => {{
            const cardBim = card.getAttribute('data-bimestre');
            const cardLin = card.getAttribute('data-linea');

            const matchBim = (activeBimestre === 'all' || cardBim === activeBimestre);
            const matchLin = (activeLinea === 'all' || cardLin === activeLinea);

            card.style.display = (matchBim && matchLin) ? 'block' : 'none';
        }});
    }}

    function toggleCardDetail(cid) {{
        const body = document.getElementById('body-' + cid);
        const ind = document.getElementById('ind-' + cid);
        if (!body) return;

        const isHidden = (body.style.display === 'none' || body.style.display === '');
        body.style.display = isHidden ? 'block' : 'none';
        if (ind) {{
            ind.innerText = isHidden ? 'Ocultar ▲' : 'Ver Dictamen ▾';
            ind.style.background = isHidden ? '#0f2d59' : '#e2e8f0';
            ind.style.color = isHidden ? '#ffffff' : '#475569';
        }}

        // Si se abrió desde la tabla, hacer scroll suave a la tarjeta
        if (isHidden) {{
            const card = document.getElementById(cid);
            if (card) card.scrollIntoView({{ behavior: 'smooth', block: 'nearest' }});
        }}
    }}

    function toggleAllCards(expand) {{
        document.querySelectorAll('.card-detail-body').forEach(b => {{
            b.style.display = expand ? 'block' : 'none';
        }});
        document.querySelectorAll('.toggle-indicator').forEach(ind => {{
            ind.innerText = expand ? 'Ocultar ▲' : 'Ver Dictamen ▾';
            ind.style.background = expand ? '#0f2d59' : '#e2e8f0';
            ind.style.color = expand ? '#ffffff' : '#475569';
        }});
    }}

    // Inicializar mostrando Bimestre 1
    document.addEventListener('DOMContentLoaded', () => {{
        applyFilters();
    }});
</script>

</body>
</html>
"""

with open(AUDITORIA_PATH, "w", encoding="utf-8") as f:
    f.write(full_html)

print(f"Generado {AUDITORIA_PATH} ({len(full_html)} bytes) de forma concisa y modular.")
