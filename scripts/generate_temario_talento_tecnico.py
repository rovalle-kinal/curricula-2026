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

def set_cell_margins(cell, top=60, bottom=60, left=80, right=80):
    tcPr = cell._element.get_or_add_tcPr()
    tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}>'
                      f'<w:top w:w="{top}" w:type="dxa"/>'
                      f'<w:left w:w="{left}" w:type="dxa"/>'
                      f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
                      f'<w:right w:w="{right}" w:type="dxa"/>'
                      f'</w:tcMar>')
    tcPr.append(tcMar)

def set_table_borders(table, color="CBD5E0", sz="4"):
    tblPr = table._element.xpath('w:tblPr')
    if tblPr:
        borders = parse_xml(
            f'<w:tblBorders {nsdecls("w")}>'
            f'<w:top w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'<w:bottom w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'<w:left w:val="none"/>'
            f'<w:right w:val="none"/>'
            f'<w:insideH w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'<w:insideV w:val="none"/>'
            f'</w:tblBorders>'
        )
        tblPr[0].append(borders)

def add_callout(doc, text, bold_prefix=""):
    table = doc.add_table(rows=1, cols=1)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    table.autofit = False
    table.columns[0].width = Inches(6.5)
    
    cell = table.cell(0, 0)
    set_cell_background(cell, "F7FAFC")
    set_cell_margins(cell, top=100, bottom=100, left=140, right=140)
    
    tcPr = cell._element.get_or_add_tcPr()
    borders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'<w:top w:val="none"/>'
        f'<w:left w:val="single" w:sz="24" w:space="0" w:color="003366"/>'
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
        r_pre.font.size = Pt(9.5)
        r_pre.font.bold = True
        r_pre.font.color.rgb = RGBColor(0, 51, 102)
    r = p.add_run(text)
    r.font.name = "Calibri"
    r.font.size = Pt(9.5)
    r.font.italic = True
    r.font.color.rgb = RGBColor(45, 55, 72)
    doc.add_paragraph().paragraph_format.space_after = Pt(6)

def style_heading(p, text, level=1):
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    r.font.name = "Calibri"
    r.font.bold = True
    if level == 1:
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(6)
        r.font.size = Pt(14)
        r.font.color.rgb = RGBColor(0, 51, 102)
    elif level == 2:
        p.paragraph_format.space_before = Pt(11)
        p.paragraph_format.space_after = Pt(4)
        r.font.size = Pt(11.5)
        r.font.color.rgb = RGBColor(0, 51, 102)
    elif level == 3:
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(2)
        r.font.size = Pt(10)
        r.font.color.rgb = RGBColor(74, 85, 104)

def style_p(p, space_before=0, space_after=4, line_spacing=1.15):
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = line_spacing

