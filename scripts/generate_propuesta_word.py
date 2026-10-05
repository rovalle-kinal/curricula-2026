import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

def set_cell_background(cell, fill_hex):
    tcPr = cell._element.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=100, bottom=100, left=150, right=150):
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
    set_cell_margins(cell, top=140, bottom=140, left=200, right=140)
    
    # Left border only
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
        r_pre.font.size = Pt(10.5)
        r_pre.font.bold = True
        r_pre.font.color.rgb = RGBColor(0, 51, 102)
        
    r_txt = p.add_run(text)
    r_txt.font.name = "Calibri"
    r_txt.font.size = Pt(10.5)
    r_txt.font.italic = True
    r_txt.font.color.rgb = RGBColor(45, 55, 72)
    
    # Add a blank spacing paragraph after
    p_post = doc.add_paragraph()
    p_post.paragraph_format.space_before = Pt(0)
    p_post.paragraph_format.space_after = Pt(6)

def style_heading(p, text, level=1, color=RGBColor(0, 51, 102)):
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    r.font.name = "Calibri"
    r.font.bold = True
    r.font.color.rgb = color
    if level == 1:
        p.paragraph_format.space_before = Pt(18)
        p.paragraph_format.space_after = Pt(6)
        r.font.size = Pt(16)
    elif level == 2:
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(4)
        r.font.size = Pt(13)
    elif level == 3:
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(2)
        r.font.size = Pt(11.5)

def style_p(p, space_before=0, space_after=6, line_spacing=1.15):
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = line_spacing

