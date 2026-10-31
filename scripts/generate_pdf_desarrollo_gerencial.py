#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador de Documento PDF Institucional:
Programa de Desarrollo Gerencial y Vinculación Empresarial
Diplomado Mandos Medios: Formación Aplicada para Mandos Medios y Supervisores
Escuela Técnica Superior — Fundación Kinal | Avalado por la Universidad del Istmo
"""

import os
import sys

# Agregar scripts/vendor al path
VENDOR_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "vendor")
if os.path.exists(VENDOR_DIR):
    sys.path.insert(0, VENDOR_DIR)

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, HRFlowable, PageBreak, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COURSE_DIR = os.path.join(WORKSPACE_DIR, "Cursos", "Desarrollo_Gerencial_Vinculacion_Empresarial")
LOGO_PATH = os.path.join(WORKSPACE_DIR, "assets", "escudo_kinal_cuadrado.png")

# Colores Institucionales Kinal
C_KINAL_BLUE = colors.HexColor("#003366")
C_KINAL_NAVY = colors.HexColor("#22376D")
C_KINAL_DARK = colors.HexColor("#0F172A")
C_KINAL_SLATE = colors.HexColor("#1E293B")
C_KINAL_GOLD = colors.HexColor("#D97706")
C_KINAL_AMBER = colors.HexColor("#F59E0B")
C_BORDER = colors.HexColor("#CBD5E1")
C_BG_LIGHT = colors.HexColor("#F8FAFC")
C_TEXT_MUTED = colors.HexColor("#64748B")

class NumberedCanvas(canvas.Canvas):
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
        # Encabezado superior en páginas 2 en adelante
        if self._pageNumber > 1:
            self.setFont("Helvetica-Bold", 8)
            self.setFillColor(C_KINAL_NAVY)
            self.drawString(36, 756, "FUNDACIÓN KINAL • ESCUELA TÉCNICA SUPERIOR")
            self.setFont("Helvetica", 8)
            self.setFillColor(C_TEXT_MUTED)
            self.drawRightString(576, 756, "Diplomado Mandos Medios • Avalado por UNIS")
            self.setStrokeColor(C_BORDER)
            self.setLineWidth(0.5)
            self.line(36, 750, 576, 750)

        # Pie de página en todas las páginas
        self.setStrokeColor(C_BORDER)
        self.setLineWidth(0.5)
        self.line(36, 42, 576, 42)
        
        self.setFont("Helvetica", 7.5)
        self.setFillColor(C_TEXT_MUTED)
        self.drawString(36, 30, "Escuela Técnica Superior — KINAL | Avalado por la Universidad del Istmo • Nota Mínima: 75/100 Puntos")
        
        page_str = f"Página {self._pageNumber} de {page_count}"
        self.drawRightString(576, 30, page_str)
        self.restoreState()


def get_styles():
    base = getSampleStyleSheet()
    styles = {
        "DocTitle": ParagraphStyle("DocTitle", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=15, leading=18, textColor=C_KINAL_NAVY),
        "DocSub": ParagraphStyle("DocSub", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=9.5, leading=12, textColor=C_KINAL_GOLD),
        "DocMeta": ParagraphStyle("DocMeta", parent=base["Normal"], fontName="Helvetica", fontSize=7.5, leading=10, textColor=C_TEXT_MUTED),
        
        "H1": ParagraphStyle("H1", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=10.5, leading=13, textColor=C_KINAL_NAVY, spaceBefore=6, spaceAfter=2),
        "H2": ParagraphStyle("H2", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=8.5, leading=11, textColor=C_KINAL_DARK, spaceBefore=4, spaceAfter=2),
        
        "Body": ParagraphStyle("Body", parent=base["Normal"], fontName="Helvetica", fontSize=7.2, leading=9.5, textColor=C_KINAL_DARK),
        "BodyBold": ParagraphStyle("BodyBold", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=7.2, leading=9.5, textColor=C_KINAL_DARK),
        
        "BannerTitle": ParagraphStyle("BannerTitle", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=9.5, leading=12, textColor=colors.white),
        "BannerSub": ParagraphStyle("BannerSub", parent=base["Normal"], fontName="Helvetica", fontSize=7.2, leading=9, textColor=colors.HexColor("#FDE68A")),
        
        "TableHead": ParagraphStyle("TableHead", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=7, leading=9, textColor=colors.white, alignment=1),
        "TableCell": ParagraphStyle("TableCell", parent=base["Normal"], fontName="Helvetica", fontSize=6.7, leading=8.6, textColor=C_KINAL_DARK),
        "TableCellBold": ParagraphStyle("TableCellBold", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=6.7, leading=8.6, textColor=C_KINAL_DARK),
        "TableCellCenter": ParagraphStyle("TableCellCenter", parent=base["Normal"], fontName="Helvetica", fontSize=6.7, leading=8.6, textColor=C_KINAL_DARK, alignment=1),
        
        "CalloutText": ParagraphStyle("CalloutText", parent=base["Normal"], fontName="Helvetica", fontSize=7, leading=9.3, textColor=C_KINAL_DARK),
        "CalloutBold": ParagraphStyle("CalloutBold", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=7.2, leading=9.5, textColor=C_KINAL_NAVY),
        
        "StatNum": ParagraphStyle("StatNum", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=11, leading=13, alignment=1, textColor=C_KINAL_NAVY),
        "StatLbl": ParagraphStyle("StatLbl", parent=base["Normal"], fontName="Helvetica-Bold", fontSize=6.5, leading=8, alignment=1, textColor=C_TEXT_MUTED),
    }
    return styles


def build_pdf():
    os.makedirs(COURSE_DIR, exist_ok=True)
    target_path = os.path.join(COURSE_DIR, "programa_formativo_desarrollo_gerencial.pdf")
    doc = SimpleDocTemplate(target_path, pagesize=letter, leftMargin=36, rightMargin=36, topMargin=44, bottomMargin=48)
    styles = get_styles()

    story = []

    # 1. ENCABEZADO INSTITUCIONAL
    logo_cell = ""
    if os.path.exists(LOGO_PATH):
        logo_cell = Image(LOGO_PATH, width=50, height=50)

    header_text = [
        Paragraph("ESCUELA TÉCNICA SUPERIOR — KINAL &bull; CRONOGRAMA OFICIAL", styles["DocSub"]),
        Spacer(1, 1),
        Paragraph("Programa de Desarrollo Gerencial y Vinculación Empresarial", styles["DocTitle"]),
        Spacer(1, 1),
        Paragraph("<b>DIPLOMADO MANDOS MEDIOS: FORMACIÓN APLICADA PARA MANDOS MEDIOS Y SUPERVISORES</b>", styles["BodyBold"]),
        Paragraph("Avalado por la Universidad del Istmo (UNIS) &bull; Formación Dual &bull; Marco DQR 6 &bull; Nota Mínima: 75/100 Puntos", styles["DocMeta"])
    ]

    header_table = Table([[logo_cell, header_text]], colWidths=[58, 482])
    header_table.setStyle(TableStyle([
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("LEFTPADDING", (0,0), (-1,-1), 0),
        ("RIGHTPADDING", (0,0), (-1,-1), 0),
        ("TOPPADDING", (0,0), (-1,-1), 0),
        ("BOTTOMPADDING", (0,0), (-1,-1), 0),
    ]))
    story.append(header_table)
    story.append(Spacer(1, 5))
    story.append(HRFlowable(width="100%", thickness=1.5, color=C_KINAL_NAVY, spaceBefore=1, spaceAfter=6))

    # 2. DASHBOARD DE MÉTRICAS EJECUTIVAS
    dash_data = [
        [
            Paragraph("<b>4 SESIONES</b>", styles["StatNum"]),
            Paragraph("8 Horas Sincrónicas", styles["StatLbl"])
        ],
        [
            Paragraph("<b>HÍBRIDO</b>", styles["StatNum"]),
            Paragraph("2 Presenciales + 2 Virtuales", styles["StatLbl"])
        ],
        [
            Paragraph("<b>&ge; 75 PTS</b>", styles["StatNum"]),
            Paragraph("Umbral Aprobatorio", styles["StatLbl"])
        ],
        [
            Paragraph("<b>ETS &bull; UNIS</b>", styles["StatNum"]),
            Paragraph("Acreditación Universitaria", styles["StatLbl"])
        ],
        [
            Paragraph("<b>MANDOS MEDIOS</b>", styles["StatNum"]),
            Paragraph("Supervisores y Jefes", styles["StatLbl"])
        ]
    ]

    box_cells = []
    for d in dash_data:
        tb = Table([[d[0]], [d[1]]], colWidths=[102])
        tb.setStyle(TableStyle([
            ("ALIGN", (0,0), (-1,-1), "CENTER"),
            ("TOPPADDING", (0,0), (-1,-1), 2),
            ("BOTTOMPADDING", (0,0), (-1,-1), 2),
            ("BACKGROUND", (0,0), (-1,-1), C_BG_LIGHT),
            ("BOX", (0,0), (-1,-1), 0.5, C_BORDER),
        ]))
        box_cells.append(tb)

    dash_table = Table([box_cells], colWidths=[108, 108, 108, 108, 108])
    dash_table.setStyle(TableStyle([
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("LEFTPADDING", (0,0), (-1,-1), 2),
        ("RIGHTPADDING", (0,0), (-1,-1), 2),
        ("TOPPADDING", (0,0), (-1,-1), 0),
        ("BOTTOMPADDING", (0,0), (-1,-1), 0),
    ]))
    story.append(dash_table)
    story.append(Spacer(1, 7))

    # 3. CRONOGRAMA OFICIAL Y PROGRAMACIÓN DE SESIONES (TABLA EXACTA)
    story.append(Paragraph("1. Calendario y Programación Oficial de Sesiones", styles["H1"]))
    story.append(Paragraph("Estructura ejecutiva de 4 sesiones diseñada para fortalecer el liderazgo operativo, la retención de personal técnico y el manejo eficiente de equipos en talleres y plantas industriales.", styles["Body"]))
    story.append(Spacer(1, 3))

    crono_rows = [
        [
            Paragraph("<b>Sesión</b>", styles["TableHead"]),
            Paragraph("<b>Fecha</b>", styles["TableHead"]),
            Paragraph("<b>Horario</b>", styles["TableHead"]),
            Paragraph("<b>Modalidad</b>", styles["TableHead"]),
            Paragraph("<b>Módulo / Tema</b>", styles["TableHead"]),
            Paragraph("<b>Dinámica y Enfoque Operativo</b>", styles["TableHead"])
        ],
        [
            Paragraph("<b>Sesión 1</b>", styles["TableCellBold"]),
            Paragraph("Martes 3 de noviembre", styles["TableCellBold"]),
            Paragraph("2:00 p. m. a 4:00 p. m.", styles["TableCellCenter"]),
            Paragraph("<font color='#059669'><b>PRESENCIAL</b></font><br/>(Campus Kinal)", styles["TableCellCenter"]),
            Paragraph("<b>Inteligencia Emocional &ndash; Factor Humano</b>", styles["TableCellBold"]),
            Paragraph("<b>Apertura vivencial:</b> potencias del alma (inteligencia y voluntad), CI vs autogobierno emocional y <b>recorrido por talleres y laboratorios de formación técnica ETS Kinal</b>.", styles["TableCell"])
        ],
        [
            Paragraph("<b>Sesión 2</b>", styles["TableCellBold"]),
            Paragraph("Martes 10 de noviembre", styles["TableCellBold"]),
            Paragraph("2:00 p. m. a 4:00 p. m.", styles["TableCellCenter"]),
            Paragraph("<font color='#2563EB'><b>VIRTUAL</b></font><br/>(Microsoft Teams)", styles["TableCellCenter"]),
            Paragraph("<b>Manejo de Personal y Mandos Medios</b>", styles["TableCellBold"]),
            Paragraph("<b>Herramientas de campo:</b> Plantilla Onboarding 30-60-90, Guía de Bolsillo Micro-Charla 7 min, Matriz de Hábitos de Confianza y Ruta de Desescalamiento 1-a-1.", styles["TableCell"])
        ],
        [
            Paragraph("<b>Sesión 3</b>", styles["TableCellBold"]),
            Paragraph("Martes 17 de noviembre", styles["TableCellBold"]),
            Paragraph("2:00 p. m. a 4:00 p. m.", styles["TableCellCenter"]),
            Paragraph("<font color='#2563EB'><b>VIRTUAL</b></font><br/>(Microsoft Teams)", styles["TableCellCenter"]),
            Paragraph("<b>Fortalecimiento de Competencias Técnicas</b>", styles["TableCellBold"]),
            Paragraph("<b>Continuidad aplicada:</b> Diagnóstico de brechas en piso, diseño de Matriz de Polivalencia (Skills Matrix), entrenamiento cruzado y estandarización de POEs.", styles["TableCell"])
        ],
        [
            Paragraph("<b>Sesión 4</b>", styles["TableCellBold"]),
            Paragraph("Martes 24 de noviembre", styles["TableCellBold"]),
            Paragraph("2:00 p. m. a 4:00 p. m.", styles["TableCellCenter"]),
            Paragraph("<font color='#059669'><b>PRESENCIAL</b></font><br/>(Campus Kinal)", styles["TableCellCenter"]),
            Paragraph("<b>Rotación de Personal y Cierre Estratégico</b>", styles["TableCellBold"]),
            Paragraph("<b>Cierre vivencial:</b> Salario emocional, retención de talento, presentación de planes de acción aplicados, alianza Kinal-UNIS y entrega solemne de diplomas.", styles["TableCell"])
        ]
    ]

    crono_table = Table(crono_rows, colWidths=[42, 80, 72, 68, 128, 150])
    crono_table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), C_KINAL_NAVY),
        ("GRID", (0,0), (-1,-1), 0.5, C_BORDER),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING", (0,0), (-1,-1), 3),
        ("BOTTOMPADDING", (0,0), (-1,-1), 3),
        ("LEFTPADDING", (0,0), (-1,-1), 4),
        ("RIGHTPADDING", (0,0), (-1,-1), 4),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, C_BG_LIGHT]),
    ]))
    story.append(crono_table)
    story.append(Spacer(1, 6))

    # BANNER DUAL Y VINCULACIÓN ACADÉMICA
    callout_dual = [
        [
            Paragraph("<b>DINÁMICA DE APERTURA Y CIERRE PRESENCIAL (SESIONES 1 Y 4)</b>", styles["CalloutBold"]),
            Paragraph("<b>CONTINUIDAD VIRTUAL APLICADA (SESIONES 2 Y 3)</b>", styles["CalloutBold"])
        ],
        [
            Paragraph("Se imparten en el campus de KINAL para facilitar dinámicas vivenciales de integración de mandos medios y permitir el recorrido por talleres y laboratorios de formación técnica.", styles["CalloutText"]),
            Paragraph("Se desarrollan en modalidad virtual sincrónica (Microsoft Teams), orientadas a la entrega y aplicación inmediata de herramientas de campo (onboarding, micro-charlas y diagnóstico de brechas técnicas).", styles["CalloutText"])
        ]
    ]
    t_dual = Table(callout_dual, colWidths=[265, 265])
    t_dual.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), colors.HexColor("#EFF6FF")),
        ("BOX", (0,0), (-1,-1), 0.5, colors.HexColor("#93C5FD")),
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("TOPPADDING", (0,0), (-1,-1), 3),
        ("BOTTOMPADDING", (0,0), (-1,-1), 3),
        ("LEFTPADDING", (0,0), (-1,-1), 6),
        ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ]))
    story.append(t_dual)
    story.append(Spacer(1, 5))

    # CALLOUT TÉCNICO UNIVERSITARIO (KINAL)
    callout_tu = [
        [
            Paragraph(
                "<b>EL TÉCNICO UNIVERSITARIO (KINAL): VINCULACIÓN EMPRESA-ACADEMIA</b><br/>"
                "Este diplomado permite a los líderes de empresa conocer de primera mano el modelo educativo del <b>Técnico Universitario de KINAL (avalado por la Universidad del Istmo)</b>, un programa de tres años enfocado en preparar mandos medios capaces de dirigir procesos técnicos y personas con rigor operativo, criterio ético y liderazgo humano.",
                styles["CalloutText"]
            )
        ]
    ]
    t_tu = Table(callout_tu, colWidths=[540])
    t_tu.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), colors.HexColor("#FEF3C7")),
        ("LINELEFT", (0,0), (0,0), 3.5, C_KINAL_GOLD),
        ("BOX", (0,0), (-1,-1), 0.5, colors.HexColor("#FDE68A")),
        ("TOPPADDING", (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
        ("LEFTPADDING", (0,0), (-1,-1), 8),
        ("RIGHTPADDING", (0,0), (-1,-1), 8),
    ]))
    story.append(t_tu)
    story.append(Spacer(1, 7))

    # 4. MARCO INSTITUCIONAL Y PRINCIPIO DEL TRABAJO BIEN HECHO
    story.append(Paragraph("2. Ideario Institucional y Principio del «Trabajo Bien Hecho»", styles["H1"]))
    story.append(Paragraph(
        "<b>Misión de Fundación Kinal:</b> <i>«Formar a jóvenes y adultos a través de una educación integral, con énfasis en las áreas técnicas y tecnológicas, influyendo positivamente en su trabajo, su familia y la sociedad»</i>.<br/>"
        "<b>Valores Nucleares:</b> <i>«Visión cristiana de la vida. Respeto a la dignidad de la persona. Espíritu de servicio. Trabajo bien hecho. Libertad personal responsable»</i>.<br/>"
        "<b>Formación Dual y DQR Nivel 6:</b> El aprender en el proceso del trabajo es base y objetivo de la formación en alternancia. La competencia se entiende como la capacidad integral de acción (conocimientos, destrezas, autonomía y responsabilidad social). En el mando medio, el <b>trabajo bien hecho</b> se traduce en escuchar con empatía, exigir con respeto, comunicar prioridades claras en piso y cuidar la dignidad e integridad de cada colaborador técnico.",
        styles["Body"]
    ))
    story.append(Spacer(1, 6))

    # SALTO DE PÁGINA PARA EL DESGLOSE MODULAR
    story.append(PageBreak())

    # 5. DESGLOSE MODULAR DETALLADO Y HERRAMIENTAS DE CAMPO
    story.append(Paragraph("3. Desglose Modular y Herramientas Operativas de Campo", styles["H1"]))
    story.append(Paragraph("Contenidos aplicados de las 4 sesiones articulados con el material didáctico oficial:", styles["Body"]))
    story.append(Spacer(1, 4))

    # MÓDULO 1
    m1_content = [
        [
            Paragraph("<b>MÓDULO 1: Inteligencia Emocional &ndash; Factor Humano (Sesión 1 &bull; Presencial Campus Kinal)</b>", styles["BannerTitle"]),
            Paragraph("Martes 3 Nov &bull; 14:00 - 16:00 (120 min) &bull; Aulas Ejecutivas y Talleres ETS", styles["BannerSub"])
        ]
    ]
    t_m1 = Table(m1_content, colWidths=[380, 160])
    t_m1.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), C_KINAL_DARK),
        ("TOPPADDING", (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
        ("LEFTPADDING", (0,0), (-1,-1), 6),
        ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ]))
    story.append(t_m1)

    m1_detail = [
        [
            Paragraph(
                "&bull; <b>La persona en el centro:</b> Dignidad incondicional, libertad responsable y capacidad de perfeccionamiento humano.<br/>"
                "&bull; <b>Potencias del alma (Aporte Prof. Vinicio Donis):</b> Inteligencia (aprender, entender y juzgar) y Voluntad (querer el bien y decidir).<br/>"
                "&bull; <b>Límites del CI vs Inteligencia Emocional:</b> El Cociente Intelectual influye en tan solo un 8% en el éxito vital y laboral. El autogobierno de los estados de ánimo es requisito indispensable para progresar (Platón: <i>«Todo aprendizaje tiene una base emocional»</i>).<br/>"
                "&bull; <b>Estrategia de desarrollo personal:</b> Dirección, libertad y esfuerzo. 4 ámbitos armónicos (físico, familiar, laboral, ético).<br/>"
                "&bull; <b>Recorrido vivencial por talleres Kinal:</b> Observación del modelo formativo del Técnico Universitario en piso de taller.",
                styles["TableCell"]
            )
        ]
    ]
    t_m1_d = Table(m1_detail, colWidths=[540])
    t_m1_d.setStyle(TableStyle([
        ("BOX", (0,0), (-1,-1), 0.5, C_BORDER),
        ("BACKGROUND", (0,0), (-1,-1), colors.white),
        ("TOPPADDING", (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
        ("LEFTPADDING", (0,0), (-1,-1), 6),
        ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ]))
    story.append(t_m1_d)
    story.append(Spacer(1, 6))

    # MÓDULO 2
    m2_content = [
        [
            Paragraph("<b>MÓDULO 2: Manejo de Personal, Clima Laboral y Manejo de Crisis (Sesión 2 &bull; Virtual Teams)</b>", styles["BannerTitle"]),
            Paragraph("Martes 10 Nov &bull; 14:00 - 16:00 (120 min) &bull; Microsoft Teams", styles["BannerSub"])
        ]
    ]
    t_m2 = Table(m2_content, colWidths=[380, 160])
    t_m2.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), C_KINAL_DARK),
        ("TOPPADDING", (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
        ("LEFTPADDING", (0,0), (-1,-1), 6),
        ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ]))
    story.append(t_m2)

    m2_detail = [
        [
            Paragraph(
                "&bull; <b>Plantilla Operativa de Onboarding 30-60-90 Días:</b> Fase 1 Asimilar (1-30d, seguridad POE, kit de herramientas, sombra, cero incidentes); Fase 2 Aplicar (31-60d, calidad, tiempos, cero reprocesos); Fase 3 Proponer (61-90d, autonomía plena, causa raíz y propuesta de mejora).<br/>"
                "&bull; <b>Estructura de la Micro-Charla de 7 Minutos (Ritual Diario de Campo):</b> Minuto 1 Conexión humana; Minutos 2-3 Píldora de seguridad o calidad (1 solo riesgo); Minutos 4-5 Prioridades operativas del turno; Minutos 6-7 Reconocimiento específico y cierre con energía.<br/>"
                "&bull; <b>Ruta de Desescalamiento 1-a-1 (Protocolo de 18 min):</b> Paso 1 Contención y despresurización en privado (min 1-5); Paso 2 Objetivación técnica despersonalizando el conflicto (min 6-12); Paso 3 Compromiso operativo y seguimiento obligatorio a 48 horas (min 13-18).<br/>"
                "&bull; <b>Construcción de Clima:</b> Seguridad psicológica para reportar desviaciones sin miedo a represalias y equidad operativa.",
                styles["TableCell"]
            )
        ]
    ]
    t_m2_d = Table(m2_detail, colWidths=[540])
    t_m2_d.setStyle(TableStyle([
        ("BOX", (0,0), (-1,-1), 0.5, C_BORDER),
        ("BACKGROUND", (0,0), (-1,-1), colors.white),
        ("TOPPADDING", (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
        ("LEFTPADDING", (0,0), (-1,-1), 6),
        ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ]))
    story.append(t_m2_d)
    story.append(Spacer(1, 6))

    # MÓDULO 3
    m3_content = [
        [
            Paragraph("<b>MÓDULO 3: Fortalecimiento de Competencias Técnicas (Sesión 3 &bull; Virtual Teams)</b>", styles["BannerTitle"]),
            Paragraph("Martes 17 Nov &bull; 14:00 - 16:00 (120 min) &bull; Microsoft Teams", styles["BannerSub"])
        ]
    ]
    t_m3 = Table(m3_content, colWidths=[380, 160])
    t_m3.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), C_KINAL_DARK),
        ("TOPPADDING", (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
        ("LEFTPADDING", (0,0), (-1,-1), 6),
        ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ]))
    story.append(t_m3)

    m3_detail = [
        [
            Paragraph(
                "&bull; <b>Diagnóstico de Brechas Técnicas en Piso:</b> Identificación de necesidades por retrabajos, demoras en ciclo y desgaste de instrumental.<br/>"
                "&bull; <b>Matriz de Polivalencia (Skills Matrix):</b> Mapeo de 4 niveles de dominio (N1 Aprendiz, N2 Guiado, N3 Autónomo, N4 Mentor) y eliminación de cuellos de botella por concentración de tareas.<br/>"
                "&bull; <b>Instrucción en el Puesto de Trabajo:</b> Método de 4 pasos (Demostrar &rarr; Guiar &rarr; Explicar &rarr; Delegar) y POEs visuales en planta.<br/>"
                "&bull; <b>El Técnico Universitario de KINAL:</b> Egresados formados con disciplina, rigor técnico y habilidades de supervisión temprana.",
                styles["TableCell"]
            )
        ]
    ]
    t_m3_d = Table(m3_detail, colWidths=[540])
    t_m3_d.setStyle(TableStyle([
        ("BOX", (0,0), (-1,-1), 0.5, C_BORDER),
        ("BACKGROUND", (0,0), (-1,-1), colors.white),
        ("TOPPADDING", (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
        ("LEFTPADDING", (0,0), (-1,-1), 6),
        ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ]))
    story.append(t_m3_d)
    story.append(Spacer(1, 6))

    # MÓDULO 4
    m4_content = [
        [
            Paragraph("<b>MÓDULO 4: Rotación de Personal y Cierre Estratégico (Sesión 4 &bull; Presencial Campus Kinal)</b>", styles["BannerTitle"]),
            Paragraph("Martes 24 Nov &bull; 14:00 - 16:00 (120 min) &bull; Auditorio Kinal", styles["BannerSub"])
        ]
    ]
    t_m4 = Table(m4_content, colWidths=[380, 160])
    t_m4.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), C_KINAL_DARK),
        ("TOPPADDING", (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
        ("LEFTPADDING", (0,0), (-1,-1), 6),
        ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ]))
    story.append(t_m4)

    m4_detail = [
        [
            Paragraph(
                "&bull; <b>Causa Raíz de la Rotación Técnica:</b> Desglose de costos directos e indirectos, jefaturas autoritarias vs formativas.<br/>"
                "&bull; <b>Salario Emocional y Fidelización:</b> Reconocimiento oportuno, validación del esfuerzo visible, sentido de pertenencia y orgullo técnico.<br/>"
                "&bull; <b>Mesa Redonda de Mandos Medios:</b> Presentación de los Planes de Acción Aplicados implementados en cada empresa aliada.<br/>"
                "&bull; <b>Alianza Estratégica Kinal - UNIS:</b> Convenios de alternancia dual, pasantías y bolsa de empleo.<br/>"
                "&bull; <b>Clausura y Entrega de Diplomas:</b> Acreditación oficial emitida por KINAL y la Universidad del Istmo.",
                styles["TableCell"]
            )
        ]
    ]
    t_m4_d = Table(m4_detail, colWidths=[540])
    t_m4_d.setStyle(TableStyle([
        ("BOX", (0,0), (-1,-1), 0.5, C_BORDER),
        ("BACKGROUND", (0,0), (-1,-1), colors.white),
        ("TOPPADDING", (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
        ("LEFTPADDING", (0,0), (-1,-1), 6),
        ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ]))
    story.append(t_m4_d)
    story.append(Spacer(1, 8))

    # 6. RÚBRICA ANALÍTICA DE EVALUACIÓN INSTITUCIONAL
    story.append(Paragraph("4. Rúbrica Analítica de Competencias y Acreditación (&ge; 75/100 Puntos)", styles["H1"]))
    rubrica_rows = [
        [
            Paragraph("<b>Criterio de Evaluación</b>", styles["TableHead"]),
            Paragraph("<b>Excelente (90-100 pts)</b>", styles["TableHead"]),
            Paragraph("<b>Competente (80-89 pts)</b>", styles["TableHead"]),
            Paragraph("<b>Suficiente (75-79 pts) [Umbral]</b>", styles["TableHead"]),
            Paragraph("<b>Insuficiente (&lt;75 pts)</b>", styles["TableHead"]),
            Paragraph("<b>Pond.</b>", styles["TableHead"])
        ],
        [
            Paragraph("<b>1. Inteligencia Emocional y Autogobierno</b>", styles["TableCellBold"]),
            Paragraph("Domina autogobierno emocional ante la presión; reconoce la dignidad incondicional y aplica escucha activa plena.", styles["TableCell"]),
            Paragraph("Mantiene serenidad y trato respetuoso; identifica emociones con reactividad menor ocasional.", styles["TableCell"]),
            Paragraph("Mantiene trato formal y respetuoso; cumple normas de convivencia sin consolidar autogobierno.", styles["TableCell"]),
            Paragraph("Reacciona impulsivamente, descalifica a colaboradores o exhibe errores en piso.", styles["TableCell"]),
            Paragraph("<b>20%</b>", styles["TableCellCenter"])
        ],
        [
            Paragraph("<b>2. Onboarding y Micro-Charla en Piso</b>", styles["TableCellBold"]),
            Paragraph("Aplica con rigor el Plan 30-60-90 y ejecuta la Micro-Charla de 7 min con estructura exacta y reconocimiento visible.", styles["TableCell"]),
            Paragraph("Aplica plantilla 30-60-90 y ejecuta micro-charlas de forma regular con leves variaciones de tiempo.", styles["TableCell"]),
            Paragraph("Diligencia formatos pero su aplicación es esporádica o excede los tiempos fijados.", styles["TableCell"]),
            Paragraph("No aplica las herramientas de campo o las reduce a trámites burocráticos sin impacto.", styles["TableCell"]),
            Paragraph("<b>30%</b>", styles["TableCellCenter"])
        ],
        [
            Paragraph("<b>3. Desescalamiento de Conflictos 1-a-1</b>", styles["TableCellBold"]),
            Paragraph("Aplica el protocolo de 3 pasos (18 min) en privado; objetiva técnicamente y da seguimiento estricto a 48 hrs.", styles["TableCell"]),
            Paragraph("Desescala en privado con base en normas técnicas; logra acuerdos claros con seguimiento estándar.", styles["TableCell"]),
            Paragraph("Separa a involucrados y dialoga, pero le cuesta centrar la discusión en hechos técnicos.", styles["TableCell"]),
            Paragraph("Toma partido público, ignora el conflicto o amenaza con despidos en caliente.", styles["TableCell"]),
            Paragraph("<b>25%</b>", styles["TableCellCenter"])
        ],
        [
            Paragraph("<b>4. Diagnóstico y Plan de Retención</b>", styles["TableCellBold"]),
            Paragraph("Presenta Matriz de Polivalencia precisa y Plan de Retención con metas medibles para abatir la rotación.", styles["TableCell"]),
            Paragraph("Elabora matriz coherente y propone acciones lógicas de retención técnica en su taller.", styles["TableCell"]),
            Paragraph("Identifica brechas técnicas básicas y propone mejoras generales poco definidas.", styles["TableCell"]),
            Paragraph("No presenta plan de retención o carece de diagnóstico técnico objetivo de cuadrilla.", styles["TableCell"]),
            Paragraph("<b>25%</b>", styles["TableCellCenter"])
        ]
    ]

    rubrica_table = Table(rubrica_rows, colWidths=[90, 100, 95, 95, 125, 35])
    rubrica_table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), C_KINAL_NAVY),
        ("GRID", (0,0), (-1,-1), 0.5, C_BORDER),
        ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
        ("TOPPADDING", (0,0), (-1,-1), 3),
        ("BOTTOMPADDING", (0,0), (-1,-1), 3),
        ("LEFTPADDING", (0,0), (-1,-1), 4),
        ("RIGHTPADDING", (0,0), (-1,-1), 4),
        ("ROWBACKGROUNDS", (0,1), (-1,-1), [colors.white, C_BG_LIGHT]),
    ]))
    story.append(rubrica_table)
    story.append(Spacer(1, 10))

    # FIRMAS Y AVAL INSTITUCIONAL
    firmas = [
        [
            Paragraph("<b>Dirección Académica</b><br/>Escuela Técnica Superior KINAL", styles["TableCellCenter"]),
            Paragraph("<b>Coordinación de Mandos Medios</b><br/>Programa de Desarrollo Gerencial", styles["TableCellCenter"]),
            Paragraph("<b>Acreditación Académica</b><br/>Universidad del Istmo (UNIS)", styles["TableCellCenter"])
        ]
    ]
    t_firmas = Table(firmas, colWidths=[180, 180, 180])
    t_firmas.setStyle(TableStyle([
        ("LINEABOVE", (0,0), (-1,-1), 0.5, C_BORDER),
        ("TOPPADDING", (0,0), (-1,-1), 6),
        ("BOTTOMPADDING", (0,0), (-1,-1), 0),
    ]))
    story.append(t_firmas)

    # Compilar documento con NumberedCanvas
    doc.build(story, canvasmaker=NumberedCanvas)
    sz_kb = os.path.getsize(target_path) / 1024
    print(f"PDF generado exitosamente: {target_path} ({sz_kb:.1f} KB)")
    return target_path

if __name__ == "__main__":
    build_pdf()