def generate_temario_doc():
    doc = docx.Document()
    
    for section in doc.sections:
        section.top_margin = Inches(0.9)
        section.bottom_margin = Inches(0.9)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    COLOR_PRIMARY = RGBColor(0, 51, 102)      # Azul Kinal
    COLOR_SECONDARY = RGBColor(74, 85, 104)    # Gris pizarra
    COLOR_DARK = RGBColor(26, 32, 44)         # Texto oscuro

    # ==========================================
    # ENCABEZADO INSTITUCIONAL
    # ==========================================
    title_p = doc.add_paragraph()
    style_p(title_p, space_before=0, space_after=4)
    run_title = title_p.add_run("Programa Ejecutivo de Vinculación y Liderazgo: Gestión del Talento Técnico y Mandos Medios")
    run_title.font.name = "Calibri"
    run_title.font.size = Pt(18)
    run_title.font.bold = True
    run_title.font.color.rgb = COLOR_PRIMARY

    sub_p = doc.add_paragraph()
    style_p(sub_p, space_before=0, space_after=12)
    run_sub = sub_p.add_run("Temario Analítico Oficial y Estructura Curricular por Módulos  |  Fundación Kinal — Dirección de Vinculación Empresarial\nTotal: 8 Horas Formativas Ejecutivas | Organización Modular: Un Módulo por Sesión (4 Módulos / 4 Sesiones de 2 Horas)\nModalidad Híbrida: 2 Sesiones Presenciales en Campus Kinal (4h) + 2 Sesiones Virtuales en Microsoft Teams (4h)")
    run_sub.font.name = "Calibri"
    run_sub.font.size = Pt(10)
    run_sub.font.italic = True
    run_sub.font.color.rgb = COLOR_SECONDARY

    add_callout(doc, 
        "«the ability and readiness of the individual to use knowledge, skills and personal, social and methodological competences and to behave in a considered, individual and socially responsible manner. Competence is understood in this sense as the comprehensive ability to act». El programa promueve un espacio de diálogo bidireccional entre la industria y Fundación Kinal para capacitar a los líderes de equipos en manejo de personal, liderazgo humanista, competencias técnicas operativas y mandos medios, integrando el Factor Humano y promoviendo el nivel Técnico Superior Universitario (TSU) como mecanismo riguroso de validación técnica y respaldo objetivo para la industria.", 
        bold_prefix="Definición de Competencia DQR e Ideario Kinal:")

    # ==========================================
    # 1. OBJETIVOS FORMATIVOS Y COMPETENCIAS
    # ==========================================
    h1_1 = doc.add_paragraph()
    style_heading(h1_1, "1. Competencia General y Resultados de Aprendizaje por Módulos", level=1)

    p_cg = doc.add_paragraph()
    style_p(p_cg, space_before=0, space_after=6)
    r = p_cg.add_run("Competencia General del Programa:\n"
                     "El participante implementa metodologías gerenciales efectivas para el manejo, desarrollo y liderazgo de personal operativo y mandos medios, aplicando la cultura del Factor Humano y los estándares de excelencia del «trabajo bien hecho», y utiliza los criterios del Técnico Superior Universitario (TSU) como marco de validación técnica y respaldo objetivo para responder con calidad y rigor a las necesidades actuales de la industria.")
    r.font.name = "Calibri"
    r.font.size = Pt(9.5)
    r.font.bold = True
    r.font.color.rgb = COLOR_PRIMARY

    mod_comps = [
        ("Módulo 1: Apertura Institucional, Liderazgo y Factor Humano en Cuadrillas de Trabajo (Sesión Presencial 1 — Campus Kinal • 2h)", 
         "Conoce la visión formativa de Kinal e implementa la cultura del Factor Humano en áreas productivas: respeto a la dignidad de la persona, erradicación tajante del maltrato verbal y fomento de seguridad psicológica para reportar fallas e incidentes sin temor.\nActividad Formativa Evaluable: Código de Convivencia Operativa y Protocolo de Seguridad Psicológica y Cero Maltrato en Planta (25 Pts)."),
        
        ("Módulo 2: Manejo de Personal Técnico y Desarrollo de Mandos Medios en Planta (Sesión Virtual 1 — Microsoft Teams • 2h)", 
         "Aplica metodologías contemporáneas para la atracción y selección por competencias demostrables, diseña planes de inducción técnica acelerada (onboarding en 30-60-90 días) para mitigar rotación temprana, y equipa a supervisores con herramientas de feedback asertivo y micro-charlas operativas de valores antes del turno vinculadas a KPIs (OEE/SSO).\nActividad Formativa Evaluable: Descriptor por Competencias, Plan Onboarding 30-60-90 y Catálogo de 3 Micro-Charlas de Factor Humano (25 Pts)."),
        
        ("Módulo 3: Fortalecimiento y Validación de Competencias: Nivel Técnico Superior (TSU) (Sesión Virtual 2 — Microsoft Teams • 2h)", 
         "Estructura matrices de competencias operativas observables (saber, hacer y ser), diseña pruebas de evaluación práctica en puesto y articula el nivel Técnico Superior (TSU) como el mecanismo institucional de validación técnica y respaldo objetivo para la industria ante tecnologías complejas.\nActividad Formativa Evaluable: Guía de Evaluación Práctica en Puesto y Matriz de Validación Técnica de Planta bajo Estándar TSU (25 Pts)."),
        
        ("Módulo 4: Sistematización de Demandas Industriales, Acuerdos de Vinculación y Clausura (Sesión Presencial 2 — Campus Kinal • 2h)", 
         "Participa en la mesa redonda plenaria de sistematización de demandas formativas de la industria para retroalimentar las carreras de Kinal, formaliza acuerdos de cooperación institucional y recibe el diploma de participación individual y reconocimiento corporativo.\nActividad Formativa Evaluable: Sustentación Plenaria de la Ficha Diagnóstica Empresarial y Firma de Acuerdos de Vinculación (25 Pts).")
    ]

    for m_tit, m_desc in mod_comps:
        p_m = doc.add_paragraph()
        style_p(p_m, space_before=3, space_after=4)
        p_m.paragraph_format.left_indent = Inches(0.2)
        r_b = p_m.add_run(f"• {m_tit}:\n")
        r_b.font.name = "Calibri"
        r_b.font.size = Pt(9.5)
        r_b.font.bold = True
        r_b.font.color.rgb = COLOR_PRIMARY
        r_d = p_m.add_run(m_desc)
        r_d.font.name = "Calibri"
        r_d.font.size = Pt(9.5)
        r_d.font.color.rgb = COLOR_DARK

    # ==========================================
    # 2. TEMARIO ANALÍTICO DETALLADO POR MÓDULOS
    # ==========================================
    h1_2 = doc.add_paragraph()
    style_heading(h1_2, "2. Temario Analítico Detallado por Módulos (Un Módulo por Sesión de 2 Horas)", level=1)

    # -------------------------------------------------------------
    # MÓDULO 1
    # -------------------------------------------------------------
    h2_m1 = doc.add_paragraph()
    style_heading(h2_m1, "MÓDULO 1: APERTURA INSTITUCIONAL, LIDERAZGO Y FACTOR HUMANO EN CUADRILLAS DE TRABAJO\n(Sesión Presencial 1 — 2 Horas en Campus Kinal)", level=2)

    temas_m1 = [
        ("1.1 Apertura Institucional y Presentación de la Iniciativa de Vinculación", [
            "Bienvenida protocolaria por autoridades de Fundación Kinal y presentación del propósito del programa.",
            "La misión formativa de Kinal: educación integral técnica, excelencia profesional y servicio a la sociedad.",
            "Dinámica de networking directivo entre representantes de empresas y sectores productivos."
        ]),
        ("1.2 La Filosofía del Factor Humano de Fundación Kinal en la Operación", [
            "La persona en el centro del trabajo productivo: el trabajo como medio de realización y servicio.",
            "Los 4 Pilares Operativos de Kinal: Respeto a la Dignidad, El Trabajo Bien Hecho, Espíritu de Servicio y Libertad Responsable.",
            "El principio del «Trabajo Bien Hecho»: orden y pulcritud (5S), custodia celosa de maquinaria y herramientas, tolerancias exactas y rigor ético."
        ]),
        ("1.3 Liderazgo Humanista y Seguridad Psicológica en Planta", [
            "Superación definitiva de la cultura del capataz: erradicación tajante del maltrato verbal, gritos y autoritarismo en planta y talleres.",
            "Seguridad psicológica en el trabajo: cómo generar confianza para que los operarios reporten averías, fallas incipientes y cuasi-accidentes de inmediato sin temor a represalias destructivas.",
            "Establecimiento de códigos de convivencia respetuosa y canales éticos de escucha en áreas técnicas."
        ])
    ]

    for sub_tit, sub_items in temas_m1:
        p_st = doc.add_paragraph()
        style_heading(p_st, sub_tit, level=3)
        for it in sub_items:
            p_it = doc.add_paragraph()
            style_p(p_it, space_before=1, space_after=2)
            p_it.paragraph_format.left_indent = Inches(0.25)
            r_b = p_it.add_run("• ")
            r_b.font.bold = True
            r_b.font.color.rgb = COLOR_PRIMARY
            r_txt = p_it.add_run(it)
            r_txt.font.name = "Calibri"
            r_txt.font.size = Pt(9.5)
            r_txt.font.color.rgb = COLOR_DARK

    p_act1 = doc.add_paragraph()
    style_p(p_act1, space_before=4, space_after=6)
    p_act1.paragraph_format.left_indent = Inches(0.25)
    r_act_lbl = p_act1.add_run("Actividad Formativa Evaluable del Módulo 1 (25 Puntos): ")
    r_act_lbl.font.bold = True
    r_act_lbl.font.color.rgb = COLOR_PRIMARY
    r_act_txt = p_act1.add_run("Código de Convivencia Operativa y Protocolo de Seguridad Psicológica y Cero Tolerancia al Maltrato en Planta.")
    r_act_txt.font.italic = True

    # -------------------------------------------------------------
    # MÓDULO 2
    # -------------------------------------------------------------
    h2_m2 = doc.add_paragraph()
    style_heading(h2_m2, "MÓDULO 2: MANEJO DE PERSONAL TÉCNICO Y DESARROLLO DE MANDOS MEDIOS EN PLANTA\n(Sesión Virtual 1 — 2 Horas en Microsoft Teams)", level=2)

    temas_m2 = [
        ("2.1 Atracción y Reclutamiento Efectivo de Talento Operativo", [
            "Por qué fracasan los descriptores de puesto tradicionales en áreas operativas y técnicas.",
            "Diseño de descriptores basados en competencias demostrables (saber conceptual, destreza manual e instrumental y actitud de seguridad).",
            "Canales efectivos y estrategias de selección para atraer personal técnico con potencial de crecimiento."
        ]),
        ("2.2 Inducción Técnica Acelerada (Onboarding en 30-60-90 Días) y Reducción de Rotación", [
            "Costos ocultos de la rotación temprana en plantas: mermas, retrabajos, desbalance de cuadrillas y desgaste de supervisión.",
            "Estructuración de planes de inducción técnica paso a paso: conocimiento de procesos, maquinaria crítica y estándares de calidad.",
            "Rutas de desarrollo técnico para fidelizar al colaborador operativo calificado."
        ]),
        ("2.3 Supervisión de Primera Línea y 'Micro-Charlas de Factor Humano'", [
            "El supervisor de taller como puente crítico: articulación entre la gerencia y la realidad cotidiana del piso de planta.",
            "Herramientas de comunicación asertiva, retroalimentación formativa sin humillar y resolución constructiva de conflictos.",
            "Diseño y conducción de 'Las Charlas de 10 Minutos de Factor Humano' antes de iniciar el turno vinculadas a KPIs (OEE y SSO)."
        ])
    ]

    for sub_tit, sub_items in temas_m2:
        p_st = doc.add_paragraph()
        style_heading(p_st, sub_tit, level=3)
        for it in sub_items:
            p_it = doc.add_paragraph()
            style_p(p_it, space_before=1, space_after=2)
            p_it.paragraph_format.left_indent = Inches(0.25)
            r_b = p_it.add_run("• ")
            r_b.font.bold = True
            r_b.font.color.rgb = COLOR_PRIMARY
            r_txt = p_it.add_run(it)
            r_txt.font.name = "Calibri"
            r_txt.font.size = Pt(9.5)
            r_txt.font.color.rgb = COLOR_DARK

    p_act2 = doc.add_paragraph()
    style_p(p_act2, space_before=4, space_after=6)
    p_act2.paragraph_format.left_indent = Inches(0.25)
    r_act_lbl = p_act2.add_run("Actividad Formativa Evaluable del Módulo 2 (25 Puntos): ")
    r_act_lbl.font.bold = True
    r_act_lbl.font.color.rgb = COLOR_PRIMARY
    r_act_txt = p_act2.add_run("Descriptor de Puesto Técnico por Competencias Demostrables, Plan de Onboarding en 30-60-90 Días y Catálogo de 3 Micro-Charlas de Factor Humano.")
    r_act_txt.font.italic = True

    # -------------------------------------------------------------
    # MÓDULO 3
    # -------------------------------------------------------------
    h2_m3 = doc.add_paragraph()
    style_heading(h2_m3, "MÓDULO 3: FORTALECIMIENTO Y VALIDACIÓN DE COMPETENCIAS: EL NIVEL TÉCNICO SUPERIOR (TSU) COMO RESPALDO INDUSTRIAL\n(Sesión Virtual 2 — 2 Horas en Microsoft Teams)", level=2)

    temas_m3 = [
        ("3.1 Mapeo y Estandarización de Competencias Operativas de Planta", [
            "Definición y estructuración de competencias técnicas de planta bajo marcos internacionales (DQR).",
            "Desglose tridimensional de la competencia técnica: saber (conocimiento normativo y analítico), saber hacer (destreza manual, calibración e instrumental) y saber ser (seguridad y orden operativo).",
            "Instrumentos objetivos para auditar el nivel técnico real del personal operativo en piso."
        ]),
        ("3.2 El Técnico Superior Universitario (TSU) como Mecanismo de Validación y Respaldo para la Industria", [
            "El Técnico Superior Universitario (TSU) como mecanismo riguroso de validación de competencias técnicas: garantía de solvencia operativa, lectura avanzada de planos e interpretación analítica de fallas.",
            "La importancia de las competencias a nivel superior en el área técnica: por qué la tecnología moderna (PLCs, control numérico, servomecanismos, redes industriales) exige respaldo formativo formal y no mera intuición empírica.",
            "El TSU como respaldo indispensable para la industria: articulación eficiente entre la ingeniería de diseño y la ejecución en piso, reduciendo tiempos muertos y costos de mantenimiento correctivo."
        ]),
        ("3.3 Evaluación Práctica en Puesto y Transferencia de Habilidades", [
            "Diseño de pruebas prácticas en banco de trabajo: evaluación de diagnóstico lógico, conexionado y medición de precisión.",
            "Esquemas de semilleros y aprendizaje continuo en planta.",
            "El rol del mentor técnico de taller (*Ausbilder*) y la metodología de 4 pasos para la enseñanza de tareas en puesto."
        ])
    ]

    for sub_tit, sub_items in temas_m3:
        p_st = doc.add_paragraph()
        style_heading(p_st, sub_tit, level=3)
        for it in sub_items:
            p_it = doc.add_paragraph()
            style_p(p_it, space_before=1, space_after=2)
            p_it.paragraph_format.left_indent = Inches(0.25)
            r_b = p_it.add_run("• ")
            r_b.font.bold = True
            r_b.font.color.rgb = COLOR_PRIMARY
            r_txt = p_it.add_run(it)
            r_txt.font.name = "Calibri"
            r_txt.font.size = Pt(9.5)
            r_txt.font.color.rgb = COLOR_DARK

    p_act3 = doc.add_paragraph()
    style_p(p_act3, space_before=4, space_after=6)
    p_act3.paragraph_format.left_indent = Inches(0.25)
    r_act_lbl = p_act3.add_run("Actividad Formativa Evaluable del Módulo 3 (25 Puntos): ")
    r_act_lbl.font.bold = True
    r_act_lbl.font.color.rgb = COLOR_PRIMARY
    r_act_txt = p_act3.add_run("Guía de Evaluación Práctica en Puesto y Matriz de Validación Técnica de Planta bajo el Estándar de Competencias del Técnico Superior (TSU).")
    r_act_txt.font.italic = True

    # -------------------------------------------------------------
    # MÓDULO 4
    # -------------------------------------------------------------
    h2_m4 = doc.add_paragraph()
    style_heading(h2_m4, "MÓDULO 4: SISTEMATIZACIÓN DE DEMANDAS INDUSTRIALES, ACUERDOS DE VINCULACIÓN Y CLAUSURA\n(Sesión Presencial 2 — 2 Horas en Campus Kinal)", level=2)

    temas_m4 = [
        ("4.1 Mesa Redonda Plenaria: Sistematización de las Necesidades Actuales de la Industria", [
            "Consolidación de las matrices y fichas diagnósticas: qué competencias técnicas y humanas demanda prioritariamente el sector productivo guatemalteco.",
            "Retroalimentación directa a directores de carrera y autoridades de Kinal para afinar los planes de estudio del nivel Técnico Superior y carreras técnicas.",
            "Identificación de tecnologías de punta para la modernización curricular y equipamiento de laboratorios."
        ]),
        ("4.2 Acuerdos de Vinculación y Rutas de Cooperación Kinal-Empresas", [
            "Mecanismos de acceso prioritario y directo a la Bolsa de Egresados y banco de talentos técnicos de Kinal.",
            "Oportunidades de convenios de semilleros técnicos, pasantías y formación dual escuela-empresa.",
            "Certificación y acreditación de competencias laborales para colaboradores de planta en instalaciones de Kinal."
        ]),
        ("4.3 Acto Solemne de Clausura y Entrega de Distinciones Institucionales", [
            "Entrega de Diplomas de Participación Individual a los representantes empresariales.",
            "Entrega de Reconocimientos Empresariales Especiales a las empresas participantes como socias estratégicas de la educación técnica.",
            "Brindis de honor y networking directivo de vinculación."
        ])
    ]

    for sub_tit, sub_items in temas_m4:
        p_st = doc.add_paragraph()
        style_heading(p_st, sub_tit, level=3)
        for it in sub_items:
            p_it = doc.add_paragraph()
            style_p(p_it, space_before=1, space_after=2)
            p_it.paragraph_format.left_indent = Inches(0.25)
            r_b = p_it.add_run("• ")
            r_b.font.bold = True
            r_b.font.color.rgb = COLOR_PRIMARY
            r_txt = p_it.add_run(it)
            r_txt.font.name = "Calibri"
            r_txt.font.size = Pt(9.5)
            r_txt.font.color.rgb = COLOR_DARK

    p_act4 = doc.add_paragraph()
    style_p(p_act4, space_before=4, space_after=6)
    p_act4.paragraph_format.left_indent = Inches(0.25)
    r_act_lbl = p_act4.add_run("Actividad Formativa Evaluable del Módulo 4 (25 Puntos): ")
    r_act_lbl.font.bold = True
    r_act_lbl.font.color.rgb = COLOR_PRIMARY
    r_act_txt = p_act4.add_run("Sustentación Plenaria de la Ficha Diagnóstica Empresarial y Firma de Acuerdos de Vinculación, culminando con la entrega de diplomas y reconocimientos.")
    r_act_txt.font.italic = True

    # ==========================================
    # 3. REFERENCIAS BIBLIOGRÁFICAS
    # ==========================================
    h1_3 = doc.add_paragraph()
    style_heading(h1_3, "3. Fuentes Bibliográficas y Documentos de Apoyo", level=1)

    referencias = [
        ("BIBB / DQR:", "German Qualifications Framework for Lifelong Learning (DQR) — Competencias y Formación Técnica Aplicada a Nivel Superior."),
        ("OIT / Cinterfor:", "Formación Profesional y Vinculación Escuela-Empresa en América Latina: Diálogo Social y Validación de Competencias Técnicas."),
        ("Fundación Kinal:", "Ideario Institucional: El Trabajo como Vocación y Servicio a la Persona Humana."),
        ("Fundación Kinal:", "Manual de Factor Humano: Liderazgo y Trabajo Bien Hecho en Cuadrillas Técnicas."),
        ("Fundación Kinal:", "Marco Curricular y Estándares del Técnico Superior Universitario (TSU): Validación de Competencias y Pertinencia Industrial.")
    ]

    for org, det in referencias:
        p_r = doc.add_paragraph()
        style_p(p_r, space_before=1, space_after=2)
        p_r.paragraph_format.left_indent = Inches(0.2)
        r_b = p_r.add_run(f"• {org} ")
        r_b.font.name = "Calibri"
        r_b.font.size = Pt(9)
        r_b.font.bold = True
        r_b.font.color.rgb = COLOR_PRIMARY
        r_d = p_r.add_run(det)
        r_d.font.name = "Calibri"
        r_d.font.size = Pt(9)
        r_d.font.color.rgb = COLOR_DARK

    section = doc.sections[0]
    footer = section.footer
    footer_p = footer.paragraphs[0]
    style_p(footer_p, space_before=0, space_after=0)
    footer_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run_f = footer_p.add_run("Fundación Kinal | Programa Ejecutivo de Vinculación y Liderazgo — Temario Oficial (8 Horas)")
    run_f.font.name = "Calibri"
    run_f.font.size = Pt(8.5)
    run_f.font.color.rgb = COLOR_SECONDARY

    for out_dir in [os.path.join("Cursos", "Talento_Tecnico"), "Talento_Tecnico"]:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "Temario_Diplomado_Talento_Tecnico_Kinal.docx")
        doc.save(out_path)
        print(f"Temario guardado con éxito en: {out_path}")

if __name__ == "__main__":
    generate_temario_doc()
