import os
import re
import html
import json
import docx

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CURSOS_DIR = os.path.join(WORKSPACE_DIR, "Cursos")
WEB_DIR = os.path.join(CURSOS_DIR, "Web")
os.makedirs(WEB_DIR, exist_ok=True)

def parse_docx(path):
    doc = docx.Document(path)
    paras = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
    tables = []
    for t in doc.tables:
        rows = []
        for r in t.rows:
            rows.append([c.text.strip() for c in r.cells])
        tables.append(rows)
    return paras, tables

def clean_html(text):
    if not text:
        return ""
    return html.escape(text).replace('\n', '<br>')

# ==============================================================================
# 1. PARSE AUTOMATIZACIÓN
# ==============================================================================
auto_prop_p, auto_prop_t = parse_docx(os.path.join(CURSOS_DIR, "Automatización", "Propuesta_Curso_Automatizacion_Kinal.docx"))
auto_dos_p, auto_dos_t = parse_docx(os.path.join(CURSOS_DIR, "Automatización", "Dosificacion_y_Secuencia_Didactica_Automatizacion_Kinal.docx"))

auto_ficha = auto_prop_t[0]
auto_dqr = auto_prop_t[5]
auto_rubric = auto_dos_t[23]
auto_bitacora = auto_dos_t[24]

