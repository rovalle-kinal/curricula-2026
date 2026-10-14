import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

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
        r.font.size = Pt(12)
        r.font.color.rgb = RGBColor(0, 51, 102)
    elif level == 3:
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(2)
        r.font.size = Pt(10.5)
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
    run_title = title_p.add_run("Diplomado de Certificación Gerencial en Gestión Estratégica del Talento Técnico")
    run_title.font.name = "Calibri"
    run_title.font.size = Pt(18)
    run_title.font.bold = True
    run_title.font.color.rgb = COLOR_PRIMARY

    sub_p = doc.add_paragraph()
    style_p(sub_p, space_before=0, space_after=12)
    run_sub = sub_p.add_run("Programa Ejecutivo Oficial y Temario Analítico Detallado  |  Modalidad Híbrida Ejecutiva (4 Semanas Intensivas Consecutivas)\nFundación Kinal — Escuela Técnica Superior | 32 Horas Directas (16h Virtual Teams + 16h en 4 Sábados Consecutivos en Kinal) + 8h Proyecto Capstone | Umbral Aprobatorio: 75/100 Puntos")
    run_sub.font.name = "Calibri"
    run_sub.font.size = Pt(10)
    run_sub.font.italic = True
    run_sub.font.color.rgb = COLOR_SECONDARY

    add_callout(doc, 
        "«the ability and readiness of the individual to use knowledge, skills and personal, social and methodological competences and to behave in a considered, individual and socially responsible manner. Competence is understood in this sense as the comprehensive ability to act». El diplomado capacita a la alta dirección, líderes de talento y reclutadores para auditar competencias técnicas operativas del Técnico Superior Universitario (TSU), implementar modelos de formación dual y desplegar el «Factor Humano» de Fundación Kinal como un sistema de valores laicos pero profundamente humanos que erradica el maltrato en planta y eleva la excelencia productiva con el estándar del «trabajo bien hecho».", 
        bold_prefix="Definición de Competencia DQR e Ideario Kinal:")

    # ==========================================
    # 1. OBJETIVOS FORMATIVOS Y COMPETENCIAS
    # ==========================================
    h1_1 = doc.add_paragraph()
    style_heading(h1_1, "1. Competencia General y Resultados de Aprendizaje por Módulo", level=1)

    p_cg = doc.add_paragraph()
    style_p(p_cg, space_before=0, space_after=6)
    r = p_cg.add_run("Competencia General del Programa:\n"
                     "El participante formula e implementa estrategias integrales de atracción, evaluación, fidelización y desarrollo de talento técnico operativo en su organización, capitalizando las competencias del Técnico Superior Universitario (TSU) y el modelo de formación dual, diseñando programas internos de Factor Humano basados en valores laicos universales para erradicar el maltrato en planta y elevar la productividad y seguridad laboral con el estándar del «trabajo bien hecho».")
    r.font.name = "Calibri"
    r.font.size = Pt(9.5)
    r.font.bold = True
    r.font.color.rgb = COLOR_PRIMARY

    mod_comps = [
        ("Módulo 1 (Semana 1): La Brecha del Talento Operativo y el Retorno de Inversión del TSU", 
         "Comprende la estructura de cualificación DQR 5-6 del TSU frente a ingenieros y bachilleres, cuantificando el impacto financiero (ROI) de la estabilidad operativa y reducción de tiempos muertos en planta."),
        ("Módulo 2 (Semana 2): Reclutamiento por Competencias Técnicas y Sistemas de Formación Dual", 
         "Diseña descriptores de puesto basados en competencias demostrables y estructura semilleros de aprendizaje dual con planes de rotación y tutores empresariales (Ausbilder) en la propia empresa."),
        ("Módulo 3 (Semana 3): Cultura del Factor Humano: Valores Laicos, Dignidad y Clima Operativo", 
         "Implementa protocolos de liderazgo humanista en cuadrillas para erradicar el maltrato en taller/planta, promoviendo el «trabajo bien hecho», la inteligencia emocional y la seguridad psicológica."),
        ("Módulo 4 (Semana 4): Taller Directivo Capstone: Creación y Defensa del Programa Corporativo", 
         "Diseña y sustenta ante el tribunal directivo de Kinal un Plan Integral de Talento Técnico y Factor Humano con métricas de impacto (OEE, SSO, retención), alcanzando el umbral de certificación institucional (>= 75 pts).")
    ]

    for m_tit, m_desc in mod_comps:
        p_m = doc.add_paragraph()
        style_p(p_m, space_before=2, space_after=4)
        p_m.paragraph_format.left_indent = Inches(0.2)
        r_b = p_m.add_run(f"• {m_tit}: ")
        r_b.font.name = "Calibri"
        r_b.font.size = Pt(9.5)
        r_b.font.bold = True
        r_b.font.color.rgb = COLOR_PRIMARY
        r_d = p_m.add_run(m_desc)
        r_d.font.name = "Calibri"
        r_d.font.size = Pt(9.5)
        r_d.font.color.rgb = COLOR_DARK

    # ==========================================
    # 2. TEMARIO ANALÍTICO DETALLADO POR MÓDULOS (4 SEMANAS CONSECUTIVAS)
    # ==========================================
    h1_2 = doc.add_paragraph()
    style_heading(h1_2, "2. Temario Analítico Jerárquico y Prácticas Directivas (4 Semanas Consecutivas)", level=1)

    p_cal_note = doc.add_paragraph()
    style_p(p_cal_note, space_before=0, space_after=6)
    r = p_cal_note.add_run("Estructura de Impartición: El diplomado se imparte en 4 semanas continuas sin interrupciones. Cada semana comprende 2 sesiones virtuales sincrónicas en Microsoft Teams (Martes y Jueves, 19:00 a 21:00 hrs = 4 horas) y 1 sesión presencial vivencial en el campus de Fundación Kinal (Sábado consecutivo, 8:00 a 12:00 hrs = 4 horas), totalizando 8 horas directas semanales y 4 sábados consecutivos presenciales.")
    r.font.name = "Calibri"
    r.font.size = Pt(9.5)
    r.font.italic = True
    r.font.color.rgb = COLOR_SECONDARY

    # -------------------------------------------------------------
    # MODULO 1
    # -------------------------------------------------------------
    h2_m1 = doc.add_paragraph()
    style_heading(h2_m1, "MÓDULO 1: LA BRECHA DEL TALENTO OPERATIVO Y EL RETORNO DE INVERSIÓN DEL TSU (8 Horas — Semana 1)", level=2)

    temas_m1 = [
        ("1.1 Sesión Virtual 1 (Martes — 2 Horas en Teams): Radiografía del Empleo Técnico en Guatemala y el 'Missing Middle'", [
            "Análisis estructural del mercado laboral guatemalteco: escasez crítica de mandos medios técnicos calificados.",
            "Los costos ocultos de la mala asignación: fallas en arranques de línea, mantenimiento reactivo, piezas dañadas por impericia y sobrecostos por consultoría externa.",
            "La trampa de la subcualificación (peritos empíricos que no dominan diagnóstico sistemático) vs sobrecualificación (ingenieros que se frustran en la operación diaria y rotan a los 6 meses).",
            "La curva de rotación técnica en industrias de alimentos, plásticos, manufactura, telecomunicaciones, energía y agroindustria en Guatemala."
        ]),
        ("1.2 Sesión Virtual 2 (Jueves — 2 Horas en Teams): El Técnico Superior Universitario (TSU) y el Marco DQR 5-6", [
            "Origen y estructura curricular del TSU en Fundación Kinal: 3 años de formación técnica superior con más de 1,500 horas de prácticas intensivas en taller y laboratorio.",
            "El perfil del TSU: sólida fundamentación en cálculo, física aplicada, instrumentación, normas internacionales y control de calidad.",
            "Estructura del Marco Alemán de Cualificaciones (DQR): correspondencia de niveles 5 y 6 (Maestro Técnico / Meister, Bachelor Professional y Técnico Superior).",
            "Comparativa de roles: el Ingeniero diseña y planifica; el TSU supervisa, calibra, programa PLCs y soluciona averías en planta; el Operario ejecuta rutinas estándar.",
            "Caso de Negocio Directivo: modelado financiero del ROI del TSU (reducción de tiempos medios de reparación MTTR, disponibilidad de máquina y ahorro por menor rotación)."
        ]),
        ("1.3 Sesión Presencial 3 (SÁBADO 1 CONSECUTIVO EN KINAL — 4 Horas, 8:00 a 12:00 hrs)", [
            "Bienvenida institucional en auditorio ejecutivo de Kinal y dinámicas de networking directivo entre pares.",
            "Recorrido de inmersión técnica por los Laboratorios de TSU: demostraciones en vivo por parte de estudiantes en bancos de Automatización Siemens, Redes Cisco y Mecatrónica CNC.",
            "Mesa redonda directiva: 'Disección de una parada de planta': análisis financiero de casos reales de paradas no programadas aportados por las empresas participantes.",
            "Taller guiado: Construcción del Business Case preliminar de asignación del TSU y cálculo del ROI potencial en la organización del participante."
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

    # -------------------------------------------------------------
    # MODULO 2
    # -------------------------------------------------------------
    h2_m2 = doc.add_paragraph()
    style_heading(h2_m2, "MÓDULO 2: RECLUTAMIENTO POR COMPETENCIAS TÉCNICAS Y SISTEMAS DE FORMACIÓN DUAL (8 Horas — Semana 2)", level=2)

    temas_m2 = [
        ("2.1 Sesión Virtual 4 (Martes — 2 Horas en Teams): Reingeniería del Perfil de Puesto Técnico hacia Competencias Demostrables", [
            "De la descripción tradicional de requisitos burocráticos a la matriz de competencias operativas verificables.",
            "Desglose de competencias: saber (conocimiento normativo y físico), saber hacer (destreza manual e instrumental) y saber ser (actitud, seguridad y orden).",
            "Definición precisa de niveles de autonomía: desde el operario asistido hasta el supervisor con responsabilidad autónoma de turno.",
            "Redacción de descriptores de puesto atractivos para captar egresados técnicos de alto rendimiento."
        ]),
        ("2.2 Sesión Virtual 5 (Jueves — 2 Horas en Teams): Entrevistas Situacionales (STAR) y el Sistema Dual Escuela-Empresa", [
            "Por qué las entrevistas psicométricas tradicionales fallan al evaluar personal técnico de planta.",
            "Estructuración de la entrevista técnica situacional basada en el método STAR (Situación, Tarea, Acción, Resultado) adaptado a fallas de máquina.",
            "Rúbricas objetivas de evaluación para reclutadores no técnicos: cómo evaluar destreza sin ser especialista operativo.",
            "Concepto oficial del Sistema Dual: alternancia formativa, convenios de aprendizaje y marco legal guatemalteco.",
            "El rol del Tutor Empresarial (Ausbilder) y la pedagogía del trabajo en el puesto de trabajo (método de 4 pasos)."
        ]),
        ("2.3 Sesión Presencial 6 (SÁBADO 2 CONSECUTIVO EN KINAL — 4 Horas, 8:00 a 12:00 hrs)", [
            "Simulación en vivo: panel de reclutamiento directivo con entrevistas situacionales reales a estudiantes de último año de TSU de Kinal.",
            "Auditoría práctica de competencias en laboratorio: los gerentes observan y califican con rúbricas técnicas una prueba de comisionamiento en tiempo real.",
            "Taller de co-diseño: estructuración de un plan de semillero dual adaptado a las líneas de producción de las empresas de los participantes.",
            "Elaboración del entregable M2: Descriptor de puesto por competencias demostrables y propuesta de convenio de semillero dual."
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

    # -------------------------------------------------------------
    # MODULO 3
    # -------------------------------------------------------------
    h2_m3 = doc.add_paragraph()
    style_heading(h2_m3, "MÓDULO 3: CULTURA DEL «FACTOR HUMANO»: VALORES LAICOS, DIGNIDAD Y CLIMA EN PLANTA (8 Horas — Semana 3)", level=2)

    temas_m3 = [
        ("3.1 Sesión Virtual 7 (Martes — 2 Horas en Teams): Antropología del Factor Humano en Kinal y los Cuatro Pilares Operativos", [
            "El Factor Humano en Kinal: la persona en el centro de toda actividad técnica y productiva.",
            "El trabajo no como carga sino como ámbito de realización personal, servicio social y perfeccionamiento humano.",
            "Pilar 1: El «Trabajo Bien Hecho» (orden 5S, tolerancias exactas, custodia de maquinaria y orgullo por la obra terminada).",
            "Pilar 2: Respeto a la Dignidad de la Persona (erradicación del maltrato y autoritarismo en cuadrillas de taller).",
            "Pilar 3: Espíritu de Servicio y Solidaridad (cooperación interdepartamental mantenimiento-producción y apoyo al compañero novato).",
            "Pilar 4: Libertad Personal Responsable y Honradez (autonomía sin supervisión policiaca, puntualidad y veracidad en registros de calidad)."
        ]),
        ("3.2 Sesión Virtual 8 (Jueves — 2 Horas en Teams): Liderazgo en Cuadrillas, Seguridad Psicológica y Canales Éticos", [
            "De la supervisión por miedo al liderazgo formador de servicio basado en el ejemplo y la autoridad moral.",
            "Inteligencia emocional del mando medio: autodominio y manejo constructivo de la presión ante paradas de planta.",
            "Comunicación asertiva: retroalimentación correctiva firme sin humillar ni dañar la autoestima del colaborador.",
            "La seguridad psicológica como motor de productividad: operarios que reportan fallas y cuasi-accidentes sin temor a represalias.",
            "Protocolos corporativos contra el maltrato y canales seguros de denuncia ética (Whistleblowing) en áreas operativas."
        ]),
        ("3.3 Sesión Presencial 9 (SÁBADO 3 CONSECUTIVO EN KINAL — 4 Horas, 8:00 a 12:00 hrs)", [
            "Laboratorio de Liderazgo y Factor Humano: dramatización y resolución de dilemas éticos reales en planta (sobornos en compras, encubrimiento de fallas, maltrato a aprendices).",
            "Taller de diseño y simulación: 'Las Charlas de 10 Minutos de Factor Humano': cómo liderar reflexiones breves de valores antes de iniciar el turno de trabajo.",
            "Asesoría individualizada y feedback directivo de los facilitadores de Kinal para afinar el Proyecto Directivo Capstone de cada gerente.",
            "Elaboración del entregable M3: Protocolo corporativo de erradicación del maltrato y catálogo de 5 cápsulas operativas de Factor Humano."
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

    # -------------------------------------------------------------
    # MODULO 4
    # -------------------------------------------------------------
    h2_m4 = doc.add_paragraph()
    style_heading(h2_m4, "MÓDULO 4: TALLER DIRECTIVO CAPSTONE: CREACIÓN Y DEFENSA DEL PROGRAMA CORPORATIVO (8 Horas — Semana 4)", level=2)

    temas_m4 = [
        ("4.1 Sesión Virtual 10 (Martes — 2 Horas en Teams): Metodología de Despliegue Corporativo e Integración en la Operación", [
            "Etapas de implementación: diagnóstico cultural en planta, sensibilización de mandos medios, piloto en línea clave y escalamiento integral.",
            "Cómo dosificar formación en Factor Humano a personal técnico sin interrumpir los ritmos de producción continua.",
            "Integración de valores y competencias en la Inducción Corporativa y en las evaluaciones de desempeño semestrales.",
            "Guías de conversación para supervisores, material de planta y reconocimientos corporativos al 'Trabajo Bien Hecho'."
        ]),
        ("4.2 Sesión Virtual 11 (Jueves — 2 Horas en Teams): Cuadro de Mando Integral (KPIs), Alianzas Kinal y Ensayo Directivo", [
            "Correlación demostrable entre Factor Humano y KPIs: índice de frecuencia de accidentes (SSO), merma de producto y retrabajo.",
            "Impacto del perfil TSU en el OEE (Overall Equipment Effectiveness): disponibilidad, rendimiento y calidad de máquina.",
            "Ecosistema de vinculación de Kinal: convenios marco, acceso a la Bolsa de Egresados y homologación de competencias.",
            "Ensayo y retroalimentación previa en salas privadas de Teams para la sustentación final del Proyecto Capstone."
        ]),
        ("4.3 Sesión Presencial 12 (SÁBADO 4 CONSECUTIVO EN KINAL — 4 Horas: DEFENSA CAPSTONE, CERTIFICACIÓN Y CLAUSURA)", [
            "Instalación del Tribunal Evaluador Directivo conformado por autoridades académicas de Fundación Kinal y líderes empresariales invitados.",
            "Sustentación individual oral del Proyecto Directivo Capstone: 'Plan Estratégico de Talento Técnico y Cultura del Factor Humano' (15 min por participante + preguntas del tribunal).",
            "Evaluación con rúbrica ejecutiva institucional (Aprobación oficial: nota mínima de 75 puntos sobre 100).",
            "Acto solemne de clausura, entrega de certificados oficiales de Fundación Kinal y brindis de honor de networking directivo."
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

    # ==========================================
    # 3. REFERENCIAS Y FUENTES DE CONSULTA
    # ==========================================
    h1_3 = doc.add_paragraph()
    style_heading(h1_3, "3. Fuentes Bibliográficas y Marcos de Referencia", level=1)

    referencias = [
        ("BIBB / DQR:", "German Qualifications Framework for Lifelong Learning (DQR) — Niveles 5 y 6 (Meister, Bachelor Professional y Formación Dual)."),
        ("OIT / Cinterfor:", "Formación Profesional Dual y Alianzas Escuela-Empresa en América Latina: Modelos de Co-Formación."),
        ("Fundación Kinal:", "Ideario Institucional: El Trabajo como Vocación y Perfeccionamiento de la Persona."),
        ("Fundación Kinal:", "Pensum y Mapa Curricular del Técnico Superior Universitario (TSU) — Años Académicos 1 a 3."),
        ("Fundación Kinal:", "Guías y Manuales de Factor Humano y Formación Integral para Cuadrillas Técnicas."),
        ("Fundación Kinal:", "Normativa de Convivencia, Asistencia y Evaluación de la Escuela Técnica Superior.")
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
    run_f = footer_p.add_run("Fundación Kinal | Diplomado Gerencial en Gestión del Talento Técnico — Temario Oficial (4 Semanas Consecutivas)")
    run_f.font.name = "Calibri"
    run_f.font.size = Pt(8.5)
    run_f.font.color.rgb = COLOR_SECONDARY

    out_dir = os.path.join("Cursos", "Talento_Tecnico")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "Temario_Diplomado_Talento_Tecnico_Kinal.docx")
    doc.save(out_path)
    print(f"Temario guardado con éxito en: {out_path}")

if __name__ == "__main__":
    generate_temario_doc()
