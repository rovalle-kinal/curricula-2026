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

def style_p(p, space_before=0, space_after=4, line_spacing=1.15):
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = line_spacing

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

def generate_dosificacion_doc():
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
    # ENCABEZADO TÉCNICO INSTITUCIONAL
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
    style_p(p_tit, space_before=10, space_after=8)
    r_tit = p_tit.add_run("DOSIFICACIÓN CURRICULAR Y SECUENCIA DIDÁCTICA DETALLADA")
    r_tit.font.name = "Calibri"
    r_tit.font.size = Pt(20)
    r_tit.font.bold = True
    r_tit.font.color.rgb = COLOR_PRIMARY

    p_sub = doc.add_paragraph()
    style_p(p_sub, space_before=0, space_after=18)
    r_sub = p_sub.add_run("Cableado Estructurado y Redes de Cobre y Fibra Óptica (20 Sesiones de 4 Horas — 80 Horas)")
    r_sub.font.name = "Calibri"
    r_sub.font.size = Pt(12)
    r_sub.font.italic = True
    r_sub.font.color.rgb = COLOR_SECONDARY

    add_callout(doc, 
        "«El aprender en el proceso del trabajo es base y a la vez objetivo de la acción formativa». Las 80 horas pedagógicas se organizan en 20 sesiones de 240 minutos (4 horas), impartidas en dos días entre semana (Martes y Jueves de 17:30 a 21:30 hrs). Cada sesión contempla 20 minutos de receso; por tanto, el tiempo de actividad formativa neta por encuentro es de 220 minutos (73 horas y 20 minutos en total). Las sesiones conectan cada concepto técnico con el caso transversal del Edificio Corporativo Torre Empresarial (120 puntos Cat 6A, backbone fibra óptica y puesta a tierra TIA-607). Nota mínima aprobatoria institucional: 75 puntos sobre 100.",
        bold_prefix="Organización Pedagógica Dual e Ideario Kinal:")

    # =========================================================================
    # 1. MATRIZ GENERAL CRONOLÓGICA DE LAS 20 SESIONES
    # =========================================================================
    h1_1 = doc.add_paragraph()
    style_heading(h1_1, "1. Matriz General de Dosificación de las 20 Sesiones (80 Horas)", level=1)

    sesiones_info = [
        ("Sesión 1", "Módulo 1: Normas y Canalizaciones", "Normas ANSI/TIA-568, subsistemas y topología jerárquica del edificio corporativo", "Diagrama en estrella del edificio"),
        ("Sesión 2", "Módulo 1: Normas y Canalizaciones", "Espacios de telecomunicaciones según ANSI/TIA-569 (TR, ER, clima, UPS, ESD)", "Ficha técnica de diseño de TR"),
        ("Sesión 3", "Módulo 1: Normas y Canalizaciones", "Tubería conduit EMT: cálculo de factor de llenado (40%) y curvado manual", "Tramos de EMT doblados a 90°"),
        ("Sesión 4", "Módulo 1: Normas y Canalizaciones", "Charolas portacables tipo malla: soportes trapecio y bajadas en cascada a rack", "Charola suspendida y alineada"),
        ("Sesión 5", "Módulo 1: Normas y Canalizaciones", "Armado, nivelación, escuadrado y anclaje de rack abierto de 19'' (42U) y gabinete", "Rack 42U aplomado y anclado"),
        ("Sesión 6", "Módulo 2: Cobre y Aterrizaje", "Física del cable Cat 6A (F/UTP), código de colores y desforre sin marcar pares", "Pares desforrados sin muescas"),
        ("Sesión 7", "Módulo 2: Cobre y Aterrizaje", "Conectorización de tomas de pared (faceplates) con Keystone Jacks Cat 6A (T568B)", "Toma de pared Cat 6A rematada"),
        ("Sesión 8", "Módulo 2: Cobre y Aterrizaje", "Ponchado de Patch Panel modular de 24 puertos con barra trasera y peinado", "Patch panel de 24p rematado"),
        ("Sesión 9", "Módulo 2: Cobre y Aterrizaje", "Sistema de puesta a tierra TIA-607: barra TGB en rack y conductor verde 6 AWG", "Barra TGB instalada y probada"),
        ("Sesión 10", "Módulo 2: Cobre y Aterrizaje", "Tendido y peinado de mazo de 24 cables con peine guía y cinchos de velcro", "Mazo peinado estético con velcro"),
        ("Sesión 11", "Módulo 3: Fibra Óptica", "Física de la luz en fibra: Monomodo OS2 vs Multimodo OM4 y normas de seguridad", "Muestrario de cables identificado"),
        ("Sesión 12", "Módulo 3: Fibra Óptica", "Técnica de pelado en 3 pasos (chaqueta, búfer 900um, acrilato 250um) y limpieza", "Fibras desnudas listas para corte"),
        ("Sesión 13", "Módulo 3: Fibra Óptica", "Corte de precisión con cleaver de diamante (< 1°) y manejo de fusionadora", "Cortes inspeccionados en cleaver"),
        ("Sesión 14", "Módulo 3: Fibra Óptica", "Empalme por fusión por arco voltaico con pérdida < 0.05 dB y horneado de manguito", "Fusiones con pérdida < 0.05 dB"),
        ("Sesión 15", "Módulo 3: Fibra Óptica", "Acomodo en casete de bandeja ODF de 1U, radios de curvatura y prueba VFL láser", "Bandeja ODF de 1U con VFL OK"),
        ("Sesión 16", "Módulo 4: Certificación y As-Built", "Certificación de cobre Tier 1 con Fluke DSX: configuración TIA Cat 6A Perm Link", "Equipo Fluke calibrado y listo"),
        ("Sesión 17", "Módulo 4: Certificación y As-Built", "Análisis de parámetros de alta frecuencia: Wiremap, NEXT, Return Loss y causas", "Reporte de fallas analizado"),
        ("Sesión 18", "Módulo 4: Certificación y As-Built", "Certificación óptica Tier 1 con OPM y fuente de luz: cálculo de Loss Budget", "Medición Tier 1 en dB guardada"),
        ("Sesión 19", "Módulo 4: Certificación y As-Built", "Administración y rotulado TIA-606-D en cables, paneles y tomas con rotuladora", "Rotulado completo industrial"),
        ("Sesión 20", "Módulo 4: Certificación y As-Built", "EXAMEN DE CERTIFICACIÓN PROFESIONAL: Certificación de rack y dossier As-Built", "Acta aprobada (>=75 pts) y dossier")
    ]

    tbl_matriz = doc.add_table(rows=len(sesiones_info) + 1, cols=4)
    tbl_matriz.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_matriz.autofit = False
    tbl_matriz.columns[0].width = Inches(1.1)
    tbl_matriz.columns[1].width = Inches(1.8)
    tbl_matriz.columns[2].width = Inches(2.3)
    tbl_matriz.columns[3].width = Inches(1.3)
    set_table_borders(tbl_matriz, color="CBD5E0", sz="4")

    hdr_m = tbl_matriz.rows[0]
    for c in hdr_m.cells:
        set_cell_background(c, "003366")
    headers_mat = ["Sesión (4h)", "Módulo Formativo", "Contenido Central del Encuentro", "Producto Observable"]
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
        if idx % 2 == 1:
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
            if c_idx in [0, 3]:
                r.font.bold = True

    doc.add_page_break()

    # =========================================================================
    # 2. MICRODISEÑO DIDÁCTICO DETALLADO SESIÓN POR SESIÓN (20 SESIONES)
    # =========================================================================
    h1_2 = doc.add_paragraph()
    style_heading(h1_2, "2. Microdiseño Didáctico Detallado por Sesión (240 Minutos por Encuentro)", level=1)

    p_micro_intro = doc.add_paragraph()
    style_p(p_micro_intro, space_before=0, space_after=8)
    r = p_micro_intro.add_run("Cada una de las 20 sesiones formativas de 4 horas (240 minutos) se desglosa rigurosamente en tres momentos didácticos (Apertura 30 min, Desarrollo 160 min con Receso de 20 min, y Cierre 30 min), aplicando el principio del «trabajo bien hecho»:")
    r.font.name = "Calibri"
    r.font.size = Pt(10)
    r.font.color.rgb = COLOR_DARK

    sesiones_detalladas = [
        # MÓDULO 1
        ("Sesión 1", "Módulo 1: Normas y Canalizaciones", "Normas ANSI/TIA-568, Subsistemas y Topología Jerárquica",
         "Identifica los 6 subsistemas de cableado y traza el esquema en estrella jerárquica para el edificio corporativo de 3 niveles.",
         "Presentación del curso, ideario de Kinal y valor del trabajo bien hecho. Planteamiento del caso del Edificio Torre Empresarial (120 usuarios en 3 plantas).",
         "Exposición dialogada sobre normas TIA-568.0-E y TIA-568.1-E. Análisis de los 6 subsistemas (Área de Trabajo, Cableado Horizontal, Backbone, TR, ER y EF). Receso (20 min). Taller de diseño: cálculo de longitudes máximas (90 m de enlace permanente + 10 m de patch cords) sobre planos arquitectónicos del edificio.",
         "Revisión de esquemas de distribución principal (MDF) e intermedio (IDF). Preguntas de control y registro de la primera lección en la Bitácora Berichtsheft.",
         "Planos arquitectónicos del edificio, normas TIA-568 impresas, escalímetros, software de diseño.",
         "Diagrama esquemático en estrella jerárquica acotado con distancias y subsistemas identificados."),

        ("Sesión 2", "Módulo 1: Normas y Canalizaciones", "Espacios de Telecomunicaciones según ANSI/TIA-569 (TR y ER)",
         "Dimensiona los requerimientos de climatización, energía, UPS, pisos antiestáticos y madera ignífuga para los cuartos de telecomunicaciones.",
         "Pregunta generadora: ¿Qué ocurre con los switches de red si el cuarto de telecomunicaciones carece de aire acondicionado dedicado y supera los 35°C?",
         "Estudio de la norma ANSI/TIA-569-E: rango de temperatura (18°C a 24°C), humedad (30% a 55%), iluminación (> 500 lux) y alimentación eléctrica regulada con UPS. Tratamiento de paredes con madera contrachapada de 3/4 pulgada con retardante de llama. Receso (20 min). Práctica de distribución espacial: maqueta a escala de la ubicación de racks, pasillos de servicio y rutas de entrada.",
         "Verificación de distancias de mantenimiento alrededor del bastidor (mínimo 1 metro al frente y detrás). Registro en Berichtsheft.",
         "Normas TIA-569, cinta métrica, muestras de madera con pintura ignífuga, formatos de cálculo de BTU de climatización.",
         "Ficha técnica de diseño arquitectónico y ambiental del Cuarto de Telecomunicaciones (TR)."),

        ("Sesión 3", "Módulo 1: Normas y Canalizaciones", "Tubería Conduit EMT: Cálculo de Llenado (40%) y Doblado Manual",
         "Calcula la capacidad de tuberías conduit según la regla del 40% inicial de TIA-569 y ejecuta curvas a 90° y monturas con curvador manual.",
         "Análisis de problema en obra: ¿Por qué no se debe jalar cable UTP a través de una tubería llena a más del 60%?",
         "Cálculo matemático de área de sección transversal y aplicación de la regla del 40% (reserva del 60% para expansiones). Técnicas de curvado de tubería conduit EMT de 3/4'' y 1'': cálculo de deducción (take-up) para curvas a 90° y monturas de salto de obstáculos. Receso (20 min). Práctica en banco de tubos: doblado manual con hickey/bender y fijación con abrazaderas tipo uña.",
         "Inspección de curvas: ausencia de aplastamiento, arrugas o rebabas cortantes en los extremos del tubo con escariador. Registro en Berichtsheft.",
         "Tubos conduit EMT 3/4'', curvadores manuales de tubo, niveles de gota, cinta métrica, escariadores de metal.",
         "Tramos de tubería EMT doblados a 90° exactos con monturas ejecutadas y escariado verificado."),

        ("Sesión 4", "Módulo 1: Normas y Canalizaciones", "Charolas Portacables Tipo Malla: Soportes y Bajadas a Bastidor",
         "Instala tramos de charola portacables de hilo electrosoldado con soportes colgantes tipo trapecio y conformación de bajadas suaves hacia racks.",
         "Reflexión técnica: el radio de curvatura en la charola determina si el cable de alta frecuencia mantiene o pierde su certificación.",
         "Características de las bandejas portacables tipo malla (canastilla electrozincada): capacidad de carga, ventilación natural y corte de hilos con cizalla angular. Ensamble de curvas horizontales a 90° y bajadas en cascada tipo trompa de elefante. Receso (20 min). Montaje en taller: suspensión con varillas roscadas de 3/8'', fijación trapecio y alineación con tiralíneas.",
         "Comprobación de la continuidad mecánica y eléctrica de la charola. Prueba de ausencia de filos cortantes con cinta de protección plástica. Registro en Berichtsheft.",
         "Charolas de malla de 100 y 200 mm, varillas roscadas, uniones mecánicas, cizallas angulares, tiralíneas.",
         "Módulo de charola aérea suspendida, alineada y con bajada en cascada hacia el bastidor de telecomunicaciones."),

        ("Sesión 5", "Módulo 1: Normas y Canalizaciones", "Montaje, Nivelación, Escuadrado y Anclaje de Racks de 19 Pulgadas",
         "Ensambla, escuadra y ancla al piso un bastidor abierto de 19'' (42U) y un gabinete de pared de 12U con nivel de burbuja y torquímetro.",
         "Presentación del reto evaluativo del Módulo 1: garantizar que el esqueleto metálico esté perfectamente aplomado y listo para recibir equipamiento.",
         "Estándar EIA-310-D: numeración de Unidades de Rack (RU) de abajo hacia arriba. Ensamble de base, postes verticales y canales superiores. Nivelación de precisión en dos ejes con nivel de burbuja y calzas metálicas. Receso (20 min). Instalación de gabinete abatible de pared con taquetes expansivos y colocación de organizadores horizontales de 1U y 2U.",
         "Evaluación sumativa de Módulo 1 (rúbrica Kinal corte en 75/100). Verificación de solidez estructural, alineación vertical y registro en Berichtsheft.",
         "Racks abiertos de 19'' (42U), gabinetes de pared de 12U, llaves de tuercas, torquímetros, niveles de burbuja, organizadores tipo pasahilos.",
         "Rack de 42U y gabinete de pared ensamblados, aplomados y anclados cumpliendo especificaciones de torque."),

        # MÓDULO 2
        ("Sesión 6", "Módulo 2: Cobre y Aterrizaje", "Física del Cable Cat 6A, Código de Colores y Desforre Seguro",
         "Diferencia cables UTP, F/UTP y S/FTP y ejecuta el deschaquetado de cable Cat 6A sin rasgar mallas ni mellar el aislamiento de los pares.",
         "Inicio del Módulo 2. Pregunta orientadora: ¿Por qué en Cat 6A la cruceta central de plástico (spline) y el blindaje son vitales para alcanzar 500 MHz?",
         "Teoría de diafonía exógena (*Alien Crosstalk* - ANEXT) y blindaje F/UTP. Código de colores de los 4 pares trenzados. Diferencias entre cable de cobre sólido (horizontal) y multifilar (patch cords). Receso (20 min). Práctica de desforre: calibración del pelador rotativo de cable, corte de la cubierta exterior sin marcar el foil de aluminio ni el hilo de drenaje.",
         "Inspección de conductores bajo lupa de aumento: cero filamentos cortados o marcados. Registro en la Bitácora Berichtsheft.",
         "Bobinas de cable Cat 6A F/UTP 23 AWG 100% cobre, peladores rotativos de cable ajustables, lupas técnicas de taller.",
         "Muestras de cable Cat 6A desforradas limpiamente con hilo de drenaje y lámina de apantallamiento preservados."),

        ("Sesión 7", "Módulo 2: Cobre y Aterrizaje", "Conectorización de Tomas de Pared (Keystone Jacks Cat 6A)",
         "Remata módulos Keystone Jack Cat 6A bajo esquema T568B manteniendo el destrenzado menor a 13 mm (0.5 pulgadas) e integrando faceplates.",
         "La regla de oro del técnico profesional: cada milímetro de par destrenzado aumenta la pérdida de paradiafonía (NEXT) y degrada la señal.",
         "Comparación de esquemas de conexión T568A vs T568B. Técnica de inserción de pares en ranuras IDC (Insulation Displacement Contact). Uso de la herramienta de impacto con cuchilla 110 orientada hacia el exterior para corte simultáneo del excedente. Receso (20 min). Montaje en módulos de pared: colocación de faceplates angulados de 2 y 4 puertos con iconos identificadores.",
         "Verificación de la correcta inserción de cada conductor sin mordeduras dobles. Revisión del destrenzado con regla milimétrica. Registro en Berichtsheft.",
         "Módulos Keystone Jack Cat 6A apantallados, herramientas de impacto tipo punch down 110, faceplates, reglas milimétricas.",
         "Toma de usuario terminada en faceplate con dos Keystone Jacks Cat 6A rematados con destrenzado < 13 mm."),

        ("Sesión 8", "Módulo 2: Cobre y Aterrizaje", "Remate de Patch Panels Modulares de 24 Puertos y Barra Trasera",
         "Poncha y peina un patch panel modular apantallado de 24 puertos en 1U utilizando la barra de alivio de tensión trasera sin tensión mecánica.",
         "Caso de estudio: desconexiones aleatorias en una oficina por peso muerto de los cables colgados directamente sobre los pines de los conectores.",
         "Distribución de puertos en patch panels de 1U: agrupación en bloques de 6 puertos. Enrutamiento lateral de los mazos hacia la barra trasera de soporte. Fijación individual de cada cable mediante presillas o amarres de alivio de tensión. Receso (20 min). Práctica en banco: ponchado secuencial de los 24 puertos Cat 6A cuidando la simetría y longitud uniforme de los pares.",
         "Inspección visual del reverso del panel: alineación perfecta, sin cruces forzados ni tensión sobre las ranuras IDC. Registro en Berichtsheft.",
         "Patch panels modulares Cat 6A de 24 puertos de 1U con barra de soporte, herramientas punch down, cortadores al ras.",
         "Patch panel modular de 24 puertos rematado íntegramente con barras traseras instaladas y pares alineados."),

        ("Sesión 9", "Módulo 2: Cobre y Aterrizaje", "Sistema de Puesta a Tierra y Unión para Telecomunicaciones (TIA-607-D)",
         "Instala la barra secundaria TGB en el rack, conecta el cable verde de cobre 6 AWG y garantiza el drenaje equipotencial de pantallas F/UTP.",
         "Reflexión ética y técnica: una pantalla de cable apantallado que no se aterriza actúa como una antena receptora que empeora el ruido de la red.",
         "Estudio de la norma ANSI/TIA-607-D: barras TMGB, TGB y RGB. Calibre de conductores de unión (mínimo 6 AWG de cobre estañado o con aislamiento verde). Limpieza con lija y aplicación de grasa antioxidante en las uniones de cobre con el bastidor. Receso (20 min). Aterrizaje del patch panel apantallado hacia la barra del rack y medición de continuidad eléctrica con multímetro (< 0.1 ohm).",
         "Comprobación de continuidad de masa en todos los puertos del patch panel. Medición de resistencia equipotencial y registro en Berichtsheft.",
         "Barras de puesta a tierra TGB para rack, zapatas de compresión de dos barrenos, conductor 6 AWG verde, multímetros, grasa antioxidante.",
         "Barra TGB montada con zapatas de dos ojos, conductor 6 AWG conectado y continuidad de pantalla verificada."),

        ("Sesión 10", "Módulo 2: Cobre y Aterrizaje", "Tendido, Peinado en Mazos con Velcro y Comprobación de Wiremap",
         "Peina un mazo de 24 cables Cat 6A en el rack utilizando peine organizador y cinchos textiles de velcro, validando el mapa de cableado (Wiremap).",
         "El lema del trabajo bien hecho: prohibición estricta de cinchos plásticos de nylon que estrangulen o deformen los conductores de datos.",
         "Técnica de peinado con herramienta tipo peine (*cable comb*): eliminación de espirales y cruces internos. Agrupación en mazos simétricos de 12 o 24 cables. Colocación de cinchos de velcro cada 20 a 30 cm manteniendo tensión firme pero no estranguladora. Receso (20 min). Comprobación de continuidad de los 24 enlaces con tester digital: detección de circuitos abiertos, cortocircuitos y pares invertidos.",
         "Evaluación de Módulo 2: Rúbrica de conectorización, peinado y wiremap sin errores (nota mínima 75/100). Registro en Berichtsheft.",
         "Peines organizadores de cables, rollos de cinta textil de velcro, comprobadores digitales de cableado (wiremap testers).",
         "Mazo de 24 cables Cat 6A peinado estéticamente en rack con velcro y reporte de comprobación wiremap 100% OK."),

        # MÓDULO 3
        ("Sesión 11", "Módulo 3: Fibra Óptica", "Física de Transmisión Óptica, Tipos de Fibra y Bioseguridad",
         "Identifica fibras Monomodo (OS2) y Multimodo (OM4) y aplica los protocolos de bioseguridad para el manejo seguro de restos de fibra de vidrio.",
         "Inicio del Módulo 3. Advertencia de seguridad vital: el peligro invisible de los fragmentos de fibra de vidrio y la radiación láser no visible.",
         "Teoría óptica: índice de refracción, núcleo, revestimiento (*cladding* de 125 um) y acrilato (250 um). Fibras Monomodo (9 um núcleo / 1310-1550 nm) vs Multimodo (50 um núcleo / 850-1300 nm). Protocolos de seguridad: uso innegociable de gafas de policarbonato, tapete de trabajo negro y contenedor hermético de eliminación. Receso (20 min). Taller de reconocimiento: despiece de cables de estructura ajustada (*tight buffer*) y tubo holgado (*loose tube*).",
         "Revisión de puestos de trabajo con cinta adhesiva para verificar que no queden residuos de fibra sueltos. Registro en Berichtsheft.",
         "Muestras de cables ópticos OS2 y OM4, gafas de seguridad con protección lateral, tapetes de contraste negros, contenedores de desechos punzocortantes.",
         "Muestrario técnico clasificado de cables ópticos y protocolo de seguridad de taller firmado por el estudiante."),

        ("Sesión 12", "Módulo 3: Fibra Óptica", "Pelado en 3 Pasos, Desengrasado y Limpieza de Caras Terminales",
         "Ejecuta el pelado secuencial de fibra con pinza de 3 muescas y realiza la limpieza profunda de la fibra desnuda con alcohol isopropílico al 99%.",
         "Pregunta inicial: ¿Por qué una partícula de polvo de 1 micra puede bloquear totalmente una señal de luz en un núcleo de 9 micras?",
         "Ajuste y uso de la peladora de fibra de 3 muescas: muesca 1 para chaqueta exterior (2-3 mm), muesca 2 para búfer (900 um) y muesca 3 para acrilato (250 um). Movimiento recto y uniforme sin quebrar la fibra. Receso (20 min). Técnica de limpieza con toallitas secas sin pelusa empapadas con alcohol isopropílico de alta pureza. Inspección visual preliminar de limpieza.",
         "Comprobación táctil y acústica del chirrido limpio de la fibra desengrasada. Inspección de ausencia de residuos de acrilato. Registro en Berichtsheft.",
         "Peladoras de fibra óptica de precisión de 3 posiciones, toallitas kimwipes sin pelusa, dispensadores de alcohol isopropílico 99%.",
         "Hilos de fibra óptica pelados a 250/125 um y desengrasados sin fracturas ni microfisuras en el cladding."),

        ("Sesión 13", "Módulo 3: Fibra Óptica", "Corte de Precisión con Cleaver de Diamante y Manejo de Fusionadora",
         "Opera la cortadora de precisión obteniendo cortes perpendiculares con ángulo inferior a 1° y configura los parámetros de la fusionadora.",
         "Demostración de física: por qué una tijera o pinza tradicional aplasta y astilla la fibra impidiendo cualquier empalme por fusión.",
         "Mecánica del cleaver de disco de diamante: tensión controlada y fractura guiada a 90° exactos. Longitud de corte estandarizada (10 mm a 16 mm). Estructura de la máquina de empalme por fusión: cámaras de alineación por perfil de núcleo (PAS), electrodos y ranuras en V. Receso (20 min). Práctica en banco: colocación de fibras en las guías, verificación del ángulo de corte en pantalla (< 1.0°) y arco de prueba.",
         "Inspección en pantalla de la fusionadora de los ejes X y Y de ambas fibras. Descarte de cortes deficientes con burbujas o labios. Registro en Berichtsheft.",
         "Cortadoras de precisión de fibra óptica (cleavers), fusionadoras por alineación de núcleo con pantalla LCD, kits de calibración de electrodos.",
         "Fibras cortadas a 90° (+/- 0.5°) colocadas en las ranuras en V de la fusionadora listas para arco voltaico."),

        ("Sesión 14", "Módulo 3: Fibra Óptica", "Empalme por Fusión por Arco Voltaico y Horneado de Manguitos",
         "Ejecuta empalmes por fusión entre fibras monomodo OS2 y pigtails LC con atenuación estimada < 0.05 dB y hornea el manguito termocontráctil.",
         "El estándar de excelencia del trabajo bien hecho: una fusión profesional debe ser casi invisible en la pantalla de la máquina y tener mínima pérdida.",
         "Colocación previa del manguito termo-retráctil (*fusen* con varilla de acero). Ejecución del ciclo automático: descarga de limpieza, arco de fusión principal y prueba mecánica de tracción (tensión de 200g). Estimación matemática de pérdida en dB. Receso (20 min). Transferencia cuidadosa al horno térmico integrado y activación del ciclo de contracción a 180°C durante 30 segundos sin burbujas de aire.",
         "Inspección del manguito enfriado: varilla de acero alineada y fibra protegida sin dobleces. Registro de la atenuación de cada empalme en Berichtsheft.",
         "Fusionadoras automáticas, manguitos termocontráctiles de 40 y 60 mm, pigtails LC Monomodo OS2, pinzas de transferencia.",
         "Conjunto de 4 empalmes por fusión horneados con atenuación estimada individual inferior a 0.05 dB."),

        ("Sesión 15", "Módulo 3: Fibra Óptica", "Acomodo en Bandejas ODF, Radios de Curvatura y Verificación VFL",
         "Acomoda los empalmes en el casete de una bandeja ODF de 1U respetando el radio de curvatura (> 30 mm) y prueba continuidad con láser rojo VFL.",
         "Problema de planta: una fusión perfecta de 0.02 dB se quiebra o atenúa a 5 dB al forzar el cable dentro de la bandeja de empalmes.",
         "Estructura de la bandeja distribuidora de fibra óptica (ODF de 1U) para rack de 19''. Ruteo en bucle circular de los tubos holgados y pigtails en el casete de empalmes. Instalación de acopladores dúplex LC en el frontal del panel. Receso (20 min). Práctica de acomodo prolijo con fijación de manguitos en las peinetas plásticas del casete. Prueba de continuidad visual con localizador de fallas (VFL láser rojo de 650 nm).",
         "Evaluación de Módulo 3: Rúbrica de fusión, acomodo en casete ODF y prueba visual de continuidad (nota mínima 75/100). Registro en Berichtsheft.",
         "Bandejas de fibra ODF de 1U de rack, casetes de empalme, acopladores dúplex LC, localizadores visuales de fallas (VFL láser 650 nm).",
         "Bandeja ODF de 1U ensamblada con 4 fusiones acomodadas en casete y emisión de luz roja continua en acopladores LC."),

        # MÓDULO 4
        ("Sesión 16", "Módulo 4: Certificación y As-Built", "Certificación Tier 1 de Cobre con Fluke DSX: Límites TIA Cat 6A",
         "Configura el analizador Fluke Networks DSX para enlace permanente Cat 6A, calibra adaptadores y ejecuta la certificación de enlaces.",
         "Inicio del Módulo 4. ¿Por qué un simple tester de continuidad de Q100 no sirve para certificar una red corporativa de 10 Gigabits?",
         "Diferencias entre Enlace Permanente (*Permanent Link* de 90 m con adaptadores de precisión) y Canal (*Channel* de 100 m con patch cords). Configuración en el software del Fluke DSX: selección de norma (TIA Cat 6A Permanent Link), tipo de cable y factor de velocidad de propagación nominal (NVP). Receso (20 min). Conexión de la unidad principal y remota a las tomas de red y ejecución del autotest (tiempo de prueba: 8 segundos).",
         "Interpretación en pantalla del resultado global: «Pass» (Pasa) vs «Fail» (Falla). Guardado de reportes con ID unívoco. Registro en Berichtsheft.",
         "Certificador Fluke Networks DSX-5000 / DSX-8000 con adaptadores de Enlace Permanente Cat 6A, cables de calibración, software LinkWare.",
         "Equipo Fluke configurado y calibrado, con primeras pruebas de enlace permanente guardadas en memoria interna."),

        ("Sesión 17", "Módulo 4: Certificación y As-Built", "Análisis de Parámetros de Alta Frecuencia y Diagnóstico de Fallas",
         "Analiza gráficas de NEXT, Return Loss e Insertion Loss y localiza averías en el dominio del tiempo con herramientas TDNXT y TDR.",
         "Reflexión ética sobre la certificación: adulterar o cambiar los límites de prueba en el equipo para lograr un 'Pass' artificial es fraude profesional.",
         "Interpretación profunda de parámetros críticos: Paradiafonía cercana (NEXT y PS-NEXT) por exceso de destrenzado; Pérdida de retorno (Return Loss) por aplastamiento o curvatura aguda; Pérdida de inserción por longitud o cable CCA. Receso (20 min). Taller de Troubleshooting: uso del reflectómetro de dominio de tiempo (TDR y TDNXT) para ubicar a qué distancia métrica exacta (ej. a 2.4 metros del jack) ocurrió la falla inducida.",
         "Corrección física del enlace fallido y repetición del test hasta obtener un «Pass» legítimo con margen positivo (> 3 dB). Registro en Berichtsheft.",
         "Certificadores Fluke DSX con trazas de diagnóstico, enlaces de prueba con fallas inducidas (destrenzado, empalme, cincho plástico apretado).",
         "Reporte de diagnóstico técnico con gráficas TDNXT y TDR analizadas y enlace corregido con certificación aprobatoria."),

        ("Sesión 18", "Módulo 4: Certificación y As-Built", "Certificación Óptica Tier 1: Medición de Atenuación con OPM y Loss Budget",
         "Calcula el presupuesto de pérdida óptica admisible (*Optical Loss Budget*) y mide la atenuación total en dB con fuente de luz y medidor OPM.",
         "Planteamiento: ¿Cuántos decibelios (dB) de luz es aceptable perder en un enlace troncal de 300 metros con 2 fusiones y 2 conectores LC?",
         "Cálculo matemático del Loss Budget según norma TIA-568.3: Atenuación del cable (dB/km) + Conectores (0.75 dB por par) + Empalmes (0.3 dB por fusión). Establecimiento de referencia óptica con método de 1 puente de grado referencia. Receso (20 min). Medición bidireccional de atenuación en 850 nm y 1300 nm (Multimodo) o 1310 nm y 1550 nm (Monomodo). Comparación del valor medido frente al límite calculado.",
         "Verificación de margen positivo (*Headroom* en dB). Registro de mediciones en la Bitácora Berichtsheft.",
         "Medidores de potencia óptica (OPM), fuentes de luz monomodo y multimodo calibradas, puentes de prueba de referencia (TRC), adaptadores de acoplamiento.",
         "Hoja de cálculo de Loss Budget y reporte de certificación Tier 1 de fibra óptica con atenuación total en dB validada."),

        ("Sesión 19", "Módulo 4: Certificación y As-Built", "Administración ANSI/TIA-606-D, Rotulado Industrial y Planos As-Built",
         "Aplica el sistema de identificación alfanumérico TIA-606-D rotulando cables, paneles y faceplates con rotuladora industrial y actualiza planos As-Built.",
         "El orden es dinero: un técnico de soporte tarda 4 horas en hallar un punto ciego sin rotular vs 30 segundos en una red con estándar TIA-606.",
         "Esquema de nomenclatura normalizado: Identificador de piso, cuarto de telecomunicaciones, rack, patch panel y puerto (ej. `1A-TR1-PP01-14` a `1A-WA01-14`). Impresión de etiquetas autolaminadas de vinil para cables y etiquetas de poliéster para puertos de panel y faceplates. Receso (20 min). Levantamiento y actualización de planos arquitectónicos «As-Built» reflejando las rutas de canalización reales.",
         "Inspección de rotulado: legibilidad, alineación recta y resistencia al roce. Revisión de planos y tablas de parcheo (*Patching Schedule*).",
         "Rotuladoras industriales de transferencia térmica (Brady / Brother / Dymo Industrial), casetes de etiquetas de vinil y poliéster, planos As-Built.",
         "Sistema completo de cableado rotulado bajo norma ANSI/TIA-606-D y planos arquitectónicos As-Built actualizados."),

        ("Sesión 20", "Módulo 4: Certificación y As-Built", "EXAMEN DE CERTIFICACIÓN PROFESIONAL: Auditoría de Rack y Sustentación",
         "Demuestra la capacidad integral de acción técnica certificando la infraestructura de rack, resolviendo averías inducidas y sustentando el dossier técnico (>=75 pts).",
         "Apertura del examen oficial de certificación técnica. Sorteo de estaciones de trabajo y entrega de pliego de requerimientos corporativos.",
         "Prueba práctica individual de certificación profesional (tiempo límite 120 minutos): el estudiante debe certificar los enlaces de cobre y fibra de su bastidor, diagnosticar y corregir 2 fallas inducidas por el tribunal en menos de 45 minutos (ej. par invertido y atenuación excesiva). Receso (20 min). Exportación de la base de datos de enlaces con el software Fluke LinkWare y generación de certificados en PDF.",
         "Sustentación oral del dossier técnico As-Built y entrega de la Bitácora Berichtsheft completa. Calificación final institucional sobre 100 puntos.",
         "Racks departamentales completos, certificadores Fluke DSX, kits de herramientas, software Fluke LinkWare, actas de evaluación Kinal.",
         "Acta oficial de evaluación de certificación técnica aprobada (>= 75 puntos) y dossier técnico As-Built completo entregado.")
    ]

    for s_info in sesiones_detalladas:
        ses_num, mod_name, tit, ind, ap, des, cie, rec, prod = s_info
        
        h2_s = doc.add_paragraph()
        style_heading(h2_s, f"{ses_num}: {tit}", level=2)

        p_mod = doc.add_paragraph()
        style_p(p_mod, space_before=0, space_after=4)
        r = p_mod.add_run(f"Unidad: {mod_name}")
        r.font.name = "Calibri"
        r.font.size = Pt(9.5)
        r.font.bold = True
        r.font.color.rgb = COLOR_SECONDARY

        # Tabla de Microdiseño
        tbl_s = doc.add_table(rows=6, cols=2)
        tbl_s.alignment = WD_TABLE_ALIGNMENT.CENTER
        tbl_s.autofit = False
        tbl_s.columns[0].width = Inches(1.8)
        tbl_s.columns[1].width = Inches(4.7)
        set_table_borders(tbl_s, color="CBD5E0", sz="4")

        filas_data = [
            ("Indicador de Logro:", ind),
            ("Apertura (30 min):", ap),
            ("Desarrollo (160 min):", des),
            ("Cierre (30 min):", cie),
            ("Recursos y Equipos:", rec),
            ("Producto Observable:", prod)
        ]

        for r_idx, (etiq, cont) in enumerate(filas_data):
            row = tbl_s.rows[r_idx]
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
            if r_idx in [0, 5]:
                r1.font.bold = True

        p_sp = doc.add_paragraph()
        style_p(p_sp, space_before=2, space_after=4)

    doc.add_page_break()

    # =========================================================================
    # 3. INSTRUMENTOS INSTITUCIONALES DE EVALUACIÓN Y BITÁCORA
    # =========================================================================
    h1_3 = doc.add_paragraph()
    style_heading(h1_3, "3. Instrumentos de Evaluación Institucional y Bitácora Berichtsheft", level=1)

    add_callout(doc,
        "La evaluación en taller se rige por la rúbrica analítica institucional de Fundación Kinal. Todo estudiante debe alcanzar al menos 75 puntos sobre 100 para aprobar cada práctica y la certificación final, demostrando apego incondicional al principio del «trabajo bien hecho».",
        bold_prefix="Criterio de Evaluación y Umbral de Aprobación:")

    p_rub = doc.add_paragraph()
    style_heading(p_rub, "3.1 Rúbrica Analítica de Desempeño Práctico en Taller de Telecomunicaciones (100 Puntos)", level=2)

    rubrica_data = [
        ("Seguridad Ocupacional y Bioseguridad en Fibra", "15 Puntos", "Uso estricto de EPP dieléctrico, contenedor sellado para restos de fibra de vidrio y cero exposición visual a puertos ópticos.", "Omite el uso de gafas, arroja residuos de fibra al suelo o desconoce normas de seguridad (< 11.2 pts)."),
        ("Calidad Técnica de Conectorización y Peinado", "30 Puntos", "Destrenzado < 13 mm, sujeción exclusiva con cinchos de velcro, peinado simétrico en rack y terminación de jacks sin pares abiertos.", "Destrenzado excesivo, uso de cinchos plásticos apretados o deformación de conductores (< 22.5 pts)."),
        ("Preparación, Corte y Fusión de Fibra Óptica", "20 Puntos", "Corte perpendicular con cleaver (< 1°), empalme por fusión con atenuación medida < 0.05 dB y horneado de manguito sin burbujas.", "Ángulos de corte deficientes, atenuación superior a 0.1 dB o fractura de fibra en casete (< 15 pts)."),
        ("Certificación Instrumental Fluke y Troubleshooting", "25 Puntos", "Configuración exacta de límites TIA, interpretación de gráficas TDNXT/TDR y corrección de fallas inducidas en el tiempo límite.", "Incapacidad para interpretar parámetros, modificación indebida de límites o demora excesiva (< 18.7 pts)."),
        ("Rotulado TIA-606, Orden (5S) y Bitácora Berichtsheft", "10 Puntos", "Identificación alfanumérica indeleble en todos los puntos, puesto de trabajo impecable y bitácora técnica al día.", "Etiquetado ausente o improvisado con cinta adhesiva, desorden en mesa o bitácora incompleta (< 7.5 pts).")
    ]

    tbl_rub = doc.add_table(rows=6, cols=4)
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
    for idx, text in enumerate(["Criterio Evaluado", "Ponderación", "Desempeño Excelente (Trabajo Bien Hecho)", "Desempeño Insuficiente (< 75%)"]):
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
    style_heading(p_bf, "3.2 Formato de Registro Semanal de la Bitácora Berichtsheft", level=2)

    tbl_b_fmt = doc.add_table(rows=6, cols=2)
    tbl_b_fmt.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_b_fmt.autofit = False
    tbl_b_fmt.columns[0].width = Inches(2.2)
    tbl_b_fmt.columns[1].width = Inches(4.3)
    set_table_borders(tbl_b_fmt, color="CBD5E0", sz="4")

    formato_data = [
        ("Datos Generales:", "Estudiante: _______________________ | Carné: _________ | Sesión N°: ____ | Fecha: ________"),
        ("Actividad Práctica Ejecutada:", "Descripción del enlace permanente Cat 6A ponchado, fusión óptica realizada o rack ensamblado."),
        ("Normas Técnicas Aplicadas:", "Estándares ANSI/TIA (568, 569, 606, 607) verificados, distancias y radios de curvatura."),
        ("Parámetros Instrumentales Medidos:", "NEXT (dB), Return Loss (dB), Longitud (m), Wiremap, Atenuación de Fusión (dB) con Fluke/OPM."),
        ("Dificultad Superada («Trabajo Bien Hecho»):", "Registro de averías o dificultades técnicas resueltas durante el encuentro y lección aprendida."),
        ("Firma del Participante y Vo.Bo. Docente:", "Firma Estudiante: ___________________  |  Vo.Bo. Instructor Kinal: ___________________")
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
    run_f = footer_p.add_run("Fundación Kinal | Cableado Estructurado y Redes de Cobre/Fibra — Dosificación Oficial")
    run_f.font.name = "Calibri"
    run_f.font.size = Pt(8.5)
    run_f.font.color.rgb = COLOR_SECONDARY

    out_dir = os.path.join("Cursos", "Cableado_Estructurado")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "Dosificacion_y_Secuencia_Didactica_Cableado_Estructurado_Kinal.docx")
    doc.save(out_path)
    print(f"Dosificación guardada con éxito en: {out_path}")

if __name__ == "__main__":
    generate_dosificacion_doc()