def generate_propuesta():
    doc = docx.Document()
    
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    COLOR_PRIMARY = RGBColor(0, 51, 102)
    COLOR_SECONDARY = RGBColor(74, 85, 104)
    COLOR_DARK = RGBColor(26, 32, 44)

    # =========================================================================
    # PORTADA INSTITUCIONAL
    # =========================================================================
    p_inst = doc.add_paragraph()
    style_p(p_inst, space_before=24, space_after=4)
    r_inst = p_inst.add_run("FUNDACIÓN KINAL")
    r_inst.font.name = "Calibri"
    r_inst.font.size = Pt(14)
    r_inst.font.bold = True
    r_inst.font.color.rgb = COLOR_PRIMARY

    p_esc = doc.add_paragraph()
    style_p(p_esc, space_before=0, space_after=24)
    r_esc = p_esc.add_run("Escuela Técnica Superior — Coordinación de Formación Continua e Innovación")
    r_esc.font.name = "Calibri"
    r_esc.font.size = Pt(11)
    r_esc.font.color.rgb = COLOR_SECONDARY

    p_tit = doc.add_paragraph()
    style_p(p_tit, space_before=18, space_after=12)
    r_tit = p_tit.add_run("PROPUESTA FORMATIVA INSTITUCIONAL:\nCURSO DE MECATRÓNICA INDUSTRIAL Y FABRICACIÓN DIGITAL APLICADA")
    r_tit.font.name = "Calibri"
    r_tit.font.size = Pt(22)
    r_tit.font.bold = True
    r_tit.font.color.rgb = COLOR_PRIMARY

    p_sub = doc.add_paragraph()
    style_p(p_sub, space_before=0, space_after=24)
    r_sub = p_sub.add_run("Integración Práctica de Impresión 3D, Corte Láser, Fresado CNC, Sensórica Industrial y Control para el Parque Productivo de Guatemala")
    r_sub.font.name = "Calibri"
    r_sub.font.size = Pt(12)
    r_sub.font.italic = True
    r_sub.font.color.rgb = COLOR_SECONDARY

    # Tabla Ficha Técnica
    tbl_ficha = doc.add_table(rows=7, cols=2)
    tbl_ficha.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_ficha.autofit = False
    tbl_ficha.columns[0].width = Inches(2.2)
    tbl_ficha.columns[1].width = Inches(4.3)
    set_table_borders(tbl_ficha, color="CBD5E0", sz="6")

    ficha_data = [
        ("Nivel Formativo de Referencia:", "Equivalencia DQR Nivel 4 - 5 (Cualificación técnica especializada y autonomía operativa)"),
        ("Duración Total:", "90 horas pedagógicas presenciales (20 sesiones sabatinas de 4.5 horas)"),
        ("Temporalidad:", "5 meses continuos (Febrero a Junio) — Sábados de 8:00 a 12:30 horas"),
        ("Modalidad:", "Presencial en Talleres de Fabricación Digital y Automatización Kinal"),
        ("Distribución Metodológica:", "25% Fundamentación Técnica / 75% Ejecución Práctica en Maquinaria y Banco"),
        ("Nota Mínima Aprobatoria:", "75 puntos sobre 100 en todas las evaluaciones de módulo y proyecto terminal"),
        ("Sede:", "Fundación Kinal — Sede Central, Zona 7, Ciudad de Guatemala")
    ]

    for idx, (label, val) in enumerate(ficha_data):
        row = tbl_ficha.rows[idx]
        set_cell_background(row.cells[0], "F7FAFC")
        set_cell_margins(row.cells[0], top=80, bottom=80, left=100, right=100)
        set_cell_margins(row.cells[1], top=80, bottom=80, left=100, right=100)
        
        p0 = row.cells[0].paragraphs[0]
        style_p(p0, space_before=0, space_after=0)
        r0 = p0.add_run(label)
        r0.font.name = "Calibri"
        r0.font.size = Pt(10)
        r0.font.bold = True
        r0.font.color.rgb = COLOR_PRIMARY

        p1 = row.cells[1].paragraphs[0]
        style_p(p1, space_before=0, space_after=0)
        r1 = p1.add_run(val)
        r1.font.name = "Calibri"
        r1.font.size = Pt(10)
        r1.font.color.rgb = COLOR_DARK

    doc.add_page_break()

    # =========================================================================
    # 1. MARCO FILOSÓFICO E IDEARIO INSTITUCIONAL DE FUNDACIÓN KINAL
    # =========================================================================
    h1_1 = doc.add_paragraph()
    style_heading(h1_1, "1. Marco Filosófico e Ideario Institucional de Fundación Kinal", level=1)

    p_id1 = doc.add_paragraph()
    style_p(p_id1, space_before=0, space_after=6)
    r = p_id1.add_run("El presente diseño formativo responde de manera estricta a la identidad, misión y valores de Fundación Kinal, asegurando que la capacitación técnica de vanguardia esté indisolublemente unida a la formación ética y humana:")
    r.font.name = "Calibri"
    r.font.size = Pt(11)
    r.font.color.rgb = COLOR_DARK

    add_callout(doc, "«Formar a jóvenes y adultos a través de una educación integral, con énfasis en las áreas técnicas y tecnológicas, influyendo positivamente en su trabajo, su familia y la sociedad».", bold_prefix="Misión Institucional de Kinal:")

    add_callout(doc, "«Visión cristiana de la vida. Respeto a la dignidad de la persona. Espíritu de servicio. Trabajo bien hecho. Libertad personal responsable».", bold_prefix="Valores Nucleares de Kinal:")

    p_wb = doc.add_paragraph()
    style_heading(p_wb, "1.1 El Principio Rector del «Trabajo Bien Hecho» en el Taller de Mecatrónica", level=2)

    p_wb_txt = doc.add_paragraph()
    style_p(p_wb_txt, space_before=0, space_after=6)
    r = p_wb_txt.add_run("En la formación mecatrónica de Kinal, el principio del «trabajo bien hecho» no es un concepto abstracto, sino una norma de ejecución tangible y evaluable en cada sesión de taller:\n"
                          "• Precisión y Exactitud Dimensional: Cero holguras imprevistas; verificación rigurosa de tolerancias (±0.1 mm) en piezas cortadas en láser, impresas en 3D y mecanizadas en CNC.\n"
                          "• Estética Industrial y Seguridad en Cableado: Prohibición total de conductores con hilos desnudos sueltos; uso obligatorio de casquillos de compresión aislados (ferrules), peinado estético en canaleta ranurada, separación física de potencia (110/220 VAC) y control (24 VDC), y rotulado alfanumérico según norma internacional IEC 60617.\n"
                          "• Cultura de Seguridad Integral: Uso permanente del Equipo de Protección Personal (EPP), aplicación de procedimientos LOTO (consignación y bloqueo de energía) y protocolo 5S de orden y limpieza en bancos y máquinas.")
    r.font.name = "Calibri"
    r.font.size = Pt(10.5)
    r.font.color.rgb = COLOR_DARK

    # =========================================================================
    # 2. FUNDAMENTACIÓN TÉCNICA Y PERTINENCIA EN EL MERCADO GUATEMALTECO
    # =========================================================================
    h1_2 = doc.add_paragraph()
    style_heading(h1_2, "2. Fundamentación Técnica y Pertinencia en el Mercado Laboral Guatemalteco", level=1)

    p_ind = doc.add_paragraph()
    style_p(p_ind, space_before=0, space_after=6)
    r = p_ind.add_run("El sector industrial de Guatemala —liderado por empresas de alimentos y bebidas, plásticos, empaques flexibles, farmacéutica, ingenios azucareros y metalmecánica— se encuentra inmerso en una modernización hacia la automatización y la Industria 4.0. No obstante, las plantas productivas enfrentan cuellos de botella operacionales recurrentes:\n"
                      "1. Obsolescencia y Ruptura de Piezas Mecánicas Descontinuadas: Muchas líneas europeas o americanas sufren paros costosos de semanas por falta de repuestos. Mediante ingeniería inversa, modelado CAD y manufactura aditiva (impresión 3D en filamentos técnicos PETG, Nylon o ABS) o sustractiva (fresado CNC), los egresados pueden solucionar contingencias en horas en el propio taller de mantenimiento.\n"
                      "2. Demanda de Dispositivos Poka-Yoke y Nidos de Ensamble (Jigs & Fixtures): La necesidad de asegurar calidad cero-defectos exige plantillas y fijaciones hechas a la medida. La cortadora láser y el router CNC permiten fabricar dispositivos de sujeción e inspección dimensional rápidos y de bajo costo.\n"
                      "3. Transición de Líneas Manuales a Automatizadas: Las plantas requieren integrar actuadores neumáticos, motores a pasos y sensórica industrial con cableados ordenados y seguros.")
    r.font.name = "Calibri"
    r.font.size = Pt(10.5)
    r.font.color.rgb = COLOR_DARK

    # =========================================================================
    # 3. MARCO ALEMÁN DE CUALIFICACIONES (DQR) Y SISTEMA DUAL
    # =========================================================================
    h1_3 = doc.add_paragraph()
    style_heading(h1_3, "3. Marco Alemán de Cualificaciones (DQR Nivel 4-5) y Enfoque Dual", level=1)

    add_callout(doc, "«concepto de aprendizaje para jóvenes que tiene como objetivo preparar a los aprendices para su vida profesional, por lo que la formación se realiza en régimen de alternancia entre la escuela o el centro de formación y la empresa. El aprender en el proceso del trabajo es base y a la vez objetivo de la acción formativa».", bold_prefix="Definición de Formación Profesional Dual:")

    add_callout(doc, "«the ability and readiness of the individual to use knowledge, skills and personal, social and methodological competences and to behave in a considered, individual and socially responsible manner. Competence is understood in this sense as the comprehensive ability to act».", bold_prefix="Definición Oficial de Competencia según el DQR:")

    p_mat = doc.add_paragraph()
    style_p(p_mat, space_before=4, space_after=6)
    r = p_mat.add_run("Estructura de la Matriz de Competencias DQR aplicada al Curso:")
    r.font.name = "Calibri"
    r.font.size = Pt(11)
    r.font.bold = True
    r.font.color.rgb = COLOR_PRIMARY

    tbl_dqr = doc.add_table(rows=5, cols=3)
    tbl_dqr.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_dqr.autofit = False
    tbl_dqr.columns[0].width = Inches(1.8)
    tbl_dqr.columns[1].width = Inches(1.6)
    tbl_dqr.columns[2].width = Inches(3.1)
    set_table_borders(tbl_dqr, color="CBD5E0", sz="4")

    # Header
    hdr = tbl_dqr.rows[0]
    set_cell_background(hdr.cells[0], "003366")
    set_cell_background(hdr.cells[1], "003366")
    set_cell_background(hdr.cells[2], "003366")
    for idx, title in enumerate(["Dimensión DQR", "Subdimensión", "Evidencia de Desempeño en el Curso"]):
        p = hdr.cells[idx].paragraphs[0]
        style_p(p, space_before=0, space_after=0)
        r = p.add_run(title)
        r.font.name = "Calibri"
        r.font.size = Pt(10)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    dqr_rows = [
        ("Competencia Profesional\n(Fachkompetenz)", "Conocimientos\n(Wissen)", "Fundamentos cinemáticos de mecanismos, ciencia de polímeros y metales mecanizables, parámetros de corte CNC, física de sensores y lógica de control secuencial."),
        ("Competencia Profesional\n(Fachkompetenz)", "Destrezas\n(Fertigkeiten)", "Modelado CAD paramétrico 3D, programación CAM y Código G, operación segura de láser, impresora 3D y CNC, ensamble mecánico y cableado bajo norma IEC 60617."),
        ("Competencia Personal\n(Personale Kompetenz)", "Competencia Social\n(Sozialkompetenz)", "Trabajo coordinado en equipo en banco de taller, comunicación técnica asertiva, resolución compartida de fallas (troubleshooting) y espíritu de servicio."),
        ("Competencia Personal\n(Personale Kompetenz)", "Autonomía\n(Selbständigkeit)", "Planificación autónoma del flujo de manufactura, verificación dimensional metrológica, apego riguroso al EPP y autoexigencia del 'trabajo bien hecho'.")
    ]

    for idx, (dim, subdim, evid) in enumerate(dqr_rows, start=1):
        row = tbl_dqr.rows[idx]
        if idx % 2 == 1:
            set_cell_background(row.cells[0], "F7FAFC")
            set_cell_background(row.cells[1], "F7FAFC")
            set_cell_background(row.cells[2], "F7FAFC")
        for c_idx, val in enumerate([dim, subdim, evid]):
            cell = row.cells[c_idx]
            set_cell_margins(cell, top=80, bottom=80, left=100, right=100)
            p = cell.paragraphs[0]
            style_p(p, space_before=0, space_after=0)
            r = p.add_run(val)
            r.font.name = "Calibri"
            r.font.size = Pt(9.5)
            r.font.color.rgb = COLOR_DARK

    doc.add_page_break()

    # =========================================================================
    # 4. PERFILES DE INGRESO Y EGRESO
    # =========================================================================
    h1_4 = doc.add_paragraph()
    style_heading(h1_4, "4. Perfiles de Ingreso y Egreso Institucional", level=1)

    p_ing = doc.add_paragraph()
    style_heading(p_ing, "4.1 Perfil de Ingreso", level=2)
    p_ing_txt = doc.add_paragraph()
    style_p(p_ing_txt, space_before=0, space_after=6)
    r = p_ing_txt.add_run("Dirigido a técnicos, electromecánicos, bachilleres industriales y estudiantes de ingeniería con nociones básicas de electricidad o mecánica, interesados en manufactura y automatización, con compromiso de puntualidad, respeto a las normas de seguridad del taller y actitud hacia el aprendizaje técnico disciplinado.")
    r.font.name = "Calibri"
    r.font.size = Pt(11)
    r.font.color.rgb = COLOR_DARK

    p_egr = doc.add_paragraph()
    style_heading(p_egr, "4.2 Perfil de Egreso", level=2)
    p_egr_txt = doc.add_paragraph()
    style_p(p_egr_txt, space_before=0, space_after=12)
    r = p_egr_txt.add_run("El egresado manufactura piezas mecánicas de precisión mediante corte láser, impresión 3D y fresado CNC, conectando y calibrando sensores y actuadores electromecánicos para poner en marcha y mantener celdas mecatrónicas industriales bajo estándares internacionales, criterios de calidad rigurosos y el valor del trabajo bien hecho.")
    r.font.name = "Calibri"
    r.font.size = Pt(11)
    r.font.color.rgb = COLOR_DARK

    # =========================================================================
    # 5. ESTRUCTURA MODULAR Y PROYECTOS POR MÓDULO (90 HORAS)
    # =========================================================================
    h1_5 = doc.add_paragraph()
    style_heading(h1_5, "5. Arquitectura Curricular y Proyectos de Desempeño por Módulo", level=1)

    p_mod_desc = doc.add_paragraph()
    style_p(p_mod_desc, space_before=0, space_after=6)
    r = p_mod_desc.add_run("El programa se organiza en 5 módulos progresivos de 18 horas cada uno (4 sesiones de 4.5 horas al mes), donde cada módulo culmina con un proyecto funcional calificado con nota mínima aprobatoria de 75 puntos:")
    r.font.name = "Calibri"
    r.font.size = Pt(10.5)
    r.font.color.rgb = COLOR_DARK

    tbl_mods = doc.add_table(rows=6, cols=5)
    tbl_mods.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_mods.autofit = False
    tbl_mods.columns[0].width = Inches(1.1)
    tbl_mods.columns[1].width = Inches(1.8)
    tbl_mods.columns[2].width = Inches(1.4)
    tbl_mods.columns[3].width = Inches(1.6)
    tbl_mods.columns[4].width = Inches(0.6)
    set_table_borders(tbl_mods, color="CBD5E0", sz="4")

    # Header
    hdr = tbl_mods.rows[0]
    for c in hdr.cells:
        set_cell_background(c, "003366")
    headers = ["Módulo / Mes", "Eje Temático Principal", "Tecnología Kinal", "Proyecto Calificado (≥ 75 pts)", "Horas"]
    for idx, text in enumerate(headers):
        p = hdr.cells[idx].paragraphs[0]
        style_p(p, space_before=0, space_after=0)
        r = p.add_run(text)
        r.font.name = "Calibri"
        r.font.size = Pt(9.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    mods_data = [
        ("Módulo 1\n(Febrero)", "Diseño CAD 3D, Metrología y Prototipado", "Cortadora Láser CO2 y Metrología", "Gabinete Industrial con Riel DIN y Nido de Sujeción (Fixture)", "18 h"),
        ("Módulo 2\n(Marzo)", "Fabricación Aditiva Avanzada (FDM)", "Granja de Impresoras 3D y Filamentos", "Garra Robótica Articulada con Insertos Térmicos y Engranes", "18 h"),
        ("Módulo 3\n(Abril)", "Mecanizado Sustractivo y Fresado CNC", "Router CNC, CAM y Código G", "Bancada Mecatrónica Plana con Cajeras de Precisión y Guías", "18 h"),
        ("Módulo 4\n(Mayo)", "Sensórica, Actuación y Control de Ejes", "Drivers, Motores a Pasos, Neumática", "Eje Lineal Motorizado con Parada Segura y Cableado Normado", "18 h"),
        ("Módulo 5\n(Junio)", "Integración y Proyecto Capstone Industrial", "Toda la Infraestructura Integrada", "Mini-Celda Mecatrónica Industrial Automatizada (Capstone)", "18 h")
    ]

    for idx, (m, eje, tec, proy, hrs) in enumerate(mods_data, start=1):
        row = tbl_mods.rows[idx]
        if idx % 2 == 1:
            for c in row.cells:
                set_cell_background(c, "F7FAFC")
        for c_idx, val in enumerate([m, eje, tec, proy, hrs]):
            cell = row.cells[c_idx]
            set_cell_margins(cell, top=70, bottom=70, left=80, right=80)
            p = cell.paragraphs[0]
            style_p(p, space_before=0, space_after=0)
            r = p.add_run(val)
            r.font.name = "Calibri"
            r.font.size = Pt(9)
            r.font.color.rgb = COLOR_DARK
            if c_idx in [0, 4]:
                r.font.bold = True

    # =========================================================================
    # 6. ESQUEMA DE EVALUACIÓN Y ACREDITACIÓN INSTITUCIONAL (KINAL)
    # =========================================================================
    h1_6 = doc.add_paragraph()
    style_heading(h1_6, "6. Esquema de Evaluación, Bitácora Berichtsheft y Acreditación", level=1)

    p_ev_desc = doc.add_paragraph()
    style_p(p_ev_desc, space_before=0, space_after=6)
    r = p_ev_desc.add_run("Conforme a la normativa institucional de Kinal, el umbral mínimo de aprobación para cada módulo y para la certificación final es de 75 puntos sobre 100. La evaluación es integral e involucra tanto el producto técnico final como los hábitos formativos:")
    r.font.name = "Calibri"
    r.font.size = Pt(10.5)
    r.font.color.rgb = COLOR_DARK

    tbl_eval = doc.add_table(rows=7, cols=3)
    tbl_eval.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_eval.autofit = False
    tbl_eval.columns[0].width = Inches(2.2)
    tbl_eval.columns[1].width = Inches(1.1)
    tbl_eval.columns[2].width = Inches(3.2)
    set_table_borders(tbl_eval, color="CBD5E0", sz="4")

    hdr_ev = tbl_eval.rows[0]
    for c in hdr_ev.cells:
        set_cell_background(c, "003366")
    for idx, text in enumerate(["Rubro de Evaluación", "Ponderación", "Criterio de Acreditación Técnica"]):
        p = hdr_ev.cells[idx].paragraphs[0]
        style_p(p, space_before=0, space_after=0)
        r = p.add_run(text)
        r.font.name = "Calibri"
        r.font.size = Pt(9.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    eval_data = [
        ("Proyecto Práctico Módulo 1 (Láser)", "15%", "Ensamble rígido con tolerancias ≤ ±0.2 mm, juntas autoblocantes y gabinete estético."),
        ("Proyecto Práctico Módulo 2 (3D FDM)", "15%", "Garra funcional resistente al esfuerzo, insertos roscados alineados y movimiento suave."),
        ("Proyecto Práctico Módulo 3 (CNC)", "15%", "Bancada mecanizada con Código G limpio, planitud, cajeras de rodamientos a tolerancia."),
        ("Proyecto Práctico Módulo 4 (Control)", "15%", "Tablero eléctrico canalizado bajo norma IEC, ferrules, rotulado y ciclo lineal motorizado."),
        ("Proyecto Final Capstone (Módulo 5)", "25%", "Celda mecatrónica en ciclo continuo autónomo (10 ciclos sin fallas) y parada de emergencia."),
        ("Bitácora Berichtsheft y Hábitos Kinal", "15%", "Documentación semanal de taller, puntualidad, orden 5S, respeto y EPP en cada sesión.")
    ]

    for idx, (rubro, pond, crit) in enumerate(eval_data, start=1):
        row = tbl_eval.rows[idx]
        if idx % 2 == 1:
            for c in row.cells:
                set_cell_background(c, "F7FAFC")
        for c_idx, val in enumerate([rubro, pond, crit]):
            cell = row.cells[c_idx]
            set_cell_margins(cell, top=70, bottom=70, left=80, right=80)
            p = cell.paragraphs[0]
            style_p(p, space_before=0, space_after=0)
            r = p.add_run(val)
            r.font.name = "Calibri"
            r.font.size = Pt(9)
            r.font.color.rgb = COLOR_DARK
            if c_idx in [0, 1]:
                r.font.bold = True

    # Nota final al pie
    p_nota = doc.add_paragraph()
    style_p(p_nota, space_before=8, space_after=0)
    r = p_nota.add_run("Nota Aprobatoria Final: ≥ 75 / 100 puntos. Los estudiantes que alcancen dicho puntaje recibirán el Diploma de Certificación Técnica en Mecatrónica Industrial y Fabricación Digital Aplicada emitido por Fundación Kinal.")
    r.font.name = "Calibri"
    r.font.size = Pt(10)
    r.font.bold = True
    r.font.color.rgb = COLOR_PRIMARY

    # Footer
    section = doc.sections[0]
    footer = section.footer
    footer_p = footer.paragraphs[0]
    style_p(footer_p, space_before=0, space_after=0)
    footer_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run_f = footer_p.add_run("Fundación Kinal | Propuesta Formativa Oficial — Mecatrónica Industrial")
    run_f.font.name = "Calibri"
    run_f.font.size = Pt(9)
    run_f.font.color.rgb = COLOR_SECONDARY

    out_dir = os.path.join("Cursos", "Mecatrónica")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "Propuesta_Curso_Mecatronica_Kinal.docx")
    doc.save(out_path)
    print(f"Propuesta guardada con éxito en: {out_path}")

if __name__ == "__main__":
    generate_propuesta()