auto_sessions = []
# 4 Módulos de 5 sesiones cada uno (total 20 sesiones de 6h)
for idx in range(2, 22):
    t = auto_dos_t[idx]
    s_num = idx - 1
    t1_row = auto_dos_t[1][s_num] if s_num < len(auto_dos_t[1]) else ["", "", "", ""]
    
    obj = t[0][1]
    ap = t[1][1]
    des = t[2][1]
    cie = t[3][1]
    evi = t[4][1]
    eq = t[5][1]
    
    mod_name = t1_row[1] if len(t1_row) > 1 else f"Módulo {((s_num-1)//5)+1}"
    title_short = t1_row[2] if len(t1_row) > 2 else f"Sesión {s_num}"
    prod_obs = t1_row[3] if len(t1_row) > 3 else ""
    
    mod_num = ((s_num - 1) // 5) + 1
    bloque_num = ((s_num - 1) % 5) + 1

    auto_sessions.append({
        "num": s_num,
        "code": f"S-{s_num:02d}",
        "mod_num": mod_num,
        "sesion_bloque": f"Encuentro {bloque_num} de 5",
        "horario": "Sábados de 13:00 a 19:00 hrs (o Domingos)",
        "module": mod_name,
        "title": title_short,
        "duration": "6 Horas (360 min)",
        "objective": obj,
        "apertura": ap,
        "desarrollo": des,
        "cierre": cie,
        "evidencias": evi,
        "equipamiento": eq,
        "producto": prod_obs
    })

auto_modules_data = [
    {
        "num": 1,
        "title": "Control Eléctrico Industrial, Mando y Diseño de Tableros de Fuerza",
        "period": "MÓDULO 1 (Sesiones 1 a 5 • 30 Horas)",
        "hours": "30 Horas de Taller",
        "logro": "Construir y verificar en banco físico tableros de control electromagnético con contactores AC-3, enclavamientos, temporizadores y protecciones térmicas bajo normas IEC 60617 y NFPA 70E.",
        "topics": [
            {
                "num": 1,
                "title": "Seguridad Eléctrica Ocupacional y Normativa Internacional (NFPA 70E / LOTO)",
                "cat": "fuerza",
                "cat_name": "⚡ Fuerza & Maniobra",
                "cat_badge": "bg-amber-100 text-amber-900 border border-amber-200",
                "desc": "Peligros del choque y arco eléctrico (Arc Flash). Procedimiento estricto LOTO (bloqueo/etiquetado), prueba 'Test Before Touch' y aterramiento según NEC Art. 250."
            },
            {
                "num": 2,
                "title": "Simbología y Lectura de Planos Eléctricos Industriales (IEC vs NEMA)",
                "cat": "fuerza",
                "cat_name": "⚡ Fuerza & Maniobra",
                "cat_badge": "bg-amber-100 text-amber-900 border border-amber-200",
                "desc": "Esquemas unifilares y multifilares normalizados. Identificación alfanumérica de bornes y aparamenta. Simulación y diseño en CAD eléctrico (CADe SIMU)."
            },
            {
                "num": 3,
                "title": "Aparamenta Electromecánica de Fuerza y Maniobra (Contactores y Relés)",
                "cat": "fuerza",
                "cat_name": "⚡ Fuerza & Maniobra",
                "cat_badge": "bg-amber-100 text-amber-900 border border-amber-200",
                "desc": "Contactores de potencia (categorías AC-1, AC-3), contactos auxiliares instantáneos/temporizados, pulsadores industriales y setas de parada con enclavamiento."
            },
            {
                "num": 4,
                "title": "Cálculo, Dimensionamiento y Coordinación de Protecciones de Motor",
                "cat": "fuerza",
                "cat_name": "⚡ Fuerza & Maniobra",
                "cat_badge": "bg-amber-100 text-amber-900 border border-amber-200",
                "desc": "Cálculo de corriente nominal (In) y de arranque (Ia/In) en motores trifásicos. Curvas termomagnéticas B/C/D, relés bimetálicos calibrados al 100% In y guardamotores."
            },
            {
                "num": 5,
                "title": "Técnicas Profesionales de Montaje en Riel DIN y Tablero Estrella-Triángulo",
                "cat": "fuerza",
                "cat_name": "⚡ Fuerza & Maniobra",
                "cat_badge": "bg-amber-100 text-amber-900 border border-amber-200",
                "desc": "Peinado simétrico en canaleta ranurada, crimpado de terminales ferrule, segregación de fuerza y control, y arranque temporizado estrella-triángulo (Y-Δ)."
            }
        ]
    },
    {
        "num": 2,
        "title": "Parametrización, Control y Puesta en Marcha de Variadores de Frecuencia (VFD)",
        "period": "MÓDULO 2 (Sesiones 6 a 10 • 30 Horas)",
        "hours": "30 Horas de Taller",
        "logro": "Comisionar variadores de frecuencia industriales (Siemens/Schneider/WEG), programar rampas, multivelocidades, control analógico 0-10V/4-20mA y frenado dinámico por resistencia.",
        "topics": [
            {
                "num": 6,
                "title": "Topología Electrónica del VFD y Cableado de Potencia Apantallado",
                "cat": "vfd",
                "cat_name": "🔄 Variadores & Motores",
                "cat_badge": "bg-blue-100 text-blue-900 border border-blue-200",
                "desc": "Etapa rectificadora, bus DC intermedio e inversor IGBT con modulación PWM. Curvas V/f y control vectorial sensorless. Conexión a tierra equipotencial y cables blindados a 360°."
            },
            {
                "num": 7,
                "title": "Puesta en Marcha Rápida y Parametrización en Teclado (BOP)",
                "cat": "vfd",
                "cat_name": "🔄 Variadores & Motores",
                "cat_badge": "bg-blue-100 text-blue-900 border border-blue-200",
                "desc": "Carga de placa de características de motor (kW, V, A, RPM, Hz, cos φ). Rutina de identificación estática (Autotuning) y parametrización de rampas t-acc y t-dec."
            },
            {
                "num": 8,
                "title": "Control Remoto por Terminales Digitales y Modos de Multivelocidad",
                "cat": "vfd",
                "cat_name": "🔄 Variadores & Motores",
                "cat_badge": "bg-blue-100 text-blue-900 border border-blue-200",
                "desc": "Conexionado PNP (Source) y NPN (Sink) en entradas digitales. Modos de marcha a 2 y 3 hilos, inversión remota de giro y selección de velocidades fijas por código binario."
            },
            {
                "num": 9,
                "title": "Regulación Analógica Continua (0-10V / 4-20mA) y Calibración",
                "cat": "vfd",
                "cat_name": "🔄 Variadores & Motores",
                "cat_badge": "bg-blue-100 text-blue-900 border border-blue-200",
                "desc": "Control de velocidad variable con potenciómetro externo de 10 kΩ y lazo de instrumentación 4-20 mA. Calibración de umbrales de frecuencia mínima y máxima."
            },
            {
                "num": 10,
                "title": "Frenado Dinámico por Resistencia y Diagnóstico de Alarmas",
                "cat": "vfd",
                "cat_name": "🔄 Variadores & Motores",
                "cat_badge": "bg-blue-100 text-blue-900 border border-blue-200",
                "desc": "Energía regenerativa en bus DC, cálculo y conexión de resistencia de frenado con chopper. Diagnóstico de códigos de falla: sobrecorriente, sobretensión y sobretemperatura."
            }
        ]
    },
    {
        "num": 3,
        "title": "Programación y Cableado de Controladores Lógicos Programables (PLC Siemens)",
        "period": "MÓDULO 3 (Sesiones 11 a 15 • 30 Horas)",
        "hours": "30 Horas de Taller",
        "logro": "Desarrollar soluciones de automatización en TIA Portal para PLC Siemens S7-1200 en lenguaje Ladder (KOP), integrando sensores industriales, temporizadores, contadores y señales analógicas.",
        "topics": [
            {
                "num": 11,
                "title": "Arquitectura del PLC Siemens S7-1200 y Cableado de Entradas/Salidas",
                "cat": "plc",
                "cat_name": "💻 Programación PLC",
                "cat_badge": "bg-purple-100 text-purple-900 border border-purple-200",
                "desc": "Fuente de alimentación, CPU 1214C y módulos SM/SB. Cableado de entradas digitales Sink/Source y sensores inductivos/ópticos PNP y NPN. Salidas a relé vs transistor."
            },
            {
                "num": 12,
                "title": "Entorno TIA Portal, Configuración de Red IP y Tabla de Variables",
                "cat": "plc",
                "cat_name": "💻 Programación PLC",
                "cat_badge": "bg-purple-100 text-purple-900 border border-purple-200",
                "desc": "Estructura de proyectos TIA Portal, asignación de IP estática en Industrial Ethernet, diagnóstico online y creación de la tabla de variables del autómata (PLC Tags)."
            },
            {
                "num": 13,
                "title": "Lógica de Contactos Ladder (KOP): Enclavamientos y Flancos",
                "cat": "plc",
                "cat_name": "💻 Programación PLC",
                "cat_badge": "bg-purple-100 text-purple-900 border border-purple-200",
                "desc": "Ciclo de scan (PII/PIQ), compuertas lógicas básicas, bobinas Set (S) y Reset (R), y detección de flancos ascendentes (P_TRIG) y descendentes (N_TRIG)."
            },
            {
                "num": 14,
                "title": "Temporizadores (TON/TOF/TP) y Contadores para Rutinas Secuenciales",
                "cat": "plc",
                "cat_name": "💻 Programación PLC",
                "cat_badge": "bg-purple-100 text-purple-900 border border-purple-200",
                "desc": "Estructura IEC_TIMER, predeterminación PT y transcurrido ET. Contadores ascendentes (CTU) y descendentes (CTD) aplicados a líneas de empaque y lotes de producción."
            },
            {
                "num": 15,
                "title": "Tratamiento de Señales Analógicas (NORM_X / SCALE_X) y Comparadores",
                "cat": "plc",
                "cat_name": "💻 Programación PLC",
                "cat_badge": "bg-purple-100 text-purple-900 border border-purple-200",
                "desc": "Conversión de cuentas digitales (0-27648) a unidades de ingeniería reales. Comparadores numéricos aplicados a control de nivel con histéresis y alarmas."
            }
        ]
    },
    {
        "num": 4,
        "title": "Integración Automatizada, Redes Industriales y Diagnóstico de Averías",
        "period": "MÓDULO 4 (Sesiones 16 a 20 • 30 Horas)",
        "hours": "30 Horas de Taller",
        "logro": "Integrar el sistema completo PLC-VFD mediante bus PROFINET y control cableado, diseñar pantallas de operador HMI WinCC, resolver averías inducidas y sustentar el examen terminal.",
        "topics": [
            {
                "num": 16,
                "title": "Integración Cableada de Mando y Consignas de Velocidad PLC-VFD",
                "cat": "redes",
                "cat_name": "🌐 Redes & Diagnóstico",
                "cat_badge": "bg-emerald-100 text-emerald-900 border border-emerald-200",
                "desc": "Gobierno de marcha, paro, sentido de giro y rampas desde salidas digitales y analógicas del PLC hacia las borneras del variador. Verificación de interbloqueos de seguridad."
            },
            {
                "num": 17,
                "title": "Comunicación Industrial PROFINET: Mapeo de Palabras STW y ZSW",
                "cat": "redes",
                "cat_name": "🌐 Redes & Diagnóstico",
                "cat_badge": "bg-emerald-100 text-emerald-900 border border-emerald-200",
                "desc": "Configuración del variador como dispositivo IO Device en TIA Portal. Transmisión de la palabra de control (STW), de estado (ZSW) y consigna de velocidad hexadecimal (PROFIdrive)."
            },
            {
                "num": 18,
                "title": "Supervisión Operativa en Pantallas Táctiles HMI (WinCC Basic)",
                "cat": "redes",
                "cat_name": "🌐 Redes & Diagnóstico",
                "cat_badge": "bg-emerald-100 text-emerald-900 border border-emerald-200",
                "desc": "Diseño en panel Siemens SIMATIC KTP400/KTP700: botones de marcha/paro con confirmación, visualización numérica de RPM, gráficos de barras de corriente y gestión de alarmas."
            },
            {
                "num": 19,
                "title": "Metodología Estructurada de Diagnóstico de Averías (Troubleshooting)",
                "cat": "redes",
                "cat_name": "🌐 Redes & Diagnóstico",
                "cat_badge": "bg-emerald-100 text-emerald-900 border border-emerald-200",
                "desc": "Aislamiento sistemático en 5 capas: alimentación, fuerza, sensórica, lógica de programa y comunicaciones. Uso de tablas de observación (Watch Table) y buffer de la CPU."
            },
            {
                "num": 20,
                "title": "Evaluación Terminal Práctica de Certificación y Dossier As-Built",
                "cat": "redes",
                "cat_name": "🌐 Redes & Diagnóstico",
                "cat_badge": "bg-emerald-100 text-emerald-900 border border-emerald-200",
                "desc": "Puesta en marcha autónoma de la celda de embotellado continuo y resolución de 2 fallas inducidas en menos de 60 minutos ante el jurado Kinal (umbral ≥ 75 pts)."
            }
        ]
    }
]

# ==============================================================================
# 2. PARSE CABLEADO ESTRUCTURADO
# ==============================================================================
cable_prop_p, cable_prop_t = parse_docx(os.path.join(CURSOS_DIR, "Cableado_Estructurado", "Propuesta_Curso_Cableado_Estructurado_Kinal.docx"))
cable_dos_p, cable_dos_t = parse_docx(os.path.join(CURSOS_DIR, "Cableado_Estructurado", "Dosificacion_y_Secuencia_Didactica_Cableado_Estructurado_Kinal.docx"))

cable_ficha = cable_prop_t[0]
cable_dqr = cable_prop_t[5]
cable_rubric = cable_dos_t[23]
cable_bitacora = cable_dos_t[24]

cable_sessions = []
# 10 Semanas (2 sesiones por semana: Martes y Jueves, total 20 sesiones de 4h)
for idx in range(2, 22):
    t = cable_dos_t[idx]
    s_num = idx - 1
    t1_row = cable_dos_t[1][s_num] if s_num < len(cable_dos_t[1]) else ["", "", "", ""]
    
    obj = t[0][1]
    ap = t[1][1]
    des = t[2][1]
    cie = t[3][1]
    evi = t[4][1]
    eq = t[5][1]
    
    mod_name = t1_row[1] if len(t1_row) > 1 else f"Módulo {((s_num-1)//5)+1}"
    title_short = t1_row[2] if len(t1_row) > 2 else f"Sesión {s_num}"
    prod_obs = t1_row[3] if len(t1_row) > 3 else ""
    
    semana_num = ((s_num - 1) // 2) + 1
    dia_semana = "Martes" if (s_num % 2 == 1) else "Jueves"

    cable_sessions.append({
        "num": s_num,
        "code": f"S-{s_num:02d}",
        "semana": f"Semana {semana_num}",
        "dia": dia_semana,
        "horario": f"{dia_semana} de 17:30 a 21:30 hrs",
        "module": mod_name,
        "title": title_short,
        "duration": "4 Horas (240 min)",
        "objective": obj,
        "apertura": ap,
        "desarrollo": des,
        "cierre": cie,
        "evidencias": evi,
        "equipamiento": eq,
        "producto": prod_obs
    })

cable_modules_data = [
    {
        "num": 1,
        "title": "Normas ANSI/TIA, Espacios y Canalizaciones Físicas (TR, ER, Racks)",
        "period": "MÓDULO 1 (Sesiones 1 a 5 • 20 Horas)",
        "hours": "20 Horas Pedagógicas",
        "logro": "Planificar la topología jerárquica del edificio corporativo, calcular factores de llenado en ductos EMT/charolas según TIA-569 y armar y anclar racks de 19'' (42U).",
        "topics": [
            {
                "num": 1,
                "title": "Normativa Internacional y Subsistemas del Cableado (ANSI/TIA-568-E)",
                "cat": "normas",
                "cat_name": "📐 Normas & Espacios",
                "cat_badge": "bg-blue-100 text-blue-900 border border-blue-200",
                "desc": "Estándares ANSI/TIA-568.0-E/1-E e ISO/IEC 11801. Los 6 subsistemas: Área de Trabajo, Horizontal, Backbone, TR, ER y Entrada de Servicios en topología estrella jerárquica."
            },
            {
                "num": 2,
                "title": "Espacios de Telecomunicaciones según ANSI/TIA-569-E (TR y ER)",
                "cat": "normas",
                "cat_name": "📐 Normas & Espacios",
                "cat_badge": "bg-blue-100 text-blue-900 border border-blue-200",
                "desc": "Climatización HVAC (18°C-24°C), control de humedad, iluminación antideslumbrante, pisos ESD, pintura ignífuga en madera terciada y circuitos eléctricos dedicados NEMA 5-20R."
            },
            {
                "num": 3,
                "title": "Canalizaciones Físicas y Tubería Conduit Metálica EMT",
                "cat": "normas",
                "cat_name": "📐 Normas & Espacios",
                "cat_badge": "bg-blue-100 text-blue-900 border border-blue-200",
                "desc": "Regla de factor de llenado del 40% inicial / 60% futuro. Curvado manual con doblador a 90°, radios mínimos de curvatura y distancias de separación de líneas eléctricas (NFPA 70)."
            },
            {
                "num": 4,
                "title": "Charolas Portacables Tipo Canastilla y Bajadas Suaves a Racks",
                "cat": "normas",
                "cat_name": "📐 Normas & Espacios",
                "cat_badge": "bg-blue-100 text-blue-900 border border-blue-200",
                "desc": "Montaje de charola aérea electrogalvanizada con soportes trapecio y varilla roscada. Accesorios de unión y bajadas en cascada para evitar estrangulamiento de mazos."
            },
            {
                "num": 5,
                "title": "Bastidores de 19 Pulgadas, Gabinetes y Anclaje Antisísmico",
                "cat": "normas",
                "cat_name": "📐 Normas & Espacios",
                "cat_badge": "bg-blue-100 text-blue-900 border border-blue-200",
                "desc": "Estándar EIA-310-D (1U = 44.45 mm). Armado, nivelación de burbuja y anclaje al piso de concreto con taquetes expansivos en rack abierto de 42U y gabinete abatible."
            }
        ]
    },
    {
        "num": 2,
        "title": "Cableado de Cobre de Alto Rendimiento (Cat 6 / Cat 6A) y Aterrizaje TIA-607",
        "period": "MÓDULO 2 (Sesiones 6 a 10 • 20 Horas)",
        "hours": "20 Horas Pedagógicas",
        "logro": "Rematar tomas de pared y patch panels de 24 puertos en Cat 6A con destrenzado mínimo (< 13 mm), peinado con velcro e interconectar la barra equipotencial TGB bajo TIA-607.",
        "topics": [
            {
                "num": 6,
                "title": "Física del Par Trenzado Balanceado (Cat 6A F/UTP) y Rechazo EMI",
                "cat": "cobre",
                "cat_name": "🔌 Cobre & PoE++",
                "cat_badge": "bg-amber-100 text-amber-900 border border-amber-200",
                "desc": "Transmisión diferencial a 500 MHz (10 Gbps a 100 m). Estructura apantallada F/UTP, hilo de drenaje y conductores 100% cobre virgen AWG 23 (riesgos de cables CCA fraudulentos)."
            },
            {
                "num": 7,
                "title": "Conectorización de Jacks Keystone Cat 6A bajo Esquema T568B",
                "cat": "cobre",
                "cat_name": "🔌 Cobre & PoE++",
                "cat_badge": "bg-amber-100 text-amber-900 border border-amber-200",
                "desc": "Asignación de pines RJ45, desforre sin muescas y remate con herramienta de impacto 110. Regla de oro del destrenzado < 0.5'' (13 mm) para evitar paradiafonía (NEXT)."
            },
            {
                "num": 8,
                "title": "Armado de Patch Panels de 24 Puertos y Organización en Rack",
                "cat": "cobre",
                "cat_name": "🔌 Cobre & PoE++",
                "cat_badge": "bg-amber-100 text-amber-900 border border-amber-200",
                "desc": "Remate posterior en paneles modulares de 1U, barras de alivio mecánico, distribución balanceada izquierda/derecha y comprobación preliminar de mapa de hilos (wiremap)."
            },
            {
                "num": 9,
                "title": "Sistema de Puesta a Tierra para Telecomunicaciones (ANSI/TIA-607-D)",
                "cat": "cobre",
                "cat_name": "🔌 Cobre & PoE++",
                "cat_badge": "bg-amber-100 text-amber-900 border border-amber-200",
                "desc": "Propósito de equipotencialidad. Instalación de barra TGB en rack, conductor BCT de cobre calibre 6 AWG y aterrizaje del blindaje de patch panels con resistencia < 0.1 Ω."
            },
            {
                "num": 10,
                "title": "Peinado Prolijo de Mazos con Velcro y Alimentación PoE++",
                "cat": "cobre",
                "cat_name": "🔌 Cobre & PoE++",
                "cat_badge": "bg-amber-100 text-amber-900 border border-amber-200",
                "desc": "Peinado con peines de cables guía y sujeción exclusiva con cinchos textiles de velcro (cero aplastamiento). Consideraciones térmicas de PoE++ (IEEE 802.3bt hasta 90W)."
            }
        ]
    },
    {
        "num": 3,
        "title": "Infraestructura de Fibra Óptica, Conectorización y Empalme por Fusión",
        "period": "MÓDULO 3 (Sesiones 11 a 15 • 20 Horas)",
        "hours": "20 Horas Pedagógicas",
        "logro": "Ejecutar empalmes por fusión con fusionadora de arco voltaico (pérdida < 0.05 dB), horneado de manguitos, acomodo en bandejas ODF y pruebas de continuidad láser VFL.",
        "topics": [
            {
                "num": 11,
                "title": "Principios de Transmisión Óptica: Monomodo (OS2) vs Multimodo (OM4)",
                "cat": "fibra",
                "cat_name": "💡 Fibra & Fusión",
                "cat_badge": "bg-purple-100 text-purple-900 border border-purple-200",
                "desc": "Índice de refracción y reflexión interna total. Núcleo de 9 µm (1310/1550 nm) vs 50 µm con láser VCSEL (850/1300 nm). Atenuación intrínseca, macrocurvaturas y seguridad ocular."
            },
            {
                "num": 12,
                "title": "Preparación y Pelado de Cable Óptico de Estructura Ajustada",
                "cat": "fibra",
                "cat_name": "💡 Fibra & Fusión",
                "cat_badge": "bg-purple-100 text-purple-900 border border-purple-200",
                "desc": "Tijeras para corte de Kevlar y peladora de fibra de 3 muescas (chaqueta, búfer 900 µm y recubrimiento 250 µm). Limpieza ultrasuave del vidrio con alcohol isopropílico al 99%."
            },
            {
                "num": 13,
                "title": "Corte de Precisión con Cleaver de Diamante (< 1° de Desviación)",
                "cat": "fibra",
                "cat_name": "💡 Fibra & Fusión",
                "cat_badge": "bg-purple-100 text-purple-900 border border-purple-200",
                "desc": "Operación de la cortadora de alta precisión, ajuste de longitud de corte (10-16 mm) y verificación microscópica de caras terminales perpendiculares antes de la fusión."
            },
            {
                "num": 14,
                "title": "Empalme por Fusión de Fibra Óptica con Arco Voltaico",
                "cat": "fibra",
                "cat_name": "💡 Fibra & Fusión",
                "cat_badge": "bg-purple-100 text-purple-900 border border-purple-200",
                "desc": "Alineación automática por ranuras en V (V-Groove) o núcleos (PAS). Fusión de pigtails LC con atenuación estimada < 0.05 dB y horneado térmico de manguitos termocontráctiles."
            },
            {
                "num": 15,
                "title": "Montaje en Bandeja Distribuidora ODF de 1U y Verificación VFL",
                "cat": "fibra",
                "cat_name": "💡 Fibra & Fusión",
                "cat_badge": "bg-purple-100 text-purple-900 border border-purple-200",
                "desc": "Ruteo circular de pigtails en casete respetando radio mínimo de 30 mm. Conexión de acopladores dúplex LC y comprobación visual de continuidad con localizador de fallas (VFL 650 nm)."
            }
        ]
    },
    {
        "num": 4,
        "title": "Certificación Instrumental con Fluke, Rotulado TIA-606 y Proyecto As-Built",
        "period": "MÓDULO 4 (Sesiones 16 a 20 • 20 Horas)",
        "hours": "20 Horas Pedagógicas",
        "logro": "Certificar enlaces permanentes Cat 6A con certificador Fluke DSX, medir atenuación óptica Tier 1 con OPM, rotular bajo TIA-606 y entregar la carpeta técnica As-Built.",
        "topics": [
            {
                "num": 16,
                "title": "Certificación Tier 1 de Cobre con Escáner Fluke Networks DSX",
                "cat": "certificacion",
                "cat_name": "📊 Certificación & As-Built",
                "cat_badge": "bg-emerald-100 text-emerald-900 border border-emerald-200",
                "desc": "Enlace Permanente (Permanent Link máx. 90 m) vs Canal (Channel máx. 100 m). Calibración de unidades Main/Remote, selección de norma TIA Cat 6A y valor NVP de propagación."
            },
            {
                "num": 17,
                "title": "Interpretación Diagnóstica de Gráficas de Alta Frecuencia (Fluke)",
                "cat": "certificacion",
                "cat_name": "📊 Certificación & As-Built",
                "cat_badge": "bg-emerald-100 text-emerald-900 border border-emerald-200",
                "desc": "Wiremap, Insertion Loss, NEXT/PS-NEXT y Return Loss. Localización milimétrica de anomalías mediante reflectometría en el dominio del tiempo (TDNXT y TDR)."
            },
            {
                "num": 18,
                "title": "Certificación Óptica Tier 1 con Medidor de Potencia (OPM) y Fuente",
                "cat": "certificacion",
                "cat_name": "📊 Certificación & As-Built",
                "cat_badge": "bg-emerald-100 text-emerald-900 border border-emerald-200",
                "desc": "Método de referencia óptica de 1 puente según TIA-526-14. Cálculo del presupuesto de pérdida admisible (Loss Budget) y verificación de pérdidas totales en dB en ambas ventanas."
            },
            {
                "num": 19,
                "title": "Administración y Rotulado Normalizado según ANSI/TIA-606-D",
                "cat": "certificacion",
                "cat_name": "📊 Certificación & As-Built",
                "cat_badge": "bg-emerald-100 text-emerald-900 border border-emerald-200",
                "desc": "Nomenclatura jerárquica formal (Edificio-Piso-TR-Rack-Panel-Puerto). Rotulación indeleble por transferencia térmica en cables, faceplates y patch panels con etiquetas de vinil."
            },
            {
                "num": 20,
                "title": "Evaluación Terminal Práctica de Certificación y Dossier As-Built",
                "cat": "certificacion",
                "cat_name": "📊 Certificación & As-Built",
                "cat_badge": "bg-emerald-100 text-emerald-900 border border-emerald-200",
                "desc": "Certificación completa de un rack departamental, resolución de 3 enlaces con fallas inducidas, exportación de reportes LinkWare y entrega de planos As-Built (umbral ≥ 75 pts)."
            }
        ]
    }
]

# ==============================================================================
# GENERADORES DE TARJETAS MODULARES PARA TEMARIO
# ==============================================================================
def build_modular_temario_html(modules):
    cards_html = ""
    for mod in modules:
        topics_items = ""
        for t in mod["topics"]:
            topics_items += f"""
            <div class="content-item item-{t['cat']} p-3.5 rounded-xl text-xs space-y-1.5 transition border border-slate-200/90 bg-white hover:bg-slate-50 shadow-sm" data-category="{t['cat']}">
                <div class="flex flex-wrap justify-between items-center gap-1.5 font-bold">
                    <span class="text-slate-900 text-sm flex items-center gap-2">
                        <span class="w-5 h-5 rounded-full bg-slate-100 text-slate-700 text-xs font-black flex items-center justify-center shrink-0">{t['num']}</span>
                        {clean_html(t['title'])}
                    </span>
                    <span class="px-2.5 py-0.5 rounded-full text-[10px] font-extrabold uppercase {t['cat_badge']}">
                        {clean_html(t['cat_name'])}
                    </span>
                </div>
                <p class="text-slate-600 leading-relaxed pl-7">{clean_html(t['desc'])}</p>
            </div>
            """
        
        cards_html += f"""
        <div class="bg-white rounded-2xl border border-slate-300 shadow-sm overflow-hidden flex flex-col hover:shadow-md transition">
            <div class="bg-slate-900 text-white p-4 sm:p-5 border-b border-slate-800 space-y-1">
                <div class="flex flex-wrap justify-between items-center text-xs text-amber-400 font-semibold mb-1 gap-2">
                    <span>{clean_html(mod['period'])}</span>
                    <span class="px-2 py-0.5 rounded bg-blue-900/60 text-blue-200 border border-blue-400/30 text-[11px] font-bold">{clean_html(mod['hours'])}</span>
                </div>
                <h4 class="text-base sm:text-lg font-bold text-white leading-snug">{clean_html(mod['title'])}</h4>
                <p class="text-xs text-slate-300 pt-1 leading-relaxed">
                    <strong class="text-amber-300">Logro esperado:</strong> {clean_html(mod['logro'])}
                </p>
            </div>
            <div class="p-4 sm:p-5 divide-y divide-slate-100 flex-1 space-y-2.5 bg-slate-50/50">
                {topics_items}
            </div>
        </div>
        """
    return cards_html

auto_modular_cards = build_modular_temario_html(auto_modules_data)
cable_modular_cards = build_modular_temario_html(cable_modules_data)

# ==============================================================================
# GENERADORES DE FICHA TÉCNICA UNIFICADA
# ==============================================================================
def build_single_card_ficha(ficha_rows, code):
    rows_html = ""
    for r in ficha_rows:
        rows_html += f"""
        <div class="py-3 sm:grid sm:grid-cols-3 sm:gap-4 flex flex-col">
            <dt class="font-bold text-slate-900 text-xs sm:col-span-1">{clean_html(r[0])}</dt>
            <dd class="text-slate-700 text-xs sm:col-span-2 mt-0.5 sm:mt-0 leading-relaxed">{clean_html(r[1])}</dd>
        </div>
        """
    
    return f"""
    <div class="bg-white rounded-3xl border border-slate-200 p-6 sm:p-8 shadow-sm space-y-5">
        <div class="flex flex-wrap items-center justify-between border-b border-slate-200 pb-4 gap-2">
            <div class="flex items-center gap-2">
                <span class="w-8 h-8 rounded-lg bg-blue-50 text-blue-900 flex items-center justify-center font-black">
                    <i data-lucide="file-badge" class="w-4 h-4"></i>
                </span>
                <h3 class="text-xl font-black text-slate-900">
                    Ficha Técnica Oficial del Programa
                </h3>
            </div>
            <span class="px-3 py-1 rounded-full bg-blue-50 text-blue-900 text-xs font-bold border border-blue-200">
                Código: {clean_html(code)}
            </span>
        </div>
        <div class="divide-y divide-slate-100">
            {rows_html}
        </div>
    </div>
    """

auto_ficha_single_card = build_single_card_ficha(auto_ficha, "AUTO-2026-KINAL")
cable_ficha_single_card = build_single_card_ficha(cable_ficha, "CABLE-2026-KINAL")

# ==============================================================================
# GENERADORES DE CALENDARIOS CRONOLÓGICOS
# ==============================================================================
def build_auto_calendar_html(sessions):
    blocks = [
        (1, "Módulo 1: Control Eléctrico y Tableros (5 Encuentros)", [s for s in sessions if s["mod_num"] == 1]),
        (2, "Módulo 2: Variadores de Frecuencia VFD (5 Encuentros)", [s for s in sessions if s["mod_num"] == 2]),
        (3, "Módulo 3: Programación PLCs Siemens (5 Encuentros)", [s for s in sessions if s["mod_num"] == 3]),
        (4, "Módulo 4: Integración & Redes PROFINET (5 Encuentros)", [s for s in sessions if s["mod_num"] == 4])
    ]
    html_out = ""
    for b_num, b_title, b_sessions in blocks:
        cards = ""
        for s in b_sessions:
            cards += f"""
            <div class="bg-white rounded-xl border border-slate-200 p-4 shadow-sm hover:border-amber-600 hover:shadow-md transition flex flex-col justify-between space-y-3">
                <div class="space-y-1.5">
                    <div class="flex justify-between items-center text-[11px]">
                        <span class="font-black px-2 py-0.5 rounded bg-slate-900 text-amber-300">{s['code']}</span>
                        <span class="font-bold text-slate-500">{s['sesion_bloque']}</span>
                    </div>
                    <h5 class="font-bold text-slate-900 text-xs leading-snug">{clean_html(s['title'])}</h5>
                    <p class="text-[11px] text-slate-500 line-clamp-2">{clean_html(s['objective'])}</p>
                </div>
                <div class="pt-2 border-t border-slate-100 flex items-center justify-between text-[11px]">
                    <span class="text-amber-800 font-semibold">{s['duration']}</span>
                    <button onclick="goToSession({s['num']})" class="text-blue-700 font-bold hover:underline flex items-center gap-0.5">
                        Ver Secuencia →
                    </button>
                </div>
            </div>
            """
        html_out += f"""
        <div class="bg-slate-50 rounded-2xl border border-slate-200 p-5 space-y-3">
            <div class="flex items-center justify-between border-b border-slate-200 pb-2">
                <h4 class="font-black text-slate-900 text-base flex items-center gap-2">
                    <i data-lucide="zap" class="w-4 h-4 text-amber-600"></i> {b_title}
                </h4>
                <span class="text-xs font-bold text-slate-500">30 Horas de Taller</span>
            </div>
            <div class="grid sm:grid-cols-2 lg:grid-cols-5 gap-3">
                {cards}
            </div>
        </div>
        """
    return html_out

def build_cable_calendar_html(sessions):
    weeks_html = ""
    for w in range(1, 11):
        w_sessions = [s for s in sessions if s["semana"] == f"Semana {w}"]
        cards = ""
        for s in w_sessions:
            cards += f"""
            <div class="bg-white rounded-xl border border-slate-200 p-4 shadow-sm hover:border-cyan-600 hover:shadow-md transition flex flex-col justify-between space-y-3">
                <div class="space-y-1.5">
                    <div class="flex justify-between items-center text-[11px]">
                        <span class="font-black px-2 py-0.5 rounded bg-slate-900 text-cyan-300">{s['code']}</span>
                        <span class="font-bold text-cyan-800 bg-cyan-50 px-2 py-0.5 rounded">{s['dia']} (17:30 - 21:30)</span>
                    </div>
                    <h5 class="font-bold text-slate-900 text-xs leading-snug">{clean_html(s['title'])}</h5>
                    <p class="text-[11px] text-slate-500 line-clamp-2">{clean_html(s['objective'])}</p>
                </div>
                <div class="pt-2 border-t border-slate-100 flex items-center justify-between text-[11px]">
                    <span class="text-slate-600 font-semibold">{s['duration']}</span>
                    <button onclick="goToSession({s['num']})" class="text-cyan-700 font-bold hover:underline flex items-center gap-0.5">
                        Ver Secuencia →
                    </button>
                </div>
            </div>
            """
        weeks_html += f"""
        <div class="bg-slate-50 rounded-2xl border border-slate-200 p-4 space-y-3">
            <div class="flex items-center justify-between border-b border-slate-200 pb-2">
                <h4 class="font-black text-slate-900 text-sm flex items-center gap-2">
                    <i data-lucide="network" class="w-4 h-4 text-cyan-700"></i> Semana {w}
                </h4>
                <span class="text-xs font-bold text-slate-500">2 Sesiones (8 Horas)</span>
            </div>
            <div class="grid sm:grid-cols-2 gap-3">
                {cards}
            </div>
        </div>
        """
    return f'<div class="grid lg:grid-cols-2 gap-4">{weeks_html}</div>'

auto_calendar_content = build_auto_calendar_html(auto_sessions)
cable_calendar_content = build_cable_calendar_html(cable_sessions)

# Rúbricas
def build_rubric_rows_html(rubric):
    return "".join([f"""
    <tr class="hover:bg-slate-50/80 transition">
        <td class="py-3.5 px-4 font-bold text-slate-900 bg-slate-50 border-r border-slate-200 align-top">{clean_html(row[0])}</td>
        <td class="py-3 px-4 text-blue-950 font-bold bg-blue-50/20 border-r border-slate-200 align-top text-center">{clean_html(row[1])}</td>
        <td class="py-3 px-4 text-emerald-950 bg-emerald-50/30 border-r border-slate-200 align-top">{clean_html(row[2])}</td>
        <td class="py-3 px-4 text-rose-950 bg-rose-50/30 align-top text-xs">{clean_html(row[3])}</td>
    </tr>
    """ for r_idx, row in enumerate(rubric) if r_idx > 0])

auto_rubric_rows = build_rubric_rows_html(auto_rubric)
cable_rubric_rows = build_rubric_rows_html(cable_rubric)

# Bitácoras
def build_bitacora_table_html(bitacora):
    rows = ""
    for r in bitacora:
        rows += f"""
        <tr class="hover:bg-slate-50 transition">
            <td class="py-2.5 px-4 font-bold text-slate-900 bg-slate-50 border-r border-slate-200 align-top text-xs w-1/3">{clean_html(r[0])}</td>
            <td class="py-2.5 px-4 text-slate-700 align-top text-xs leading-relaxed">{clean_html(r[1])}</td>
        </tr>
        """
    return f"""
    <div class="bg-white rounded-3xl border border-slate-200 p-6 sm:p-8 shadow-sm space-y-4">
        <div class="flex items-center justify-between border-b border-slate-200 pb-3">
            <h4 class="font-black text-slate-900 text-base flex items-center gap-2">
                <i data-lucide="clipboard-check" class="w-5 h-5 text-blue-700"></i>
                Estructura de la Bitácora de Taller («Berichtsheft»)
            </h4>
            <span class="px-2.5 py-1 rounded-full bg-blue-100 text-blue-900 font-bold text-xs">Visado Semanal Obligatorio</span>
        </div>
        <p class="text-xs text-slate-600">
            Formato oficial de registro de evidencias técnico-prácticas que cada aprendiz completa al finalizar su turno de laboratorio.
        </p>
        <div class="overflow-x-auto border border-slate-200 rounded-2xl">
            <table class="w-full text-left border-collapse divide-y divide-slate-100">
                <tbody>
                    {rows}
                </tbody>
            </table>
        </div>
    </div>
    """

auto_bitacora_card = build_bitacora_table_html(auto_bitacora)
cable_bitacora_card = build_bitacora_table_html(cable_bitacora)

print("Datos parseados correctamente. Generando páginas...")

# ==============================================================================
# HTML BUILDER: AUTOMATIZACION.HTML
# ==============================================================================
auto_sessions_json = json.dumps(auto_sessions, ensure_ascii=False)

automatizacion_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Automatización y Control Eléctrico Industrial con PLC y VFD | Kinal 2026</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@500;700;800;900&display=swap');
        body {{ font-family: 'Inter', sans-serif; background-color: #f8fafc; color: #0f172a; }}
        h1, h2, h3, h4, .font-heading {{ font-family: 'Space Grotesk', sans-serif; }}
        .hero-pattern {{
            background: linear-gradient(135deg, #09172e 0%, #172554 50%, #9a3412 100%);
        }}
        .tab-btn.active {{
            background-color: #003366;
            color: #ffffff;
            font-weight: 700;
        }}
        .session-item.active {{
            background-color: #003366;
            color: #ffffff;
            border-color: #003366;
        }}
        .session-item.active span, .session-item.active p {{
            color: #e2e8f0;
        }}
        .session-item.active .badge-code {{
            background-color: #f59e0b;
            color: #0f172a;
        }}
    </style>
</head>
<body class="antialiased min-h-screen flex flex-col">

    <!-- Top Navigation Header -->
    <header class="bg-slate-950 text-white border-b border-slate-800 sticky top-0 z-50 shadow-md">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3 flex flex-wrap justify-between items-center gap-4">
            <div class="flex items-center gap-3">
                <a href="index.html" class="bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-bold px-3 py-1.5 rounded-lg transition flex items-center gap-1.5">
                    <i data-lucide="arrow-left" class="w-3.5 h-3.5"></i> Cursos
                </a>
                <span class="text-slate-600">|</span>
                <div class="text-slate-200 font-bold text-xs sm:text-sm flex items-center gap-2">
                    <i data-lucide="zap" class="w-4 h-4 text-amber-400"></i>
                    Automatización & Control Eléctrico Industrial con PLC y VFD
                </div>
            </div>
            
            <!-- Quick Download Buttons -->
            <div class="flex items-center gap-2 text-xs">
                <span class="text-slate-400 hidden sm:inline">Word:</span>
                <a href="../Automatización/Propuesta_Curso_Automatizacion_Kinal.docx" download class="px-2.5 py-1 rounded bg-blue-900/60 hover:bg-blue-800 text-blue-200 transition font-medium" title="Descargar Propuesta Oficial">
                    Propuesta
                </a>
                <a href="../Automatización/Temario_Curso_Automatizacion_Kinal.docx" download class="px-2.5 py-1 rounded bg-emerald-900/60 hover:bg-emerald-800 text-emerald-200 transition font-medium" title="Descargar Temario Oficial">
                    Temario
                </a>
                <a href="../Automatización/Dosificacion_y_Secuencia_Didactica_Automatizacion_Kinal.docx" download class="px-2.5 py-1 rounded bg-amber-900/60 hover:bg-amber-800 text-amber-200 transition font-medium" title="Descargar Dosificación Oficial">
                    Dosificación
                </a>
            </div>
        </div>
    </header>

    <!-- Hero Course Banner -->
    <section class="hero-pattern text-white py-10 px-4 sm:px-6 lg:px-8">
        <div class="max-w-7xl mx-auto space-y-3">
            <div class="flex flex-wrap items-center gap-2">
                <span class="px-3 py-1 rounded-full bg-amber-500/20 border border-amber-400/30 text-amber-300 text-xs font-bold tracking-wide uppercase">
                    Especialidad Práctica en Laboratorios de Potencia
                </span>
                <span class="px-3 py-1 rounded-full bg-blue-500/20 border border-blue-400/30 text-blue-300 text-xs font-bold">
                    DQR Nivel 4 - 5
                </span>
                <span class="px-3 py-1 rounded-full bg-emerald-500/20 border border-emerald-400/30 text-emerald-300 text-xs font-bold">
                    Aprobación: ≥ 75 Pts
                </span>
            </div>
            <h1 class="text-2xl sm:text-4xl font-black tracking-tight leading-tight">
                Automatización y Control Eléctrico Industrial con PLC y Variadores de Frecuencia (VFD)
            </h1>
            <p class="text-slate-300 text-xs sm:text-sm max-w-4xl leading-relaxed">
                Control electromagnético de potencia, seguridad eléctrica bajo norma NFPA 70E / LOTO, parametrización de variadores de frecuencia comerciales, programación en TIA Portal para PLC Siemens S7-1200, comunicación por red industrial PROFINET y diagnóstico estructurado de fallas en líneas continuas.
            </p>
        </div>
    </section>

    <!-- Tab Bar Navigation (UNA SOLA PALABRA, SIN NUMERACIÓN) -->
    <div class="bg-white border-b border-slate-200 sticky top-14 z-40 shadow-sm">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <nav class="flex space-x-2 sm:space-x-3 py-2.5 overflow-x-auto text-xs font-bold">
                <button onclick="switchTab('propuesta')" id="btn-propuesta" class="tab-btn active px-4 py-2 rounded-xl transition flex items-center gap-1.5 shrink-0">
                    <i data-lucide="file-text" class="w-3.5 h-3.5"></i> Propuesta
                </button>
                <button onclick="switchTab('temario')" id="btn-temario" class="tab-btn px-4 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 transition flex items-center gap-1.5 shrink-0">
                    <i data-lucide="list-tree" class="w-3.5 h-3.5"></i> Temario
                </button>
                <button onclick="switchTab('calendario')" id="btn-calendario" class="tab-btn px-4 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 transition flex items-center gap-1.5 shrink-0">
                    <i data-lucide="calendar" class="w-3.5 h-3.5"></i> Calendario
                </button>
                <button onclick="switchTab('secuencias')" id="btn-secuencias" class="tab-btn px-4 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 transition flex items-center gap-1.5 shrink-0">
                    <i data-lucide="layers" class="w-3.5 h-3.5"></i> Secuencias
                </button>
                <button onclick="switchTab('evaluacion')" id="btn-evaluacion" class="tab-btn px-4 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 transition flex items-center gap-1.5 shrink-0">
                    <i data-lucide="award" class="w-3.5 h-3.5"></i> Evaluación
                </button>
            </nav>
        </div>
    </div>

    <!-- Main Container -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 flex-1 space-y-8">

        <!-- ================================================================== -->
        <!-- PESTAÑA 1: PROPUESTA -->
        <!-- ================================================================== -->
        <div id="tab-propuesta" class="tab-content space-y-8">
            
            <!-- Ficha Técnica (UNA SOLA TARJETA) -->
            {auto_ficha_single_card}

            <!-- Marco Filosófico Kinal -->
            <div class="grid md:grid-cols-2 gap-6">
                <div class="bg-blue-50 border-l-4 border-blue-900 p-6 rounded-r-3xl space-y-3 shadow-sm">
                    <div class="flex items-center gap-2 text-blue-900 font-extrabold text-sm uppercase">
                        <i data-lucide="flag" class="w-4 h-4"></i> Misión Institucional de Fundación Kinal
                    </div>
                    <p class="text-slate-700 text-xs italic leading-relaxed">
                        «Formar a jóvenes y adultos a través de una educación integral, con énfasis en las áreas técnicas y tecnológicas, influyendo positivamente en su trabajo, su familia y la sociedad».
                    </p>
                    <div class="pt-2 text-xs font-bold text-blue-950">
                        Valores Nucleares: <span class="font-normal italic">Visión cristiana de la vida. Respeto a la dignidad de la persona. Espíritu de servicio. Trabajo bien hecho. Libertad personal responsable.</span>
                    </div>
                </div>

                <div class="bg-amber-50 border-l-4 border-amber-600 p-6 rounded-r-3xl space-y-3 shadow-sm">
                    <div class="flex items-center gap-2 text-amber-900 font-extrabold text-sm uppercase">
                        <i data-lucide="sparkle" class="w-4 h-4"></i> El Principio Rector del «Trabajo Bien Hecho»
                    </div>
                    <p class="text-slate-700 text-xs leading-relaxed">
                        En el laboratorio de automatización, el trabajo bien hecho se traduce en <strong>cero cortocircuitos</strong>, peinado pulcro y rotulado estandarizado en ductos ranurados, calibración milimétrica de protecciones térmicas, código Ladder estructurado y trazable, y respeto irrenunciable al protocolo de bloqueo y etiquetado (LOTO) para salvaguardar la vida humana.
                    </p>
                </div>
            </div>

            <!-- Matriz DQR -->
            <div class="bg-white rounded-3xl border border-slate-200 p-8 shadow-sm space-y-6">
                <div class="space-y-1">
                    <h3 class="text-xl font-black text-slate-900 flex items-center gap-2">
                        <i data-lucide="award" class="w-5 h-5 text-blue-700"></i>
                        Alineación con el Marco Alemán de Cualificaciones (DQR Nivel 4-5)
                    </h3>
                    <p class="text-slate-600 text-xs">
                        Desglose de competencias integrales de acción (Handlungskompetenz) desarrolladas en banco de potencia.
                    </p>
                </div>

                <div class="overflow-x-auto">
                    <table class="w-full text-xs text-left border-collapse">
                        <thead>
                            <tr class="bg-slate-100 text-slate-700 uppercase font-black border-b border-slate-200">
                                <th class="py-3 px-4">Dimensión DQR</th>
                                <th class="py-3 px-4">Subdimensión</th>
                                <th class="py-3 px-4">Evidencia de Desempeño en el Curso</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-100 text-slate-700">
                            <tr>
                                <td class="py-3 px-4 font-bold text-blue-900 bg-blue-50/50">Competencia Profesional (Fachkompetenz)</td>
                                <td class="py-3 px-4 font-bold">Conocimiento (Wissen)</td>
                                <td class="py-3 px-4">Domina las leyes de la electrotecnia trifásica, curvas V/f en VFDs, arquitectura de autómatas programables, comunicaciones PROFINET y normas internacionales (NFPA 70E, NEC, IEC 60617, IEC 61131-3).</td>
                            </tr>
                            <tr>
                                <td class="py-3 px-4 font-bold text-blue-900 bg-blue-50/50">Competencia Profesional (Fachkompetenz)</td>
                                <td class="py-3 px-4 font-bold">Destrezas (Fertigkeiten)</td>
                                <td class="py-3 px-4">Monta y cablea tableros con canaleta y riel DIN, comisiona variadores con potenciómetro o lazo 4-20mA, programa secuencias en Ladder (KOP) y aplica aislamiento sistemático de fallas en menos de 60 min.</td>
                            </tr>
                            <tr>
                                <td class="py-3 px-4 font-bold text-emerald-900 bg-emerald-50/50">Competencia Personal (Personale Kompetenz)</td>
                                <td class="py-3 px-4 font-bold">Autonomía (Selbständigkeit)</td>
                                <td class="py-3 px-4">Puesta en servicio individual de circuitos y diagnóstico autónomo de averías inducidas en banco de pruebas con multímetro y software, tomando decisiones de intervención seguras.</td>
                            </tr>
                            <tr>
                                <td class="py-3 px-4 font-bold text-emerald-900 bg-emerald-50/50">Competencia Personal (Personale Kompetenz)</td>
                                <td class="py-3 px-4 font-bold">Competencia Social (Sozialkompetenz)</td>
                                <td class="py-3 px-4">Trabajo coordinado en equipo de planta para la integración de la celda continua, respeto mutuo, comunicación asertiva y transferencia ordenada del puesto de trabajo según estándares 5S.</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

        </div>

        <!-- ================================================================== -->
        <!-- PESTAÑA 2: TEMARIO (ESTÉTICA DE CONSTRUCCIÓN APARTADO 3) -->
        <!-- ================================================================== -->
        <div id="tab-temario" class="tab-content hidden space-y-6">
            
            <!-- Barra Superior de Filtros por Categoría -->
            <div class="bg-white rounded-3xl p-5 border border-slate-200 shadow-sm space-y-3">
                <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2">
                    <div>
                        <h3 class="text-xl font-black text-slate-900 flex items-center gap-2">
                            <i data-lucide="layers" class="w-5 h-5 text-blue-700"></i>
                            Distribución Modular con Código de Color
                        </h3>
                        <p class="text-slate-600 text-xs">
                            Estructura de 4 módulos formativos divididos por especialidad técnica. Filtra por categoría para enfocar el análisis.
                        </p>
                    </div>
                    <span class="text-xs font-bold text-slate-500 bg-slate-100 px-3 py-1 rounded-full">
                        Total: 20 Contenidos Clave
                    </span>
                </div>

                <!-- Botones de Filtro -->
                <div class="flex flex-wrap gap-2 pt-2 border-t border-slate-100">
                    <button onclick="filterAutoCategory('all')" id="btn-cat-all" class="px-3.5 py-1.5 rounded-xl text-xs font-extrabold bg-slate-900 text-white shadow-sm transition">
                        Todos los Temas (20)
                    </button>
                    <button onclick="filterAutoCategory('fuerza')" id="btn-cat-fuerza" class="px-3.5 py-1.5 rounded-xl text-xs font-extrabold bg-amber-50 hover:bg-amber-100 text-amber-900 border border-amber-200 transition">
                        ⚡ Fuerza & Maniobra
                    </button>
                    <button onclick="filterAutoCategory('vfd')" id="btn-cat-vfd" class="px-3.5 py-1.5 rounded-xl text-xs font-extrabold bg-blue-50 hover:bg-blue-100 text-blue-900 border border-blue-200 transition">
                        🔄 Variadores & Motores
                    </button>
                    <button onclick="filterAutoCategory('plc')" id="btn-cat-plc" class="px-3.5 py-1.5 rounded-xl text-xs font-extrabold bg-purple-50 hover:bg-purple-100 text-purple-900 border border-purple-200 transition">
                        💻 Programación PLC
                    </button>
                    <button onclick="filterAutoCategory('redes')" id="btn-cat-redes" class="px-3.5 py-1.5 rounded-xl text-xs font-extrabold bg-emerald-50 hover:bg-emerald-100 text-emerald-900 border border-emerald-200 transition">
                        🌐 Redes & Diagnóstico
                    </button>
                </div>
            </div>

            <!-- Cuadrícula Modular de Temas -->
            <div class="grid lg:grid-cols-2 gap-6" id="auto-modules-grid">
                {auto_modular_cards}
            </div>

        </div>

        <!-- ================================================================== -->
        <!-- PESTAÑA 3: CALENDARIO CRONOLÓGICO -->
        <!-- ================================================================== -->
        <div id="tab-calendario" class="tab-content hidden space-y-6">
            
            <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-3 bg-white rounded-3xl p-6 border border-slate-200 shadow-sm">
                <div>
                    <h3 class="text-xl font-black text-slate-900 flex items-center gap-2">
                        <i data-lucide="calendar" class="w-5 h-5 text-amber-600"></i>
                        Calendario Cronológico de Taller Intensivo
                    </h3>
                    <p class="text-slate-600 text-xs mt-1">
                        Programa de 20 encuentros formativos de 6 horas cada uno (120h totales) organizados en 4 bloques de 5 sesiones.
                    </p>
                </div>
                <div class="flex items-center gap-2 text-xs font-bold text-amber-900 bg-amber-50 px-3 py-1.5 rounded-xl border border-amber-200">
                    <i data-lucide="map-pin" class="w-4 h-4 text-amber-700"></i> Laboratorio de Electrotecnia Kinal
                </div>
            </div>

            <!-- Grid de Calendario -->
            <div class="space-y-6">
                {auto_calendar_content}
            </div>

        </div>

        <!-- ================================================================== -->
        <!-- PESTAÑA 4: SECUENCIAS (MASTER-DETAIL SIN ALARGAR LA PÁGINA) -->
        <!-- ================================================================== -->
        <div id="tab-secuencias" class="tab-content hidden space-y-6">
            
            <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-3 bg-white rounded-3xl p-5 border border-slate-200 shadow-sm">
                <div>
                    <h3 class="text-xl font-black text-slate-900 flex items-center gap-2">
                        <i data-lucide="layers" class="w-5 h-5 text-blue-700"></i>
                        Secuencia Didáctica Interactiva Sesión a Sesión
                    </h3>
                    <p class="text-slate-600 text-xs mt-0.5">
                        Selecciona un encuentro en el panel izquierdo para consultar su microdiseño en 3 momentos (Apertura 30 min, Desarrollo 280 min con Receso de 30 min, Cierre 50 min).
                    </p>
                </div>
                <div class="flex items-center gap-2 w-full sm:w-auto">
                    <div class="relative w-full sm:w-56">
                        <i data-lucide="search" class="w-3.5 h-3.5 text-slate-400 absolute left-3 top-2.5"></i>
                        <input type="text" id="auto-sec-search" oninput="filterAutoList()" placeholder="Buscar sesión..." class="w-full pl-8 pr-3 py-1.5 text-xs rounded-xl border border-slate-200 bg-slate-50 focus:bg-white focus:outline-none focus:ring-2 focus:ring-blue-600 transition">
                    </div>
                </div>
            </div>

            <!-- Master-Detail Container -->
            <div class="grid lg:grid-cols-12 gap-6 items-start">
                
                <!-- LISTADO LATERAL (MASTER) -->
                <div class="lg:col-span-4 bg-white rounded-3xl border border-slate-200 p-4 shadow-sm space-y-2">
                    <div class="text-[11px] font-black uppercase tracking-wider text-slate-400 px-2 pb-1 border-b border-slate-100 flex justify-between">
                        <span>Listado de Sesiones</span>
                        <span id="auto-count-badge">20 Sesiones</span>
                    </div>
                    <div id="auto-sessions-list" class="space-y-1.5 max-h-[560px] overflow-y-auto pr-1">
                        <!-- Rendered by JS -->
                    </div>
                </div>

                <!-- DETALLE DE LA SESIÓN SELECCIONADA (DETAIL) -->
                <div class="lg:col-span-8 bg-white rounded-3xl border border-slate-200 p-6 sm:p-8 shadow-sm space-y-6" id="auto-detail-card">
                    <!-- Rendered by JS -->
                </div>

            </div>

        </div>

        <!-- ================================================================== -->
        <!-- PESTAÑA 5: EVALUACIÓN -->
        <!-- ================================================================== -->
        <div id="tab-evaluacion" class="tab-content hidden space-y-8">
            
            <!-- Esquema Resumen -->
            <div class="bg-white rounded-3xl border border-slate-200 p-8 shadow-sm space-y-6">
                <div class="flex items-center justify-between border-b border-slate-200 pb-3">
                    <h3 class="text-xl font-black text-slate-900 flex items-center gap-2">
                        <i data-lucide="check-square" class="w-5 h-5 text-blue-700"></i>
                        Esquema de Evaluación Institucional & Acreditación
                    </h3>
                    <span class="px-3 py-1 rounded-full bg-amber-100 text-amber-900 font-black text-xs">
                        Umbral Mínimo: 75 / 100 Puntos
                    </span>
                </div>
                <div class="grid md:grid-cols-4 gap-4 text-xs">
                    <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 text-center space-y-1">
                        <div class="text-slate-500 font-bold uppercase text-[10px]">Evaluaciones Prácticas de Banco</div>
                        <div class="text-3xl font-black text-blue-900">40%</div>
                        <div class="text-slate-600">4 Proyectos de Taller (10% c/u)</div>
                    </div>
                    <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 text-center space-y-1">
                        <div class="text-slate-500 font-bold uppercase text-[10px]">Examen Terminal de Certificación</div>
                        <div class="text-3xl font-black text-emerald-700">35%</div>
                        <div class="text-slate-600">Comisionamiento & Troubleshooting</div>
                    </div>
                    <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 text-center space-y-1">
                        <div class="text-slate-500 font-bold uppercase text-[10px]">Bitácora Berichtsheft</div>
                        <div class="text-3xl font-black text-purple-700">15%</div>
                        <div class="text-slate-600">Registro Semanal Visado</div>
                    </div>
                    <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 text-center space-y-1">
                        <div class="text-slate-500 font-bold uppercase text-[10px]">Orden 5S & Seguridad LOTO</div>
                        <div class="text-3xl font-black text-amber-700">10%</div>
                        <div class="text-slate-600">EPP y Trabajo Bien Hecho</div>
                    </div>
                </div>
            </div>

            <!-- Rúbrica Terminal -->
            <div class="bg-white rounded-3xl border border-slate-200 p-8 shadow-sm space-y-6">
                <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2 border-b border-slate-200 pb-4">
                    <div>
                        <h3 class="text-xl font-black text-slate-900 flex items-center gap-2">
                            <i data-lucide="award" class="w-5 h-5 text-blue-700"></i>
                            Rúbrica Analítica Terminal de Evaluación Práctica
                        </h3>
                        <p class="text-slate-600 text-xs mt-1">
                            Evaluación objetiva del desempeño técnico con ponderaciones explícitas y umbral institucional de 75 puntos.
                        </p>
                    </div>
                    <span class="px-3 py-1.5 rounded-xl bg-amber-100 text-amber-900 font-extrabold text-xs">
                        Aprobación Mínima: ≥ 75 Pts
                    </span>
                </div>

                <div class="overflow-x-auto">
                    <table class="w-full text-xs text-left border-collapse">
                        <thead>
                            <tr class="bg-slate-100 text-slate-800 uppercase font-black border-b border-slate-200">
                                <th class="py-3 px-4 w-1/4">Criterio Evaluado</th>
                                <th class="py-3 px-4 w-20 text-center">Ponderación</th>
                                <th class="py-3 px-4 text-emerald-900">Desempeño Excelente (Trabajo Bien Hecho)</th>
                                <th class="py-3 px-4 text-rose-900">Desempeño Insuficiente (&lt; 75%)</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-100">
                            {auto_rubric_rows}
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- Bitácora Berichtsheft Card -->
            {auto_bitacora_card}

        </div>

    </main>

    <!-- Footer -->
    <footer class="bg-slate-950 text-slate-400 py-8 border-t border-slate-800 text-xs">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col sm:flex-row justify-between items-center gap-4 text-center sm:text-left">
            <div>
                <p class="font-bold text-slate-200">Fundación Kinal • Escuela Técnica Superior & Coordinación de Formación Continua</p>
                <p class="text-slate-500">Diseño Curricular e Instruccional 2026 | Estándares DQR 4-5 & Sistema Dual</p>
            </div>
            <div class="flex items-center gap-4">
                <a href="index.html" class="hover:text-amber-400 transition">Catálogo de Cursos</a>
                <span class="text-slate-700">•</span>
                <a href="mecatronica.html" class="hover:text-amber-400 transition">Mecatrónica</a>
                <span class="text-slate-700">•</span>
                <a href="ciberseguridad.html" class="hover:text-amber-400 transition">Ciberseguridad</a>
                <span class="text-slate-700">•</span>
                <a href="cableado_estructurado.html" class="hover:text-amber-400 transition">Cableado Estructurado</a>
            </div>
        </div>
    </footer>

    <!-- JavaScript Interactivity -->
    <script>
        const autoSessionsData = {auto_sessions_json};
        let currentAutoSessionId = 1;

        function switchTab(tabId) {{
            document.querySelectorAll('.tab-content').forEach(el => el.classList.add('hidden'));
            document.querySelectorAll('.tab-btn').forEach(btn => {{
                btn.classList.remove('active');
                btn.classList.add('bg-slate-100', 'text-slate-700');
            }});

            const targetTab = document.getElementById('tab-' + tabId);
            const targetBtn = document.getElementById('btn-' + tabId);
            if (targetTab && targetBtn) {{
                targetTab.classList.remove('hidden');
                targetBtn.classList.add('active');
                targetBtn.classList.remove('bg-slate-100', 'text-slate-700');
            }}
            window.scrollTo({{ top: 0, behavior: 'smooth' }});
        }}

        function filterAutoCategory(cat) {{
            document.querySelectorAll('#tab-temario button[id^="btn-cat-"]').forEach(btn => {{
                btn.className = "px-3.5 py-1.5 rounded-xl text-xs font-extrabold bg-slate-100 hover:bg-slate-200 text-slate-700 transition";
            }});

            const activeBtn = document.getElementById('btn-cat-' + cat);
            if (activeBtn) {{
                activeBtn.className = "px-3.5 py-1.5 rounded-xl text-xs font-extrabold bg-slate-900 text-white shadow-sm transition";
            }}

            const items = document.querySelectorAll('.content-item');
            items.forEach(it => {{
                if (cat === 'all' || it.getAttribute('data-category') === cat) {{
                    it.style.display = 'block';
                }} else {{
                    it.style.display = 'none';
                }}
            }});
        }}

        function renderAutoSessionsList(filteredSessions) {{
            const container = document.getElementById('auto-sessions-list');
            container.innerHTML = '';

            filteredSessions.forEach(s => {{
                const item = document.createElement('div');
                item.className = `session-item p-3 rounded-2xl border border-slate-200 cursor-pointer transition flex items-center justify-between text-xs hover:border-blue-900 hover:bg-slate-50 ${{s.num === currentAutoSessionId ? 'active' : 'bg-white'}}`;
                item.onclick = () => selectAutoSession(s.num);
                
                item.innerHTML = `
                    <div class="space-y-0.5 pr-2">
                        <div class="flex items-center gap-1.5 font-bold">
                            <span class="badge-code px-2 py-0.5 rounded text-[10px] font-black bg-slate-100 text-slate-800">${{s.code}}</span>
                            <span class="line-clamp-1 text-slate-900 text-xs">${{s.title}}</span>
                        </div>
                        <div class="text-[10px] text-slate-500">${{s.module}}</div>
                    </div>
                    <i data-lucide="chevron-right" class="w-4 h-4 text-slate-400 shrink-0"></i>
                `;
                container.appendChild(item);
            }});
            lucide.createIcons();
        }}

        function selectAutoSession(num) {{
            currentAutoSessionId = num;
            const s = autoSessionsData.find(item => item.num === num);
            if (!s) return;

            document.querySelectorAll('.session-item').forEach(el => {{
                el.classList.remove('active');
                el.classList.add('bg-white');
            }});

            renderAutoSessionsList(autoSessionsData);

            const detailContainer = document.getElementById('auto-detail-card');
            detailContainer.innerHTML = `
                <div class="border-b border-slate-200 pb-5 space-y-2">
                    <div class="flex flex-wrap justify-between items-center gap-2">
                        <div class="flex items-center gap-2">
                            <span class="px-3 py-1 rounded-xl bg-slate-950 text-amber-400 font-black text-xs tracking-wider">${{s.code}}</span>
                            <span class="px-2.5 py-0.5 rounded-lg bg-blue-50 text-blue-900 font-bold text-xs border border-blue-200">${{s.module}}</span>
                        </div>
                        <span class="text-xs font-bold text-slate-500 bg-slate-100 px-3 py-1 rounded-lg">${{s.duration}}</span>
                    </div>
                    <h3 class="text-xl sm:text-2xl font-black text-slate-900 leading-snug">${{s.title}}</h3>
                    <div class="text-xs text-amber-800 font-bold pt-1">
                        Encuentro Sabatino: ${{s.horario}}
                    </div>
                </div>

                <div class="bg-amber-50/60 rounded-2xl p-4 border border-amber-200 space-y-1">
                    <div class="text-[11px] uppercase font-black tracking-wider text-amber-900 flex items-center gap-1.5">
                        <i data-lucide="target" class="w-3.5 h-3.5 text-amber-700"></i> Indicador de Logro / Objetivo Formativo
                    </div>
                    <p class="text-slate-800 text-xs leading-relaxed font-medium">${{s.objective}}</p>
                </div>

                <div class="space-y-4">
                    <h4 class="text-sm font-black text-slate-900 uppercase tracking-wide flex items-center gap-2 border-b border-slate-100 pb-2">
                        <i data-lucide="clock" class="w-4 h-4 text-blue-700"></i> Secuencia Didáctica en Tres Momentos
                    </h4>

                    <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-1.5">
                        <div class="flex items-center justify-between">
                            <span class="font-bold text-xs text-blue-950 flex items-center gap-2">
                                <span class="w-2.5 h-2.5 rounded-full bg-blue-600"></span> Fase 1: Apertura
                            </span>
                            <span class="text-[11px] font-bold text-slate-500">30 Minutos</span>
                        </div>
                        <p class="text-slate-700 text-xs leading-relaxed pl-4.5">${{s.apertura}}</p>
                    </div>

                    <div class="p-4 rounded-2xl bg-blue-50/40 border border-blue-200 space-y-1.5">
                        <div class="flex items-center justify-between">
                            <span class="font-bold text-xs text-blue-950 flex items-center gap-2">
                                <span class="w-2.5 h-2.5 rounded-full bg-emerald-600"></span> Fase 2: Desarrollo & Práctica en Banco
                            </span>
                            <span class="text-[11px] font-bold text-emerald-800 bg-emerald-100 px-2 py-0.5 rounded">280 Minutos (Receso: 30 min)</span>
                        </div>
                        <p class="text-slate-700 text-xs leading-relaxed pl-4.5">${{s.desarrollo}}</p>
                    </div>

                    <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-1.5">
                        <div class="flex items-center justify-between">
                            <span class="font-bold text-xs text-blue-950 flex items-center gap-2">
                                <span class="w-2.5 h-2.5 rounded-full bg-purple-600"></span> Fase 3: Cierre, Evaluación y Orden 5S
                            </span>
                            <span class="text-[11px] font-bold text-slate-500">50 Minutos</span>
                        </div>
                        <p class="text-slate-700 text-xs leading-relaxed pl-4.5">${{s.cierre}}</p>
                    </div>
                </div>

                <div class="grid sm:grid-cols-2 gap-4 pt-2">
                    <div class="bg-emerald-50/60 rounded-2xl p-4 border border-emerald-200 space-y-1.5">
                        <div class="text-[11px] uppercase font-black tracking-wider text-emerald-900 flex items-center gap-1.5">
                            <i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-emerald-700"></i> Evidencias & Producto Observable
                        </div>
                        <p class="text-slate-700 text-xs leading-relaxed">${{s.evidencias}}</p>
                    </div>

                    <div class="bg-slate-100 rounded-2xl p-4 border border-slate-200 space-y-1.5">
                        <div class="text-[11px] uppercase font-black tracking-wider text-slate-900 flex items-center gap-1.5">
                            <i data-lucide="shield-check" class="w-3.5 h-3.5 text-blue-700"></i> Equipamiento & Seguridad LOTO
                        </div>
                        <p class="text-slate-700 text-xs leading-relaxed">${{s.equipamiento}}</p>
                    </div>
                </div>
            `;
            lucide.createIcons();
        }}

        function filterAutoList() {{
            const q = document.getElementById('auto-sec-search').value.toLowerCase();
            const filtered = autoSessionsData.filter(s => 
                s.title.toLowerCase().includes(q) || 
                s.code.toLowerCase().includes(q) ||
                s.module.toLowerCase().includes(q) ||
                s.objective.toLowerCase().includes(q)
            );
            document.getElementById('auto-count-badge').textContent = `${{filtered.length}} Sesiones`;
            renderAutoSessionsList(filtered);
        }}

        function goToSession(num) {{
            switchTab('secuencias');
            selectAutoSession(num);
        }}

        document.addEventListener('DOMContentLoaded', () => {{
            lucide.createIcons();
            selectAutoSession(1);
        }});
    </script>
</body>
</html>
"""

with open(os.path.join(WEB_DIR, "automatizacion.html"), "w", encoding="utf-8") as f:
    f.write(automatizacion_html)
print("Generado: Cursos/Web/automatizacion.html")

# ==============================================================================
# HTML BUILDER: CABLEADO_ESTRUCTURADO.HTML
# ==============================================================================
cable_sessions_json = json.dumps(cable_sessions, ensure_ascii=False)

cableado_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cableado Estructurado y Redes de Cobre y Fibra Óptica | Kinal 2026</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@500;700;800;900&display=swap');
        body {{ font-family: 'Inter', sans-serif; background-color: #f8fafc; color: #0f172a; }}
        h1, h2, h3, h4, .font-heading {{ font-family: 'Space Grotesk', sans-serif; }}
        .hero-pattern {{
            background: linear-gradient(135deg, #082f49 0%, #0f172a 50%, #0f766e 100%);
        }}
        .tab-btn.active {{
            background-color: #003366;
            color: #ffffff;
            font-weight: 700;
        }}
        .session-item.active {{
            background-color: #003366;
            color: #ffffff;
            border-color: #003366;
        }}
        .session-item.active span, .session-item.active p {{
            color: #e2e8f0;
        }}
        .session-item.active .badge-code {{
            background-color: #06b6d4;
            color: #082f49;
        }}
    </style>
</head>
<body class="antialiased min-h-screen flex flex-col">

    <!-- Top Navigation Header -->
    <header class="bg-slate-950 text-white border-b border-slate-800 sticky top-0 z-50 shadow-md">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3 flex flex-wrap justify-between items-center gap-4">
            <div class="flex items-center gap-3">
                <a href="index.html" class="bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-bold px-3 py-1.5 rounded-lg transition flex items-center gap-1.5">
                    <i data-lucide="arrow-left" class="w-3.5 h-3.5"></i> Cursos
                </a>
                <span class="text-slate-600">|</span>
                <div class="text-slate-200 font-bold text-xs sm:text-sm flex items-center gap-2">
                    <i data-lucide="network" class="w-4 h-4 text-cyan-400"></i>
                    Cableado Estructurado y Redes de Cobre y Fibra Óptica
                </div>
            </div>
            
            <!-- Quick Download Buttons -->
            <div class="flex items-center gap-2 text-xs">
                <span class="text-slate-400 hidden sm:inline">Word:</span>
                <a href="../Cableado_Estructurado/Propuesta_Curso_Cableado_Estructurado_Kinal.docx" download class="px-2.5 py-1 rounded bg-blue-900/60 hover:bg-blue-800 text-blue-200 transition font-medium" title="Descargar Propuesta Oficial">
                    Propuesta
                </a>
                <a href="../Cableado_Estructurado/Temario_Curso_Cableado_Estructurado_Kinal.docx" download class="px-2.5 py-1 rounded bg-emerald-900/60 hover:bg-emerald-800 text-emerald-200 transition font-medium" title="Descargar Temario Oficial">
                    Temario
                </a>
                <a href="../Cableado_Estructurado/Dosificacion_y_Secuencia_Didactica_Cableado_Estructurado_Kinal.docx" download class="px-2.5 py-1 rounded bg-amber-900/60 hover:bg-amber-800 text-amber-200 transition font-medium" title="Descargar Dosificación Oficial">
                    Dosificación
                </a>
            </div>
        </div>
    </header>

    <!-- Hero Course Banner -->
    <section class="hero-pattern text-white py-10 px-4 sm:px-6 lg:px-8">
        <div class="max-w-7xl mx-auto space-y-3">
            <div class="flex flex-wrap items-center gap-2">
                <span class="px-3 py-1 rounded-full bg-cyan-500/20 border border-cyan-400/30 text-cyan-300 text-xs font-bold tracking-wide uppercase">
                    Especialidad Presencial en Laboratorios de Redes
                </span>
                <span class="px-3 py-1 rounded-full bg-blue-500/20 border border-blue-400/30 text-blue-300 text-xs font-bold">
                    DQR Nivel 4 - 5
                </span>
                <span class="px-3 py-1 rounded-full bg-emerald-500/20 border border-emerald-400/30 text-emerald-300 text-xs font-bold">
                    Aprobación: ≥ 75 Pts
                </span>
            </div>
            <h1 class="text-2xl sm:text-4xl font-black tracking-tight leading-tight">
                Cableado Estructurado y Redes de Cobre y Fibra Óptica
            </h1>
            <p class="text-slate-300 text-xs sm:text-sm max-w-4xl leading-relaxed">
                Planificación de canalizaciones físicas según ANSI/TIA-569, montaje y anclaje de racks de 19 pulgadas (EIA-310), conectorización Cat 6A con mínimo destrenzado, empalme de fibra óptica por fusión con arco voltaico (&lt; 0.05 dB), certificación instrumental Tier 1 con Fluke Networks y rotulado TIA-606.
            </p>
        </div>
    </section>

    <!-- Tab Bar Navigation (UNA SOLA PALABRA, SIN NUMERACIÓN) -->
    <div class="bg-white border-b border-slate-200 sticky top-14 z-40 shadow-sm">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <nav class="flex space-x-2 sm:space-x-3 py-2.5 overflow-x-auto text-xs font-bold">
                <button onclick="switchTab('propuesta')" id="btn-propuesta" class="tab-btn active px-4 py-2 rounded-xl transition flex items-center gap-1.5 shrink-0">
                    <i data-lucide="file-text" class="w-3.5 h-3.5"></i> Propuesta
                </button>
                <button onclick="switchTab('temario')" id="btn-temario" class="tab-btn px-4 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 transition flex items-center gap-1.5 shrink-0">
                    <i data-lucide="list-tree" class="w-3.5 h-3.5"></i> Temario
                </button>
                <button onclick="switchTab('calendario')" id="btn-calendario" class="tab-btn px-4 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 transition flex items-center gap-1.5 shrink-0">
                    <i data-lucide="calendar" class="w-3.5 h-3.5"></i> Calendario
                </button>
                <button onclick="switchTab('secuencias')" id="btn-secuencias" class="tab-btn px-4 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 transition flex items-center gap-1.5 shrink-0">
                    <i data-lucide="layers" class="w-3.5 h-3.5"></i> Secuencias
                </button>
                <button onclick="switchTab('evaluacion')" id="btn-evaluacion" class="tab-btn px-4 py-2 rounded-xl bg-slate-100 hover:bg-slate-200 text-slate-700 transition flex items-center gap-1.5 shrink-0">
                    <i data-lucide="award" class="w-3.5 h-3.5"></i> Evaluación
                </button>
            </nav>
        </div>
    </div>

    <!-- Main Container -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 flex-1 space-y-8">

        <!-- ================================================================== -->
        <!-- PESTAÑA 1: PROPUESTA -->
        <!-- ================================================================== -->
        <div id="tab-propuesta" class="tab-content space-y-8">
            
            <!-- Ficha Técnica (UNA SOLA TARJETA) -->
            {cable_ficha_single_card}

            <!-- Marco Filosófico Kinal -->
            <div class="grid md:grid-cols-2 gap-6">
                <div class="bg-blue-50 border-l-4 border-blue-900 p-6 rounded-r-3xl space-y-3 shadow-sm">
                    <div class="flex items-center gap-2 text-blue-900 font-extrabold text-sm uppercase">
                        <i data-lucide="flag" class="w-4 h-4"></i> Misión Institucional de Fundación Kinal
                    </div>
                    <p class="text-slate-700 text-xs italic leading-relaxed">
                        «Formar a jóvenes y adultos a través de una educación integral, con énfasis en las áreas técnicas y tecnológicas, influyendo positivamente en su trabajo, su familia y la sociedad».
                    </p>
                    <div class="pt-2 text-xs font-bold text-blue-950">
                        Valores Nucleares: <span class="font-normal italic">Visión cristiana de la vida. Respeto a la dignidad de la persona. Espíritu de servicio. Trabajo bien hecho. Libertad personal responsable.</span>
                    </div>
                </div>

                <div class="bg-teal-50 border-l-4 border-teal-600 p-6 rounded-r-3xl space-y-3 shadow-sm">
                    <div class="flex items-center gap-2 text-teal-900 font-extrabold text-sm uppercase">
                        <i data-lucide="sparkle" class="w-4 h-4"></i> El Principio Rector del «Trabajo Bien Hecho»
                    </div>
                    <p class="text-slate-700 text-xs leading-relaxed">
                        En infraestructura de telecomunicaciones, el trabajo bien hecho es sinónimo de <strong>estética profesional impecable</strong>: peinado simétrico sin cruces en rack, sujeción exclusiva con cinchos de velcro, respeto estricto a la física del destrenzado (&lt; 13 mm) para evitar paradiafonía (NEXT), cortes perpendiculares con cleaver (&lt; 1°) y etiquetado normalizado indeleble según TIA-606.
                    </p>
                </div>
            </div>

            <!-- Matriz DQR -->
            <div class="bg-white rounded-3xl border border-slate-200 p-8 shadow-sm space-y-6">
                <div class="space-y-1">
                    <h3 class="text-xl font-black text-slate-900 flex items-center gap-2">
                        <i data-lucide="award" class="w-5 h-5 text-blue-700"></i>
                        Alineación con el Marco Alemán de Cualificaciones (DQR Nivel 4-5)
                    </h3>
                    <p class="text-slate-600 text-xs">
                        Desglose de competencias integrales de acción (Handlungskompetenz) desarrolladas en infraestructura física de red.
                    </p>
                </div>

                <div class="overflow-x-auto">
                    <table class="w-full text-xs text-left border-collapse">
                        <thead>
                            <tr class="bg-slate-100 text-slate-700 uppercase font-black border-b border-slate-200">
                                <th class="py-3 px-4">Dimensión DQR</th>
                                <th class="py-3 px-4">Subdimensión</th>
                                <th class="py-3 px-4">Evidencia de Desempeño en el Curso</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-100 text-slate-700">
                            <tr>
                                <td class="py-3 px-4 font-bold text-blue-900 bg-blue-50/50">Competencia Profesional (Fachkompetenz)</td>
                                <td class="py-3 px-4 font-bold">Conocimiento (Wissen)</td>
                                <td class="py-3 px-4">Domina los estándares ANSI/TIA (568, 569, 606, 607), topologías jerárquicas de cableado, propagación de ondas electromagnéticas a 500 MHz, reflexión óptica en fibras OS2/OM4 y parámetros de certificación Fluke.</td>
                            </tr>
                            <tr>
                                <td class="py-3 px-4 font-bold text-blue-900 bg-blue-50/50">Competencia Profesional (Fachkompetenz)</td>
                                <td class="py-3 px-4 font-bold">Destrezas (Fertigkeiten)</td>
                                <td class="py-3 px-4">Curva tubería EMT, monta y aploma racks de 19'', conectoriza jacks Keystone Cat 6A, empalma fibras ópticas por fusión (&lt; 0.05 dB), maneja escáneres Fluke DSX e interpreta reflectometría TDNXT/TDR.</td>
                            </tr>
                            <tr>
                                <td class="py-3 px-4 font-bold text-emerald-900 bg-emerald-50/50">Competencia Personal (Personale Kompetenz)</td>
                                <td class="py-3 px-4 font-bold">Autonomía (Selbständigkeit)</td>
                                <td class="py-3 px-4">Diagnóstico y corrección metódica e independiente de enlaces defectuosos, cálculo del presupuesto de pérdida óptica y elaboración completa de carpetas técnicas As-Built para entrega al cliente.</td>
                            </tr>
                            <tr>
                                <td class="py-3 px-4 font-bold text-emerald-900 bg-emerald-50/50">Competencia Personal (Personale Kompetenz)</td>
                                <td class="py-3 px-4 font-bold">Competencia Social (Sozialkompetenz)</td>
                                <td class="py-3 px-4">Coordinación en cuadrilla de instalación para tendido simultáneo de mazos de cables, seguridad compartida en cuartos de telecomunicaciones, manejo seguro de residuos de fibra de vidrio y orden 5S.</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>

        </div>

        <!-- ================================================================== -->
        <!-- PESTAÑA 2: TEMARIO (ESTÉTICA DE CONSTRUCCIÓN APARTADO 3) -->
        <!-- ================================================================== -->
        <div id="tab-temario" class="tab-content hidden space-y-6">
            
            <!-- Barra Superior de Filtros por Categoría -->
            <div class="bg-white rounded-3xl p-5 border border-slate-200 shadow-sm space-y-3">
                <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2">
                    <div>
                        <h3 class="text-xl font-black text-slate-900 flex items-center gap-2">
                            <i data-lucide="layers" class="w-5 h-5 text-cyan-700"></i>
                            Distribución Modular con Código de Color
                        </h3>
                        <p class="text-slate-600 text-xs">
                            Estructura de 4 módulos formativos divididos por especialidad técnica. Filtra por categoría para enfocar el análisis.
                        </p>
                    </div>
                    <span class="text-xs font-bold text-slate-500 bg-slate-100 px-3 py-1 rounded-full">
                        Total: 20 Contenidos Clave
                    </span>
                </div>

                <!-- Botones de Filtro -->
                <div class="flex flex-wrap gap-2 pt-2 border-t border-slate-100">
                    <button onclick="filterCableCategory('all')" id="btn-cable-all" class="px-3.5 py-1.5 rounded-xl text-xs font-extrabold bg-slate-900 text-white shadow-sm transition">
                        Todos los Temas (20)
                    </button>
                    <button onclick="filterCableCategory('normas')" id="btn-cable-normas" class="px-3.5 py-1.5 rounded-xl text-xs font-extrabold bg-blue-50 hover:bg-blue-100 text-blue-900 border border-blue-200 transition">
                        📐 Normas & Espacios
                    </button>
                    <button onclick="filterCableCategory('cobre')" id="btn-cable-cobre" class="px-3.5 py-1.5 rounded-xl text-xs font-extrabold bg-amber-50 hover:bg-amber-100 text-amber-900 border border-amber-200 transition">
                        🔌 Cobre & PoE++
                    </button>
                    <button onclick="filterCableCategory('fibra')" id="btn-cable-fibra" class="px-3.5 py-1.5 rounded-xl text-xs font-extrabold bg-purple-50 hover:bg-purple-100 text-purple-900 border border-purple-200 transition">
                        💡 Fibra & Fusión
                    </button>
                    <button onclick="filterCableCategory('certificacion')" id="btn-cable-certificacion" class="px-3.5 py-1.5 rounded-xl text-xs font-extrabold bg-emerald-50 hover:bg-emerald-100 text-emerald-900 border border-emerald-200 transition">
                        📊 Certificación & As-Built
                    </button>
                </div>
            </div>

            <!-- Cuadrícula Modular de Temas -->
            <div class="grid lg:grid-cols-2 gap-6" id="cable-modules-grid">
                {cable_modular_cards}
            </div>

        </div>

        <!-- ================================================================== -->
        <!-- PESTAÑA 3: CALENDARIO CRONOLÓGICO -->
        <!-- ================================================================== -->
        <div id="tab-calendario" class="tab-content hidden space-y-6">
            
            <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-3 bg-white rounded-3xl p-6 border border-slate-200 shadow-sm">
                <div>
                    <h3 class="text-xl font-black text-slate-900 flex items-center gap-2">
                        <i data-lucide="calendar" class="w-5 h-5 text-cyan-700"></i>
                        Calendario Cronológico de Taller Semanal
                    </h3>
                    <p class="text-slate-600 text-xs mt-1">
                        Programa de 10 semanas continuas • 2 sesiones por semana (Martes y Jueves de 17:30 a 21:30 hrs • 4h por encuentro).
                    </p>
                </div>
                <div class="flex items-center gap-2 text-xs font-bold text-cyan-900 bg-cyan-50 px-3 py-1.5 rounded-xl border border-cyan-200">
                    <i data-lucide="map-pin" class="w-4 h-4 text-cyan-700"></i> Laboratorio de Redes Kinal
                </div>
            </div>

            <!-- Grid de Calendario -->
            <div class="space-y-6">
                {cable_calendar_content}
            </div>

        </div>

        <!-- ================================================================== -->
        <!-- PESTAÑA 4: SECUENCIAS (MASTER-DETAIL SIN ALARGAR LA PÁGINA) -->
        <!-- ================================================================== -->
        <div id="tab-secuencias" class="tab-content hidden space-y-6">
            
            <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-3 bg-white rounded-3xl p-5 border border-slate-200 shadow-sm">
                <div>
                    <h3 class="text-xl font-black text-slate-900 flex items-center gap-2">
                        <i data-lucide="layers" class="w-5 h-5 text-cyan-700"></i>
                        Secuencia Didáctica Interactiva Sesión a Sesión
                    </h3>
                    <p class="text-slate-600 text-xs mt-0.5">
                        Selecciona una sesión en el panel izquierdo para consultar su microdiseño en 3 momentos (Apertura 20 min, Desarrollo 180 min con Receso de 20 min, Cierre 40 min).
                    </p>
                </div>
                <div class="flex items-center gap-2 w-full sm:w-auto">
                    <div class="relative w-full sm:w-56">
                        <i data-lucide="search" class="w-3.5 h-3.5 text-slate-400 absolute left-3 top-2.5"></i>
                        <input type="text" id="cable-sec-search" oninput="filterCableList()" placeholder="Buscar sesión..." class="w-full pl-8 pr-3 py-1.5 text-xs rounded-xl border border-slate-200 bg-slate-50 focus:bg-white focus:outline-none focus:ring-2 focus:ring-cyan-600 transition">
                    </div>
                </div>
            </div>

            <!-- Master-Detail Container -->
            <div class="grid lg:grid-cols-12 gap-6 items-start">
                
                <!-- LISTADO LATERAL (MASTER) -->
                <div class="lg:col-span-4 bg-white rounded-3xl border border-slate-200 p-4 shadow-sm space-y-2">
                    <div class="text-[11px] font-black uppercase tracking-wider text-slate-400 px-2 pb-1 border-b border-slate-100 flex justify-between">
                        <span>Listado de Sesiones</span>
                        <span id="cable-count-badge">20 Sesiones</span>
                    </div>
                    <div id="cable-sessions-list" class="space-y-1.5 max-h-[560px] overflow-y-auto pr-1">
                        <!-- Rendered by JS -->
                    </div>
                </div>

                <!-- DETALLE DE LA SESIÓN SELECCIONADA (DETAIL) -->
                <div class="lg:col-span-8 bg-white rounded-3xl border border-slate-200 p-6 sm:p-8 shadow-sm space-y-6" id="cable-detail-card">
                    <!-- Rendered by JS -->
                </div>

            </div>

        </div>

        <!-- ================================================================== -->
        <!-- PESTAÑA 5: EVALUACIÓN -->
        <!-- ================================================================== -->
        <div id="tab-evaluacion" class="tab-content hidden space-y-8">
            
            <!-- Esquema Resumen -->
            <div class="bg-white rounded-3xl border border-slate-200 p-8 shadow-sm space-y-6">
                <div class="flex items-center justify-between border-b border-slate-200 pb-3">
                    <h3 class="text-xl font-black text-slate-900 flex items-center gap-2">
                        <i data-lucide="check-square" class="w-5 h-5 text-blue-700"></i>
                        Esquema de Evaluación Institucional & Acreditación
                    </h3>
                    <span class="px-3 py-1 rounded-full bg-amber-100 text-amber-900 font-black text-xs">
                        Umbral Mínimo: 75 / 100 Puntos
                    </span>
                </div>
                <div class="grid md:grid-cols-4 gap-4 text-xs">
                    <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 text-center space-y-1">
                        <div class="text-slate-500 font-bold uppercase text-[10px]">Evaluaciones Prácticas de Taller</div>
                        <div class="text-3xl font-black text-blue-900">40%</div>
                        <div class="text-slate-600">4 Prácticas Integradas (10% c/u)</div>
                    </div>
                    <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 text-center space-y-1">
                        <div class="text-slate-500 font-bold uppercase text-[10px]">Examen Terminal de Certificación</div>
                        <div class="text-3xl font-black text-emerald-700">35%</div>
                        <div class="text-slate-600">Certificación Rack & As-Built</div>
                    </div>
                    <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 text-center space-y-1">
                        <div class="text-slate-500 font-bold uppercase text-[10px]">Bitácora Berichtsheft</div>
                        <div class="text-3xl font-black text-purple-700">15%</div>
                        <div class="text-slate-600">Registro Semanal Visado</div>
                    </div>
                    <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 text-center space-y-1">
                        <div class="text-slate-500 font-bold uppercase text-[10px]">Bioseguridad & Orden 5S</div>
                        <div class="text-3xl font-black text-amber-700">10%</div>
                        <div class="text-slate-600">Residuos de Fibra y EPP</div>
                    </div>
                </div>
            </div>

            <!-- Rúbrica Terminal -->
            <div class="bg-white rounded-3xl border border-slate-200 p-8 shadow-sm space-y-6">
                <div class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-2 border-b border-slate-200 pb-4">
                    <div>
                        <h3 class="text-xl font-black text-slate-900 flex items-center gap-2">
                            <i data-lucide="award" class="w-5 h-5 text-blue-700"></i>
                            Rúbrica Analítica Terminal de Evaluación Práctica
                        </h3>
                        <p class="text-slate-600 text-xs mt-1">
                            Evaluación objetiva del desempeño técnico con ponderaciones explícitas y umbral institucional de 75 puntos.
                        </p>
                    </div>
                    <span class="px-3 py-1.5 rounded-xl bg-amber-100 text-amber-900 font-extrabold text-xs">
                        Aprobación Mínima: ≥ 75 Pts
                    </span>
                </div>

                <div class="overflow-x-auto">
                    <table class="w-full text-xs text-left border-collapse">
                        <thead>
                            <tr class="bg-slate-100 text-slate-800 uppercase font-black border-b border-slate-200">
                                <th class="py-3 px-4 w-1/4">Criterio Evaluado</th>
                                <th class="py-3 px-4 w-20 text-center">Ponderación</th>
                                <th class="py-3 px-4 text-emerald-900">Desempeño Excelente (Trabajo Bien Hecho)</th>
                                <th class="py-3 px-4 text-rose-900">Desempeño Insuficiente (&lt; 75%)</th>
                            </tr>
                        </thead>
                        <tbody class="divide-y divide-slate-100">
                            {cable_rubric_rows}
                        </tbody>
                    </table>
                </div>
            </div>

            <!-- Bitácora Berichtsheft Card -->
            {cable_bitacora_card}

        </div>

    </main>

    <!-- Footer -->
    <footer class="bg-slate-950 text-slate-400 py-8 border-t border-slate-800 text-xs">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col sm:flex-row justify-between items-center gap-4 text-center sm:text-left">
            <div>
                <p class="font-bold text-slate-200">Fundación Kinal • Escuela Técnica Superior & Coordinación de Formación Continua</p>
                <p class="text-slate-500">Diseño Curricular e Instruccional 2026 | Estándares DQR 4-5 & Sistema Dual</p>
            </div>
            <div class="flex items-center gap-4">
                <a href="index.html" class="hover:text-amber-400 transition">Catálogo de Cursos</a>
                <span class="text-slate-700">•</span>
                <a href="mecatronica.html" class="hover:text-amber-400 transition">Mecatrónica</a>
                <span class="text-slate-700">•</span>
                <a href="ciberseguridad.html" class="hover:text-amber-400 transition">Ciberseguridad</a>
                <span class="text-slate-700">•</span>
                <a href="automatizacion.html" class="hover:text-amber-400 transition">Automatización Industrial</a>
            </div>
        </div>
    </footer>

    <!-- JavaScript Interactivity -->
    <script>
        const cableSessionsData = {cable_sessions_json};
        let currentCableSessionId = 1;

        function switchTab(tabId) {{
            document.querySelectorAll('.tab-content').forEach(el => el.classList.add('hidden'));
            document.querySelectorAll('.tab-btn').forEach(btn => {{
                btn.classList.remove('active');
                btn.classList.add('bg-slate-100', 'text-slate-700');
            }});

            const targetTab = document.getElementById('tab-' + tabId);
            const targetBtn = document.getElementById('btn-' + tabId);
            if (targetTab && targetBtn) {{
                targetTab.classList.remove('hidden');
                targetBtn.classList.add('active');
                targetBtn.classList.remove('bg-slate-100', 'text-slate-700');
            }}
            window.scrollTo({{ top: 0, behavior: 'smooth' }});
        }}

        function filterCableCategory(cat) {{
            document.querySelectorAll('#tab-temario button[id^="btn-cable-"]').forEach(btn => {{
                btn.className = "px-3.5 py-1.5 rounded-xl text-xs font-extrabold bg-slate-100 hover:bg-slate-200 text-slate-700 transition";
            }});

            const activeBtn = document.getElementById('btn-cable-' + cat);
            if (activeBtn) {{
                activeBtn.className = "px-3.5 py-1.5 rounded-xl text-xs font-extrabold bg-slate-900 text-white shadow-sm transition";
            }}

            const items = document.querySelectorAll('.content-item');
            items.forEach(it => {{
                if (cat === 'all' || it.getAttribute('data-category') === cat) {{
                    it.style.display = 'block';
                }} else {{
                    it.style.display = 'none';
                }}
            }});
        }}

        function renderCableSessionsList(filteredSessions) {{
            const container = document.getElementById('cable-sessions-list');
            container.innerHTML = '';

            filteredSessions.forEach(s => {{
                const item = document.createElement('div');
                item.className = `session-item p-3 rounded-2xl border border-slate-200 cursor-pointer transition flex items-center justify-between text-xs hover:border-cyan-800 hover:bg-slate-50 ${{s.num === currentCableSessionId ? 'active' : 'bg-white'}}`;
                item.onclick = () => selectCableSession(s.num);
                
                item.innerHTML = `
                    <div class="space-y-0.5 pr-2">
                        <div class="flex items-center gap-1.5 font-bold">
                            <span class="badge-code px-2 py-0.5 rounded text-[10px] font-black bg-slate-100 text-slate-800">${{s.code}}</span>
                            <span class="line-clamp-1 text-slate-900 text-xs">${{s.title}}</span>
                        </div>
                        <div class="text-[10px] text-slate-500">${{s.semana}} • ${{s.dia}}</div>
                    </div>
                    <i data-lucide="chevron-right" class="w-4 h-4 text-slate-400 shrink-0"></i>
                `;
                container.appendChild(item);
            }});
            lucide.createIcons();
        }}

        function selectCableSession(num) {{
            currentCableSessionId = num;
            const s = cableSessionsData.find(item => item.num === num);
            if (!s) return;

            document.querySelectorAll('.session-item').forEach(el => {{
                el.classList.remove('active');
                el.classList.add('bg-white');
            }});

            renderCableSessionsList(cableSessionsData);

            const detailContainer = document.getElementById('cable-detail-card');
            detailContainer.innerHTML = `
                <div class="border-b border-slate-200 pb-5 space-y-2">
                    <div class="flex flex-wrap justify-between items-center gap-2">
                        <div class="flex items-center gap-2">
                            <span class="px-3 py-1 rounded-xl bg-slate-950 text-cyan-400 font-black text-xs tracking-wider">${{s.code}}</span>
                            <span class="px-2.5 py-0.5 rounded-lg bg-cyan-50 text-cyan-900 font-bold text-xs border border-cyan-200">${{s.module}}</span>
                        </div>
                        <span class="text-xs font-bold text-slate-500 bg-slate-100 px-3 py-1 rounded-lg">${{s.duration}}</span>
                    </div>
                    <h3 class="text-xl sm:text-2xl font-black text-slate-900 leading-snug">${{s.title}}</h3>
                    <div class="text-xs text-cyan-800 font-bold pt-1">
                        ${{s.semana}} • ${{s.horario}}
                    </div>
                </div>

                <div class="bg-cyan-50/60 rounded-2xl p-4 border border-cyan-200 space-y-1">
                    <div class="text-[11px] uppercase font-black tracking-wider text-cyan-900 flex items-center gap-1.5">
                        <i data-lucide="target" class="w-3.5 h-3.5 text-cyan-700"></i> Indicador de Logro / Objetivo Formativo
                    </div>
                    <p class="text-slate-800 text-xs leading-relaxed font-medium">${{s.objective}}</p>
                </div>

                <div class="space-y-4">
                    <h4 class="text-sm font-black text-slate-900 uppercase tracking-wide flex items-center gap-2 border-b border-slate-100 pb-2">
                        <i data-lucide="clock" class="w-4 h-4 text-cyan-700"></i> Secuencia Didáctica en Tres Momentos
                    </h4>

                    <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-1.5">
                        <div class="flex items-center justify-between">
                            <span class="font-bold text-xs text-blue-950 flex items-center gap-2">
                                <span class="w-2.5 h-2.5 rounded-full bg-blue-600"></span> Fase 1: Apertura
                            </span>
                            <span class="text-[11px] font-bold text-slate-500">20 Minutos</span>
                        </div>
                        <p class="text-slate-700 text-xs leading-relaxed pl-4.5">${{s.apertura}}</p>
                    </div>

                    <div class="p-4 rounded-2xl bg-cyan-50/40 border border-cyan-200 space-y-1.5">
                        <div class="flex items-center justify-between">
                            <span class="font-bold text-xs text-blue-950 flex items-center gap-2">
                                <span class="w-2.5 h-2.5 rounded-full bg-emerald-600"></span> Fase 2: Desarrollo & Práctica de Taller
                            </span>
                            <span class="text-[11px] font-bold text-emerald-800 bg-emerald-100 px-2 py-0.5 rounded">180 Minutos (Receso: 20 min)</span>
                        </div>
                        <p class="text-slate-700 text-xs leading-relaxed pl-4.5">${{s.desarrollo}}</p>
                    </div>

                    <div class="p-4 rounded-2xl bg-slate-50 border border-slate-200 space-y-1.5">
                        <div class="flex items-center justify-between">
                            <span class="font-bold text-xs text-blue-950 flex items-center gap-2">
                                <span class="w-2.5 h-2.5 rounded-full bg-purple-600"></span> Fase 3: Cierre, Evaluación y Orden 5S
                            </span>
                            <span class="text-[11px] font-bold text-slate-500">40 Minutos</span>
                        </div>
                        <p class="text-slate-700 text-xs leading-relaxed pl-4.5">${{s.cierre}}</p>
                    </div>
                </div>

                <div class="grid sm:grid-cols-2 gap-4 pt-2">
                    <div class="bg-emerald-50/60 rounded-2xl p-4 border border-emerald-200 space-y-1.5">
                        <div class="text-[11px] uppercase font-black tracking-wider text-emerald-900 flex items-center gap-1.5">
                            <i data-lucide="check-circle-2" class="w-3.5 h-3.5 text-emerald-700"></i> Evidencias & Producto Observable
                        </div>
                        <p class="text-slate-700 text-xs leading-relaxed">${{s.evidencias}}</p>
                    </div>

                    <div class="bg-slate-100 rounded-2xl p-4 border border-slate-200 space-y-1.5">
                        <div class="text-[11px] uppercase font-black tracking-wider text-slate-900 flex items-center gap-1.5">
                            <i data-lucide="shield-check" class="w-3.5 h-3.5 text-cyan-700"></i> Equipamiento & Bioseguridad en Fibra
                        </div>
                        <p class="text-slate-700 text-xs leading-relaxed">${{s.equipamiento}}</p>
                    </div>
                </div>
            `;
            lucide.createIcons();
        }}

        function filterCableList() {{
            const q = document.getElementById('cable-sec-search').value.toLowerCase();
            const filtered = cableSessionsData.filter(s => 
                s.title.toLowerCase().includes(q) || 
                s.code.toLowerCase().includes(q) ||
                s.module.toLowerCase().includes(q) ||
                s.objective.toLowerCase().includes(q)
            );
            document.getElementById('cable-count-badge').textContent = `${{filtered.length}} Sesiones`;
            renderCableSessionsList(filtered);
        }}

        function goToSession(num) {{
            switchTab('secuencias');
            selectCableSession(num);
        }}

        document.addEventListener('DOMContentLoaded', () => {{
            lucide.createIcons();
            selectCableSession(1);
        }});
    </script>
</body>
</html>
"""

with open(os.path.join(WEB_DIR, "cableado_estructurado.html"), "w", encoding="utf-8") as f:
    f.write(cableado_html)
print("Generado: Cursos/Web/cableado_estructurado.html")

# ==============================================================================
# ACTUALIZACIÓN DE INDEX.HTML CON LOS 4 CURSOS
# ==============================================================================
index_4_cursos_html = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Catálogo de Nuevos Cursos en Desarrollo | Ecosistema Kinal 2026</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@500;700;800;900&display=swap');
        body { font-family: 'Inter', sans-serif; background-color: #f8fafc; color: #0f172a; }
        h1, h2, h3, h4, .font-heading { font-family: 'Space Grotesk', sans-serif; }
        .hero-gradient {
            background: linear-gradient(135deg, #09172e 0%, #0f2d59 50%, #1e3a8a 100%);
        }
        .card-hover {
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }
        .card-hover:hover {
            transform: translateY(-4px);
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
        }
    </style>
</head>
<body class="antialiased min-h-screen flex flex-col">

    <!-- Top Institutional Header -->
    <header class="bg-slate-950 text-white border-b border-slate-800 sticky top-0 z-50 shadow-md">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3 flex flex-wrap justify-between items-center gap-4">
            <div class="flex items-center gap-3">
                <a href="../../index.html" class="bg-gradient-to-r from-amber-500 to-amber-600 text-slate-950 font-black text-xs tracking-wider uppercase px-2.5 py-1 rounded shadow-sm hover:opacity-90 transition flex items-center gap-1">
                    <i data-lucide="arrow-left" class="w-3.5 h-3.5"></i> Portal Maestro
                </a>
                <span class="text-slate-600">|</span>
                <div class="text-slate-200 font-bold text-xs sm:text-sm flex items-center gap-2">
                    <i data-lucide="folder-kanban" class="w-4 h-4 text-blue-400"></i>
                    Formación Continua & Empleabilidad • Portafolio de 4 Cursos
                </div>
            </div>
            <nav class="flex items-center gap-2 text-xs">
                <a href="../../TSU/index.html" class="px-3 py-1.5 rounded-lg bg-slate-800/80 hover:bg-slate-700 text-slate-300 transition flex items-center gap-1">
                    <i data-lucide="graduation-cap" class="w-3.5 h-3.5 text-blue-400"></i> TSU (3er Año)
                </a>
                <a href="../../Revision_Temarios/index.html" class="px-3 py-1.5 rounded-lg bg-slate-800/80 hover:bg-slate-700 text-slate-300 transition flex items-center gap-1">
                    <i data-lucide="wrench" class="w-3.5 h-3.5 text-amber-400"></i> Especialidades Técnicas
                </a>
            </nav>
        </div>
    </header>

    <!-- Hero Section -->
    <section class="hero-gradient text-white py-14 px-4 sm:px-6 lg:px-8">
        <div class="max-w-6xl mx-auto text-center space-y-4">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-500/20 border border-blue-400/30 text-blue-300 text-xs font-semibold">
                <i data-lucide="sparkles" class="w-3.5 h-3.5 text-amber-400"></i> Catálogo Curricular & Didáctico Kinal 2026 • Marco Alemán DQR 4-5
            </div>
            <h1 class="text-3xl sm:text-5xl font-black tracking-tight leading-tight text-white">
                Portafolio de Nuevos Cursos Técnicos en Desarrollo
            </h1>
            <p class="text-slate-300 text-sm sm:text-base max-w-3xl mx-auto leading-relaxed">
                Plataforma interactiva para la exploración y gestión de los programas formativos diseñados para la reconversión laboral, especialización industrial y actualización tecnológica bajo los estándares institucionales de <strong>Fundación Kinal</strong>.
            </p>

            <!-- Metrics Summary Grid (4 CURSOS) -->
            <div class="grid grid-cols-2 md:grid-cols-4 gap-4 pt-4 max-w-4xl mx-auto text-left">
                <div class="bg-white/10 backdrop-blur rounded-2xl p-4 border border-white/10">
                    <div class="text-[11px] uppercase tracking-wider text-slate-300 font-bold">Cursos en Diseño</div>
                    <div class="text-3xl font-black text-white">4 Activos</div>
                    <div class="text-[11px] text-amber-300 font-medium">Meca • Ciber • Auto • Cableado</div>
                </div>
                <div class="bg-white/10 backdrop-blur rounded-2xl p-4 border border-white/10">
                    <div class="text-[11px] uppercase tracking-wider text-slate-300 font-bold">Carga Formativa Total</div>
                    <div class="text-3xl font-black text-white">370 Horas</div>
                    <div class="text-[11px] text-emerald-300 font-medium">90h + 80h + 120h + 80h</div>
                </div>
                <div class="bg-white/10 backdrop-blur rounded-2xl p-4 border border-white/10">
                    <div class="text-[11px] uppercase tracking-wider text-slate-300 font-bold">Microdiseño Didáctico</div>
                    <div class="text-3xl font-black text-purple-300">80 Sesiones</div>
                    <div class="text-[11px] text-purple-200 font-medium">Apertura • Desarrollo • Cierre</div>
                </div>
                <div class="bg-white/10 backdrop-blur rounded-2xl p-4 border border-white/10">
                    <div class="text-[11px] uppercase tracking-wider text-slate-300 font-bold">Exigencia Terminal</div>
                    <div class="text-3xl font-black text-amber-400">≥ 75 Pts</div>
                    <div class="text-[11px] text-slate-300 font-medium">Ideario del «Trabajo Bien Hecho»</div>
                </div>
            </div>
        </div>
    </section>

    <!-- Main Content: Course Cards & Hub -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 space-y-12 flex-1">
        
        <div class="flex flex-col sm:flex-row justify-between items-start sm:items-end gap-4 border-b border-slate-200 pb-5">
            <div>
                <h2 class="text-2xl sm:text-3xl font-black text-slate-900 tracking-tight">
                    Cursos Disponibles para Consulta
                </h2>
                <p class="text-slate-600 text-sm mt-1">
                    Selecciona un curso para consultar su propuesta institucional, temario modular completo, dosificación detallada sesión por sesión y rúbricas.
                </p>
            </div>
            <div class="inline-flex items-center gap-2 px-3 py-1.5 rounded-lg bg-emerald-50 text-emerald-800 border border-emerald-200 text-xs font-bold">
                <i data-lucide="check-circle-2" class="w-4 h-4 text-emerald-600"></i> Documentación Word Oficial Sincronizada
            </div>
        </div>

        <!-- Course Cards Grid (2x2) -->
        <div class="grid lg:grid-cols-2 gap-8">
            
            <!-- TARJETA 1: MECATRÓNICA -->
            <div class="bg-white rounded-3xl border border-slate-200 p-7 shadow-sm card-hover flex flex-col justify-between space-y-6">
                <div class="space-y-4">
                    <div class="flex flex-wrap justify-between items-start gap-2">
                        <span class="px-3 py-1 rounded-full bg-blue-50 text-blue-900 font-extrabold text-xs tracking-wide uppercase border border-blue-200 flex items-center gap-1.5">
                            <i data-lucide="cpu" class="w-3.5 h-3.5 text-blue-700"></i> Modalidad 100% Presencial
                        </span>
                        <span class="px-2.5 py-0.5 rounded-md bg-amber-50 text-amber-900 border border-amber-200 text-xs font-bold">
                            DQR Nivel 4 - 5
                        </span>
                    </div>

                    <div>
                        <h3 class="text-2xl font-black text-slate-900 hover:text-blue-900 transition leading-snug">
                            Mecatrónica Industrial y Fabricación Digital Aplicada
                        </h3>
                        <p class="text-slate-600 text-sm mt-2 leading-relaxed">
                            Mecánica aplicada, tolerancias dimensionales, prototipado rápido en cortadora láser CO2, manufactura aditiva FDM, fresado CNC, electroneumática, automatización con PLC Siemens S7-1200 y puesta en marcha de celdas industriales integradas.
                        </p>
                    </div>

                    <!-- Tech Badges -->
                    <div class="flex flex-wrap gap-1.5 pt-1">
                        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-semibold">CAD 3D Paramétrico</span>
                        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-semibold">Láser CO2</span>
                        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-semibold">Impresión 3D FDM</span>
                        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-semibold">Mecanizado CNC</span>
                        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-semibold">PLC Siemens S7-1200</span>
                    </div>

                    <!-- Specific Course Metrics -->
                    <div class="grid grid-cols-3 gap-3 bg-slate-50 rounded-2xl p-3.5 border border-slate-200 text-center">
                        <div>
                            <div class="text-[10px] uppercase font-bold text-slate-500">Duración</div>
                            <div class="text-lg font-black text-blue-900">90 Horas</div>
                            <div class="text-[10px] text-slate-500">20 Sábados (4.5h)</div>
                        </div>
                        <div>
                            <div class="text-[10px] uppercase font-bold text-slate-500">Enfoque</div>
                            <div class="text-lg font-black text-emerald-700">75% Taller</div>
                            <div class="text-[10px] text-slate-500">25% Fundamentos</div>
                        </div>
                        <div>
                            <div class="text-[10px] uppercase font-bold text-slate-500">Proyecto</div>
                            <div class="text-lg font-black text-purple-900">Capstone</div>
                            <div class="text-[10px] text-slate-500">Celda Mecatrónica</div>
                        </div>
                    </div>
                </div>

                <!-- Action Buttons -->
                <div class="space-y-2.5 pt-2 border-t border-slate-100">
                    <a href="mecatronica.html" class="w-full inline-flex justify-center items-center gap-2 px-5 py-3 rounded-xl bg-blue-900 hover:bg-blue-800 text-white font-bold text-sm shadow-md transition">
                        <i data-lucide="eye" class="w-4 h-4"></i> Explorar Curso Web Completo
                    </a>
                    <div class="grid grid-cols-3 gap-2 text-center text-xs">
                        <a href="../Mecatrónica/Propuesta_Curso_Mecatronica_Kinal.docx" download class="p-2 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 font-medium transition flex items-center justify-center gap-1" title="Descargar Propuesta en Word">
                            <i data-lucide="file-text" class="w-3.5 h-3.5 text-blue-700"></i> Propuesta
                        </a>
                        <a href="../Mecatrónica/Temario_Curso_Mecatronica_Kinal.docx" download class="p-2 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 font-medium transition flex items-center justify-center gap-1" title="Descargar Temario en Word">
                            <i data-lucide="list-checks" class="w-3.5 h-3.5 text-emerald-700"></i> Temario
                        </a>
                        <a href="../Mecatrónica/Dosificacion_y_Secuencia_Didactica_Mecatronica_Kinal.docx" download class="p-2 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 font-medium transition flex items-center justify-center gap-1" title="Descargar Dosificación en Word">
                            <i data-lucide="calendar" class="w-3.5 h-3.5 text-amber-700"></i> Dosificación
                        </a>
                    </div>
                </div>
            </div>

            <!-- TARJETA 2: CIBERSEGURIDAD -->
            <div class="bg-white rounded-3xl border border-slate-200 p-7 shadow-sm card-hover flex flex-col justify-between space-y-6">
                <div class="space-y-4">
                    <div class="flex flex-wrap justify-between items-start gap-2">
                        <span class="px-3 py-1 rounded-full bg-indigo-50 text-indigo-900 font-extrabold text-xs tracking-wide uppercase border border-indigo-200 flex items-center gap-1.5">
                            <i data-lucide="shield-check" class="w-3.5 h-3.5 text-indigo-700"></i> Modalidad Híbrida (80/20)
                        </span>
                        <span class="px-2.5 py-0.5 rounded-md bg-amber-50 text-amber-900 border border-amber-200 text-xs font-bold">
                            DQR Nivel 4 - 5
                        </span>
                    </div>

                    <div>
                        <h3 class="text-2xl font-black text-slate-900 hover:text-indigo-900 transition leading-snug">
                            Ciberseguridad y Fundamentos de Seguridad de la Información
                        </h3>
                        <p class="text-slate-600 text-sm mt-2 leading-relaxed">
                            Protección de datos, identidad y accesos (IAM), comunicaciones seguras, gobierno, gestión de vulnerabilidades CVE/CVSS y cumplimiento de normativas internacionales mediante un Caso Práctico Transversal de Empresa Ficticia.
                        </p>
                    </div>

                    <!-- Tech Badges -->
                    <div class="flex flex-wrap gap-1.5 pt-1">
                        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-semibold">Tríada CIA / ITIL</span>
                        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-semibold">IAM / MFA / RBAC</span>
                        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-semibold">Criptografía & PKI</span>
                        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-semibold">CVE / CVSS</span>
                        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-semibold">ISO 27001 & SOC 2</span>
                    </div>

                    <!-- Specific Course Metrics -->
                    <div class="grid grid-cols-3 gap-3 bg-slate-50 rounded-2xl p-3.5 border border-slate-200 text-center">
                        <div>
                            <div class="text-[10px] uppercase font-bold text-slate-500">Duración</div>
                            <div class="text-lg font-black text-indigo-900">80 Horas</div>
                            <div class="text-[10px] text-slate-500">20 Sesiones (4h c/u)</div>
                        </div>
                        <div>
                            <div class="text-[10px] uppercase font-bold text-slate-500">Estructura</div>
                            <div class="text-lg font-black text-emerald-700">80% Virt. / 20% Pres.</div>
                            <div class="text-[10px] text-slate-500">64h Online / 16h Sede</div>
                        </div>
                        <div>
                            <div class="text-[10px] uppercase font-bold text-slate-500">Entregable</div>
                            <div class="text-lg font-black text-purple-900">Expediente</div>
                            <div class="text-[10px] text-slate-500">Caso Transversal</div>
                        </div>
                    </div>
                </div>

                <!-- Action Buttons -->
                <div class="space-y-2.5 pt-2 border-t border-slate-100">
                    <a href="ciberseguridad.html" class="w-full inline-flex justify-center items-center gap-2 px-5 py-3 rounded-xl bg-indigo-900 hover:bg-indigo-800 text-white font-bold text-sm shadow-md transition">
                        <i data-lucide="eye" class="w-4 h-4"></i> Explorar Curso Web Completo
                    </a>
                    <div class="grid grid-cols-3 gap-2 text-center text-xs">
                        <a href="../Ciberseguridad/Propuesta_Curso_Ciberseguridad_Kinal.docx" download class="p-2 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 font-medium transition flex items-center justify-center gap-1" title="Descargar Propuesta en Word">
                            <i data-lucide="file-text" class="w-3.5 h-3.5 text-indigo-700"></i> Propuesta
                        </a>
                        <a href="../Ciberseguridad/Temario_Curso_Ciberseguridad_Kinal.docx" download class="p-2 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 font-medium transition flex items-center justify-center gap-1" title="Descargar Temario en Word">
                            <i data-lucide="list-checks" class="w-3.5 h-3.5 text-emerald-700"></i> Temario
                        </a>
                        <a href="../Ciberseguridad/Dosificacion_y_Secuencia_Didactica_Ciberseguridad.docx" download class="p-2 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 font-medium transition flex items-center justify-center gap-1" title="Descargar Dosificación en Word">
                            <i data-lucide="calendar" class="w-3.5 h-3.5 text-amber-700"></i> Dosificación
                        </a>
                    </div>
                </div>
            </div>

            <!-- TARJETA 3: AUTOMATIZACIÓN Y CONTROL ELÉCTRICO -->
            <div class="bg-white rounded-3xl border border-slate-200 p-7 shadow-sm card-hover flex flex-col justify-between space-y-6">
                <div class="space-y-4">
                    <div class="flex flex-wrap justify-between items-start gap-2">
                        <span class="px-3 py-1 rounded-full bg-amber-50 text-amber-900 font-extrabold text-xs tracking-wide uppercase border border-amber-200 flex items-center gap-1.5">
                            <i data-lucide="zap" class="w-3.5 h-3.5 text-amber-600"></i> Híbrida Asimétrica (80/20)
                        </span>
                        <span class="px-2.5 py-0.5 rounded-md bg-blue-50 text-blue-900 border border-blue-200 text-xs font-bold">
                            DQR Nivel 4 - 5
                        </span>
                    </div>

                    <div>
                        <h3 class="text-2xl font-black text-slate-900 hover:text-amber-700 transition leading-snug">
                            Automatización y Control Eléctrico Industrial con PLC y VFD
                        </h3>
                        <p class="text-slate-600 text-sm mt-2 leading-relaxed">
                            Control electromagnético de potencia, seguridad eléctrica bajo norma NFPA 70E / LOTO, parametrización de variadores de frecuencia comerciales, programación en TIA Portal para PLC Siemens S7-1200, comunicación PROFINET y diagnóstico metódico de averías en líneas continuas.
                        </p>
                    </div>

                    <!-- Tech Badges -->
                    <div class="flex flex-wrap gap-1.5 pt-1">
                        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-semibold">NFPA 70E / LOTO</span>
                        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-semibold">Contactores AC-3</span>
                        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-semibold">Variadores VFD</span>
                        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-semibold">PLC Siemens S7-1200</span>
                        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-semibold">PROFINET / WinCC HMI</span>
                    </div>

                    <!-- Specific Course Metrics -->
                    <div class="grid grid-cols-3 gap-3 bg-slate-50 rounded-2xl p-3.5 border border-slate-200 text-center">
                        <div>
                            <div class="text-[10px] uppercase font-bold text-slate-500">Duración</div>
                            <div class="text-lg font-black text-amber-700">120 Horas</div>
                            <div class="text-[10px] text-slate-500">20 Sesiones (6h c/u)</div>
                        </div>
                        <div>
                            <div class="text-[10px] uppercase font-bold text-slate-500">Práctica</div>
                            <div class="text-lg font-black text-emerald-700">80% Banco</div>
                            <div class="text-[10px] text-slate-500">96h Taller / 24h LMS</div>
                        </div>
                        <div>
                            <div class="text-[10px] uppercase font-bold text-slate-500">Proyecto</div>
                            <div class="text-lg font-black text-blue-900">Certificación</div>
                            <div class="text-[10px] text-slate-500">Troubleshooting en Celda</div>
                        </div>
                    </div>
                </div>

                <!-- Action Buttons -->
                <div class="space-y-2.5 pt-2 border-t border-slate-100">
                    <a href="automatizacion.html" class="w-full inline-flex justify-center items-center gap-2 px-5 py-3 rounded-xl bg-slate-900 hover:bg-slate-800 text-amber-400 font-bold text-sm shadow-md transition">
                        <i data-lucide="eye" class="w-4 h-4"></i> Explorar Curso Web Completo
                    </a>
                    <div class="grid grid-cols-3 gap-2 text-center text-xs">
                        <a href="../Automatización/Propuesta_Curso_Automatizacion_Kinal.docx" download class="p-2 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 font-medium transition flex items-center justify-center gap-1" title="Descargar Propuesta en Word">
                            <i data-lucide="file-text" class="w-3.5 h-3.5 text-blue-700"></i> Propuesta
                        </a>
                        <a href="../Automatización/Temario_Curso_Automatizacion_Kinal.docx" download class="p-2 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 font-medium transition flex items-center justify-center gap-1" title="Descargar Temario en Word">
                            <i data-lucide="list-checks" class="w-3.5 h-3.5 text-emerald-700"></i> Temario
                        </a>
                        <a href="../Automatización/Dosificacion_y_Secuencia_Didactica_Automatizacion_Kinal.docx" download class="p-2 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 font-medium transition flex items-center justify-center gap-1" title="Descargar Dosificación en Word">
                            <i data-lucide="calendar" class="w-3.5 h-3.5 text-amber-700"></i> Dosificación
                        </a>
                    </div>
                </div>
            </div>

            <!-- TARJETA 4: CABLEADO ESTRUCTURADO Y FIBRA ÓPTICA -->
            <div class="bg-white rounded-3xl border border-slate-200 p-7 shadow-sm card-hover flex flex-col justify-between space-y-6">
                <div class="space-y-4">
                    <div class="flex flex-wrap justify-between items-start gap-2">
                        <span class="px-3 py-1 rounded-full bg-cyan-50 text-cyan-900 font-extrabold text-xs tracking-wide uppercase border border-cyan-200 flex items-center gap-1.5">
                            <i data-lucide="network" class="w-3.5 h-3.5 text-cyan-700"></i> Presencial con Apoyo Digital
                        </span>
                        <span class="px-2.5 py-0.5 rounded-md bg-amber-50 text-amber-900 border border-amber-200 text-xs font-bold">
                            DQR Nivel 4 - 5
                        </span>
                    </div>

                    <div>
                        <h3 class="text-2xl font-black text-slate-900 hover:text-cyan-700 transition leading-snug">
                            Cableado Estructurado y Redes de Cobre y Fibra Óptica
                        </h3>
                        <p class="text-slate-600 text-sm mt-2 leading-relaxed">
                            Canalizaciones físicas y cuartos de telecomunicaciones bajo ANSI/TIA-569, montaje de racks de 19'', conectorización Cat 6A, empalme de fibra óptica por fusión (&lt; 0.05 dB), certificación instrumental con escáneres Fluke Networks y rotulado TIA-606.
                        </p>
                    </div>

                    <!-- Tech Badges -->
                    <div class="flex flex-wrap gap-1.5 pt-1">
                        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-semibold">ANSI/TIA-568-E</span>
                        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-semibold">Cat 6A F/UTP</span>
                        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-semibold">Fusión Fibra OS2/OM4</span>
                        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-semibold">Fluke DSX Certificación</span>
                        <span class="px-2.5 py-1 rounded-lg bg-slate-100 text-slate-700 text-xs font-semibold">TIA-606 Rotulado</span>
                    </div>

                    <!-- Specific Course Metrics -->
                    <div class="grid grid-cols-3 gap-3 bg-slate-50 rounded-2xl p-3.5 border border-slate-200 text-center">
                        <div>
                            <div class="text-[10px] uppercase font-bold text-slate-500">Duración</div>
                            <div class="text-lg font-black text-cyan-800">80 Horas</div>
                            <div class="text-[10px] text-slate-500">20 Sesiones (4h c/u)</div>
                        </div>
                        <div>
                            <div class="text-[10px] uppercase font-bold text-slate-500">Horario</div>
                            <div class="text-lg font-black text-emerald-700">10 Semanas</div>
                            <div class="text-[10px] text-slate-500">Martes y Jueves</div>
                        </div>
                        <div>
                            <div class="text-[10px] uppercase font-bold text-slate-500">Entregable</div>
                            <div class="text-lg font-black text-purple-900">Dossier</div>
                            <div class="text-[10px] text-slate-500">Planos & Certificados</div>
                        </div>
                    </div>
                </div>

                <!-- Action Buttons -->
                <div class="space-y-2.5 pt-2 border-t border-slate-100">
                    <a href="cableado_estructurado.html" class="w-full inline-flex justify-center items-center gap-2 px-5 py-3 rounded-xl bg-cyan-900 hover:bg-cyan-800 text-white font-bold text-sm shadow-md transition">
                        <i data-lucide="eye" class="w-4 h-4"></i> Explorar Curso Web Completo
                    </a>
                    <div class="grid grid-cols-3 gap-2 text-center text-xs">
                        <a href="../Cableado_Estructurado/Propuesta_Curso_Cableado_Estructurado_Kinal.docx" download class="p-2 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 font-medium transition flex items-center justify-center gap-1" title="Descargar Propuesta en Word">
                            <i data-lucide="file-text" class="w-3.5 h-3.5 text-blue-700"></i> Propuesta
                        </a>
                        <a href="../Cableado_Estructurado/Temario_Curso_Cableado_Estructurado_Kinal.docx" download class="p-2 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 font-medium transition flex items-center justify-center gap-1" title="Descargar Temario en Word">
                            <i data-lucide="list-checks" class="w-3.5 h-3.5 text-emerald-700"></i> Temario
                        </a>
                        <a href="../Cableado_Estructurado/Dosificacion_y_Secuencia_Didactica_Cableado_Estructurado_Kinal.docx" download class="p-2 rounded-lg bg-slate-100 hover:bg-slate-200 text-slate-700 font-medium transition flex items-center justify-center gap-1" title="Descargar Dosificación en Word">
                            <i data-lucide="calendar" class="w-3.5 h-3.5 text-amber-700"></i> Dosificación
                        </a>
                    </div>
                </div>
            </div>

        </div>

        <!-- Comparative Matrix (4 Cursos) -->
        <div class="bg-white rounded-3xl border border-slate-200 p-8 shadow-sm space-y-6">
            <div class="space-y-1">
                <h3 class="text-xl font-black text-slate-900 flex items-center gap-2">
                    <i data-lucide="sliders-horizontal" class="w-5 h-5 text-blue-700"></i>
                    Matriz Comparativa Ejecutiva de los 4 Programas en Desarrollo
                </h3>
                <p class="text-slate-600 text-xs">
                    Comparación transversal de parámetros metodológicos, temporales y evaluativos entre todas las especialidades.
                </p>
            </div>

            <div class="overflow-x-auto">
                <table class="w-full text-xs text-left border-collapse">
                    <thead>
                        <tr class="bg-slate-100 text-slate-700 uppercase font-black tracking-wider border-b border-slate-200">
                            <th class="py-3 px-4">Dimensión Curricular</th>
                            <th class="py-3 px-4 text-blue-900">Mecatrónica Industrial</th>
                            <th class="py-3 px-4 text-indigo-900">Ciberseguridad TI</th>
                            <th class="py-3 px-4 text-amber-800">Automatización & PLC</th>
                            <th class="py-3 px-4 text-cyan-800">Cableado & Fibra</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-100 text-slate-700">
                        <tr>
                            <td class="py-3 px-4 font-bold bg-slate-50">Carga Horaria</td>
                            <td class="py-3 px-4">90 Horas (20 sábados • 4.5h)</td>
                            <td class="py-3 px-4">80 Horas (20 sesiones • 4h)</td>
                            <td class="py-3 px-4 font-bold text-amber-900">120 Horas (20 sesiones • 6h)</td>
                            <td class="py-3 px-4">80 Horas (20 sesiones • 4h)</td>
                        </tr>
                        <tr>
                            <td class="py-3 px-4 font-bold bg-slate-50">Modalidad</td>
                            <td class="py-3 px-4"><span class="px-2 py-0.5 rounded bg-blue-100 text-blue-800 font-bold">100% Presencial</span></td>
                            <td class="py-3 px-4"><span class="px-2 py-0.5 rounded bg-indigo-100 text-indigo-800 font-bold">Híbrida (80/20)</span></td>
                            <td class="py-3 px-4"><span class="px-2 py-0.5 rounded bg-amber-100 text-amber-800 font-bold">Híbrida Práctica (80/20)</span></td>
                            <td class="py-3 px-4"><span class="px-2 py-0.5 rounded bg-cyan-100 text-cyan-800 font-bold">Presencial en Taller</span></td>
                        </tr>
                        <tr>
                            <td class="py-3 px-4 font-bold bg-slate-50">Módulos</td>
                            <td class="py-3 px-4">5 Módulos temáticos</td>
                            <td class="py-3 px-4">8 Módulos progresivos</td>
                            <td class="py-3 px-4">4 Módulos de 30h</td>
                            <td class="py-3 px-4">4 Módulos de 20h</td>
                        </tr>
                        <tr>
                            <td class="py-3 px-4 font-bold bg-slate-50">Equipamiento</td>
                            <td class="py-3 px-4">Láser CO2, FDM, CNC, Festo, S7-1200</td>
                            <td class="py-3 px-4">Linux, Wireshark, SIEM, NIST NVD</td>
                            <td class="py-3 px-4">Bancos de potencia, VFDs, S7-1200, KTP HMI</td>
                            <td class="py-3 px-4">Racks 42U, Fusionadora fibra, Fluke DSX</td>
                        </tr>
                        <tr>
                            <td class="py-3 px-4 font-bold bg-slate-50">Entregable Terminal</td>
                            <td class="py-3 px-4 font-bold">Celda Mecatrónica Funcional</td>
                            <td class="py-3 px-4 font-bold">Expediente Caso Transversal</td>
                            <td class="py-3 px-4 font-bold">Celda Operativa + Troubleshooting</td>
                            <td class="py-3 px-4 font-bold">Certificación Rack + As-Built</td>
                        </tr>
                        <tr>
                            <td class="py-3 px-4 font-bold bg-slate-50">Nota Mínima</td>
                            <td class="py-3 px-4 font-bold text-amber-700">75 / 100 Pts</td>
                            <td class="py-3 px-4 font-bold text-amber-700">75 / 100 Pts</td>
                            <td class="py-3 px-4 font-bold text-amber-700">75 / 100 Pts</td>
                            <td class="py-3 px-4 font-bold text-amber-700">75 / 100 Pts</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>

        <!-- Institutional Quotes & Philosophy Section -->
        <div class="grid md:grid-cols-2 gap-6 text-xs">
            <div class="bg-blue-50 border-l-4 border-blue-900 p-5 rounded-r-2xl space-y-2">
                <div class="font-extrabold text-blue-900 uppercase tracking-wide">Misión Institucional de Fundación Kinal</div>
                <p class="text-slate-700 italic leading-relaxed">
                    «Formar a jóvenes y adultos a través de una educación integral, con énfasis en las áreas técnicas y tecnológicas, influyendo positivamente en su trabajo, su familia y la sociedad».
                </p>
            </div>
            <div class="bg-amber-50 border-l-4 border-amber-600 p-5 rounded-r-2xl space-y-2">
                <div class="font-extrabold text-amber-900 uppercase tracking-wide">Valores Nucleares de Kinal</div>
                <p class="text-slate-700 italic leading-relaxed">
                    «Visión cristiana de la vida. Respeto a la dignidad de la persona. Espíritu de servicio. Trabajo bien hecho. Libertad personal responsable».
                </p>
            </div>
        </div>

    </main>

    <!-- Footer -->
    <footer class="bg-slate-950 text-slate-400 py-8 border-t border-slate-800 text-xs">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex flex-col sm:flex-row justify-between items-center gap-4 text-center sm:text-left">
            <div>
                <p class="font-bold text-slate-200">Fundación Kinal • Dirección Académica & Escuela Técnica Superior</p>
                <p class="text-slate-500">Diseño Curricular, Didáctico e Instruccional 2026 | Sistema Dual & DQR 4-5</p>
            </div>
            <div class="flex items-center gap-4">
                <a href="../../index.html" class="hover:text-amber-400 transition">Portal Maestro</a>
                <span class="text-slate-700">•</span>
                <a href="mecatronica.html" class="hover:text-amber-400 transition">Mecatrónica</a>
                <span class="text-slate-700">•</span>
                <a href="ciberseguridad.html" class="hover:text-amber-400 transition">Ciberseguridad</a>
                <span class="text-slate-700">•</span>
                <a href="automatizacion.html" class="hover:text-amber-400 transition">Automatización</a>
                <span class="text-slate-700">•</span>
                <a href="cableado_estructurado.html" class="hover:text-amber-400 transition">Cableado Estructurado</a>
            </div>
        </div>
    </footer>

    <script>
        lucide.createIcons();
    </script>
</body>
</html>
"""

with open(os.path.join(WEB_DIR, "index.html"), "w", encoding="utf-8") as f:
    f.write(index_4_cursos_html)
print("Actualizado: Cursos/Web/index.html con los 4 cursos.")
