#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador de Expedientes Curriculares PDF Individuales por Curso / Taller
Fundación Kinal - Escuela Técnica Superior (ETS)
Genera 1 PDF independiente por cada curso/taller de las carreras técnicas de ETS.
"""

import os
import sys
import re

# Inclusión de librerías en scripts/vendor
VENDOR_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "vendor")
if os.path.exists(VENDOR_DIR):
    sys.path.insert(0, VENDOR_DIR)

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, KeepTogether, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(WORKSPACE_DIR, "output", "curricula_2026_cursos_pdfs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

LOGO_PATH = os.path.join(WORKSPACE_DIR, "assets", "escudo_kinal_cuadrado.png")

# Colores Institucionales Kinal
C_KINAL_BLUE = colors.HexColor("#22376D")
C_KINAL_DARK = colors.HexColor("#0F172A")
C_KINAL_GOLD = colors.HexColor("#F59E0B")
C_KINAL_AMBER = colors.HexColor("#D97706")
C_BORDER = colors.HexColor("#CBD5E1")
C_TEXT_DARK = colors.HexColor("#0F172A")
C_TEXT_MUTED = colors.HexColor("#64748B")

STATUS_CONFIG = {
    "keep": {
        "label": "MANTENER",
        "icon": "🟢",
        "bg": colors.HexColor("#F0FDF4"),
        "border": colors.HexColor("#16A34A"),
        "text": colors.HexColor("#15803D"),
    },
    "update": {
        "label": "ACTUALIZAR",
        "icon": "🟡",
        "bg": colors.HexColor("#FEFCE8"),
        "border": colors.HexColor("#EAB308"),
        "text": colors.HexColor("#B45309"),
    },
    "new": {
        "label": "AGREGAR",
        "icon": "🔵",
        "bg": colors.HexColor("#EFF6FF"),
        "border": colors.HexColor("#2563EB"),
        "text": colors.HexColor("#1D4ED8"),
    },
    "delete": {
        "label": "ELIMINAR",
        "icon": "🔴",
        "bg": colors.HexColor("#FEF2F2"),
        "border": colors.HexColor("#DC2626"),
        "text": colors.HexColor("#B91C1C"),
    }
}

class NumberedCanvas(canvas.Canvas):
    """Canvas de dos pasadas para numeración y membrete dinámico"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_decorations(self, page_count):
        self.saveState()
        doc_header = getattr(self, "doc_header_title", "Revisión Curricular 2026")

        # Encabezado superior en páginas 2 en adelante
        if self._pageNumber > 1:
            self.setFont("Helvetica-Bold", 8)
            self.setFillColor(C_KINAL_BLUE)
            self.drawString(36, 758, "FUNDACIÓN KINAL • ESCUELA TÉCNICA SUPERIOR")
            self.setFont("Helvetica", 8)
            self.setFillColor(C_TEXT_MUTED)
            self.drawRightString(576, 758, doc_header[:50])
            self.setStrokeColor(C_BORDER)
            self.setLineWidth(0.5)
            self.line(36, 752, 576, 752)

        # Pie de página en todas las páginas
        self.setStrokeColor(C_BORDER)
        self.setLineWidth(0.5)
        self.line(36, 42, 576, 42)
        
        self.setFont("Helvetica", 7.5)
        self.setFillColor(C_TEXT_MUTED)
        self.drawString(36, 30, "Dirección Académica ETS • Marco DQR 6 / Dual • Nota Mínima Aprobatoria: 75/100 Puntos")
        
        page_str = f"Página {self._pageNumber} de {page_count}"
        self.drawRightString(576, 30, page_str)
        self.restoreState()


