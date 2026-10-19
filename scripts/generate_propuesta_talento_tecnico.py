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
        
    r = p.add_run(text)
    r.font.name = "Calibri"
    r.font.size = Pt(10)
    r.font.italic = True
    r.font.color.rgb = RGBColor(45, 55, 72)
    
    p_after = doc.add_paragraph()
    p_after.paragraph_format.space_before = Pt(0)
    p_after.paragraph_format.space_after = Pt(4)

def style_heading(p, text, level=1):
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    r.font.name = "Calibri"
    r.font.bold = True
    if level == 1:
        p.paragraph_format.space_before = Pt(16)
        p.paragraph_format.space_after = Pt(6)
        r.font.size = Pt(15)
        r.font.color.rgb = RGBColor(0, 51, 102)
    elif level == 2:
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(4)
        r.font.size = Pt(12.5)
        r.font.color.rgb = RGBColor(0, 51, 102)
    elif level == 3:
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(2)
        r.font.size = Pt(11)
        r.font.color.rgb = RGBColor(74, 85, 104)

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
    style_p(p_inst, space_before=15, space_after=2)
    r_inst = p_inst.add_run("FUNDACIÓN KINAL")
    r_inst.font.name = "Calibri"
    r_inst.font.size = Pt(14)
    r_inst.font.bold = True
    r_inst.font.color.rgb = COLOR_PRIMARY

    p_esc = doc.add_paragraph()
    style_p(p_esc, space_before=0, space_after=18)
    r_esc = p_esc.add_run("Dirección de Vinculación Empresarial — Centro de Desarrollo Gerencial y Técnico")
    r_esc.font.name = "Calibri"
    r_esc.font.size = Pt(11)
    r_esc.font.color.rgb = COLOR_SECONDARY

    p_tit = doc.add_paragraph()
    style_p(p_tit, space_before=10, space_after=8)
    r_tit = p_tit.add_run("PROPUESTA FORMATIVA INSTITUCIONAL:\nPROGRAMA EJECUTIVO DE VINCULACIÓN Y LIDERAZGO: GESTIÓN DEL TALENTO TÉCNICO Y MANDOS MEDIOS")
    r_tit.font.name = "Calibri"
    r_tit.font.size = Pt(16)
    r_tit.font.bold = True
    r_tit.font.color.rgb = COLOR_PRIMARY

    p_sub = doc.add_paragraph()
    style_p(p_sub, space_before=0, space_after=18)
    r_sub = p_sub.add_run("Capacitación Gerencial y Diálogo Estratégico para Representantes de Empresas: Manejo de Personal, Liderazgo, Factor Humano, Fortalecimiento de Competencias y Necesidades Actuales de la Industria (1 Mes de Duración | Modalidad Virtual Semanal + 2 Jornadas Presenciales Especiales)")
    r_sub.font.name = "Calibri"
    r_sub.font.size = Pt(11)
    r_sub.font.italic = True
    r_sub.font.color.rgb = COLOR_SECONDARY

    # Ficha Técnica
    tbl_ficha = doc.add_table(rows=8, cols=2)
    tbl_ficha.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_ficha.autofit = False
    tbl_ficha.columns[0].width = Inches(2.3)
    tbl_ficha.columns[1].width = Inches(4.2)
    set_table_borders(tbl_ficha, color="CBD5E0", sz="6")

    ficha_data = [
        ("Naturaleza del Programa:", "Capacitación gerencial e iniciativa de vinculación empresarial de Fundación Kinal"),
        ("Población Destinataria:", "Gerentes Generales, Gerentes de Operaciones/Planta/Mantenimiento, Directores y Gerentes de Talento Humano / RRHH, Reclutadores y Mandos Medios con equipos a su cargo"),
        ("Duración Total:", "1 mes de duración (4 semanas) | 16 horas de contacto sincrónico/presencial + 4 horas de autodiagnóstico empresarial (20 horas formativas ejecutivas totales)"),
        ("Modalidad Híbrida Ejecutiva:", "Híbrida: 1 sesión virtual semanal de 2 horas en Microsoft Teams (8h virtuales) + 2 jornadas presenciales especiales en campus Kinal (8h presenciales)"),
        ("Jornadas Presenciales Especiales:", "1) Sesión Inicial de Apertura, Presentación de la Iniciativa y Diálogo (Kinal) | 2) Jornada de Cierre, Plenaria de Necesidades Industriales y Entrega de Diplomas y Reconocimientos (Kinal)"),
        ("Los 5 Ejes Temáticos Oficiales:", "1. Manejo y desarrollo de personal | 2. Liderazgo y factor humano | 3. Fortalecimiento de competencias técnicas | 4. Desarrollo de mandos medios | 5. Necesidades actuales de la industria"),
        ("Acreditación y Reconocimiento:", "Diploma de Participación Individual y Reconocimiento Empresarial Institucional otorgado por Fundación Kinal a la empresa y a su representante (Aprobación >= 75 pts)"),
        ("Sede Presencial:", "Fundación Kinal — Auditorio Ejecutivo y Complejo de Talleres y Laboratorios de Formación Técnica, Zona 7, Ciudad de Guatemala")
    ]

    for idx, (label, val) in enumerate(ficha_data):
        row = tbl_ficha.rows[idx]
        set_cell_background(row.cells[0], "F7FAFC")
        set_cell_margins(row.cells[0], top=60, bottom=60, left=80, right=80)
        set_cell_margins(row.cells[1], top=60, bottom=60, left=80, right=80)
        
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
    # 1. MARCO INSTITUCIONAL E IDEARIO DE KINAL: LA PERSONA EN EL CENTRO
    # =========================================================================
    h1_1 = doc.add_paragraph()
    style_heading(h1_1, "1. Marco Institucional e Ideario de Fundación Kinal", level=1)

    p_id_desc = doc.add_paragraph()
    style_p(p_id_desc, space_before=0, space_after=6)
    r = p_id_desc.add_run("Fundación Kinal impulsa esta iniciativa directiva sustentada en su vocación histórica de servicio a la sociedad guatemalteca, articulando la excelencia técnica y operativa con el cultivo permanente de los valores humanos fundamentales:")
    r.font.name = "Calibri"
    r.font.size = Pt(10.5)
    r.font.color.rgb = COLOR_DARK

    add_callout(doc, "«Formar a jóvenes y adultos a través de una educación integral, con énfasis en las áreas técnicas y tecnológicas, influyendo positivamente en su trabajo, su familia y la sociedad».", bold_prefix="Misión Institucional de Kinal:")

    add_callout(doc, "«Visión cristiana de la vida. Respeto a la dignidad de la persona. Espíritu de servicio. Trabajo bien hecho. Libertad personal responsable».", bold_prefix="Valores Nucleares de Kinal:")

    p_et = doc.add_paragraph()
    style_heading(p_et, "1.1 El Factor Humano: Liderazgo y Dignidad en el Ámbito Operativo", level=2)

    p_et_txt = doc.add_paragraph()
    style_p(p_et_txt, space_before=0, space_after=6)
    r = p_et_txt.add_run("En Fundación Kinal, el **Factor Humano** es una rama de formación humana laica y universal que acompaña a todos los procesos formativos y de vinculación con la empresa. En este programa para líderes empresariales, el Factor Humano se traduce en herramientas gerenciales concretas:\n"
                          "• Respeto Irrenunciable a la Dignidad de la Persona: Desterrar en forma definitiva el maltrato verbal, el autoritarismo, el sarcasmo y los climas hostiles en cuadrillas de planta y taller. Reconocer que los operarios y mandos medios merecen un liderazgo justo, formador y empático.\n"
                          "• El Principio del «Trabajo Bien Hecho»: La calidad cotidiana entendida como estándar ético y deber profesional: orden riguroso (5S), custodia celosa de la maquinaria, veracidad absoluta en bitácoras de calidad y orgullo por el oficio bien desempeñado.\n"
                          "• Libertad Personal Responsable: Desarrollar colaboradores maduros y autónomos que actúan por convicción técnica y moral, reduciendo la necesidad de supervisión policiaca.\n"
                          "• Espíritu de Servicio y Solidaridad: La cooperación activa entre departamentos (producción, mantenimiento y calidad) para derribar silos organizacionales y construir un clima de colaboración genuina.")
    r.font.name = "Calibri"
    r.font.size = Pt(10)
    r.font.color.rgb = COLOR_DARK

    # =========================================================================
    # 2. FUNDAMENTACIÓN ESTRATÉGICA: CAPACITACIÓN GERENCIAL Y DIÁLOGO EMPRESARIAL
    # =========================================================================
    h1_2 = doc.add_paragraph()
    style_heading(h1_2, "2. Fundamentación: Capacitación para Líderes y Vinculación con la Industria", level=1)

    p_met = doc.add_paragraph()
    style_p(p_met, space_before=0, space_after=6)
    r = p_met.add_run("Este programa responde a una doble necesidad estratégica del sector empresarial y educativo guatemalteco:\n"
                      "1. Dotar a los Gerentes y Líderes de Herramientas Prácticas de Gestión Humana y Técnica: Los directivos y mandos medios enfrentan diariamente el reto de liderar cuadrillas operativas, acelerar curvas de aprendizaje, resolver conflictos de piso, evaluar competencias y reducir la rotación prematura de personal.\n"
                      "2. Conocer de Primera Mano las Necesidades Actuales de la Industria: Las tecnologías operativas (automatización, IoT industrial, robótica, redes y mantenimiento predictivo) demandan una constante actualización. Kinal abre este espacio de diálogo para escuchar a las empresas y retroalimentar la formación de sus estudiantes y egresados técnicos, fortaleciendo el vínculo escuela-empresa.")
    r.font.name = "Calibri"
    r.font.size = Pt(10)
    r.font.color.rgb = COLOR_DARK

    # =========================================================================
    # 3. LOS 5 EJES TEMÁTICOS OFICIALES DEL PROGRAMA
    # =========================================================================
    h1_3 = doc.add_paragraph()
    style_heading(h1_3, "3. Articulación de los 5 Ejes Temáticos del Programa", level=1)

    ejes = [
        ("1. Manejo y Desarrollo de Personal", 
         "Métodos directivos de atracción e inducción técnica acelerada (onboarding en 30-60-90 días). Gestión de la curva de aprendizaje en piso de planta, diseño de planes de carrera operativa y estrategias de fidelización para mitigar la rotación prematura."),
        ("2. Liderazgo y Factor Humano", 
         "La filosofía del Factor Humano de Fundación Kinal aplicada a cuadrillas: dignidad de la persona, erradicación del maltrato verbal y el autoritarismo en talleres, seguridad psicológica para el reporte de averías/incidentes y cultura del «trabajo bien hecho»."),
        ("3. Fortalecimiento de Competencias Técnicas", 
         "Mapeo y diseño de matrices de competencias operativas observables (saber, saber hacer y saber ser). Evaluación técnica práctica en el puesto de trabajo y esquemas de aprendizaje continuo y formación dual escuela-empresa."),
        ("4. Desarrollo de Mandos Medios", 
         "Herramientas formativas para supervisores de primera línea, jefes de taller y jefes de turno: comunicación asertiva, retroalimentación constructiva, resolución de conflictos de equipo, liderazgo pedagógico (*Ausbilder*) y 'Charlas de 10 minutos de Factor Humano'."),
        ("5. Necesidades Actuales de la Industria (Eje de Diálogo)", 
         "Espacio formal y estructurado de diálogo bidireccional en las dos jornadas presenciales especiales, donde las empresas comparten sus requerimientos tecnológicos, brechas operativas y destrezas demandadas para retroalimentar los planes formativos de Kinal.")
    ]

    for e_tit, e_desc in ejes:
        p_e = doc.add_paragraph()
        style_p(p_e, space_before=2, space_after=4)
        p_e.paragraph_format.left_indent = Inches(0.2)
        r_b = p_e.add_run(f"• {e_tit}: ")
        r_b.font.name = "Calibri"
        r_b.font.size = Pt(9.5)
        r_b.font.bold = True
        r_b.font.color.rgb = COLOR_PRIMARY
        r_d = p_e.add_run(e_desc)
        r_d.font.name = "Calibri"
        r_d.font.size = Pt(9.5)
        r_d.font.color.rgb = COLOR_DARK

    # =========================================================================
    # 4. COMPETENCIA GENERAL Y PERFILES DEL PARTICIPANTE
    # =========================================================================
    h1_4 = doc.add_paragraph()
    style_heading(h1_4, "4. Competencia General y Perfil de los Participantes", level=1)

    p_comp = doc.add_paragraph()
    style_p(p_comp, space_before=0, space_after=6)
    r = p_comp.add_run("Competencia General del Programa:\n"
                       "El participante aplica herramientas gerenciales contemporáneas para el manejo, desarrollo y liderazgo de personal operativo y mandos medios, integrando la cultura del Factor Humano y el estándar del «trabajo bien hecho» en sus cuadrillas, y participa activamente en el diálogo de vinculación industria-academia para identificar y alinear las competencias técnicas y humanas requeridas por el sector productivo.")
    r.font.name = "Calibri"
    r.font.size = Pt(10)
    r.font.bold = True
    r.font.color.rgb = COLOR_PRIMARY

    p_perfiles = doc.add_paragraph()
    style_p(p_perfiles, space_before=4, space_after=6)
    r = p_perfiles.add_run("• Perfil de Ingreso: Gerentes Generales, Gerentes de Operaciones, Planta o Mantenimiento, Directores/Gerentes de Talento Humano y Recursos Humanos, Jefes de Reclutamiento y Supervisores Generales con responsabilidad sobre equipos técnicos en sectores como manufactura, agroindustria, alimentos, plásticos, telecomunicaciones, energía y servicios técnicos.\n"
                            "• Perfil de Egreso: Líder empresarial capacitado en metodologías de supervisión formativa, con visión estratégica del talento operativo, capaz de erradicar el maltrato en sus áreas de trabajo, fortalecer las competencias técnicas de su personal y colaborar activamente con Fundación Kinal en iniciativas de empleabilidad y formación técnica.")
    r.font.name = "Calibri"
    r.font.size = Pt(10)
    r.font.color.rgb = COLOR_DARK

    # =========================================================================
    # 5. ESTRUCTURA FORMATIVA Y CALENDARIO OFICIAL (1 MES)
    # =========================================================================
    h1_5 = doc.add_paragraph()
    style_heading(h1_5, "5. Estructura Formativa Oficial (1 Mes de Duración | Híbrido Ejecutivo)", level=1)

    p_est_desc = doc.add_paragraph()
    style_p(p_est_desc, space_before=0, space_after=6)
    r = p_est_desc.add_run("El programa articula **1 sesión semanal virtual** a lo largo de un mes con **2 jornadas presenciales especiales** en las instalaciones de Fundación Kinal, garantizando un formato ágil y de alto impacto para los ejecutivos:")
    r.font.name = "Calibri"
    r.font.size = Pt(10)
    r.font.color.rgb = COLOR_DARK

    modulos_data = [
        ("Jornada Especial 1 (Presencial)", "Apertura Institucional, Presentación de la Iniciativa y Mesa de Diálogo 1: Necesidades de la Industria", "4 Horas", "Presencial en Campus Kinal (8:30 a 12:30 hrs)", "Ficha Diagnóstica Inicial de Necesidades y Expectativas"),
        ("Semana 1 / Sesión Virtual 1", "Manejo y Desarrollo de Personal Técnico: Atracción, Inducción Acelerada y Retención", "2 Horas", "Virtual Sincrónico (Microsoft Teams)", "Descriptor de Puesto por Competencias y Plan de Inducción"),
        ("Semana 2 / Sesión Virtual 2", "Liderazgo y Factor Humano: Dignidad en el Trabajo, Trabajo Bien Hecho y Erradicación del Maltrato", "2 Horas", "Virtual Sincrónico (Microsoft Teams)", "Código de Convivencia Operativa y Protocolo Cero Maltrato"),
        ("Semana 3 / Sesión Virtual 3", "Fortalecimiento de Competencias Técnicas: Mapeo de Destrezas, Evaluación y Aprendizaje Continuo", "2 Horas", "Virtual Sincrónico (Microsoft Teams)", "Matriz de Competencias Operativas y Plan de Capacitación en Piso"),
        ("Semana 4 / Sesión Virtual 4", "Desarrollo de Mandos Medios: Herramientas para Supervisores, Feedback Asertivo y Micro-Charlas", "2 Horas", "Virtual Sincrónico (Microsoft Teams)", "Catálogo de 5 Micro-Charlas de Factor Humano para el Turno"),
        ("Jornada Especial 2 (Presencial)", "Mesa Redonda Plenaria: Sistematización de Demandas Industriales, Entrega de Diplomas y Reconocimientos", "4 Horas", "Presencial en Campus Kinal (8:30 a 12:30 hrs)", "Diplomas Oficiales Entregados y Acuerdos de Vinculación")
    ]

    tbl_mod = doc.add_table(rows=7, cols=5)
    tbl_mod.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_mod.autofit = False
    tbl_mod.columns[0].width = Inches(1.3)
    tbl_mod.columns[1].width = Inches(2.2)
    tbl_mod.columns[2].width = Inches(0.7)
    tbl_mod.columns[3].width = Inches(1.1)
    tbl_mod.columns[4].width = Inches(1.2)
    set_table_borders(tbl_mod, color="CBD5E0", sz="4")

    hdr_mod = tbl_mod.rows[0]
    for c in hdr_mod.cells:
        set_cell_background(c, "003366")
    headers_mod_txt = ["Encuentro / Modalidad", "Eje Temático / Actividad", "Horas", "Formato / Plataforma", "Producto Observable"]
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
        if "Presencial" in m_id or "Jornada" in m_id:
            for c in row.cells:
                set_cell_background(c, "EBF8FF")
        elif idx % 2 == 1:
            for c in row.cells:
                set_cell_background(c, "F7FAFC")
        for c_idx, val in enumerate([m_id, m_nom, m_hrs, m_ses, m_prod]):
            cell = row.cells[c_idx]
            set_cell_margins(cell, top=50, bottom=50, left=60, right=60)
            p = cell.paragraphs[0]
            style_p(p, space_before=0, space_after=0)
            r = p.add_run(val)
            r.font.name = "Calibri"
            r.font.size = Pt(8.5)
            r.font.color.rgb = COLOR_DARK
            if c_idx in [0, 2] or "Presencial" in m_id:
                r.font.bold = True

    p_balance = doc.add_paragraph()
    style_p(p_balance, space_before=8, space_after=6)
    r = p_balance.add_run("Balance Formativo:\n"
                          "• 8 Horas Presenciales Vivenciales (2 Jornadas Especiales en Kinal): Apertura institucional, recorrido guiado de talleres, networking y 2 mesas de diálogo sobre necesidades de la industria, culminando con la entrega protocolaria de diplomas y reconocimientos.\n"
                          "• 8 Horas Virtuales Sincrónicas en Microsoft Teams: 4 sesiones semanales de 2 horas (1 sesión por semana) dedicadas a herramientas gerenciales en manejo de personal, liderazgo humanista, competencias operativas y mandos medios.\n"
                          "• 4 Horas de Autodiagnóstico en Kinal.academy (Moodle): Ficha diagnóstica de necesidades de cualificación y plan de mejora operativa para su equipo.\n"
                          "• Total: 20 Horas Formativas Ejecutivas.")
    r.font.name = "Calibri"
    r.font.size = Pt(9.5)
    r.font.color.rgb = COLOR_DARK

    # =========================================================================
    # 6. ESTRATEGIA ANDRAGÓGICA Y ESPACIOS DE DIÁLOGO
    # =========================================================================
    h1_6 = doc.add_paragraph()
    style_heading(h1_6, "6. Metodología Andragógica de Formación Gerencial", level=1)

    p_metod = doc.add_paragraph()
    style_p(p_metod, space_before=0, space_after=6)
    r = p_metod.add_run("El programa emplea un enfoque andragógico participativo adaptado a directivos y líderes de talento:\n"
                        "1. Estudio de Casos Gerenciales: Análisis de situaciones críticas de piso de planta (resistencia al cambio, conflictos entre áreas de mantenimiento y producción, supervisores autoritarios, curvas lentas de onboarding).\n"
                        "2. Mesas de Diálogo Industria-Kinal: Espacios formales donde la gerencia retroalimenta a la academia sobre los perfiles técnicos requeridos en el mercado.\n"
                        "3. Caja de Herramientas de Gestión: Plantillas editables de descriptores por competencias, protocolos contra el maltrato y formatos de micro-charlas de valores listas para aplicar en la empresa.")
    r.font.name = "Calibri"
    r.font.size = Pt(10)
    r.font.color.rgb = COLOR_DARK

    # =========================================================================
    # 7. ACREDITACIÓN, DIPLOMAS Y RECONOCIMIENTOS EMPRESARIALES
    # =========================================================================
    h1_7 = doc.add_paragraph()
    style_heading(h1_7, "7. Acreditación Institucional, Diplomas y Reconocimientos", level=1)

    p_acred = doc.add_paragraph()
    style_p(p_acred, space_before=0, space_after=6)
    r = p_acred.add_run("En la Jornada Presencial de Cierre en campus Kinal se realizará un acto protocolario especial con dos distinciones oficiales:\n"
                        "1. Diploma de Participación Individual: Otorgado al representante empresarial que cumplió con el 80% de asistencia a las sesiones sincrónicas y la entrega de sus productos aplicativos (con nota mínima aprobatoria institucional de 75/100 puntos).\n"
                        "2. Reconocimiento Empresarial Institucional: Galardón emitido por Fundación Kinal a la empresa participante, acreditándola como «Empresa Aliada en la Vinculación Técnica y Formación del Talento Humano», con acceso prioritario a la Bolsa de Egresados y convenios formativos.")
    r.font.name = "Calibri"
    r.font.size = Pt(10)
    r.font.color.rgb = COLOR_DARK

    # =========================================================================
    # 8. PLATAFORMAS TECNOLÓGICAS E INFRAESTRUCTURA
    # =========================================================================
    h1_8 = doc.add_paragraph()
    style_heading(h1_8, "8. Ecosistema Digital e Infraestructura Institucional", level=1)

    p_infra = doc.add_paragraph()
    style_p(p_infra, space_before=0, space_after=6)
    r = p_infra.add_run("En cumplimiento de los estándares institucionales de Fundación Kinal:\n"
                        "• Plataforma Virtual Sincrónica: Microsoft Teams para las 4 sesiones semanales interactivas, con salas de trabajo grupal y grabación de respaldo.\n"
                        "• Plataforma LMS Oficial: Kinal.academy (Moodle) para la gestión del material de lectura, instrumentos de autodiagnóstico y levantamiento de necesidades de la industria.\n"
                        "• Instalaciones Presenciales en Kinal: Auditorio Ejecutivo climatizado con soporte audiovisual, salas de networking directivo y recorrido guiado por talleres y laboratorios de formación técnica.")
    r.font.name = "Calibri"
    r.font.size = Pt(9.5)
    r.font.color.rgb = COLOR_DARK

    section = doc.sections[0]
    footer = section.footer
    footer_p = footer.paragraphs[0]
    style_p(footer_p, space_before=0, space_after=0)
    footer_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run_f = footer_p.add_run("Fundación Kinal | Programa Ejecutivo de Vinculación y Liderazgo — Propuesta Oficial")
    run_f.font.name = "Calibri"
    run_f.font.size = Pt(8.5)
    run_f.font.color.rgb = COLOR_SECONDARY

    # Guardar en ambas ubicaciones para total consistencia
    for out_dir in [os.path.join("Cursos", "Talento_Tecnico"), "Talento_Tecnico"]:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "Propuesta_Diplomado_Talento_Tecnico_Kinal.docx")
        doc.save(out_path)
        print(f"Propuesta guardada con éxito en: {out_path}")

if __name__ == "__main__":
    generate_propuesta_doc()
