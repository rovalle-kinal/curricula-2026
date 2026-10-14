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

def style_p(p, space_before=0, space_after=6, line_spacing=1.15):
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = line_spacing

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

def generate_temario_doc():
    doc = docx.Document()

    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    COLOR_PRIMARY = RGBColor(0, 51, 102)      # Azul Kinal
    COLOR_SECONDARY = RGBColor(74, 85, 104)    # Gris pizarra
    COLOR_DARK = RGBColor(26, 32, 44)         # Texto oscuro

    # ==========================================
    # ENCABEZADO INSTITUCIONAL
    # ==========================================
    title_p = doc.add_paragraph()
    style_p(title_p, space_before=0, space_after=6)
    run_title = title_p.add_run("Automatización y Control Eléctrico Industrial con PLC y Variadores de Frecuencia (VFD)")
    run_title.font.name = "Calibri"
    run_title.font.size = Pt(20)
    run_title.font.bold = True
    run_title.font.color.rgb = COLOR_PRIMARY

    sub_p = doc.add_paragraph()
    style_p(sub_p, space_before=0, space_after=14)
    run_sub = sub_p.add_run("Programa Oficial de Formación y Temario Analítico Detallado  |  Duración: 120 Horas Formativas  |  20 Sesiones\nFundación Kinal — Escuela Técnica Superior | Nivel DQR 4 - 5 | Umbral Aprobatorio: 75/100 Puntos")
    run_sub.font.name = "Calibri"
    run_sub.font.size = Pt(11)
    run_sub.font.italic = True
    run_sub.font.color.rgb = COLOR_SECONDARY

    add_callout(doc, 
        "«the ability and readiness of the individual to use knowledge, skills and personal, social and methodological competences and to behave in a considered, individual and socially responsible manner. Competence is understood in this sense as the comprehensive ability to act». Este programa técnico-profesional garantiza que cada hora formativa combine conocimientos rigurosos de ingeniería con ejecución práctica manual en banco de pruebas bajo el ideario del «trabajo bien hecho» y respeto irrenunciable a la seguridad humana (NFPA 70E).", 
        bold_prefix="Definición de Competencia DQR e Ideario Kinal:")

    # ==========================================
    # 1. OBJETIVOS FORMATIVOS Y COMPETENCIAS
    # ==========================================
    h1_1 = doc.add_paragraph()
    style_heading(h1_1, "1. Competencia General y Resultados de Aprendizaje por Módulo", level=1)

    p_cg = doc.add_paragraph()
    style_p(p_cg, space_before=0, space_after=6)
    r = p_cg.add_run("Competencia General del Programa:\n"
                     "El participante dimensiona, ensambla, cablea, parametriza y programa sistemas de control eléctrico y fuerza para procesos industriales continuos, utilizando contactores, variadores de frecuencia (VFD) y controladores lógicos programables (PLC Siemens S7-1200 / LOGO!), aplicando estrictamente las normativas de seguridad eléctrica (NFPA 70E / NEC), interpretando diagramas bajo norma IEC/NEMA y demostrando un estándar de trabajo bien hecho, orden y diagnóstico metódico de averías en banco de pruebas real.")
    r.font.name = "Calibri"
    r.font.size = Pt(10)
    r.font.bold = True
    r.font.color.rgb = COLOR_PRIMARY

    mod_comps = [
        ("Módulo 1: Control Eléctrico Industrial y Tableros de Fuerza", 
         "Construye y prueba en tablero físico circuitos electromagnéticos de fuerza y mando (inversión de giro, estrella-triángulo), calculando y calibrando protecciones térmicas y guardamotores bajo normas IEC 60617 y NFPA 70E, con cero cortocircuitos."),
        ("Módulo 2: Parametrización y Puesta en Marcha de VFDs", 
         "Comisiona y parametriza variadores de frecuencia comerciales en banco de motores, configurando rampas de aceleración/deceleración, control por terminales analógicas (4-20mA / 0-10V) y protecciones de sobretorque sin asistencia en menos de 45 minutos."),
        ("Módulo 3: Programación y Cableado de PLCs Siemens", 
         "Desarrolla en software TIA Portal y descarga en el autómata un programa en lenguaje Ladder (KOP) con temporizadores, contadores y sensórica industrial, validando el mapeo correcto de señales y la lógica de parada de emergencia."),
        ("Módulo 4: Integración Automatizada y Diagnóstico de Averías", 
         "Integra el enlace de control entre PLC y Variador de Frecuencia gobernando un proceso continuo; detecta y soluciona 2 fallas inducidas en el cableado o programa en un tiempo máximo de 60 minutos, sustentando el informe técnico de conformidad.")
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
    # 2. TEMARIO ANALÍTICO DETALLADO POR MÓDULOS
    # ==========================================
    h1_2 = doc.add_paragraph()
    style_heading(h1_2, "2. Temario Analítico Jerárquico y Prácticas de Laboratorio", level=1)

    # -------------------------------------------------------------
    # MODULO 1
    # -------------------------------------------------------------
    h2_m1 = doc.add_paragraph()
    style_heading(h2_m1, "MÓDULO 1: CONTROL ELÉCTRICO INDUSTRIAL, MANDO Y DISEÑO DE TABLEROS DE FUERZA (30 Horas)", level=2)

    temas_m1 = [
        ("1.1 Seguridad Eléctrica Ocupacional y Normativa Internacional", [
            "Peligros de la electricidad en media y baja tensión: choque eléctrico, quemaduras y arco eléctrico (Arc Flash).",
            "Norma NFPA 70E: Categorías de EPP dieléctrico, límites de aproximación segura y cálculo de energía incidente.",
            "Procedimiento estandarizado de Bloqueo y Etiquetado (LOTO): candados, aldabas, tarjetas y prueba de ausencia de tensión (Test Before Touch).",
            "Puesta a tierra industrial (Grounding y Bonding) según Código Eléctrico Nacional (NEC Art. 250)."
        ]),
        ("1.2 Simbología y Lectura de Planos Eléctricos Industriales", [
            "Simbología internacional bajo norma IEC 60617 vs. estándar NEMA / ANSI.",
            "Interpretación de esquemas unifilares, multifilares y de conexiones por borneras.",
            "Estructura y numeración alfanumérica de cables, borneras y aparamenta (etiquetado normalizado).",
            "Diseño y simulación de circuitos de fuerza y control en software CAD eléctrico (CADe SIMU)."
        ]),
        ("1.3 Aparamenta Electromecánica de Fuerza y Maniobra", [
            "Contactores de potencia: categorías de servicio (AC-1, AC-3, AC-4), cámara apagachispas y bobinas de accionamiento.",
            "Contactos auxiliares instantáneos y temporizados (bloques neumáticos ON-Delay y OFF-Delay).",
            "Pulsadores industriales (NA/NC), selectores de 2 y 3 posiciones con retorno, y setas de parada de emergencia con enclavamiento.",
            "Relés auxiliares encapsulados de 8 y 11 pines (bases octales y undecales) para acoplamiento de señales."
        ]),
        ("1.4 Cálculo, Dimensionamiento y Coordinación de Protecciones", [
            "Fórmulas de potencia en corriente alterna trifásica: potencia activa (kW), reactiva (kVAR), aparente (kVA) y factor de potencia.",
            "Cálculo de corriente nominal (In) y corriente de arranque (Ia/In) en motores de inducción.",
            "Interruptores termomagnéticos (curvas B, C, D) y fusibles ultrarrápidos para cortocircuitos.",
            "Relés bimetálicos de sobrecarga y guardamotores termomagnéticos: curva de disparo térmico, rearme manual/automático y calibración al 100% de In."
        ]),
        ("1.5 Técnicas Profesionales de Ensamble y Montaje en Tablero", [
            "Distribución mecánica de componentes en riel DIN simétrico de 35 mm y canaleta ranurada.",
            "Selección de calibres de conductores según ampacidad y caída de tensión (AWG/kcmil).",
            "Técnica de prensado con terminales de compresión (ferrules y terminales de ojo/espada) con pinza crimpadora calibrada.",
            "Peinado pulcro, segregación de tensión de fuerza (220V/480V) y control (24VDC/120VAC) para evitar interferencias inductivas."
        ]),
        ("1.6 Prácticas de Taller y Ensamble en Banco Físico", [
            "Práctica 1.1: Circuito de marcha-paro con enclavamiento eléctrico, memoria por contacto auxiliar y señalización luminosa.",
            "Práctica 1.2: Circuito de inversión de giro con enclavamiento mecánico y eléctrico doble por pulsadores y contactores.",
            "Práctica 1.3: Circuito temporizado de arranque secuencial de tres motores (semáforo industrial).",
            "Práctica 1.4: Tablero completo de arranque estrella-triángulo (Y-Δ) para motor trifásico con temporizador neumático y protección térmica.",
            "Práctica 1.5: Sistema automático de bombeo alternado para tanque de agua con boyas de nivel y conmutación por falla de sobrecarga."
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
    style_heading(h2_m2, "MÓDULO 2: PARAMETRIZACIÓN, CONTROL Y PUESTA EN MARCHA DE VARIADORES DE FRECUENCIA (VFD) (30 Horas)", level=2)

    temas_m2 = [
        ("2.1 Principio de Funcionamiento y Topología Electrónica del VFD", [
            "Etapa rectificadora (puente de diodos trifásico), bus intermedio de corriente continua (banco de condensadores y bobina de choque).",
            "Etapa inversora: transistores bipolares de puerta aislada (IGBT) y modulación por ancho de pulso (PWM).",
            "Relación Voltaje/Frecuencia (V/f lineal, cuadrática) y control vectorial sensorless de flujo magnético.",
            "Armónicos en la red, reflexiones de onda en cables largos (dv/dt) y uso de filtros de línea o reactores inductivos."
        ]),
        ("2.2 Cableado de Fuerza y Control en el Variador", [
            "Conexión de entrada de red (L1, L2, L3 / PE) y bornes de salida al motor (U, V, W).",
            "Importancia de la conexión equipotencial de tierra y uso de cables apantallados con blindaje continuo de 360°.",
            "Bornes de control digital: entradas digitales (DI1..DI6) en modo PNP (Source) y NPN (Sink).",
            "Bornes de control analógico: entradas de tensión (0-10V) y entradas de corriente (4-20 mA) con interruptores DIP de selección.",
            "Salidas a relé programables (señalización de fallas, motor en marcha) y salida analógica para monitoreo de RPM o corriente."
        ]),
        ("2.3 Puesta en Marcha Rápida y Parametrización en Teclado (BOP)", [
            "Estructura de menús y parámetros en marcas líderes (Siemens Sinamics V20/G120, Schneider Altivar, WEG CFW).",
            "Ingreso de placa de datos del motor: potencia nominal (kW/HP), tensión (V), corriente (A), frecuencia base (Hz), RPM nominales y cos φ.",
            "Autotuning y rutina de identificación estática del motor (motor identification at standstill).",
            "Configuración del tiempo de rampa de aceleración (t-acc) y rampa de deceleración (t-dec)."
        ]),
        ("2.4 Modos de Control y Aplicaciones Industriales Prácticas", [
            "Modo Local vs. Modo Remoto (control por botonera frontal vs. bornera de control exterior).",
            "Configuración de multivelocidades fijas mediante combinaciones binarias de entradas digitales.",
            "Control de velocidad variable continuo con potenciómetro analógico externo de 10 kΩ.",
            "Control en lazo cerrado por lazo de corriente 4-20 mA desde un transmisor de presión/temperatura.",
            "Inversión de giro comandada por señal externa y funcionamiento en modo JOG (avance a impulsos para calibración de maquinaria)."
        ]),
        ("2.5 Frenado Dinámico y Protecciones Avanzadas", [
            "Sobretensión en el bus DC por energía regenerativa del motor al desacelerar cargas de alta inercia.",
            "Cálculo y conexión de resistencia de frenado dinámico (Braking Resistor) y chopper de frenado.",
            "Método de frenado por inyección de corriente continua (DC Braking).",
            "Diagnóstico de códigos de alarma y falla en pantalla: sobrecorriente de salida (F0001 / OCF), sobretensión de bus (F0002 / ObF), sobretemperatura (F0004 / OHF) y fallo de tierra (F0003)."
        ]),
        ("2.6 Prácticas de Taller y Parametrización en Banco", [
            "Práctica 2.1: Parametrización inicial rápida en panel BOP, arranque en modo manual con potenciómetro frontal y verificación de sentido de giro.",
            "Práctica 2.2: Conexión y configuración de control remoto por pulsadores externos (marcha 2 hilos / 3 hilos e inversión de giro).",
            "Práctica 2.3: Configuración de tabla de 4 velocidades preseleccionadas para faja transportadora con selector rotativo.",
            "Práctica 2.4: Control de velocidad suave de bomba mediante potenciómetro de 10 kΩ y limitación de velocidad mínima y máxima por parámetro.",
            "Práctica 2.5: Simulación de parada de emergencia con frenado brusco dinámico por resistencia y diagnóstico de fallas inducidas por el instructor."
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
    style_heading(h2_m3, "MÓDULO 3: PROGRAMACIÓN Y CABLEADO DE CONTROLADORES LÓGICOS PROGRAMABLES (PLC SIEMENS) (30 Horas)", level=2)

    temas_m3 = [
        ("3.1 Arquitectura del Autómata y Cableado de Entradas/Salidas", [
            "Estructura modular y compacta del PLC: fuente de alimentación interna, CPU, buses de comunicación y tarjetas de I/O.",
            "Cableado eléctrico de entradas digitales de 24 VDC: concepto de sumidero (Sink) y fuente (Source).",
            "Conexionado de sensores industriales discretos: interruptores mecánicos, finales de carrera, inductivos, capacitivos y ópticos (tecnologías PNP y NPN a 3 y 4 hilos).",
            "Salidas discretas del autómata: salidas por contacto seco a relé (máx. 2A) vs. salidas por transistor de estado sólido (24 VDC / alta velocidad para tren de pulsos PTO/PWM)."
        ]),
        ("3.2 Entorno de Desarrollo TIA Portal y Configuración de Hardware", [
            "Instalación, estructura de proyectos y licencias en Siemens TIA Portal / LOGO! Soft Comfort.",
            "Comunicación Industrial Ethernet: asignación de dirección IP estática, máscara de subred y escaneo de dispositivos accesibles.",
            "Configuración del catálogo de hardware: selección de CPU Siemens S7-1200 (CPU 1214C DC/DC/DC) y módulos de señales (SM / SB).",
            "Creación de la tabla de variables del PLC (PLC Tags): nomenclatura estructurada y tipos de datos (Bool, Byte, Word, DWord, Int, DInt, Real, Time)."
        ]),
        ("3.3 Programación Básica en Lenguaje de Contactos (Ladder - KOP)", [
            "Ciclo de scan del PLC: lectura de imagen de entradas (PII), ejecución cíclica del programa y actualización de salidas (PIQ).",
            "Instrucciones lógicas combinacionales fundamentales: contacto normalmente abierto (NO), contacto normalmente cerrado (NC), bobina estándar, bobina negada.",
            "Enclavamientos por software: auto-retención tradicional por contacto auxiliar y uso de instrucciones Set (S) y Reset (R).",
            "Detección de flancos de señal: flanco ascendente (P_TRIG / Flanco positivo) y flanco descendente (N_TRIG) para pulsos de sincronismo."
        ]),
        ("3.4 Temporizadores y Contadores en Rutinas Industriales", [
            "Temporizador de retardo a la conexión (TON): estructura de datos IEC_TIMER, tiempo predeterminado (PT) y tiempo transcurrido (ET).",
            "Temporizador de retardo a la desconexión (TOF) y temporizador de pulso (TP).",
            "Contadores ascendentes (CTU), descendentes (CTD) y bidireccionales (CTUD): conteo de productos, reseteo y comparación de lote cumplido.",
            "Bloques de función y organización: Bloques de Organización (OB1 - Main, OB100 - Startup), Funciones (FC) y Bloques de Función con memoria (FB con DB de instancia)."
        ]),
        ("3.5 Tratamiento de Señales Analógicas e Instrucciones de Comparación", [
            "Canales de entrada analógica integrados (0-10V / 0-27648 cuentas en S7-1200).",
            "Instrucciones de normalización (NORM_X) y escalado matemático (SCALE_X) para convertir cuentas crudas en magnitudes de ingeniería físicas (°C, bar, m/s).",
            "Comparadores numéricos (CMP ==, CMP <>, CMP >=, CMP <=) aplicados a controles de histéresis y alarmas.",
            "Gestión segura de la parada de emergencia: interbloqueo obligatorio por hardware en serie con la bobina y monitoreo por software en el autómata."
        ]),
        ("3.6 Prácticas de Taller y Programación en Banco", [
            "Práctica 3.1: Cableado físico de sensores inductivos y fotocélulas a bornera del S7-1200 y prueba de variables online en TIA Portal.",
            "Práctica 3.2: Programación de control secuencial de un semáforo industrial de 3 estados con temporizadores TON.",
            "Práctica 3.3: Automatización de estación de llenado y tapado con faja transportadora, conteo de 12 botellas por caja y aviso de caja llena.",
            "Práctica 3.4: Programación de sistema de arranque de 2 motores con alternancia automática por horas de servicio simuladas y conmutación por falla térmica.",
            "Práctica 3.5: Lectura de sensor analógico de nivel 0-10V, escalado en porcentaje (0-100%) y activación de bomba de achique con umbrales de histéresis."
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
    style_heading(h2_m4, "MÓDULO 4: INTEGRACIÓN AUTOMATIZADA, REDES INDUSTRIALES Y DIAGNÓSTICO DE AVERÍAS (30 Horas)", level=2)

    temas_m4 = [
        ("4.1 Integración Cableada de Mando y Consignas entre PLC y VFD", [
            "Topología de control discreto: salidas a transistor/relé del PLC comandando marcha, paro, sentido de giro y multivelocidad del VFD.",
            "Topología de control analógico: salida analógica del PLC (AQ) inyectando consigna de velocidad de 0-10V / 4-20mA al variador.",
            "Retroalimentación de estado: entradas digitales del PLC recibiendo señales de 'Variador Listo', 'Motor en Marcha' y 'Falla Activa (Fault)'.",
            "Mapeo de señales y puesta a punto de secuencias coordinadas entre fajas de alimentación y fajas de empaque."
        ]),
        ("4.2 Comunicación Digital Industrial (PROFINET y Modbus RTU)", [
            "Introducción a buses de campo industriales: ventajas de la comunicación por bus frente al cableado punto a punto tradicional.",
            "Redes PROFINET en TIA Portal: cable verde apantallado Cat 5e/Cat 6, conectores RJ45 industriales y topología en estrella/línea.",
            "Configuración del variador como dispositivo PROFINET IO Device en la vista de redes de TIA Portal.",
            "Palabra de control (Control Word - STW) y palabra de estado (Status Word - ZSW) bajo perfil PROFIdrive: bits de habilitación de pulsos, rampa y rearme de fallas.",
            "Consigna de velocidad en formato hexadecimal normalizado (4000H = 100% velocidad nominal)."
        ]),
        ("4.3 Interfaces de Supervisión Operativa (Pantallas HMI Básicas)", [
            "Concepto de interfaz Hombre-Máquina (HMI) en planta: paneles de operador Siemens SIMATIC KTP400 / KTP700 Basic.",
            "Creación de pantallas operativas en WinCC: botones de marcha/paro con confirmación, lámparas de señalización y campos de entrada/salida numérica.",
            "Diseño de visualizador de velocidad actual del motor (RPM / Hz) e indicador gráfico de barra para corriente consumida.",
            "Gestión visual de avisos de alarma activos y pantalla de registro histórico de eventos."
        ]),
        ("4.4 Metodología Estructurada de Diagnóstico de Averías (Troubleshooting)", [
            "Enfoque metódico frente al método empírico de adivinanza: las 5 preguntas del diagnóstico industrial sistemático.",
            "Estrategia de aislamiento de falla por capas: capa de alimentación general, capa de fuerza electromecánica, capa de sensores/entradas de campo, capa lógica de programa en PLC y capa de comunicaciones.",
            "Herramientas de diagnóstico de software: tabla de observación (Watch Table), forzado permanente de variables (Force Table) y buffer de diagnóstico de la CPU.",
            "Uso del multímetro y osciloscopio portátil en campo para descarte de caídas de tensión, ruido eléctrico y falsos contactos."
        ]),
        ("4.5 Normativa de Entrega, Dossier Técnico y Planos «As-Built»", [
            "Elaboración del dossier técnico final de la máquina según buenas prácticas de ingeniería.",
            "Actualización rigurosa de planos eléctricos «As-Built» (reflejando todas las modificaciones reales ejecutadas en el cableado de campo).",
            "Listado consolidado de entradas y salidas (I/O List) con descripción funcional, bornera asociada y número de cable.",
            "Manual de operación, tabla de códigos de falla y procedimiento de mantenimiento preventivo para el operador de planta."
        ]),
        ("4.6 Prácticas de Taller y Examen Práctico de Certificación", [
            "Práctica 4.1: Integración completa cableada: PLC S7-1200 gobernando rampa de arranque y frenado suave de un variador con motor trifásico.",
            "Práctica 4.2: Enlace por red PROFINET entre PLC y VFD: envío de consigna de frecuencia por bus y lectura cíclica de corriente del motor.",
            "Práctica 4.3: Diseño de pantalla HMI con botón de arranque, visualización de RPM reales y botón de reseteo de fallas.",
            "Práctica 4.4: Taller de simulación de fallas en planta: resolución de fallas reales inducidas (conductor desprendido, sensor descalibrado, sobrecarga simulada, error de bit en Ladder).",
            "Práctica 4.5: EXAMEN TERMINAL PRÁCTICO INDIVIDUAL DE CERTIFICACIÓN PROFESIONAL: Comisionamiento de celda integrada continua y resolución de 2 fallas inducidas en menos de 60 minutos (Umbral mínimo aprobatorio: 75 puntos)."
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
    # 3. REFERENCIAS Y NORMAS TÉCNICAS
    # ==========================================
    h1_3 = doc.add_paragraph()
    style_heading(h1_3, "3. Normas Internacionales y Manuales Técnicos de Referencia", level=1)

    referencias = [
        ("NFPA 70E:", "Standard for Electrical Safety in the Workplace (Edición 2024). National Fire Protection Association."),
        ("NFPA 70 / NEC:", "National Electrical Code (NEC). Artículos 430 (Motores), 409 (Tableros Industriales) y 250 (Puesta a Tierra)."),
        ("IEC 60617:", "Graphical Symbols for Diagrams. International Electrotechnical Commission."),
        ("IEC 61131-3:", "Programmable Controllers - Part 3: Programming Languages (LD, FBD, IL, ST, SFC)."),
        ("Siemens Industry Support:", "SIMATIC S7-1200 Programmable Controller System Manual (A5E02486680)."),
        ("Siemens AG:", "SINAMICS V20 Inverter Operating Instructions & Parameter Manual."),
        ("Schneider Electric:", "Altivar Machine ATV320 Programming and Installation Manuals."),
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
    run_f = footer_p.add_run("Fundación Kinal | Automatización y Control Eléctrico Industrial — Temario Oficial")
    run_f.font.name = "Calibri"
    run_f.font.size = Pt(8.5)
    run_f.font.color.rgb = COLOR_SECONDARY

    out_dir = os.path.join("Cursos", "Automatización")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "Temario_Curso_Automatizacion_Kinal.docx")
    doc.save(out_path)
    print(f"Temario guardado con éxito en: {out_path}")

if __name__ == "__main__":
    generate_temario_doc()
