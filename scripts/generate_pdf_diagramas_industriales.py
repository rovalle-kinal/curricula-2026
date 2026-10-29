#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador de Documento PDF Corporativo:
Levantamiento e Interpretación de Diagramas y P&ID para Sistemas Industriales (Fundación Kinal)
Especialidad: Agua de Proceso, Combustibles (Búnker/Diésel), Neumática e Hidráulica
Escuela Técnica Superior — Coordinación de Capacitación Corporativa
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
            self.drawRightString(572, 755, "Diagramas y P&ID Industriales (Agua, Combustibles, Neumática, Hidráulica)")
            self.setStrokeColor(C_BORDER)
            self.setLineWidth(0.5)
            self.line(40, 748, 572, 748)

        # Pie de página en todas las páginas
        self.setStrokeColor(C_BORDER)
        self.setLineWidth(0.5)
        self.line(40, 42, 572, 42)
        
        self.setFont("Helvetica", 7.5)
        self.setFillColor(C_TEXT_MUTED)
        self.drawString(40, 30, "Capacitación Corporativa • Marco DQR Nivel 4-5 • Nota Mínima Aprobatoria: 75/100 Puntos")
        
        page_str = f"Página {self._pageNumber} de {page_count}"
        self.drawRightString(572, 30, page_str)
        self.restoreState()

