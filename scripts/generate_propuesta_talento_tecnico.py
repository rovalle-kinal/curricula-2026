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
    r_esc = p_esc.add_run("Escuela Técnica Superior — Centro de Desarrollo Empresarial y Formación Continua")
    r_esc.font.name = "Calibri"
    r_esc.font.size = Pt(11)
    r_esc.font.color.rgb = COLOR_SECONDARY

    p_tit = doc.add_paragraph()
    style_p(p_tit, space_before=14, space_after=10)
    r_tit = p_tit.add_run("PLANIFICACIÓN Y PROPUESTA FORMATIVA INSTITUCIONAL:\nDIPLOMADO DE CERTIFICACIÓN GERENCIAL EN GESTIÓN ESTRATÉGICA DEL TALENTO TÉCNICO")
    r_tit.font.name = "Calibri"
    r_tit.font.size = Pt(17)
    r_tit.font.bold = True
    r_tit.font.color.rgb = COLOR_PRIMARY

    p_sub = doc.add_paragraph()
    style_p(p_sub, space_before=0, space_after=20)
    r_sub = p_sub.add_run("Programa Ejecutivo Híbrido para la Alta Dirección y Líderes de Talento: Capitalizando el Valor del Técnico Superior Universitario (TSU), la Formación Dual y la Cultura del Factor Humano (4 Semanas Intensivas Consecutivas)")
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
        ("Nivel Formativo de Referencia:", "Equivalencia DQR Nivel 6 - 7 (Dirección estratégica de talento, diseño organizacional y liderazgo)"),
        ("Población Destinataria:", "Gerentes Generales, Gerentes de Talento Humano / RRHH, Reclutadores y Gerentes de Operaciones/Planta"),
        ("Duración Total:", "32 horas directas sincrónicas/presenciales (40 horas formativas totales en 4 semanas consecutivas intensivas)"),
        ("Modalidad Híbrida Ejecutiva:", "Híbrido: 16h Virtual Sincrónico (Microsoft Teams) + 16h Presencial (4 Sábados consecutivos en Kinal) + Kinal.academy"),
        ("Estructura de Horarios:", "Martes y Jueves (19:00 a 21:00 hrs en Teams) y 4 Sábados consecutivos (8:00 a 12:00 hrs en campus Kinal)"),
        ("Ejes Estratégicos del Programa:", "Valor del TSU en la industria, reclutamiento por competencias, modelos de formación dual y Factor Humano"),
        ("Nota Mínima Aprobatoria:", "75 puntos sobre 100 en análisis de casos, auditoría de competencias y Proyecto Directivo Capstone"),
        ("Sede Presencial:", "Fundación Kinal — Auditorio Ejecutivo y Complejo de Talleres y Laboratorios TSU, Zona 7, Ciudad de Guatemala")
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
    # 1. MARCO FILOSÓFICO E IDEARIO DE KINAL: LA PERSONA EN EL CENTRO
    # =========================================================================
    h1_1 = doc.add_paragraph()
    style_heading(h1_1, "1. Marco Filosófico e Ideario Institucional de Fundación Kinal", level=1)

    p_id_desc = doc.add_paragraph()
    style_p(p_id_desc, space_before=0, space_after=6)
    r = p_id_desc.add_run("Este diplomado gerencial se sustenta en la visión humanística del trabajo de Fundación Kinal, la cual postula que la rentabilidad y la eficiencia operativa de una organización son fruto directo de la dignidad, la formación integral y el cuidado de las personas que la integran:")
    r.font.name = "Calibri"
    r.font.size = Pt(10.5)
    r.font.color.rgb = COLOR_DARK

    add_callout(doc, "«Formar a jóvenes y adultos a través de una educación integral, con énfasis en las áreas técnicas y tecnológicas, influyendo positivamente en su trabajo, su familia y la sociedad».", bold_prefix="Misión Institucional de Kinal:")

    add_callout(doc, "«Visión cristiana de la vida. Respeto a la dignidad de la persona. Espíritu de servicio. Trabajo bien hecho. Libertad personal responsable».", bold_prefix="Valores Nucleares de Kinal:")

    p_et = doc.add_paragraph()
    style_heading(p_et, "1.1 El Factor Humano: La Rama Formativa que Transforma la Cultura Productiva", level=2)

    p_et_txt = doc.add_paragraph()
    style_p(p_et_txt, space_before=0, space_after=6)
    r = p_et_txt.add_run("En la tradición formativa de Kinal, el **Factor Humano** no es un módulo accesorio ni una charla motivacional pasajera; es la columna vertebral que acompaña a cada técnico y profesional a lo largo de toda su trayectoria. En este diplomado, los líderes empresariales descubren cómo trasladar esta filosofía a sus propias organizaciones a través de valores laicos pero profundamente humanos:\n"
                          "• Respeto Irrenunciable a la Dignidad de la Persona: Desterrar de manera definitiva el maltrato verbal, el autoritarismo, el sarcasmo y los climas hostiles en cuadrillas de planta y taller. Reconocer que el operario técnico merece un liderazgo justo, formador y empático.\n"
                          "• El Principio del «Trabajo Bien Hecho»: La excelencia técnica cotidiana entendida como deber moral y profesional: orden estricto (5S), custodia impecable de la maquinaria, veracidad absoluta en registros de calidad y orgullo por la obra bien terminada.\n"
                          "• Libertad Personal Responsable y Autonomía: Fomentar colaboradores maduros que actúan por convicción y profesionalismo, sin requerir supervisores policíacos detrás de ellos.\n"
                          "• Espíritu de Servicio y Solidaridad: La cooperación interdepartamental genuina para derribar los silos entre operaciones, mantenimiento, recursos humanos y dirección general.")
    r.font.name = "Calibri"
    r.font.size = Pt(10)
    r.font.color.rgb = COLOR_DARK

    # =========================================================================
    # 2. FUNDAMENTACIÓN TÉCNICA: EL DILEMA DEL TALENTO Y EL VALOR DEL TSU
    # =========================================================================
    h1_2 = doc.add_paragraph()
    style_heading(h1_2, "2. Fundamentación Estratégica: El Retorno de Inversión del TSU", level=1)

    p_met = doc.add_paragraph()
    style_p(p_met, space_before=0, space_after=6)
    r = p_met.add_run("La industria guatemalteca sufre una paradoja crónica en su gestión operativa: gasta sumas millonarias en maquinaria de última generación (Industria 4.0, PLCs, redes, robótica), pero tropieza sistemáticamente al seleccionar al personal que debe operarla y mantenerla:\n"
                      "• El Error de la Subcualificación: Asignar líneas automatizadas a personal con formación básica empírica o bachilleres sin especialización técnica superior. El resultado es mantenimiento reactivo destructivo, paradas de planta no programadas y mermas intolerables por falta de método analítico de diagnóstico.\n"
                      "• El Error de la Sobrecualificación: Contratar ingenieros universitarios recién graduados para puestos de supervisión de línea o mantenimiento directo. El resultado es frustración inmediata: el ingeniero busca diseño o gestión de oficina, rechaza el trabajo de campo en el taller, percibe el puesto como transitorio y renuncia a los 6 u 8 meses, disparando los costos de rotación.\n"
                      "• La Solución Estratégica: El Técnico Superior Universitario (TSU): El grado TSU de Kinal (3 años de educación técnica superior y universitaria, con más de 1,500 horas de prácticas de banco, laboratorios y plantas piloto) representa el 'eslabón perdido' de la productividad nacional. Equivale exactamente al *Meister* (Maestro Técnico) o *Techniker* del sistema alemán (DQR Niveles 5-6): domina la física y el cálculo aplicado, resuelve averías complejas en campo y posee la formación humana para liderar cuadrillas operativas con estabilidad a largo plazo.")
    r.font.name = "Calibri"
    r.font.size = Pt(10)
    r.font.color.rgb = COLOR_DARK

    # =========================================================================
    # 3. MARCO ALEMÁN DQR Y SISTEMA DUAL DE APRENDIZAJE
    # =========================================================================
    h1_3 = doc.add_paragraph()
    style_heading(h1_3, "3. Marco Alemán de Cualificaciones (DQR) y Formación Dual en la Empresa", level=1)

    add_callout(doc, "«concepto de aprendizaje para jóvenes que tiene como objetivo preparar a los aprendices para su vida profesional, por lo que la formación se realiza en régimen de alternancia entre la escuela o el centro de formación y la empresa. El aprender en el proceso del trabajo es base y a la vez objetivo de la acción formativa».", bold_prefix="Definición de Formación Profesional Dual:")

    add_callout(doc, "«the ability and readiness of the individual to use knowledge, skills and personal, social and methodological competences and to behave in a considered, individual and socially responsible manner. Competence is understood in this sense as the comprehensive ability to act».", bold_prefix="Concepto de Competencia en el DQR:")

    p_dqr_txt = doc.add_paragraph()
    style_p(p_dqr_txt, space_before=0, space_after=6)
    r = p_dqr_txt.add_run("El diplomado enseña a los gerentes a incorporar los estándares duales en sus propias plantas:\n"
                          "1. Co-Formación en Alternancia: Pasar de la postura pasiva ('esperar a ver qué me envía la academia') a la postura dual activa, donde la empresa se convierte en un centro de aprendizaje estructurado mediante semilleros técnicos y pasantías planificadas.\n"
                          "2. El Tutor Empresarial (Ausbilder): Formar a los jefes de taller y supervisores de línea como mentores técnicos capaces de transferir conocimientos sin egoísmos y guiar al joven en su integración cultural.\n"
                          "3. Evaluación por Resultados de Aprendizaje: Sustituir los filtros basados únicamente en diplomas de papel por pruebas situacionales donde se evidencia la *capacidad integral de acción técnica*.")
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
                       "El participante formula e implementa estrategias integrales de atracción, evaluación, fidelización y desarrollo de talento técnico operativo en su organización, capitalizando las competencias del Técnico Superior Universitario (TSU) y el modelo de formación dual, diseñando programas internos de Factor Humano basados en valores laicos universales para erradicar el maltrato en planta y elevar la productividad y seguridad laboral con el estándar del «trabajo bien hecho».")
    r.font.name = "Calibri"
    r.font.size = Pt(10)
    r.font.bold = True
    r.font.color.rgb = COLOR_PRIMARY

    p_perfiles = doc.add_paragraph()
    style_p(p_perfiles, space_before=4, space_after=6)
    r = p_perfiles.add_run("• Perfil de Ingreso: Gerentes Generales, Directores de Recursos Humanos / Talento Humano, Gerentes de Planta, Jefes de Reclutamiento, Gerentes de Mantenimiento y líderes de operaciones en empresas del sector manufacturero, agroindustrial, telecomunicaciones, energía, servicios técnicos y construcción en Guatemala.\n"
                           "• Perfil de Egreso: Líder estratégico certificado capaz de estructurar matrices de competencias operativas precisas, reducir drásticamente el costo de rotación técnica, establecer semilleros duales con Fundación Kinal y liderar programas de Factor Humano que humanicen los procesos productivos.")
    r.font.name = "Calibri"
    r.font.size = Pt(10)
    r.font.color.rgb = COLOR_DARK

    # =========================================================================
    # 5. ESTRUCTURA MODULAR Y DOSIFICACIÓN HORARIA (4 SEMANAS CONSECUTIVAS)
    # =========================================================================
    h1_5 = doc.add_paragraph()
    style_heading(h1_5, "5. Estructura Modular y Distribución Formativa (4 Semanas Consecutivas)", level=1)

    modulos_data = [
        ("Módulo 1 (Semana 1)", "El Valor del TSU y la Radiografía del Talento Operativo en Guatemala", "8 Horas", "2 Virtuales (4h) + Sábado 1 Kinal (4h)", "Diagnóstico de Brechas Operativas y Caso de Negocio (ROI del TSU)"),
        ("Módulo 2 (Semana 2)", "Reclutamiento por Competencias Técnicas y Sistemas de Formación Dual", "8 Horas", "2 Virtuales (4h) + Sábado 2 Kinal (4h)", "Descriptor por Competencias Demostrables y Plan Semillero Dual"),
        ("Módulo 3 (Semana 3)", "Cultura del Factor Humano: Valores Laicos, Dignidad y Clima Operativo", "8 Horas", "2 Virtuales (4h) + Sábado 3 Kinal (4h)", "Protocolo de Erradicación del Maltrato y Charla de Factor Humano"),
        ("Módulo 4 (Semana 4)", "Diseño e Implementación del Programa Corporativo (Proyecto Capstone)", "8 Horas", "2 Virtuales (4h) + Sábado 4 Kinal (4h)", "Plan Integral de Talento y Factor Humano Evaluado (>= 75 Pts)")
    ]

    tbl_mod = doc.add_table(rows=5, cols=5)
    tbl_mod.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_mod.autofit = False
    tbl_mod.columns[0].width = Inches(1.1)
    tbl_mod.columns[1].width = Inches(2.1)
    tbl_mod.columns[2].width = Inches(0.8)
    tbl_mod.columns[3].width = Inches(1.1)
    tbl_mod.columns[4].width = Inches(1.4)
    set_table_borders(tbl_mod, color="CBD5E0", sz="4")

    hdr_mod = tbl_mod.rows[0]
    for c in hdr_mod.cells:
        set_cell_background(c, "003366")
    headers_mod_txt = ["Módulo / Semana", "Nombre de la Unidad Formativa", "Horas", "Sesiones", "Producto Terminal del Módulo"]
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
    r = p_balance.add_run("Balance de la Modalidad Híbrida Ejecutiva (4 Semanas Intensivas Consecutivas):\n"
                          "• Ritmo Continuo sin Interrupciones: 4 semanas calendario consecutivas de inmersión ejecutiva.\n"
                          "• 16 Horas Virtuales Sincrónicas en Microsoft Teams: 8 sesiones nocturnas de 2 horas (Martes y Jueves de 19:00 a 21:00 hrs) dedicadas al marco conceptual, herramientas directivas y análisis de casos.\n"
                          "• 16 Horas Presenciales en Kinal (4 Sábados Consecutivos sin sábados de por medio): 4 sábados consecutivos de 4 horas (8:00 a 12:00 hrs) con inmersión en talleres y laboratorios de TSU, networking directivo y sustentación.\n"
                          "• Plataforma LMS Kinal.academy (Moodle): Alojamiento de lecturas ejecutivas, rúbricas y entrega del Proyecto Capstone.")
    r.font.name = "Calibri"
    r.font.size = Pt(9.5)
    r.font.color.rgb = COLOR_DARK

    # =========================================================================
    # 6. ESTRATEGIA DIDÁCTICA Y PROYECTO DIRECTIVO CAPSTONE
    # =========================================================================
    h1_6 = doc.add_paragraph()
    style_heading(h1_6, "6. Estrategia Pedagógica Ejecutiva e Inmersión Vivencial", level=1)

    p_didact = doc.add_paragraph()
    style_p(p_didact, space_before=0, space_after=6)
    r = p_didact.add_run("El programa adopta un enfoque andragógico directivo basado en tres pilares:\n"
                         "1. Método del Caso Industrial: Discusión guiada de situaciones reales de empresas guatemaltecas (conflictos de cuadrilla, accidentes por descuido, rotación crítica de técnicos, reclutamiento fallido).\n"
                         "2. Inmersión Vivencial en Laboratorios de Kinal (4 Sábados Consecutivos): Durante cada sábado consecutivo, los gerentes recorren los laboratorios de automatización, mecatrónica, redes, ciberseguridad y manufactura, dialogando directamente con estudiantes de TSU que exponen sus proyectos finales. Esto desmitifica de forma palpable la capacidad técnica y madurez de los graduandos.\n"
                         "3. Proyecto Directivo Capstone: Cada gerente participante desarrolla a lo largo de las 4 semanas el 'Plan de Talento Técnico y Cultura del Factor Humano' aplicable directamente a su empresa real, con asesoría individualizada de expertos de Kinal.")
    r.font.name = "Calibri"
    r.font.size = Pt(10)
    r.font.color.rgb = COLOR_DARK

    # =========================================================================
    # 7. SISTEMA DE EVALUACIÓN Y UMBRAL APROBATORIO INSTITUCIONAL
    # =========================================================================
    h1_7 = doc.add_paragraph()
    style_heading(h1_7, "7. Sistema de Evaluación Institucional y Criterio de Certificación", level=1)

    add_callout(doc, "La obtención de la certificación ejecutiva emitida por Fundación Kinal exige alcanzar una calificación mínima de 75 puntos sobre 100 en la evaluación continua de casos y en la defensa del Proyecto Directivo Capstone en el Sábado 4 consecutivo, conforme a la normativa de evaluación institucional.", bold_prefix="Umbral Aprobatorio Institucional Obligatorio:")

    eval_data = [
        ("Participación en Casos y Foros Directivos en Teams (25%)", "Aportes fundamentados en el análisis de dilemas de contratación, casos de rotación y dinámicas de grupo en sesiones virtuales."),
        ("Talleres Presenciales e Inmersión en Laboratorios Kinal (25%)", "Asistencia activa a los 4 sábados consecutivos en campus Kinal, auditoría de competencias en bancos reales y ejercicios de rol directivo."),
        ("Diseño de Herramientas de Factor Humano (20%)", "Elaboración de matrices de reclutamiento por competencias y protocolos de charlas de Factor Humano para mandos medios."),
        ("Defensa del Proyecto Directivo Capstone (30%)", "Presentación oral y escrita del Plan Integral de Talento Técnico y Factor Humano para su empresa ante el comité evaluador de Kinal en el Sábado 4.")
    ]

    tbl_ev = doc.add_table(rows=5, cols=2)
    tbl_ev.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_ev.autofit = False
    tbl_ev.columns[0].width = Inches(2.7)
    tbl_ev.columns[1].width = Inches(3.8)
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
    # 8. ECOSISTEMA DIGITAL Y ESPACIOS FÍSICOS
    # =========================================================================
    h1_8 = doc.add_paragraph()
    style_heading(h1_8, "8. Ecosistema Digital Institucional y Espacios Físicos", level=1)

    p_infra = doc.add_paragraph()
    style_p(p_infra, space_before=0, space_after=6)
    r = p_infra.add_run("En cumplimiento de los estándares institucionales de Fundación Kinal:\n"
                        "• Plataforma Virtual Sincrónica: Microsoft Teams para las 8 sesiones nocturnas interactivas, con canales dedicados para análisis de casos y repositorio de grabaciones.\n"
                        "• Plataforma LMS Oficial: Kinal.academy (Moodle) para la gestión académica, descarga de lecturas de liderazgo, rúbricas de evaluación y entrega formal del Proyecto Capstone.\n"
                        "• Instalaciones Presenciales en Kinal: Auditorio con soporte multimedia, salas de trabajo ejecutivo y recorrido guiado por los talleres de TSU (Laboratorios de Automatización Siemens, Mecatrónica CNC, Electrónica y Redes) durante los 4 sábados consecutivos.")
    r.font.name = "Calibri"
    r.font.size = Pt(9.5)
    r.font.color.rgb = COLOR_DARK

    section = doc.sections[0]
    footer = section.footer
    footer_p = footer.paragraphs[0]
    style_p(footer_p, space_before=0, space_after=0)
    footer_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run_f = footer_p.add_run("Fundación Kinal | Diplomado de Certificación Gerencial en Gestión del Talento Técnico — Propuesta Oficial")
    run_f.font.name = "Calibri"
    run_f.font.size = Pt(8.5)
    run_f.font.color.rgb = COLOR_SECONDARY

    out_dir = os.path.join("Cursos", "Talento_Tecnico")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "Propuesta_Diplomado_Talento_Tecnico_Kinal.docx")
    doc.save(out_path)
    print(f"Propuesta guardada con éxito en: {out_path}")

if __name__ == "__main__":
    generate_propuesta_doc()
