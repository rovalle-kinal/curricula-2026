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
    r_sub = p_sub.add_run("Capacitación Gerencial y Diálogo Estratégico para Representantes de Empresas: Manejo de Personal, Liderazgo, Factor Humano, Fortalecimiento de Competencias y Validación Técnica a Nivel Superior (1 Mes de Duración | Modalidad Virtual Semanal + 2 Jornadas Presenciales Especiales)")
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
        ("Organización Curricular:", "6 Módulos Temáticos (Un módulo por sesión: Módulo 1 en Apertura, Módulos 2 a 5 en Virtuales, Módulo 6 en Cierre) con una Actividad Formativa Evaluable por sesión"),
        ("Ejes Temáticos Oficiales:", "Manejo y desarrollo de personal, Liderazgo y factor humano, Fortalecimiento de competencias técnicas y validación TSU, Desarrollo de mandos medios, y Necesidades actuales de la industria"),
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
    # 2. FUNDAMENTACIÓN ESTRATÉGICA: VALIDACIÓN TÉCNICA Y COMPETENCIAS A NIVEL SUPERIOR
    # =========================================================================
    h1_2 = doc.add_paragraph()
    style_heading(h1_2, "2. Fundamentación Estratégica: El Nivel Técnico Superior como Respaldo Industrial", level=1)

    p_met = doc.add_paragraph()
    style_p(p_met, space_before=0, space_after=6)
    r = p_met.add_run("La manufactura y los servicios técnicos contemporáneos en Guatemala han alcanzado niveles de sofisticación tecnológica (automatización de líneas, PLCs avanzados, instrumentación de precisión, redes industriales y mantenimiento predictivo) que vuelven obsoleto el aprendizaje puramente empírico e intuitivo.\n\n"
                      "En este contexto, la industria requiere certidumbre y respaldo objetivo:\n"
                      "• El Técnico Superior Universitario (TSU) como Mecanismo de Validación de Competencias: La acreditación técnica a nivel superior formaliza y avala que el personal operativo y de supervisión domina el cálculo aplicado, el diagnóstico analítico de fallas, la lectura de planos normalizados y los protocolos de seguridad industrial. El TSU no compite con la ingeniería de diseño ni sustituye al operario de rutina: se constituye en el respaldo técnico y metodológico más confiable para las jefaturas de planta.\n"
                      "• Importancia de las Competencias a Nivel Superior en el Área Técnica: Formar mandos medios con competencias superiores técnicas permite cerrar la brecha entre la planeación gerencial y la ejecución en piso, reduciendo paradas no programadas, averías por impericia y retrabajos costosos.\n"
                      "• Capacitación Gerencial para Auditar y Fortalecer Equipos: Los gerentes participantes adquieren herramientas objetivas para diagnosticar el nivel real de destrezas de sus colaboradores y estructurar planes de desarrollo técnico continuo en sus empresas.")
    r.font.name = "Calibri"
    r.font.size = Pt(10)
    r.font.color.rgb = COLOR_DARK

    # =========================================================================
    # 3. COMPETENCIA GENERAL Y PERFILES DEL PARTICIPANTE
    # =========================================================================
    h1_3 = doc.add_paragraph()
    style_heading(h1_3, "3. Competencia General y Perfil de los Participantes", level=1)

    p_comp = doc.add_paragraph()
    style_p(p_comp, space_before=0, space_after=6)
    r = p_comp.add_run("Competencia General del Programa:\n"
                       "El participante formula e implementa estrategias gerenciales para el manejo, desarrollo y liderazgo de personal operativo y mandos medios, incorporando la cultura del Factor Humano y el estándar del «trabajo bien hecho», y utiliza los criterios del Técnico Superior Universitario (TSU) como marco de validación y fortalecimiento de competencias técnicas a nivel superior para responder a las necesidades actuales de la industria.")
    r.font.name = "Calibri"
    r.font.size = Pt(10)
    r.font.bold = True
    r.font.color.rgb = COLOR_PRIMARY

    p_perfiles = doc.add_paragraph()
    style_p(p_perfiles, space_before=4, space_after=6)
    r = p_perfiles.add_run("• Perfil de Ingreso: Gerentes Generales, Gerentes de Operaciones, Planta o Mantenimiento, Directores/Gerentes de Talento Humano y Recursos Humanos, Jefes de Reclutamiento y Supervisores Generales con responsabilidad sobre equipos técnicos en sectores industriales de Guatemala.\n"
                            "• Perfil de Egreso: Líder empresarial capacitado en metodologías de supervisión formativa, con capacidad para auditar competencias técnicas operativas con estándares de nivel superior, erradicar el maltrato en planta, estructurar semilleros de aprendizaje y vincular a su empresa con Fundación Kinal.")
    r.font.name = "Calibri"
    r.font.size = Pt(10)
    r.font.color.rgb = COLOR_DARK

    # =========================================================================
    # 4. ESTRUCTURA MODULAR: UN MÓDULO POR SESIÓN CON ACTIVIDAD EVALUABLE
    # =========================================================================
    h1_4 = doc.add_paragraph()
    style_heading(h1_4, "4. Estructura Curricular: Un Módulo por Sesión y Actividades Evaluables", level=1)

    p_est_desc = doc.add_paragraph()
    style_p(p_est_desc, space_before=0, space_after=6)
    r = p_est_desc.add_run("El programa se organiza en **6 Módulos Formativos (un módulo por sesión)**, cada uno dotado de una **Actividad Formativa Evaluable** que asegura la transferencia inmediata de herramientas gerenciales a la empresa:")
    r.font.name = "Calibri"
    r.font.size = Pt(10)
    r.font.color.rgb = COLOR_DARK

    modulos_data = [
        ("Módulo 1 (Presencial)", "Apertura Institucional, Presentación de la Iniciativa y Diagnóstico de Necesidades Industriales", "4 Horas", "Presencial en Campus Kinal", "Matriz Diagnóstica de Necesidades Industriales y Brechas Técnicas"),
        ("Módulo 2 (Virtual 1)", "Manejo y Desarrollo de Personal Técnico: Atracción, Inducción Acelerada y Retención", "2 Horas", "Virtual Sincrónico (Teams)", "Descriptor de Puesto por Competencias y Plan de Onboarding (30-60-90 Días)"),
        ("Módulo 3 (Virtual 2)", "Liderazgo y Factor Humano en Cuadrillas: Dignidad, Trabajo Bien Hecho y Cero Maltrato", "2 Horas", "Virtual Sincrónico (Teams)", "Código de Convivencia Operativa y Protocolo de Seguridad Psicológica"),
        ("Módulo 4 (Virtual 3)", "Fortalecimiento de Competencias Técnicas: El Nivel Técnico Superior (TSU) como Respaldo", "2 Horas", "Virtual Sincrónico (Teams)", "Matriz de Validación Técnica de Planta bajo Estándar de Competencias TSU"),
        ("Módulo 5 (Virtual 4)", "Desarrollo de Mandos Medios: Supervisión de Primera Línea, Feedback y Charlas de Valores", "2 Horas", "Virtual Sincrónico (Teams)", "Plan de Coaching para Supervisores y Catálogo de 5 Micro-Charlas de Factor Humano"),
        ("Módulo 6 (Presencial)", "Plenaria de Diálogo Industria-Academia, Acuerdos de Vinculación y Clausura", "4 Horas", "Presencial en Campus Kinal", "Sustentación Plenaria del Plan de Acción y Entrega de Diplomas Oficiales")
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
    headers_mod_txt = ["Módulo / Formato", "Nombre del Módulo", "Horas", "Modalidad / Plataforma", "Actividad Formativa Evaluable"]
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
        if "Presencial" in m_id:
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
                          "• 8 Horas Presenciales Vivenciales (Módulos 1 y 6 en Campus Kinal): Apertura institucional, inmersión en talleres técnicos, mesas de diálogo industria-academia, acuerdos de vinculación y entrega solemne de diplomas y reconocimientos.\n"
                          "• 8 Horas Virtuales Sincrónicas en Microsoft Teams (Módulos 2 a 5): 4 sesiones semanales de 2 horas dedicadas a herramientas gerenciales en manejo de personal, liderazgo humanista, competencias técnicas nivel superior (TSU) y mandos medios.\n"
                          "• 4 Horas de Autodiagnóstico en Kinal.academy (Moodle): Consolidación de instrumentos de gestión técnica y plan de acción empresarial.\n"
                          "• Total: 20 Horas Formativas Ejecutivas.")
    r.font.name = "Calibri"
    r.font.size = Pt(9.5)
    r.font.color.rgb = COLOR_DARK

    # =========================================================================
    # 5. METODOLOGÍA ANDRAGÓGICA Y CAJA DE HERRAMIENTAS
    # =========================================================================
    h1_5 = doc.add_paragraph()
    style_heading(h1_5, "5. Metodología Andragógica de Formación Gerencial", level=1)

    p_metod = doc.add_paragraph()
    style_p(p_metod, space_before=0, space_after=6)
    r = p_metod.add_run("El programa aplica un modelo andragógico dinámico diseñado para la alta dirección y líderes de área:\n"
                        "1. Dinámica de Casos Gerenciales: Discusión de escenarios reales de planta (retrasos de producción, supervisores autoritarios, resistencia al reporte de averías, curvas lentas de adaptación técnica).\n"
                        "2. Entregables Prácticos por Módulo: Cada sesión culmina con una herramienta técnica directamente aplicable en la empresa del participante (descriptores, protocolos, matrices y micro-charlas).\n"
                        "3. Espacios Formales de Diálogo Industria-Academia: Intercambio bidireccional donde los gerentes aportan retroalimentación crítica sobre las demandas actuales de cualificación técnica.")
    r.font.name = "Calibri"
    r.font.size = Pt(10)
    r.font.color.rgb = COLOR_DARK

    # =========================================================================
    # 6. ACREDITACIÓN, DIPLOMAS Y RECONOCIMIENTOS EMPRESARIALES
    # =========================================================================
    h1_6 = doc.add_paragraph()
    style_heading(h1_6, "6. Acreditación Institucional, Diplomas y Reconocimientos", level=1)

    p_acred = doc.add_paragraph()
    style_p(p_acred, space_before=0, space_after=6)
    r = p_acred.add_run("En el Módulo 6 (Jornada Presencial de Cierre) en campus Kinal se realizará la ceremonia de clausura con dos acreditaciones oficiales:\n"
                        "1. Diploma de Participación Individual: Otorgado al representante empresarial que cumplió con el 80% de asistencia a las sesiones sincrónicas y la entrega de sus actividades formativas (nota mínima aprobatoria de 75/100 puntos).\n"
                        "2. Reconocimiento Empresarial Institucional: Galardón otorgado por Fundación Kinal a la empresa participante, acreditándola como «Empresa Aliada en la Vinculación Técnica y Formación del Talento Humano».")
    r.font.name = "Calibri"
    r.font.size = Pt(10)
    r.font.color.rgb = COLOR_DARK

    # =========================================================================
    # 7. PLATAFORMAS TECNOLÓGICAS E INFRAESTRUCTURA
    # =========================================================================
    h1_7 = doc.add_paragraph()
    style_heading(h1_7, "7. Ecosistema Digital e Infraestructura Institucional", level=1)

    p_infra = doc.add_paragraph()
    style_p(p_infra, space_before=0, space_after=6)
    r = p_infra.add_run("En cumplimiento de los estándares institucionales de Fundación Kinal:\n"
                        "• Plataforma Virtual Sincrónica: Microsoft Teams para las sesiones virtuales semanales, con salas de trabajo grupal y repositorio de grabaciones.\n"
                        "• Plataforma LMS Oficial: Kinal.academy (Moodle) para la descarga de lecturas, plantillas gerenciales y entrega de actividades evaluables.\n"
                        "• Instalaciones Presenciales en Kinal: Auditorio Ejecutivo climatizado con soporte multimedia, salas de trabajo directivo y recorrido por los talleres y laboratorios de formación técnica.")
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

    for out_dir in [os.path.join("Cursos", "Talento_Tecnico"), "Talento_Tecnico"]:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "Propuesta_Diplomado_Talento_Tecnico_Kinal.docx")
        doc.save(out_path)
        print(f"Propuesta guardada con éxito en: {out_path}")

if __name__ == "__main__":
    generate_propuesta_doc()