def get_styles():
    base = getSampleStyleSheet()
    styles = {
        "DocSubtitle": ParagraphStyle("DocSubtitle", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=10, leading=13, textColor=C_KINAL_BLUE),
        "DocCourseTitle": ParagraphStyle("DocCourseTitle", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=17, leading=21, textColor=C_KINAL_DARK),
        "DocCareerTag": ParagraphStyle("DocCareerTag", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=9.5, leading=12, textColor=C_KINAL_AMBER if hasattr(colors, 'HexColor') else colors.darkgray),
        "DocMeta": ParagraphStyle("DocMeta", parent=base["Normal"], fontName="Helvetica", fontSize=8, leading=11, textColor=C_TEXT_MUTED),
        
        "ModSub": ParagraphStyle("ModSub", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=8, leading=10, textColor=C_KINAL_GOLD),
        "ModTitle": ParagraphStyle("ModTitle", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=11, leading=14, textColor=colors.white),
        "ModLogro": ParagraphStyle("ModLogro", parent=base["Normal"], fontName="Helvetica", fontSize=8, leading=11, textColor=colors.HexColor("#E2E8F0")),
        
        "ItemTitle": ParagraphStyle("ItemTitle", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=8.5, leading=11, textColor=C_TEXT_DARK),
        "ItemCat": ParagraphStyle("ItemCat", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=7, leading=9, textColor=C_TEXT_MUTED),
        "ItemObs": ParagraphStyle("ItemObs", parent=base["Normal"], fontName="Helvetica", fontSize=7.5, leading=10.5, textColor=colors.HexColor("#334155")),
        
        "StatNum": ParagraphStyle("StatNum", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=13, leading=15, alignment=1),
        "StatLbl": ParagraphStyle("StatLbl", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=7, leading=8.5, alignment=1, textColor=C_TEXT_MUTED),
    }
    return styles


