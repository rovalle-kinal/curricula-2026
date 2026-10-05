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
    r_sub = p_sub.add_run("Automatización y Control Eléctrico Industrial con PLC y Variadores de Frecuencia (20 Sesiones de 6 Horas — 120 Horas Formativas)")
    r_sub.font.name = "Calibri"
    r_sub.font.size = Pt(12)
    r_sub.font.italic = True
    r_sub.font.color.rgb = COLOR_SECONDARY

    add_callout(doc, 
        "«El aprender en el proceso del trabajo es base y a la vez objetivo de la acción formativa». Las 120 horas formativas se estructuran en 20 sesiones presenciales intensivas de 360 minutos (6 horas). Cada sesión contempla 30 minutos de receso y un tiempo neto de actividad formativa de 330 minutos (110 horas netas totales). El programa reproduce la integración progresiva de una línea piloto de embotellado y empaque continuo en el laboratorio de electrotecnia de Kinal. Nota mínima aprobatoria institucional: 75 puntos sobre 100 en todas las comprobaciones de banco.",
        bold_prefix="Organización Pedagógica Dual e Ideario Kinal:")

    # =========================================================================
    # 1. MATRIZ GENERAL CRONOLÓGICA DE LAS 20 SESIONES
    # =========================================================================
    h1_1 = doc.add_paragraph()
    style_heading(h1_1, "1. Matriz General de Dosificación de las 20 Sesiones (120 Horas)", level=1)

    sesiones_info = [
        ("Sesión 1", "Módulo 1: Control Eléctrico", "Seguridad eléctrica en planta (NFPA 70E, LOTO) y lectura de planos IEC", "Diagrama y protocolo LOTO"),
        ("Sesión 2", "Módulo 1: Control Eléctrico", "Aparamenta de maniobra: contactores AC-3, relés auxiliares y pulsadores", "Circuito marcha-paro probado"),
        ("Sesión 3", "Módulo 1: Control Eléctrico", "Inversión de giro electromagnética con enclavamientos mecánicos y eléctricos", "Tablero de inversión funcional"),
        ("Sesión 4", "Módulo 1: Control Eléctrico", "Protecciones térmicas, guardamotores y temporizadores neumáticos/electrónicos", "Circuito temporizado calibrado"),
        ("Sesión 5", "Módulo 1: Control Eléctrico", "Tablero de fuerza completo: arranque estrella-triángulo y bomba alternada", "Tablero Y-Δ sin cortocircuitos"),
        ("Sesión 6", "Módulo 2: Variadores VFD", "Topología del VFD (rectificador, bus DC, IGBTs PWM) y cableado apantallado", "Cableado de fuerza y tierra PE"),
        ("Sesión 7", "Módulo 2: Variadores VFD", "Puesta en marcha en teclado BOP, placa de motor y autotuning de parámetros", "Motor girando en modo manual"),
        ("Sesión 8", "Módulo 2: Variadores VFD", "Control remoto por terminales: marcha 2/3 hilos, inversión y multivelocidades", "Tabla de 4 velocidades probada"),
        ("Sesión 9", "Módulo 2: Variadores VFD", "Regulación analógica por potenciómetro 0-10V y lazo de corriente 4-20mA", "Control de velocidad continuo"),
        ("Sesión 10", "Módulo 2: Variadores VFD", "Frenado dinámico con resistencia, chopper y diagnóstico de códigos de falla", "Prueba de frenado y fallas"),
        ("Sesión 11", "Módulo 3: PLCs Siemens", "Arquitectura del S7-1200, cableado de entradas Sink/Source y sensores NPN/PNP", "Mapeo de sensores comprobado"),
        ("Sesión 12", "Módulo 3: PLCs Siemens", "Entorno TIA Portal, configuración de hardware, IP industrial y tabla de variables", "Proyecto online y CPU en RUN"),
        ("Sesión 13", "Módulo 3: PLCs Siemens", "Lógica de contactos Ladder (KOP): compuertas, enclavamientos y bobinas Set/Reset", "Semáforo secuencial funcional"),
        ("Sesión 14", "Módulo 3: PLCs Siemens", "Temporizadores TON/TOF/TP y contadores CTU aplicados a conteo de empaque", "Estación de conteo por lotes"),
        ("Sesión 15", "Módulo 3: PLCs Siemens", "Entradas analógicas, normalización NORM_X, escalado SCALE_X y comparadores", "Control de nivel por histéresis"),
        ("Sesión 16", "Módulo 4: Integración y Redes", "Integración física cableada de mando y velocidad entre salidas PLC y VFD", "Secuencia PLC gobernando VFD"),
        ("Sesión 17", "Módulo 4: Integración y Redes", "Red industrial PROFINET: configuración IO Device, palabras STW y ZSW", "Bus PROFINET enviando consigna"),
        ("Sesión 18", "Módulo 4: Integración y Redes", "Diseño de pantallas de supervisión operativa en panel HMI táctil WinCC", "Pantalla HMI operando celda"),
        ("Sesión 19", "Módulo 4: Integración y Redes", "Metodología estructurada de diagnóstico de averías (troubleshooting en 5 pasos)", "Diagnóstico de 3 fallas inducidas"),
        ("Sesión 20", "Módulo 4: Integración y Redes", "EXAMEN DE CERTIFICACIÓN PROFESIONAL: Comisionamiento integral y sustentación", "Celda operativa y dossier As-Built")
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
    headers_mat = ["Sesión (6h)", "Módulo Formativo", "Contenido Central del Encuentro", "Producto Observable"]
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
    # 2. MICRODISEÑO DIDÁCTICO DETALLADO SESIÓN POR SESIÓN
    # =========================================================================
    h1_2 = doc.add_paragraph()
    style_heading(h1_2, "2. Microdiseño Didáctico Detallado por Sesión (360 Minutos por Encuentro)", level=1)

    p_micro_intro = doc.add_paragraph()
    style_p(p_micro_intro, space_before=0, space_after=8)
    r = p_micro_intro.add_run("Cada una de las 20 sesiones formativas de 6 horas (360 minutos) se desglosa rigurosamente en tres momentos didácticos (Apertura 30 min, Desarrollo 280 min con Receso de 30 min, y Cierre 50 min), aplicando el principio institucional del «trabajo bien hecho»:")
    r.font.name = "Calibri"
    r.font.size = Pt(10)
    r.font.color.rgb = COLOR_DARK

    sesiones_detalladas = [
        # MÓDULO 1
        ("Sesión 1", "Módulo 1: Control Eléctrico", "Seguridad Eléctrica Industrial, Protocolo LOTO y Simbología IEC",
         "Aplica el protocolo de bloqueo/etiquetado LOTO e interpreta un plano eléctrico unifilar y multifilar identificando aparamenta sin errores.",
         "Bienvenida, ideario Kinal y valores del trabajo bien hecho. Análisis de caso real de planta: accidente por falta de etiquetado LOTO en una faja transportadora en Villa Nueva.",
         "Exposición dialogada de la norma NFPA 70E y categorías de EPP dieléctrico. Demostración práctica de aplicación de candados y aldabas LOTO con verificación multímetro (Test Before Touch). Simbología IEC 60617 en pizarra y software CADe SIMU. Receso (30 min). Práctica guiada: levantamiento y rotulado de componentes en tablero desenergizado.",
         "Inspección de planos elaborados por cada estudiante. Verificación de cero tensión en bornes. Registro de la primera lección en la Bitácora Berichtsheft.",
         "Kits de bloqueo LOTO, multímetros True-RMS, EPP dieléctrico, manuales de simbología, software CADe SIMU.",
         "Protocolo LOTO ejecutado en banco y diagrama unifilar acotado con simbología IEC normalizada."),

        ("Sesión 2", "Módulo 1: Control Eléctrico", "Aparamenta de Maniobra y Circuito de Marcha-Paro con Memoria",
         "Cablea un circuito electromagnético de marcha y paro con contactor AC-3, asegurando la autorretención eléctrica y la señalización luminosa correcta.",
         "Revisión de la bitácora anterior. Pregunta generadora: ¿Por qué no debemos accionar un motor trifásico directamente con un interruptor manual domiciliario?",
         "Estudio de las categorías de servicio de contactores (AC-1 vs AC-3). Análisis del arco voltaico en cámara apagachispas. Montaje mecánico de contactores y pulsadores en riel DIN. Práctica de cableado de circuito de control de marcha-paro con memoria por contacto auxiliar 13-14. Receso (30 min). Cableado del circuito de fuerza trifásico con motor acoplado.",
         "Protocolo de energización escalonada supervisada por el instructor. Prueba de pulsadores de marcha verde y paro rojo. Orden y peinado en canaleta. Registro en Berichtsheft.",
         "Contactores Siemens Sirius / Schneider TeSys, pulsadores NA/NC, luces piloto LED 24V/120V, conductores AWG 14 y 12, pinzas crimpadoras, ferrules.",
         "Tablero físico funcional con circuito de marcha-paro y señalización de estado verificado bajo rúbrica."),

        ("Sesión 3", "Módulo 1: Control Eléctrico", "Inversión de Giro Electromagnética con Doble Enclavamiento",
         "Construye un circuito de inversión de giro para motor trifásico incorporando enclavamiento eléctrico por contactos auxiliares y mecánico sin riesgo de cortocircuito entre fases.",
         "Retroalimentación rápida. Planteamiento del problema en la planta embotelladora: atasco en la faja de botellas que exige retroceso inmediato de la línea.",
         "Teoría del campo magnético giratorio e intercambio de fases L1-L2-L3. Demostración del cortocircuito franco si dos contactores de inversión entran en simultáneo. Cableado del doble enclavamiento: mecánico (bloque entre contactores) y eléctrico (contactos NC cruzados 21-22). Receso (30 min). Cableado de fuerza y prueba de giro horario y antihorario en banco de pruebas.",
         "Comprobación de la imposibilidad física de energizar ambos contactores a la vez. Medición de corrientes de arranque en ambos sentidos con pinza amperimétrica. Limpieza y registro en Berichtsheft.",
         "Tableros de entrenamiento, pares de contactores con enclavamiento mecánico, motores trifásicos 1 HP, pinzas amperimétricas, herramientas de electricista.",
         "Circuito de inversión de giro probado bajo tensión con doble enclavamiento y medición de corrientes documentada."),

        ("Sesión 4", "Módulo 1: Control Eléctrico", "Cálculo, Calibración de Protecciones Térmicas y Temporizadores",
         "Dimensiona y calibra un guardamotor y relé bimetálico para un motor trifásico, integrando un temporizador para arranque retardado según cálculos de placa.",
         "Análisis de falla: ¿Qué le sucede al devanado de un motor si se pierde una fase durante la producción continua?",
         "Cálculo de corriente nominal (In) y factor de servicio (FS). Curvas de disparo térmico clase 10 y clase 20. Conexionado y calibración de relé térmico y guardamotor. Integración de temporizadores electrónicos de retardo a la conexión (ON-Delay). Receso (30 min). Práctica de montaje de circuito de arranque temporizado automático con aviso previo de sirena/baliza.",
         "Simulación manual de disparo térmico (botón Test) y verificación de corte instantáneo de la bobina del contactor. Verificación de tiempos de retardo con cronómetro. Registro en Berichtsheft.",
         "Relés de sobrecarga bimetálicos, guardamotores magneto-térmicos, temporizadores multirango, balizas acústicas/luminosas, cronómetros.",
         "Hoja de cálculo de protecciones según placa de motor y circuito temporizado calibrado operando en tablero."),

        ("Sesión 5", "Módulo 1: Control Eléctrico", "Tablero de Fuerza Completo: Arranque Estrella-Triángulo (Y-Δ) y Bombeo Alternado",
         "Ensambla y prueba un sistema de arranque estrella-triángulo o bombeo alternado con cableado pulcro en canaleta ranurada, cumpliendo el umbral institucional de 75 puntos.",
         "Presentación del reto evaluativo de cierre de módulo: comisionar el sistema de suministro de agua de la planta con dos motores que alternan servicio.",
         "Revisión de esquemas estrella-triángulo: reducción de la corriente de arranque a 1/3 de la nominal. Cableado integral del circuito de 3 contactores (Línea, Triángulo, Estrella) con temporizador de transición. Receso (30 min). Montaje autónomo por parejas aplicando técnicas profesionales de prensado de terminales y peinado.",
         "Evaluación sumativa de Módulo 1 mediante rúbrica analítica Kinal (nota mínima 75/100). Verificación de rotulación, ajuste de borneras con torquímetro y puesta en marcha.",
         "Tableros industriales completos, 3 contactores por estación, temporizador estrella-triángulo, motores de 6 bornes 220/380V, boyas de nivel.",
         "Tablero estrella-triángulo o bombeo alternado evaluado y aprobado en funcionamiento real sin cortocircuitos."),

        # MÓDULO 2
        ("Sesión 6", "Módulo 2: Variadores VFD", "Topología del Variador de Frecuencia y Cableado de Blindaje PE",
         "Identifica los bloques internos del inversor (rectificador, bus DC, IGBT) y ejecuta el cableado de fuerza y tierra apantallada conforme a normas EMC.",
         "Introducción al Módulo 2. Reflexión: limitaciones del arranque directo frente a la necesidad de controlar velocidad precisa en el llenado de líquidos.",
         "Fundamentos de modulación por ancho de pulso (PWM) y conmutación de transistores IGBT. Identificación de bornes de potencia (L1-L2-L3, U-V-W, +DC/-DC, PB). Demostración del fenómeno dv/dt y corrientes parásitas en rodamientos. Receso (30 min). Práctica de cableado de fuerza con cable apantallado especial para variadores y conexión de blindaje a masa en 360°.",
         "Medición de resistencia de aislamiento con megóhmetro entre bornes del motor y tierra. Comprobación de orden en el peinado de fuerza vs control. Registro en Berichtsheft.",
         "Variadores Siemens Sinamics V20 / Schneider ATV320, cable apantallado para variador, prensacables metálicos EMC, megóhmetro digital.",
         "Montaje electromecánico del variador en riel DIN y conexión de cables de fuerza y tierra con blindaje verificado."),

        ("Sesión 7", "Módulo 2: Variadores VFD", "Parametrización en Teclado BOP y Rutina de Identificación Estática",
         "Configura la placa del motor en el panel de control del variador y ejecuta la rutina de identificación de parámetros estáticos (autotuning).",
         "Pregunta inicial: ¿Por qué un variador recién sacado de su caja no debe encenderse sin antes configurar los datos de placa del motor conectado?",
         "Navegación por el árbol de parámetros del panel BOP (Basic Operator Panel). Parámetros fundamentales: P0100 (frecuencia 50/60 Hz), P0304 (voltaje), P0305 (corriente), P0307 (potencia), P0310 (frecuencia nominal) y P0311 (RPM). Receso (30 min). Práctica en banco: ejecución del autotuning estático para calibrar la resistencia del estator. Arranque en modo manual local con teclas de flecha.",
         "Verificación del sentido de giro del motor y contraste de la corriente en vacío mostrada en pantalla frente a la pinza amperimétrica. Registro en Berichtsheft.",
         "Bancos de motores trifásicos, paneles BOP de variadores, pinzas amperimétricas, tacómetros digitales láser.",
         "Variador parametrizado con datos reales de placa y motor funcionando en modo local con giro verificado."),

        ("Sesión 8", "Módulo 2: Variadores VFD", "Control Remoto por Terminales Digitales y Multivelocidades Fijas",
         "Comisiona el control del variador mediante entradas discretas cableadas configurando tabla de 4 velocidades preseleccionadas para una banda transportadora.",
         "Planteamiento del requerimiento industrial: la máquina necesita velocidad lenta para inspección, velocidad media para enjuague y velocidad alta para llenado.",
         "Configuración de macros de aplicación en el variador (conexión a 2 hilos y 3 hilos). Cableado de entradas digitales DI1 (Marcha), DI2 (Inversión), DI3 y DI4 (selección binaria de velocidades). Parametrización de frecuencias fijas (15 Hz, 30 Hz, 45 Hz, 60 Hz). Receso (30 min). Ajuste de rampas de aceleración (t-acc = 3s) y desaceleración (t-dec = 2s).",
         "Prueba de conmutación de velocidades mediante selector de levas externo. Medición de velocidad con tacómetro láser en cada escalón. Registro en Berichtsheft.",
         "Selectores rotativos de 3 y 4 posiciones, botoneras industriales externas, variadores, tacómetros láser.",
         "Sistema de 4 velocidades prefijadas operando por selectores externos con tiempos de rampa verificados."),

        ("Sesión 9", "Módulo 2: Variadores VFD", "Regulación Analógica por Potenciómetro y Lazo de Corriente 4-20 mA",
         "Calibra la entrada analógica del variador para control suave con potenciómetro externo de 10 kΩ y lazo de corriente industrial de 4-20 mA.",
         "Diferencias prácticas entre señales de tensión (0-10V) y señales de corriente (4-20 mA) en ambientes industriales con alto ruido electromagnético.",
         "Conexionado del potenciómetro a la fuente interna de 10VDC del variador. Configuración de parámetros de escalado analógico (frecuencia mínima P1080 = 10 Hz, frecuencia máxima P1082 = 60 Hz). Receso (30 min). Conversión de entrada analógica a lazo de corriente 4-20 mA mediante jumper/switch físico. Conexión de generador de corriente simulando transmisor de presión.",
         "Calibración de la respuesta en frecuencia ante 4 mA (0 Hz / mín) y 20 mA (60 Hz / máx). Detección de pérdida de señal de corriente (falla 4mA loop break). Registro en Berichtsheft.",
         "Potenciómetros de precisión 10 kΩ, calibradores de proceso de corriente 4-20 mA, cables apantallados de instrumentación, multímetros.",
         "Variador respondiendo proporcionalmente a lazo de corriente 4-20 mA y potenciómetro con límites acotados."),

        ("Sesión 10", "Módulo 2: Variadores VFD", "Frenado Dinámico, Chopper y Diagnóstico de Alarmas del VFD",
         "Dimensiona y conecta una resistencia de frenado dinámico en bornes DC+/B y resuelve códigos de error típicos (OC, OV, OH) en banco de pruebas.",
         "Caso de estudio: una faja transportadora con botellas derrama producto porque el motor se tarda 15 segundos en detenerse por inercia.",
         "Concepto de energía regenerativa y aumento de voltaje en el bus de continua. Cálculo del valor óhmico y potencia de la resistencia de frenado. Conexión en bornes PB/DC+ del chopper integrado. Receso (30 min). Parámetros de frenado por inyección DC y parada rápida (OFF3). Taller de diagnóstico: simulación de fallas de sobrecorriente (F0001) y sobretensión (F0002) y procedimiento de reset.",
         "Evaluación de Módulo 2: Comisionamiento completo de variador ante el instructor en menos de 45 minutos (nota mínima 75/100). Registro en Berichtsheft.",
         "Resistencias de frenado dinámico disipativas blindadas, cronómetros, generadores de falla simulada.",
         "Prueba de parada rápida con frenado dinámico por resistencia y reporte de diagnóstico de fallas superado."),

        # MÓDULO 3
        ("Sesión 11", "Módulo 3: PLCs Siemens", "Arquitectura del Autómata S7-1200 y Cableado de Entradas/Salidas Discretas",
         "Cablea sensores industriales discretos (inductivos, capacitivos, ópticos) a las entradas digitales de una CPU Siemens S7-1200 en modo Sink/Source.",
         "Inicio del Módulo 3. Análisis: transición del control electromecánico cableado al control lógico programable para flexibilidad total de planta.",
         "Estructura del hardware S7-1200 (CPU 1214C DC/DC/DC). Alimentación de 24 VDC y conexión de masa común (1M / 2M). Diferencias de cableado entre sensores PNP (conmutación a positivo) y NPN (conmutación a negativo). Receso (30 min). Cableado práctico de un sensor inductivo para detección de latas metálicas y fotocélula para botellas plásticas a los bornes de entrada del PLC.",
         "Verificación visual del encendido de los LEDs de entrada (DIa .0, .1, .2) al excitar manualmente cada sensor. Cero cortocircuitos. Registro en Berichtsheft.",
         "PLCs Siemens S7-1200, fuentes de alimentación industriales 24VDC / 5A, sensores inductivos, ópticos difusos, reflectivos y capacitivos.",
         "Tablero de PLC con cableado ordenado de sensores de campo y comprobación de activación de LEDs de entrada."),

        ("Sesión 12", "Módulo 3: PLCs Siemens", "Entorno TIA Portal, Configuración de Hardware y Enlace Ethernet",
         "Crea un proyecto en Siemens TIA Portal, establece comunicación Industrial Ethernet con la CPU y estructura la tabla de variables del proceso.",
         "Pregunta orientadora: ¿Cómo dialoga la computadora de ingeniería con el procesador del autómata en un ambiente industrial ruidoso?",
         "Introducción a la interfaz del Totally Integrated Automation (TIA Portal). Creación de proyecto nuevo y configuración de hardware por catálogo o detección automática. Asignación de dirección IP estática en la misma subred. Receso (30 min). Descarga de configuración a la CPU y puesta en modo RUN. Creación de la tabla de variables (PLC Tags) con nombres nemotécnicos estandarizados.",
         "Uso de la función «Parpadear LED» para confirmar la identificación del PLC físico en la red. Verificación de comunicación online sin errores de diagnóstico.",
         "Laptops con TIA Portal V18/V19 instalado, cables de red Ethernet Cat 6 con conectores industriales RJ45, switches industriales no administrados.",
         "Proyecto de TIA Portal online con la CPU real en RUN y tabla de variables de planta debidamente estructurada."),

        ("Sesión 13", "Módulo 3: PLCs Siemens", "Lógica Combinacional en Ladder (KOP), Enclavamientos y Flancos",
         "Desarrolla programas en lenguaje Ladder utilizando contactos NA/NC, bobinas, enclavamientos y detección de flancos para control de secuencias.",
         "Repaso del ciclo de scan del autómata (PII -> Programa -> PIQ). Reto: programar la seguridad de arranque de la faja transportadora con múltiples condiciones.",
         "Sintaxis del editor de bloques en el Bloque de Organización principal (OB1). Lógica AND, OR y NOT en peldaños Ladder. Programación de autorretención tradicional vs instrucciones Set (S) y Reset (R). Receso (30 min). Detección de pulsos cortos mediante instrucciones de flanco positivo (P_TRIG) para conteo de productos a alta velocidad.",
         "Prueba del programa descargado en el PLC forzando variables de entrada y observando las salidas a través de la herramienta «Observar bloque» (gafas verdes). Registro en Berichtsheft.",
         "Software TIA Portal, autómatas S7-1200, botoneras de entrada conectadas, lámparas de salida a 24VDC.",
         "Programa Ladder probado online en el PLC con control de arranque seguro y detección de flancos operativos."),

        ("Sesión 14", "Módulo 3: PLCs Siemens", "Temporizadores Industriales (TON/TOF) y Contadores de Producción (CTU)",
         "Programa rutinas de llenado temporizado y empaque por cajas utilizando temporizadores TON y contadores CTU validados con sensórica real.",
         "Caso de la planta: llenado de botellas durante 4.5 segundos exactos, avance de faja y parada automática al completar una caja de 12 unidades.",
         "Estructura de datos del bloque IEC_TIMER en temporizadores TON (retardo a conexión) y TOF (retardo a desconexión). Bloque contador ascendente CTU con valor de preselección (PV). Receso (30 min). Programación de la secuencia cíclica en Ladder: detección de botella por sensor óptico, paro de faja, temporizado de electroválvula de llenado y conteo de caja llena.",
         "Prueba de la rutina en el banco con botellas de muestra. Reseteo del contador al retirar la caja llena. Verificación de robustez ante paradas repentinas. Registro en Berichtsheft.",
         "Kits de sensores ópticos, bandas transportadoras didácticas miniatura, electroválvulas neumáticas 24VDC, botellas plásticas de prueba.",
         "Lógica de llenado y conteo de lotes por empaque funcionando de forma autónoma en el autómata."),

        ("Sesión 15", "Módulo 3: PLCs Siemens", "Señales Analógicas, Normalización (NORM_X), Escalado y Comparadores",
         "Procesa una señal analógica de nivel/presión en el PLC utilizando instrucciones NORM_X y SCALE_X y activa alarmas por comparadores de magnitud.",
         "Reto técnico: ¿Cómo entiende el PLC un valor de temperatura o presión que cambia continuamente entre 0 y 100 grados o 0 y 10 bar?",
         "Canales analógicos integrados (IW64 / 0 a 27648 cuentas). Fórmula matemática y bloque de normalización NORM_X (conversión de Int a Real entre 0.0 y 1.0). Bloque de escalado SCALE_X (conversión a unidades de ingeniería). Receso (30 min). Programación de comparadores numéricos (CMP >=, CMP <=) para control de histéresis de arranque y paro de bomba de achique.",
         "Evaluación de Módulo 3: Prueba práctica individual de programación en TIA Portal ante el docente (nota mínima 75/100). Registro en Berichtsheft.",
         "Potenciómetros 0-10V conectados a entradas analógicas del PLC, transmisores industriales didácticos, TIA Portal.",
         "Programa analógico escalado en unidades físicas de ingeniería operando con histéresis y alarmas validadas."),

        # MÓDULO 4
        ("Sesión 16", "Módulo 4: Integración y Redes", "Integración Cableada de Mando y Consignas entre PLC S7-1200 y Variador VFD",
         "Conecta físicamente y sincroniza las salidas del PLC con las entradas de control y velocidad del variador para gobernar un proceso continuo.",
         "Inicio del Módulo 4. Misión integradora: unir el cerebro de control (PLC) con el músculo de potencia y velocidad (VFD) para la línea continua.",
         "Diseño del esquema de interconexión entre salidas a transistor del PLC y entradas digitales del variador (marcha, paro, cambio de giro). Conexión de la salida analógica del PLC (AQ) a la entrada analógica del variador (AI). Receso (30 min). Programación en Ladder de perfiles de aceleración y desaceleración coordinados con las estaciones previas y posteriores.",
         "Puesta en marcha del conjunto PLC-VFD-Motor. Prueba de interbloqueo: la faja solo avanza si la máquina llenadora está lista y no hay fallas térmicas activas. Registro en Berichtsheft.",
         "Estaciones integradas de PLC S7-1200 acopladas a variadores Sinamics/Schneider, motores trifásicos, cableado de señales.",
         "Línea de transporte gobernada en velocidad y sentido por el PLC a través de interconexión física comprobada."),

        ("Sesión 17", "Módulo 4: Integración y Redes", "Comunicación Industrial por Red PROFINET entre PLC y Variador",
         "Configura el variador como esclavo PROFINET IO en TIA Portal y gobierna el motor mediante palabras de control (STW) y estado (ZSW) por bus de datos.",
         "Pregunta de planta: ¿Por qué la industria moderna reemplaza 15 cables de cobre de control por un solo cable Ethernet industrial verde?",
         "Fundamentos de PROFINET RT (Real-Time). Importación del archivo GSD/GSDML del variador al catálogo de TIA Portal. Configuración de la red y asignación de dispositivo PROFINET. Receso (30 min). Perfil PROFIdrive: desglose bit a bit de la palabra de control STW1 (bits de marcha 047E / 047F) y consigna de velocidad en la palabra NSOLL_A. Lectura de corriente real devuelta por el variador.",
         "Comprobación del tráfico cíclico de datos por bus PROFINET. Monitoreo en tabla de observación de TIA Portal de los telegramas de comunicación. Registro en Berichtsheft.",
         "Cables PROFINET certificados con blindaje de cobre y conectores RJ45 apantallados, variadores con puerto PROFINET integrado, TIA Portal.",
         "Variador comisionado y controlado 100% por red PROFINET enviando consignas y reportando telemetría al PLC."),

        ("Sesión 18", "Módulo 4: Integración y Redes", "Supervisión Operativa con Pantalla HMI Táctil Siemens WinCC",
         "Diseña y descarga una interfaz gráfica HMI en panel SIMATIC KTP con comandos de marcha/paro, visualización de RPM y gestión de alarmas de falla.",
         "Planteamiento ergonómico: cómo facilitar al operario de planta el control de la celda automatizada sin abrir el tablero eléctrico de alta tensión.",
         "Configuración del panel HMI Siemens en el proyecto de TIA Portal (SIMATIC KTP400 / KTP700 Basic). Conexión de variables HMI con marcas y bloques DB del PLC. Diseño de pantalla principal: pulsadores táctiles de mando, lámparas de estado multicolores y visualizador numérico de RPM reales. Receso (30 min). Creación de pantalla de avisos de falla con botón de acuse de recibo y reseteo.",
         "Descarga de la aplicación al panel HMI físico. Prueba de operación completa de la celda desde la pantalla táctil sin tocar botones físicos. Registro en Berichtsheft.",
         "Paneles HMI táctiles Siemens SIMATIC KTP, software WinCC Basic en TIA Portal, cables Ethernet de comunicación.",
         "Interfaz HMI funcional en panel táctil gobernando la celda y mostrando telemetría en tiempo real."),

        ("Sesión 19", "Módulo 4: Integración y Redes", "Metodología Estructurada de Diagnóstico de Averías (Troubleshooting)",
         "Aplica el protocolo metódico de 5 pasos para aislar, identificar y corregir fallas inducidas en hardware, cableado y programación en banco real.",
         "Reflexión ética sobre el «trabajo bien hecho»: un técnico profesional no adivina ni cambia piezas a ciegas; aplica un método científico de descarte seguro.",
         "Las 5 etapas del troubleshooting industrial: 1. Escuchar al operador y delimitar síntomas, 2. Inspección visual y mediciones básicas de energía, 3. Aislamiento por capas, 4. Corrección de causa raíz, 5. Prueba de confirmación y registro. Receso (30 min). Dinámica de laboratorio: el instructor induce de manera controlada 3 fallas reales en estaciones de trabajo ajenas (falso contacto en borne, cable invertido en 24VDC, contacto negado en Ladder).",
         "Resolución metódica de averías por parejas bajo límite de tiempo (máx. 25 min por avería). Redacción del informe técnico de causa raíz. Registro en Berichtsheft.",
         "Kits de fallas inducidas, multímetros, trazadores de señal, software TIA Portal con herramientas de diagnóstico online.",
         "Informe técnico de diagnóstico y resolución de averías firmado con causa raíz identificada y remediada."),

        ("Sesión 20", "Módulo 4: Integración y Redes", "EXAMEN DE CERTIFICACIÓN PROFESIONAL: Comisionamiento y Defensa Técnica",
         "Demuestra la capacidad integral de acción técnica comisionando la celda integrada continua y sustentando el dossier técnico As-Built (Umbral: ≥75 pts).",
         "Apertura del examen oficial de certificación. Verificación de condiciones de seguridad LOTO y revisión del estado de los bancos de prueba.",
         "Prueba práctica individual de certificación profesional (tiempo límite 120 minutos): el participante recibe el requerimiento de una celda de empaque, debe parametrizar el variador, programar la rutina en PLC S7-1200, verificar el cableado de sensores y poner en marcha el proceso continuo. Receso (30 min). Inducción de 2 averías en tiempo real por parte del tribunal evaluador que deben ser resueltas en menos de 45 minutos.",
         "Sustentación oral del dossier técnico As-Built y entrega de la Bitácora Berichtsheft completa. Calificación final sobre 100 puntos y retroalimentación personalizada.",
         "Bancos completos de automatización industrial, instrumental calibrado, rúbricas de evaluación institucional Kinal.",
         "Acta oficial de evaluación práctica de certificación profesional aprobada (≥ 75 puntos) y dossier técnico entregado.")
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
            ("Desarrollo (280 min):", des),
            ("Cierre (50 min):", cie),
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
        "La evaluación en banco de pruebas se rige por la rúbrica analítica institucional de Fundación Kinal. Todo estudiante debe alcanzar al menos 75 puntos sobre 100 para aprobar cada práctica y la certificación final, demostrando apego incondicional al principio del «trabajo bien hecho».",
        bold_prefix="Criterio de Evaluación y Umbral de Aprobación:")

    p_rub = doc.add_paragraph()
    style_heading(p_rub, "3.1 Rúbrica Analítica de Desempeño Práctico en Banco de Pruebas (100 Puntos)", level=2)

    rubrica_data = [
        ("Seguridad Ocupacional y LOTO", "20 Puntos", "Aplica bloqueo LOTO, EPP dieléctrico completo y verificación con multímetro antes de intervenir. Cero faltas de seguridad.", "Omite algún paso del protocolo LOTO o usa herramientas inadecuadas (< 15 pts)."),
        ("Calidad Técnica del Cableado y Ensamble", "25 Puntos", "Peinado en canaleta sin cruces forzados, uso de terminales ferrule prensados correctamente y rotulado legible en cada borne.", "Cables flojos, falta de ferrules, empalmes o desorden en el peinado (< 19 pts)."),
        ("Lógica de Funcionamiento y Parametrización", "30 Puntos", "El circuito o programa en PLC/VFD cumple al 100% con la secuencia exigida, rampas, temporizadores y enclavamientos sin fallas.", "El motor no arranca, secuencias invertidas o errores en parámetros básicos (< 23 pts)."),
        ("Diagnóstico Metódico y Resolución de Averías", "15 Puntos", "Aplica aislamiento estructurado por capas y localiza y repara averías inducidas en el tiempo asignado.", "Adivina o cambia conexiones al azar sin justificar mediciones técnicas (< 11 pts)."),
        ("Orden, Limpieza (5S) y Bitácora Berichtsheft", "10 Puntos", "Puesto de trabajo impecable al finalizar y registro detallado de la práctica en la bitácora técnica visada.", "Herramientas desordenadas, residuos de cable en el piso o bitácora incompleta (< 7.5 pts).")
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
        ("Actividad Práctica Ejecutada:", "Descripción técnica del circuito montado, programa Ladder descargado o VFD comisionado."),
        ("Normas de Seguridad Aplicadas:", "Protocolo LOTO verificado, bloqueo físico de disyuntores, uso de EPP y mediciones con multímetro."),
        ("Mediciones Técnicas Obtenidas:", "Tensión de línea (V), corriente de arranque (Ia), corriente nominal (In), frecuencia (Hz), RPM."),
        ("Dificultad Superada («Trabajo Bien Hecho»):", "Registro de averías o dificultades técnicas resueltas durante la sesión y lección aprendida."),
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
    run_f = footer_p.add_run("Fundación Kinal | Automatización y Control Eléctrico Industrial — Dosificación Oficial")
    run_f.font.name = "Calibri"
    run_f.font.size = Pt(8.5)
    run_f.font.color.rgb = COLOR_SECONDARY

    out_dir = os.path.join("Cursos", "Automatización")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "Dosificacion_y_Secuencia_Didactica_Automatizacion_Kinal.docx")
    doc.save(out_path)
    print(f"Dosificación guardada con éxito en: {out_path}")

if __name__ == "__main__":
    generate_dosificacion_doc()
