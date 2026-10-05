import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def set_cell_background(cell, fill_hex):
    tcPr = cell._element.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=70, bottom=70, left=90, right=90):
    tcPr = cell._element.get_or_add_tcPr()
    tcMar = parse_xml(
        f'<w:tcMar {nsdecls("w")}>'
        f'<w:top w:w="{top}" w:type="dxa"/>'
        f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
        f'<w:left w:w="{left}" w:type="dxa"/>'
        f'<w:right w:w="{right}" w:type="dxa"/>'
        f'</w:tcMar>'
    )
    tcPr.append(tcMar)

def set_table_borders(table, color="CBD5E0", sz="4"):
    tblPr = table._element.xpath('w:tblPr')
    if tblPr:
        borders = parse_xml(
            f'<w:tblBorders {nsdecls("w")}>'
            f'<w:top w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'<w:bottom w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'<w:insideH w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'<w:insideV w:val="none"/>'
            f'<w:left w:val="none"/>'
            f'<w:right w:val="none"/>'
            f'</w:tblBorders>'
        )
        tblPr[0].append(borders)

def add_callout(doc, text, bold_prefix="", fill_hex="F7FAFC", border_color="003366"):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    tbl.columns[0].width = Inches(6.5)
    
    cell = tbl.cell(0, 0)
    set_cell_background(cell, fill_hex)
    set_cell_margins(cell, top=120, bottom=120, left=180, right=120)
    
    tcPr = cell._element.get_or_add_tcPr()
    borders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'<w:left w:val="single" w:sz="24" w:space="0" w:color="{border_color}"/>'
        f'<w:top w:val="none"/>'
        f'<w:bottom w:val="none"/>'
        f'<w:right w:val="none"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.15
    
    if bold_prefix:
        r_pre = p.add_run(bold_prefix + " ")
        r_pre.font.name = "Calibri"
        r_pre.font.size = Pt(10)
        r_pre.font.bold = True
        r_pre.font.color.rgb = RGBColor(0, 51, 102)
        
    r_txt = p.add_run(text)
    r_txt.font.name = "Calibri"
    r_txt.font.size = Pt(10)
    r_txt.font.italic = True
    r_txt.font.color.rgb = RGBColor(45, 55, 72)
    
    p_post = doc.add_paragraph()
    style_p(p_post, space_before=0, space_after=6)

def style_heading(p, text, level=1, color=RGBColor(0, 51, 102)):
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    r.font.name = "Calibri"
    r.font.bold = True
    r.font.color.rgb = color
    if level == 1:
        p.paragraph_format.space_before = Pt(16)
        p.paragraph_format.space_after = Pt(6)
        r.font.size = Pt(15)
    elif level == 2:
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(4)
        r.font.size = Pt(13)
    elif level == 3:
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(2)
        r.font.size = Pt(11)

def style_p(p, space_before=0, space_after=6, line_spacing=1.15):
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = line_spacing