def parse_course_data(filepath, pane_id):
    """Extrae con precisión las tarjetas y temas de un curso específico en el HTML"""
    full_path = os.path.join(WORKSPACE_DIR, filepath)
    if not os.path.exists(full_path):
        return []

    with open(full_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Si es standalone (como cad_topografia)
    if pane_id == "general":
        ptext = html
    else:
        # Buscar el bloque del curso
        start_m = re.search(rf'<div[^>]*id=\"course-pane-{pane_id}\"[^>]*>', html)
        if not start_m:
            return []
        start_idx = start_m.start()
        # Buscar siguiente pane o fin de documento
        next_m = re.search(r'<div[^>]*id=\"course-pane-', html[start_idx + len(start_m.group(0)):])
        if next_m:
            end_idx = start_idx + len(start_m.group(0)) + next_m.start()
        else:
            end_idx = len(html)
        ptext = html[start_idx:end_idx]

    # Extraer módulos basados en el encabezado slate-900
    hdr_starts = [m.start() for m in re.finditer(r'<div class=\"bg-slate-900 text-white p-4 border-b border-slate-800\">', ptext)]
    cards = []
    for j, start in enumerate(hdr_starts):
        end = hdr_starts[j+1] if j+1 < len(hdr_starts) else len(ptext)
        card_html = ptext[start:end]

        weeks = re.search(r'<span>(M[ÓO]DULO\s+\d+[^<]*)</span>', card_html, re.IGNORECASE)
        hours = re.search(r'<span>(Duraci[óo]n:[^<]*)</span>', card_html, re.IGNORECASE)
        title = re.search(r'<h4[^>]*>(.*?)</h4>', card_html, re.DOTALL)
        logro = re.search(r'<strong>Logro esperado:</strong>\s*(.*?)</p>', card_html, re.DOTALL)
        if not logro:
            logro = re.search(r'<strong>Correspondencia[^<]*</strong>\s*(.*?)</p>', card_html, re.DOTALL)

        items = []
        item_matches = list(re.finditer(r'<div class=\"(?:content-item|audit-item)\s+item-([a-z]+)[^\"]*\"[^>]*data-(?:status|category)=\"([^\"]*)\">(.*?)(?=<div class=\"(?:content-item|audit-item)|\s*</div>\s*</div>|\Z)', card_html, re.DOTALL))
        for im in item_matches:
            st = im.group(1).lower()
            if st not in STATUS_CONFIG:
                st = "keep"
            ibody = im.group(3)

            t_m = re.search(r'<div class=\"flex justify-between[^\"]*\">(.*?)</div>', ibody, re.DOTALL)
            if t_m:
                spans = re.findall(r'<span[^>]*>(.*?)</span>', t_m.group(1), re.DOTALL)
                ititle = spans[0] if spans else "Tema de Estudio"
                ibadge = spans[1] if len(spans) > 1 else ""
            else:
                ititle = "Tema de Estudio"
                ibadge = ""

            cat_m = re.search(r'<div class=\"text-\[11px\][^\"]*\"[^>]*>(.*?)</div>', ibody, re.DOTALL)
            icat = cat_m.group(1).strip() if cat_m else ""

            p_m = re.search(r'<p[^>]*>(.*?)</p>', ibody, re.DOTALL)
            iobs = p_m.group(1).strip() if p_m else ""

            items.append({
                "status": st,
                "title": re.sub(r'<[^>]+>', '', ititle).strip(),
                "badge": re.sub(r'<[^>]+>', '', ibadge).strip(),
                "category": re.sub(r'<[^>]+>', '', icat).strip(),
                "observation": re.sub(r'<[^>]+>', '', iobs).strip()
            })

        cards.append({
            "weeks": weeks.group(1).strip() if weeks else f"MÓDULO {j+1}",
            "hours": hours.group(1).strip() if hours else "",
            "title": re.sub(r'<[^>]+>', '', title.group(1)).strip() if title else f"Módulo {j+1}",
            "logro": re.sub(r'<[^>]+>', '', logro.group(1)).strip() if logro else "",
            "items": items
        })

    return cards


def build_single_course_pdf(course_info):
    """Genera un PDF independiente para un curso o taller"""
    course_title = course_info["course_title"]
    career_name = course_info["career_name"]
    hours_info = course_info["hours"]
    filename = course_info["filename"]
    pdf_path = os.path.join(OUTPUT_DIR, filename)

    styles = get_styles()
    cards = course_info["cards"]

    # Conteo de temas
    total_modules = len(cards)
    total_items = 0
    counts = {"keep": 0, "update": 0, "new": 0, "delete": 0}

    for m in cards:
        for item in m["items"]:
            total_items += 1
            st = item["status"]
            if st in counts:
                counts[st] += 1

    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=36,
        rightMargin=36,
        topMargin=46,
        bottomMargin=46
    )

    story = []

    # 1. ENCABEZADO INSTITUCIONAL
    logo_cell = ""
    if os.path.exists(LOGO_PATH):
        logo_cell = Image(LOGO_PATH, width=54, height=54)

    text_cell = [
        Paragraph("FUNDACIÓN KINAL • ESCUELA TÉCNICA SUPERIOR", styles["DocSubtitle"]),
        Spacer(1, 1),
        Paragraph(course_title, styles["DocCourseTitle"]),
        Spacer(1, 1.5),
        Paragraph(f"<b>CARRERA:</b> {career_name.upper()} &nbsp;•&nbsp; <b>CARGA HORARIA:</b> {hours_info}", styles["DocCareerTag"]),
        Spacer(1, 2),
        Paragraph(
            "<b>Dossier Técnico de Revisión y Modernización Curricular 2026</b><br/>"
            "Marco Curricular DQR Nivel 6 • Formación Dual en Alternancia • Acreditación Kinal",
            styles["DocMeta"]
        )
    ]

    header_table = Table([[logo_cell, text_cell]], colWidths=[62, 478])
    header_table.setStyle(TableStyle([
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("LEFTPADDING", (0,0), (-1,-1), 0),
        ("RIGHTPADDING", (0,0), (-1,-1), 0),
        ("TOPPADDING", (0,0), (-1,-1), 0),
        ("BOTTOMPADDING", (0,0), (-1,-1), 0),
    ]))
    story.append(header_table)
    story.append(Spacer(1, 7))

    # Línea decorativa
    story.append(HRFlowable(width="100%", thickness=2, color=C_KINAL_BLUE, spaceBefore=2, spaceAfter=8))

    # 2. DASHBOARD DE ESTADÍSTICAS DEL CURSO
    stat_boxes = [
        [
            Paragraph(f"<font color='#15803D'><b>{counts['keep']}</b></font>", styles["StatNum"]),
            Paragraph("MANTENER", styles["StatLbl"])
        ],
        [
            Paragraph(f"<font color='#B45309'><b>{counts['update']}</b></font>", styles["StatNum"]),
            Paragraph("ACTUALIZAR", styles["StatLbl"])
        ],
        [
            Paragraph(f"<font color='#1D4ED8'><b>{counts['new']}</b></font>", styles["StatNum"]),
            Paragraph("NUEVOS / AGREGAR", styles["StatLbl"])
        ],
        [
            Paragraph(f"<font color='#B91C1C'><b>{counts['delete']}</b></font>", styles["StatNum"]),
            Paragraph("ELIMINAR / DEPURAR", styles["StatLbl"])
        ],
        [
            Paragraph(f"<b>{total_items}</b>", styles["StatNum"]),
            Paragraph(f"TOTAL ({total_modules} MÓDULOS)", styles["StatLbl"])
        ]
    ]

    box_cells = []
    for sb in stat_boxes:
        t_box = Table([[sb[0]], [sb[1]]], colWidths=[102])
        t_box.setStyle(TableStyle([
            ("ALIGN", (0,0), (-1,-1), "CENTER"),
            ("TOPPADDING", (0,0), (-1,-1), 3),
            ("BOTTOMPADDING", (0,0), (-1,-1), 3),
            ("BACKGROUND", (0,0), (-1,-1), colors.HexColor("#F8FAFC")),
            ("BOX", (0,0), (-1,-1), 0.5, C_BORDER),
        ]))
        box_cells.append(t_box)

    dash_table = Table([box_cells], colWidths=[108, 108, 108, 108, 108])
    dash_table.setStyle(TableStyle([
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("LEFTPADDING", (0,0), (-1,-1), 2),
        ("RIGHTPADDING", (0,0), (-1,-1), 2),
        ("TOPPADDING", (0,0), (-1,-1), 0),
        ("BOTTOMPADDING", (0,0), (-1,-1), 0),
    ]))
    story.append(dash_table)
    story.append(Spacer(1, 10))

    # 3. TARJETAS MODULARES Y TEMAS AUDITADOS
    for m_idx, card in enumerate(cards):
        card_story = []

        # Encabezado oscuro slate-900 del módulo
        hdr_content = [
            Paragraph(f"{card['weeks'].upper()} {('• ' + card['hours']) if card['hours'] else ''}", styles["ModSub"]),
            Spacer(1, 1),
            Paragraph(card["title"], styles["ModTitle"])
        ]
        if card["logro"]:
            hdr_content.extend([
                Spacer(1, 2),
                Paragraph(f"<b>Logro esperado:</b> {card['logro']}", styles["ModLogro"])
            ])

        hdr_table = Table([[hdr_content]], colWidths=[540])
        hdr_table.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,-1), C_KINAL_DARK),
            ("TOPPADDING", (0,0), (-1,-1), 6),
            ("BOTTOMPADDING", (0,0), (-1,-1), 6),
            ("LEFTPADDING", (0,0), (-1,-1), 10),
            ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ]))
        card_story.append(hdr_table)
        card_story.append(Spacer(1, 3))

        # Items de la tarjeta
        for item in card["items"]:
            st_cfg = STATUS_CONFIG.get(item["status"], STATUS_CONFIG["keep"])
            badge_html = f"<font color='{st_cfg['text'].hexval()}'><b>[{st_cfg['icon']} {st_cfg['label']}]</b></font>"

            item_rows = [
                Paragraph(f"<b>{item['title']}</b> &nbsp;&nbsp; {badge_html}", styles["ItemTitle"])
            ]
            if item["category"]:
                item_rows.append(Paragraph(item["category"].upper(), styles["ItemCat"]))
            if item["observation"]:
                item_rows.append(Paragraph(f"<b>Observación / Justificación:</b> {item['observation']}", styles["ItemObs"]))

            item_table = Table([[item_rows]], colWidths=[540])
            item_table.setStyle(TableStyle([
                ("BACKGROUND", (0,0), (-1,-1), st_cfg["bg"]),
                ("LINELEFT", (0,0), (0,0), 3.5, st_cfg["border"]),
                ("BOX", (0,0), (-1,-1), 0.5, colors.HexColor("#E2E8F0")),
                ("TOPPADDING", (0,0), (-1,-1), 3.5),
                ("BOTTOMPADDING", (0,0), (-1,-1), 3.5),
                ("LEFTPADDING", (0,0), (-1,-1), 8),
                ("RIGHTPADDING", (0,0), (-1,-1), 8),
            ]))
            card_story.append(item_table)
            card_story.append(Spacer(1, 2.5))

        card_story.append(Spacer(1, 6))

        # Mantener juntos el encabezado y los primeros temas
        story.append(KeepTogether(card_story[:3]) if len(card_story) >= 3 else card_story[0])
        for flow in card_story[3:]:
            story.append(flow)

    # Construir con canvas numerado
    class CourseCanvas(NumberedCanvas):
        pass
    CourseCanvas.doc_header_title = f"{course_title} • {career_name}"

    doc.build(story, canvasmaker=CourseCanvas)
    size_kb = os.path.getsize(pdf_path) / 1024
    print(f" PDF generado: {filename} ({size_kb:.1f} KB) | {total_modules} mód. | {total_items} temas.")
    return pdf_path


