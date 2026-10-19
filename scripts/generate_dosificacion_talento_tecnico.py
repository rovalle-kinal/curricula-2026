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

def set_cell_margins(cell, top=50, bottom=50, left=70, right=70):
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
        r.font.size = Pt(13.5)
        r.font.color.rgb = RGBColor(0, 51, 102)
    elif level == 2:
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(4)
        r.font.size = Pt(11)
        r.font.color.rgb = RGBColor(0, 51, 102)
    elif level == 3:
        p.paragraph_format.space_before = Pt(7)
        p.paragraph_format.space_after = Pt(2)
        r.font.size = Pt(9.5)
        r.font.color.rgb = RGBColor(74, 85, 104)

def style_p(p, space_before=0, space_after=4, line_spacing=1.15):
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = line_spacing

def generate_dosificacion_doc():
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
    p_inst = doc.add_paragraph()
    style_p(p_inst, space_before=0, space_after=2)
    r_inst = p_inst.add_run("FUNDACIÓN KINAL — DIRECCIÓN DE VINCULACIÓN EMPRESARIAL")
    r_inst.font.name = "Calibri"
    r_inst.font.size = Pt(11)
    r_inst.font.bold = True
    r_inst.font.color.rgb = COLOR_PRIMARY

    p_tit = doc.add_paragraph()
    style_p(p_tit, space_before=0, space_after=4)
    r_tit = p_tit.add_run("DOSIFICACIÓN DIDÁCTICA Y SECUENCIACIÓN OPERATIVA:\nPROGRAMA EJECUTIVO DE VINCULACIÓN Y LIDERAZGO: GESTIÓN DEL TALENTO TÉCNICO Y MANDOS MEDIOS")
    r_tit.font.name = "Calibri"
    r_tit.font.size = Pt(16)
    r_tit.font.bold = True
    r_tit.font.color.rgb = COLOR_PRIMARY

    p_sub = doc.add_paragraph()
    style_p(p_sub, space_before=0, space_after=10)
    r_sub = p_sub.add_run("Cronograma Pedagógico Encuentro por Encuentro | 1 Mes de Duración | Organización Modular: Un Módulo por Sesión (6 Módulos / 6 Sesiones / 6 Actividades Evaluables)\nModalidad Híbrida: 2 Jornadas Presenciales Especiales en Campus Kinal (8h) + 4 Sesiones Virtuales Semanales en Microsoft Teams (8h)")
    r_sub.font.name = "Calibri"
    r_sub.font.size = Pt(10)
    r_sub.font.italic = True
    r_sub.font.color.rgb = COLOR_SECONDARY

    add_callout(doc, 
        "«El aprender en el proceso del trabajo es base y a la vez objetivo de la acción formativa». Las 16 horas de contacto sincrónico y presencial se organizan estrictamente en 6 Módulos Formativos (un módulo por sesión): 4 sesiones virtuales semanales de 2 horas en Microsoft Teams y 2 jornadas presenciales especiales de 4 horas en el campus de Fundación Kinal (Apertura y Clausura con entrega de Diplomas y Reconocimientos). Cada módulo integra una Actividad Formativa Evaluable orientada a la aplicación directa en la empresa. El programa articula el Factor Humano y consolida el Técnico Superior Universitario (TSU) como mecanismo riguroso de validación de competencias técnicas para la industria. Umbral aprobatorio institucional: 75 puntos sobre 100.",
        bold_prefix="Organización Pedagógica Modular e Ideario Kinal:")

    # =========================================================================
    # 1. MATRIZ GENERAL CRONOLÓGICA DE LOS 6 ENCUENTROS
    # =========================================================================
    h1_1 = doc.add_paragraph()
    style_heading(h1_1, "1. Matriz General de Dosificación Modular (1 Mes — 6 Módulos / 6 Sesiones)", level=1)

    sesiones_info = [
        ("Módulo 1\n(Presencial 1 • 4h)", "Necesidades Actuales de la Industria y Diagnóstico del Talento Operativo", "Apertura institucional, presentación de iniciativa, networking, recorrido técnico y Mesa de Diálogo 1 sobre brechas operativas", "Actividad 1: Matriz Diagnóstica de Necesidades Industriales y Brechas Técnicas de Planta (15 Pts)"),
        ("Módulo 2\n(Virtual 1 • 2h)", "Manejo y Desarrollo de Personal Técnico en Planta", "Atracción por competencias, descriptores operativos rigurosos, onboarding acelerado (30-60-90 días) y reducción de rotación", "Actividad 2: Descriptor de Puesto Técnico por Competencias y Plan de Onboarding 30-60-90 Días (15 Pts)"),
        ("Módulo 3\n(Virtual 2 • 2h)", "Liderazgo y Factor Humano en Cuadrillas de Trabajo", "Filosofía del Factor Humano, los 4 pilares operativos de Kinal, erradicación del maltrato en planta y fomento de seguridad psicológica", "Actividad 3: Código de Convivencia Operativa y Protocolo de Seguridad Psicológica y Cero Maltrato (15 Pts)"),
        ("Módulo 4\n(Virtual 3 • 2h)", "Fortalecimiento y Validación de Competencias: Nivel Técnico Superior (TSU)", "Mapeo de matrices técnicas operativas (saber, hacer, ser), el TSU como mecanismo de validación y respaldo industrial, y evaluación en puesto", "Actividad 4: Guía de Evaluación Práctica y Matriz de Validación Técnica bajo Estándar TSU (20 Pts)"),
        ("Módulo 5\n(Virtual 4 • 2h)", "Desarrollo de Mandos Medios y Supervisión de Primera Línea", "Herramientas para supervisores de piso, retroalimentación asertiva, micro-charlas de valores de inicio de turno e impacto en KPIs (OEE/SSO)", "Actividad 5: Plan de Coaching para Mandos Medios y Catálogo de 5 Micro-Charlas de Factor Humano (15 Pts)"),
        ("Módulo 6\n(Presencial 2 • 4h)", "Sistematización de Demandas, Acuerdos de Vinculación y Clausura", "Mesa Redonda Plenaria: Sistematización de demandas de la industria, convenios de cooperación técnica y entrega solemne de diplomas y distinciones", "Actividad 6: Sustentación Plenaria del Plan de Acción Empresarial y Firma de Acuerdos de Vinculación (20 Pts)")
    ]

    tbl_cron = doc.add_table(rows=7, cols=4)
    tbl_cron.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_cron.autofit = False
    tbl_cron.columns[0].width = Inches(1.3)
    tbl_cron.columns[1].width = Inches(1.8)
    tbl_cron.columns[2].width = Inches(2.0)
    tbl_cron.columns[3].width = Inches(1.4)
    set_table_borders(tbl_cron, color="CBD5E0", sz="4")

    hdr = tbl_cron.rows[0]
    for c in hdr.cells:
        set_cell_background(c, "003366")
    headers_txt = ["Módulo / Sesión", "Eje / Tema Principal", "Contenidos y Metodología Clave", "Actividad Formativa Evaluable"]
    for idx, text in enumerate(headers_txt):
        p = hdr.cells[idx].paragraphs[0]
        style_p(p, space_before=0, space_after=0)
        r = p.add_run(text)
        r.font.name = "Calibri"
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    for idx, (ses, mod, cont, prod) in enumerate(sesiones_info, start=1):
        row = tbl_cron.rows[idx]
        if "Presencial" in ses:
            for c in row.cells:
                set_cell_background(c, "EBF8FF")
        elif idx % 2 == 1:
            for c in row.cells:
                set_cell_background(c, "F7FAFC")
        for c_idx, val in enumerate([ses, mod, cont, prod]):
            cell = row.cells[c_idx]
            set_cell_margins(cell, top=45, bottom=45, left=55, right=55)
            p = cell.paragraphs[0]
            style_p(p, space_before=0, space_after=0)
            r = p.add_run(val)
            r.font.name = "Calibri"
            r.font.size = Pt(8)
            r.font.color.rgb = COLOR_DARK
            if c_idx in [0, 3] or "Presencial" in ses:
                r.font.bold = True

    doc.add_page_break()

    # =========================================================================
    # 2. MICRODISEÑO DIDÁCTICO DETALLADO DE LOS 6 MÓDULOS
    # =========================================================================
    h1_2 = doc.add_paragraph()
    style_heading(h1_2, "2. Microdiseño Didáctico Detallado por Módulos (6 Encuentros Formativos)", level=1)

    p_micro_intro = doc.add_paragraph()
    style_p(p_micro_intro, space_before=0, space_after=8)
    r = p_micro_intro.add_run("A continuación se desglosa la secuencia metodológica detallada para cada uno de los 6 Módulos Formativos (un módulo por sesión: 4 horas para las 2 jornadas presenciales en campus Kinal y 2 horas para las 4 sesiones virtuales semanales en Microsoft Teams):")
    r.font.name = "Calibri"
    r.font.size = Pt(9.5)
    r.font.color.rgb = COLOR_DARK

    sesiones_detalladas = [
        # MÓDULO 1
        ("Módulo 1: Necesidades Actuales de la Industria y Diagnóstico del Talento Operativo", 
         "Jornada Presencial Especial 1 (Campus Kinal)  |  4 Horas (240 min)",
         "Apertura Institucional, Presentación de la Iniciativa y Mesa de Diálogo 1: Necesidades de la Industria",
         "Conoce la visión formativa integral de Kinal, establece redes de contacto directivo y formaliza el diagnóstico inicial sobre las necesidades de cualificación y brechas técnicas operativas en las empresas.",
         "Apertura (30 min): Recepción protocolaria de los representantes empresariales en el Auditorio Ejecutivo de Fundación Kinal. Palabras de bienvenida a cargo de la Dirección de Vinculación y Dirección General. Encuadre de los objetivos del programa y dinámica de networking ejecutivo entre sectores productivos.",
         "Desarrollo (180 min con pausa activa de 20 min): Recorrido guiado por los talleres y laboratorios técnicos de Kinal (automatización, robótica, mecatrónica CNC, electrónica y redes). Observación de metodologías de aprendizaje práctico. Mesa de Diálogo 1: conversatorio abierto entre gerentes y autoridades de Kinal sobre los principales retos en la gestión de personal operativo y las brechas de competencias más críticas en la industria.",
         "Cierre (30 min): Plenaria de síntesis de la jornada, encuadre para la plataforma Microsoft Teams y Kinal.academy, y entrega de pautas para la Matriz Diagnóstica.",
         "Campus Fundación Kinal (Auditorio Ejecutivo y Complejo de Laboratorios Técnicos), guías impresas, estación de café.",
         "Actividad Formativa Evaluable 1: Matriz Diagnóstica de Necesidades Industriales y Brechas Técnicas de Planta (identificación de puestos operativos críticos y tecnologías emergentes). Ponderación: 15 Puntos."),

        # MÓDULO 2
        ("Módulo 2: Manejo y Desarrollo de Personal Técnico en Planta", 
         "Sesión Virtual 1 (Semana 1 — Microsoft Teams)  |  2 Horas (120 min)",
         "Atracción por Competencias, Inducción Técnica Acelerada (Onboarding) y Reducción de Rotación",
         "Aplica técnicas contemporáneas para el reclutamiento operativo basado en competencias demostrables y estructura planes de inducción técnica acelerada que mitiguen la rotación temprana.",
         "Apertura (15 min): Bienvenida en Teams y pregunta detonante: '¿Cuánto le cuesta realmente a su organización la rotación de un colaborador técnico en los primeros 90 días?'. Discusión en el chat interactivo.",
         "Desarrollo (90 min con pausa de 10 min): Por qué fracasan los descriptores de puesto tradicionales en piso operativo. Diseño de matrices de competencias demostrables (saber, saber hacer y saber ser). Estructuración de la curva de aprendizaje en 30-60-90 días. Taller en salas de Teams: rediseño de un puesto técnico crítico para la empresa del participante.",
         "Cierre (15 min): Socialización de matrices mejoradas en plenaria, conclusiones ejecutivas y pautas para subir el entregable a Kinal.academy.",
         "Microsoft Teams, salas grupales de Teams, Kinal.academy, plantilla de descriptores de puesto.",
         "Actividad Formativa Evaluable 2: Descriptor de Puesto Técnico por Competencias Demostrables y Plan de Onboarding Operativo en 30-60-90 Días. Ponderación: 15 Puntos."),

        # MÓDULO 3
        ("Módulo 3: Liderazgo y Factor Humano en Cuadrillas de Trabajo", 
         "Sesión Virtual 2 (Semana 2 — Microsoft Teams)  |  2 Horas (120 min)",
         "Dignidad en el Trabajo, el Principio del «Trabajo Bien Hecho» y Erradicación del Maltrato",
         "Formula políticas y protocolos de liderazgo humanista para erradicar el maltrato en cuadrillas de taller y promover la excelencia y seguridad psicológica en las operaciones.",
         "Apertura (15 min): Presentación del video testimonial institucional: 'El valor de la persona en el trabajo técnico'. Reflexión grupal sobre el trabajo como ámbito de dignidad y servicio.",
         "Desarrollo (90 min con pausa de 10 min): La filosofía del Factor Humano de Fundación Kinal y sus 4 pilares: Respeto a la Dignidad, Trabajo Bien Hecho (orden 5S, custodia de maquinaria y precisión moral), Espíritu de Servicio y Libertad Responsable. Análisis del caso: 'El costo oculto de la supervisión autoritaria en planta'. Cómo generar seguridad psicológica para que los operarios reporten averías e incidentes inmediatamente sin temor a represalias.",
         "Cierre (15 min): Síntesis de buenas prácticas de liderazgo, pautas para el protocolo de cero maltrato y consignas en Kinal.academy.",
         "Microsoft Teams, pizarras digitales, casos de estudio industrial de Kinal, Kinal.academy.",
         "Actividad Formativa Evaluable 3: Borrador de Código de Convivencia Operativa y Protocolo de Seguridad Psicológica y Cero Tolerancia al Maltrato en Planta. Ponderación: 15 Puntos."),

        # MÓDULO 4
        ("Módulo 4: Fortalecimiento y Validación de Competencias Técnicas: El Nivel Técnico Superior (TSU) como Respaldo Industrial", 
         "Sesión Virtual 3 (Semana 3 — Microsoft Teams)  |  2 Horas (120 min)",
         "Mapeo de Competencias de Planta, el TSU como Mecanismo de Validación y Evaluación Práctica en Puesto",
         "Diseña instrumentos objetivos para mapear y evaluar competencias técnicas operativas y articula el nivel Técnico Superior (TSU) como mecanismo de validación rigurosa y respaldo para la industria.",
         "Apertura (15 min): Sondeo interactivo: '¿Cómo evalúa hoy en día si un técnico domina el diagnóstico analítico de un PLC o sistema electromecánico antes de asignarle la línea crítica?'.",
         "Desarrollo (90 min con pausa de 10 min): Mapeo de competencias operativas bajo estándares internacionales (DQR). El Técnico Superior Universitario (TSU) como mecanismo riguroso de validación de competencias técnicas: acreditación de capacidades superiores en diagnóstico, interpretación de diagramas y cálculo aplicado. Por qué la industria requiere el respaldo del nivel superior técnico para cerrar la brecha entre ingeniería y piso de planta. Diseño de pruebas prácticas en banco de trabajo y el rol del mentor técnico (*Ausbilder*) para la transferencia en el puesto.",
         "Cierre (15 min): Presentación de la matriz de validación técnica de planta y asignación del entregable en Kinal.academy.",
         "Microsoft Teams, marco curricular TSU Kinal, matriz de competencias técnicas en Excel, Kinal.academy.",
         "Actividad Formativa Evaluable 4: Guía de Evaluación Práctica y Matriz de Validación Técnica de Planta bajo el Estándar de Competencias del Técnico Superior (TSU). Ponderación: 20 Puntos."),

        # MÓDULO 5
        ("Módulo 5: Desarrollo de Mandos Medios y Supervisión de Primera Línea", 
         "Sesión Virtual 4 (Semana 4 — Microsoft Teams)  |  2 Horas (120 min)",
         "Herramientas para Supervisores de Primera Línea, Feedback Asertivo y Micro-Charlas de Valores",
         "Estructura un plan de fortalecimiento para mandos medios que vincule el liderazgo formativo con indicadores operativos (OEE, SSO) y consolida el plan de acción empresarial.",
         "Apertura (15 min): Encuadre: el supervisor de taller como puente crítico entre la dirección estratégica y el piso operativo.",
         "Desarrollo (90 min con pausa de 10 min): Habilidades formativas para mandos medios: comunicación asertiva, retroalimentación correctiva sin humillar y manejo constructivo de conflictos en cuadrillas. Diseño y ejecución de 'Las Charlas de 10 Minutos de Factor Humano' antes de iniciar el turno. Correlación entre factor humano y KPIs de negocio (OEE, tasa de accidentes SSO y merma). Consolidación final de la propuesta de mejora técnica para la jornada de clausura.",
         "Cierre (15 min): Instrucciones protocolarias para la Jornada Presencial de Cierre, sustentación de planes y entrega de distinciones en campus Kinal.",
         "Microsoft Teams, guía de micro-charlas de valores, formato de consolidación de plan de acción, Kinal.academy.",
         "Actividad Formativa Evaluable 5: Plan de Coaching para Mandos Medios y Catálogo de 5 Micro-Charlas de Factor Humano para el Inicio de Turno (vinculadas a KPIs OEE/SSO). Ponderación: 15 Puntos."),

        # MÓDULO 6
        ("Módulo 6: Sistematización de Demandas Industriales, Acuerdos de Vinculación y Clausura", 
         "Jornada Presencial Especial 2 (Campus Kinal)  |  4 Horas (240 min)",
         "Mesa Redonda Plenaria: Sistematización de Necesidades Industriales, Diplomas y Reconocimientos",
         "Participa activamente en la sustentación del plan de acción empresarial, la retroalimentación de planes curriculares de Kinal y recibe el diploma de participación y reconocimiento corporativo.",
         "Apertura (20 min): Bienvenida protocolaria en Auditorio Ejecutivo por el Consejo Directivo y Directores Académicos de Fundación Kinal.",
         "Desarrollo (190 min con pausa de 20 min): Mesa Redonda Plenaria: 'Construyendo la Pertinencia Técnica de Guatemala'. Sustentación ejecutiva de los planes de acción y matrices diagnósticas por parte de los representantes empresariales. Diálogo abierto con las autoridades de Kinal para la retroalimentación de planes de estudio del nivel Técnico Superior y carreras técnicas. Formalización de acuerdos de cooperación institucional (bolsa de empleo prioritaria, semilleros y pasantías).",
         "Cierre (30 min): Acto solemne de clausura: Entrega de Diplomas de Participación Individual a los representantes empresariales y entrega de Reconocimientos Empresariales Especiales a las empresas aliadas. Brindis de honor y networking directivo.",
         "Auditorio Ejecutivo de Kinal, actas de evaluación, diplomas oficiales encuadernados, placas de reconocimiento empresarial, cóctel.",
         "Actividad Formativa Evaluable 6: Sustentación Plenaria del Plan de Acción Empresarial y Firma de Acuerdos de Vinculación Institucional. Ponderación: 20 Puntos.")
    ]

    for mod_nom, ses_form, tema_nom, obj_esp, act_ap, act_des, act_cie, rec_did, prod_obs in sesiones_detalladas:
        p_tit = doc.add_paragraph()
        style_heading(p_tit, mod_nom, level=2)

        tbl_s = doc.add_table(rows=7, cols=2)
        tbl_s.alignment = WD_TABLE_ALIGNMENT.CENTER
        tbl_s.autofit = False
        tbl_s.columns[0].width = Inches(1.8)
        tbl_s.columns[1].width = Inches(4.7)
        set_table_borders(tbl_s, color="CBD5E0", sz="4")

        s_rows = [
            ("Formato y Duración:", ses_form),
            ("Objetivo Específico:", obj_esp),
            ("Secuencia Didáctica — Apertura:", act_ap),
            ("Secuencia Didáctica — Desarrollo:", act_des),
            ("Secuencia Didáctica — Cierre:", act_cie),
            ("Recursos y Plataformas:", rec_did),
            ("Actividad Formativa Evaluable:", prod_obs)
        ]

        for r_idx, (etiq, cont) in enumerate(s_rows):
            row = tbl_s.rows[r_idx]
            if "Presencial" in ses_form:
                set_cell_background(row.cells[0], "EBF8FF")
            else:
                set_cell_background(row.cells[0], "F7FAFC")
            set_cell_margins(row.cells[0], top=50, bottom=50, left=70, right=70)
            set_cell_margins(row.cells[1], top=50, bottom=50, left=70, right=70)
            
            p0 = row.cells[0].paragraphs[0]
            style_p(p0, space_before=0, space_after=0)
            r0 = p0.add_run(etiq)
            r0.font.name = "Calibri"
            r0.font.size = Pt(8.5)
            r0.font.bold = True
            r0.font.color.rgb = COLOR_PRIMARY

            p1 = row.cells[1].paragraphs[0]
            style_p(p1, space_before=0, space_after=0)
            r1 = p1.add_run(cont)
            r1.font.name = "Calibri"
            r1.font.size = Pt(8.5)
            r1.font.color.rgb = COLOR_DARK
            if r_idx in [0, 6]:
                r1.font.bold = True

        p_sp = doc.add_paragraph()
        style_p(p_sp, space_before=2, space_after=4)

    doc.add_page_break()

    # =========================================================================
    # 3. INSTRUMENTOS DE EVALUACIÓN Y RÚBRICA MODULAR (100 PUNTOS)
    # =========================================================================
    h1_3 = doc.add_paragraph()
    style_heading(h1_3, "3. Instrumentos de Acreditación, Rúbrica Modular y Matriz Diagnóstica", level=1)

    add_callout(doc,
        "Para hacerse acreedor al Diploma de Participación Individual y al Reconocimiento Empresarial Institucional de Fundación Kinal, el representante debe cumplir con un mínimo del 80% de asistencia sincrónica y alcanzar una calificación mínima de 75 puntos sobre 100 en el consolidado de las 6 actividades formativas evaluables del programa.",
        bold_prefix="Requisitos de Acreditación Institucional:")

    p_rub = doc.add_paragraph()
    style_heading(p_rub, "3.1 Rúbrica Analítica de las 6 Actividades Formativas Evaluables (100 Puntos Totales)", level=2)

    rubrica_data = [
        ("Módulo 1: Matriz Diagnóstica de Necesidades y Brechas", "15 Puntos", "Identifica con precisión puestos críticos, desfases de cualificación operativa y tecnologías emergentes de su planta.", "Diagnóstico genérico o superficial sin datos específicos de la realidad técnica de planta (< 11.2 pts)."),
        ("Módulo 2: Descriptor por Competencias y Plan Onboarding", "15 Puntos", "Estructura un descriptor técnico riguroso por competencias observables (saber, hacer, ser) y plan de inducción a 30-60-90 días.", "Descriptor tradicional burocrático sin desglose de destrezas operativas ni curva de adaptación (< 11.2 pts)."),
        ("Módulo 3: Código de Convivencia y Protocolo Cero Maltrato", "15 Puntos", "Establece normas claras de seguridad psicológica, canales de reporte de averías sin temor y erradicación del maltrato en cuadrilla.", "Directrices teóricas sin aplicabilidad directa a las dinámicas y tensiones del taller operativo (< 11.2 pts)."),
        ("Módulo 4: Guía de Evaluación Práctica y Validación TSU", "20 Puntos", "Diseña una prueba práctica en banco de trabajo y utiliza el estándar Técnico Superior (TSU) como mecanismo de validación técnica rigurosa.", "Evaluación teórica tradicional sin pruebas de destreza manual o sin respaldo de competencias de nivel superior (< 15.0 pts)."),
        ("Módulo 5: Plan de Coaching y 5 Micro-Charlas de Factor Humano", "15 Puntos", "Diseña 5 micro-charlas operativas de valores para inicio de turno vinculadas a KPIs medibles (OEE, reducción de accidentes SSO y merma).", "Charlas desvinculadas de la operación diaria o sin conexión con la mejora de indicadores de planta (< 11.2 pts)."),
        ("Módulo 6: Sustentación Plenaria y Acuerdos de Vinculación", "20 Puntos", "Sustenta con solvencia el plan de acción en la mesa plenaria, aporta retroalimentación crítica a Kinal y formaliza acuerdos de vinculación.", "Participación pasiva en la plenaria sin aportes significativos a la vinculación escuela-empresa (< 15.0 pts).")
    ]

    tbl_rub = doc.add_table(rows=7, cols=4)
    tbl_rub.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_rub.autofit = False
    tbl_rub.columns[0].width = Inches(1.8)
    tbl_rub.columns[1].width = Inches(0.9)
    tbl_rub.columns[2].width = Inches(2.3)
    tbl_rub.columns[3].width = Inches(1.5)
    set_table_borders(tbl_rub, color="CBD5E0", sz="4")

    hdr_r = tbl_rub.rows[0]
    for c in hdr_r.cells:
        set_cell_background(c, "003366")
    for idx, text in enumerate(["Actividad Formativa / Módulo", "Puntos", "Desempeño Excelente (Estándar Kinal)", "Desempeño Insuficiente (< 75%)"]):
        p = hdr_r.cells[idx].paragraphs[0]
        style_p(p, space_before=0, space_after=0)
        r = p.add_run(text)
        r.font.name = "Calibri"
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    for idx, (crit, pond, exc, ins) in enumerate(rubrica_data, start=1):
        row = tbl_rub.rows[idx]
        if idx % 2 == 1:
            for c in row.cells:
                set_cell_background(c, "F7FAFC")
        for c_idx, val in enumerate([crit, pond, exc, ins]):
            cell = row.cells[c_idx]
            set_cell_margins(cell, top=50, bottom=50, left=60, right=60)
            p = cell.paragraphs[0]
            style_p(p, space_before=0, space_after=0)
            r = p.add_run(val)
            r.font.name = "Calibri"
            r.font.size = Pt(8)
            r.font.color.rgb = COLOR_DARK
            if c_idx in [0, 1]:
                r.font.bold = True

    p_bf = doc.add_paragraph()
    style_heading(p_bf, "3.2 Formato de Levantamiento: Matriz Diagnóstica de Necesidades Industriales", level=2)

    tbl_b_fmt = doc.add_table(rows=6, cols=2)
    tbl_b_fmt.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_b_fmt.autofit = False
    tbl_b_fmt.columns[0].width = Inches(2.3)
    tbl_b_fmt.columns[1].width = Inches(4.2)
    set_table_borders(tbl_b_fmt, color="CBD5E0", sz="4")

    formato_data = [
        ("Datos de la Empresa y Representante:", "Empresa: _______________________________ | Sector Productivo: _______________________\nRepresentante: ___________________________ | Cargo Directivo: _________________________"),
        ("Competencias Técnicas más Demandadas:", "Principales destrezas y conocimientos técnicos más difíciles de encontrar en el personal operativo: __________________________________________________________________"),
        ("Brechas en Mandos Medios y Factor Humano:", "Habilidades de liderazgo y humanas más necesarias en supervisores de planta (comunicación, respeto, trabajo bien hecho, etc.): _______________________________________________"),
        ("Tecnologías Emergentes en su Planta:", "Nuevas maquinarias, protocolos o tecnologías a incorporar en los próximos 1-3 años (automatización, IoT, robótica, redes, etc.): _______________________________________________"),
        ("Modalidad de Vinculación de Interés:", "[  ] Bolsa de Empleo Kinal    [  ] Semilleros de Formación Dual    [  ] Pasantías Técnicas    [  ] Capacitación a la Medida"),
        ("Validación y Entrega:", "Firma Representante Empresarial: _________________ | Vo.Bo. Dirección Vinculación Kinal: _________________")
    ]

    for idx, (campo, lineas) in enumerate(formato_data):
        row = tbl_b_fmt.rows[idx]
        set_cell_background(row.cells[0], "F7FAFC")
        set_cell_margins(row.cells[0], top=55, bottom=55, left=75, right=75)
        set_cell_margins(row.cells[1], top=55, bottom=55, left=75, right=75)

        p0 = row.cells[0].paragraphs[0]
        style_p(p0, space_before=0, space_after=0)
        r0 = p0.add_run(campo)
        r0.font.name = "Calibri"
        r0.font.size = Pt(9)
        r0.font.bold = True
        r0.font.color.rgb = COLOR_PRIMARY

        p1 = row.cells[1].paragraphs[0]
        style_p(p1, space_before=0, space_after=0)
        r1 = p1.add_run(lineas)
        r1.font.name = "Calibri"
        r1.font.size = Pt(9)
        r1.font.color.rgb = COLOR_DARK

    section = doc.sections[0]
    footer = section.footer
    footer_p = footer.paragraphs[0]
    style_p(footer_p, space_before=0, space_after=0)
    footer_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run_f = footer_p.add_run("Fundación Kinal | Programa Ejecutivo de Vinculación y Liderazgo — Dosificación Oficial")
    run_f.font.name = "Calibri"
    run_f.font.size = Pt(8.5)
    run_f.font.color.rgb = COLOR_SECONDARY

    for out_dir in [os.path.join("Cursos", "Talento_Tecnico"), "Talento_Tecnico"]:
        os.makedirs(out_dir, exist_ok=True)
        out_path = os.path.join(out_dir, "Dosificacion_y_Secuencia_Didactica_Talento_Tecnico_Kinal.docx")
        doc.save(out_path)
        print(f"Dosificación guardada con éxito en: {out_path}")

if __name__ == "__main__":
    generate_dosificacion_doc()
