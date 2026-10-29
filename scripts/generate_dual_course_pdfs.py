#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador de Documentos PDF Institucionales (Versiones 25 Horas y 40 Horas):
Levantamiento de Planos y Diagramas para Proyectos (Fundación Kinal)
Escuela Técnica Superior — Coordinación de Formación Continua
"""

import os
import sys

VENDOR_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "vendor")
if os.path.exists(VENDOR_DIR):
    sys.path.insert(0, VENDOR_DIR)

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COURSE_DIR = os.path.join(WORKSPACE_DIR, "Cursos", "Levantamiento_Planos_Diagramas")
OUTPUT_DIR = os.path.join(WORKSPACE_DIR, "output")
LOGO_PATH = os.path.join(WORKSPACE_DIR, "assets", "escudo_kinal_cuadrado.png")

# Colores Institucionales Kinal
C_KINAL_BLUE = colors.HexColor("#003366")
C_KINAL_NAVY = colors.HexColor("#22376D")
C_KINAL_DARK = colors.HexColor("#1A202C")
C_BORDER = colors.HexColor("#CBD5E0")
C_BG_LIGHT = colors.HexColor("#F7FAFC")
C_TEXT_MUTED = colors.HexColor("#4A5568")

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []
        self.doc_header_subtitle = "Levantamiento de Planos y Diagramas para Proyectos"

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
            self.setFillColor(C_KINAL_BLUE)
            self.drawString(40, 755, "FUNDACIÓN KINAL • ESCUELA TÉCNICA SUPERIOR")
            self.setFont("Helvetica", 8)
            self.setFillColor(C_TEXT_MUTED)
            self.drawRightString(572, 755, getattr(self, "doc_header_subtitle", "Levantamiento de Planos y Diagramas"))
            self.setStrokeColor(C_BORDER)
            self.setLineWidth(0.5)
            self.line(40, 748, 572, 748)

        # Pie de página en todas las páginas
        self.setStrokeColor(C_BORDER)
        self.setLineWidth(0.5)
        self.line(40, 42, 572, 42)
        
        self.setFont("Helvetica", 7.5)
        self.setFillColor(C_TEXT_MUTED)
        self.drawString(40, 30, "Fundación Kinal • Marco DQR Nivel 4-5 • Nota Mínima Aprobatoria: 75/100 Puntos")
        
        page_str = f"Página {self._pageNumber} de {page_count}"
        self.drawRightString(572, 30, page_str)
        self.restoreState()


def get_common_styles():
    return {
        "Title": ParagraphStyle("DocTitle", fontName="Helvetica-Bold", fontSize=17, leading=21, textColor=C_KINAL_BLUE),
        "Subtitle": ParagraphStyle("DocSub", fontName="Helvetica-Oblique", fontSize=9.5, leading=13, textColor=C_TEXT_MUTED),
        "H1": ParagraphStyle("H1", fontName="Helvetica-Bold", fontSize=11, leading=15, textColor=C_KINAL_BLUE, spaceBefore=12, spaceAfter=5),
        "H2": ParagraphStyle("H2", fontName="Helvetica-Bold", fontSize=9.5, leading=12, textColor=C_KINAL_NAVY, spaceBefore=7, spaceAfter=3),
        "Body": ParagraphStyle("Body", fontName="Helvetica", fontSize=8, leading=11, textColor=C_KINAL_DARK),
        "CalloutTitle": ParagraphStyle("CalloutTitle", fontName="Helvetica-Bold", fontSize=8, leading=11, textColor=C_KINAL_BLUE),
        "CalloutText": ParagraphStyle("CalloutText", fontName="Helvetica", fontSize=8, leading=11, textColor=C_KINAL_DARK),
        "TableHead": ParagraphStyle("TableHead", fontName="Helvetica-Bold", fontSize=7.5, leading=9.5, textColor=C_KINAL_BLUE),
        "TableCell": ParagraphStyle("TableCell", fontName="Helvetica", fontSize=7, leading=9.5, textColor=C_KINAL_DARK),
        "TableCellBold": ParagraphStyle("TableCellBold", fontName="Helvetica-Bold", fontSize=7, leading=9.5, textColor=C_KINAL_DARK),
    }

def make_callout(bold_lbl, text, styles):
    content = [
        Paragraph(bold_lbl, styles["CalloutTitle"]),
        Spacer(1, 2),
        Paragraph(text, styles["CalloutText"])
    ]
    t = Table([[content]], colWidths=[532])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_BG_LIGHT),
        ('LINELEFT', (0,0), (-1,-1), 3.5, C_KINAL_BLUE),
        ('BOX', (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 9),
        ('RIGHTPADDING', (0,0), (-1,-1), 7),
    ]))
    return t

def build_pdf_25h():
    target_path = os.path.join(COURSE_DIR, "programa_formativo_levantamiento_planos_25h.pdf")
    doc = SimpleDocTemplate(target_path, pagesize=letter, leftMargin=40, rightMargin=40, topMargin=45, bottomMargin=55)
    styles = get_common_styles()
    story = []

    # ENCABEZADO
    if os.path.exists(LOGO_PATH):
        img = Image(LOGO_PATH, width=44, height=44)
        header_text = [
            Paragraph("FUNDACIÓN KINAL • ESCUELA TÉCNICA SUPERIOR", ParagraphStyle("HPre", fontName="Helvetica-Bold", fontSize=9.5, leading=11, textColor=C_KINAL_BLUE)),
            Paragraph("Levantamiento de Planos y Diagramas para Proyectos", styles["Title"]),
            Paragraph("Modalidad Intensiva Sabatina (25 Horas Presenciales) | 5 Sábados: 31 Oct - 28 Nov 2026", styles["Subtitle"])
        ]
        t_header = Table([[img, header_text]], colWidths=[52, 480])
        t_header.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('LEFTPADDING', (1,0), (1,0), 6),
            ('BOTTOMPADDING', (0,0), (-1,-1), 0),
            ('TOPPADDING', (0,0), (-1,-1), 0),
        ]))
        story.append(t_header)

    story.append(Spacer(1, 8))
    story.append(HRFlowable(width="100%", thickness=1.5, color=C_KINAL_BLUE, spaceBefore=2, spaceAfter=8))

    # FICHA TÉCNICA 25H
    ficha_data = [
        [Paragraph("Institución / Sede", styles["TableCellBold"]), Paragraph("<b>Fundación Kinal</b> — Escuela Técnica Superior (Sede Central, Zona 7, Ciudad de Guatemala)", styles["TableCell"])],
        [Paragraph("Nivel DQR de Referencia", styles["TableCellBold"]), Paragraph("<b>Equivalencia DQR Nivel 4 - 5</b> (Especialización ocupacional y rigor métrico)", styles["TableCell"])],
        [Paragraph("Carga Horaria y Calendario", styles["TableCellBold"]), Paragraph("<b>25 horas pedagógicas presenciales</b> (5 sábados de 5 horas: 08:00 a 13:00 hrs)<br/>• <b>Inicio:</b> 31 de Octubre de 2026 &nbsp;|&nbsp; <b>Finalización:</b> 28 de Noviembre de 2026", styles["TableCell"])],
        [Paragraph("Entorno Tecnológico", styles["TableCellBold"]), Paragraph("Laboratorio CAD (AutoCAD 2D), Tablets con Stylus, Cintas rígidas y de 50m, Distanciómetro Láser", styles["TableCell"])],
        [Paragraph("Ecosistema Digital", styles["TableCellBold"]), Paragraph("<b>Moodle (Kinal.academy)</b> y <b>Microsoft Teams / Microsoft 365</b>", styles["TableCell"])],
        [Paragraph("Nota Mínima Aprobatoria", styles["TableCellBold"]), Paragraph("<b>75 puntos sobre 100</b> en evaluaciones prácticas, laboratorios CAD y Proyecto Capstone", styles["TableCell"])],
    ]
    t_ficha = Table(ficha_data, colWidths=[145, 387])
    t_ficha.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_BG_LIGHT),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_ficha)
    story.append(Spacer(1, 10))

    # MARCO FILOSÓFICO
    story.append(Paragraph("1. Marco Filosófico e Ideario Institucional de Fundación Kinal", styles["H1"]))
    story.append(make_callout("Misión Institucional de Kinal:", "«Formar a jóvenes y adultos a través de una educación integral, con énfasis en las áreas técnicas y tecnológicas, influyendo positivamente en su trabajo, su familia y la sociedad».", styles))
    story.append(Spacer(1, 3))
    story.append(make_callout("Valores Nucleares de Kinal:", "«Visión cristiana de la vida. Respeto a la dignidad de la persona. Espíritu de servicio. Trabajo bien hecho. Libertad personal responsable».", styles))
    story.append(Spacer(1, 3))
    story.append(make_callout(
        "Concepto de Competencia Profesional (Marco DQR):",
        "La competencia es la capacidad y disposición de la persona para integrar conocimientos técnicos, destrezas prácticas y responsabilidad personal y social, actuando con criterio ético y autonomía ante situaciones reales de trabajo.<br/>"
        "<b>Competencia Diseñada para el Curso:</b> El participante planifica, ejecuta y documenta levantamientos métricos rigurosos mediante cintas y metro láser aplicando métodos de <b>triangulación</b> y <b>radiaciones</b>, elabora croquis en tablet y mano alzada, y modela planos 2D y diagramas en AutoCAD maquetados a escala ejecutiva con membrete Kinal bajo el estándar del trabajo bien hecho.",
        styles
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("El Principio del «Trabajo Bien Hecho» en la Metrología y el Dibujo Técnico:", styles["H2"]))
    story.append(Paragraph(
        "En el levantamiento de planos para obras y remodelaciones, asumir ortogonalidad en recintos con falsa escuadra genera sobrecostos y demoliciones. En este programa se inculca el rigor del trabajo bien hecho: cero tolerancia al redondeo de cotas, verificación in situ mediante <b>triangulaciones</b> y <b>radiaciones</b> con metro láser, trazado exacto en AutoCAD con herramientas de precisión (OSNAP, Polar), Referencias Externas (XREFs), bloques de instalaciones y maquetación ejecutiva a escala 1:50 en Paper Space.",
        styles["Body"]
    ))
    story.append(Spacer(1, 10))

    # TEMARIO JERÁRQUICO 25H
    story.append(Paragraph("2. Temario Curricular Jerárquico (25 Horas Presenciales)", styles["H1"]))
    temario_data = [
        [Paragraph("Módulo", styles["TableHead"]), Paragraph("Duración", styles["TableHead"]), Paragraph("Contenidos Nucleares y Competencias", styles["TableHead"])],
        [
            Paragraph("<b>Módulo 1:</b><br/>Metrología de Campo, Triangulación, Radiaciones y Croquis", styles["TableCellBold"]),
            Paragraph("<b>10 Horas</b><br/>(Sábados 1 y 2)", styles["TableCell"]),
            Paragraph(
                "• Flexómetros (gancho corredizo para interiores/exteriores) y cinta larga de 50m (tensión y catenaria).<br/>"
                "• Metro láser digital: tracking continuo, áreas (m²), volúmenes (m³) y alturas por Pitágoras.<br/>"
                "• <b>Método de Triangulación y Trilateración:</b> División de recintos no ortogonales en triángulos por diagonales cruzadas y líneas de amarre. Comprobación 3-4-5.<br/>"
                "• <b>Método de Radiación de Campo:</b> Estación base central y medición radial de distancias con láser.<br/>"
                "• Croquis a mano alzada y en tablet con stylus: organización en capas y exportación a DWG/PDF.",
                styles["TableCell"]
            )
        ],
        [
            Paragraph("<b>Módulo 2:</b><br/>AutoCAD 2D Práctico: Precisión, XREFs y Cotas", styles["TableCellBold"]),
            Paragraph("<b>10 Horas</b><br/>(Sábados 3 y 4)", styles["TableCell"]),
            Paragraph(
                "• Configuración directa de unidades métricas con comando <code>UNITS</code> (decimal, precisión 0.000 m).<br/>"
                "• Herramientas de captura indispensables: <code>OSNAP</code> (Endpoint, Midpoint, Intersection, Perpendicular) y <code>Polar Tracking</code> (F10 a 45°/90°).<br/>"
                "• Referencias Externas (<code>XREFs</code>): enlazado del croquis de la tablet escalado a tamaño real 1:1.<br/>"
                "• Trazado de muros con polilíneas cerradas y recorte de vanos (<code>OFFSET</code>, <code>FILLET</code>, <code>TRIM</code>).<br/>"
                "• Comprobación de diagonales con comando <code>DIST</code> para verificar cierre geométrico.<br/>"
                "• Estilos de cota Kinal (<code>DIMSTYLE</code>): cotas continuas y alineadas legibles sin solapes.",
                styles["TableCell"]
            )
        ],
        [
            Paragraph("<b>Módulo 3:</b><br/>Bloques de Instalaciones, Maquetación y Capstone", styles["TableCellBold"]),
            Paragraph("<b>5 Horas</b><br/>(Sábado 5)", styles["TableCell"]),
            Paragraph(
                "• Bloques para instalaciones eléctricas (tableros, tomas, luminarias) e hidrosanitarias (válvulas, grifos) con atributos.<br/>"
                "• Diagrama unifilar básico esquematizado del tablero eléctrico del recinto.<br/>"
                "• Maquetación en Paper Space: lámina Doble Carta o A3, Viewport bloqueado a escala normalizada <b>1:50</b>.<br/>"
                "• Membrete oficial de Fundación Kinal y tabla de plumillas monocromáticas <code>.CTB</code>.<br/>"
                "• <b>Proyecto Capstone Integrador:</b> Levantamiento real en Kinal, dibujo 2D y defensa oral (&ge; 75 pts).",
                styles["TableCell"]
            )
        ],
    ]
    t_temario = Table(temario_data, colWidths=[130, 80, 322])
    t_temario.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#EDF2F7")),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_temario)
    story.append(Spacer(1, 10))

    # CRONOGRAMA 25H
    story.append(Paragraph("3. Macroplanificación — 5 Sábados de 5 Horas (08:00 a 13:00 hrs)", styles["H1"]))
    cron_data = [
        [Paragraph("Fecha / Sesión", styles["TableHead"]), Paragraph("Módulo", styles["TableHead"]), Paragraph("Actividades Prácticas Clave", styles["TableHead"]), Paragraph("Entregable Evaluativo", styles["TableHead"])],
        [
            Paragraph("<b>Sábado 1</b><br/>31 Oct 2026", styles["TableCellBold"]),
            Paragraph("M1: Medición y Triangulación", styles["TableCell"]),
            Paragraph("Calibración de flexómetros, cinta de 50m, metro láser y práctica del método de triangulación por diagonales cruzadas y comprobación 3-4-5.", styles["TableCell"]),
            Paragraph("Ficha de medición y croquis a mano alzada acotado y diagonalizado.", styles["TableCellBold"])
        ],
        [
            Paragraph("<b>Sábado 2</b><br/>07 Nov 2026", styles["TableCellBold"]),
            Paragraph("M1: Radiaciones y Tablet", styles["TableCell"]),
            Paragraph("Levantamiento por el método de radiación desde estación base con láser en nave técnica, croquis vectorial en tablet en 3 capas y exportación DWG.", styles["TableCell"]),
            Paragraph("Reporte de radiación + Croquis digital en tablet exportado a DWG/PDF.", styles["TableCellBold"])
        ],
        [
            Paragraph("<b>Sábado 3</b><br/>14 Nov 2026", styles["TableCellBold"]),
            Paragraph("M2: AutoCAD Precisión y XREF", styles["TableCell"]),
            Paragraph("Configuración de unidades métricas (0.000 m), herramientas OSNAP y Polar Tracking, enlazado de XREF a escala 1:1 y trazo de muros comprobando diagonales.", styles["TableCell"]),
            Paragraph("Archivo DWG con XREF enlazada y muros trazados con precisión milimétrica.", styles["TableCellBold"])
        ],
        [
            Paragraph("<b>Sábado 4</b><br/>21 Nov 2026", styles["TableCellBold"]),
            Paragraph("M2/M3: Cotas y Bloques", styles["TableCell"]),
            Paragraph("Acotación completa DIMSTYLE Kinal, inserción de bloques de instalaciones con atributos y trazado del diagrama unifilar del tablero.", styles["TableCell"]),
            Paragraph("Planta acotada con bloques de instalaciones y diagrama unifilar.", styles["TableCellBold"])
        ],
        [
            Paragraph("<b>Sábado 5</b><br/>28 Nov 2026", styles["TableCellBold"]),
            Paragraph("M3: Maquetación y Capstone", styles["TableCell"]),
            Paragraph("Maquetación en Paper Space con Viewport bloqueado a escala exacta 1:50, membrete oficial Kinal, plumillas CTB y sustentación individual del Capstone.", styles["TableCell"]),
            Paragraph("<b>Expediente Capstone Aprobado (&ge; 75 puntos)</b>.", styles["TableCellBold"])
        ],
    ]
    t_cron = Table(cron_data, colWidths=[75, 110, 215, 132])
    t_cron.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#EDF2F7")),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_cron)
    story.append(Spacer(1, 10))

    # RÚBRICA DE EVALUACIÓN
    story.append(Paragraph("4. Sistema de Evaluación y Rúbrica Analítica Terminal (Nota Mínima: 75/100)", styles["H1"]))
    rub_data = [
        [Paragraph("Dimensión Evaluada", styles["TableHead"]), Paragraph("Excelente (90 - 100)", styles["TableHead"]), Paragraph("Satisfactorio (75 - 89)<br/><i>[Aprobatorio Kinal]</i>", styles["TableHead"]), Paragraph("En Desarrollo (< 75)", styles["TableHead"])],
        [
            Paragraph("<b>1. Metrología de Campo, Triangulación y Radiaciones</b>", styles["TableCellBold"]),
            Paragraph("Mediciones milimétricas exactas; compensación impecable del gancho; dominio de Pitágoras en láser; triangulación y radiaciones sin discrepancias.", styles["TableCell"]),
            Paragraph("Mediciones precisas con cintas y láser; aplica triangulación y radiación con errores dentro de tolerancia (&le; 5 mm) <b>(&ge; 75 pts)</b>.", styles["TableCell"]),
            Paragraph("Errores por descuido en referencia láser o catenaria; diagonales que no cierran; medidas falseadas.", styles["TableCell"])
        ],
        [
            Paragraph("<b>2. Croquizado Técnico</b><br/>(Mano Alzada y Tablet)", styles["TableCellBold"]),
            Paragraph("Proporción visual perfecta a mano alzada; croquis en tablet vectorizado con excelente gestión de capas; exportación limpia para CAD.", styles["TableCell"]),
            Paragraph("Croquis legible a mano alzada con cotas completas y diagonales; croquis en tablet en capas; archivo vectorial exportado correctamente <b>(&ge; 75 pts)</b>.", styles["TableCell"]),
            Paragraph("Croquis desproporcionado o confuso; omisión de capas en tablet; notas ilegibles o archivos dañados.", styles["TableCell"])
        ],
        [
            Paragraph("<b>3. AutoCAD 2D: Precisión, XREFs, Bloques y Paper Space</b>", styles["TableCellBold"]),
            Paragraph("Unidades métricas estrictas; uso impecable de OSNAP y Polar; XREF con ruta relativa; cotas legibles; bloques con atributos; Viewport a escala 1:50 y CTB perfecto.", styles["TableCell"]),
            Paragraph("Modela en AutoCAD con unidades métricas y capas; utiliza OSNAP y Polar; acotación completa; XREF y bloques; maquetación a escala 1:50 con membrete Kinal <b>(&ge; 75 pts)</b>.", styles["TableCell"]),
            Paragraph("Desorden en capas; dibujo fuera de escala en Paper Space; líneas duplicadas; ausencia de bloques.", styles["TableCell"])
        ],
        [
            Paragraph("<b>4. Ética y Trabajo Bien Hecho</b><br/>(Ideario Kinal)", styles["TableCellBold"]),
            Paragraph("Encarna de forma ejemplar el trabajo bien hecho. Cero tolerancia al falseamiento de cotas; puntualidad perfecta; cuidado del instrumental y espíritu de servicio.", styles["TableCell"]),
            Paragraph("Registro ordenado en libreta y bitácora; puntualidad, respeto a normas de seguridad de taller y de laboratorio <b>(&ge; 75 pts)</b>.", styles["TableCell"]),
            Paragraph("Indisciplina, tardanzas, descuido en el uso del instrumental o falseamiento intencional de medidas.", styles["TableCell"])
        ],
    ]
    t_rub = Table(rub_data, colWidths=[110, 140, 142, 140])
    t_rub.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#EDF2F7")),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_rub)

    nc = NumberedCanvas
    doc.build(story, canvasmaker=nc)
    print(f"PDF 25h generado: {target_path}")

    # Copia a programa_formativo_levantamiento_planos.pdf y a output/
    import shutil
    shutil.copyfile(target_path, os.path.join(COURSE_DIR, "programa_formativo_levantamiento_planos.pdf"))
    shutil.copyfile(target_path, os.path.join(OUTPUT_DIR, "programa_formativo_levantamiento_planos.pdf"))
    shutil.copyfile(target_path, os.path.join(OUTPUT_DIR, "programa_formativo_levantamiento_planos_25h.pdf"))


def build_pdf_40h():
    target_path = os.path.join(COURSE_DIR, "programa_formativo_levantamiento_planos_40h.pdf")
    doc = SimpleDocTemplate(target_path, pagesize=letter, leftMargin=40, rightMargin=40, topMargin=45, bottomMargin=55)
    styles = get_common_styles()
    story = []

    # ENCABEZADO 40H
    if os.path.exists(LOGO_PATH):
        img = Image(LOGO_PATH, width=44, height=44)
        header_text = [
            Paragraph("FUNDACIÓN KINAL • ESCUELA TÉCNICA SUPERIOR", ParagraphStyle("HPre", fontName="Helvetica-Bold", fontSize=9.5, leading=11, textColor=C_KINAL_BLUE)),
            Paragraph("Levantamiento de Planos y Diagramas para Proyectos", styles["Title"]),
            Paragraph("Modalidad de Especialización Técnica (40 Horas Presenciales) | 10 Sesiones de 4 Horas", styles["Subtitle"])
        ]
        t_header = Table([[img, header_text]], colWidths=[52, 480])
        t_header.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('LEFTPADDING', (1,0), (1,0), 6),
            ('BOTTOMPADDING', (0,0), (-1,-1), 0),
            ('TOPPADDING', (0,0), (-1,-1), 0),
        ]))
        story.append(t_header)

    story.append(Spacer(1, 8))
    story.append(HRFlowable(width="100%", thickness=1.5, color=C_KINAL_BLUE, spaceBefore=2, spaceAfter=8))

    # FICHA TÉCNICA 40H
    ficha_data = [
        [Paragraph("Institución / Sede", styles["TableCellBold"]), Paragraph("<b>Fundación Kinal</b> — Escuela Técnica Superior (Sede Central, Zona 7, Ciudad de Guatemala)", styles["TableCell"])],
        [Paragraph("Nivel DQR de Referencia", styles["TableCellBold"]), Paragraph("<b>Equivalencia DQR Nivel 4 - 5</b> (Especialización avanzada, autonomía operativa y juicio crítico)", styles["TableCell"])],
        [Paragraph("Carga Horaria y Modalidad", styles["TableCellBold"]), Paragraph("<b>40 horas pedagógicas presenciales</b> estructuradas en <b>10 sesiones de 4 horas</b> (240 min cada una)<br/>• <b>Opción A (Ciclo 2027):</b> 2 jornadas semanales entre semana (ej. Martes y Jueves 17:30 a 21:30 hrs)<br/>• <b>Opción B (Ciclo 2027):</b> 10 sábados regulares matutinos (08:00 a 12:00 hrs)", styles["TableCell"])],
        [Paragraph("Entorno Tecnológico", styles["TableCellBold"]), Paragraph("Laboratorio CAD de Alta Gama (AutoCAD 2D Avanzado), Tablets con Stylus, Cintas rígidas/largas y Láser", styles["TableCell"])],
        [Paragraph("Ecosistema Digital", styles["TableCellBold"]), Paragraph("<b>Moodle (Kinal.academy)</b> y <b>Microsoft Teams / Microsoft 365</b>", styles["TableCell"])],
        [Paragraph("Nota Mínima Aprobatoria", styles["TableCellBold"]), Paragraph("<b>75 puntos sobre 100</b> en evaluaciones de campo, laboratorios CAD y Proyecto Capstone", styles["TableCell"])],
    ]
    t_ficha = Table(ficha_data, colWidths=[145, 387])
    t_ficha.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_BG_LIGHT),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_ficha)
    story.append(Spacer(1, 10))

    # MARCO FILOSÓFICO
    story.append(Paragraph("1. Marco Filosófico e Ideario Institucional de Fundación Kinal", styles["H1"]))
    story.append(make_callout("Misión Institucional de Kinal:", "«Formar a jóvenes y adultos a través de una educación integral, con énfasis en las áreas técnicas y tecnológicas, influyendo positivamente en su trabajo, su familia y la sociedad».", styles))
    story.append(Spacer(1, 3))
    story.append(make_callout("Valores Nucleares de Kinal:", "«Visión cristiana de la vida. Respeto a la dignidad de la persona. Espíritu de servicio. Trabajo bien hecho. Libertad personal responsable».", styles))
    story.append(Spacer(1, 3))
    story.append(make_callout(
        "Concepto de Competencia Profesional (Marco DQR):",
        "La competencia es la capacidad y disposición de la persona para integrar conocimientos técnicos, destrezas prácticas y responsabilidad personal y social, actuando con criterio ético y autonomía ante situaciones reales de trabajo.<br/>"
        "<b>Competencia Diseñada para el Curso (40 Horas):</b> El egresado planifica, ejecuta y documenta levantamientos métricos complejos empleando flexómetros, cintas largas y metro láser digital con métodos de <b>triangulación y radiaciones</b>; genera croquis proporcionales en tablet y papel; y desarrolla en AutoCAD 2D planos arquitectónicos e ingenieriles con referencias externas (XREFs), cotas normalizadas, bibliotecas de bloques de instalaciones con atributos y maquetación ejecutiva a escala exacta con membrete Kinal.",
        styles
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("El Principio del «Trabajo Bien Hecho» en la Metrología y el Dibujo Técnico:", styles["H2"]))
    story.append(Paragraph(
        "El programa de 40 horas profundiza en la resolución de problemas geométricos de obra: cero tolerancia al falseamiento de cotas, verificación rigurosa de ortogonalidad mediante triangulación y radiaciones, estructuración modular con Referencias Externas (XREFs), librerías de bloques de instalaciones con atributos y presentación ejecutiva en Paper Space.",
        styles["Body"]
    ))
    story.append(Spacer(1, 10))

    # TEMARIO JERÁRQUICO 40H
    story.append(Paragraph("2. Temario Curricular Jerárquico — Modalidad 40 Horas (10 Sesiones de 4 Horas)", styles["H1"]))
    temario_data = [
        [Paragraph("Módulo", styles["TableHead"]), Paragraph("Duración", styles["TableHead"]), Paragraph("Contenidos Nucleares y Competencias", styles["TableHead"])],
        [
            Paragraph("<b>Módulo 1:</b><br/>Metrología de Campo, Triangulación y Radiaciones", styles["TableCellBold"]),
            Paragraph("<b>12 Horas</b><br/>(Sesiones 1 a 3)", styles["TableCell"]),
            Paragraph(
                "• Flexómetros (gancho corredizo para interiores/exteriores) y cinta larga de 50m (catenaria y tensión).<br/>"
                "• Metro láser digital: tracking continuo, áreas (m²), volúmenes (m³) y alturas por Pitágoras.<br/>"
                "• <b>Método de Triangulación y Trilateración:</b> Descomposición de recintos irregulares en triángulos mediante diagonales cruzadas y líneas de amarre. Comprobación 3-4-5.<br/>"
                "• <b>Método de Radiación de Campo:</b> Estación base central y medición radial de distancias con láser.<br/>"
                "• Croquis a mano alzada: proporción visual sin escalímetro, simbología y acotación encadenada.",
                styles["TableCell"]
            )
        ],
        [
            Paragraph("<b>Módulo 2:</b><br/>Croquizado Digital en Tablet y Preparación CAD", styles["TableCellBold"]),
            Paragraph("<b>6 Horas</b><br/>(Sesiones 4 y 5)", styles["TableCell"]),
            Paragraph(
                "• Configuración de tablet y stylus: sensibilidad, cuadrículas métricas y trazado asistido.<br/>"
                "• Organización en capas digitales: Muros, Vanos/Mobiliario, Cotas y Notas de campo.<br/>"
                "• Levantamiento de detalles constructivos in situ y notas técnicas legibles.<br/>"
                "• Flujo de exportación e interoperabilidad: formatos vectoriales (DWG, DXF) y PDF a escala.",
                styles["TableCell"]
            )
        ],
        [
            Paragraph("<b>Módulo 3:</b><br/>AutoCAD 2D: Precisión, XREFs, Cotas y Bloques", styles["TableCellBold"]),
            Paragraph("<b>14 Horas</b><br/>(Sesiones 6 a 8)", styles["TableCell"]),
            Paragraph(
                "• Configuración de unidades métricas con comando <code>UNITS</code> (decimal, precisión 0.000 m).<br/>"
                "• Herramientas de captura indispensables: <code>OSNAP</code> completo y <code>Polar Tracking</code> (F10 a 45°/90°).<br/>"
                "• Referencias Externas (<code>XREFs</code>): enlazado del croquis de tablet escalado a tamaño real 1:1.<br/>"
                "• Trazado de muros con polilíneas cerradas y recorte de vanos; comprobación con comando <code>DIST</code>.<br/>"
                "• Estilos de cota Kinal (<code>DIMSTYLE</code>): lineales, alineadas, continuas y angulares sin solapes.<br/>"
                "• Bloques para levantamiento de instalaciones eléctricas e hidrosanitarias con atributos (<code>ATTDEF</code>).",
                styles["TableCell"]
            )
        ],
        [
            Paragraph("<b>Módulo 4:</b><br/>Diagramas Técnicos, Maquetación y Capstone", styles["TableCellBold"]),
            Paragraph("<b>8 Horas</b><br/>(Sesiones 9 y 10)", styles["TableCell"]),
            Paragraph(
                "• Diagramas unifilares eléctricos de cuadros de carga y distribución.<br/>"
                "• Diagramas esquemáticos de tuberías e instrumentación (P&ID básico / redes hidrosanitarias).<br/>"
                "• Maquetación en Paper Space: láminas Doble Carta o A3, Viewports a escala normalizada <b>1:50</b> y <b>1:20</b>.<br/>"
                "• Membrete oficial de Kinal y tabla de plumillas monocromáticas <code>.CTB</code>.<br/>"
                "• <b>Proyecto Capstone Integrador:</b> Levantamiento integral in situ de un recinto de Kinal y defensa oral (&ge; 75 pts).",
                styles["TableCell"]
            )
        ],
    ]
    t_temario = Table(temario_data, colWidths=[130, 80, 322])
    t_temario.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#EDF2F7")),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_temario)
    story.append(Spacer(1, 10))

    # CRONOGRAMA 10 SESIONES (40H)
    story.append(Paragraph("3. Macroplanificación — 10 Sesiones de 4 Horas (40 Horas Presenciales)", styles["H1"]))
    cron_data = [
        [Paragraph("Sesión", styles["TableHead"]), Paragraph("Módulo y Tema", styles["TableHead"]), Paragraph("Actividades Prácticas Clave", styles["TableHead"]), Paragraph("Entregable Evaluativo", styles["TableHead"])],
        [Paragraph("<b>Sesión 1</b>", styles["TableCellBold"]), Paragraph("M1: Metrología y Cintas", styles["TableCell"]), Paragraph("Calibración de flexómetros, compensación de gancho y medición de naves con cinta de 50m.", styles["TableCell"]), Paragraph("Ficha de medición de vanos y tolerancias.", styles["TableCellBold"])],
        [Paragraph("<b>Sesión 2</b>", styles["TableCellBold"]), Paragraph("M1: Láser y Triangulación", styles["TableCell"]), Paragraph("Modos de medición láser, áreas/volúmenes, Pitágoras y triangulación de recintos irregulares.", styles["TableCell"]), Paragraph("Reporte de medición láser y diagonales.", styles["TableCellBold"])],
        [Paragraph("<b>Sesión 3</b>", styles["TableCellBold"]), Paragraph("M1: Radiaciones y Croquis", styles["TableCell"]), Paragraph("Método de radiación desde punto base con distanciómetro láser y croquis a mano alzada.", styles["TableCell"]), Paragraph("Croquis a mano alzada acotado y diagonalizado.", styles["TableCellBold"])],
        [Paragraph("<b>Sesión 4</b>", styles["TableCellBold"]), Paragraph("M2: Croquizado en Tablet", styles["TableCell"]), Paragraph("Calibración de stylus, trazado con guías ortogonales, capas y exportación a DWG.", styles["TableCell"]), Paragraph("Croquis digital en tablet exportado a DWG.", styles["TableCellBold"])],
        [Paragraph("<b>Sesión 5</b>", styles["TableCellBold"]), Paragraph("M2/M3: Preparación CAD", styles["TableCell"]), Paragraph("Revisión de archivos vectoriales, notas de campo e inserción en plantilla Kinal .DWT.", styles["TableCell"]), Paragraph("Expediente de campo digital validado.", styles["TableCellBold"])],
        [Paragraph("<b>Sesión 6</b>", styles["TableCellBold"]), Paragraph("M3: AutoCAD y XREFs", styles["TableCell"]), Paragraph("Unidades métricas (0.000 m), OSNAP, Polar Tracking y enlazado de XREF a escala 1:1.", styles["TableCell"]), Paragraph("Planta base con XREF y muros perimetrales.", styles["TableCellBold"])],
        [Paragraph("<b>Sesión 7</b>", styles["TableCellBold"]), Paragraph("M3: Cotas Normalizadas", styles["TableCell"]), Paragraph("Estilos de cota DIMSTYLE Kinal, acotación continua y alineada sin solapes.", styles["TableCell"]), Paragraph("Planta arquitectónica completamente acotada.", styles["TableCellBold"])],
        [Paragraph("<b>Sesión 8</b>", styles["TableCellBold"]), Paragraph("M3: Bloques de Instalaciones", styles["TableCell"]), Paragraph("Inserción de bloques con atributos (tableros, tomas, luminarias, válvulas) y alineación a muros.", styles["TableCell"]), Paragraph("Planta con distribución de instalaciones.", styles["TableCellBold"])],
        [Paragraph("<b>Sesión 9</b>", styles["TableCellBold"]), Paragraph("M4: Diagramación Técnica", styles["TableCell"]), Paragraph("Dibujo de diagrama unifilar del tablero y esquema de tuberías con simbología normalizada.", styles["TableCell"]), Paragraph("Lámina de diagramas técnicos de instalaciones.", styles["TableCellBold"])],
        [Paragraph("<b>Sesión 10</b>", styles["TableCellBold"]), Paragraph("M4: Paper Space y Capstone", styles["TableCell"]), Paragraph("Maquetación a escala exacta 1:50 en Paper Space, membrete Kinal, plumillas CTB y sustentación.", styles["TableCell"]), Paragraph("<b>Expediente Capstone Aprobado (&ge; 75 pts)</b>.", styles["TableCellBold"])],
    ]
    t_cron = Table(cron_data, colWidths=[55, 120, 225, 132])
    t_cron.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#EDF2F7")),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_cron)
    story.append(Spacer(1, 10))

    # RÚBRICA 40H
    story.append(Paragraph("4. Sistema de Evaluación y Rúbrica Analítica Terminal (Nota Mínima: 75/100)", styles["H1"]))
    rub_data = [
        [Paragraph("Dimensión Evaluada", styles["TableHead"]), Paragraph("Excelente (90 - 100)", styles["TableHead"]), Paragraph("Satisfactorio (75 - 89)<br/><i>[Aprobatorio Kinal]</i>", styles["TableHead"]), Paragraph("En Desarrollo (< 75)", styles["TableHead"])],
        [
            Paragraph("<b>1. Metrología de Campo, Triangulación y Radiaciones</b>", styles["TableCellBold"]),
            Paragraph("Mediciones milimétricas exactas; compensación impecable del gancho; dominio de Pitágoras en láser; triangulación y radiaciones sin discrepancias.", styles["TableCell"]),
            Paragraph("Mediciones precisas con cintas y láser; aplica triangulación y radiación con errores dentro de tolerancia (&le; 5 mm) <b>(&ge; 75 pts)</b>.", styles["TableCell"]),
            Paragraph("Errores por descuido en referencia láser o catenaria; diagonales que no cierran; medidas falseadas.", styles["TableCell"])
        ],
        [
            Paragraph("<b>2. Croquizado Técnico</b><br/>(Mano Alzada y Tablet)", styles["TableCellBold"]),
            Paragraph("Proporción visual perfecta a mano alzada; croquis en tablet vectorizado con excelente gestión de capas; exportación limpia para CAD.", styles["TableCell"]),
            Paragraph("Croquis legible a mano alzada con cotas completas y diagonales; croquis en tablet en capas; archivo vectorial exportado correctamente <b>(&ge; 75 pts)</b>.", styles["TableCell"]),
            Paragraph("Croquis desproporcionado o confuso; omisión de capas en tablet; notas ilegibles o archivos dañados.", styles["TableCell"])
        ],
        [
            Paragraph("<b>3. AutoCAD 2D: Precisión, XREFs, Bloques y Paper Space</b>", styles["TableCellBold"]),
            Paragraph("Unidades métricas estrictas; uso impecable de OSNAP y Polar; XREF con ruta relativa; cotas legibles; bloques con atributos; Viewport a escala 1:50 y CTB perfecto.", styles["TableCell"]),
            Paragraph("Modela en AutoCAD con unidades métricas y capas; utiliza OSNAP y Polar; acotación completa; XREF y bloques; maquetación a escala 1:50 con membrete Kinal <b>(&ge; 75 pts)</b>.", styles["TableCell"]),
            Paragraph("Desorden en capas; dibujo fuera de escala en Paper Space; líneas duplicadas; ausencia de bloques.", styles["TableCell"])
        ],
        [
            Paragraph("<b>4. Ética y Trabajo Bien Hecho</b><br/>(Ideario Kinal)", styles["TableCellBold"]),
            Paragraph("Encarna de forma ejemplar el trabajo bien hecho. Cero tolerancia al falseamiento de cotas; puntualidad perfecta; cuidado del instrumental y espíritu de servicio.", styles["TableCell"]),
            Paragraph("Registro ordenado en libreta y bitácora; puntualidad, respeto a normas de seguridad de taller y de laboratorio <b>(&ge; 75 pts)</b>.", styles["TableCell"]),
            Paragraph("Indisciplina, tardanzas, descuido en el uso del instrumental o falseamiento intencional de medidas.", styles["TableCell"])
        ],
    ]
    t_rub = Table(rub_data, colWidths=[110, 140, 142, 140])
    t_rub.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#EDF2F7")),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_rub)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF 40h generado: {target_path}")

    import shutil
    shutil.copyfile(target_path, os.path.join(OUTPUT_DIR, "programa_formativo_levantamiento_planos_40h.pdf"))

if __name__ == "__main__":
    build_pdf_25h()
    build_pdf_40h()