def build_pdf():
    target_path = os.path.join(COURSE_DIR, "programa_formativo_diagramas_industriales.pdf")
    doc = SimpleDocTemplate(target_path, pagesize=letter, leftMargin=40, rightMargin=40, topMargin=45, bottomMargin=55)

    base = getSampleStyleSheet()
    styles = {
        "Title": ParagraphStyle("DocTitle", fontName="Helvetica-Bold", fontSize=16, leading=20, textColor=C_KINAL_BLUE),
        "Subtitle": ParagraphStyle("DocSub", fontName="Helvetica-Oblique", fontSize=9, leading=13, textColor=C_TEXT_MUTED),
        "H1": ParagraphStyle("H1", fontName="Helvetica-Bold", fontSize=11, leading=15, textColor=C_KINAL_BLUE, spaceBefore=12, spaceAfter=5),
        "H2": ParagraphStyle("H2", fontName="Helvetica-Bold", fontSize=9.5, leading=12, textColor=C_KINAL_NAVY, spaceBefore=7, spaceAfter=3),
        "Body": ParagraphStyle("Body", fontName="Helvetica", fontSize=8, leading=11, textColor=C_KINAL_DARK),
        "CalloutTitle": ParagraphStyle("CalloutTitle", fontName="Helvetica-Bold", fontSize=8, leading=11, textColor=C_KINAL_BLUE),
        "CalloutText": ParagraphStyle("CalloutText", fontName="Helvetica", fontSize=8, leading=11, textColor=C_KINAL_DARK),
        "TableHead": ParagraphStyle("TableHead", fontName="Helvetica-Bold", fontSize=7.5, leading=9.5, textColor=C_KINAL_BLUE),
        "TableCell": ParagraphStyle("TableCell", fontName="Helvetica", fontSize=7, leading=9.5, textColor=C_KINAL_DARK),
        "TableCellBold": ParagraphStyle("TableCellBold", fontName="Helvetica-Bold", fontSize=7, leading=9.5, textColor=C_KINAL_DARK),
    }

    story = []

    # ENCABEZADO CON LOGO
    if os.path.exists(LOGO_PATH):
        img = Image(LOGO_PATH, width=44, height=44)
        header_text = [
            Paragraph("FUNDACIÓN KINAL • ESCUELA TÉCNICA SUPERIOR", ParagraphStyle("HPre", fontName="Helvetica-Bold", fontSize=9.5, leading=11, textColor=C_KINAL_BLUE)),
            Paragraph("Levantamiento e Interpretación de Diagramas y P&ID para Sistemas Industriales", styles["Title"]),
            Paragraph("Propuesta Corporativa (40 Horas Híbridas) | Agua de Proceso, Búnker/Diésel, Neumática e Hidráulica", styles["Subtitle"])
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

    # FICHA TÉCNICA CORPORATIVA
    ficha_data = [
        [Paragraph("Programa y Código", styles["TableCellBold"]), Paragraph("<b>Levantamiento e Interpretación de Diagramas y P&ID para Sistemas Industriales</b> (ETS-CORP-P&ID-40H)", styles["TableCell"])],
        [Paragraph("Población Objetivo", styles["TableCellBold"]), Paragraph("<b>6 a 10 colaboradores de planta</b> (Mecánicos, Electricistas, Instrumentistas y Dibujante Técnico)", styles["TableCell"])],
        [Paragraph("Carga Horaria y Modalidad", styles["TableCellBold"]), Paragraph("<b>40 horas pedagógicas híbridas</b> (10 sesiones de 4 horas / 240 min c/u):<br/>• <b>20% Virtual Sincrónico (8 Horas / 2 sesiones):</b> Fundamentación normativa en Microsoft Teams.<br/>• <b>80% Presencial Práctico (32 Horas / 8 sesiones):</b> Relevamiento en planta y modelado CAD en Kinal.", styles["TableCell"])],
        [Paragraph("Horarios y Ventana Sugerida", styles["TableCellBold"]), Paragraph("Adaptado a la jornada de la empresa (L-J 07:00-16:00 / V 07:00-15:00):<br/>• <b>Horario sugerido:</b> Martes y Jueves de 07:30 a 11:30 hrs (o 12:00 a 16:00 hrs) — 5 semanas.<br/>• <b>Fechas de Inicio:</b> <b>Diciembre 2026</b> o <b>Enero 2027</b>.", styles["TableCell"])],
        [Paragraph("Sistemas Abordados", styles["TableCellBold"]), Paragraph("<b>1) Agua de proceso y potable</b> &nbsp;|&nbsp; <b>2) Búnker y diésel</b> &nbsp;|&nbsp; <b>3) Neumática de aire</b> &nbsp;|&nbsp; <b>4) Oleohidráulica básica</b>", styles["TableCell"])],
        [Paragraph("Nota Mínima Aprobatoria", styles["TableCellBold"]), Paragraph("<b>75 puntos sobre 100</b> en evaluaciones de campo, laboratorios CAD y Proyecto Capstone", styles["TableCell"])],
    ]
    t_ficha = Table(ficha_data, colWidths=[140, 392])
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

    # SECCIÓN 1: MARCO FILOSÓFICO
    story.append(Paragraph("1. Marco Filosófico e Ideario Institucional de Fundación Kinal", styles["H1"]))
    
    def make_callout(bold_lbl, text):
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

    story.append(make_callout("Misión Institucional de Kinal:", "«Formar a jóvenes y adultos a través de una educación integral, con énfasis en las áreas técnicas y tecnológicas, influyendo positivamente en su trabajo, su familia y la sociedad»."))
    story.append(Spacer(1, 3))
    story.append(make_callout("Valores Nucleares de Kinal:", "«Visión cristiana de la vida. Respeto a la dignidad de la persona. Espíritu de servicio. Trabajo bien hecho. Libertad personal responsable»."))
    story.append(Spacer(1, 3))
    story.append(make_callout(
        "Concepto de Competencia Profesional (Marco DQR):",
        "La competencia es la capacidad y disposición de la persona para integrar conocimientos técnicos, destrezas prácticas y responsabilidad personal y social, actuando con criterio ético y autonomía ante situaciones reales de trabajo.<br/>"
        "<b>Competencia Diseñada para el Programa Industrial:</b> El equipo técnico interpreta con rigor, releva en campo y modela en AutoCAD 2D diagramas de flujo y P&ID de sistemas de agua de proceso, combustibles pesados y livianos (búnker/diésel con traceado de vapor), redes de aire comprimido y circuitos hidráulicos básicos bajo normas ANSI/ISA-5.1, ISO 10628, ISO 1219 y ASME A13.1, garantizando planos as-built fidedignos bajo el estándar del trabajo bien hecho de Fundación Kinal."
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("El Principio del «Trabajo Bien Hecho» en la Seguridad Operativa de Planta:", styles["H2"]))
    story.append(Paragraph(
        "En operaciones industriales continuas, un plano de tuberías desactualizado o una válvula mal rotulada representa un peligro crítico de derrame, sobrepresión o accidente en maniobras LOTO. En Kinal, el trabajo bien hecho se concreta en la fidelidad total entre el plano y la realidad de campo, la prolijidad técnica en capas y bloques inteligentes en AutoCAD, y la articulación fluida entre mecánicos, electricistas, instrumentistas y dibujante.",
        styles["Body"]
    ))
    story.append(Spacer(1, 10))

    # SECCIÓN 2: LOS 4 SISTEMAS INDUSTRIALES
    story.append(Paragraph("2. Alcance Técnico de los 4 Sistemas Industriales de Planta", styles["H1"]))
    sistemas_data = [
        [
            Paragraph("<b>💧 1. Agua de Proceso y Potable</b><br/>• Redes de agua cruda, suavizada y potable.<br/>• Bombas centrífugas, curvas de operación y cebado.<br/>• Válvulas compuerta, mariposa, retención/check y globo.<br/>• Filtros de arena, lechos suavizadores y caudal.<br/>• Tuberías: NPS, Schedule 40/80 y bridas ANSI.", styles["TableCell"]),
            Paragraph("<b>🔥 2. Combustibles (Búnker y Diésel)</b><br/>• Tanques principales y tanques de día con venteos.<br/>• Bombas de desplazamiento positivo (engranes/tornillo).<br/>• Traceado de vapor (<i>steam tracing</i>) e intercambiadores.<br/>• Válvulas de corte rápido con fusible térmico y alivios PSV.<br/>• Filtros canasta dúplex y sellos de diafragma.", styles["TableCell"])
        ],
        [
            Paragraph("<b>💨 3. Sistemas Neumáticos de Aire</b><br/>• Compresores de tornillo y pistón.<br/>• Tanque pulmón, purgas y secadores (+3°C).<br/>• Red en anillo cerrado (<i>loop</i>) con cuellos de cisne.<br/>• Unidades de Mantenimiento FRL.<br/>• Simbología ISO 1219: válvulas 3/2, 5/2 y cilindros.", styles["TableCell"]),
            Paragraph("<b>⚙️ 4. Sistemas Hidráulicos Básicos</b><br/>• Unidades de potencia hidráulica HPU.<br/>• Bombas de engranajes, paletas y pistones axiales.<br/>• Válvulas de alivio principal (1,000-3,000 PSI).<br/>• Válvulas direccionales 4/3 (abierto, cerrado, tándem).<br/>• Cilindros de alta presión y motores hidráulicos.", styles["TableCell"])
        ],
    ]
    t_sist = Table(sistemas_data, colWidths=[266, 266])
    t_sist.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), C_BG_LIGHT),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_sist)
    story.append(Spacer(1, 10))

    # SECCIÓN 3: TEMARIO JERÁRQUICO
    story.append(Paragraph("3. Temario Curricular Jerárquico (40 Horas Híbridas)", styles["H1"]))
    temario_data = [
        [Paragraph("Módulo", styles["TableHead"]), Paragraph("Modalidad", styles["TableHead"]), Paragraph("Contenidos Nucleares y Competencias", styles["TableHead"])],
        [
            Paragraph("<b>Módulo 1:</b><br/>Normas ISA-5.1 e ISO 10628", styles["TableCellBold"]),
            Paragraph("<b>8 Horas</b><br/>Virtual (Teams)", styles["TableCell"]),
            Paragraph("• BFD, PFD y P&ID. Norma <b>ANSI/ISA-5.1:</b> círculos ISA, variables (P,T,F,L), modificadores y líneas de señal.<br/>• Norma <b>ISO 10628:</b> simbología de válvulas manuales/automáticas y equipos dinámicos.<br/>• Código de colores ASME A13.1 y filosofía de fallas seguras (FC, FO, FL).", styles["TableCell"])
        ],
        [
            Paragraph("<b>Módulo 2:</b><br/>Agua de Proceso y Modelado CAD", styles["TableCellBold"]),
            Paragraph("<b>8 Horas</b><br/>Campo + CAD", styles["TableCell"]),
            Paragraph("• Redes de agua, bombeo centrífugo, filtración y suavizadores.<br/>• Metrología de tuberías: NPS, OD, Schedule y uniones bridadas. Croquis de campo.<br/>• Modelado en AutoCAD 2D: plantilla P&ID Kinal (.DWT), capas por fluido y bloques con atributos.", styles["TableCell"])
        ],
        [
            Paragraph("<b>Módulo 3:</b><br/>Búnker y Diésel con Traceado", styles["TableCellBold"]),
            Paragraph("<b>8 Horas</b><br/>Campo + CAD", styles["TableCell"]),
            Paragraph("• Tanques de día, viscosidad de búnker vs. diésel, bombas de engranes/tornillo.<br/>• Precalentamiento, traceado de vapor (<i>steam tracing</i>) y trampas de vapor.<br/>• Válvulas de corte con fusible térmico, filtros dúplex y digitalización CAD con lazo TIC.", styles["TableCell"])
        ],
        [
            Paragraph("<b>Módulo 4:</b><br/>Sistemas Neumáticos (ISO 1219)", styles["TableCellBold"]),
            Paragraph("<b>8 Horas</b><br/>Campo + CAD", styles["TableCell"]),
            Paragraph("• Compresores de tornillo, pulmón, secadores refrigerativos y filtros coalescentes.<br/>• Red en anillo cerrado con bajadas en cuello de cisne y purgas de condensado.<br/>• Unidades FRL, válvulas direccionales y cilindros neumáticos en AutoCAD según ISO 1219.", styles["TableCell"])
        ],
        [
            Paragraph("<b>Módulo 5:</b><br/>Oleohidráulica y Capstone", styles["TableCellBold"]),
            Paragraph("<b>8 Horas</b><br/>Taller + CAD", styles["TableCell"]),
            Paragraph("• Centrales HPU: depósito, bombas de alta presión, válvulas de alivio y direccionales 4/3.<br/>• Extracción automática de tablas de válvulas/equipos con comando <code>EATTEXT</code> en AutoCAD.<br/>• Maquetación en Paper Space con membrete Kinal y sustentación grupal del Proyecto Capstone (&ge; 75 pts).", styles["TableCell"])
        ],
    ]
    t_tem = Table(temario_data, colWidths=[125, 75, 332])
    t_tem.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#EDF2F7")),
        ('GRID', (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_tem)
    story.append(Spacer(1, 10))

    # SECCIÓN 4: MACROPLANIFICACIÓN 10 SESIONES
    story.append(Paragraph("4. Macroplanificación Sesión por Sesión (10 Sesiones de 4 Horas)", styles["H1"]))
    cron_data = [
        [Paragraph("Sesión", styles["TableHead"]), Paragraph("Modalidad", styles["TableHead"]), Paragraph("Actividades Prácticas y Entorno", styles["TableHead"]), Paragraph("Entregable Evaluativo", styles["TableHead"])],
        [Paragraph("<b>Sesión 1</b>", styles["TableCellBold"]), Paragraph("Virtual (Teams)", styles["TableCell"]), Paragraph("Decodificación de tags ISA-5.1, tipos de líneas de señal y código de colores ASME A13.1.", styles["TableCell"]), Paragraph("Taller de tags y señales ISA (&ge; 75 pts).", styles["TableCellBold"])],
        [Paragraph("<b>Sesión 2</b>", styles["TableCellBold"]), Paragraph("Virtual (Teams)", styles["TableCell"]), Paragraph("Simbología de válvulas ISO 10628, rastreo de líneas de proceso en P&IDs industriales y fallas seguras.", styles["TableCell"]), Paragraph("Taller de rastreo de P&ID industrial.", styles["TableCellBold"])],
        [Paragraph("<b>Sesión 3</b>", styles["TableCellBold"]), Paragraph("Presencial (Planta)", styles["TableCell"]), Paragraph("Medición de tuberías de agua (NPS, Schedule), calibración vernier, bombeo centrífugo y croquis en tablet.", styles["TableCell"]), Paragraph("Croquis de campo de estación de agua.", styles["TableCellBold"])],
        [Paragraph("<b>Sesión 4</b>", styles["TableCellBold"]), Paragraph("Presencial (CAD)", styles["TableCell"]), Paragraph("Digitalización en AutoCAD del sistema de agua: plantilla Kinal, capas normalizadas y bloques con atributos.", styles["TableCell"]), Paragraph("Plano P&ID de agua en AutoCAD 2D (&ge; 75 pts).", styles["TableCellBold"])],
        [Paragraph("<b>Sesión 5</b>", styles["TableCellBold"]), Paragraph("Presencial (Planta)", styles["TableCell"]), Paragraph("Rastreo de líneas de búnker y diésel, tanques de día, bombas de engranes, traceado de vapor y válvulas de seguridad.", styles["TableCell"]), Paragraph("Croquis de campo de combustibles y traceado.", styles["TableCellBold"])],
        [Paragraph("<b>Sesión 6</b>", styles["TableCellBold"]), Paragraph("Presencial (CAD)", styles["TableCell"]), Paragraph("Modelado en AutoCAD del P&ID de combustibles: representación de traceado de vapor y lazo de temperatura TIC.", styles["TableCell"]), Paragraph("Plano P&ID de búnker/diésel en AutoCAD (&ge; 75 pts).", styles["TableCellBold"])],
        [Paragraph("<b>Sesión 7</b>", styles["TableCellBold"]), Paragraph("Presencial (Planta)", styles["TableCell"]), Paragraph("Relevamiento de sala de compresores, secador, pulmón, red en anillo, estaciones FRL y simbología ISO 1219.", styles["TableCell"]), Paragraph("Croquis de red de aire y diagrama neumático.", styles["TableCellBold"])],
        [Paragraph("<b>Sesión 8</b>", styles["TableCellBold"]), Paragraph("Presencial (CAD)", styles["TableCell"]), Paragraph("Digitalización del P&ID neumático y circuito de automatización ISO 1219 con bloques dinámicos en AutoCAD.", styles["TableCell"]), Paragraph("Plano P&ID y esquema neumático CAD (&ge; 75 pts).", styles["TableCellBold"])],
        [Paragraph("<b>Sesión 9</b>", styles["TableCellBold"]), Paragraph("Presencial (Taller/CAD)", styles["TableCell"]), Paragraph("Levantamiento físico de central hidráulica HPU, líneas de presión/retorno, válvulas 4/3 y modelado ISO 1219.", styles["TableCell"]), Paragraph("Esquema funcional hidráulico HPU en CAD.", styles["TableCellBold"])],
        [Paragraph("<b>Sesión 10</b>", styles["TableCellBold"]), Paragraph("Presencial (CAD)", styles["TableCell"]), Paragraph("Extracción de listas de válvulas e instrumentos (EATTEXT), maquetación en Paper Space y sustentación Capstone.", styles["TableCell"]), Paragraph("<b>Expediente Capstone Aprobado (&ge; 75 pts)</b>.", styles["TableCellBold"])],
    ]
    t_cron = Table(cron_data, colWidths=[55, 95, 250, 132])
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

    # SECCIÓN 5: RÚBRICA Y EVALUACIÓN
    story.append(Paragraph("5. Sistema de Evaluación y Rúbrica Analítica Terminal (Nota Mínima: 75/100)", styles["H1"]))
    rub_data = [
        [Paragraph("Dimensión Evaluada", styles["TableHead"]), Paragraph("Excelente (90 - 100)", styles["TableHead"]), Paragraph("Satisfactorio (75 - 89)<br/><i>[Aprobatorio Kinal]</i>", styles["TableHead"]), Paragraph("En Desarrollo (< 75)", styles["TableHead"])],
        [
            Paragraph("<b>1. Interpretación Normativa y Fluidos</b><br/>(ISA, ISO, ASME)", styles["TableCellBold"]),
            Paragraph("Decodificación perfecta de tags ISA y lazos de control; correlación exacta de tuberías NPS/Schedule; dominio de agua, búnker con traceado, aire e hidráulica.", styles["TableCell"]),
            Paragraph("Identifica tags ISA y válvulas principales; determina diámetros NPS; interpreta los 4 sistemas de fluidos correctamente <b>(&ge; 75 pts)</b>.", styles["TableCell"]),
            Paragraph("Confunde letras modificadoras ISA o no sabe determinar el diámetro nominal; errores graves en lazos de control.", styles["TableCell"])
        ],
        [
            Paragraph("<b>2. Relevamiento de Campo y Croquizado</b><br/>(Planta y Tablet)", styles["TableCellBold"]),
            Paragraph("Croquis de campo técnico, proporcionado y exhaustivo; registro completo de placas de bombas, tags y traceados; excelente uso de capas en tablet.", styles["TableCell"]),
            Paragraph("Croquis legible a mano alzada y en tablet con simbología comprensible; registra componentes y tags sin omisiones críticas <b>(&ge; 75 pts)</b>.", styles["TableCell"]),
            Paragraph("Croquis ininteligible o desproporcionado; omisión de válvulas de seguridad o purgas; pérdida de información técnica.", styles["TableCell"])
        ],
        [
            Paragraph("<b>3. Modelado en AutoCAD 2D y P&ID</b><br/>(Bloques, Capas y Paper Space)", styles["TableCellBold"]),
            Paragraph("Plantilla Kinal respetada al 100%; capas por fluido perfectas; bloques con atributos; extracción automática EATTEXT y maquetación ejecutiva a escala.", styles["TableCell"]),
            Paragraph("Modela el P&ID en AutoCAD con capas normalizadas; inserta bloques con atributos; genera tabla de equipos y maqueta con membrete Kinal <b>(&ge; 75 pts)</b>.", styles["TableCell"]),
            Paragraph("Líneas de tubería desconectadas; desorden en capas; textos solapados sobre líneas de proceso; ausencia de bloques.", styles["TableCell"])
        ],
        [
            Paragraph("<b>4. Seguridad Industrial y Trabajo Bien Hecho</b><br/>(Ideario Kinal)", styles["TableCellBold"]),
            Paragraph("Encarna de forma ejemplar el trabajo bien hecho. Cero tolerancia a planos desactualizados; riguroso respeto a normas LOTO y seguridad de fluidos térmicos.", styles["TableCell"]),
            Paragraph("Mantiene un registro ordenado en bitácora; puntualidad, cumplimiento de normas de seguridad en planta y espíritu de servicio <b>(&ge; 75 pts)</b>.", styles["TableCell"]),
            Paragraph("Negligencia ante riesgos de fluidos calientes o alta presión; indisciplina, impuntualidad reiterada o falseamiento de datos.", styles["TableCell"])
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
    print(f"PDF Corporativo P&ID generado exitosamente en: {target_path}")

    # Copia en output
    import shutil
    shutil.copyfile(target_path, os.path.join(OUTPUT_DIR, "programa_formativo_diagramas_industriales.pdf"))
    print(f"Copia creada en: {os.path.join(OUTPUT_DIR, 'programa_formativo_diagramas_industriales.pdf')}")

if __name__ == "__main__":
    build_pdf()
