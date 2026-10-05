#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Vincula la Línea de Gestión y Supervisión (Pensum TSU) con la Auditoría de Administración (administracion_auditoria.html)
"""

import os
import re
import shutil

def update_tsu_index(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Agregar Banner destacado en la cabecera de la Línea de Gestión
    banner_html = """        <!-- BANNER DE VINCULACIÓN A LA AUDITORÍA DE PLANES ACTUALES 2026 -->
        <div class="linea-audit-alert" style="background: linear-gradient(135deg, #eff6ff 0%, #fefce8 100%); border: 2px solid #3b82f6; border-radius: 12px; padding: 16px 20px; margin-top: 16px; margin-bottom: 24px; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.04);">
            <div style="max-width: 820px;">
                <div style="display: flex; align-items: center; gap: 8px; margin-bottom: 4px;">
                    <span style="background: #2563eb; color: #ffffff; font-size: 0.72rem; font-weight: 800; padding: 2px 8px; border-radius: 4px; text-transform: uppercase;">Auditoría Docente 2026</span>
                    <strong style="color: #0f2d59; font-size: 1rem;">Propuesta de Nuevo Temario Dosificado vinculada a esta Línea de Estudio</strong>
                </div>
                <p style="font-size: 0.88rem; color: #334155; margin: 0; line-height: 1.45;">
                    Revisión minuciosa clase por clase de los <strong>8 planes de clase (40 sesiones anuales)</strong> del curso de Administración (Prof. Sergio Ávalos). Análisis de 4 colores: <strong>28 temas útiles mantenidos</strong>, <strong>18 modernizados</strong>, <strong>16 agregados</strong> (IA, SSO Acdo. 229-2014, Código de Trabajo, OEE, Lean 5S, ISO 9001) y <strong>10 eliminados</strong>.
                </p>
            </div>
            <a href="administracion_auditoria.html" style="background: #0f2d59; color: #ffffff; padding: 10px 18px; border-radius: 8px; font-weight: 700; font-size: 0.88rem; text-decoration: none; display: inline-flex; align-items: center; gap: 8px; box-shadow: 0 4px 12px rgba(15,45,89,0.25); transition: background 0.2s;" onmouseover="this.style.background='#1d4ed8'" onmouseout="this.style.background='#0f2d59'">
                <span>💼</span> Abrir Auditoría & Dosificación Completa →
            </a>
        </div>
"""
    if "linea-audit-alert" not in content:
        # Insertar después del cierre de linea-header en linea-gestion
        target_marker = '<section class="linea-section" id="linea-gestion">\n        <div class="linea-header" style="border-left-color: #d97706;">'
        if target_marker in content:
            # Buscar el final del div linea-header
            pos = content.find(target_marker)
            end_header = content.find('</div>\n        </div>', pos)
            if end_header != -1:
                end_pos = end_header + len('</div>\n        </div>')
                content = content[:end_pos] + "\n" + banner_html + content[end_pos:]
                print("Banner insertado en linea-gestion de TSU/index.html")

    # 2. Mapeo de Cursos a Módulos de Auditoría
    mapping = {
        ("b1_fundamentos_administracion", "Módulo 1"): "modulo-1",
        ("b1_planeacion_control_trabajo", "Módulo 2"): "modulo-2",
        ("b2_herramientas_contables", "Módulo 4"): "modulo-4",
        ("b2_administracion_rrhh_sso", "Módulo 3"): "modulo-3",
        ("b3_metodos_produccion", "Módulo 6"): "modulo-6",
        ("b3_servicio_cliente", "Módulo 5"): "modulo-5",
        ("b4_control_calidad", "Módulo 8"): "modulo-8",
        ("b4_fundamentos_marketing", "Módulo 7"): "modulo-7",
    }

    for (c_id, mod_label), mod_anchor in mapping.items():
        # Buscar el bloque del título del temario
        pattern = f'(id="temario-{c_id}".*?<div class="temario-title-bar">.*?)(<a href="#audit-{c_id}".*?>Ver Dictamen y Auditoría ↓</a>)'
        replacement = f'\\1<div style="display:flex;gap:8px;flex-wrap:wrap;"><a href="administracion_auditoria.html#{mod_anchor}" class="btn-auditoria-link" style="background:#eff6ff;color:#1e40af;border-color:#93c5fd;font-weight:700;">🔍 Auditoría Plan Actual ({mod_label}) ↗</a> \\2</div>'
        if f'administracion_auditoria.html#{mod_anchor}' not in content:
            content = re.sub(pattern, replacement, content, flags=re.DOTALL)

        # Buscar en la sección de auditoría
        audit_pattern = f'(<div class="audit-card".*?id="audit-{c_id}".*?<div class="audit-actions">.*?)(<a href="#temario-{c_id}" class="btn-goto-temario">Ver Temario Completo y Unidades ↑</a>)'
        audit_replacement = f'\\1<a href="administracion_auditoria.html#{mod_anchor}" class="btn-goto-temario" style="margin-right:12px;color:#d97706;font-weight:700;">🔍 Ver Auditoría de Plan Actual Docente ({mod_label}) ↗</a> \\2'
        if f'administracion_auditoria.html#{mod_anchor}' not in content:
            content = re.sub(audit_pattern, audit_replacement, content, flags=re.DOTALL)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"TSU/index.html actualizado exitosamente en {file_path}")

def update_temarios_por_linea(file_path):
    if not os.path.exists(file_path):
        return
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    mapping = {
        ("b1_fundamentos_administracion", "Módulo 1"): "modulo-1",
        ("b1_planeacion_control_trabajo", "Módulo 2"): "modulo-2",
        ("b2_herramientas_contables", "Módulo 4"): "modulo-4",
        ("b2_administracion_rrhh_sso", "Módulo 3"): "modulo-3",
        ("b3_metodos_produccion", "Módulo 6"): "modulo-6",
        ("b3_servicio_cliente", "Módulo 5"): "modulo-5",
        ("b4_control_calidad", "Módulo 8"): "modulo-8",
        ("b4_fundamentos_marketing", "Módulo 7"): "modulo-7",
    }

    # Banner en temarios_por_linea.html
    banner = """        <!-- BANNER DE AUDITORÍA DOCENTE 2026 -->
        <div style="background: linear-gradient(135deg, #eff6ff 0%, #fefce8 100%); border: 2px solid #3b82f6; border-radius: 10px; padding: 14px 18px; margin: 16px 0 24px 0; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px;">
            <div>
                <span style="background: #2563eb; color: #fff; font-size: 0.72rem; font-weight: 800; padding: 2px 6px; border-radius: 4px; text-transform: uppercase;">Auditoría Docente 2026</span>
                <strong style="color: #0f2d59; font-size: 0.95rem; display: block; margin-top: 2px;">Auditoría Curricular y Dosificación de los 8 Planes de Clase de Administración</strong>
                <p style="font-size: 0.82rem; color: #334155; margin: 0;">Revisión de 40 sesiones anuales (Sergio Ávalos). 28 temas útiles, 18 a actualizar, 16 agregados y 10 eliminados.</p>
            </div>
            <a href="administracion_auditoria.html" style="background: #0f2d59; color: #fff; padding: 8px 14px; border-radius: 6px; font-weight: 700; font-size: 0.82rem; text-decoration: none;">
                💼 Ver Auditoría & Dosificación →
            </a>
        </div>
