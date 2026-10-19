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
        r.font.size = Pt(11.5)
        r.font.color.rgb = RGBColor(0, 51, 102)
    elif level == 3:
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after = Pt(2)
        r.font.size = Pt(10)
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

    # =========================================================================
    # ENCABEZADO INSTITUCIONAL
    # =========================================================================
    p_inst = doc.add_paragraph()
    style_p(p_inst, space_before=0, space_after=2)
    r_inst = p_inst.add_run("FUNDACIÓN KINAL — DIRECCIÓN DE VINCULACIÓN EMPRESARIAL")
    r_inst.font.name = "Calibri"
    r_inst.font.size = Pt(11)
    r_inst.font.bold = True
    r_inst.font.color.rgb = COLOR_PRIMARY

    p_tit = doc.add_paragraph()
    style_p(p_tit, space_before=0, space_after=4)
    r_tit = p_tit.add_run("DOSIFICACIÓN DIDÁCTICA Y SECUENCIACIÓN OPERATIVA:\nPROGRAMA EJECUTIVO EN GESTIÓN DEL TALENTO TÉCNICO, LIDERAZGO Y FACTOR HUMANO")
    r_tit.font.name = "Calibri"
    r_tit.font.size = Pt(16)
    r_tit.font.bold = True
    r_tit.font.color.rgb = COLOR_PRIMARY

    p_sub = doc.add_paragraph()
    style_p(p_sub, space_before=0, space_after=10)
    r_sub = p_sub.add_run("Cronograma Pedagógico Encuentro por Encuentro | 1 Mes de Duración | Modalidad Híbrida Ejecutiva (6 Encuentros: 2 Jornadas Presenciales Especiales en Kinal + 4 Sesiones Virtuales Semanales en Teams)")
    r_sub.font.name = "Calibri"
    r_sub.font.size = Pt(10.5)
    r_sub.font.italic = True
    r_sub.font.color.rgb = COLOR_SECONDARY

    add_callout(doc, 
        "«El aprender en el proceso del trabajo es base y a la vez objetivo de la acción formativa». Las 16 horas de contacto directo se estructuran a lo largo de un mes mediante 4 sesiones virtuales semanales de 2 horas en Microsoft Teams y 2 jornadas presenciales especiales de 4 horas en el campus de Fundación Kinal (Jornada Inicial de Apertura y Jornada de Cierre con Entrega de Diplomas y Reconocimientos). El programa genera un espacio de diálogo bidireccional industria-academia para identificar oportunidades de mejora y dotar a los líderes de equipos de herramientas prácticas en manejo de personal, liderazgo humanista y desarrollo de mandos medios. Umbral aprobatorio institucional: 75 puntos sobre 100.",
        bold_prefix="Organización Pedagógica Dual e Ideario Kinal:")

    # =========================================================================
    # 1. MATRIZ GENERAL CRONOLÓGICA DE LOS 6 ENCUENTROS
    # =========================================================================
    h1_1 = doc.add_paragraph()
    style_heading(h1_1, "1. Matriz General de Dosificación Cronológica (1 Mes — 6 Encuentros)", level=1)

    sesiones_info = [
        ("Jornada Especial 1 (Presencial)", "Apertura e Inmersión Kinal", "Apertura institucional, presentación de la iniciativa, networking y recorrido por laboratorios TSU", "Ficha diagnóstica inicial de expectativas y necesidades"),
        ("Sem. 1 / Sesión Virtual 1", "Manejo de Personal", "Atracción, reclutamiento técnico, inducción acelerada y reducción de costos por rotación ('Missing Middle')", "Descriptor de puesto técnico por competencias demostrables"),
        ("Sem. 2 / Sesión Virtual 2", "Liderazgo y Factor Humano", "Antropología de Kinal, los 4 pilares operativos, erradicación del maltrato en planta y seguridad psicológica", "Código de convivencia operativa y protocolo cero maltrato"),
        ("Sem. 3 / Sesión Virtual 3", "Competencias y Formación Dual", "Marco DQR 5-6, retorno de inversión (ROI) del TSU y esquemas de co-formación dual escuela-empresa", "Propuesta de semillero técnico dual y perfil de tutor Ausbilder"),
        ("Sem. 4 / Sesión Virtual 4", "Mandos Medios y Demanda Industrial", "Desarrollo del supervisor de primera línea, medición de KPIs (OEE, SSO) y demandas de Industria 4.0", "Catálogo de 5 micro-charlas de valores y borrador de diagnóstico"),
        ("Jornada Especial 2 (Presencial)", "Diálogo Industria y Clausura", "Plenaria de diálogo Kinal-Empresas, consolidación de necesidades técnicas y humanas, entrega de diplomas y reconocimientos", "Diplomas oficiales entregados y acuerdos de vinculación")
    ]

    tbl_matriz = doc.add_table(rows=len(sesiones_info) + 1, cols=4)
    tbl_matriz.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_matriz.autofit = False
    tbl_matriz.columns[0].width = Inches(1.4)
    tbl_matriz.columns[1].width = Inches(1.5)
    tbl_matriz.columns[2].width = Inches(2.2)
    tbl_matriz.columns[3].width = Inches(1.4)
    set_table_borders(tbl_matriz, color="CBD5E0", sz="4")

    hdr_m = tbl_matriz.rows[0]
    for c in hdr_m.cells:
        set_cell_background(c, "003366")
    headers_mat = ["Encuentro / Formato", "Eje Temático", "Contenido Central del Encuentro", "Producto Observable"]
    for idx, text in enumerate(headers_mat):
        p = hdr_m.cells[idx].paragraphs[0]
        style_p(p, space_before=0, space_after=0)
        r = p.add_run(text)
        r.font.name = "Calibri"
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    for idx, (ses, mod, cont, prod) in enumerate(sesiones_info, start=1):
        row = tbl_matriz.rows[idx]
        if "Presencial" in ses:
            for c in row.cells:
                set_cell_background(c, "EBF8FF")  # Resaltado azul para jornadas presenciales especiales
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
    # 2. MICRODISEÑO DIDÁCTICO DETALLADO DE LOS 6 ENCUENTROS
    # =========================================================================
    h1_2 = doc.add_paragraph()
    style_heading(h1_2, "2. Microdiseño Didáctico Detallado por Encuentro (6 Jornadas)", level=1)

    p_micro_intro = doc.add_paragraph()
    style_p(p_micro_intro, space_before=0, space_after=8)
    r = p_micro_intro.add_run("A continuación se desglosa la secuencia metodológica de cada encuentro formativo: 4 horas para las 2 jornadas presenciales especiales en campus Kinal y 2 horas para las 4 sesiones virtuales semanales en Microsoft Teams:")
    r.font.name = "Calibri"
    r.font.size = Pt(9.5)
    r.font.color.rgb = COLOR_DARK

    sesiones_detalladas = [
        # ENCUENTRO 1
        ("Jornada Presencial Especial 1 (Campus Kinal)", "Apertura Institucional e Inmersión Técnica",
         "Inauguración de la Iniciativa de Vinculación, Networking Directivo y Recorrido por Talleres TSU",
         "Conoce en profundidad la propuesta formativa integral de Kinal, establece vínculos de diálogo directivo y comprueba in situ la capacidad de los laboratorios de educación técnica superior.",
         "Apertura (30 min): Recepción protocolaria de los representantes empresariales en el Auditorio Ejecutivo de Fundación Kinal. Palabras de bienvenida a cargo de la Dirección de Vinculación y Dirección General. Encuadre del propósito del programa y dinámica de presentación de empresas participantes.",
         "Desarrollo (180 min con pausa activa de 20 min): Recorrido inmersivo guiado por los complejos de formación técnica: Laboratorios de Automatización Industrial y PLCs Siemens, Robótica, Mecatrónica CNC, Redes y Telecomunicaciones, Electrónica y Talleres de Mecánica. Estudiantes de último año de TSU realizan demostraciones operativas en vivo. Mesa de trabajo preliminar: diálogo abierto sobre la disponibilidad de personal técnico calificado y los desafíos del 'Missing Middle' en las empresas.",
         "Cierre (30 min): Plenaria de síntesis de la jornada, instrucciones para el acceso al aula virtual en Kinal.academy y la plataforma Microsoft Teams, y brindis de café de bienvenida.",
         "Campus Fundación Kinal (Auditorio Ejecutivo y Complejo de Laboratorios TSU), guías impresas, estación de café.",
         "Ficha diagnóstica preliminar de expectativas empresariales y registro formal de participación.", "4 Horas (240 min)"),

        # ENCUENTRO 2
        ("Sesión Virtual 1 (Semana 1 — Microsoft Teams)", "Manejo y Desarrollo de Personal Técnico",
         "Atracción, Inducción Técnica Acelerada y Retención de Talento Operativo",
         "Aplica técnicas contemporáneas para el reclutamiento por competencias y la estructuración de procesos de inducción que mitiguen la rotación prematura en planta.",
         "Apertura (15 min): Bienvenida en Teams y pregunta detonante: '¿Cuánto le cuesta realmente a su organización la rotación de un técnico en los primeros 90 días?'. Discusión en el chat interactivo.",
         "Desarrollo (90 min con pausa de 10 min): Exposición interactiva: por qué fracasan los perfiles de puesto tradicionales en el ámbito operativo. Metodología de descriptores por competencias demostrables (saber, saber hacer y saber ser). Estructuración de la curva de aprendizaje en 30-60-90 días. Trabajo en salas privadas de Teams: rediseño de un perfil técnico crítico para la empresa.",
         "Cierre (15 min): Socialización de perfiles mejorados, conclusiones ejecutivas y asignación de la lectura sobre Factor Humano en Kinal.academy.",
         "Microsoft Teams, salas grupales de Teams, Kinal.academy, plantilla de descriptores de puesto.",
         "Descriptor de puesto técnico por competencias demostrables y esquema de inducción acelerada.", "2 Horas (120 min)"),

        # ENCUENTRO 3
        ("Sesión Virtual 2 (Semana 2 — Microsoft Teams)", "Liderazgo y Factor Humano en Cuadrillas",
         "Dignidad en el Trabajo, el Principio del «Trabajo Bien Hecho» y Erradicación del Maltrato",
         "Formula políticas y protocolos de liderazgo humanista para erradicar el maltrato en cuadrillas de taller y promover la excelencia y seguridad psicológica.",
         "Apertura (15 min): Presentación del video testimonial: 'El sello del técnico de Kinal en la industria'. Reflexión sobre el trabajo como ámbito de dignidad y servicio.",
         "Desarrollo (90 min con pausa de 10 min): La filosofía del Factor Humano de Fundación Kinal y sus 4 pilares: Respeto a la Dignidad, Trabajo Bien Hecho (orden 5S, custodia de maquinaria y precisión moral), Espíritu de Servicio y Libertad Responsable. Análisis del caso: 'El costo oculto de la supervisión autoritaria en planta'. Cómo generar seguridad psicológica para que los operarios reporten averías e incidentes inmediatamente sin temor a represalias.",
         "Cierre (15 min): Síntesis de buenas prácticas de liderazgo, pautas para el protocolo de cero maltrato y preparación del siguiente eje en Kinal.academy.",
         "Microsoft Teams, pizarras digitales, casos de estudio industrial de Kinal, Kinal.academy.",
         "Borrador de Código de Convivencia Operativa y Protocolo de Tolerancia Cero al Maltrato en Planta.", "2 Horas (120 min)"),

        # ENCUENTRO 4
        ("Sesión Virtual 3 (Semana 3 — Microsoft Teams)", "Fortalecimiento de Competencias Técnicas y Formación Dual",
         "Estándares Internacionales (DQR 5-6), el Valor del TSU y Semilleros de Formación Dual",
         "Comprende la correspondencia de cualificaciones del Técnico Superior Universitario y diseña esquemas de semilleros duales con tutores de empresa (Ausbilder).",
         "Apertura (15 min): Sondeo interactivo: '¿Ha experimentado la frustración de contratar a un ingeniero para operar una máquina y que renuncie a los 6 meses?'. Debate inicial.",
         "Desarrollo (90 min con pausa de 10 min): Marco Alemán de Cualificaciones (DQR Niveles 5 y 6 / Meister). Comparativa de perfiles: Ingeniero (diseño y estrategia) vs TSU (supervisión, programación de PLCs y resolución de averías en campo) vs Operario empírico. Modelado del Retorno de Inversión (ROI): ahorro por reducción de MTTR y merma. Fundamentos del Sistema Dual en alternancia y el rol del tutor en planta (*Ausbilder*).",
         "Cierre (15 min): Pautas para la articulación de convenios de semilleros de aprendizaje con Fundación Kinal y consignas de trabajo.",
         "Microsoft Teams, calculadora de ROI en Excel, matriz comparativa DQR, Kinal.academy.",
         "Propuesta conceptual de semillero técnico dual y perfil del tutor empresarial de planta.", "2 Horas (120 min)"),

        # ENCUENTRO 5
        ("Sesión Virtual 4 (Semana 4 — Microsoft Teams)", "Desarrollo de Mandos Medios y Necesidades Actuales",
         "Herramientas para Supervisores de Primera Línea, KPIs Operativos y Demandas de la Industria",
         "Estructura un plan de fortalecimiento para mandos medios que vincule el factor humano con indicadores de productividad (OEE) y consolida la ficha de diagnóstico empresarial.",
         "Apertura (15 min): Encuadre: el supervisor de taller como articulador clave entre la estrategia gerencial y el piso operativo.",
         "Desarrollo (90 min con pausa de 10 min): Habilidades formativas para mandos medios: comunicación asertiva, retroalimentación correctiva sin humillar y manejo de conflictos en equipo. Diseño de 'Las Charlas de 10 Minutos de Factor Humano' antes de arrancar el turno. Nuevas tendencias tecnológicas (Industria 4.0, IoT y automatización) y su impacto en las destrezas requeridas. Revisión de la Ficha Diagnóstica de Necesidades de la Industria.",
         "Cierre (15 min): Instrucciones protocolarias para la Jornada Presencial de Cierre, entrega de diplomas y reconocimientos en campus Kinal.",
         "Microsoft Teams, guía de micro-charlas de valores, formato de diagnóstico de necesidades, Kinal.academy.",
         "Ficha de Diagnóstico de Necesidades Industriales completada y catálogo de 5 micro-charlas de Factor Humano.", "2 Horas (120 min)"),

        # ENCUENTRO 6
        ("Jornada Presencial Especial 2 (Campus Kinal)", "Diálogo Industria-Academia, Reconocimientos y Clausura",
         "Mesa Redonda Plenaria Kinal-Empresas, Entrega de Diplomas y Reconocimientos Institucionales",
         "Participa activamente en la sistematización de demandas formativas de la industria y recibe el diploma de participación y reconocimiento corporativo de Fundación Kinal.",
         "Apertura (20 min): Bienvenida protocolaria en Auditorio Ejecutivo por el Consejo Directivo y Directores Académicos de Kinal.",
         "Desarrollo (190 min con pausa de 20 min): Mesa Redonda Plenaria: 'Construyendo el futuro de la educación técnica en Guatemala'. Presentación de los hallazgos consolidados de las fichas diagnósticas: qué competencias técnicas y humanas demanda prioritariamente el sector industrial. Diálogo abierto con las autoridades de Kinal para la retroalimentación de planes de estudio y actualización de carreras. Firma de compromisos y convenios marco de vinculación (bolsa de empleo y semilleros duales).",
         "Cierre (30 min): Acto solemne de clausura: Entrega de Diplomas de Participación a los representantes empresariales y entrega de Reconocimientos Empresariales Especiales a las empresas aliadas. Brindis de honor y networking directivo.",
         "Auditorio Ejecutivo de Kinal, actas de evaluación, diplomas oficiales encuadernados, placas de reconocimiento empresarial, cóctel.",
         "Diplomas de Participación y Reconocimientos Empresariales oficialmente entregados (Acreditación institucional >= 75 Pts).", "4 Horas (240 min)")
    ]

    for ses_nom, eje_nom, tema_nom, obj_esp, act_ap, act_des, act_cie, rec_did, prod_obs, dur_txt in sesiones_detalladas:
        p_tit = doc.add_paragraph()
        style_heading(p_tit, f"{ses_nom} — {tema_nom}", level=2)

        tbl_s = doc.add_table(rows=7, cols=2)
        tbl_s.alignment = WD_TABLE_ALIGNMENT.CENTER
        tbl_s.autofit = False
        tbl_s.columns[0].width = Inches(1.8)
        tbl_s.columns[1].width = Inches(4.7)
        set_table_borders(tbl_s, color="CBD5E0", sz="4")

        s_rows = [
            ("Eje y Duración:", f"{eje_nom}  |  {dur_txt}"),
            ("Objetivo Específico:", obj_esp),
            ("Secuencia Didáctica — Apertura:", act_ap),
            ("Secuencia Didáctica — Desarrollo:", act_des),
            ("Secuencia Didáctica — Cierre:", act_cie),
            ("Recursos y Plataformas:", rec_did),
            ("Entregable y Evidencia:", prod_obs)
        ]

        for r_idx, (etiq, cont) in enumerate(s_rows):
            row = tbl_s.rows[r_idx]
            if "Presencial" in ses_nom or "Jornada" in ses_nom:
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
    # 3. INSTRUMENTOS DE EVALUACIÓN, RÚBRICA Y FICHA DIAGNÓSTICA
    # =========================================================================
    h1_3 = doc.add_paragraph()
    style_heading(h1_3, "3. Instrumentos de Acreditación, Rúbrica y Ficha Diagnóstica de la Industria", level=1)

    add_callout(doc,
        "Para recibir el Diploma de Participación Individual y el Reconocimiento Empresarial Institucional de Fundación Kinal, el representante debe cumplir con un mínimo del 80% de asistencia sincrónica y alcanzar una calificación mínima de 75 puntos sobre 100 en la entrega de sus productos aplicativos y participación en el diálogo de vinculación.",
        bold_prefix="Requisitos de Acreditación Institucional:")

    p_rub = doc.add_paragraph()
    style_heading(p_rub, "3.1 Rúbrica Analítica de Acreditación y Participación Ejecutiva (100 Puntos)", level=2)

    rubrica_data = [
        ("Participación en Sesiones y Aporte al Diálogo", "25 Puntos", "Participa activamente en las 2 jornadas presenciales y sesiones en Teams, compartiendo la realidad operativa y desafíos de su organización.", "Inasistencia injustificada o participación pasiva sin retroalimentación al diálogo (< 18.7 pts)."),
        ("Descriptor por Competencias y Plan de Inducción", "25 Puntos", "Redacta un descriptor técnico riguroso basado en competencias demostrables (saber, hacer, ser) y esquema de onboarding acelerado.", "Descriptor genérico basado en requisitos burocráticos sin criterios de evaluación técnica (< 18.7 pts)."),
        ("Protocolo de Factor Humano y Charlas Operativas", "25 Puntos", "Propone directrices claras de cero tolerancia al maltrato en planta, seguridad psicológica y diseña 5 micro-charlas de valores.", "Planteamiento abstracto sin aplicación práctica a las dinámicas de taller o cuadrilla (< 18.7 pts)."),
        ("Ficha de Diagnóstico de Necesidades Industriales", "25 Puntos", "Aporta información detallada sobre las tecnologías emergentes, competencias técnicas y humanas demandadas en su sector para retroalimentar a Kinal.", "Ficha incompleta, superficial o sin datos sobre las brechas reales de cualificación técnica (< 18.7 pts).")
    ]

    tbl_rub = doc.add_table(rows=5, cols=4)
    tbl_rub.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_rub.autofit = False
    tbl_rub.columns[0].width = Inches(1.8)
    tbl_rub.columns[1].width = Inches(1.0)
    tbl_rub.columns[2].width = Inches(2.2)
    tbl_rub.columns[3].width = Inches(1.5)
    set_table_borders(tbl_rub, color="CBD5E0", sz="4")

    hdr_r = tbl_rub.rows[0]
    for c in hdr_r.cells:
        set_cell_background(c, "003366")
    for idx, text in enumerate(["Criterio Evaluado", "Ponderación", "Desempeño Excelente (Estándar Kinal)", "Desempeño Insuficiente (< 75%)"]):
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
    style_heading(p_bf, "3.2 Ficha Diagnóstica: Levantamiento de Necesidades Actuales de la Industria", level=2)

    tbl_b_fmt = doc.add_table(rows=6, cols=2)
    tbl_b_fmt.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_b_fmt.autofit = False
    tbl_b_fmt.columns[0].width = Inches(2.3)
    tbl_b_fmt.columns[1].width = Inches(4.2)
    set_table_borders(tbl_b_fmt, color="CBD5E0", sz="4")

    formato_data = [
        ("Datos de la Empresa y Representante:", "Empresa: _______________________________ | Sector Productivo: _______________________\nRepresentante: ___________________________ | Cargo Directivo: _________________________"),
        ("Competencias Técnicas más Escasas:", "Principales dificultades técnicas observadas al contratar personal operativo (PLCs, calibración, mecánica, redes, etc.): __________________________________________________________________"),
        ("Brechas en Mandos Medios y Factor Humano:", "Habilidades humanas y de liderazgo más necesarias en supervisores de planta (comunicación, respeto, trabajo bien hecho, etc.): _______________________________________________"),
        ("Tecnologías Emergentes en su Planta:", "Nuevas maquinarias, protocolos o tecnologías a incorporar en los próximos 1-3 años (Industria 4.0, IoT, robótica, etc.): _____________________________________________________"),
        ("Modalidad de Vinculación de Interés:", "[  ] Semilleros de Formación Dual    [  ] Pasantías TSU    [  ] Bolsa de Empleo Kinal    [  ] Capacitación a la medida"),
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
    run_f = footer_p.add_run("Fundación Kinal | Programa Ejecutivo de Vinculación en Talento Técnico — Dosificación Oficial")
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
