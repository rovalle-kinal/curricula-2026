#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
unify_tsu_portal.py
Unifica toda la revisión curricular del TSU, distribución temática, temarios por línea,
mapa curricular (rejilla + grafo SVG) y dictamen de auditoría en una sola landing page completa:
TSU/index.html.
Mueve todas las páginas individuales y anteriores a la carpeta TSU/historico/.
"""

import os
import shutil
import json
import re

base_dir = "/Users/arqovalle/Library/CloudStorage/OneDrive-Personal/Software/Antigravity/Diseño Instruccional/TSU"
mybrain_dir = "/Users/arqovalle/Library/CloudStorage/OneDrive-Personal/MyBrain/MyBrain/01 - My Brain/Kinal/TSU"
historico_dir = os.path.join(base_dir, "historico")
mybrain_historico_dir = os.path.join(mybrain_dir, "historico")

os.makedirs(historico_dir, exist_ok=True)
os.makedirs(mybrain_historico_dir, exist_ok=True)

# 1. Cargar datos de build_tsu_subpages.py
import build_tsu_subpages
cursos_subpages = build_tsu_subpages.cursos_data
lineas_estudio = build_tsu_subpages.lineas_estudio

# 2. Cargar datos de auditoría de generate_tsu_all_courses.py
import generate_tsu_all_courses
audit_by_id = {c["id"]: c for c in generate_tsu_all_courses.courses}

# 3. Fusionar datos completos en una sola estructura unificada
unified_courses = {}
for cid, c in cursos_subpages.items():
    audit = audit_by_id.get(cid, {})
    unified_courses[cid] = {
        **c,
        "actual": audit.get("actual", "Contenido tradicional del pensum anterior."),
        "anular": audit.get("anular", "Contenidos teóricos o abstractos sin aplicación técnica."),
        "actualizar": audit.get("actualizar", "Modernización con normas y herramientas vigentes."),
        "nuevo": audit.get("nuevo", "Competencias emergentes demandadas por la industria guatemalteca 2026."),
        "justificacion": audit.get("justificacion", "Requerimiento de la industria guatemalteca (CIG / AGEXPORT) para mandos medios.")
    }

print(f"Total cursos consolidados: {len(unified_courses)}")

# -------------------------------------------------------------
# CONSTRUCCIÓN DE COMPONENTES HTML DE LA LANDING PAGE MAESTRA
# -------------------------------------------------------------

# Especialidades Técnicas de Kinal
especialidades = [
    {
        "nombre": "Construcción",
        "icono": "🏗️",
        "enfoque": "Supervisión de obra civil, cubicajes y presupuestos, control de calidad en probetas de concreto y acero, seguridad en andamios (SSO) y liderazgo de cuadrillas."
    },
    {
        "nombre": "Desarrollo de Aplicaciones Empresariales",
        "icono": "💻",
        "enfoque": "Liderazgo de proyectos ágiles de software (Scrum/Kanban), estimación de costos en la nube, calidad de código con linters de IA, SLAs del 99.9% y automatización con Python."
    },
    {
        "nombre": "Electricidad Industrial",
        "icono": "⚡",
        "enfoque": "Subestaciones, pliegos tarifarios industriales (EEGSA/ENERGUATE), corrección del factor de potencia, protocolos de bloqueo LOTO y balances de carga energética."
    },
    {
        "nombre": "Electrónica Industrial",
        "icono": "🔌",
        "enfoque": "Instrumentación y sensores de planta (4-20 mA), acondicionamiento de señales, interbloqueos de seguridad booleana, disipación térmica y adquisición de datos con Python."
    },
    {
        "nombre": "Mecánica Automotriz",
        "icono": "🚗",
        "enfoque": "Gestión de talleres y bahías de servicio, diagnóstico electrónico OBD-II, torque y metrología dimensional, costeo de órdenes de trabajo (OT) y contratos de flotas corporativas."
    },
    {
        "nombre": "Mecánica Industrial",
        "icono": "⚙️",
        "enfoque": "Mantenimiento electromecánico y paradas de planta, cálculo de Downtime Cost, manufactura esbelta 5S y SMED, resistencia y fatiga de materiales y maquinado CNC."
    },
    {
        "nombre": "Telecomunicaciones",
        "icono": "📡",
        "enfoque": "Tendido de fibra óptica y radiobases con respaldo solar, cumplimiento de SLAs de disponibilidad de red, izaje seguro de racks y ciberseguridad física."
    }
]

especialidades_cards_html = ""
for esp in especialidades:
    especialidades_cards_html += f"""
    <div class="spec-card">
        <span class="spec-icon">{esp["icono"]}</span>
        <div class="spec-content">
            <h4>{esp["nombre"]}</h4>
            <p>{esp["enfoque"]}</p>
        </div>
    </div>
    """

# -------------------------------------------------------------
# SECCIÓN 2: REJILLA CURRICULAR Y RED SVG
# -------------------------------------------------------------
grid_rows_html = ""
for linea in lineas_estudio:
    cursos_linea = [unified_courses[cid] for cid in linea["cursos_ids"]]
    b_cols = {1: [], 2: [], 3: [], 4: []}
    for c in cursos_linea:
        b_cols[c["bimestre_num"]].append(c)

    cols_html = ""
    for b_num in range(1, 5):
        c_list = b_cols[b_num]
        cards_in_col = ""
        for c in c_list:
            prereqs_str = ",".join(c["prerequisitos"])
            habilita_str = ",".join(c["habilita"])
            
            cards_in_col += f"""
            <div class="node-card" id="node-{c["id"]}" 
                 data-id="{c["id"]}" 
                 data-codigo="{c["codigo"]}"
                 data-linea="{c["linea_id"]}"
                 data-prereq="{prereqs_str}" 
                 data-habilita="{habilita_str}"
                 onclick="selectCourseNode('{c["id"]}')"
                 onmouseenter="highlightNodeRuta('{c["id"]}')"
                 onmouseleave="clearHighlightNode()">
                <div class="node-badge-row">
                    <span class="node-code">{c["codigo"]}</span>
                    <span class="node-period">{c["periodo"].split()[0]} {c["periodo"].split()[1]}</span>
                </div>
                <div class="node-title">
                    <span class="node-icon">{c["icono"]}</span>
                    <strong>{c["nombre"]}</strong>
                </div>
                <div class="node-sub">{c["subtitulo"]}</div>
                <div class="node-conn-summary">
                    <span class="conn-count in" title="Prerrequisitos previos">⬅️ {len(c["prerequisitos"])}</span>
                    <span class="conn-count out" title="Cursos que desbloquea">➡️ {len(c["habilita"])}</span>
                </div>
            </div>
            """
        cols_html += f"""
        <div class="grid-cell bimestre-col-{b_num}">
            {cards_in_col}
        </div>
        """

    grid_rows_html += f"""
    <div class="grid-linea-row" id="row-{linea["id"]}">
        <div class="grid-linea-label" style="border-left-color: {linea["color_accent"]};">
            <span class="linea-row-icon">{linea["icono"]}</span>
            <div>
                <strong>{linea["nombre"]}</strong>
                <div class="linea-row-sub">{len(cursos_linea)} Asignaturas • {len(cursos_linea)*13.5} hrs</div>
            </div>
        </div>
        <div class="grid-linea-cols">
            {cols_html}
        </div>
    </div>
    """

# Coordenadas Grafo SVG
col_x = {1: 125, 2: 375, 3: 625, 4: 875}
row_y = {
    "b1_etica_general_1": 80,
    "b1_fundamentos_administracion": 200,
    "b1_planeacion_control_trabajo": 320,
    "b1_matematica_basica_1": 450,
    "b1_fisica_basica_1": 580,
    "b2_etica_general_2": 80,
    "b2_herramientas_contables": 200,
    "b2_administracion_rrhh_sso": 320,
    "b2_matematica_basica_2": 450,
    "b2_fisica_aplicada_1": 580,
    "b3_etica_profesional_1": 80,
    "b3_metodos_produccion": 200,
    "b3_servicio_cliente": 320,
    "b3_matematica_aplicada_1": 450,
    "b3_fisica_aplicada_2": 580,
    "b4_etica_profesional_2": 80,
    "b4_control_calidad": 200,
    "b4_fundamentos_marketing": 320,
    "b4_matematica_aplicada_2": 450,
    "b4_fisica_aplicada_3": 580,
}

linea_color_map = {
    "linea-etica": "#0284c7",
    "linea-gestion": "#d97706",
    "linea-matematica": "#16a34a",
    "linea-fisica": "#7c3aed"
}

node_w = 170
node_h = 60

svg_edges_html = ""
for cid, c in unified_courses.items():
    x1 = col_x[c["bimestre_num"]] + (node_w / 2)
    y1 = row_y[cid]
    linea_id = c["linea_id"]
    base_color = linea_color_map[linea_id]

    for h_id in c["habilita"]:
        if h_id in unified_courses:
            target = unified_courses[h_id]
            x2 = col_x[target["bimestre_num"]] - (node_w / 2)
            y2 = row_y[h_id]

            dx = x2 - x1
            cx1 = x1 + dx * 0.45
            cx2 = x2 - dx * 0.45

            edge_id = f"svg-edge-{cid}-{h_id}"
            is_cross = (c["linea_id"] != target["linea_id"])
            dash_attr = 'stroke-dasharray="4 3"' if is_cross else ''

            svg_edges_html += f"""
            <path id="{edge_id}" 
                  class="svg-edge edge-source-{cid} edge-target-{h_id} edge-linea-{linea_id}"
                  data-source="{cid}" data-target="{h_id}"
                  d="M {x1} {y1} C {cx1} {y1}, {cx2} {y2}, {x2} {y2}" 
                  fill="none" 
                  stroke="{base_color}" 
                  stroke-width="2.2" 
                  stroke-opacity="0.65"
                  {dash_attr}
                  marker-end="url(#marker-{linea_id})" />
            """

svg_nodes_html = ""
for cid, c in unified_courses.items():
    cx = col_x[c["bimestre_num"]]
    cy = row_y[cid]
    rx = cx - (node_w / 2)
    ry = cy - (node_h / 2)
    color = linea_color_map[c["linea_id"]]

    svg_nodes_html += f"""
    <g id="svg-node-{cid}" class="svg-node-group" data-id="{cid}" data-linea="{c["linea_id"]}"
       onclick="selectCourseNode('{cid}')" 
       onmouseenter="highlightNodeRuta('{cid}')" 
       onmouseleave="clearHighlightNode()"
       style="cursor: pointer;">
        <rect id="svg-rect-{cid}" class="svg-node-rect" 
              x="{rx}" y="{ry}" width="{node_w}" height="{node_h}" rx="8" ry="8"
              fill="#ffffff" stroke="{color}" stroke-width="2" />
        
        <path d="M {rx} {ry+8} A 8 8 0 0 1 {rx+8} {ry} L {rx+10} {ry} L {rx+10} {ry+node_h} L {rx+8} {ry+node_h} A 8 8 0 0 1 {rx} {ry+node_h-8} Z" fill="{color}" />

        <text x="{rx + 18}" y="{ry + 18}" font-size="10" font-weight="800" fill="#475569">{c["codigo"]}</text>
        <text x="{rx + node_w - 12}" y="{ry + 18}" text-anchor="end" font-size="9" font-weight="600" fill="#94a3b8">{c["periodo"].split()[0]} {c["periodo"].split()[1]}</text>

        <text x="{rx + 18}" y="{ry + 36}" font-size="11.5" font-weight="700" fill="#0f2d59">{c["icono"]} {c["nombre"]}</text>
        <text x="{rx + 18}" y="{ry + 50}" font-size="8.5" fill="#64748b">{c["subtitulo"][:26]}...</text>
    </g>
    """

# -------------------------------------------------------------
# SECCIÓN 3: TEMARIOS POR LÍNEA DE ESTUDIO
# -------------------------------------------------------------
temarios_lineas_html = ""
for linea in lineas_estudio:
    cursos_en_linea = [unified_courses[cid] for cid in linea["cursos_ids"]]
    total_cursos = len(cursos_en_linea)
    total_horas = total_cursos * 13.5
    
    cards_html = ""
    for c in cursos_en_linea:
        unidades_html = ""
        for u in c["unidades"]:
            temas_li = "".join([f"<li>{t}</li>" for t in u["temas"]])
            unidades_html += f"""
            <div class="unidad-box">
                <div class="unidad-title">
                    <span class="unidad-badge">{u["num"]}</span>
                    <h4>{u["titulo"]}</h4>
                </div>
                <ul class="unidad-temas">
                    {temas_li}
                </ul>
            </div>
            """

        prereq_badges = ""
        if c["prerequisitos"]:
            prereq_badges = " ".join([f'<a href="#temario-{pr}" class="conn-pill prereq-pill">{unified_courses[pr]["codigo"]} • {unified_courses[pr]["nombre"]}</a>' for pr in c["prerequisitos"]])
        else:
            prereq_badges = '<span class="conn-pill no-prereq">Ingreso TSU (Sin prerrequisito previo de 3er año)</span>'

        habilita_badges = ""
        if c["habilita"]:
            habilita_badges = " ".join([f'<a href="#temario-{hb}" class="conn-pill habilita-pill">{unified_courses[hb]["codigo"]} • {unified_courses[hb]["nombre"]}</a>' for hb in c["habilita"]])
        else:
            habilita_badges = '<span class="conn-pill final-curso">Culminación del Plan / Graduación TSU</span>'

        cards_html += f"""
        <article class="temario-card" id="temario-{c["id"]}" data-bimestre="{c["bimestre_num"]}" data-linea="{linea["id"]}">
            <div class="temario-header">
                <div class="temario-meta">
                    <span class="badge-bimestre">{c["bimestre"]}</span>
                    <span class="badge-periodo">{c["periodo"]}</span>
                    <span class="badge-code">{c["codigo"]}</span>
                    <span class="badge-horas">⏱️ {c["horas"]}</span>
                </div>
                <div class="temario-title-bar">
                    <h3><span>{c["icono"]}</span> {c["nombre"]}</h3>
                    <a href="#audit-{c["id"]}" class="btn-auditoria-link" onclick="scrollToAudit('{c["id"]}')">Ver Dictamen y Auditoría ↓</a>
                </div>
                <div class="temario-subtitulo">{c["subtitulo"]}</div>
            </div>

            <div class="temario-body">
                <div class="temario-callout">
                    <strong>🎯 Objetivo Curricular Transversal:</strong> {c["objetivo_transversal"]}
                </div>

                <div class="correlatividades-box">
                    <div class="corr-item">
                        <span class="corr-label">⬅️ Prerrequisito Requerido:</span>
                        <div class="corr-links">{prereq_badges}</div>
                    </div>
                    <div class="corr-item">
                        <span class="corr-label">➡️ Habilita a / Da Paso a:</span>
                        <div class="corr-links">{habilita_badges}</div>
                    </div>
                </div>

                <div class="unidades-container">
                    <div class="unidades-header">
                        <h5>📖 Contenido y Unidades Temáticas Modernizadas (Pensum 2026)</h5>
                        <button class="btn-toggle-unidades" onclick="toggleUnidades('{c["id"]}')">Desplegar / Ocultar Temas</button>
                    </div>
                    <div class="unidades-content" id="unidades-{c["id"]}">
                        {unidades_html}
                    </div>
                </div>

                <div class="ia-box">
                    <div class="ia-header">
                        <span class="ia-badge">🤖 Subtema de Inteligencia Artificial (IA)</span>
                    </div>
                    <p>{c["subtema_ia"]}</p>
                </div>

                <div class="temario-footer-grid">
                    <div class="footer-block">
                        <strong>🛠️ Herramientas, Software y Normas Aplicadas:</strong>
                        <p>{c["herramientas"]}</p>
                    </div>
                    <div class="footer-block">
                        <strong>🏗️ Aplicabilidad a las 7 Especialidades de Kinal:</strong>
                        <p>{c["aplicabilidad_7"]}</p>
                    </div>
                </div>
            </div>
        </article>
        """

    temarios_lineas_html += f"""
    <section class="linea-section" id="{linea["id"]}">
        <div class="linea-header" style="border-left-color: {linea["color_accent"]};">
            <div class="linea-header-info">
                <span class="linea-badge" style="background: {linea["color_bg"]}; color: {linea["color_accent"]}; border-color: {linea["color_border"]};">
                    Línea de Estudio Especializada
                </span>
                <h2><span>{linea["icono"]}</span> {linea["nombre"]}</h2>
                <p class="linea-desc">{linea["descripcion"]}</p>
            </div>
            <div class="linea-stats">
                <div class="stat-pill"><strong>{total_cursos}</strong> Cursos</div>
                <div class="stat-pill"><strong>{total_horas}</strong> Horas</div>
                <div class="stat-pill"><strong>B1 a B4</strong></div>
            </div>
        </div>
        
        <div class="linea-courses-list">
            {cards_html}
        </div>
    </section>
    """

# -------------------------------------------------------------
# SECCIÓN 4: AUDITORÍA Y MATRIZ DE DICTAMEN (ANULAR / ACTUALIZAR / NUEVO)
# -------------------------------------------------------------
audit_cards_html = ""
for cid, c in unified_courses.items():
    audit_cards_html += f"""
    <article class="audit-card" id="audit-{c["id"]}" data-bimestre="{c["bimestre_num"]}" data-linea="{c["linea_id"]}">
        <div class="audit-card-header">
            <div class="audit-meta">
                <span class="badge-bimestre">{c["bimestre"]}</span>
                <span class="badge-code">{c["codigo"]}</span>
                <span class="badge-eje">{c["eje"]}</span>
            </div>
            <h3><span>{c["icono"]}</span> {c["nombre"]}</h3>
            <div class="audit-sub">{c["subtitulo"]}</div>
        </div>

        <div class="audit-body">
            <table class="audit-table">
                <thead>
                    <tr>
                        <th style="width: 25%;">Dimensión</th>
                        <th style="width: 15%;">Dictamen</th>
                        <th style="width: 60%;">Contenido y Diagnóstico</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>Contenido Original (Pensum Previo)</strong></td>
                        <td><span class="tag-pill tag-original">Original</span></td>
                        <td>{c["actual"]}</td>
                    </tr>
                    <tr class="row-anular">
                        <td><strong>Lo que se Anula</strong></td>
                        <td><span class="tag-pill tag-anular">Anular</span></td>
                        <td>
                            <div class="audit-callout callout-red">
                                <strong>Motivo de anulación:</strong> {c["anular"]}
                            </div>
                        </td>
                    </tr>
                    <tr class="row-actualizar">
                        <td><strong>Contenidos a Actualizar</strong></td>
                        <td><span class="tag-pill tag-actualizar">Actualizar</span></td>
                        <td>
                            <div class="audit-callout callout-yellow">
                                <strong>Modernización:</strong> {c["actualizar"]}
                            </div>
                        </td>
                    </tr>
                    <tr class="row-nuevo">
                        <td><strong>Nuevos Conocimientos</strong></td>
                        <td><span class="tag-pill tag-nuevo">Nuevo</span></td>
                        <td>
                            <div class="audit-callout callout-blue">
                                <strong>Innovación 2026:</strong> {c["nuevo"]}
                            </div>
                        </td>
                    </tr>
                </tbody>
            </table>

            <div class="audit-justificacion">
                <strong>📈 Justificación y Demanda del Mercado Guatemalteco (CIG / AGEXPORT):</strong>
                <p>{c["justificacion"]}</p>
            </div>

            <div class="audit-actions">
                <a href="#temario-{c["id"]}" class="btn-goto-temario">Ver Temario Completo y Unidades ↑</a>
            </div>
        </div>
    </article>
    """

# -------------------------------------------------------------
# SECCIÓN 5: VISTA OPERATIVA POR BIMESTRES
# -------------------------------------------------------------
bimestres_blocks_html = ""
for b_num in range(1, 5):
    b_cursos = [c for c in unified_courses.values() if c["bimestre_num"] == b_num]
    
    b_cards = ""
    for c in b_cursos:
        b_cards += f"""
        <div class="bimestre-course-card">
            <div class="b-period">{c["periodo"]}</div>
            <div class="b-code">{c["codigo"]}</div>
            <h4><span>{c["icono"]}</span> {c["nombre"]}</h4>
            <div class="b-eje">{c["eje"]}</div>
            <p class="b-sub">{c["subtitulo"]}</p>
            <div class="b-links">
                <a href="#node-{c["id"]}" onclick="selectCourseNode('{c["id"]}'); scrollToMap();">Ver en Mapa</a> • 
                <a href="#temario-{c["id"]}">Ver Temario</a>
            </div>
        </div>
        """

    bimestres_blocks_html += f"""
    <div class="bimestre-group" id="bimestre-bloque-{b_num}">
        <div class="bimestre-group-header">
            <h3>Bimestre {b_num}</h3>
            <span>5 Asignaturas Obligatorias (50 min c/u) • 67.5 Horas Lectivas</span>
        </div>
        <div class="bimestre-grid">
            {b_cards}
        </div>
    </div>
    """

# Construir JSON para interactividad JS
relaciones_json = {}
for cid, c in unified_courses.items():
    relaciones_json[cid] = {
        "id": c["id"],
        "codigo": c["codigo"],
        "nombre": c["nombre"],
        "subtitulo": c["subtitulo"],
        "bimestre": c["bimestre"],
        "periodo": c["periodo"],
        "linea_id": c["linea_id"],
        "eje": c["eje"],
        "icono": c["icono"],
        "horas": c["horas"],
        "prerequisitos": c["prerequisitos"],
        "habilita": c["habilita"],
        "objetivo": c["objetivo_transversal"],
        "subtema_ia": c["subtema_ia"],
        "herramientas": c["herramientas"]
    }
relaciones_str = json.dumps(relaciones_json, ensure_ascii=False)

# -------------------------------------------------------------
# PLANTILLA HTML MAESTRA COMPLETA
# -------------------------------------------------------------
master_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portal Curricular Integral TSU 2026 | Fundación Kinal</title>
    <style>
        :root {{
            --kinal-blue: #0f2d59;
            --kinal-blue-dark: #0b1f3a;
            --kinal-blue-light: #1e3a8a;
            --kinal-accent: #d97706;
            --kinal-accent-light: #fef3c7;
            --kinal-light: #f8fafc;
            --text-dark: #1e293b;
            --text-muted: #64748b;
            --border-color: #cbd5e1;
            --border-light: #e2e8f0;
            --color-actualizar-bg: #fef9c3;
            --color-actualizar-text: #854d0e;
            --color-actualizar-border: #facc15;
            --color-anular-bg: #fee2e2;
            --color-anular-text: #991b1b;
            --color-anular-border: #f87171;
            --color-nuevo-bg: #dbeafe;
            --color-nuevo-text: #1e40af;
            --color-nuevo-border: #60a5fa;
            --color-ia: #6366f1;
            --color-ia-bg: #eef2ff;
            /* Rutas */
            --color-node-selected: #0f2d59;
            --color-node-prereq: #059669;
            --color-node-habilita: #d97706;
        }}

        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        html {{ scroll-behavior: smooth; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background-color: #f1f5f9;
            color: var(--text-dark);
            line-height: 1.6;
            padding: 20px;
        }}
        .app-container {{
            max-width: 1440px;
            margin: 0 auto;
            background: #ffffff;
            border-radius: 12px;
            box-shadow: 0 4px 24px rgba(0,0,0,0.08);
            overflow: hidden;
            border: 1px solid var(--border-color);
        }}

        /* HERO HEADER */
        header.main-header {{
            background: linear-gradient(135deg, var(--kinal-blue-dark) 0%, var(--kinal-blue) 50%, #1e3a8a 100%);
            color: #ffffff;
            padding: 40px 48px;
            border-bottom: 5px solid var(--kinal-accent);
            position: relative;
        }}
        .header-top-badges {{
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
            margin-bottom: 14px;
        }}
        .badge-pill {{
            background: rgba(217, 119, 6, 0.25);
            color: #fef08a;
            border: 1px solid var(--kinal-accent);
            padding: 4px 14px;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        .badge-pill-alt {{
            background: rgba(255, 255, 255, 0.12);
            color: #ffffff;
            border: 1px solid rgba(255,255,255,0.25);
            padding: 4px 14px;
            border-radius: 20px;
            font-size: 0.8rem;
            font-weight: 600;
        }}
        header.main-header h1 {{
            font-size: 2.3rem;
            font-weight: 800;
            line-height: 1.2;
            margin-bottom: 10px;
            letter-spacing: -0.5px;
        }}
        header.main-header p {{
            color: #cbd5e1;
            font-size: 1.05rem;
            max-width: 1050px;
            line-height: 1.55;
            margin-bottom: 20px;
        }}
        .header-stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 12px;
            margin-top: 10px;
        }}
        .stat-card {{
            background: rgba(255,255,255,0.08);
            border: 1px solid rgba(255,255,255,0.18);
            padding: 12px 16px;
            border-radius: 8px;
            backdrop-filter: blur(4px);
        }}
        .stat-card strong {{
            display: block;
            font-size: 1.4rem;
            color: #fef08a;
            font-weight: 800;
            line-height: 1;
            margin-bottom: 4px;
        }}
        .stat-card span {{
            font-size: 0.82rem;
            color: #e2e8f0;
        }}

        /* STICKY UNIFIED NAVBAR */
        nav.sticky-nav {{
            position: sticky;
            top: 0;
            z-index: 1000;
            background: var(--kinal-blue-dark);
            padding: 0 40px;
            display: flex;
            gap: 8px;
            overflow-x: auto;
            border-bottom: 1px solid rgba(255,255,255,0.12);
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        }}
        nav.sticky-nav a {{
            color: #94a3b8;
            text-decoration: none;
            padding: 16px 18px;
            font-weight: 600;
            font-size: 0.92rem;
            display: inline-flex;
            align-items: center;
            gap: 8px;
            border-bottom: 3px solid transparent;
            transition: all 0.2s;
            white-space: nowrap;
        }}
        nav.sticky-nav a:hover {{
            color: #ffffff;
            border-bottom-color: var(--kinal-accent);
        }}
        nav.sticky-nav a.active {{
            color: #ffffff;
            background: rgba(255,255,255,0.08);
            border-bottom-color: var(--kinal-accent);
        }}

        main.main-content {{
            padding: 40px 48px;
        }}

        /* SECCIONES */
        section.portal-section {{
            margin-bottom: 56px;
            scroll-margin-top: 80px;
        }}
        .section-header-bar {{
            padding-bottom: 14px;
            border-bottom: 2px solid var(--border-light);
            margin-bottom: 28px;
            display: flex;
            justify-content: space-between;
            align-items: flex-end;
            flex-wrap: wrap;
            gap: 12px;
        }}
        .section-title-group h2 {{
            font-size: 1.7rem;
            color: var(--kinal-blue);
            font-weight: 800;
            display: flex;
            align-items: center;
            gap: 12px;
        }}
        .section-title-group p {{
            color: var(--text-muted);
            font-size: 0.96rem;
            margin-top: 4px;
        }}

        /* ESPECIALIDADES GRID */
        .specs-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 16px;
            margin-bottom: 32px;
        }}
        .spec-card {{
            background: #f8fafc;
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 18px;
            display: flex;
            align-items: flex-start;
            gap: 14px;
            transition: transform 0.2s, box-shadow 0.2s;
        }}
        .spec-card:hover {{
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.05);
            border-color: var(--kinal-blue);
        }}
        .spec-icon {{ font-size: 2rem; line-height: 1; }}
        .spec-content h4 {{
            font-size: 1rem;
            color: var(--kinal-blue);
            font-weight: 700;
            margin-bottom: 4px;
        }}
        .spec-content p {{
            font-size: 0.85rem;
            color: var(--text-dark);
            line-height: 1.45;
        }}

        .callout-gold {{
            background: #fffbeb;
            border-left: 4px solid var(--kinal-accent);
            padding: 20px 24px;
            border-radius: 0 8px 8px 0;
            margin-bottom: 30px;
        }}
        .callout-gold h4 {{ color: #92400e; font-size: 1.05rem; margin-bottom: 6px; }}
        .callout-gold p {{ color: #78350f; font-size: 0.92rem; line-height: 1.5; }}

        /* MAPA CURRICULAR Y RED SVG */
        .map-instructions {{
            background: #f8fafc;
            border: 1px solid var(--border-color);
            border-left: 4px solid var(--kinal-blue);
            padding: 18px 24px;
            border-radius: 0 8px 8px 0;
            margin-bottom: 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 16px;
        }}
        .legend-bar {{
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
            background: #ffffff;
            padding: 8px 14px;
            border-radius: 6px;
            border: 1px solid var(--border-color);
            font-size: 0.82rem;
        }}
        .legend-chip {{
            display: flex;
            align-items: center;
            gap: 6px;
            font-weight: 600;
        }}
        .chip-dot {{ width: 12px; height: 12px; border-radius: 3px; }}
        .chip-selected {{ background: var(--color-node-selected); }}
        .chip-prereq {{ background: var(--color-node-prereq); }}
        .chip-habilita {{ background: var(--color-node-habilita); }}

        .view-controls {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 14px;
            background: #f8fafc;
            border: 1px solid var(--border-color);
            padding: 12px 20px;
            border-radius: 8px;
            margin-bottom: 20px;
        }}
        .mode-buttons {{ display: flex; gap: 8px; }}
        .mode-btn {{
            background: #ffffff;
            border: 1px solid var(--border-color);
            padding: 8px 16px;
            border-radius: 6px;
            font-size: 0.88rem;
            font-weight: 700;
            color: var(--text-dark);
            cursor: pointer;
            transition: all 0.2s;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .mode-btn.active {{
            background: var(--kinal-blue);
            color: #ffffff;
            border-color: var(--kinal-blue);
        }}
        .filter-linea-select select {{
            padding: 6px 12px;
            border-radius: 6px;
            border: 1px solid var(--border-color);
            font-size: 0.88rem;
            outline: none;
            background: #ffffff;
        }}

        .map-layout {{
            display: grid;
            grid-template-columns: 1fr 280px;
            gap: 16px;
            align-items: start;
        }}
        .curriculum-grid-container {{
            background: #ffffff;
            border: 1px solid var(--border-color);
            border-radius: 10px;
            overflow-x: auto;
            box-shadow: 0 2px 8px rgba(0,0,0,0.03);
        }}
        .grid-header-row {{
            display: grid;
            grid-template-columns: 150px repeat(4, minmax(135px, 1fr));
            background: var(--kinal-blue-dark);
            color: #ffffff;
            font-weight: 700;
            font-size: 0.82rem;
            border-bottom: 2px solid var(--kinal-accent);
        }}
        .grid-header-cell {{
            padding: 10px 8px;
            text-align: center;
            border-right: 1px solid rgba(255,255,255,0.1);
            font-size: 0.82rem;
            line-height: 1.25;
        }}
        .grid-header-cell:first-child {{ text-align: left; }}
        .grid-header-cell:last-child {{ border-right: none; }}

        .grid-linea-row {{
            display: grid;
            grid-template-columns: 150px 1fr;
            border-bottom: 1px solid var(--border-color);
        }}
        .grid-linea-row:last-child {{ border-bottom: none; }}

        .grid-linea-label {{
            background: #f8fafc;
            border-right: 1px solid var(--border-color);
            border-left: 4px solid var(--kinal-blue);
            padding: 12px 10px;
            display: flex;
            align-items: flex-start;
            gap: 8px;
        }}
        .linea-row-icon {{ font-size: 1.25rem; line-height: 1; flex-shrink: 0; margin-top: 2px; }}
        .grid-linea-label strong {{
            font-size: 0.78rem;
            color: var(--kinal-blue);
            line-height: 1.25;
            display: block;
        }}
        .linea-row-sub {{ font-size: 0.70rem; color: var(--text-muted); margin-top: 3px; line-height: 1.2; }}

        .grid-linea-cols {{
            display: grid;
            grid-template-columns: repeat(4, minmax(135px, 1fr));
        }}
        .grid-cell {{
            padding: 8px;
            border-right: 1px solid var(--border-color);
            display: flex;
            flex-direction: column;
            gap: 8px;
            background: #fafbfc;
        }}
        .grid-cell:last-child {{ border-right: none; }}

        .node-card {{
            background: #ffffff;
            border: 1.5px solid var(--border-color);
            border-radius: 6px;
            padding: 8px 8px;
            cursor: pointer;
            transition: all 0.2s;
            position: relative;
        }}
        .node-card:hover {{
            transform: translateY(-1px);
            border-color: var(--kinal-blue);
            box-shadow: 0 3px 8px rgba(0,0,0,0.08);
        }}
        .node-badge-row {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 4px;
        }}
        .node-code {{
            background: #e2e8f0;
            color: #1e293b;
            font-weight: 800;
            font-size: 0.65rem;
            padding: 1px 5px;
            border-radius: 3px;
        }}
        .node-period {{ font-size: 0.65rem; color: var(--text-muted); font-weight: 600; }}
        .node-title {{
            display: flex;
            align-items: flex-start;
            gap: 4px;
            margin-bottom: 3px;
        }}
        .node-icon {{ font-size: 0.85rem; line-height: 1.2; flex-shrink: 0; }}
        .node-title strong {{
            font-size: 0.76rem;
            color: var(--kinal-blue);
            line-height: 1.2;
        }}
        .node-sub {{
            font-size: 0.68rem;
            color: var(--text-muted);
            line-height: 1.2;
            margin-bottom: 5px;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }}
        .node-conn-summary {{
            display: flex;
            gap: 6px;
            font-size: 0.64rem;
            border-top: 1px solid var(--border-light);
            padding-top: 4px;
        }}
        .conn-count {{ padding: 1px 4px; border-radius: 3px; font-weight: 700; }}
        .conn-count.in {{ background: #ecfdf5; color: #065f46; }}
        .conn-count.out {{ background: #fffbeb; color: #92400e; }}

        .node-card.selected {{
            border-color: var(--color-node-selected) !important;
            background: #eff6ff !important;
            box-shadow: 0 0 0 3px rgba(15, 45, 89, 0.3) !important;
            transform: scale(1.02);
            z-index: 10;
        }}
        .node-card.prereq-active {{
            border-color: var(--color-node-prereq) !important;
            background: #ecfdf5 !important;
            box-shadow: 0 0 0 2px rgba(5, 150, 105, 0.4) !important;
        }}
        .node-card.prereq-active::after {{
            content: "⬅️ PRERREQUISITO";
            position: absolute;
            top: -9px;
            right: 8px;
            background: var(--color-node-prereq);
            color: #ffffff;
            font-size: 0.62rem;
            font-weight: 800;
            padding: 1px 5px;
            border-radius: 3px;
        }}
        .node-card.habilita-active {{
            border-color: var(--color-node-habilita) !important;
            background: #fffbeb !important;
            box-shadow: 0 0 0 2px rgba(217, 119, 6, 0.4) !important;
        }}
        .node-card.habilita-active::after {{
            content: "➡️ HABILITA A";
            position: absolute;
            top: -9px;
            right: 8px;
            background: var(--color-node-habilita);
            color: #ffffff;
            font-size: 0.62rem;
            font-weight: 800;
            padding: 1px 5px;
            border-radius: 3px;
        }}
        .node-card.dimmed {{ opacity: 0.32; filter: grayscale(40%); }}

        /* RED SVG */
        .network-svg-container {{
            display: none;
            background: #ffffff;
            border: 1px solid var(--border-color);
            border-radius: 10px;
            padding: 20px;
            overflow-x: auto;
            box-shadow: 0 2px 8px rgba(0,0,0,0.03);
        }}
        .svg-canvas {{ width: 100%; min-width: 980px; height: 680px; display: block; }}
        .svg-edge {{ transition: stroke 0.2s, stroke-width 0.2s, stroke-opacity 0.2s; }}
        .svg-edge.edge-prereq-active {{
            stroke: #059669 !important;
            stroke-width: 3.5 !important;
            stroke-opacity: 1 !important;
            marker-end: url(#marker-prereq) !important;
        }}
        .svg-edge.edge-habilita-active {{
            stroke: #d97706 !important;
            stroke-width: 3.5 !important;
            stroke-opacity: 1 !important;
            marker-end: url(#marker-habilita) !important;
        }}
        .svg-edge.dimmed {{ stroke-opacity: 0.1 !important; }}
        .svg-node-rect {{ transition: stroke 0.2s, fill 0.2s; }}
        .svg-node-group:hover .svg-node-rect {{ stroke-width: 3; }}
        .svg-node-group.selected .svg-node-rect {{
            fill: #eff6ff !important;
            stroke: #0f2d59 !important;
            stroke-width: 3.5 !important;
        }}
        .svg-node-group.prereq-active .svg-node-rect {{
            fill: #ecfdf5 !important;
            stroke: #059669 !important;
            stroke-width: 3 !important;
        }}
        .svg-node-group.habilita-active .svg-node-rect {{
            fill: #fffbeb !important;
            stroke: #d97706 !important;
            stroke-width: 3 !important;
        }}
        .svg-node-group.dimmed {{ opacity: 0.35; }}

        /* SIDE PANEL */
        .side-detail-panel {{
            background: #ffffff;
            border: 1px solid var(--border-color);
            border-radius: 10px;
            padding: 24px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
            position: sticky;
            top: 80px;
        }}
        .side-detail-header {{
            padding-bottom: 14px;
            border-bottom: 1px solid var(--border-color);
            margin-bottom: 16px;
        }}
        .side-detail-badge {{
            display: inline-block;
            background: var(--kinal-blue);
            color: #ffffff;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 0.75rem;
            font-weight: 800;
            margin-bottom: 8px;
        }}
        .side-detail-header h3 {{
            font-size: 1.15rem;
            color: var(--kinal-blue);
            line-height: 1.3;
            margin-bottom: 4px;
        }}
        .side-detail-sub {{ font-size: 0.85rem; color: var(--text-muted); }}
        .side-section {{ margin-bottom: 16px; }}
        .side-section-title {{
            font-size: 0.76rem;
            font-weight: 800;
            text-transform: uppercase;
            color: var(--text-muted);
            letter-spacing: 0.4px;
            margin-bottom: 6px;
        }}
        .side-list {{
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 6px;
        }}
        .side-list li {{
            font-size: 0.82rem;
            padding: 6px 10px;
            border-radius: 6px;
            cursor: pointer;
            transition: all 0.15s;
        }}
        .side-list-prereq li {{ background: #ecfdf5; color: #065f46; border: 1px solid #a7f3d0; }}
        .side-list-prereq li:hover {{ background: #d1fae5; }}
        .side-list-habilita li {{ background: #fffbeb; color: #92400e; border: 1px solid #fde68a; }}
        .side-list-habilita li:hover {{ background: #fef3c7; }}
        .side-callout {{
            background: #f8fafc;
            border: 1px solid var(--border-light);
            padding: 12px;
            border-radius: 6px;
            font-size: 0.82rem;
            color: #334155;
            line-height: 1.4;
            margin-bottom: 16px;
        }}
        .btn-side-action {{
            display: block;
            width: 100%;
            text-align: center;
            background: var(--kinal-blue);
            color: #ffffff;
            text-decoration: none;
            padding: 9px;
            border-radius: 6px;
            font-size: 0.85rem;
            font-weight: 600;
            margin-bottom: 8px;
        }}
        .btn-side-action:hover {{ background: #1e3a8a; }}

        /* RUTAS TRANSVERSALES */
        .transversal-routes {{
            margin-top: 40px;
            background: #ffffff;
            border: 1px solid var(--border-color);
            border-radius: 10px;
            padding: 28px;
        }}
        .transversal-routes h3 {{
            color: var(--kinal-blue);
            font-size: 1.3rem;
            margin-bottom: 6px;
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        .routes-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 16px;
            margin-top: 18px;
        }}
        .route-card {{
            background: #f8fafc;
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 18px;
            border-top: 4px solid var(--kinal-blue);
        }}
        .route-card h4 {{ font-size: 0.98rem; color: var(--kinal-blue); margin-bottom: 6px; }}
        .route-card p {{ font-size: 0.84rem; color: var(--text-dark); margin-bottom: 12px; }}
        .route-steps {{ display: flex; flex-direction: column; gap: 6px; }}
        .route-step-item {{
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 0.82rem;
            padding: 4px 8px;
            background: #ffffff;
            border: 1px solid var(--border-light);
            border-radius: 4px;
        }}
        .step-arrow {{ color: var(--kinal-accent); font-weight: 700; }}

        /* TEMARIOS */
        .controls-panel {{
            background: #f8fafc;
            border: 1px solid var(--border-color);
            border-radius: 10px;
            padding: 20px 24px;
            margin-bottom: 32px;
            display: flex;
            flex-direction: column;
            gap: 16px;
        }}
        .controls-top {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 12px;
        }}
        .search-box {{ flex-grow: 1; max-width: 360px; position: relative; }}
        .search-input {{
            width: 100%;
            padding: 8px 14px 8px 36px;
            border: 1px solid var(--border-color);
            border-radius: 6px;
            font-size: 0.9rem;
            outline: none;
        }}
        .search-icon {{ position: absolute; left: 10px; top: 50%; transform: translateY(-50%); color: var(--text-muted); }}
        .linea-tabs {{ display: flex; gap: 10px; flex-wrap: wrap; }}
        .tab-btn {{
            background: #ffffff;
            border: 1px solid var(--border-color);
            padding: 8px 16px;
            border-radius: 6px;
            font-size: 0.88rem;
            font-weight: 600;
            color: var(--text-dark);
            cursor: pointer;
            transition: all 0.2s;
        }}
        .tab-btn.active {{
            background: var(--kinal-blue);
            color: #ffffff;
            border-color: var(--kinal-blue);
        }}

        .linea-header {{
            background: #ffffff;
            border: 1px solid var(--border-color);
            border-left: 6px solid var(--kinal-blue);
            border-radius: 8px;
            padding: 22px 28px;
            margin-bottom: 24px;
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            flex-wrap: wrap;
            gap: 16px;
        }}
        .linea-header h2 {{ font-size: 1.45rem; color: var(--kinal-blue); margin-bottom: 6px; }}
        .linea-badge {{
            display: inline-block;
            padding: 3px 10px;
            border-radius: 4px;
            font-size: 0.78rem;
            font-weight: 700;
            text-transform: uppercase;
            border: 1px solid;
            margin-bottom: 8px;
        }}
        .linea-courses-list {{ display: flex; flex-direction: column; gap: 24px; }}
        .temario-card {{
            background: #ffffff;
            border: 1px solid var(--border-color);
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 2px 8px rgba(0,0,0,0.04);
            scroll-margin-top: 100px;
        }}
        .temario-header {{ background: #f8fafc; padding: 20px 24px; border-bottom: 1px solid var(--border-color); }}
        .temario-meta {{ display: flex; gap: 8px; align-items: center; flex-wrap: wrap; margin-bottom: 8px; }}
        .badge-bimestre {{ background: #e2e8f0; color: #1e293b; padding: 3px 8px; border-radius: 4px; font-size: 0.78rem; font-weight: 700; }}
        .badge-periodo {{ background: #fef3c7; color: #92400e; padding: 3px 8px; border-radius: 4px; font-size: 0.78rem; font-weight: 600; }}
        .badge-horas {{ background: #e0f2fe; color: #0369a1; padding: 3px 8px; border-radius: 4px; font-size: 0.78rem; font-weight: 600; }}
        .temario-title-bar {{ display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px; }}
        .temario-title-bar h3 {{ font-size: 1.25rem; color: var(--kinal-blue); display: flex; align-items: center; gap: 10px; }}
        .btn-auditoria-link {{
            color: var(--kinal-blue);
            text-decoration: none;
            font-size: 0.85rem;
            font-weight: 600;
            padding: 5px 12px;
            border: 1px solid var(--border-color);
            border-radius: 6px;
            background: #ffffff;
        }}
        .btn-auditoria-link:hover {{ background: var(--kinal-blue); color: #ffffff; }}
        .temario-subtitulo {{ font-size: 0.95rem; color: var(--text-muted); }}
        .temario-body {{ padding: 24px; }}
        .temario-callout {{ background: #eff6ff; border-left: 4px solid #3b82f6; padding: 12px 18px; border-radius: 0 6px 6px 0; font-size: 0.92rem; color: #1e3a8a; margin-bottom: 18px; }}
        
        .correlatividades-box {{
            background: #f8fafc;
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 14px 18px;
            margin-bottom: 20px;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 12px;
        }}
        .corr-item {{ display: flex; flex-direction: column; gap: 6px; }}
        .corr-label {{ font-size: 0.78rem; font-weight: 700; text-transform: uppercase; color: var(--text-muted); }}
        .corr-links {{ display: flex; gap: 6px; flex-wrap: wrap; }}
        .conn-pill {{ display: inline-block; padding: 4px 10px; border-radius: 6px; font-size: 0.8rem; font-weight: 600; text-decoration: none; }}
        .prereq-pill {{ background: #ecfdf5; color: #065f46; border: 1px solid #a7f3d0; }}
        .habilita-pill {{ background: #fffbeb; color: #92400e; border: 1px solid #fde68a; }}
        .no-prereq {{ background: #f1f5f9; color: #64748b; border: 1px solid #cbd5e1; font-size: 0.78rem; }}
        .final-curso {{ background: #fef3c7; color: #92400e; border: 1px solid #fde68a; font-size: 0.78rem; }}

        .unidades-container {{ margin-bottom: 20px; }}
        .unidades-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; }}
        .btn-toggle-unidades {{ background: none; border: 1px solid var(--border-color); padding: 4px 10px; border-radius: 4px; font-size: 0.78rem; cursor: pointer; }}
        .unidades-content {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px; }}
        .unidad-box {{ background: #ffffff; border: 1px solid var(--border-color); border-radius: 8px; padding: 14px 16px; }}
        .unidad-title {{ display: flex; align-items: center; gap: 8px; margin-bottom: 10px; padding-bottom: 6px; border-bottom: 1px solid var(--border-light); }}
        .unidad-badge {{ background: #f1f5f9; color: var(--kinal-blue); font-size: 0.72rem; font-weight: 800; padding: 2px 6px; border-radius: 4px; }}
        .unidad-title h4 {{ font-size: 0.88rem; color: var(--kinal-blue); }}
        .unidad-temas {{ padding-left: 18px; font-size: 0.82rem; color: #334155; line-height: 1.45; }}
        .unidad-temas li {{ margin-bottom: 6px; }}

        .ia-box {{ background: var(--color-ia-bg); border-left: 4px solid var(--color-ia); padding: 14px 18px; border-radius: 0 8px 8px 0; margin-bottom: 18px; }}
        .ia-badge {{ font-size: 0.75rem; font-weight: 800; color: var(--color-ia); text-transform: uppercase; }}
        .ia-box p {{ font-size: 0.88rem; color: #312e81; margin: 0; }}

        .temario-footer-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 14px; padding-top: 14px; border-top: 1px solid var(--border-light); font-size: 0.86rem; }}
        .footer-block strong {{ display: block; color: var(--kinal-blue); margin-bottom: 4px; font-size: 0.82rem; text-transform: uppercase; }}

        /* AUDITORÍA */
        .audit-list {{ display: flex; flex-direction: column; gap: 24px; }}
        .audit-card {{
            background: #ffffff;
            border: 1px solid var(--border-color);
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 2px 8px rgba(0,0,0,0.03);
            scroll-margin-top: 100px;
        }}
        .audit-card-header {{ background: #f8fafc; padding: 18px 24px; border-bottom: 1px solid var(--border-color); }}
        .audit-meta {{ display: flex; gap: 8px; margin-bottom: 6px; }}
        .audit-card-header h3 {{ font-size: 1.25rem; color: var(--kinal-blue); display: flex; align-items: center; gap: 10px; }}
        .audit-sub {{ font-size: 0.9rem; color: var(--text-muted); }}
        .audit-body {{ padding: 24px; }}
        .audit-table {{ width: 100%; border-collapse: collapse; margin-bottom: 18px; font-size: 0.9rem; }}
        .audit-table th, .audit-table td {{ padding: 12px 16px; border: 1px solid var(--border-color); vertical-align: top; text-align: left; }}
        .audit-table th {{ background: #f8fafc; color: var(--kinal-blue); font-weight: 700; }}
        .row-anular {{ background: #fff5f5; }}
        .row-actualizar {{ background: #fefce8; }}
        .row-nuevo {{ background: #eff6ff; }}

        .tag-pill {{ display: inline-block; padding: 3px 8px; border-radius: 4px; font-size: 0.78rem; font-weight: 700; text-transform: uppercase; }}
        .tag-original {{ background: #e2e8f0; color: #334155; }}
        .tag-anular {{ background: var(--color-anular-bg); color: var(--color-anular-text); border: 1px solid var(--color-anular-border); }}
        .tag-actualizar {{ background: var(--color-actualizar-bg); color: var(--color-actualizar-text); border: 1px solid var(--color-actualizar-border); }}
        .tag-nuevo {{ background: var(--color-nuevo-bg); color: var(--color-nuevo-text); border: 1px solid var(--color-nuevo-border); }}

        .audit-callout {{ padding: 8px 12px; border-radius: 6px; font-size: 0.88rem; }}
        .callout-red {{ background: var(--color-anular-bg); color: var(--color-anular-text); border-left: 4px solid var(--color-anular-border); }}
        .callout-yellow {{ background: var(--color-actualizar-bg); color: var(--color-actualizar-text); border-left: 4px solid var(--color-actualizar-border); }}
        .callout-blue {{ background: var(--color-nuevo-bg); color: var(--color-nuevo-text); border-left: 4px solid var(--color-nuevo-border); }}

        .audit-justificacion {{ background: #f8fafc; border: 1px solid var(--border-light); padding: 14px 18px; border-radius: 8px; font-size: 0.88rem; margin-bottom: 16px; }}
        .audit-justificacion strong {{ display: block; color: var(--kinal-blue); margin-bottom: 4px; }}
        .audit-actions {{ text-align: right; }}
        .btn-goto-temario {{ font-size: 0.85rem; color: var(--kinal-blue); font-weight: 600; text-decoration: none; }}
        .btn-goto-temario:hover {{ text-decoration: underline; }}

        /* BIMESTRES OPERATIVO */
        .bimestre-group {{ margin-bottom: 36px; }}
        .bimestre-group-header {{
            background: #0b1f3a;
            color: #ffffff;
            padding: 14px 20px;
            border-radius: 8px 8px 0 0;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .bimestre-group-header h3 {{ font-size: 1.25rem; color: #fef08a; }}
        .bimestre-group-header span {{ font-size: 0.85rem; color: #cbd5e1; }}
        .bimestre-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
            gap: 16px;
            padding: 20px;
            background: #ffffff;
            border: 1px solid var(--border-color);
            border-top: none;
            border-radius: 0 0 8px 8px;
        }}
        .bimestre-course-card {{
            background: #f8fafc;
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 16px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}
        .b-period {{ font-size: 0.76rem; font-weight: 700; color: var(--kinal-accent); text-transform: uppercase; }}
        .b-code {{ font-size: 0.75rem; font-weight: 800; color: var(--kinal-blue); }}
        .bimestre-course-card h4 {{ font-size: 1rem; color: var(--kinal-blue); margin: 6px 0; }}
        .b-eje {{ font-size: 0.8rem; color: #0369a1; font-weight: 600; margin-bottom: 6px; }}
        .b-sub {{ font-size: 0.82rem; color: var(--text-muted); margin-bottom: 12px; flex-grow: 1; }}
        .b-links {{ font-size: 0.82rem; border-top: 1px solid var(--border-light); padding-top: 8px; }}
        .b-links a {{ color: var(--kinal-blue); text-decoration: none; font-weight: 600; }}
        .b-links a:hover {{ text-decoration: underline; }}

        footer.main-footer {{
            background: var(--kinal-blue-dark);
            color: #94a3b8;
            padding: 32px 48px;
            font-size: 0.9rem;
            text-align: center;
            border-top: 1px solid rgba(255,255,255,0.1);
        }}

        @media (max-width: 1024px) {{
            .map-layout {{ grid-template-columns: 1fr; }}
            .side-detail-panel {{ position: static; }}
            main.main-content {{ padding: 24px 20px; }}
            header.main-header {{ padding: 30px 24px; }}
        }}
    </style>
</head>
<body>

<div class="app-container">

    <!-- HERO HEADER -->
    <header class="main-header">
        <div class="header-top-badges">
            <span class="badge-pill">Pensum Consolidado 2026</span>
            <span class="badge-pill-alt">Escuela Técnica Superior Fundación Kinal</span>
            <span class="badge-pill-alt">Convenio Universidad del Istmo (UNIS)</span>
            <span class="badge-pill-alt">Equivalencia DQR Niveles 5 y 6</span>
        </div>
        <h1>AUDITORÍA Y REDISEÑO CURRICULAR INTEGRAL: TSU 2026</h1>
        <p>Portal curricular unificado de los <strong>20 cursos</strong> del 3er Año Académico del <strong>Técnico Superior Universitario (TSU)</strong>. Plataforma única que consolida el mapa curricular interactivo con red de correlatividades, los temarios completos por línea de estudio, el dictamen de auditoría (lo que se anula, actualiza y nuevo) y la distribución transversal para las 7 carreras técnicas con Inteligencia Artificial.</p>
        
        <div class="header-stats-grid">
            <div class="stat-card">
                <strong>20 Cursos</strong>
                <span>Tronco común de supervisión</span>
            </div>
            <div class="stat-card">
                <strong>4 Bimestres</strong>
                <span>10 meses lectivos (270 hrs)</span>
            </div>
            <div class="stat-card">
                <strong>4 Líneas</strong>
                <span>Ejes formativos articulados</span>
            </div>
            <div class="stat-card">
                <strong>7 Especialidades</strong>
                <span>Convergencia técnica Kinal</span>
            </div>
            <div class="stat-card">
                <strong>&ge; 75 Puntos</strong>
                <span>Nota mínima aprobatoria</span>
            </div>
        </div>
    </header>

    <!-- STICKY NAVBAR -->
    <nav class="sticky-nav">
        <a href="#seccion-resumen" class="active"><span>📋</span> Resumen & Especialidades</a>
        <a href="#seccion-mapa"><span>🗺️</span> Mapa Curricular & Red</a>
        <a href="#seccion-temarios"><span>📚</span> Temarios por Línea</a>
        <a href="#seccion-auditoria"><span>⚖️</span> Auditoría & Dictamen</a>
        <a href="#seccion-bimestres"><span>🗓️</span> Distribución Bimestral</a>
    </nav>

    <main class="main-content">

        <!-- ======================================================== -->
        <!-- SECCIÓN 1: RESUMEN, IDEARIO Y 7 ESPECIALIDADES TÉCNICAS   -->
        <!-- ======================================================== -->
        <section class="portal-section" id="seccion-resumen">
            <div class="section-header-bar">
                <div class="section-title-group">
                    <h2><span>📋</span> Fundamentación Curricular y Principio de Transversalidad</h2>
                    <p>El 3er año del TSU integra a técnicos graduados de 7 especialidades para formar mandos medios con visión gerencial y ética profesional.</p>
                </div>
            </div>

            <div class="callout-gold">
                <h4>Ideario Kinal y Parámetros Académicos Institucionales</h4>
                <p>
                    La formación del TSU se fundamenta en los cinco pilares institucionales: <em>"Visión cristiana de la vida. Respeto a la dignidad de la persona. Espíritu de servicio. Trabajo bien hecho. Libertad personal responsable"</em>.
                    <br><strong>Exigencias de Egreso:</strong> Nota mínima aprobatoria de <strong>&ge; 75 puntos sobre 100</strong> en todas las asignaturas y certificación de nivel <strong>A2</strong> en idioma inglés mediante la prueba ELASH II (Kinal Language School).
                </p>
            </div>

            <h3 style="color: var(--kinal-blue); font-size: 1.25rem; margin-bottom: 16px;">Convergencia de las 7 Especialidades Técnicas de Kinal (UNIS)</h3>
            <div class="specs-grid">
                {especialidades_cards_html}
            </div>
        </section>

        <!-- ======================================================== -->
        <!-- SECCIÓN 2: MAPA CURRICULAR Y RED DE PRERREQUISITOS       -->
        <!-- ======================================================== -->
        <section class="portal-section" id="seccion-mapa">
            <div class="section-header-bar">
                <div class="section-title-group">
                    <h2><span>🗺️</span> Mapa Curricular Interactivo y Red de Prerrequisitos</h2>
                    <p>Descubre qué curso conduce a cuál otro mediante la Rejilla Matricial o el Grafo SVG con flechas dirigidas.</p>
                </div>
            </div>

            <div class="map-instructions">
                <div class="map-instructions-text">
                    <p>Haz <strong>clic o pasa el ratón</strong> sobre cualquier tarjeta o nodo para iluminar su <strong>Ruta Crítica</strong>: se resaltarán en verde sus prerrequisitos y en ámbar los cursos que desbloquea.</p>
                </div>
                <div class="legend-bar">
                    <div class="legend-chip"><span class="chip-dot chip-selected"></span> Seleccionado</div>
                    <div class="legend-chip"><span class="chip-dot chip-prereq"></span> Prerrequisito Requerido</div>
                    <div class="legend-chip"><span class="chip-dot chip-habilita"></span> Curso que Habilita</div>
                </div>
            </div>

            <div class="view-controls">
                <div class="mode-buttons">
                    <button class="mode-btn active" id="btnModeGrid" onclick="switchViewMode('grid')">
                        <span>📊</span> Rejilla Curricular (Matriz 4x4)
                    </button>
                    <button class="mode-btn" id="btnModeNetwork" onclick="switchViewMode('network')">
                        <span>🕸️</span> Red de Correlatividades (Grafo SVG)
                    </button>
                </div>

                <div class="filter-linea-select">
                    <span>Línea Formativa:</span>
                    <select id="lineaFilterSelect" onchange="filterMapByLinea(this.value)">
                        <option value="all">Todas las 4 Líneas de Estudio</option>
                        <option value="linea-etica">🛡️ Formación Humana y Ética</option>
                        <option value="linea-gestion">📋 Gestión y Supervisión</option>
                        <option value="linea-matematica">📐 Ciencias Exactas y Analítica</option>
                        <option value="linea-fisica">⚡ Física y Tecnología 4.0</option>
                    </select>
                </div>
            </div>

            <div class="map-layout">
                <!-- VISTA 1: REJILLA -->
                <div class="curriculum-grid-container" id="gridContainer">
                    <div class="grid-header-row">
                        <div class="grid-header-cell">Línea Formativa / Eje</div>
                        <div class="grid-header-cell">Bimestre 1<br><small style="font-weight:400; opacity:0.8;">Fundamentos y Estática</small></div>
                        <div class="grid-header-cell">Bimestre 2<br><small style="font-weight:400; opacity:0.8;">Costos, SSO y Materiales</small></div>
                        <div class="grid-header-cell">Bimestre 3<br><small style="font-weight:400; opacity:0.8;">Lean, SLAs y Analítica</small></div>
                        <div class="grid-header-cell">Bimestre 4<br><small style="font-weight:400; opacity:0.8;">Calidad, BI, Finanzas y Python</small></div>
                    </div>
                    {grid_rows_html}
                </div>

                <!-- VISTA 2: RED SVG -->
                <div class="network-svg-container" id="networkContainer">
                    <svg class="svg-canvas" viewBox="0 0 1020 660">
                        <defs>
                            <marker id="marker-linea-etica" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                                <path d="M 0 1 L 10 5 L 0 9 z" fill="#0284c7" />
                            </marker>
                            <marker id="marker-linea-gestion" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                                <path d="M 0 1 L 10 5 L 0 9 z" fill="#d97706" />
                            </marker>
                            <marker id="marker-linea-matematica" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                                <path d="M 0 1 L 10 5 L 0 9 z" fill="#16a34a" />
                            </marker>
                            <marker id="marker-linea-fisica" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                                <path d="M 0 1 L 10 5 L 0 9 z" fill="#7c3aed" />
                            </marker>
                            <marker id="marker-prereq" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
                                <path d="M 0 1 L 10 5 L 0 9 z" fill="#059669" />
                            </marker>
                            <marker id="marker-habilita" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
                                <path d="M 0 1 L 10 5 L 0 9 z" fill="#d97706" />
                            </marker>
                        </defs>

                        <rect x="30" y="10" width="190" height="640" rx="8" fill="#f8fafc" stroke="#e2e8f0" />
                        <text x="125" y="32" text-anchor="middle" font-size="12" font-weight="800" fill="#0f2d59">BIMESTRE 1</text>

                        <rect x="280" y="10" width="190" height="640" rx="8" fill="#fafbfc" stroke="#e2e8f0" />
                        <text x="375" y="32" text-anchor="middle" font-size="12" font-weight="800" fill="#0f2d59">BIMESTRE 2</text>

                        <rect x="530" y="10" width="190" height="640" rx="8" fill="#f8fafc" stroke="#e2e8f0" />
                        <text x="625" y="32" text-anchor="middle" font-size="12" font-weight="800" fill="#0f2d59">BIMESTRE 3</text>

                        <rect x="780" y="10" width="190" height="640" rx="8" fill="#fafbfc" stroke="#e2e8f0" />
                        <text x="875" y="32" text-anchor="middle" font-size="12" font-weight="800" fill="#0f2d59">BIMESTRE 4</text>

                        <g id="svgEdgesGroup">{svg_edges_html}</g>
                        <g id="svgNodesGroup">{svg_nodes_html}</g>
                    </svg>
                </div>

                <!-- PANEL LATERAL -->
                <aside class="side-detail-panel" id="sideDetailPanel">
                    <div class="side-detail-header">
                        <span class="side-detail-badge" id="sideBadge">B1-C1</span>
                        <h3 id="sideTitle">🛡️ Ética General 1</h3>
                        <div class="side-detail-sub" id="sideSub">Antropología y Sentido Trascendente del Trabajo</div>
                    </div>

                    <div class="side-section">
                        <div class="side-section-title">⬅️ Prerrequisitos de Entrada</div>
                        <ul class="side-list side-list-prereq" id="sidePrereqList">
                            <li>Ingreso al 3er Año TSU</li>
                        </ul>
                    </div>

                    <div class="side-section">
                        <div class="side-section-title">➡️ Asignaturas que Habilita</div>
                        <ul class="side-list side-list-habilita" id="sideHabilitaList">
                            <li>B2-C1 • Ética General 2</li>
                            <li>B2-C3 • Administración de RRHH y SSO</li>
                        </ul>
                    </div>

                    <div class="side-section">
                        <div class="side-section-title">🎯 Objetivo Transversal</div>
                        <div class="side-callout" id="sideObjetivo">
                            Forjar el carácter ético del supervisor técnico bajo el ideario de Kinal: la persona en el centro de la operación y el trabajo bien hecho como medio de superación.
                        </div>
                    </div>

                    <div class="side-section">
                        <div class="side-section-title">🤖 Integración con IA</div>
                        <div class="side-callout" id="sideIA" style="background: #eef2ff; color: #3730a3; border-color: #c7d2fe;">
                            Sesgos cognitivos humanos frente a sesgos en modelos de IA: el papel de la conciencia moral que ninguna máquina puede replicar.
                        </div>
                    </div>

                    <div style="margin-top: 18px;">
                        <a href="#temario-b1_etica_general_1" class="btn-side-action" id="sideLinkTemario">Ver Temario Completo ↓</a>
                        <a href="#audit-b1_etica_general_1" class="btn-side-action" id="sideLinkAudit" style="background:#475569;">Ver Auditoría y Dictamen ↓</a>
                    </div>
                </aside>
            </div>

            <!-- RUTAS TRANSVERSALES -->
            <div class="transversal-routes">
                <h3><span>🔗</span> Conexiones Curriculares Inter-Ejes (Rutas Críticas Transversales)</h3>
                <p>Las competencias cuantitativas y físicas sustentan directamente las decisiones operativas, financieras y éticas de los mandos medios.</p>

                <div class="routes-grid">
                    <div class="route-card" style="border-top-color: #16a34a;">
                        <h4>Ruta Cuantitativa & Financiera</h4>
                        <p>De la proporcionalidad matemática a la justificación de inversiones de capital (CAPEX):</p>
                        <div class="route-steps">
                            <div class="route-step-item"><span>📐</span> B1-C4 Matemática Básica 1 (Excel)</div>
                            <div class="route-step-item"><span class="step-arrow">↓</span> 💰 B2-C2 Herramientas Contables (Costos)</div>
                            <div class="route-step-item"><span class="step-arrow">↓</span> 📊 B3-C4 Matemática Aplicada 1 (Estadística)</div>
                            <div class="route-step-item"><span class="step-arrow">↓</span> 🏦 B4-C4 Matemática Aplicada 2 (Ing. Económica VPN/TIR)</div>
                        </div>
                    </div>

                    <div class="route-card" style="border-top-color: #d97706;">
                        <h4>Ruta de Procesos, Lean & Six Sigma</h4>
                        <p>De la secuenciación de turnos al aseguramiento de cero defectos en la fuente:</p>
                        <div class="route-steps">
                            <div class="route-step-item"><span>📋</span> B1-C2 Fundamentos de la Administración</div>
                            <div class="route-step-item"><span class="step-arrow">↓</span> ⏱️ B1-C3 Planeación y Control (OEE & Kanban)</div>
                            <div class="route-step-item"><span class="step-arrow">↓</span> 🏭 B3-C2 Métodos de Producción (Lean & VSM)</div>
                            <div class="route-step-item"><span class="step-arrow">↓</span> 🎯 B4-C2 Control de Calidad (Six Sigma DMAIC & AMFE)</div>
                        </div>
                    </div>

                    <div class="route-card" style="border-top-color: #7c3aed;">
                        <h4>Ruta Tecnológica e Industria 4.0</h4>
                        <p>De la lógica formal a la analítica de datos en Power BI y automatización con Python:</p>
                        <div class="route-steps">
                            <div class="route-step-item"><span>📉</span> B2-C4 Matemática Básica 2 (Lógica Booleana)</div>
                            <div class="route-step-item"><span class="step-arrow">↓</span> ⚡ B3-C5 Física Aplicada 2 (Energía y Curvas de Carga)</div>
                            <div class="route-step-item"><span class="step-arrow">↓</span> 📈 B4-C3 Marketing & BI (Power BI)</div>
                            <div class="route-step-item"><span class="step-arrow">↓</span> 💻 B4-C5 Física Aplicada 3 (Sensores & Python)</div>
                        </div>
                    </div>

                    <div class="route-card" style="border-top-color: #0284c7;">
                        <h4>Ruta Ética, Legislación y Gobernanza Humana</h4>
                        <p>Del respeto inalienable a la supervisión humana indelegable (HITL):</p>
                        <div class="route-steps">
                            <div class="route-step-item"><span>🛡️</span> B1-C1 Ética General 1 (Dignidad del Trabajo)</div>
                            <div class="route-step-item"><span class="step-arrow">↓</span> 🦺 B2-C3 Administración de RRHH & SSO (Código de Trabajo/IGSS)</div>
                            <div class="route-step-item"><span class="step-arrow">↓</span> 🤖 B3-C1 Ética Profesional 1 (Transición Justa)</div>
                            <div class="route-step-item"><span class="step-arrow">↓</span> 🧠 B4-C1 Ética Profesional 2 (Principio HITL)</div>
                        </div>
                    </div>
                </div>
            </div>
        </section>

        <!-- ======================================================== -->
        <!-- SECCIÓN 3: TEMARIOS POR LÍNEA DE ESTUDIO                 -->
        <!-- ======================================================== -->
        <section class="portal-section" id="seccion-temarios">
            <div class="section-header-bar">
                <div class="section-title-group">
                    <h2><span>📚</span> Temarios Modernizados por Línea de Estudio</h2>
                    <p>Desglose exhaustivo de las 4 unidades temáticas, vinculación con IA, herramientas y aplicación técnica para cada asignatura.</p>
                </div>
            </div>

            <div class="controls-panel">
                <div class="controls-top">
                    <div class="linea-tabs">
                        <button class="tab-btn active" onclick="filterByLinea('all', this)">
                            <span>🌐</span> Todas las Líneas (20)
                        </button>
                        <button class="tab-btn" onclick="filterByLinea('linea-etica', this)">
                            <span>🛡️</span> Ética (4)
                        </button>
                        <button class="tab-btn" onclick="filterByLinea('linea-gestion', this)">
                            <span>📋</span> Gestión & Supervisión (8)
                        </button>
                        <button class="tab-btn" onclick="filterByLinea('linea-matematica', this)">
                            <span>📐</span> Ciencias Exactas (4)
                        </button>
                        <button class="tab-btn" onclick="filterByLinea('linea-fisica', this)">
                            <span>⚡</span> Física & Tecnología 4.0 (4)
                        </button>
                    </div>

                    <div class="search-box">
                        <span class="search-icon">🔎</span>
                        <input type="text" id="searchInput" class="search-input" placeholder="Buscar por software, tema o código..." onkeyup="filterTemarios()">
                    </div>
                </div>

                <div style="font-size: 0.85rem; color: var(--text-muted); border-top: 1px solid var(--border-light); padding-top: 8px;">
                    <span>Acciones de unidades:</span>
                    <button style="background:none;border:none;color:var(--kinal-blue);cursor:pointer;font-weight:600;" onclick="toggleAllUnidades(true)">Expandir todas</button> • 
                    <button style="background:none;border:none;color:var(--kinal-blue);cursor:pointer;font-weight:600;" onclick="toggleAllUnidades(false)">Colapsar todas</button>
                </div>
            </div>

            {temarios_lineas_html}
        </section>

        <!-- ======================================================== -->
        <!-- SECCIÓN 4: AUDITORÍA Y MATRIZ DE DICTAMEN                -->
        <!-- ======================================================== -->
        <section class="portal-section" id="seccion-auditoria">
            <div class="section-header-bar">
                <div class="section-title-group">
                    <h2><span>⚖️</span> Auditoría Curricular y Matriz de Dictamen (20 Cursos)</h2>
                    <p>Diagnóstico comparativo formal: lo que se anula por obsolescencia, lo que se actualiza y los nuevos conocimientos demandados por la industria.</p>
                </div>
            </div>

            <div class="audit-list">
                {audit_cards_html}
            </div>
        </section>

        <!-- ======================================================== -->
        <!-- SECCIÓN 5: DISTRIBUCIÓN OPERATIVA POR BIMESTRES          -->
        <!-- ======================================================== -->
        <section class="portal-section" id="seccion-bimestres">
            <div class="section-header-bar">
                <div class="section-title-group">
                    <h2><span>🗓️</span> Distribución Académica Operativa del Año Lectivo</h2>
                    <p>Secuencia temporal de los 4 bimestres (10 meses lectivos, febrero a noviembre) con sus 5 periodos diarios de 50 minutos.</p>
                </div>
            </div>

            {bimestres_blocks_html}

            <div style="background: #e2e8f0; padding: 24px; border-radius: 8px; margin-top: 24px;">
                <h3 style="color: var(--kinal-blue); margin-bottom: 8px;">Acreditación y Salida Profesional</h3>
                <p style="font-size: 0.92rem; color: var(--text-dark);">
                    Al completar y aprobar satisfactoriamente los 4 bimestres (20 asignaturas con nota &ge; 75 pts) y certificar el nivel A2 en inglés (prueba ELASH II vía Kinal Language School), el egresado obtiene el <strong>Título de Técnico Superior Universitario en su Especialidad</strong> avalado por la <strong>Universidad del Istmo (UNIS)</strong> y Fundación Kinal, con equivalencia internacional a los niveles 5 y 6 del Marco Alemán de Cualificaciones (DQR).
                </p>
            </div>
        </section>

    </main>

    <footer class="main-footer">
        <p><strong>Fundación Kinal • Escuela Técnica Superior • Pensum General del Técnico Superior Universitario (TSU 2026)</strong></p>
        <p style="margin-top: 6px; font-size: 0.82rem; opacity: 0.8;">Convenio Universidad del Istmo (UNIS) • Marco Alemán de Cualificaciones (DQR 5/6) • Guatemala, 2026</p>
    </footer>

</div>

<script>
    const cursosData = {relaciones_str};
    let selectedCourseId = "b1_etica_general_1";
    let currentViewMode = "grid";

    function switchViewMode(mode) {{
        currentViewMode = mode;
        const btnGrid = document.getElementById('btnModeGrid');
        const btnNet = document.getElementById('btnModeNetwork');
        const gridContainer = document.getElementById('gridContainer');
        const netContainer = document.getElementById('networkContainer');

        if (mode === 'grid') {{
            btnGrid.classList.add('active');
            btnNet.classList.remove('active');
            gridContainer.style.display = 'block';
            netContainer.style.display = 'none';
        }} else {{
            btnGrid.classList.remove('active');
            btnNet.classList.add('active');
            gridContainer.style.display = 'none';
            netContainer.style.display = 'block';
        }}
        renderActiveRuta(selectedCourseId);
    }}

    function filterMapByLinea(lineaId) {{
        const rows = document.querySelectorAll('.grid-linea-row');
        rows.forEach(r => {{
            r.style.display = (lineaId === 'all' || r.id === 'row-' + lineaId) ? 'grid' : 'none';
        }});

        const svgNodes = document.querySelectorAll('.svg-node-group');
        const svgEdges = document.querySelectorAll('.svg-edge');

        svgNodes.forEach(node => {{
            const nLinea = node.getAttribute('data-linea');
            node.style.display = (lineaId === 'all' || nLinea === lineaId) ? 'block' : 'none';
        }});

        svgEdges.forEach(edge => {{
            edge.style.display = (lineaId === 'all' || edge.classList.contains('edge-linea-' + lineaId)) ? 'block' : 'none';
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

        const allGridNodes = document.querySelectorAll('.node-card');
        allGridNodes.forEach(node => {{
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

        const allSvgNodes = document.querySelectorAll('.svg-node-group');
        allSvgNodes.forEach(node => {{
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

        const allSvgEdges = document.querySelectorAll('.svg-edge');
        allSvgEdges.forEach(edge => {{
            edge.classList.remove('edge-prereq-active', 'edge-habilita-active', 'dimmed');
            const src = edge.getAttribute('data-source');
            const tgt = edge.getAttribute('data-target');

            if (tgt === courseId && course.prerequisitos.includes(src)) {{
                edge.classList.add('edge-prereq-active');
            }} else if (src === courseId && course.habilita.includes(tgt)) {{
                edge.classList.add('edge-habilita-active');
            }} else {{
                edge.classList.add('dimmed');
            }}
        }});
    }}

    function updateSidePanel(courseId) {{
        const course = cursosData[courseId];
        if (!course) return;

        document.getElementById('sideBadge').innerText = course.codigo + ' • ' + course.bimestre;
        document.getElementById('sideTitle').innerHTML = course.icono + ' ' + course.nombre;
        document.getElementById('sideSub').innerText = course.subtitulo;
        document.getElementById('sideObjetivo').innerText = course.objetivo;
        document.getElementById('sideIA').innerText = course.subtema_ia;

        const prereqList = document.getElementById('sidePrereqList');
        prereqList.innerHTML = '';
        if (course.prerequisitos.length > 0) {{
            course.prerequisitos.forEach(pId => {{
                const pInfo = cursosData[pId];
                const li = document.createElement('li');
                li.innerText = '⬅️ ' + pInfo.codigo + ' • ' + pInfo.nombre;
                li.onclick = () => selectCourseNode(pId);
                prereqList.appendChild(li);
            }});
        }} else {{
            const li = document.createElement('li');
            li.style.background = '#f1f5f9';
            li.style.color = '#64748b';
            li.style.borderColor = '#cbd5e1';
            li.innerText = 'Ingreso al 3er Año TSU (Sin prerrequisito previo de 3er año)';
            prereqList.appendChild(li);
        }}

        const habilitaList = document.getElementById('sideHabilitaList');
        habilitaList.innerHTML = '';
        if (course.habilita.length > 0) {{
            course.habilita.forEach(hId => {{
                const hInfo = cursosData[hId];
                const li = document.createElement('li');
                li.innerText = '➡️ ' + hInfo.codigo + ' • ' + hInfo.nombre;
                li.onclick = () => selectCourseNode(hId);
                habilitaList.appendChild(li);
            }});
        }} else {{
            const li = document.createElement('li');
            li.style.background = '#fef3c7';
            li.style.color = '#92400e';
            li.style.borderColor = '#fde68a';
            li.innerText = 'Culminación del Plan / Graduación TSU';
            habilitaList.appendChild(li);
        }}

        document.getElementById('sideLinkTemario').href = '#temario-' + course.id;
        document.getElementById('sideLinkAudit').href = '#audit-' + course.id;
    }}

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

    function scrollToMap() {{
        const el = document.getElementById('seccion-mapa');
        if (el) el.scrollIntoView({{ behavior: 'smooth' }});
    }}

    function scrollToAudit(id) {{
        const el = document.getElementById('audit-' + id);
        if (el) el.scrollIntoView({{ behavior: 'smooth' }});
    }}

    // Resaltar link activo en scroll
    window.addEventListener('scroll', () => {{
        const sections = document.querySelectorAll('section.portal-section');
        const scrollPos = window.scrollY + 120;

        sections.forEach(sec => {{
            const top = sec.offsetTop;
            const height = sec.offsetHeight;
            const id = sec.getAttribute('id');
            if (scrollPos >= top && scrollPos < top + height) {{
                document.querySelectorAll('nav.sticky-nav a').forEach(a => {{
                    a.classList.remove('active');
                    if (a.getAttribute('href') === '#' + id) {{
                        a.classList.add('active');
                    }}
                }});
            }}
        }});
    }});

    document.addEventListener('DOMContentLoaded', () => {{
        selectCourseNode('b1_etica_general_1');
    }});
</script>

</body>
</html>
"""