"""
    if "<!-- BANNER DE AUDITORÍA DOCENTE 2026 -->" not in content and '<section class="linea-section" id="linea-gestion">' in content:
        pos = content.find('<section class="linea-section" id="linea-gestion">')
        end_hdr = content.find('</div>\n        </div>', pos)
        if end_hdr != -1:
            end_pos = end_hdr + len('</div>\n        </div>')
            content = content[:end_pos] + "\n" + banner + content[end_pos:]

    for (c_id, mod_label), mod_anchor in mapping.items():
        pattern = f'(<article class="temario-card" id="{c_id}".*?<div class="temario-title-bar">.*?<h3>.*?</h3>)'
        btn = f' <a href="administracion_auditoria.html#{mod_anchor}" style="background:#eff6ff;color:#1e40af;border:1px solid #93c5fd;font-weight:700;font-size:0.8rem;padding:4px 10px;border-radius:6px;text-decoration:none;">🔍 Auditoría ({mod_label}) ↗</a>'
        if f'administracion_auditoria.html#{mod_anchor}' not in content:
            content = re.sub(pattern, f'\\1{btn}', content, flags=re.DOTALL)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"temarios_por_linea.html actualizado exitosamente en {file_path}")

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    tsu_dir = os.path.join(base_dir, "TSU")
    curricula_dir = os.path.join(base_dir, "curricula-2026", "TSU")
    mybrain_dir = "/Users/arqovalle/Library/CloudStorage/OneDrive-Personal/MyBrain/MyBrain/01 - My Brain/Kinal/TSU"

    # Actualizar TSU/index.html
    idx_path = os.path.join(tsu_dir, "index.html")
    update_tsu_index(idx_path)

    # Actualizar TSU/temarios_por_linea.html
    tpl_path = os.path.join(tsu_dir, "temarios_por_linea.html")
    update_temarios_por_linea(tpl_path)

    # Replicar en curricula-2026/TSU/
    if os.path.exists(curricula_dir):
        shutil.copyfile(idx_path, os.path.join(curricula_dir, "index.html"))
        if os.path.exists(tpl_path):
            shutil.copyfile(tpl_path, os.path.join(curricula_dir, "temarios_por_linea.html"))
        print("Sincronizado a curricula-2026/TSU/")

    # Replicar en MyBrain
    if os.path.exists(mybrain_dir):
        shutil.copyfile(idx_path, os.path.join(mybrain_dir, "index.html"))
        if os.path.exists(tpl_path):
            shutil.copyfile(tpl_path, os.path.join(mybrain_dir, "temarios_por_linea.html"))
        print("Sincronizado a MyBrain/Kinal/TSU/")

if __name__ == "__main__":
    main()
