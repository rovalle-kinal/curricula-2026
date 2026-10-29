#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador de Documento PDF Corporativo:
Interpretación y Levantamiento de Diagramas P&ID (Fundación Kinal)
Simbología Técnica Normada, Relevamiento de Campo y Dibujo en AutoCAD 2D
Escuela Técnica Superior — Coordinación de Capacitación Corporativa
"""

import os
import sys

VENDOR_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "vendor")
if os.path.exists(VENDOR_DIR):
    sys.path.append(VENDOR_DIR)

from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, HRFlowable, PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COURSE_DIR = os.path.join(WORKSPACE_DIR, "Cursos", "Levantamiento_Planos_Diagramas")
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
            self.drawRightString(572, 755, "Interpretación y Levantamiento de Diagramas P&ID")
            self.setStrokeColor(C_BORDER)
            self.setLineWidth(0.5)
            self.line(40, 748, 572, 748)

        # Pie de página en todas las páginas
        self.setStrokeColor(C_BORDER)
        self.setLineWidth(0.5)
        self.line(40, 42, 572, 42)
        
        self.setFont("Helvetica", 7.5)
        self.setFillColor(C_TEXT_MUTED)
        self.drawString(40, 30, "Capacitación Técnica Corporativa • Marco DQR Nivel 4-5 • Nota Mínima Aprobatoria: 75/100 Puntos")
        
        page_str = f"Página {self._pageNumber} de {page_count}"
        self.drawRightString(572, 30, page_str)
        self.restoreState()

def build_pdf():
    os.makedirs(COURSE_DIR, exist_ok=True)
    target_path = os.path.join(COURSE_DIR, "programa_formativo_diagramas_industriales.pdf")
    doc = SimpleDocTemplate(target_path, pagesize=letter, leftMargin=40, rightMargin=40, topMargin=42, bottomMargin=50)

    base = getSampleStyleSheet()
    styles = {
        "Title": ParagraphStyle("DocTitle", fontName="Helvetica-Bold", fontSize=14, leading=17, textColor=C_KINAL_BLUE),
        "Subtitle": ParagraphStyle("DocSub", fontName="Helvetica-Oblique", fontSize=8, leading=11, textColor=C_TEXT_MUTED),
        "H1": ParagraphStyle("H1", fontName="Helvetica-Bold", fontSize=10, leading=13, textColor=C_KINAL_BLUE, spaceBefore=7, spaceAfter=3),
        "H2": ParagraphStyle("H2", fontName="Helvetica-Bold", fontSize=8.5, leading=11, textColor=C_KINAL_NAVY, spaceBefore=4, spaceAfter=2),
        "Body": ParagraphStyle("Body", fontName="Helvetica", fontSize=7.2, leading=9.8, textColor=C_KINAL_DARK),
        "CalloutTitle": ParagraphStyle("CalloutTitle", fontName="Helvetica-Bold", fontSize=7.2, leading=9.8, textColor=C_KINAL_BLUE),
        "CalloutText": ParagraphStyle("CalloutText", fontName="Helvetica", fontSize=7.2, leading=9.8, textColor=C_KINAL_DARK),
        "TableHead": ParagraphStyle("TableHead", fontName="Helvetica-Bold", fontSize=7.2, leading=9.2, textColor=C_KINAL_BLUE, alignment=1),
        "TableCell": ParagraphStyle("TableCell", fontName="Helvetica", fontSize=6.8, leading=8.8, textColor=C_KINAL_DARK),
        "TableCellBold": ParagraphStyle("TableCellBold", fontName="Helvetica-Bold", fontSize=6.8, leading=8.8, textColor=C_KINAL_DARK),
        "TableCellCenter": ParagraphStyle("TableCellCenter", fontName="Helvetica", fontSize=6.8, leading=8.8, textColor=C_KINAL_DARK, alignment=1),
        "TableCellCenterBold": ParagraphStyle("TableCellCenterBold", fontName="Helvetica-Bold", fontSize=6.8, leading=8.8, textColor=C_KINAL_DARK, alignment=1),
    }

    story = []

    # =========================================================================
    # PÁGINA 1: PRESENTACIÓN EJECUTIVA DEL CURSO Y TEMARIO RESUMIDO
    # (Toda la presentación del curso en una sola hoja ejecutiva)
    # =========================================================================

    # ENCABEZADO CON LOGO INSTITUCIONAL
    if os.path.exists(LOGO_PATH):
        img = Image(LOGO_PATH, width=38, height=38)
        header_text = [
            Paragraph("FUNDACIÓN KINAL • ESCUELA TÉCNICA SUPERIOR", ParagraphStyle("HPre", fontName="Helvetica-Bold", fontSize=8.5, leading=10, textColor=C_KINAL_BLUE)),
            Paragraph("Interpretación y Levantamiento de Diagramas P&ID", styles["Title"]),
            Paragraph("Simbología Técnica Normada, Relevamiento de Campo y Dibujo en AutoCAD 2D (40 Horas Híbridas)", styles["Subtitle"])
        ]
        t_header = Table([[img, header_text]], colWidths=[46, 486])
        t_header.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('LEFTPADDING', (1,0), (1,0), 6),
            ('BOTTOMPADDING', (0,0), (-1,-1), 0),
            ('TOPPADDING', (0,0), (-1,-1), 0),
        ]))
        story.append(t_header)

    story.append(Spacer(1, 3))
    story.append(HRFlowable(width="100%", thickness=1.5, color=C_KINAL_BLUE, spaceBefore=1, spaceAfter=4))

    # FICHA TÉCNICA CORPORATIVA
    ficha_data = [
        [Paragraph("Programa", styles["TableCellBold"]), Paragraph("<b>Interpretación y Levantamiento de Diagramas P&ID</b>", styles["TableCell"])],
        [Paragraph("Población Objetivo", styles["TableCellBold"]), Paragraph("<b>6 a 10 colaboradores técnicos</b> (Mecánicos, Electricistas, Instrumentistas y Dibujantes Técnicos)", styles["TableCell"])],
        [Paragraph("Carga Horaria y Formato", styles["TableCellBold"]), Paragraph("<b>40 horas pedagógicas híbridas</b> (10 sesiones de 4 horas / 240 min c/u):<br/>• <b>20% Virtual Sincrónico (8h / 2 ses.):</b> Simbología técnica normada y lectura analítica en Microsoft Teams.<br/>• <b>80% Presencial Práctico (32h / 8 ses.):</b> Walkdown en planta, metrología de tuberías y dibujo en Lab CAD.", styles["TableCell"])],
        [Paragraph("Horarios y Fechas", styles["TableCellBold"]), Paragraph("Adaptable a jornada de planta (L-J 07:00-16:00 / V 07:00-15:00): Martes y Jueves (5 sem.) o intensivo sabatino. Inicio: <b>Diciembre 2026 / Enero 2027</b>.", styles["TableCell"])],
        [Paragraph("Enfoque Formativo", styles["TableCellBold"]), Paragraph("<b>Lectura Analítica de Lazos</b> &nbsp;|&nbsp; <b>Relevamiento de Campo (Walkdown y Croquis)</b> &nbsp;|&nbsp; <b>Dibujo en AutoCAD 2D</b> &nbsp;|&nbsp; <b>Potencia Fluida</b>", styles["TableCell"])],
        [Paragraph("Nota Mínima Aprobatoria", styles["TableCellBold"]), Paragraph("<b>75 puntos sobre 100</b> en talleres de campo, proyectos CAD y defensa del Proyecto Capstone", styles["TableCell"])],
    ]
    t_ficha = Table(ficha_data, colWidths=[110, 422])
    t_ficha.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_BG_LIGHT),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_ficha)
    story.append(Spacer(1, 4))

    # MARCO FILOSÓFICO Y EL PRINCIPIO DEL «TRABAJO BIEN HECHO»
    story.append(Paragraph("1. Marco Filosófico y Principio del «Trabajo Bien Hecho»", styles["H1"]))
    
    def make_callout(bold_lbl, text):
        content = [
            Paragraph(bold_lbl, styles["CalloutTitle"]),
            Spacer(1, 1),
            Paragraph(text, styles["CalloutText"])
        ]
        t = Table([[content]], colWidths=[532])
        t.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), C_BG_LIGHT),
            ('LINELEFT', (0,0), (-1,-1), 3, C_KINAL_BLUE),
            ('BOX', (0,0), (-1,-1), 0.5, C_BORDER),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('TOPPADDING', (0,0), (-1,-1), 2),
            ('BOTTOMPADDING', (0,0), (-1,-1), 2),
            ('LEFTPADDING', (0,0), (-1,-1), 6),
            ('RIGHTPADDING', (0,0), (-1,-1), 5),
        ]))
        return t

    story.append(make_callout("Misión Institucional de Kinal:", "«Formar a jóvenes y adultos a través de una educación integral, con énfasis en las áreas técnicas y tecnológicas, influyendo positivamente en su trabajo, su familia y la sociedad»."))
    story.append(Spacer(1, 2))
    story.append(make_callout("Valores Nucleares de Kinal:", "«Visión cristiana de la vida. Respeto a la dignidad de la persona. Espíritu de servicio. Trabajo bien hecho. Libertad personal responsable»."))
    story.append(Spacer(1, 3))

    story.append(Paragraph(
        "En la ingeniería de planta, un plano técnico es una directriz operativa crítica donde el <b>trabajo bien hecho</b> se manifiesta en: "
        "<b>1) Fidelidad As-Built Real:</b> Dibujar con honestidad lo existente en campo sin falsear trayectorias; "
        "<b>2) Disciplina CAD:</b> Estructura impecable de capas por fluido, bloques inteligentes con atributos normados y rotulado claro; "
        "<b>3) Seguridad y Confiabilidad:</b> Rotulado exacto de válvulas de alivio, sentidos de flujo y fallas seguras para maniobras LOTO; y "
        "<b>4) Servicio Multidisciplinario:</b> Crear información gráfica unificada que facilite la cooperación entre mecánicos, electricistas e instrumentistas.",
        styles["Body"]
    ))
    story.append(Spacer(1, 4))

    # TEMARIO CURRICULAR RESUMIDO (EN LA HOJA 1)
    # Requisito explícito: Textos justificados al centro vertical de las celdas (VALIGN MIDDLE)
    story.append(Paragraph("2. Temario Curricular Resumido (5 Módulos / 40 Horas Híbridas)", styles["H1"]))
    
    temario_resumido_data = [
        [
            Paragraph("Módulo Curricular", styles["TableHead"]),
            Paragraph("Modalidad y Horas", styles["TableHead"]),
            Paragraph("Síntesis de Contenidos Nucleares de Interpretación y Dibujo", styles["TableHead"])
        ],
        [
            Paragraph("<b>Módulo 1:</b><br/>Fundamentos de P&ID y Simbología Técnica Normada", styles["TableCellBold"]),
            Paragraph("<b>8 Horas</b><br/>Virtual (Teams)", styles["TableCellCenterBold"]),
            Paragraph("Simbología técnica normada, globos e identificación de instrumentos, variables (P, T, F, L), líneas de señal (eléctrica/neumática/digital), códigos de tuberías estandarizados y lazos con falla segura (FC/FO).", styles["TableCell"])
        ],
        [
            Paragraph("<b>Módulo 2:</b><br/>Simbología de Válvulas, Actuadores y Equipos", styles["TableCellBold"]),
            Paragraph("<b>8 Horas</b><br/>Virtual (Teams)", styles["TableCellCenterBold"]),
            Paragraph("Simbología de válvulas manuales y de control, actuadores neumáticos y eléctricos, recipientes a presión, tanques, bombas y compresores. Rastreo analítico de líneas de proceso (Line Tracing).", styles["TableCell"])
        ],
        [
            Paragraph("<b>Módulo 3:</b><br/>Levantamiento de Campo, Metrología y Croquis", styles["TableCellBold"]),
            Paragraph("<b>8 Horas</b><br/>Planta / Taller", styles["TableCellCenterBold"]),
            Paragraph("Metodología de walkdown, metrología de tuberías con vernier (diámetro exterior, NPS y cédula Schedule), accesorios y uniones bridadas estandarizadas. Croquizado proporcional a mano alzada y tablet.", styles["TableCell"])
        ],
        [
            Paragraph("<b>Módulo 4:</b><br/>Modelado de P&ID en AutoCAD 2D", styles["TableCellBold"]),
            Paragraph("<b>8 Horas</b><br/>Laboratorio CAD", styles["TableCellCenterBold"]),
            Paragraph("Plantilla institucional (.DWT), capas estandarizadas por fluido/servicio, herramientas de precisión (OSNAP), creación de bloques inteligentes con atributos editables (ATTDEF) y resolución de cruces.", styles["TableCell"])
        ],
        [
            Paragraph("<b>Módulo 5:</b><br/>Esquemas de Potencia Fluida y Proyecto Capstone", styles["TableCellBold"]),
            Paragraph("<b>8 Horas</b><br/>Taller + Lab CAD", styles["TableCellCenterBold"]),
            Paragraph("Simbología estandarizada de neumática e hidráulica (FRL, válvulas direccionales, cilindros), extracción automática de tablas con EATTEXT, maquetación ejecutiva y sustentación oral grupal (&ge; 75 pts).", styles["TableCell"])
        ],
    ]
    
    t_tem_res = Table(temario_resumido_data, colWidths=[130, 80, 322])
    t_tem_res.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#EDF2F7")),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        # TEXTO JUSTIFICADO AL CENTRO VERTICAL DE LAS CELDAS
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_tem_res)

    # =========================================================================
    # SALTO DE PÁGINA: LA PLANIFICACIÓN EN OTRA HOJA EXCLUSIVA (PÁGINA 2)
    # =========================================================================
    story.append(PageBreak())

    story.append(Paragraph("3. Planificación y Dosificación de Sesiones (10 Sesiones / 40 Horas Totales)", styles["H1"]))
    story.append(Paragraph(
        "A continuación se presenta la planificación detallada sesión por sesión, articulando las actividades analíticas virtuales sincrónicas en Microsoft Teams "
        "con los talleres presenciales de inspección de campo en planta y modelado estandarizado en Laboratorio CAD:",
        styles["Body"]
    ))
    story.append(Spacer(1, 4))

    cron_data = [
        [Paragraph("Sesión", styles["TableHead"]), Paragraph("Modalidad y Entorno", styles["TableHead"]), Paragraph("Actividades de Interpretación, Campo y CAD", styles["TableHead"]), Paragraph("Entregable Evaluativo", styles["TableHead"])],
        [
            Paragraph("<b>Sesión 1</b><br/>(4 Horas)", styles["TableCellCenterBold"]),
            Paragraph("<b>Virtual Sincrónico</b><br/>Microsoft Teams", styles["TableCellCenter"]),
            Paragraph("Simbología técnica normada, globos de instrumentos, letras modificadoras de variables, líneas de señal y código de tuberías.", styles["TableCell"]),
            Paragraph("Taller de decodificación de símbolos y tags de instrumentos (&ge; 75 pts).", styles["TableCellBold"])
        ],
        [
            Paragraph("<b>Sesión 2</b><br/>(4 Horas)", styles["TableCellCenterBold"]),
            Paragraph("<b>Virtual Sincrónico</b><br/>Microsoft Teams", styles["TableCellCenter"]),
            Paragraph("Simbología estandarizada de válvulas, actuadores, equipos estáticos/dinámicos y rastreo de líneas de proceso (Line Tracing).", styles["TableCell"]),
            Paragraph("Taller de rastreo de líneas e interpretación de P&ID industrial (&ge; 75 pts).", styles["TableCellBold"])
        ],
        [
            Paragraph("<b>Sesión 3</b><br/>(4 Horas)", styles["TableCellCenterBold"]),
            Paragraph("<b>Presencial Práctico</b><br/>Planta / Taller Kinal", styles["TableCellCenter"]),
            Paragraph("Metodología del walkdown, medición dimensional con calibrador vernier (OD, NPS, Schedule), uniones bridadas estandarizadas y accesorios.", styles["TableCell"]),
            Paragraph("Ficha técnica de relevamiento dimensional de tuberías en campo.", styles["TableCellBold"])
        ],
        [
            Paragraph("<b>Sesión 4</b><br/>(4 Horas)", styles["TableCellCenterBold"]),
            Paragraph("<b>Presencial Práctico</b><br/>Planta / Taller Kinal", styles["TableCellCenter"]),
            Paragraph("Croquizado rápido a mano alzada y en tablet: proporción visual, registro de tags in situ, válvulas, bypass y sentidos de flujo.", styles["TableCell"]),
            Paragraph("Croquis de campo consolidado y validado en brigada (&ge; 75 pts).", styles["TableCellBold"])
        ],
        [
            Paragraph("<b>Sesión 5</b><br/>(4 Horas)", styles["TableCellCenterBold"]),
            Paragraph("<b>Presencial CAD</b><br/>Laboratorio CAD", styles["TableCellCenter"]),
            Paragraph("Entorno CAD, plantilla institucional (.DWT), capas normalizadas por fluido, OSNAP, calco y trazado vectorial de líneas principales.", styles["TableCell"]),
            Paragraph("Plano DWG estructurado en capas normalizadas (&ge; 75 pts).", styles["TableCellBold"])
        ],
        [
            Paragraph("<b>Sesión 6</b><br/>(4 Horas)", styles["TableCellCenterBold"]),
            Paragraph("<b>Presencial CAD</b><br/>Laboratorio CAD", styles["TableCellCenter"]),
            Paragraph("Creación de bloques inteligentes con atributos editables (ATTDEF), rotulado de tags normalizados y resolución gráfica de cruces de líneas.", styles["TableCell"]),
            Paragraph("Plano P&ID en CAD con bloques y tags editables (&ge; 75 pts).", styles["TableCellBold"])
        ],
        [
            Paragraph("<b>Sesión 7</b><br/>(4 Horas)", styles["TableCellCenterBold"]),
            Paragraph("<b>Presencial Práctico</b><br/>Taller / Lab. CAD", styles["TableCellCenter"]),
            Paragraph("Simbología estandarizada de potencia fluida: unidades FRL, válvulas direccionales y modelado de circuitos neumáticos en AutoCAD.", styles["TableCell"]),
            Paragraph("Esquema neumático funcional dibujado en AutoCAD (&ge; 75 pts).", styles["TableCellBold"])
        ],
        [
            Paragraph("<b>Sesión 8</b><br/>(4 Horas)", styles["TableCellCenterBold"]),
            Paragraph("<b>Presencial Práctico</b><br/>Taller / Lab. CAD", styles["TableCellCenter"]),
            Paragraph("Simbología hidráulica estandarizada: unidades de potencia HPU, válvulas de alivio, válvulas 4/3 y modelado de circuitos oleohidráulicos.", styles["TableCell"]),
            Paragraph("Esquema hidráulico funcional dibujado en AutoCAD (&ge; 75 pts).", styles["TableCellBold"])
        ],
        [
            Paragraph("<b>Sesión 9</b><br/>(4 Horas)", styles["TableCellCenterBold"]),
            Paragraph("<b>Presencial CAD</b><br/>Laboratorio CAD", styles["TableCellCenter"]),
            Paragraph("Extracción automática de datos (EATTEXT) para tablas de equipos/válvulas, maquetación en Layouts (espacio papel) y plumillas .CTB.", styles["TableCell"]),
            Paragraph("Lámina P&ID maquetada con tablas y membrete oficial Kinal (&ge; 75 pts).", styles["TableCellBold"])
        ],
        [
            Paragraph("<b>Sesión 10</b><br/>(4 Horas)", styles["TableCellCenterBold"]),
            Paragraph("<b>Presencial Panel</b><br/>Laboratorio CAD", styles["TableCellCenter"]),
            Paragraph("Auditoría terminal as-built, exportación a PDF vectorial y sustentación técnica oral grupal del Proyecto Capstone ante el panel evaluador.", styles["TableCell"]),
            Paragraph("<b>Expediente Capstone Defendido y Acreditado (&ge; 75 pts)</b>.", styles["TableCellBold"])
        ],
    ]
    t_cron = Table(cron_data, colWidths=[55, 95, 247, 135])
    t_cron.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#EDF2F7")),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_cron)

    # =========================================================================
    # SALTO DE PÁGINA: EVALUACIÓN Y RÚBRICA EN PÁGINA DEDICADA (PÁGINA 3)
    # =========================================================================
    story.append(PageBreak())

    story.append(Paragraph("4. Sistema de Evaluación y Rúbrica Analítica Terminal (Nota Mínima Aprobatoria: 75/100 Puntos)", styles["H1"]))
    story.append(Paragraph(
        "El modelo de evaluación de competencias técnicas de Fundación Kinal califica la suficiencia demostrada en cuatro dimensiones integradas, "
        "conforme a los estándares del Marco de Cualificaciones (Nivel 4-5) y el principio del trabajo bien hecho:",
        styles["Body"]
    ))
    story.append(Spacer(1, 6))

    rub_data = [
        [Paragraph("Dimensión Evaluada", styles["TableHead"]), Paragraph("Nivel Excelente (90 - 100)", styles["TableHead"]), Paragraph("Nivel Satisfactorio (75 - 89)<br/><i>[Aprobatorio Kinal]</i>", styles["TableHead"]), Paragraph("En Desarrollo (< 75)", styles["TableHead"])],
        [
            Paragraph("<b>1. Saber Técnico</b><br/>(Simbología y Normas)", styles["TableCellBold"]),
            Paragraph("Decodificación perfecta de símbolos y tags de instrumentos; correlación exacta de tuberías NPS/Schedule; dominio de simbología de válvulas y modos de falla.", styles["TableCell"]),
            Paragraph("Identifica símbolos y tags de instrumentos principales; determina diámetros NPS; interpreta diagramas P&ID con precisión funcional <b>(&ge; 75 pts)</b>.", styles["TableCell"]),
            Paragraph("Confunde códigos de instrumentos o desconoce cómo determinar diámetros nominales; errores graves de lectura funcional.", styles["TableCell"])
        ],
        [
            Paragraph("<b>2. Saber Hacer</b><br/>(Relevamiento y Croquis)", styles["TableCellBold"]),
            Paragraph("Medición dimensional exacta con calibrador; croquis de campo técnico, proporcional y limpio en tablet/papel; registro exhaustivo de tags y sentidos de flujo.", styles["TableCell"]),
            Paragraph("Releva diámetros y elabora croquis comprensibles con simbología técnica normalizada; registra componentes sin omisiones críticas <b>(&ge; 75 pts)</b>.", styles["TableCell"]),
            Paragraph("Croquis desproporcionado, ilegible o con bypass omitidos; errores e inexactitudes en la toma de medidas físicas en campo.", styles["TableCell"])
        ],
        [
            Paragraph("<b>3. Saber Hacer</b><br/>(Dibujo CAD y Tablas)", styles["TableCellBold"]),
            Paragraph("Plano DWG impecable: capas normalizadas por fluido, bloques inteligentes con atributos editables, cruces resueltos, tablas automáticas EATTEXT y maquetación a escala.", styles["TableCell"]),
            Paragraph("Dibuja el P&ID en AutoCAD con capas organizadas; inserta bloques con atributos; genera tablas de equipos y maqueta con membrete Kinal <b>(&ge; 75 pts)</b>.", styles["TableCell"]),
            Paragraph("Líneas de tubería desconectadas, desorden de capas, textos solapados sobre líneas de proceso o ausencia de bloques inteligentes.", styles["TableCell"])
        ],
        [
            Paragraph("<b>4. Saber Ser y Estar</b><br/>(Trabajo Bien Hecho y LOTO)", styles["TableCellBold"]),
            Paragraph("Encarna con excelencia el trabajo bien hecho: verdad en el plano as-built sin inventar datos, rigor en seguridad LOTO y defensa técnica sólida ante el panel.", styles["TableCell"]),
            Paragraph("Compromiso ético y técnico; participa activamente en la brigada de relevamiento y sustenta con solvencia su proyecto Capstone <b>(&ge; 75 pts)</b>.", styles["TableCell"]),
            Paragraph("Falseamiento de datos en el plano, desatención a normas de seguridad o débil defensa técnica grupal.", styles["TableCell"])
        ],
    ]
    t_rub = Table(rub_data, colWidths=[110, 140, 142, 140])
    t_rub.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#EDF2F7")),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 5.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5.5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_rub)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF generado exitosamente en: {target_path}")

if __name__ == "__main__":
    build_pdf()
