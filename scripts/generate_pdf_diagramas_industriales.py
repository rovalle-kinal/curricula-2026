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
    doc = SimpleDocTemplate(target_path, pagesize=letter, leftMargin=40, rightMargin=40, topMargin=45, bottomMargin=55)

    base = getSampleStyleSheet()
    styles = {
        "Title": ParagraphStyle("DocTitle", fontName="Helvetica-Bold", fontSize=15, leading=19, textColor=C_KINAL_BLUE),
        "Subtitle": ParagraphStyle("DocSub", fontName="Helvetica-Oblique", fontSize=8.5, leading=12, textColor=C_TEXT_MUTED),
        "H1": ParagraphStyle("H1", fontName="Helvetica-Bold", fontSize=11, leading=15, textColor=C_KINAL_BLUE, spaceBefore=10, spaceAfter=4),
        "H2": ParagraphStyle("H2", fontName="Helvetica-Bold", fontSize=9, leading=12, textColor=C_KINAL_NAVY, spaceBefore=6, spaceAfter=3),
        "Body": ParagraphStyle("Body", fontName="Helvetica", fontSize=7.5, leading=10.5, textColor=C_KINAL_DARK),
        "CalloutTitle": ParagraphStyle("CalloutTitle", fontName="Helvetica-Bold", fontSize=7.5, leading=10.5, textColor=C_KINAL_BLUE),
        "CalloutText": ParagraphStyle("CalloutText", fontName="Helvetica", fontSize=7.5, leading=10.5, textColor=C_KINAL_DARK),
        "TableHead": ParagraphStyle("TableHead", fontName="Helvetica-Bold", fontSize=7.5, leading=9.5, textColor=C_KINAL_BLUE),
        "TableCell": ParagraphStyle("TableCell", fontName="Helvetica", fontSize=7, leading=9.2, textColor=C_KINAL_DARK),
        "TableCellBold": ParagraphStyle("TableCellBold", fontName="Helvetica-Bold", fontSize=7, leading=9.2, textColor=C_KINAL_DARK),
    }

    story = []

    # =========================================================================
    # PÁGINA 1: FICHA TÉCNICA, QUÉ ES P&ID, TRABAJO BIEN HECHO Y TEMARIO
    # =========================================================================

    # ENCABEZADO CON LOGO
    if os.path.exists(LOGO_PATH):
        img = Image(LOGO_PATH, width=42, height=42)
        header_text = [
            Paragraph("FUNDACIÓN KINAL • ESCUELA TÉCNICA SUPERIOR", ParagraphStyle("HPre", fontName="Helvetica-Bold", fontSize=9, leading=11, textColor=C_KINAL_BLUE)),
            Paragraph("Interpretación y Levantamiento de Diagramas P&ID", styles["Title"]),
            Paragraph("Simbología Técnica Normada, Relevamiento de Campo y Dibujo en AutoCAD 2D (40 Horas Híbridas)", styles["Subtitle"])
        ]
        t_header = Table([[img, header_text]], colWidths=[50, 482])
        t_header.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('LEFTPADDING', (1,0), (1,0), 6),
            ('BOTTOMPADDING', (0,0), (-1,-1), 0),
            ('TOPPADDING', (0,0), (-1,-1), 0),
        ]))
        story.append(t_header)

    story.append(Spacer(1, 4))
    story.append(HRFlowable(width="100%", thickness=1.5, color=C_KINAL_BLUE, spaceBefore=2, spaceAfter=5))

    # FICHA TÉCNICA CORPORATIVA (SIN CÓDIGO)
    ficha_data = [
        [Paragraph("Programa", styles["TableCellBold"]), Paragraph("<b>Interpretación y Levantamiento de Diagramas P&ID</b>", styles["TableCell"])],
        [Paragraph("Población Objetivo", styles["TableCellBold"]), Paragraph("<b>6 a 10 colaboradores técnicos</b> (Mecánicos, Electricistas, Instrumentistas y Dibujantes Técnicos)", styles["TableCell"])],
        [Paragraph("Carga Horaria y Formato", styles["TableCellBold"]), Paragraph("<b>40 horas pedagógicas híbridas</b> (10 sesiones de 4 horas / 240 min c/u):<br/>• <b>20% Virtual Sincrónico (8 Horas / 2 sesiones):</b> Fundamentación de P&ID, simbología técnica normada y lectura analítica en Teams.<br/>• <b>80% Presencial Práctico (32 Horas / 8 sesiones):</b> Relevamiento en planta (walkdown, croquis, metrología de tuberías) y dibujo en Laboratorio CAD.", styles["TableCell"])],
        [Paragraph("Horarios y Fechas", styles["TableCellBold"]), Paragraph("Adaptado a jornada de planta (L-J 07:00-16:00 / V 07:00-15:00): Martes y Jueves (5 sem.) o Viernes intensivo. Inicio: <b>Diciembre 2026</b> o <b>Enero 2027</b>.", styles["TableCell"])],
        [Paragraph("Enfoque Formativo", styles["TableCellBold"]), Paragraph("<b>Lectura e Interpretación Analítica</b> &nbsp;|&nbsp; <b>Relevamiento de Campo (Walkdown y Croquis)</b> &nbsp;|&nbsp; <b>Dibujo Estandarizado en AutoCAD 2D</b> &nbsp;|&nbsp; <b>Esquemas de Potencia Fluida</b>", styles["TableCell"])],
        [Paragraph("Nota Mínima Aprobatoria", styles["TableCellBold"]), Paragraph("<b>75 puntos sobre 100</b> en evaluaciones de campo, laboratorios CAD y sustentación del Proyecto Capstone", styles["TableCell"])],
    ]
    t_ficha = Table(ficha_data, colWidths=[115, 417])
    t_ficha.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_BG_LIGHT),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_ficha)
    story.append(Spacer(1, 6))

    # SECCIÓN: ¿QUÉ ES UN DIAGRAMA P&ID?
    story.append(Paragraph("1. ¿Qué es un Diagrama P&ID (Piping and Instrumentation Diagram)?", styles["H1"]))
    story.append(Paragraph(
        "Un <b>P&ID</b> es el plano técnico maestro de ingeniería que describe la interconexión esquemática y funcional de una planta industrial. "
        "No representa una distribución física a escala geográfica, sino la <b>lógica de proceso y control</b> estructurada en cuatro componentes fundamentales: "
        "<b>1) Equipos de proceso</b> (tanques, recipientes a presión, bombas centrífugas/desplazamiento positivo, compresores, intercambiadores); "
        "<b>2) Red de tuberías y líneas de servicio</b> (especificación de diámetro nominal NPS, cédula Schedule, códigos de fluido y flechas de sentido de flujo); "
        "<b>3) Válvulas y actuadores</b> (válvulas manuales, válvulas de control automático y válvulas de seguridad/alivio con indicación de su modo de falla segura); y "
        "<b>4) Instrumentación y lazos de control</b> (símbolos y globos de identificación normalizados con códigos alfanuméricos y líneas de señal eléctrica, neumática o digital).",
        styles["Body"]
    ))
    story.append(Spacer(1, 5))

    # SECCIÓN: MARCO FILOSÓFICO Y EL TRABAJO BIEN HECHO
    story.append(Paragraph("2. Marco Filosófico y el Principio del «Trabajo Bien Hecho»", styles["H1"]))
    
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
            ('TOPPADDING', (0,0), (-1,-1), 2.5),
            ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
            ('LEFTPADDING', (0,0), (-1,-1), 7),
            ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ]))
        return t

    story.append(make_callout("Misión Institucional de Kinal:", "«Formar a jóvenes y adultos a través de una educación integral, con énfasis en las áreas técnicas y tecnológicas, influyendo positivamente en su trabajo, su familia y la sociedad»."))
    story.append(Spacer(1, 2))
    story.append(make_callout("Valores Nucleares de Kinal:", "«Visión cristiana de la vida. Respeto a la dignidad de la persona. Espíritu de servicio. Trabajo bien hecho. Libertad personal responsable»."))
    story.append(Spacer(1, 3))

    story.append(Paragraph("El Principio del «Trabajo Bien Hecho» en la Interpretación y Dibujo de Planos:", styles["H2"]))
    story.append(Paragraph(
        "En la planta industrial, un plano no es un boceto decorativo; es la guía operativa y legal sobre la que se ejecutan mantenimientos y procedimientos de seguridad crítica. "
        "En este curso, el <b>trabajo bien hecho</b> se concreta en: "
        "<b>1) Verdad y Fidelidad Técnica (As-Built Real):</b> Compromiso ético de reflejar en el dibujo exactamente lo verificado en campo, sin suponer trayectorias ni omitir accesorios; "
        "<b>2) Prolijidad Gráfica y Disciplina CAD:</b> Estructuración estricta de capas por fluido, bloques inteligentes con atributos normalizados, textos nítidos y escalas coherentes; "
        "<b>3) Protección de la Vida y Confiabilidad:</b> Rotulado fidedigno de sentidos de flujo, válvulas de alivio y modos de falla para garantizar maniobras de bloqueo LOTO 100% seguras; y "
        "<b>4) Sentido de Servicio Multidisciplinario:</b> Elaborar planos comprensibles y estandarizados que sirvan de puente de colaboración entre mecánicos, electricistas e instrumentistas.",
        styles["Body"]
    ))
    story.append(Spacer(1, 6))

    # =========================================================================
    # SALTO DE PÁGINA: TEMARIO CURRICULAR (PÁGINA 2)
    # =========================================================================
    story.append(PageBreak())

    # SECCIÓN: TEMARIO JERÁRQUICO
    story.append(Paragraph("3. Temario Curricular Jerárquico (5 Módulos / 40 Horas Híbridas)", styles["H1"]))
    temario_data = [
        [Paragraph("Módulo", styles["TableHead"]), Paragraph("Modalidad", styles["TableHead"]), Paragraph("Contenidos Nucleares de Interpretación y Dibujo", styles["TableHead"])],
        [
            Paragraph("<b>Módulo 1:</b><br/>Fundamentos de P&ID y Simbología Técnica", styles["TableCellBold"]),
            Paragraph("<b>8 Horas</b><br/>Virtual (Teams)", styles["TableCell"]),
            Paragraph("• Qué es un P&ID, anatomía del plano y jerarquía técnica (BFD, PFD, P&ID).<br/>• <b>Simbología Técnica Normada:</b> Símbolos y globos de instrumentos, letras de variables (P, T, F, L), letras modificadoras de función (I, C, T, V) y líneas de señal (eléctrica, neumática, digital).<br/>• Códigos de tuberías estandarizados (Line Numbering), código de colores y lectura de lazos de control con modos de falla segura (FC, FO, FL).", styles["TableCell"])
        ],
        [
            Paragraph("<b>Módulo 2:</b><br/>Simbología de Válvulas y Equipos", styles["TableCellBold"]),
            Paragraph("<b>8 Horas</b><br/>Virtual (Teams)", styles["TableCell"]),
            Paragraph("• Simbología estandarizada de válvulas: compuerta, globo, bola, mariposa, retención (check), diafragma, aguja, alivio y seguridad (PSV/PRV).<br/>• Actuadores gráficos: manual, diafragma neumático, motor eléctrico y solenoide.<br/>• Representación gráfica de recipientes a presión, tanques, bombas centrífugas/desplazamiento positivo, compresores e intercambiadores.<br/>• Rastreo analítico de líneas de proceso (Line Tracing) e interpretación de planos P&ID industriales completos.", styles["TableCell"])
        ],
        [
            Paragraph("<b>Módulo 3:</b><br/>Levantamiento de Campo y Croquis", styles["TableCellBold"]),
            Paragraph("<b>8 Horas</b><br/>Planta / Taller", styles["TableCell"]),
            Paragraph("• Metodología del levantamiento en campo (Field Walkdown): límites de batería y protocolos EPP.<br/>• Metrología de tuberías: medición de diámetro exterior (OD), determinación de diámetro nominal NPS y cédula Schedule con calibrador vernier.<br/>• Reconocimiento de accesorios, uniones bridadas estandarizadas (Clase 150/300 RF/FF) y conexiones roscadas NPT.<br/>• Técnicas de croquizado rápido a mano alzada y en tablet con stylus: proporción visual, ortogonalidad y validación en brigada.", styles["TableCell"])
        ],
        [
            Paragraph("<b>Módulo 4:</b><br/>Dibujo de P&ID en AutoCAD 2D", styles["TableCellBold"]),
            Paragraph("<b>8 Horas</b><br/>Laboratorio CAD", styles["TableCell"]),
            Paragraph("• Configuración del espacio CAD: plantilla institucional (.DWT) y sistema de capas normalizadas por fluido (L-PROCESO, L-SERVICIOS, E-EQUIPOS, E-VALVULAS, I-INSTRUMENTOS, TEXTOS).<br/>• Herramientas de dibujo ortogonal y precisión esquemática: OSNAP y Polar Tracking.<br/>• Creación de bloques inteligentes con atributos editables (ATTDEF/BATTMAN) para identificación de instrumentos.<br/>• Resolución gráfica de cruces de líneas (puentes/arcos vs. cruces limpios sin conexión) y derivaciones.", styles["TableCell"])
        ],
        [
            Paragraph("<b>Módulo 5:</b><br/>Esquemas de Fluidos y Proyecto Capstone", styles["TableCellBold"]),
            Paragraph("<b>8 Horas</b><br/>Taller + CAD", styles["TableCell"]),
            Paragraph("• Simbología estandarizada de potencia fluida: unidades FRL, válvulas direccionales (3/2, 5/2, 4/3), cilindros neumáticos e hidráulicos.<br/>• Extracción automática de tablas de instrumentos y válvulas en AutoCAD con comando <code>EATTEXT</code>.<br/>• Maquetación ejecutiva en Layouts con cajetín corporativo Kinal y plumillas .CTB.<br/>• <b>Sustentación del Proyecto Capstone:</b> Presentación y defensa técnica grupal del plano P&ID as-built terminado (&ge; 75 pts).", styles["TableCell"])
        ],
    ]
    t_tem = Table(temario_data, colWidths=[120, 75, 337])
    t_tem.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#EDF2F7")),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_tem)

    # =========================================================================
    # SALTO DE PÁGINA: LA PLANIFICACIÓN EN OTRA HOJA EXCLUSIVA (PÁGINA 2)
    # =========================================================================
    story.append(PageBreak())

    story.append(Paragraph("4. Planificación y Dosificación de Sesiones (10 Sesiones / 40 Horas Totales)", styles["H1"]))
    story.append(Paragraph(
        "A continuación se presenta la planificación detallada sesión por sesión, articulando las actividades analíticas virtuales sincrónicas en Microsoft Teams "
        "con los talleres presenciales de inspección de campo en planta y modelado estandarizado en Laboratorio CAD:",
        styles["Body"]
    ))
    story.append(Spacer(1, 6))

    cron_data = [
        [Paragraph("Sesión", styles["TableHead"]), Paragraph("Modalidad y Entorno", styles["TableHead"]), Paragraph("Actividades de Interpretación, Campo y CAD", styles["TableHead"]), Paragraph("Entregable Evaluativo", styles["TableHead"])],
        [
            Paragraph("<b>Sesión 1</b><br/>(4 Horas)", styles["TableCellBold"]),
            Paragraph("<b>Virtual Sincrónico</b><br/>Microsoft Teams", styles["TableCell"]),
            Paragraph("¿Qué es un P&ID? Simbología técnica normada, globos de instrumentos, letras modificadoras de variables, líneas de señal y código de tuberías.", styles["TableCell"]),
            Paragraph("Taller de decodificación de símbolos y tags de instrumentos (&ge; 75 pts).", styles["TableCellBold"])
        ],
        [
            Paragraph("<b>Sesión 2</b><br/>(4 Horas)", styles["TableCellBold"]),
            Paragraph("<b>Virtual Sincrónico</b><br/>Microsoft Teams", styles["TableCell"]),
            Paragraph("Simbología estandarizada de válvulas, actuadores, equipos estáticos/dinámicos y rastreo de líneas de proceso (Line Tracing).", styles["TableCell"]),
            Paragraph("Taller de rastreo de líneas e interpretación de P&ID industrial (&ge; 75 pts).", styles["TableCellBold"])
        ],
        [
            Paragraph("<b>Sesión 3</b><br/>(4 Horas)", styles["TableCellBold"]),
            Paragraph("<b>Presencial Práctico</b><br/>Planta / Taller Kinal", styles["TableCell"]),
            Paragraph("Metodología del walkdown, medición dimensional con calibrador vernier (OD, NPS, Schedule), uniones bridadas estandarizadas y accesorios.", styles["TableCell"]),
            Paragraph("Ficha técnica de relevamiento dimensional de tuberías en campo.", styles["TableCellBold"])
        ],
        [
            Paragraph("<b>Sesión 4</b><br/>(4 Horas)", styles["TableCellBold"]),
            Paragraph("<b>Presencial Práctico</b><br/>Planta / Taller Kinal", styles["TableCell"]),
            Paragraph("Croquizado rápido a mano alzada y en tablet: proporción visual, registro de tags in situ, válvulas, bypass y sentidos de flujo.", styles["TableCell"]),
            Paragraph("Croquis de campo consolidado y validado en brigada (&ge; 75 pts).", styles["TableCellBold"])
        ],
        [
            Paragraph("<b>Sesión 5</b><br/>(4 Horas)", styles["TableCellBold"]),
            Paragraph("<b>Presencial CAD</b><br/>Laboratorio CAD", styles["TableCell"]),
            Paragraph("Entorno CAD, plantilla institucional (.DWT), capas normalizadas por fluido, OSNAP, calco y trazado vectorial de líneas principales.", styles["TableCell"]),
            Paragraph("Plano DWG estructurado en capas normalizadas (&ge; 75 pts).", styles["TableCellBold"])
        ],
        [
            Paragraph("<b>Sesión 6</b><br/>(4 Horas)", styles["TableCellBold"]),
            Paragraph("<b>Presencial CAD</b><br/>Laboratorio CAD", styles["TableCell"]),
            Paragraph("Creación de bloques inteligentes con atributos editables (ATTDEF), rotulado de tags normalizados y resolución gráfica de cruces de líneas.", styles["TableCell"]),
            Paragraph("Plano P&ID en CAD con bloques y tags editables (&ge; 75 pts).", styles["TableCellBold"])
        ],
        [
            Paragraph("<b>Sesión 7</b><br/>(4 Horas)", styles["TableCellBold"]),
            Paragraph("<b>Presencial Práctico</b><br/>Taller / Lab. CAD", styles["TableCell"]),
            Paragraph("Simbología estandarizada de potencia fluida: unidades FRL, válvulas direccionales y modelado de circuitos neumáticos en AutoCAD.", styles["TableCell"]),
            Paragraph("Esquema neumático funcional dibujado en AutoCAD (&ge; 75 pts).", styles["TableCellBold"])
        ],
        [
            Paragraph("<b>Sesión 8</b><br/>(4 Horas)", styles["TableCellBold"]),
            Paragraph("<b>Presencial Práctico</b><br/>Taller / Lab. CAD", styles["TableCell"]),
            Paragraph("Simbología hidráulica estandarizada: unidades de potencia HPU, válvulas de alivio, válvulas 4/3 y modelado de circuitos oleohidráulicos.", styles["TableCell"]),
            Paragraph("Esquema hidráulico funcional dibujado en AutoCAD (&ge; 75 pts).", styles["TableCellBold"])
        ],
        [
            Paragraph("<b>Sesión 9</b><br/>(4 Horas)", styles["TableCellBold"]),
            Paragraph("<b>Presencial CAD</b><br/>Laboratorio CAD", styles["TableCell"]),
            Paragraph("Extracción automática de datos (EATTEXT) para tablas de equipos/válvulas, maquetación en Layouts (espacio papel) y plumillas .CTB.", styles["TableCell"]),
            Paragraph("Lámina P&ID maquetada con tablas y membrete oficial Kinal (&ge; 75 pts).", styles["TableCellBold"])
        ],
        [
            Paragraph("<b>Sesión 10</b><br/>(4 Horas)", styles["TableCellBold"]),
            Paragraph("<b>Presencial Panel</b><br/>Laboratorio CAD", styles["TableCell"]),
            Paragraph("Auditoría terminal as-built, exportación a PDF vectorial y sustentación técnica oral grupal del Proyecto Capstone ante el panel evaluador.", styles["TableCell"]),
            Paragraph("<b>Expediente Capstone Defendido y Acreditado (&ge; 75 pts)</b>.", styles["TableCellBold"])
        ],
    ]
    t_cron = Table(cron_data, colWidths=[55, 100, 242, 135])
    t_cron.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#EDF2F7")),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 4.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4.5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_cron)

    # =========================================================================
    # SALTO DE PÁGINA: EVALUACIÓN Y RÚBRICA EN PÁGINA DEDICADA (PÁGINA 3)
    # =========================================================================
    story.append(PageBreak())

    story.append(Paragraph("5. Sistema de Evaluación y Rúbrica Analítica Terminal (Nota Mínima Aprobatoria: 75/100 Puntos)", styles["H1"]))
    story.append(Paragraph(
        "El modelo de evaluación de competencias técnicas de Fundación Kinal califica la suficiencia demostrada en cuatro dimensiones integradas, "
        "conforme a los estándares del Marco de Cualificaciones (Nivel 4-5) y el principio del trabajo bien hecho:",
        styles["Body"]
    ))
    story.append(Spacer(1, 8))

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
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_rub)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF generado exitosamente en: {target_path}")

if __name__ == "__main__":
    build_pdf()