def generate_propuesta_doc():
    doc = docx.Document()
    
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    COLOR_PRIMARY = RGBColor(0, 51, 102)      # Azul Kinal
    COLOR_SECONDARY = RGBColor(74, 85, 104)    # Gris pizarra
    COLOR_DARK = RGBColor(26, 32, 44)         # Texto oscuro

    # =========================================================================
    # PORTADA INSTITUCIONAL
    # =========================================================================
    p_inst = doc.add_paragraph()
    style_p(p_inst, space_before=20, space_after=2)
    r_inst = p_inst.add_run("FUNDACIÓN KINAL")
    r_inst.font.name = "Calibri"
    r_inst.font.size = Pt(14)
    r_inst.font.bold = True
    r_inst.font.color.rgb = COLOR_PRIMARY

    p_esc = doc.add_paragraph()
    style_p(p_esc, space_before=0, space_after=20)
    r_esc = p_esc.add_run("Escuela Técnica Superior — Coordinación de Formación Continua y Empleabilidad")
    r_esc.font.name = "Calibri"
    r_esc.font.size = Pt(11)
    r_esc.font.color.rgb = COLOR_SECONDARY

    p_tit = doc.add_paragraph()
    style_p(p_tit, space_before=14, space_after=10)
    r_tit = p_tit.add_run("PLANIFICACIÓN Y PROPUESTA FORMATIVA INSTITUCIONAL:\nAUTOMATIZACIÓN Y CONTROL ELÉCTRICO INDUSTRIAL CON PLC Y VARIADORES DE FRECUENCIA (VFD)")
    r_tit.font.name = "Calibri"
    r_tit.font.size = Pt(18)
    r_tit.font.bold = True
    r_tit.font.color.rgb = COLOR_PRIMARY

    p_sub = doc.add_paragraph()
    style_p(p_sub, space_before=0, space_after=20)
    r_sub = p_sub.add_run("Programa de Certificación Técnica Profesional para la Operación, Parametrización y Comisionamiento en Plantas Industriales de Guatemala (120 Horas — 20 Sesiones)")
    r_sub.font.name = "Calibri"
    r_sub.font.size = Pt(11.5)
    r_sub.font.italic = True
    r_sub.font.color.rgb = COLOR_SECONDARY

    # Ficha Técnica
    tbl_ficha = doc.add_table(rows=8, cols=2)
    tbl_ficha.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_ficha.autofit = False
    tbl_ficha.columns[0].width = Inches(2.2)
    tbl_ficha.columns[1].width = Inches(4.3)
    set_table_borders(tbl_ficha, color="CBD5E0", sz="6")

    ficha_data = [
        ("Nivel Formativo de Referencia:", "Equivalencia DQR Nivel 4 - 5 (Competencia técnica especializada y autonomía operativa)"),
        ("Población Destinataria:", "Técnicos electricistas, electromecánicos, peritos industriales y supervisores de mantenimiento"),
        ("Duración Total:", "120 horas formativas (20 sesiones de 6 horas / 360 min; 110h de actividad neta de laboratorio)"),
        ("Modalidad de Impartición:", "Híbrida Asimétrica: 80% Práctica en Bancos Reales de Kinal (96h) y 20% Plataforma Virtual LMS (24h)"),
        ("Estructura de Horarios:", "Encuentros sabatinos de 1:00 p.m. a 7:00 p.m. o domingos intensivos (adaptado a turnos de planta)"),
        ("Orientación de Empleabilidad:", "Técnico especialista en automatización, electricista de planta, integrador de tableros industriales"),
        ("Nota Mínima Aprobatoria:", "75 puntos sobre 100 en todas las comprobaciones de banco, rúbricas de cableado y proyecto terminal"),
        ("Sede Presencial:", "Fundación Kinal — Laboratorios de Electrotecnia y Automatización, Sede Central, Zona 7, Ciudad de Guatemala")
    ]

    for idx, (label, val) in enumerate(ficha_data):
        row = tbl_ficha.rows[idx]
        set_cell_background(row.cells[0], "F7FAFC")
        set_cell_margins(row.cells[0], top=65, bottom=65, left=90, right=90)
        set_cell_margins(row.cells[1], top=65, bottom=65, left=90, right=90)
        
        p0 = row.cells[0].paragraphs[0]
        style_p(p0, space_before=0, space_after=0)
        r0 = p0.add_run(label)
        r0.font.name = "Calibri"
        r0.font.size = Pt(9.5)
        r0.font.bold = True
        r0.font.color.rgb = COLOR_PRIMARY

        p1 = row.cells[1].paragraphs[0]
        style_p(p1, space_before=0, space_after=0)
        r1 = p1.add_run(val)
        r1.font.name = "Calibri"
        r1.font.size = Pt(9.5)
        r1.font.color.rgb = COLOR_DARK

    doc.add_page_break()

    # =========================================================================
    # 1. MARCO FILOSÓFICO E IDEARIO DE KINAL: ÉTICA Y EL TRABAJO BIEN HECHO
    # =========================================================================
    h1_1 = doc.add_paragraph()
    style_heading(h1_1, "1. Marco Filosófico e Ideario Institucional de Fundación Kinal", level=1)

    p_id_desc = doc.add_paragraph()
    style_p(p_id_desc, space_before=0, space_after=6)
    r = p_id_desc.add_run("El diseño formativo de esta certificación técnica se fundamenta de forma irrenunciable en la visión cristiana del trabajo y en los principios pedagógicos e institucionales que caracterizan a Fundación Kinal:")
    r.font.name = "Calibri"
    r.font.size = Pt(10.5)
    r.font.color.rgb = COLOR_DARK

    add_callout(doc, "«Formar a jóvenes y adultos a través de una educación integral, con énfasis en las áreas técnicas y tecnológicas, influyendo positivamente en su trabajo, su familia y la sociedad».", bold_prefix="Misión Institucional de Kinal:")

    add_callout(doc, "«Visión cristiana de la vida. Respeto a la dignidad de la persona. Espíritu de servicio. Trabajo bien hecho. Libertad personal responsable».", bold_prefix="Valores Nucleares de Kinal:")

    p_et = doc.add_paragraph()
    style_heading(p_et, "1.1 El Principio del «Trabajo Bien Hecho» en el Control Eléctrico y Automatización Industrial", level=2)

    p_et_txt = doc.add_paragraph()
    style_p(p_et_txt, space_before=0, space_after=6)
    r = p_et_txt.add_run("En el ámbito del control eléctrico industrial y la automatización de procesos, la ética profesional y la excelencia operativa trascienden la mera operatividad de una máquina. Una conexión deficiente o un mal dimensionamiento no solo causa pérdidas millonarias por paradas de producción, sino que compromete la integridad física y la vida de los operadores. En este programa, el «trabajo bien hecho» se traduce en exigencias innegociables:\n"
                          "• Rigor y Estética Profesional en el Cableado: Peinado milimétrico de conductores, uso obligatorio de terminales de compresión (ferrules), rotulado alfanumérico indeleble bajo norma en cada borne y peinado en canaleta ranurada sin cruces desordenados ni cables forzados.\n"
                          "• Seguridad de Vida y Cero Tolerancia al Descuido: Aplicación estricta de protocolos de Bloqueo y Etiquetado (LOTO), verificación de desenergización con multímetro calibrado antes de cualquier manipulación y cumplimiento exhaustivo de las distancias de seguridad contra arco eléctrico (NFPA 70E).\n"
                          "• Honestidad y Trazabilidad Técnica: Registro fiel en planos «As-Built» de cada modificación realizada en planta, documentación veraz de fallas y códigos de error, sin ocultar averías ni realizar 'puentes' provisionales inseguros que vulneren las protecciones térmicas o paradas de emergencia.")
    r.font.name = "Calibri"
    r.font.size = Pt(10)
    r.font.color.rgb = COLOR_DARK

    # =========================================================================
    # 2. FUNDAMENTACIÓN TÉCNICA Y CASO TRANSVERSAL DE PLANTA INDUSTRIAL
    # =========================================================================
    h1_2 = doc.add_paragraph()
    style_heading(h1_2, "2. Fundamentación Técnica, Enfoque Pedagógico y Caso Transversal de Planta", level=1)

    p_met = doc.add_paragraph()
    style_p(p_met, space_before=0, space_after=6)
    r = p_met.add_run("A diferencia de capacitaciones tradicionales basadas en pizarrón o diapositivas desarticuladas, este programa adopta un enfoque de ingeniería práctica guiado por el contexto productivo de Guatemala (parques industriales de Mixco, Villa Nueva, Amatitlán, Escuintla y Carretera al Atlántico):\n"
                      "• Caso Transversal de Planta: Línea Continua de Embotellado y Empaque Automatizado: A lo largo de las 20 sesiones, los participantes desarrollan e integran modularmente el sistema electromecánico y de control de una línea de transporte y envasado. Se inicia con el dimensionamiento del tablero de fuerza y contactores, se prosigue con el control suave de velocidad y torque de bandas transportadoras mediante variadores VFD, se implementa la lógica combinacional y secuencial en PLC con sensórica industrial, culminando en la supervisión y diagnóstico de fallas inducidas en tiempo real.\n"
                      "• Práctica Directa en Banco Físico Individual y de Pareja: Cada participante trabaja con tableros de grado industrial, equipados con aparamenta real (Schneider / Siemens / ABB), motores trifásicos de inducción acoplados, variadores de frecuencia y autómatas programables Siemens S7-1200 y LOGO!.\n"
                      "• Metodología de la Acción Completa: Cada sesión reproduce las 6 etapas del método alemán: Informarse, Planificar, Decidir, Realizar, Controlar y Evaluar, desarrollando autonomía técnica y juicio crítico en diagnóstico sistemático.")
    r.font.name = "Calibri"
    r.font.size = Pt(10)
    r.font.color.rgb = COLOR_DARK

    # =========================================================================
    # 3. MARCO DQR Y SISTEMA DUAL DE APRENDIZAJE
    # =========================================================================
    h1_3 = doc.add_paragraph()
    style_heading(h1_3, "3. Marco Alemán de Cualificaciones (DQR Nivel 4-5) y Enfoque Dual", level=1)

    add_callout(doc, "«concepto de aprendizaje para jóvenes que tiene como objetivo preparar a los aprendices para su vida profesional, por lo que la formación se realiza en régimen de alternancia entre la escuela o el centro de formación y la empresa. El aprender en el proceso del trabajo es base y a la vez objetivo de la acción formativa».", bold_prefix="Definición de Formación Profesional Dual:")

    add_callout(doc, "«the ability and readiness of the individual to use knowledge, skills and personal, social and methodological competences and to behave in a considered, individual and socially responsible manner. Competence is understood in this sense as the comprehensive ability to act».", bold_prefix="Concepto de Competencia en el DQR:")

    p_dqr_txt = doc.add_paragraph()
    style_p(p_dqr_txt, space_before=0, space_after=6)
    r = p_dqr_txt.add_run("El programa articula las dos dimensiones maestras de competencia del Marco Alemán de Cualificaciones:\n"
                          "1. Dimensión de Competencia Profesional (Professional Competence):\n"
                          "   • Conocimientos (Knowledge): Dominio riguroso de leyes eléctricas, diagramas bajo norma IEC 60617 / NEMA, arquitectura interna de PLCs, modulación PWM en variadores y protocolos de comunicación industrial (PROFINET / Modbus RTU).\n"
                          "   • Destrezas (Skills): Habilidad manual para cableado pulcro de tableros, uso diestro de instrumental (multímetros True-RMS, pinzas amperimétricas, tacómetros digitales), programación en Ladder estructurado y resolución metódica de averías bajo presión temporal.\n"
                          "2. Dimensión de Competencia Personal (Personal Competence):\n"
                          "   • Competencia Social (Social Competence): Trabajo colaborativo en cuadrilla técnica, comunicación asertiva en handover de turnos y reporte claro a jefaturas de planta.\n"
                          "   • Autonomía (Autonomy): Responsabilidad autónoma para verificar la seguridad de una instalación, reflexividad técnica para justificar elecciones de diseño y apego voluntario a las normas de seguridad ocupacional.")
    r.font.name = "Calibri"
    r.font.size = Pt(10)
    r.font.color.rgb = COLOR_DARK

    # =========================================================================
    # 4. COMPETENCIA GENERAL Y PERFILES DE ENTRADA Y SALIDA
    # =========================================================================
    h1_4 = doc.add_paragraph()
    style_heading(h1_4, "4. Competencia General y Perfiles del Participante", level=1)

    p_comp = doc.add_paragraph()
    style_p(p_comp, space_before=0, space_after=6)
    r = p_comp.add_run("Competencia General del Programa:\n"
                       "El egresado dimensiona, ensambla, cablea, parametriza y programa sistemas de control eléctrico y fuerza para procesos industriales continuos, utilizando contactores, variadores de frecuencia (VFD) y controladores lógicos programables (PLC Siemens S7-1200 / LOGO!), aplicando estrictamente las normativas de seguridad eléctrica (NFPA 70E / NEC), interpretando diagramas bajo norma IEC/NEMA y demostrando un estándar de «trabajo bien hecho», orden y diagnóstico metódico de averías en banco de pruebas real.")
    r.font.name = "Calibri"
    r.font.size = Pt(10)
    r.font.bold = True
    r.font.color.rgb = COLOR_PRIMARY

    p_perfiles = doc.add_paragraph()
    style_p(p_perfiles, space_before=4, space_after=6)
    r = p_perfiles.add_run("• Perfil de Ingreso: Técnicos electricistas, electromecánicos, peritos en electricidad o electrónica, bachilleres industriales o personal empírico con un mínimo de 1 año de experiencia en mantenimiento de plantas o talleres. Requiere comprensión de circuitos eléctricos básicos (Ley de Ohm, corriente alterna monofásica/trifásica) y manejo elemental de computadora.\n"
                           "• Perfil de Egreso y Empleabilidad: Técnico especialista capacitado para integrarse de inmediato a departamentos de mantenimiento eléctrico, instrumentación o proyectos en fábricas de alimentos, plásticos, empaques, farmacéuticas y talleres de integración de tableros, con solvencia para intervenir fallas, poner en marcha motores con variador y programar rutinas de automatización en PLC con total apego a normas de seguridad.")
    r.font.name = "Calibri"
    r.font.size = Pt(10)
    r.font.color.rgb = COLOR_DARK

    # =========================================================================
    # 5. ESTRUCTURA MODULAR Y DOSIFICACIÓN DE LA CARGA HORARIA
    # =========================================================================
    h1_5 = doc.add_paragraph()
    style_heading(h1_5, "5. Estructura Modular y Distribución Formativa (120 Horas)", level=1)

    modulos_data = [
        ("Módulo 1", "Control Eléctrico Industrial, Mando y Diseño de Tableros de Fuerza", "30 Horas", "5 Sesiones", "Tablero de Fuerza y Mando Ensamble Físico con Inversión de Giro y Estrella-Triángulo"),
        ("Módulo 2", "Parametrización, Control y Puesta en Marcha de Variadores de Frecuencia (VFD)", "30 Horas", "5 Sesiones", "Puesta en Marcha de VFD con Multivelocidad, Señal 4-20mA y Rampas de Frenado"),
        ("Módulo 3", "Programación y Cableado de Controladores Lógicos Programables (PLC Siemens)", "30 Horas", "5 Sesiones", "Automatización de Estación de Envasado con Sensores Industriales y PLC S7-1200"),
        ("Módulo 4", "Integración Automatizada, Redes Industriales y Diagnóstico de Averías", "30 Horas", "5 Sesiones", "Comisionamiento Integral PLC-VFD-HMI y Resolución de Fallas Inducidas en Banco")
    ]

    tbl_mod = doc.add_table(rows=5, cols=5)
    tbl_mod.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_mod.autofit = False
    tbl_mod.columns[0].width = Inches(1.0)
    tbl_mod.columns[1].width = Inches(2.2)
    tbl_mod.columns[2].width = Inches(0.8)
    tbl_mod.columns[3].width = Inches(0.9)
    tbl_mod.columns[4].width = Inches(1.6)
    set_table_borders(tbl_mod, color="CBD5E0", sz="4")

    hdr_mod = tbl_mod.rows[0]
    for c in hdr_mod.cells:
        set_cell_background(c, "003366")
    headers_mod_txt = ["Módulo", "Nombre de la Unidad Formativa", "Horas", "Sesiones", "Producto Terminal del Módulo"]
    for idx, text in enumerate(headers_mod_txt):
        p = hdr_mod.cells[idx].paragraphs[0]
        style_p(p, space_before=0, space_after=0)
        r = p.add_run(text)
        r.font.name = "Calibri"
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    for idx, (m_id, m_nom, m_hrs, m_ses, m_prod) in enumerate(modulos_data, start=1):
        row = tbl_mod.rows[idx]
        if idx % 2 == 1:
            for c in row.cells:
                set_cell_background(c, "F7FAFC")
        for c_idx, val in enumerate([m_id, m_nom, m_hrs, m_ses, m_prod]):
            cell = row.cells[c_idx]
            set_cell_margins(cell, top=55, bottom=55, left=65, right=65)
            p = cell.paragraphs[0]
            style_p(p, space_before=0, space_after=0)
            r = p.add_run(val)
            r.font.name = "Calibri"
            r.font.size = Pt(8.5)
            r.font.color.rgb = COLOR_DARK
            if c_idx in [0, 2]:
                r.font.bold = True

    p_balance = doc.add_paragraph()
    style_p(p_balance, space_before=8, space_after=6)
    r = p_balance.add_run("Balance de Modalidad y Distribución del Tiempo Pedagógico:\n"
                          "• 80% Horas Prácticas en Taller/Laboratorio (96 horas): Cableado directo en tableros, configuración en teclado de variadores, montaje de sensores, descargas de programas a PLC y resolución de averías en banco físico de pruebas.\n"
                          "• 20% Horas en Plataforma Digital e Interpretación (24 horas): Lectura analítica de manuales técnicos de fabricante (Siemens, Schneider, WEG), diagramación en software CAD eléctrico (CADe SIMU) y cuestionarios previos de seguridad en Google Classroom institucional.")
    r.font.name = "Calibri"
    r.font.size = Pt(9.5)
    r.font.color.rgb = COLOR_DARK

    # =========================================================================
    # 6. ESTRATEGIA DIDÁCTICA EN TALLER Y BITÁCORA BERICHTSHEFT
    # =========================================================================
    h1_6 = doc.add_paragraph()
    style_heading(h1_6, "6. Estrategia Didáctica en Laboratorio y Bitácora Semanal «Berichtsheft»", level=1)

    p_didact = doc.add_paragraph()
    style_p(p_didact, space_before=0, space_after=6)
    r = p_didact.add_run("Para garantizar la asimilación profunda y la transferencia real al puesto de trabajo, se implementan dos pilares metodológicos:\n"
                         "1. Método de las 6 Fases de la Acción Completa (Modell der vollständigen Handlung):\n"
                         "   • Fase 1 - Informar: Análisis del problema de planta y especificaciones técnicas de la máquina.\n"
                         "   • Fase 2 - Planificar: Diseño de esquemas eléctricos, selección de calibres y asignación de direcciones de I/O.\n"
                         "   • Fase 3 - Decidir: Validación conjunta con el instructor antes de realizar cualquier conexión física.\n"
                         "   • Fase 4 - Ejecutar: Montaje mecánico en riel DIN, cableado pulcro y programación en software.\n"
                         "   • Fase 5 - Controlar: Protocolo de energización escalonada y medición con multímetro de aislamientos y continuidades.\n"
                         "   • Fase 6 - Valorar: Reflexión sobre dificultades encontradas, tiempos de ejecución y lecciones aprendidas.\n"
                         "2. Bitácora Semanal de Aprendizaje Berichtsheft (Estándar Dual Alemán):\n"
                         "   Cada estudiante registra semanalmente: fecha de la práctica, descripción detallada del circuito o rutina programada, normas de seguridad aplicadas, problemas y fallas enfrentadas, y cómo fueron resueltos bajo el criterio del «trabajo bien hecho». Esta bitácora es visada por el instructor y constituye un requisito obligatorio para optar a la certificación final.")
    r.font.name = "Calibri"
    r.font.size = Pt(10)
    r.font.color.rgb = COLOR_DARK

    # =========================================================================
    # 7. SISTEMA DE EVALUACIÓN Y UMBRAL APROBATORIO INSTITUCIONAL
    # =========================================================================
    h1_7 = doc.add_paragraph()
    style_heading(h1_7, "7. Sistema de Evaluación Institucional y Criterio de Acreditación", level=1)

    add_callout(doc, "La aprobación de cada módulo formativo y la certificación profesional final requieren alcanzar una calificación mínima de 75 puntos sobre 100 en todas las comprobaciones de banco, listas de cotejo de taller y evaluación de proyecto terminal, de acuerdo con la Normativa de Convivencia y Evaluación de Fundación Kinal.", bold_prefix="Umbral Aprobatorio Institucional Obligatorio:")

    eval_data = [
        ("Pruebas Prácticas de Taller y Rúbricas de Ensamble (40%)", "Evaluación continua sesión por sesión del cableado, conexionado, peinado, rotulado y pruebas de funcionamiento de circuitos de fuerza y control sin cortocircuitos."),
        ("Programación y Comisionamiento en Software / PLC / VFD (30%)", "Evaluación de la lógica estructurada en Ladder, correcta parametrización de variadores, mapeo de señales y comisionamiento de secuencias automáticas."),
        ("Bitácora Semanal Berichtsheft y Dossier Técnico (10%)", "Revisión quincenal de bitácoras, diagramas 'As-Built' actualizados y hojas de cálculo de calibración de protecciones eléctricas."),
        ("Proyecto Integrador Terminal y Diagnóstico de Fallas (20%)", "Prueba individual de certificación en banco real: puesta en marcha de un proceso continuo integrado y diagnóstico de 2 fallas inducidas en menos de 60 minutos.")
    ]

    tbl_ev = doc.add_table(rows=5, cols=2)
    tbl_ev.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_ev.autofit = False
    tbl_ev.columns[0].width = Inches(2.5)
    tbl_ev.columns[1].width = Inches(4.0)
    set_table_borders(tbl_ev, color="CBD5E0", sz="4")

    hdr_ev = tbl_ev.rows[0]
    for c in hdr_ev.cells:
        set_cell_background(c, "003366")
    for idx, text in enumerate(["Componente de Evaluación", "Criterio de Desempeño y Evidencia"]):
        p = hdr_ev.cells[idx].paragraphs[0]
        style_p(p, space_before=0, space_after=0)
        r = p.add_run(text)
        r.font.name = "Calibri"
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    for idx, (comp, crit) in enumerate(eval_data, start=1):
        row = tbl_ev.rows[idx]
        if idx % 2 == 1:
            for c in row.cells:
                set_cell_background(c, "F7FAFC")
        for c_idx, val in enumerate([comp, crit]):
            cell = row.cells[c_idx]
            set_cell_margins(cell, top=55, bottom=55, left=65, right=65)
            p = cell.paragraphs[0]
            style_p(p, space_before=0, space_after=0)
            r = p.add_run(val)
            r.font.name = "Calibri"
            r.font.size = Pt(8.5)
            r.font.color.rgb = COLOR_DARK
            if c_idx == 0:
                r.font.bold = True

    # =========================================================================
    # 8. INFRAESTRUCTURA Y SEGURIDAD INDUSTRIAL EN KINAL
    # =========================================================================
    h1_8 = doc.add_paragraph()
    style_heading(h1_8, "8. Equipamiento de Laboratorio y Requerimientos de Seguridad Industrial", level=1)

    p_infra = doc.add_paragraph()
    style_p(p_infra, space_before=0, space_after=6)
    r = p_infra.add_run("El programa se imparte íntegramente en los laboratorios de electrotecnia y automatización de Fundación Kinal, dotados de:\n"
                        "• Estaciones de Trabajo Eléctricas: Módulos con riel DIN, canaleta ranurada, tomas trifásicas de 220V/208V y monofásicas de 120V con protección diferencial GFCI.\n"
                        "• Aparamenta Industrial: Contactores AC-3 (Siemens Sirius / Schneider TeSys), relés térmicos, guardamotores magneto-térmicos, temporizadores y botoneras de mando industrial.\n"
                        "• Bancos de Motores y Variadores: Motores trifásicos jaula de ardilla (0.5 a 1.5 HP), variadores de frecuencia de última generación (Siemens Sinamics V20 / Schneider Altivar / Danfoss) con paneles de operación integrados.\n"
                        "• Controladores Lógicos y Sensórica: PLCs Siemens S7-1200 (CPU 1214C DC/DC/DC) y módulos LOGO! 24RCE con software TIA Portal con licencias académicas, sensores industriales inductivos, fotoeléctricos y capacitivos.\n"
                        "• Normas de Seguridad Obligatorias: Uso innegociable de calzado de seguridad con puntera dieléctrica, gafas de protección policarbonato, candados y tarjetas LOTO individuales, y prohibición estricta de anillos, relojes metálicos o ropa holgada.")
    r.font.name = "Calibri"
    r.font.size = Pt(9.5)
    r.font.color.rgb = COLOR_DARK

    section = doc.sections[0]
    footer = section.footer
    footer_p = footer.paragraphs[0]
    style_p(footer_p, space_before=0, space_after=0)
    footer_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run_f = footer_p.add_run("Fundación Kinal | Automatización y Control Eléctrico Industrial — Propuesta Curricular Oficial")
    run_f.font.name = "Calibri"
    run_f.font.size = Pt(8.5)
    run_f.font.color.rgb = COLOR_SECONDARY

    out_dir = os.path.join("Cursos", "Automatización")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "Propuesta_Curso_Automatizacion_Kinal.docx")
    doc.save(out_path)
    print(f"Propuesta guardada con éxito en: {out_path}")

if __name__ == "__main__":
    generate_propuesta_doc()
