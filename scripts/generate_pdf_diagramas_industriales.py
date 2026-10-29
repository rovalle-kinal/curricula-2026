#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador de Documento PDF Corporativo:
Interpretación y Levantamiento de Diagramas P&ID (Fundación Kinal)
Fundamentos Normativos (ANSI/ISA-5.1, ISO 10628, ISO 1219), Relevamiento de Campo y Dibujo en AutoCAD 2D
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
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, HRFlowable
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
        "H1": ParagraphStyle("H1", fontName="Helvetica-Bold", fontSize=10.5, leading=14, textColor=C_KINAL_BLUE, spaceBefore=10, spaceAfter=4),
        "H2": ParagraphStyle("H2", fontName="Helvetica-Bold", fontSize=9, leading=12, textColor=C_KINAL_NAVY, spaceBefore=6, spaceAfter=3),
        "Body": ParagraphStyle("Body", fontName="Helvetica", fontSize=7.5, leading=10.5, textColor=C_KINAL_DARK),
        "CalloutTitle": ParagraphStyle("CalloutTitle", fontName="Helvetica-Bold", fontSize=7.5, leading=10.5, textColor=C_KINAL_BLUE),
        "CalloutText": ParagraphStyle("CalloutText", fontName="Helvetica", fontSize=7.5, leading=10.5, textColor=C_KINAL_DARK),
        "TableHead": ParagraphStyle("TableHead", fontName="Helvetica-Bold", fontSize=7, leading=9, textColor=C_KINAL_BLUE),
        "TableCell": ParagraphStyle("TableCell", fontName="Helvetica", fontSize=6.8, leading=8.8, textColor=C_KINAL_DARK),
        "TableCellBold": ParagraphStyle("TableCellBold", fontName="Helvetica-Bold", fontSize=6.8, leading=8.8, textColor=C_KINAL_DARK),
    }

    story = []

    # ENCABEZADO CON LOGO
    if os.path.exists(LOGO_PATH):
        img = Image(LOGO_PATH, width=42, height=42)
        header_text = [
            Paragraph("FUNDACIÓN KINAL • ESCUELA TÉCNICA SUPERIOR", ParagraphStyle("HPre", fontName="Helvetica-Bold", fontSize=9, leading=11, textColor=C_KINAL_BLUE)),
            Paragraph("Interpretación y Levantamiento de Diagramas P&ID", styles["Title"]),
            Paragraph("Fundamentos Normativos (ANSI/ISA-5.1, ISO 10628, ISO 1219), Relevamiento de Campo y Dibujo en AutoCAD 2D (40 Horas)", styles["Subtitle"])
        ]
        t_header = Table([[img, header_text]], colWidths=[50, 482])
        t_header.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
            ('LEFTPADDING', (1,0), (1,0), 6),
            ('BOTTOMPADDING', (0,0), (-1,-1), 0),
            ('TOPPADDING', (0,0), (-1,-1), 0),
        ]))
        story.append(t_header)

    story.append(Spacer(1, 6))
    story.append(HRFlowable(width="100%", thickness=1.5, color=C_KINAL_BLUE, spaceBefore=2, spaceAfter=6))

    # FICHA TÉCNICA CORPORATIVA (SIN CÓDIGO)
    ficha_data = [
        [Paragraph("Programa", styles["TableCellBold"]), Paragraph("<b>Interpretación y Levantamiento de Diagramas P&ID</b>", styles["TableCell"])],
        [Paragraph("Población Objetivo", styles["TableCellBold"]), Paragraph("<b>6 a 10 colaboradores de planta</b> (Mecánicos, Electricistas, Instrumentistas y Dibujantes Técnicos)", styles["TableCell"])],
        [Paragraph("Carga Horaria y Formato", styles["TableCellBold"]), Paragraph("<b>40 horas pedagógicas híbridas</b> (10 sesiones de 4 horas / 240 min c/u):<br/>• <b>20% Virtual Sincrónico (8 Horas / 2 sesiones):</b> Fundamentación de P&ID, normas ISA-5.1, ISO 10628 e ISO 1219 en Teams.<br/>• <b>80% Presencial Práctico (32 Horas / 8 sesiones):</b> Relevamiento en planta (walkdown, croquis, metrología) y dibujo en Laboratorio CAD.", styles["TableCell"])],
        [Paragraph("Horarios Sugeridos", styles["TableCellBold"]), Paragraph("Adaptado a jornada laboral de planta (L-J 07:00-16:00 / V 07:00-15:00):<br/>• <b>Opción 1:</b> Martes y Jueves de 07:30 a 11:30 hrs (5 semanas).<br/>• <b>Opción 2:</b> 1 jornada semanal intensiva los Viernes.<br/>• <b>Inicio Propuesto:</b> <b>Diciembre 2026</b> o <b>Enero 2027</b>.", styles["TableCell"])],
        [Paragraph("Enfoque Formativo", styles["TableCellBold"]), Paragraph("<b>Lectura e Interpretación Analítica</b> &nbsp;|&nbsp; <b>Levantamiento de Campo (Walkdown y Croquis)</b> &nbsp;|&nbsp; <b>Dibujo Estandarizado en AutoCAD 2D</b> &nbsp;|&nbsp; <b>Esquemas de Fluidos ISO 1219</b>", styles["TableCell"])],
        [Paragraph("Nota Mínima Aprobatoria", styles["TableCellBold"]), Paragraph("<b>75 puntos sobre 100</b> en evaluaciones teórico-prácticas, laboratorios CAD y sustentación del Proyecto Capstone", styles["TableCell"])],
    ]
    t_ficha = Table(ficha_data, colWidths=[120, 412])
    t_ficha.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_BG_LIGHT),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_ficha)
    story.append(Spacer(1, 8))

    # SECCIÓN: ¿QUÉ ES UN DIAGRAMA P&ID?
    story.append(Paragraph("1. ¿Qué es un Diagrama P&ID (Piping and Instrumentation Diagram)?", styles["H1"]))
    story.append(Paragraph(
        "Un <b>P&ID</b> es el plano maestro de ingeniería que describe la interconexión esquemática y funcional de una planta industrial. "
        "No representa una distribución geográfica a escala, sino la <b>lógica operativa y de control</b> del proceso a través de cuatro componentes esenciales: "
        "<b>1) Equipos de proceso</b> (tanques, recipientes, bombas, compresores, intercambiadores); "
        "<b>2) Tuberías y líneas de servicio</b> (indicando diámetro nominal NPS, cédula Schedule, código de fluido y flechas de sentido de flujo); "
        "<b>3) Válvulas y actuadores</b> (válvulas manuales, de control y de seguridad PSV con su modo de falla segura); y "
        "<b>4) Instrumentación y lazos de control</b> (globos ISA-5.1 con tags alfanuméricos y líneas de señal eléctrica, neumática o digital).",
        styles["Body"]
    ))
    story.append(Spacer(1, 6))

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
            ('TOPPADDING', (0,0), (-1,-1), 3),
            ('BOTTOMPADDING', (0,0), (-1,-1), 3),
            ('LEFTPADDING', (0,0), (-1,-1), 8),
            ('RIGHTPADDING', (0,0), (-1,-1), 6),
        ]))
        return t

    story.append(make_callout("Misión Institucional de Kinal:", "«Formar a jóvenes y adultos a través de una educación integral, con énfasis en las áreas técnicas y tecnológicas, influyendo positivamente en su trabajo, su familia y la sociedad»."))
    story.append(Spacer(1, 2))
    story.append(make_callout("Valores Nucleares de Kinal:", "«Visión cristiana de la vida. Respeto a la dignidad de la persona. Espíritu de servicio. Trabajo bien hecho. Libertad personal responsable»."))
    story.append(Spacer(1, 4))

    story.append(Paragraph("El Principio del «Trabajo Bien Hecho» en la Interpretación y Dibujo de Planos:", styles["H2"]))
    story.append(Paragraph(
        "En el entorno industrial, un plano mal interpretado o un dibujo desactualizado es una causa directa de accidentes operacionales graves, fallas en maniobras de bloqueo LOTO o roturas por sobrepresión. "
        "En este curso, el <b>trabajo bien hecho</b> se materializa en cuatro pilares inmutables: "
        "<b>1) Verdad y Fidelidad Técnica (As-Built Real):</b> Compromiso ético de dibujar exactamente lo que existe en campo, sin suponer trayectorias ni omitir accesorios; "
        "<b>2) Prolijidad Gráfica y Disciplina CAD:</b> Estructuración estricta de capas por fluido, bloques inteligentes normalizados con atributos, textos nítidos y escalas coherentes; "
        "<b>3) Protección de la Vida y Seguridad:</b> Rigor al rotular sentidos de flujo, válvulas de alivio y modos de falla para que las intervenciones operativas sean seguras; y "
        "<b>4) Sentido de Servicio Multidisciplinario:</b> Producir planos claros y accesibles que sirvan de puente de colaboración entre mecánicos, electricistas e instrumentistas.",
        styles["Body"]
    ))
    story.append(Spacer(1, 8))

    # SECCIÓN: TEMARIO JERÁRQUICO (ENFOQUE EN INTERPRETACIÓN Y DIBUJO)
    story.append(Paragraph("3. Temario Curricular Jerárquico (40 Horas Híbridas)", styles["H1"]))
    temario_data = [
        [Paragraph("Módulo", styles["TableHead"]), Paragraph("Modalidad", styles["TableHead"]), Paragraph("Contenidos y Competencias de Interpretación y Dibujo", styles["TableHead"])],
        [
            Paragraph("<b>Módulo 1:</b><br/>Fundamentos de P&ID y Norma ISA-5.1", styles["TableCellBold"]),
            Paragraph("<b>8 Horas</b><br/>Virtual (Teams)", styles["TableCell"]),
            Paragraph("• Qué es un P&ID, arquitectura de planos y jerarquía (BFD, PFD, P&ID).<br/>• Norma <b>ANSI/ISA-5.1:</b> Simbología de globos de instrumentos, letras de variables (P, T, F, L), modificadores (I, C, T, V) y líneas de señal (eléctrica, neumática, bus de datos).<br/>• Código de tuberías (Line Numbering) y código de colores ASME A13.1.<br/>• Lectura e interpretación de lazos de control cerrados y modos de falla segura (FC, FO, FL).", styles["TableCell"])
        ],
        [
            Paragraph("<b>Módulo 2:</b><br/>Simbología de Válvulas y Equipos", styles["TableCellBold"]),
            Paragraph("<b>8 Horas</b><br/>Virtual (Teams)", styles["TableCell"]),
            Paragraph("• Simbología de válvulas según <b>ISO 10628 / ISA-5.1:</b> compuerta, globo, bola, mariposa, retención (check), diafragma, seguridad y alivio (PSV/PRV).<br/>• Tipos de actuadores gráficos: manual, diafragma neumático, motor eléctrico y solenoide.<br/>• Representación gráfica de tanques, recipientes a presión, bombas centrífugas, bombas de desplazamiento positivo, compresores e intercambiadores.<br/>• Técnicas de rastreo de líneas de proceso (Line Tracing) e interpretación de P&IDs industriales completos.", styles["TableCell"])
        ],
        [
            Paragraph("<b>Módulo 3:</b><br/>Levantamiento de Campo y Croquis", styles["TableCellBold"]),
            Paragraph("<b>8 Horas</b><br/>Planta / Taller", styles["TableCell"]),
            Paragraph("• Metodología del levantamiento en campo (Field Walkdown): límites de batería y puntos de conexión.<br/>• Metrología de tuberías: medición de diámetro exterior (OD), determinación de diámetro nominal NPS y cédula Schedule con calibrador vernier.<br/>• Identificación física de accesorios, bridas ANSI (150/300 RF/FF) y uniones roscadas NPT.<br/>• Técnicas de croquizado técnico a mano alzada y en tablet con stylus: proporción, alineación ortogonal y validación cruzada.", styles["TableCell"])
        ],
        [
            Paragraph("<b>Módulo 4:</b><br/>Dibujo de P&ID en AutoCAD 2D", styles["TableCellBold"]),
            Paragraph("<b>8 Horas</b><br/>Laboratorio CAD", styles["TableCell"]),
            Paragraph("• Configuración del espacio de trabajo en AutoCAD: plantilla institucional (.DWT) y sistema de capas normalizadas (L-PROCESO, L-SERVICIOS, E-EQUIPOS, E-VALVULAS, I-INSTRUMENTOS).<br/>• Herramientas de precisión esquemática: OSNAP y Polar Tracking.<br/>• Creación de bloques inteligentes con atributos editables (ATTDEF/BATTMAN) para tags ISA.<br/>• Resolución gráfica de cruces de líneas (puentes/arcos vs. cruces limpios) y derivaciones.", styles["TableCell"])
        ],
        [
            Paragraph("<b>Módulo 5:</b><br/>Esquemas ISO 1219 y Proyecto Capstone", styles["TableCellBold"]),
            Paragraph("<b>8 Horas</b><br/>Taller + CAD", styles["TableCell"]),
            Paragraph("• Simbología de potencia fluida bajo <b>ISO 1219:</b> unidades FRL, válvulas direccionales (3/2, 5/2, 4/3), cilindros neumáticos e hidráulicos.<br/>• Extracción automática de tablas de instrumentos y válvulas con comando <code>EATTEXT</code>.<br/>• Maquetación en espacio papel (Layouts) con cajetín corporativo Kinal y plumillas .CTB.<br/>• <b>Sustentación del Proyecto Capstone:</b> Presentación y defensa grupal del plano P&ID as-built terminado (&ge; 75 pts).", styles["TableCell"])
        ],
    ]
    t_tem = Table(temario_data, colWidths=[120, 75, 337])
    t_tem.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#EDF2F7")),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_tem)
    story.append(Spacer(1, 8))

    # SECCIÓN: MACROPLANIFICACIÓN 10 SESIONES
    story.append(Paragraph("4. Macroplanificación de Sesiones (10 Sesiones de 4 Horas)", styles["H1"]))
    cron_data = [
        [Paragraph("Sesión", styles["TableHead"]), Paragraph("Modalidad", styles["TableHead"]), Paragraph("Actividades de Interpretación, Campo y CAD", styles["TableHead"]), Paragraph("Entregable Evaluativo", styles["TableHead"])],
        [Paragraph("<b>Sesión 1</b>", styles["TableCellBold"]), Paragraph("Virtual (Teams)", styles["TableCell"]), Paragraph("¿Qué es un P&ID? Norma ISA-5.1, globos de instrumentos, modificadores, líneas de señal y código de tuberías.", styles["TableCell"]), Paragraph("Taller de decodificación de tags ISA (&ge; 75 pts).", styles["TableCellBold"])],
        [Paragraph("<b>Sesión 2</b>", styles["TableCellBold"]), Paragraph("Virtual (Teams)", styles["TableCell"]), Paragraph("Simbología de válvulas ISO 10628, actuadores, equipos y rastreo de líneas de proceso (Line Tracing).", styles["TableCell"]), Paragraph("Taller de rastreo de P&ID industrial (&ge; 75 pts).", styles["TableCellBold"])],
        [Paragraph("<b>Sesión 3</b>", styles["TableCellBold"]), Paragraph("Presencial (Planta)", styles["TableCell"]), Paragraph("Metodología del walkdown, medición dimensional con calibrador vernier (OD, NPS, Schedule) y bridas ANSI.", styles["TableCell"]), Paragraph("Ficha técnica de relevamiento dimensional.", styles["TableCellBold"])],
        [Paragraph("<b>Sesión 4</b>", styles["TableCellBold"]), Paragraph("Presencial (Planta)", styles["TableCell"]), Paragraph("Croquizado rápido a mano alzada y en tablet: proporción visual, registro de tags, válvulas y sentidos de flujo.", styles["TableCell"]), Paragraph("Croquis de campo consolidado y validado.", styles["TableCellBold"])],
        [Paragraph("<b>Sesión 5</b>", styles["TableCellBold"]), Paragraph("Presencial (CAD)", styles["TableCell"]), Paragraph("Entorno CAD, plantilla Kinal (.DWT), capas normalizadas por fluido, OSNAP, calco y trazado vectorial de líneas.", styles["TableCell"]), Paragraph("Plano DWG con capas normalizadas (&ge; 75 pts).", styles["TableCellBold"])],
        [Paragraph("<b>Sesión 6</b>", styles["TableCellBold"]), Paragraph("Presencial (CAD)", styles["TableCell"]), Paragraph("Creación de bloques inteligentes con atributos (ATTDEF), rotulado de tags ISA y resolución de cruces de líneas.", styles["TableCell"]), Paragraph("Plano P&ID en CAD con bloques y tags editables.", styles["TableCellBold"])],
        [Paragraph("<b>Sesión 7</b>", styles["TableCellBold"]), Paragraph("Presencial (Taller/CAD)", styles["TableCell"]), Paragraph("Simbología de potencia fluida ISO 1219: unidades FRL, válvulas direccionales y modelado de circuito neumático.", styles["TableCell"]), Paragraph("Esquema neumático ISO 1219 en AutoCAD (&ge; 75 pts).", styles["TableCellBold"])],
        [Paragraph("<b>Sesión 8</b>", styles["TableCellBold"]), Paragraph("Presencial (Taller/CAD)", styles["TableCell"]), Paragraph("Simbología oleohidráulica ISO 1219: unidades HPU, válvulas de alivio, válvulas 4/3 y modelado de circuito hidráulico.", styles["TableCell"]), Paragraph("Esquema hidráulico ISO 1219 en AutoCAD (&ge; 75 pts).", styles["TableCellBold"])],
        [Paragraph("<b>Sesión 9</b>", styles["TableCellBold"]), Paragraph("Presencial (CAD)", styles["TableCell"]), Paragraph("Extracción automática de datos (EATTEXT) para tablas de equipos/válvulas, maquetación en Layouts y plumillas .CTB.", styles["TableCell"]), Paragraph("Lámina P&ID maquetada con tablas y membrete Kinal.", styles["TableCellBold"])],
        [Paragraph("<b>Sesión 10</b>", styles["TableCellBold"]), Paragraph("Presencial (Panel)", styles["TableCell"]), Paragraph("Auditoría terminal as-built, exportación a PDF vectorial y sustentación técnica oral grupal del Proyecto Capstone.", styles["TableCell"]), Paragraph("<b>Expediente Capstone Aprobado (&ge; 75 pts)</b>.", styles["TableCellBold"])],
    ]
    t_cron = Table(cron_data, colWidths=[55, 90, 255, 132])
    t_cron.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#EDF2F7")),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_cron)
    story.append(Spacer(1, 8))

    # SECCIÓN: RÚBRICA ANALÍTICA TERMINAL
    story.append(Paragraph("5. Sistema de Evaluación y Rúbrica Analítica Terminal (Nota Mínima: 75/100)", styles["H1"]))
    rub_data = [
        [Paragraph("Dimensión DQR", styles["TableHead"]), Paragraph("Excelente (90 - 100)", styles["TableHead"]), Paragraph("Satisfactorio (75 - 89)<br/><i>[Aprobatorio Kinal]</i>", styles["TableHead"]), Paragraph("En Desarrollo (< 75)", styles["TableHead"])],
        [
            Paragraph("<b>1. Saber Técnico</b><br/>(Normas ISA, ISO, ASME)", styles["TableCellBold"]),
            Paragraph("Decodificación perfecta de tags ISA y lazos de control; correlación exacta de tuberías NPS/Schedule; dominio de simbología de válvulas y modos de falla.", styles["TableCell"]),
            Paragraph("Identifica tags ISA y válvulas principales; determina diámetros NPS; interpreta diagramas P&ID con precisión funcional <b>(&ge; 75 pts)</b>.", styles["TableCell"]),
            Paragraph("Confunde variables de instrumentos ISA o no sabe determinar el diámetro nominal; errores graves de interpretación.", styles["TableCell"])
        ],
        [
            Paragraph("<b>2. Saber Hacer</b><br/>(Relevamiento y Croquis)", styles["TableCellBold"]),
            Paragraph("Medición precisa con calibrador; croquis de campo proporcional, limpio y estructurado en tablet/papel; registro completo de tags y sentidos de flujo.", styles["TableCell"]),
            Paragraph("Releva diámetros y elabora croquis comprensibles con simbología normalizada; registra componentes sin omisiones críticas <b>(&ge; 75 pts)</b>.", styles["TableCell"]),
            Paragraph("Croquis desproporcionado o ilegible; omisión de válvulas de purga o bypass; errores en toma de medidas físicas.", styles["TableCell"])
        ],
        [
            Paragraph("<b>3. Saber Hacer</b><br/>(Dibujo CAD y Tablas)", styles["TableCellBold"]),
            Paragraph("Plano DWG impecable: capas normalizadas, bloques con atributos editables, cruces resueltos, tablas automáticas EATTEXT y maquetación a escala.", styles["TableCell"]),
            Paragraph("Dibuja el P&ID en AutoCAD con capas organizadas; inserta bloques con atributos; genera tablas de equipos y maqueta con membrete Kinal <b>(&ge; 75 pts)</b>.", styles["TableCell"]),
            Paragraph("Líneas desconectadas, desorden de capas, textos sobre líneas de proceso o ausencia de bloques inteligentes.", styles["TableCell"])
        ],
        [
            Paragraph("<b>4. Saber Ser y Estar</b><br/>(Trabajo Bien Hecho y LOTO)", styles["TableCellBold"]),
            Paragraph("Encarna con excelencia el trabajo bien hecho: verdad en el plano as-built sin inventar datos, rigor en seguridad LOTO y defensa Capstone sólida.", styles["TableCell"]),
            Paragraph("Compromiso ético y técnico; participa activamente en la brigada de relevamiento y sustenta con claridad su proyecto <b>(&ge; 75 pts)</b>.", styles["TableCell"]),
            Paragraph("Falseamiento de datos en el plano, desatención a normas de seguridad o débil defensa técnica grupal.", styles["TableCell"])
        ],
    ]
    t_rub = Table(rub_data, colWidths=[110, 140, 142, 140])
    t_rub.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#EDF2F7")),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_rub)

    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF generado exitosamente en: {target_path}")

if __name__ == "__main__":
    build_pdf()