# -------------------------------------------------------------
# ARCHIVAR PÁGINAS PREVIAS EN TSU/historico/
# -------------------------------------------------------------
files_to_archive = [
    "nueva_distribucion_tematica_tsu.html",
    "temarios_por_linea.html",
    "mapa_curricular.html",
    "administracion.html",
    "etica.html",
    "fisica.html",
    "matematica.html"
]

# Agregar los 20 cursos individuales
for cid in unified_courses.keys():
    files_to_archive.append(f"{cid}.html")

print(f"Total archivos a mover a histórico: {len(files_to_archive) + 1} (incluyendo index previo)")

# Respaldar el index anterior a historico/index_anterior.html
current_index_path = os.path.join(base_dir, "index.html")
if os.path.exists(current_index_path):
    shutil.copy2(current_index_path, os.path.join(historico_dir, "index_anterior.html"))
    try:
        shutil.copy2(current_index_path, os.path.join(mybrain_historico_dir, "index_anterior.html"))
    except Exception:
        pass
    print("✓ Respaldado index.html previo en historico/index_anterior.html")

# Mover archivos a histórico
for fname in files_to_archive:
    src = os.path.join(base_dir, fname)
    if os.path.exists(src):
        dst = os.path.join(historico_dir, fname)
        shutil.move(src, dst)
        print(f"✓ Movido a histórico: {fname}")

    # En MyBrain
    mb_src = os.path.join(mybrain_dir, fname)
    if os.path.exists(mb_src):
        mb_dst = os.path.join(mybrain_historico_dir, fname)
        try:
            shutil.move(mb_src, mb_dst)
            print(f"✓ MyBrain movido a histórico: {fname}")
        except Exception:
            pass

# Escribir la nueva landing page maestra en TSU/index.html
with open(current_index_path, "w", encoding="utf-8") as f:
    f.write(master_html)
print(f"✓ Creada exitosamente la Landing Page Maestra Unificada: {current_index_path}")

# Mirror en MyBrain
mb_index_path = os.path.join(mybrain_dir, "index.html")
try:
    with open(mb_index_path, "w", encoding="utf-8") as f:
        f.write(master_html)
    print(f"✓ Creada exitosamente la réplica en MyBrain: {mb_index_path}")
except Exception as e:
    print(f"Nota MyBrain: {e}")

print("\n¡Unificación completada con éxito!")
