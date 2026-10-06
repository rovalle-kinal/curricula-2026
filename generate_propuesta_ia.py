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
    r_tit = p_tit.add_run("PLANIFICACIÓN Y PROPUESTA FORMATIVA INSTITUCIONAL:\nINTELIGENCIA ARTIFICIAL APLICADA, INGENIERÍA DE PROMPTS Y PRODUCTIVIDAD ÉTICA")
    r_tit.font.name = "Calibri"
    r_tit.font.size = Pt(18)
    r_tit.font.bold = True
    r_tit.font.color.rgb = COLOR_PRIMARY

    p_sub = doc.add_paragraph()
    style_p(p_sub, space_before=0, space_after=20)
    r_sub = p_sub.add_run("Programa Práctico Introductorio para Potenciar Capacidades Humanas y Eficiencia Laboral mediante IA Generativa (16 Horas — 8 Sesiones Nocturnas)")
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
        ("Nivel Formativo de Referencia:", "Equivalencia DQR Nivel 3 - 4 (Habilitación operativa, autonomía de criterio y aplicación práctica)"),
        ("Población Destinataria:", "Jóvenes y adultos sin formación especializada interesados en potenciar su productividad personal y laboral"),
        ("Duración Total:", "16 horas pedagógicas (1 mes calendario: 8 sesiones de 2 horas / 120 min; 15h de actividad neta)"),
        ("Modalidad y Formato:", "Virtual Sincrónica Interactiva (Microsoft Teams + Plataforma Kinal.academy / Moodle)"),
        ("Estructura de Horarios:", "Dos noches entre semana (Martes y Jueves de 19:00 a 21:00 hrs), adaptado al público activo"),
        ("Eje Metodológico Central:", "Ingeniería de prompts estructurada, aplicaciones reales en oficina/negocio y uso ético centrado en la persona"),
        ("Nota Mínima Aprobatoria:", "75 puntos sobre 100 en actividades aplicadas, verificación crítica y proyecto integrador"),
        ("Sede / Plataforma:", "Fundación Kinal — Aulas Virtuales Microsoft Teams y Portal Kinal.academy")
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
    # 1. MARCO FILOSÓFICO E IDEARIO DE KINAL: ÉTICA Y EL LADO HUMANO DE LA IA
    # =========================================================================
    h1_1 = doc.add_paragraph()
    style_heading(h1_1, "1. Marco Filosófico e Ideario Institucional de Fundación Kinal", level=1)

    p_id_desc = doc.add_paragraph()
    style_p(p_id_desc, space_before=0, space_after=6)
    r = p_id_desc.add_run("El diseño formativo de este curso parte de una convicción humanística fundamental: la tecnología adquiere su verdadero valor cuando se pone al servicio de la persona, enriqueciendo su trabajo y dignificando su vida:")
    r.font.name = "Calibri"
    r.font.size = Pt(10.5)
    r.font.color.rgb = COLOR_DARK

    add_callout(doc, "«Formar a jóvenes y adultos a través de una educación integral, con énfasis en las áreas técnicas y tecnológicas, influyendo positivamente en su trabajo, su familia y la sociedad».", bold_prefix="Misión Institucional de Kinal:")

    add_callout(doc, "«Visión cristiana de la vida. Respeto a la dignidad de la persona. Espíritu de servicio. Trabajo bien hecho. Libertad personal responsable».", bold_prefix="Valores Nucleares de Kinal:")

    p_et = doc.add_paragraph()
    style_heading(p_et, "1.1 El Enfoque Positivo: Potenciar Capacidades sin Perder el Lado Humano", level=2)

    p_et_txt = doc.add_paragraph()
    style_p(p_et_txt, space_before=0, space_after=6)
    r = p_et_txt.add_run("Este programa no se plantea desde la ansiedad tecnológica ni desde una visión de confrontación con la máquina, sino desde una perspectiva de oportunidad constructiva y elevación del talento humano:\n"
                          "• La IA como Copiloto que Multiplica Capacidades: La inteligencia artificial no sustituye el discernimiento, la empatía ni la creatividad humana; actúa como un multiplicador de productividad que asume las tareas mecánicas y repetitivas (redactar borradores, ordenar listas, resumir textos), liberando tiempo para lo esencialmente humano: la toma de decisiones, la calidez en el trato y el servicio a los demás.\n"
                          "• El Principio del «Trabajo Bien Hecho» Aplicado a la IA: En la era de la generación automática de contenidos, la excelencia no radica en la cantidad de texto generado, sino en la veracidad, pulcritud, personalización y criterio con que se evalúa y perfecciona el resultado. Entregar un texto sin revisar, con alucinaciones o datos falsos, es contrario al ideario de Kinal. El participante aprende a ser el director crítico de la herramienta.\n"
                          "• Honestidad Profesional y Verdad: Promover el uso transparente de la IA como instrumento de apoyo, fomentando la autoría responsable y el respeto a los derechos ajenos y a la privacidad de los datos personales y empresariales.")
    r.font.name = "Calibri"
    r.font.size = Pt(10)
    r.font.color.rgb = COLOR_DARK

    # =========================================================================
    # 2. FUNDAMENTACIÓN PEDAGÓGICA Y ENFOQUE PRÁCTICO
    # =========================================================================
    h1_2 = doc.add_paragraph()
    style_heading(h1_2, "2. Fundamentación Técnica y Enfoque Didáctico del Programa", level=1)

    p_met = doc.add_paragraph()
    style_p(p_met, space_before=0, space_after=6)
    r = p_met.add_run("El curso está diseñado para garantizar una experiencia formativa ágil, motivadora y libre de barreras técnicas artificiales:\n"
                      "• Cero Tecnicismos Innecesarios: No se abordan fórmulas matemáticas, algoritmos abstractos ni líneas de código de programación. El aprendizaje se centra 100% en el lenguaje natural (español claro y cotidiano) como interfaz universal para comunicarse eficazmente con los modelos de lenguaje.\n"
                      "• Metodología «Aprender Haciendo» (Learning by Doing): Cada sesión de 2 horas sigue un ciclo dinámico: 20 minutos de demostración del instructor, 70 minutos de práctica guiada interactiva en vivo por parte de los estudiantes (usando sus computadoras o teléfonos inteligentes) y 30 minutos de puesta en común, análisis de resultados y refinamiento.\n"
                      "• Ecosistema Accesible y Gratuito: Las actividades se desarrollan exclusivamente sobre herramientas de libre acceso (Google Gemini, ChatGPT con GPT-4o mini, Microsoft Copilot y Claude), garantizando que ningún participante enfrente barreras de pago o suscripción para aplicar lo aprendido desde el primer día.")
    r.font.name = "Calibri"
    r.font.size = Pt(10)
    r.font.color.rgb = COLOR_DARK

    # =========================================================================
    # 3. MARCO DQR Y SISTEMA DE CUALIFICACIÓN
    # =========================================================================
    h1_3 = doc.add_paragraph()
    style_heading(h1_3, "3. Marco Alemán de Cualificaciones (DQR Nivel 3 - 4) y Competencia Integral", level=1)

    add_callout(doc, "«concepto de aprendizaje para jóvenes que tiene como objetivo preparar a los aprendices para su vida profesional, por lo que la formación se realiza en régimen de alternancia entre la escuela o el centro de formación y la empresa. El aprender en el proceso del trabajo es base y a la vez objetivo de la acción formativa».", bold_prefix="Definición de Formación Profesional Dual:")

    add_callout(doc, "«the ability and readiness of the individual to use knowledge, skills and personal, social and methodological competences and to behave in a considered, individual and socially responsible manner. Competence is understood in this sense as the comprehensive ability to act».", bold_prefix="Concepto de Competencia en el DQR:")

    p_dqr_txt = doc.add_paragraph()
    style_p(p_dqr_txt, space_before=0, space_after=6)
    r = p_dqr_txt.add_run("El programa desarrolla de manera equilibrada las dimensiones de competencia del DQR:\n"
                          "1. Dimensión de Competencia Profesional (Professional Competence):\n"
                          "   • Conocimientos (Knowledge): Comprensión operativa de cómo procesan información los modelos generativos, sus capacidades reales, alcances y limitaciones naturales (probabilidad estadística, ventanas de contexto, riesgo de alucinación).\n"
                          "   • Destrezas (Skills): Habilidad práctica para diseñar prompts estructurados (método RC-TRF: Rol, Contexto, Tarea, Restricción, Formato), anclaje a documentos propios, refinamiento iterativo y extracción estructurada de datos.\n"
                          "2. Dimensión de Competencia Personal (Personal Competence):\n"
                          "   • Competencia Social (Social Competence): Comunicación asertiva mediada por IA, empatía en la redacción corporativa y colaboración efectiva.\n"
                          "   • Autonomía y Juicio Crítico (Autonomy): Capacidad autónoma para discernir entre respuestas confiables y alucinaciones, preservación ética de la privacidad de la información y toma de decisiones independiente.")
    r.font.name = "Calibri"
    r.font.size = Pt(10)
    r.font.color.rgb = COLOR_DARK

    # =========================================================================
    # 4. COMPETENCIA GENERAL Y PERFILES DEL PARTICIPANTE
    # =========================================================================
    h1_4 = doc.add_paragraph()
    style_heading(h1_4, "4. Competencia General y Perfiles del Participante", level=1)

    p_comp = doc.add_paragraph()
    style_p(p_comp, space_before=0, space_after=6)
    r = p_comp.add_run("Competencia General del Programa:\n"
                       "El egresado interactúa de manera autónoma, fluida y crítica con herramientas de inteligencia artificial generativa, formulando prompts estructurados y profesionales para optimizar tareas de comunicación, análisis de información y productividad cotidiana, aplicando estrictos criterios éticos de privacidad, veracidad y el principio del «trabajo bien hecho» de Fundación Kinal, preservando en todo momento el valor insustituible del criterio humano.")
    r.font.name = "Calibri"
    r.font.size = Pt(10)
    r.font.bold = True
    r.font.color.rgb = COLOR_PRIMARY

    p_perfiles = doc.add_paragraph()
    style_p(p_perfiles, space_before=4, space_after=6)
    r = p_perfiles.add_run("• Perfil de Ingreso: Jóvenes y adultos sin formación especializada en tecnología (asistentes administrativos, recepcionistas, comerciantes, emprendedores, docentes, bachilleres y público en general) que desean descubrir y aprovechar los beneficios de la inteligencia artificial para hacer más eficiente su labor diaria. Requiere manejo elemental de computadora o teléfono inteligente con acceso a internet y lectura comprensiva.\n"
                           "• Perfil de Egreso y Empleabilidad: Usuario productivo y ético de IA capaz de redactar correspondencia profesional en minutos, sintetizar informes densos en tablas ejecutivas, formular consultas de alto impacto mediante ingeniería de prompts y auditar con pensamiento crítico los resultados generados, elevando su competitividad laboral.")
    r.font.name = "Calibri"
    r.font.size = Pt(10)
    r.font.color.rgb = COLOR_DARK

    # =========================================================================
    # 5. ESTRUCTURA MODULAR Y DOSIFICACIÓN DE LA CARGA HORARIA (16 HORAS)
    # =========================================================================
    h1_5 = doc.add_paragraph()
    style_heading(h1_5, "5. Estructura Modular y Cronograma Semanal (16 Horas — 8 Sesiones)", level=1)

    modulos_data = [
        ("Módulo 1", "Descubriendo la IA: Fundamentos y Primeros Pasos Prácticos", "4 Horas", "2 Sesiones", "Configuración de Entorno Multimodelo y Primeros Diálogos Efectivos"),
        ("Módulo 2", "Ingeniería de Prompts: El Arte de Instruir con Precisión (Método RC-TRF)", "4 Horas", "2 Sesiones", "Catálogo de Prompts Estructurados con Ejemplos (Few-Shot)"),
        ("Módulo 3", "Casos Reales en la Oficina, Negocio y Vida Profesional", "4 Horas", "2 Sesiones", "Automatización de Correos, Minutas y Síntesis de Documentos Extensos"),
        ("Módulo 4", "Ética, Privacidad, Caza de Alucinaciones y Proyecto Integrador", "4 Horas", "2 Sesiones", "Asistente Personal de Productividad y Dossier de Prompts Evaluado")
    ]

    tbl_mod = doc.add_table(rows=5, cols=5)
    tbl_mod.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_mod.autofit = False
    tbl_mod.columns[0].width = Inches(1.0)
    tbl_mod.columns[1].width = Inches(2.3)
    tbl_mod.columns[2].width = Inches(0.8)
    tbl_mod.columns[3].width = Inches(0.8)
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
    r = p_balance.add_run("Organización del Tiempo y Formato Nocturno:\n"
                          "• Duración del Ciclo: 1 mes calendario distribuido en 4 semanas.\n"
                          "• Carga Semanal: 4 horas por semana divididas en 2 sesiones nocturnas de 2 horas (120 min por sesión: Martes y Jueves de 19:00 a 21:00 hrs).\n"
                          "• Dinámica de Sesión: 100% interactiva, con participación activa constante y ejercicios prácticos resueltos en tiempo real durante la clase.")
    r.font.name = "Calibri"
    r.font.size = Pt(9.5)
    r.font.color.rgb = COLOR_DARK

    # =========================================================================
    # 6. SISTEMA DE EVALUACIÓN INSTITUCIONAL Y UMBRAL APROBATORIO
    # =========================================================================
    h1_6 = doc.add_paragraph()
    style_heading(h1_6, "6. Sistema de Evaluación Institucional y Criterio de Acreditación", level=1)

    add_callout(doc, "La acreditación del curso y la obtención de la constancia oficial de Fundación Kinal requieren una calificación mínima de 75 puntos sobre 100, evaluada a través de la resolución práctica de casos y la entrega del proyecto integrador, demostrando el principio del «trabajo bien hecho».", bold_prefix="Umbral Aprobatorio Institucional Obligatorio:")

    eval_data = [
        ("Talleres Prácticos y Retos Semanales de Aplicación (40%)", "Resolución de casos en vivo en cada sesión: redacción de correos, síntesis de textos y diseño de tablas con prompts estructurados."),
        ("Pensamiento Crítico y Detección de Alucinaciones (20%)", "Auditoría de textos generados por IA, identificación de datos inexactos y aplicación de técnicas de verificación y anclaje a fuentes fiables."),
        ("Bitácora de Prompts y Reflexión Ética (15%)", "Compilación de lecciones aprendidas, registro de plantillas de prompts depuradas y aplicación de normas de privacidad y confidencialidad."),
        ("Proyecto Integrador: Asistente Personal de Productividad (25%)", "Construcción y sustentación de un sistema de prompts maestros personalizados para la ocupación real del estudiante, con rúbrica institucional.")
    ]

    tbl_ev = doc.add_table(rows=5, cols=2)
    tbl_ev.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_ev.autofit = False
    tbl_ev.columns[0].width = Inches(2.6)
    tbl_ev.columns[1].width = Inches(3.9)
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
    # 7. INFRAESTRUCTURA DIGITAL Y HERRAMIENTAS
    # =========================================================================
    h1_7 = doc.add_paragraph()
    style_heading(h1_7, "7. Infraestructura Digital y Plataformas de Trabajo", level=1)

    p_infra = doc.add_paragraph()
    style_p(p_infra, space_before=0, space_after=6)
    r = p_infra.add_run("Para asegurar la máxima accesibilidad y equidad de aprendizaje:\n"
                        "• Plataforma Educativa Oficial: Portal Kinal.academy (Moodle) para entrega de plantillas de prompts, materiales de apoyo, grabaciones y tareas.\n"
                        "• Aula Virtual Sincrónica: Microsoft Teams institucional con canales de práctica interactiva y salas de trabajo colaborativo.\n"
                        "• Modelos de IA Utilizados: Google Gemini, ChatGPT (OpenAI - GPT-4o mini), Microsoft Copilot y Claude (Anthropic), accesibles desde cualquier navegador web o aplicación móvil gratuita.\n"
                        "• Requisitos para el Participante: Computadora de escritorio, portátil o tableta/teléfono inteligente con conexión estable a internet (mínimo 5 Mbps) y cuenta personal de correo electrónico.")
    r.font.name = "Calibri"
    r.font.size = Pt(9.5)
    r.font.color.rgb = COLOR_DARK

    section = doc.sections[0]
    footer = section.footer
    footer_p = footer.paragraphs[0]
    style_p(footer_p, space_before=0, space_after=0)
    footer_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run_f = footer_p.add_run("Fundación Kinal | Inteligencia Artificial Aplicada y Productividad Ética — Propuesta Oficial")
    run_f.font.name = "Calibri"
    run_f.font.size = Pt(8.5)
    run_f.font.color.rgb = COLOR_SECONDARY

    out_dir = os.path.join("Cursos", "Inteligencia_Artificial")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "Propuesta_Curso_IA_Kinal.docx")
    doc.save(out_path)
    print(f"Propuesta guardada con éxito en: {out_path}")

if __name__ == "__main__":
    generate_propuesta_doc()