def main():
    print("==================================================================")
    print(" INICIANDO GENERACIÓN DE 21 DOSSIERS PDF INDIVIDUALES POR CURSO")
    print(" FUNDACIÓN KINAL - ESCUELA TÉCNICA SUPERIOR (ETS)")
    print("==================================================================")

    COURSES_TO_GENERATE = [
        # Dibujo de Construcción (7 cursos/talleres)
        {
            "file": "construccion.html",
            "pane": "fundamentos_construccion",
            "course_title": "Fundamentos de la Construcción y Dibujo Técnico",
            "career_name": "Perito en Dibujo Técnico y de Construcción",
            "hours": "180 Horas",
            "filename": "1_Construccion_Fundamentos_de_la_Construccion.pdf"
        },
        {
            "file": "construccion.html",
            "pane": "administracion_obras",
            "course_title": "Administración y Supervisión de Obras",
            "career_name": "Perito en Dibujo Técnico y de Construcción",
            "hours": "180 Horas",
            "filename": "2_Construccion_Administracion_y_Supervision_de_Obras.pdf"
        },
        {
            "file": "construccion.html",
            "pane": "autocad",
            "course_title": "AutoCAD 2D y Modelado Básico",
            "career_name": "Perito en Dibujo Técnico y de Construcción",
            "hours": "90 Horas",
            "filename": "3_Construccion_AutoCAD_2D_y_Modelado_Basico.pdf"
        },
        {
            "file": "construccion.html",
            "pane": "revit_architecture",
            "course_title": "Revit Architecture y Modelado BIM",
            "career_name": "Perito en Dibujo Técnico y de Construcción",
            "hours": "90 Horas",
            "filename": "4_Construccion_Revit_Architecture_y_Modelado_BIM.pdf"
        },
        {
            "file": "construccion.html",
            "pane": "revit_structure_mep",
            "course_title": "Revit Structure, MEP y Coordinación BIM",
            "career_name": "Perito en Dibujo Técnico y de Construcción",
            "hours": "90 Horas",
            "filename": "5_Construccion_Revit_Structure_MEP_y_Coordinacion.pdf"
        },
        {
            "file": "construccion.html",
            "pane": "civil_3d",
            "course_title": "Civil 3D y Topografía Digital",
            "career_name": "Perito en Dibujo Técnico y de Construcción",
            "hours": "90 Horas",
            "filename": "6_Construccion_Civil_3D_y_Topografia_Digital.pdf"
        },
        {
            "file": "cad_topografia_auditoria.html",
            "pane": "general",
            "course_title": "CAD para Topografía (Civil 3D)",
            "career_name": "Especialidad en Topografía y Construcción",
            "hours": "90 Horas",
            "filename": "7_Construccion_CAD_para_Topografia_Civil_3D.pdf"
        },

        # Electricidad Industrial (5 cursos/talleres)
        {
            "file": "electricidad.html",
            "pane": "instalaciones_electricas",
            "course_title": "Instalaciones Eléctricas Industriales",
            "career_name": "Perito en Electricidad Industrial",
            "hours": "180 Horas",
            "filename": "8_Electricidad_Instalaciones_Electricas_Industriales.pdf"
        },
        {
            "file": "electricidad.html",
            "pane": "controles_maquinas",
            "course_title": "Controles y Máquinas Eléctricas",
            "career_name": "Perito en Electricidad Industrial",
            "hours": "180 Horas",
            "filename": "9_Electricidad_Controles_y_Maquinas_Electricas.pdf"
        },
        {
            "file": "electricidad.html",
            "pane": "electronica_analogica",
            "course_title": "Electrónica Analógica y Digital",
            "career_name": "Perito en Electricidad Industrial",
            "hours": "180 Horas",
            "filename": "10_Electricidad_Electronica_Analogica_y_Digital.pdf"
        },
        {
            "file": "electricidad.html",
            "pane": "control_programables",
            "course_title": "Controladores Lógicos Programables (PLC)",
            "career_name": "Perito en Electricidad Industrial",
            "hours": "180 Horas",
            "filename": "11_Electricidad_Controladores_Logicos_Programables_PLC.pdf"
        },
        {
            "file": "electricidad.html",
            "pane": "automatizacion_industrial",
            "course_title": "Automatización Industrial y Redes de Comunicación",
            "career_name": "Perito en Electricidad Industrial",
            "hours": "180 Horas",
            "filename": "12_Electricidad_Automatizacion_Industrial_y_Redes.pdf"
        },

        # Mecánica Industrial (3 cursos/talleres)
        {
            "file": "mecanica.html",
            "pane": "mantenimiento_mecanico",
            "course_title": "Mantenimiento Mecánico Industrial y Mecánica de Banco",
            "career_name": "Perito en Mecánica Industrial",
            "hours": "180 Horas",
            "filename": "13_Mecanica_Mantenimiento_Mecanico_Industrial_y_Banco.pdf"
        },
        {
            "file": "mecanica.html",
            "pane": "soldadura_industrial",
            "course_title": "Soldadura Industrial y Procesos de Unión",
            "career_name": "Perito en Mecánica Industrial",
            "hours": "180 Horas",
            "filename": "14_Mecanica_Soldadura_Industrial_y_Procesos_de_Union.pdf"
        },
        {
            "file": "mecanica.html",
            "pane": "calderas_vapor",
            "course_title": "Calderas de Vapor y Máquinas Térmicas",
            "career_name": "Perito en Mecánica Industrial",
            "hours": "90 Horas",
            "filename": "15_Mecanica_Calderas_de_Vapor_y_Maquinas_Termicas.pdf"
        },

        # Mecánica Automotriz (6 cursos/talleres)
        {
            "file": "automotriz.html",
            "pane": "motores_gasolina",
            "course_title": "Mecánica de Motores de Gasolina",
            "career_name": "Perito en Mecánica Automotriz",
            "hours": "180 Horas",
            "filename": "16_Automotriz_Mecanica_de_Motores_de_Gasolina.pdf"
        },
        {
            "file": "automotriz.html",
            "pane": "mecanismos_automovil",
            "course_title": "Mecanismos del Automóvil (Chasis y Frenos)",
            "career_name": "Perito en Mecánica Automotriz",
            "hours": "180 Horas",
            "filename": "17_Automotriz_Mecanismos_del_Automovil.pdf"
        },
        {
            "file": "automotriz.html",
            "pane": "electromecanica_automotriz",
            "course_title": "Electromecánica Automotriz",
            "career_name": "Perito en Mecánica Automotriz",
            "hours": "180 Horas",
            "filename": "18_Automotriz_Electromecanica_Automotriz.pdf"
        },
        {
            "file": "automotriz.html",
            "pane": "inyeccion_electronica",
            "course_title": "Inyección Electrónica Automotriz (Gasolina y Diésel)",
            "career_name": "Perito en Mecánica Automotriz",
            "hours": "180 Horas",
            "filename": "19_Automotriz_Inyeccion_Electronica_Automotriz.pdf"
        },
        {
            "file": "automotriz.html",
            "pane": "aire_acondicionado",
            "course_title": "Aire Acondicionado Automotriz y Climatización",
            "career_name": "Perito en Mecánica Automotriz",
            "hours": "90 Horas",
            "filename": "20_Automotriz_Aire_Acondicionado_Automotriz.pdf"
        },
        {
            "file": "automotriz.html",
            "pane": "mecanica_motocicletas",
            "course_title": "Mecánica y Mantenimiento de Motocicletas",
            "career_name": "Perito en Mecánica Automotriz",
            "hours": "90 Horas",
            "filename": "21_Automotriz_Mecanica_y_Mantenimiento_de_Motocicletas.pdf"
        }
    ]

    generated = []
    for cinfo in COURSES_TO_GENERATE:
        cards = parse_course_data(cinfo["file"], cinfo["pane"])
        cinfo["cards"] = cards
        pdf_path = build_single_course_pdf(cinfo)
        generated.append((cinfo["course_title"], cinfo["filename"], pdf_path, len(cards), sum(len(cd["items"]) for cd in cards)))

    print("\n==================================================================")
    print(f" TOTAL: {len(generated)} DOSSIERS PDF GENERADOS SATISFACTORIAMENTE")
    print("==================================================================")
    for title, fname, path, n_mods, n_it in generated:
        sz = os.path.getsize(path) / 1024
        print(f"• {fname:55} | {sz:5.1f} KB | {n_mods:2} mód | {n_it:3} temas")

if __name__ == "__main__":
    main()
