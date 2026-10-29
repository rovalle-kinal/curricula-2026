#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador Maestro de Dossiers PDF de Revisión Curricular 2026 por Carrera
Fundación Kinal - Escuela Técnica Superior (ETS)
"""

import os
import sys
import re

# Agregar librerías de scripts/vendor al path
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
OUTPUT_DIR = os.path.join(WORKSPACE_DIR, "output", "curricula_2026_pdfs")
os.makedirs(OUTPUT_DIR, exist_ok=True)

LOGO_PATH = os.path.join(WORKSPACE_DIR, "assets", "escudo_kinal_cuadrado.png")

# Paleta de Colores Institucional
C_KINAL_BLUE = colors.HexColor("#22376D")
C_KINAL_DARK = colors.HexColor("#0F172A")
C_KINAL_SLATE = colors.HexColor("#1E293B")
C_KINAL_AMBER = colors.HexColor("#D97706")
C_KINAL_GOLD = colors.HexColor("#F59E0B")
C_BORDER = colors.HexColor("#CBD5E1")
C_TEXT_DARK = colors.HexColor("#0F172A")
C_TEXT_MUTED = colors.HexColor("#64748B")

# Colores de Dictamen / Estado
STATUS_CONFIG = {
    "keep": {
        "label": "MANTENER",
        "icon": "🟢",
        "bg": colors.HexColor("#F0FDF4"),
        "border": colors.HexColor("#16A34A"),
        "text": colors.HexColor("#15803D"),
        "badge_bg": colors.HexColor("#DCFCE7")
    },
    "update": {
        "label": "ACTUALIZAR",
        "icon": "🟡",
        "bg": colors.HexColor("#FEFCE8"),
        "border": colors.HexColor("#EAB308"),
        "text": colors.HexColor("#B45309"),
        "badge_bg": colors.HexColor("#FEF08A")
    },
    "new": {
        "label": "AGREGAR",
        "icon": "🔵",
        "bg": colors.HexColor("#EFF6FF"),
        "border": colors.HexColor("#2563EB"),
        "text": colors.HexColor("#1D4ED8"),
        "badge_bg": colors.HexColor("#DBEAFE")
    },
    "delete": {
        "label": "ELIMINAR",
        "icon": "🔴",
        "bg": colors.HexColor("#FEF2F2"),
        "border": colors.HexColor("#DC2626"),
        "text": colors.HexColor("#B91C1C"),
        "badge_bg": colors.HexColor("#FEE2E2")
    }
}

class NumberedCanvas(canvas.Canvas):
    """Canvas de dos pasadas para numeración dinámica y membrete institucional"""
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
        career_title = getattr(self, "career_title", "Revisión Curricular 2026")

        # Encabezado corriente (páginas 2 en adelante)
        if self._pageNumber > 1:
            self.setFont("Helvetica-Bold", 8)
            self.setFillColor(C_KINAL_BLUE)
            self.drawString(36, 758, "FUNDACIÓN KINAL • ESCUELA TÉCNICA SUPERIOR")
            self.setFont("Helvetica", 8)
            self.setFillColor(C_TEXT_MUTED)
            self.drawRightString(576, 758, career_title[:45])
            self.setStrokeColor(C_BORDER)
            self.setLineWidth(0.5)
            self.line(36, 752, 576, 752)

        # Pie de página corriente (todas las páginas)
        self.setStrokeColor(C_BORDER)
        self.setLineWidth(0.5)
        self.line(36, 42, 576, 42)
        
        self.setFont("Helvetica", 7.5)
        self.setFillColor(C_TEXT_MUTED)
        self.drawString(36, 30, "Dirección Académica ETS • Marco DQR 6 / Dual • Nota Mínima: 75/100 Puntos")
        
        page_str = f"Página {self._pageNumber} de {page_count}"
        self.drawRightString(576, 30, page_str)
        self.restoreState()


def get_styles():
    base = getSampleStyleSheet()
    styles = {
        "DocTitle": ParagraphStyle("DocTitle", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=18, leading=22, textColor=C_KINAL_DARK),
        "DocSubtitle": ParagraphStyle("DocSubtitle", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=10.5, leading=13, textColor=C_KINAL_BLUE),
        "DocMeta": ParagraphStyle("DocMeta", parent=base["Normal"], fontName="Helvetica", fontSize=8, leading=11, textColor=C_TEXT_MUTED),
        
        "BannerTitle": ParagraphStyle("BannerTitle", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=12, leading=15, textColor=colors.white),
        "BannerSub": ParagraphStyle("BannerSub", parent=base["Normal"], fontName="Helvetica", fontSize=8, leading=10.5, textColor=colors.HexColor("#FDE68A")),
        
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


def parse_html_page(filepath, default_course_title="Curso Técnico"):
    """Extrae cursos, módulos y temas con observaciones pedagógicas de los archivos HTML"""
    if not os.path.exists(filepath):
        return []
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    # Detectar panes de curso
    pane_matches = list(re.finditer(r'<div[^>]*id=\"course-pane-([^\"]+)\"[^>]*>', html))
    if not pane_matches:
        panes_data = [("general", html)]
    else:
        panes_data = []
        for i, m in enumerate(pane_matches):
            pid = m.group(1)
            start = m.start()
            end = pane_matches[i+1].start() if i+1 < len(pane_matches) else len(html)
            panes_data.append((pid, html[start:end]))

    courses = []
    for pid, ptext in panes_data:
        # Título del curso
        ctitle_m = re.search(r'<h[123][^>]*>(.*?)</h[123]>', ptext[:2500])
        ctitle = re.sub(r'<[^>]+>', '', ctitle_m.group(1)).strip() if ctitle_m else default_course_title
        if "Matriz" in ctitle or "Sección" in ctitle or not ctitle:
            ctitle = default_course_title

        # Horas del curso
        hrs_m = re.search(r'(\d+\s*Horas)', ptext[:3000], re.IGNORECASE)
        chours = hrs_m.group(1).strip() if hrs_m else ""

        # Módulos (cabeceras oscuras)
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

        courses.append({
            "course_id": pid,
            "course_title": ctitle,
            "course_hours": chours,
            "cards": cards
        })
    return courses


def build_career_pdf(career_dict):
    """Construye un documento PDF de alta calidad editorial para una carrera"""
    pdf_filename = career_dict["filename"]
    pdf_path = os.path.join(OUTPUT_DIR, pdf_filename)
    styles = get_styles()

    # Calcular estadísticas globales
    total_courses = len(career_dict["courses"])
    total_modules = sum(len(c["cards"]) for c in career_dict["courses"])
    total_items = 0
    counts = {"keep": 0, "update": 0, "new": 0, "delete": 0}

    for c in career_dict["courses"]:
        for m in c["cards"]:
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

    # 1. ENCABEZADO INSTITUCIONAL DE PRIMERA PÁGINA
    logo_cell = ""
    if os.path.exists(LOGO_PATH):
        logo_cell = Image(LOGO_PATH, width=52, height=52)

    text_cell = [
        Paragraph("FUNDACIÓN KINAL • ESCUELA TÉCNICA SUPERIOR (ETS)", styles["DocSubtitle"]),
        Spacer(1, 1),
        Paragraph(career_dict["title"], styles["DocTitle"]),
        Spacer(1, 2),
        Paragraph(
            "<b>Expediente Técnico de Revisión y Modernización Curricular 2026</b><br/>"
            "Marco Curricular DQR Nivel 6 • Formación Dual en Alternancia • Estándares Industriales y Normativa Nacional",
            styles["DocMeta"]
        )
    ]

    header_table = Table([[logo_cell, text_cell]], colWidths=[60, 480])
    header_table.setStyle(TableStyle([
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("LEFTPADDING", (0,0), (-1,-1), 0),
        ("RIGHTPADDING", (0,0), (-1,-1), 0),
        ("TOPPADDING", (0,0), (-1,-1), 0),
        ("BOTTOMPADDING", (0,0), (-1,-1), 0),
    ]))
    story.append(header_table)
    story.append(Spacer(1, 8))

    # Línea decorativa bicolor
    story.append(HRFlowable(width="100%", thickness=2, color=C_KINAL_BLUE, spaceBefore=2, spaceAfter=8))

    # 2. TABLERO DE RESUMEN EJECUTIVO (METRICS DASHBOARD)
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
            Paragraph(f"TOTAL TEMAS ({total_modules} MÓD.)", styles["StatLbl"])
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
    story.append(Spacer(1, 12))

    # 3. CURSOS, TARJETAS Y CONTENIDOS DETALLADOS
    for c_idx, course in enumerate(career_dict["courses"]):
        course_name = course["course_title"]
        course_hrs = course["course_hours"]
        n_cards = len(course["cards"])
        n_items = sum(len(cd["items"]) for cd in course["cards"])

        # Separador / Encabezado de Curso
        c_banner_cells = [
            Paragraph(f"<b>CURSO {c_idx+1}: {course_name.upper()}</b>", styles["BannerTitle"]),
            Paragraph(f"Carga: {course_hrs or '180 Horas'} • {n_cards} Módulos • {n_items} Temas Auditados", styles["BannerSub"])
        ]
        c_banner_table = Table([[c_banner_cells]], colWidths=[540])
        c_banner_table.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,-1), C_KINAL_BLUE),
            ("TOPPADDING", (0,0), (-1,-1), 5),
            ("BOTTOMPADDING", (0,0), (-1,-1), 5),
            ("LEFTPADDING", (0,0), (-1,-1), 10),
            ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ]))
        story.append(c_banner_table)
        story.append(Spacer(1, 8))

        # Iterar sobre las tarjetas de módulo
        for m_idx, card in enumerate(course["cards"]):
            card_story = []

            # Encabezado oscuro slate-900 del Módulo
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

            # Filas de Temas / Items
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
            story.append(KeepTogether(card_story[:3]) if len(card_story) >= 3 else card_story[0])
            for flow in card_story[3:]:
                story.append(flow)

        story.append(Spacer(1, 8))

    # Construir PDF usando NumberedCanvas
    class CareerCanvas(NumberedCanvas):
        pass
    CareerCanvas.career_title = career_dict["title"]

    doc.build(story, canvasmaker=CareerCanvas)
    file_size_kb = os.path.getsize(pdf_path) / 1024
    print(f" PDF generado: {pdf_filename} ({file_size_kb:.1f} KB) con {total_modules} módulos y {total_items} temas.")
    return pdf_path


def main():
    print("================================================================")
    print(" INICIANDO GENERACIÓN DE DOSSIERS CURRICULARES PDF KINAL 2026")
    print("================================================================")

    # Definir datos y carreras
    carreras = [
        {
            "id": "construccion",
            "title": "Perito en Dibujo Técnico y de Construcción",
            "filename": "1_Revision_Curricular_Dibujo_de_Construccion_2026.pdf",
            "sources": [
                ("construccion.html", "Dibujo de Construcción"),
                ("cad_topografia_auditoria.html", "CAD para Topografía (Civil 3D)")
            ]
        },
        {
            "id": "electricidad",
            "title": "Perito en Electricidad Industrial",
            "filename": "2_Revision_Curricular_Electricidad_Industrial_2026.pdf",
            "sources": [
                ("electricidad.html", "Electricidad Industrial")
            ]
        },
        {
            "id": "mecanica",
            "title": "Perito en Mecánica Industrial",
            "filename": "3_Revision_Curricular_Mecanica_Industrial_2026.pdf",
            "sources": [
                ("mecanica.html", "Mecánica Industrial")
            ]
        },
        {
            "id": "automotriz",
            "title": "Perito en Mecánica Automotriz",
            "filename": "4_Revision_Curricular_Mecanica_Automotriz_2026.pdf",
            "sources": [
                ("automotriz.html", "Mecánica Automotriz")
            ]
        },
        {
            "id": "tsu",
            "title": "Técnico Superior Universitario (TSU)",
            "filename": "5_Revision_Curricular_Tecnico_Superior_Universitario_TSU_2026.pdf",
            "sources": [
                ("TSU/administracion_auditoria.html", "Línea de Administración y Gestión Empresarial"),
                ("TSU/etica_auditoria.html", "Línea de Ética y Responsabilidad Social"),
                ("TSU/matematica_auditoria.html", "Línea de Matemática Aplicada")
            ]
        },
        {
            "id": "cad_topografia",
            "title": "CAD para Topografía (Civil 3D)",
            "filename": "6_Revision_Curricular_CAD_para_Topografia_2026.pdf",
            "sources": [
                ("cad_topografia_auditoria.html", "CAD para Topografía (Civil 3D)")
            ]
        }
    ]

    generated_pdfs = []
    for c in carreras:
        print(f"\nProcesando: {c['title']}...")
        all_courses = []
        for src_rel, def_title in c["sources"]:
            src_path = os.path.join(WORKSPACE_DIR, src_rel)
            parsed_courses = parse_html_page(src_path, default_course_title=def_title)
            all_courses.extend(parsed_courses)

        c["courses"] = all_courses
        pdf_path = build_career_pdf(c)
        generated_pdfs.append((c["title"], c["filename"], pdf_path))

    print("\n================================================================")
    print(f" RESUMEN: {len(generated_pdfs)} PDFs GENERADOS CON ÉXITO")
    print("================================================================")
    for title, fname, p in generated_pdfs:
        print(f"• {title}: {p} ({os.path.getsize(p)/1024:.1f} KB)")

if __name__ == "__main__":
    main()
