#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador del Archivo Temporal 'automotriz_temporal.html'
Alinea la maquetación gráfica de los pensums de Mecánica (Automotriz y Motocicletas) con el estándar de Construcción:
- Una tarjeta por módulo en cuadrícula de 2 columnas (grid lg:grid-cols-2 gap-8 pt-4).
- Cada tarjeta de módulo con encabezado oscuro (bg-slate-900 text-white), logro esperado y duración.
- Todos los temas del módulo apilados dentro de la tarjeta de ese módulo.
- Filtros interactivos funcionales para cada curso.
- Nomenclatura institucional estricta:
  * "Industrial" para Mecánica Industrial (enlace a mecanica_temporal.html)
  * "Mecánica" para Mecánica Automotriz y Motocicletas (esta página)
"""

import os
import re
import sys
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

SOURCE_HTML = r"D:\OneDrive\Software\Antigravity\Diseño Instruccional\automotriz.html"
OUTPUT_HTML = r"D:\OneDrive\Software\Antigravity\Diseño Instruccional\automotriz_temporal.html"

# Metadata pedagógica de los 48 módulos de los 6 cursos
MODULE_METADATA = {
    "motores_gasolina": [
        {
            "num": 1,
            "weeks": "Semanas 1 a 4",
            "hours": "18 Horas",
            "logro": "Comprender la termodinámica del ciclo Otto de 4 tiempos, clasificación de motores e identificación anatómica de componentes fijos y móviles del motor."
        },
        {
            "num": 2,
            "weeks": "Semanas 5 a 8",
            "hours": "18 Horas",
            "logro": "Diagnosticar pérdidas de compresión, hermeticidad de cilindros y consumo anómalo de aceite mediante manómetros, vacuómetros y detector de fugas."
        },
        {
            "num": 3,
            "weeks": "Semanas 9 a 12",
            "hours": "18 Horas",
            "logro": "Poner a punto trenes de distribución por cadena, faja dentada y engranajes, inspeccionando tensores hidráulicos y calado de árboles de levas."
        },
        {
            "num": 4,
            "weeks": "Semanas 13 a 16",
            "hours": "18 Horas",
            "logro": "Comprobar planitud de culata con regla de pelo y galgas, asentar válvulas, sustituir sellos de guía y calibrar holguras de punterías."
        },
        {
            "num": 5,
            "weeks": "Semanas 17 a 20",
            "hours": "18 Horas",
            "logro": "Medir conicidad, ovalamiento y desgaste de cilindros con alexómetro micrométrico, bruñir camisas y verificar conductos de lubricación y refrigeración."
        },
        {
            "num": 6,
            "weeks": "Semanas 21 a 24",
            "hours": "18 Horas",
            "logro": "Ajustar cojinetes de biela y bancada con Plastigage, verificar luz de aceite, holgura entre puntas de anillos y alineación axial de cigüeñal."
        },
        {
            "num": 7,
            "weeks": "Semanas 25 a 28",
            "hours": "18 Horas",
            "logro": "Aplicar leyes eléctricas, medir caídas de tensión y verificar consumidores de alto amperaje en los circuitos de soporte del motor."
        },
        {
            "num": 8,
            "weeks": "Semanas 29 a 32",
            "hours": "18 Horas",
            "logro": "Conectar equipos de diagnóstico al puerto DLC, interpretar códigos de falla DTC (genéricos y de fabricante) y leer flujo de datos en tiempo real."
        },
        {
            "num": 9,
            "weeks": "Semanas 33 a 36",
            "hours": "18 Horas",
            "logro": "Evaluar bobinas individuales COP y paquetes DIS con osciloscopio automotriz, inspeccionando bujías de iridio/platino y tiempo de quemado."
        },
        {
            "num": 10,
            "weeks": "Semanas 37 a 40",
            "hours": "18 Horas",
            "logro": "Comprobar presión, caudal y caída de presión en rieles MPI y bombas de alta presión GDI, diagnosticando inyectores y reguladores de combustible."
        }
    ],
    "mecanismos_automovil": [
        {
            "num": 1,
            "weeks": "Semanas 1 a 4",
            "hours": "18 Horas",
            "logro": "Utilizar vernier, micrómetro exterior y torquímetros con precisión en milímetros y pulgadas, aplicando normas de seguridad en el taller mecánico."
        },
        {
            "num": 2,
            "weeks": "Semanas 5 a 8",
            "hours": "18 Horas",
            "logro": "Inspeccionar, rectificar y sustituir discos, tambores, pastillas y zapatas de freno, verificando espesores mínimos y alabeo lateral con reloj comparador."
        },
        {
            "num": 3,
            "weeks": "Semanas 9 a 12",
            "hours": "18 Horas",
            "logro": "Diagnosticar la bomba principal, servofreno (booster), purgar líneas con fluido DOT 3/4/5.1 y comprobar funcionamiento de válvulas dosificadoras."
        },
        {
            "num": 4,
            "weeks": "Semanas 13 a 16",
            "hours": "18 Horas",
            "logro": "Desmontar, diagnosticar y reemplazar amortiguadores McPherson, resortes helicoidales, rótulas, terminales y barras estabilizadoras de suspensión."
        },
        {
            "num": 5,
            "weeks": "Semanas 17 a 20",
            "hours": "18 Horas",
            "logro": "Evaluar cajas de dirección mecánicas, hidráulicas y asistidas eléctricamente (EPS), ajustando precarga de cremallera y geometría de alineación."
        },
        {
            "num": 6,
            "weeks": "Semanas 21 a 24",
            "hours": "18 Horas",
            "logro": "Diagnosticar plato de presión, disco de fricción, collarín y volante bimasa, ajustando accionamientos hidráulicos y mecánicos de embrague."
        },
        {
            "num": 7,
            "weeks": "Semanas 25 a 28",
            "hours": "18 Horas",
            "logro": "Desarmar transmisiones manuales para inspeccionar sincronizadores, trenes de engranajes, rodamientos cónicos y horquillas selectoras de cambio."
        },
        {
            "num": 8,
            "weeks": "Semanas 29 a 32",
            "hours": "18 Horas",
            "logro": "Reparar juntas homocinéticas, flechas de tracción delantera, crucetas de cardán y soportes centrales en vehículos con tracción RWD y 4WD."
        },
        {
            "num": 9,
            "weeks": "Semanas 33 a 36",
            "hours": "18 Horas",
            "logro": "Ajustar holgura de corona y piñón de ataque (backlash), precarga de rodamientos y patrón de contacto con azul de Prusia en diferenciales automotrices."
        },
        {
            "num": 10,
            "weeks": "Semanas 37 a 40",
            "hours": "18 Horas",
            "logro": "Diagnosticar mandos electrohidráulicos en transmisiones automáticas y CVT, reconociendo solenoides de cambio y sensores de velocidad de flecha."
        }
    ],
    "electromecanica_automotriz": [
        {
            "num": 1,
            "weeks": "Semanas 1 a 4",
            "hours": "18 Horas",
            "logro": "Calcular y medir voltaje, corriente y resistencia en circuitos serie, paralelo y mixtos, detectando cortocircuitos y caídas de tensión parásitas."
        },
        {
            "num": 2,
            "weeks": "Semanas 5 a 8",
            "hours": "18 Horas",
            "logro": "Probar diodos rectificadores, transistores bipolares/MOSFET y reguladores integrados utilizados en módulos de control vehicular."
        },
        {
            "num": 3,
            "weeks": "Semanas 9 a 12",
            "hours": "18 Horas",
            "logro": "Operar DMM automotriz con medición de ciclo de trabajo (Duty Cycle), frecuencia en Hertz y prueba de consumo de corriente en reposo (parasitic drain)."
        },
        {
            "num": 4,
            "weeks": "Semanas 13 a 16",
            "hours": "18 Horas",
            "logro": "Realizar pruebas de conductancia digital (CCA), carga lenta/rápida, densidad de electrolito y diagnóstico de baterías con tecnología Start-Stop (EFB/AGM)."
        },
        {
            "num": 5,
            "weeks": "Semanas 17 a 20",
            "hours": "18 Horas",
            "logro": "Diagnosticar y reparar motores de arranque, solenoide, conmutador, escobillas e inducido, evaluando caída de tensión durante el arranque del motor."
        },
        {
            "num": 6,
            "weeks": "Semanas 21 a 24",
            "hours": "18 Horas",
            "logro": "Comprobar alternadores trifásicos, puente de diodos, rizado de CA con osciloscopio y sistemas de carga controlados por PWM por la ECU/PCM."
        },
        {
            "num": 7,
            "weeks": "Semanas 25 a 28",
            "hours": "18 Horas",
            "logro": "Rastrear circuitos en diagramas esquemáticos bajo normativas DIN (alemana) y SAE (americana), identificando tierras, fusibles y relevadores."
        },
        {
            "num": 8,
            "weeks": "Semanas 29 a 32",
            "hours": "18 Horas",
            "logro": "Reparar luces principales (halógeno, xenón HID y LED automotriz), limpia-parabrisas, elevavidrios y cierre centralizado mediante módulos BCM."
        },
        {
            "num": 9,
            "weeks": "Semanas 33 a 36",
            "hours": "18 Horas",
            "logro": "Analizar sensores de posición inductivos y de efecto Hall (CKP/CMP) y su sincronización en el disparo del encendido electrónico automotriz."
        },
        {
            "num": 10,
            "weeks": "Semanas 37 a 40",
            "hours": "18 Horas",
            "logro": "Interpretar formas de onda de primario y secundario de encendido en osciloscopio, detectando fugas de alta tensión y fallas de ignición (misfire)."
        }
    ],
    "inyeccion_electronica": [
        {
            "num": 1,
            "weeks": "Semanas 1 a 4",
            "hours": "18 Horas",
            "logro": "Comprender la arquitectura de microprocesadores de la PCM, convertidores analógico-digitales (ADC) y fuentes reguladas de referencia (5V)."
        },
        {
            "num": 2,
            "weeks": "Semanas 5 a 8",
            "hours": "18 Horas",
            "logro": "Distinguir estrategias de inyección multipunto (MPI), inyección directa estratificada/homogénea (GDI) y control en bucle abierto/cerrado."
        },
        {
            "num": 3,
            "weeks": "Semanas 9 a 12",
            "hours": "18 Horas",
            "logro": "Diagnosticar sensores térmicos (ECT, IAT) por termistores NTC, sensores de posición (TPS, APP) y potenciómetros sin contacto."
        },
        {
            "num": 4,
            "weeks": "Semanas 13 a 16",
            "hours": "18 Horas",
            "logro": "Evaluar sensores de flujo de masa de aire de hilo caliente (MAF) y de presión absoluta de múltiple (MAP) con voltímetro y escáner automotriz."
        },
        {
            "num": 5,
            "weeks": "Semanas 17 a 20",
            "hours": "18 Horas",
            "logro": "Analizar sensores de circonio convencionales y sondas lambda de banda ancha (A/F Ratio), diagnosticando catalizadores y recirculación EGR."
        },
        {
            "num": 6,
            "weeks": "Semanas 21 a 24",
            "hours": "18 Horas",
            "logro": "Probar inyectores saturados y de retención por pico (Peak and Hold), ciclo de inyección en milisegundos y actuadores PWM en bomba de combustible."
        },
        {
            "num": 7,
            "weeks": "Semanas 25 a 28",
            "hours": "18 Horas",
            "logro": "Analizar los ajustes de combustible a corto y largo plazo (Short/Long Term Fuel Trims), Monitores OBD-II y cuadros congelados (Freeze Frame)."
        },
        {
            "num": 8,
            "weeks": "Semanas 29 a 32",
            "hours": "18 Horas",
            "logro": "Medir resistencias de terminación de 120 ohms en bus CAN-High/CAN-Low y decodificar tramas diferenciales de alta velocidad con osciloscopio."
        },
        {
            "num": 9,
            "weeks": "Semanas 33 a 36",
            "hours": "18 Horas",
            "logro": "Localizar pines de potencia, masas de chasis y líneas de datos entre PCM, TCM, BCM y tablero de instrumentos en esquemas OEM."
        },
        {
            "num": 10,
            "weeks": "Semanas 37 a 40",
            "hours": "18 Horas",
            "logro": "Ejecutar pruebas bidireccionales de actuadores, reseteo de adaptaciones de mezcla, calibración de cuerpos de aceleración TAC y reaprendizajes."
        }
    ],
    "aire_acondicionado": [
        {
            "num": 1,
            "weeks": "Semanas 1 a 20",
            "hours": "90 Horas",
            "logro": "Dominar el ciclo termodinámico de climatización vehicular, refrigerantes R-134a y HFO-1234yf, servicio a compresores fijos/variables, recuperación de gas, vacío profundo y recarga por peso."
        },
        {
            "num": 2,
            "weeks": "Semanas 21 a 40",
            "hours": "90 Horas",
            "logro": "Diagnosticar presostatos binarios/trinarios, transductores lineales, válvulas solenoide PWM, servomotores de mezcla y el módulo climatizador automático (HVAC) con escáner."
        }
    ],
    "mecanica_motocicletas": [
        {
            "num": 1,
            "weeks": "Semanas 1 a 7",
            "hours": "30 Horas",
            "logro": "Utilizar torquímetros, calibradores de lainas y micrómetros para el mantenimiento preventivo del bastidor, ruedas, rodamientos cónicos y pernos de chasis."
        },
        {
            "num": 2,
            "weeks": "Semanas 8 a 14",
            "hours": "30 Horas",
            "logro": "Reacondicionar horquillas telescópicas convencionales e invertidas, amortiguadores monoshock, purgar frenos hidráulicos y calibrar sistemas de tambor."
        },
        {
            "num": 3,
            "weeks": "Semanas 15 a 21",
            "hours": "30 Horas",
            "logro": "Comprobar estatores trifásicos y monofásicos de magneto permanente, reguladores-rectificadores de voltaje, bobinas de alta tensión y módulos CDI/TCI."
        },
        {
            "num": 4,
            "weeks": "Semanas 22 a 28",
            "hours": "30 Horas",
            "logro": "Calibrar carburadores de vacío constante (CV), sincronizar carburadores múltiples con vacuómetros y diagnosticar sistemas de inyección electrónica EFI para motos."
        },
        {
            "num": 5,
            "weeks": "Semanas 29 a 34",
            "hours": "30 Horas",
            "logro": "Desarmar y evaluar cilindro, pistón, anillos, árbol de levas OHC/DOHC, calibrar válvulas y reparar cajas secuenciales con embrague multidisco en baño de aceite."
        },
        {
            "num": 6,
            "weeks": "Semanas 35 a 40",
            "hours": "30 Horas",
            "logro": "Aplicar protocolos de diagnóstico sistemático para identificar ruidos internos de biela/cadena, fallas de compresión, embragues centrífugos y fallas de ignición."
        }
    ]
}


def build_module_card_html(mod_meta, mod_title, items):
    """
    Construye la tarjeta de módulo idéntica a la de construccion.html.
    """
    topics_html_list = []
    for idx, item in enumerate(items, 1):
        status = item.get('data-status', 'keep')
        # Title of topic
        title_span = item.find('span', class_=re.compile(r'font-bold'))
        raw_title = title_span.get_text(strip=True) if title_span else ""
        # Remove any existing leading number if present
        clean_title = re.sub(r'^\d+[\.\)]\s*', '', raw_title)
        
        # Badge
        badge_span = item.find('span', class_=re.compile(r'rounded'))
        badge_text = badge_span.get_text(strip=True) if badge_span else "🟢"
        
        # Color style
        if status == 'delete':
            item_cls = 'item-delete'
            badge_cls = 'bg-red-100 text-red-800'
        elif status == 'update':
            item_cls = 'item-update'
            badge_cls = 'bg-amber-100 text-amber-800'
        elif status == 'new':
            item_cls = 'item-new'
            badge_cls = 'bg-blue-100 text-blue-700'
        else: # keep
            item_cls = 'item-keep'
            badge_cls = 'bg-emerald-100 text-emerald-800'

        # Description / text
        p_desc = item.find('p')
        desc_text = p_desc.decode_contents() if p_desc else ""

        # Category / Linea formativa
        cat_div = item.find('div', class_=re.compile(r'uppercase'))
        cat_html = ""
        if cat_div:
            cat_html = f'<div class="text-[11px] font-medium text-slate-500 uppercase tracking-wider">{cat_div.get_text(strip=True)}</div>'

        topic_card = f"""
                            <div class="content-item {item_cls} p-3 rounded text-xs space-y-1" data-status="{status}">
                                <div class="flex justify-between items-center font-bold">
                                    <span>{idx}. {clean_title}</span>
                                    <span class="px-2 py-0.5 rounded text-xs font-bold whitespace-nowrap {badge_cls}">{badge_text}</span>
                                </div>
                                {cat_html}
                                <p class="text-slate-700 leading-relaxed">{desc_text}</p>
                            </div>"""
        topics_html_list.append(topic_card)

    all_topics_joined = "\n".join(topics_html_list)

    card_html = f"""
                    <!-- MÓDULO {mod_meta['num']} -->
                    <div class="bg-white rounded-xl border border-slate-300 shadow-sm overflow-hidden flex flex-col">
                        <div class="bg-slate-900 text-white p-4 border-b border-slate-800">
                            <div class="flex justify-between items-center text-xs text-amber-400 font-semibold mb-1">
                                <span>MÓDULO {mod_meta['num']} ({mod_meta['weeks']})</span>
                                <span>Duración: ~{mod_meta['hours']}</span>
                            </div>
                            <h4 class="text-lg font-bold">{mod_title}</h4>
                            <p class="text-xs text-slate-300 mt-1">
                                <strong>Logro esperado:</strong> {mod_meta['logro']}
                            </p>
                        </div>
                        <div class="p-5 divide-y divide-slate-100 flex-1 space-y-2">
{all_topics_joined}
                        </div>
                    </div>"""
    return card_html


def transform_automotriz():
    print(f"Leyendo archivo fuente: {SOURCE_HTML}")
    with open(SOURCE_HTML, 'r', encoding='utf-8') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    courses_config = [
        ("motores_gasolina", "Mecánica de Motores de Gasolina", "propuesta_motores_gasolina"),
        ("mecanismos_automovil", "Mecanismos del Automóvil", "propuesta_mecanismos_automovil"),
        ("electromecanica_automotriz", "Electromecánica Automotriz", "propuesta_electromecanica_automotriz"),
        ("inyeccion_electronica", "Inyección Electrónica Automotriz", "propuesta_inyeccion_electronica"),
        ("aire_acondicionado", "Aire Acondicionado Automotriz", "propuesta_aire_acondicionado"),
        ("mecanica_motocicletas", "Mecánica de Motocicletas", "propuesta_mecanica_motocicletas")
    ]

    for c_key, c_name, sec_id in courses_config:
        pane = soup.find('div', id=f'course-pane-{c_key}')
        if not pane:
            print(f"[WARN] No se encontró pane: course-pane-{c_key}")
            continue

        print(f"\nProcesando curso: {c_name} (pane: course-pane-{c_key})")
        
        # 1. Encontrar la Sección 3
        sec3_tag = None
        for sec in pane.find_all('section'):
            txt = sec.get_text()
            if 'Sección 3' in txt or 'Distribución Modular' in txt or 'propuesta' in sec.get('id', ''):
                sec3_tag = sec
                break

        if not sec3_tag:
            print(f"[WARN] No se encontró Sección 3 en {c_key}")
            continue

        print(f"Sección 3 encontrada para {c_key}")

        # Extraer módulos actuales dentro de Sección 3
        # En automotriz.html están en divs con class 'bg-slate-50/50'
        mod_divs = sec3_tag.find_all('div', class_=re.compile(r'bg-slate-50/50'))
        print(f"Módulos detectados en {c_key}: {len(mod_divs)}")

        mod_metas = MODULE_METADATA.get(c_key, [])
        new_module_cards = []

        for idx, mod_div in enumerate(mod_divs):
            h4 = mod_div.find('h4')
            mod_title = h4.get_text(strip=True) if h4 else f"Módulo {idx+1}"
            
            # Extraer topics dentro de este módulo
            items = mod_div.find_all('div', class_=re.compile(r'\bcontent-item\b'))
            
            # Metadata correspondiente
            if idx < len(mod_metas):
                meta = mod_metas[idx]
            else:
                meta = {
                    "num": idx + 1,
                    "weeks": f"Semanas {idx*4+1} a {(idx+1)*4}",
                    "hours": "18 Horas",
                    "logro": f"Dominio teórico y práctico de {mod_title} conforme a los estándares de la industria automotriz."
                }

            card_html = build_module_card_html(meta, mod_title, items)
            new_module_cards.append(card_html)

        # Contadores de items para los botones de filtro
        all_items = sec3_tag.find_all('div', class_=re.compile(r'\bcontent-item\b'))
        cnt_all = len(all_items)
        cnt_del = len([it for it in all_items if it.get('data-status') == 'delete'])
        cnt_upd = len([it for it in all_items if it.get('data-status') == 'update'])
        cnt_new = len([it for it in all_items if it.get('data-status') == 'new'])
        cnt_keep = len([it for it in all_items if it.get('data-status') == 'keep'])

        legend_html = """
                <!-- Código de Leyenda Explicativo -->
                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3 text-xs">
                    <div class="p-3 rounded-lg border border-red-200 bg-red-50 text-red-900 flex items-start gap-2">
                        <span class="inline-block w-3 h-3 rounded-full bg-red-500 mt-0.5 shrink-0"></span>
                        <div>
                            <strong>Color Rojo (Eliminar):</strong> Prácticas obsoletas o solapamientos retirados para maximizar horas de diagnóstico práctico.
                        </div>
                    </div>
                    <div class="p-3 rounded-lg border border-yellow-300 bg-yellow-50 text-yellow-900 flex items-start gap-2">
                        <span class="inline-block w-3 h-3 rounded-full bg-yellow-500 mt-0.5 shrink-0"></span>
                        <div>
                            <strong>Color Amarillo (Actualizar):</strong> Temas modernizados a inyección electrónica GDI/Common Rail, CAN-Bus y refrigerantes ecológicos.
                        </div>
                    </div>
                    <div class="p-3 rounded-lg border border-blue-200 bg-blue-50 text-blue-900 flex items-start gap-2">
                        <span class="inline-block w-3 h-3 rounded-full bg-blue-500 mt-0.5 shrink-0"></span>
                        <div>
                            <strong>Color Azul (Nuevo Propuesto):</strong> Competencias de osciloscopio, diagnósticos computarizados y transmisiones modernas.
                        </div>
                    </div>
                    <div class="p-3 rounded-lg border border-emerald-200 bg-emerald-50 text-emerald-900 flex items-start gap-2">
                        <span class="inline-block w-3 h-3 rounded-full bg-emerald-500 mt-0.5 shrink-0"></span>
                        <div>
                            <strong>Color Verde (Mantener):</strong> Fundamentos de metrología, ajustes mecánicos y desarmado que conservan plena vigencia.
                        </div>
                    </div>
                </div>"""

        new_sec3_html = f"""
        <!-- SECCIÓN 3: PROPUESTA CURRICULAR CON CÓDIGO DE COLOR -->
        <section id="{sec_id}" class="space-y-6">
            <div class="bg-white rounded-2xl border border-slate-200 p-6 sm:p-8 shadow-sm space-y-6">
                <div class="flex flex-wrap items-center justify-between gap-4 border-b border-slate-100 pb-4">
                    <div class="flex items-center gap-3">
                        <div class="p-2.5 rounded-lg bg-indigo-50 text-indigo-700">
                            <i data-lucide="git-merge" class="w-6 h-6"></i>
                        </div>
                        <div>
                            <h3 class="text-xl font-bold text-slate-900">
                                3. Distribución Modular Auditada con Código de Color
                            </h3>
                            <p class="text-sm text-slate-500">
                                Visualización interactiva que resalta exactamente qué eliminar, qué actualizar y qué incorporar según los estándares automotrices.
                            </p>
                        </div>
                    </div>

                    <!-- Botones de Filtro -->
                    <div class="flex flex-wrap items-center gap-2 text-xs font-semibold no-print">
                        <button onclick="filterEtsItems('all', '{c_key}')" id="btn-all-{c_key}" class="px-3 py-1.5 rounded-lg bg-slate-900 text-white shadow-sm transition">Todos ({cnt_all})</button>
                        <button onclick="filterEtsItems('delete', '{c_key}')" id="btn-delete-{c_key}" class="px-3 py-1.5 rounded-lg bg-red-100 text-red-700 hover:bg-red-200 transition">🔴 Solo Eliminar ({cnt_del})</button>
                        <button onclick="filterEtsItems('update', '{c_key}')" id="btn-update-{c_key}" class="px-3 py-1.5 rounded-lg bg-amber-100 text-amber-800 hover:bg-amber-200 transition">🟡 Solo Actualizar ({cnt_upd})</button>
                        <button onclick="filterEtsItems('new', '{c_key}')" id="btn-new-{c_key}" class="px-3 py-1.5 rounded-lg bg-blue-100 text-blue-700 hover:bg-blue-200 transition">🔵 Solo Nuevos ({cnt_new})</button>
                        <button onclick="filterEtsItems('keep', '{c_key}')" id="btn-keep-{c_key}" class="px-3 py-1.5 rounded-lg bg-emerald-100 text-emerald-800 hover:bg-emerald-200 transition">🟢 Mantener ({cnt_keep})</button>
                    </div>
                </div>

                {legend_html}

                <!-- Cuadrícula Modular de Temarios (1 tarjeta por módulo) -->
                <div class="grid lg:grid-cols-2 gap-8 pt-4">
{''.join(new_module_cards)}
                </div>
            </div>
        </section>"""

        # Reemplazar la sección antigua por la nueva
        parsed_sec3 = BeautifulSoup(new_sec3_html, 'html.parser')
        sec3_tag.replace_with(parsed_sec3)
        print(f"[OK] Reemplazada exitosamente Sección 3 para {c_key}")

    # Actualizar la barra de navegación para respetar la regla estricta:
    # "lo que es mecanica industrial le nombramos Industrial y lo que es automotriz le nombramos mecánica."
    # Y vincular a los temporales mientras se revisa localmente
    nav = soup.find('nav')
    if nav:
        new_nav_html = """
            <nav class="flex items-center gap-2 sm:gap-3 text-xs overflow-x-auto no-scrollbar py-1">
                <a href="construccion.html" class="px-3.5 py-2 rounded-lg bg-white hover:bg-slate-50 border text-[#22376D] transition flex items-center gap-1.5 shadow-sm whitespace-nowrap border-slate-200 hover:border-[#22376D] font-bold">
                    <i data-lucide="hard-hat" class="w-4 h-4 text-[#EC9123]"></i> Construcción
                </a>
                <a href="electricidad.html" class="px-3.5 py-2 rounded-lg bg-white hover:bg-slate-50 border text-[#22376D] transition flex items-center gap-1.5 shadow-sm whitespace-nowrap border-slate-200 hover:border-[#22376D] font-bold">
                    <i data-lucide="zap" class="w-4 h-4 text-[#EC9123]"></i> Electricidad
                </a>
                <a href="mecanica_temporal.html" class="px-3.5 py-2 rounded-lg bg-white hover:bg-slate-50 border text-[#22376D] transition flex items-center gap-1.5 shadow-sm whitespace-nowrap border-slate-200 hover:border-[#22376D] font-bold">
                    <i data-lucide="wrench" class="w-4 h-4 text-[#EC9123]"></i> Industrial
                </a>
                <a href="automotriz_temporal.html" class="px-3.5 py-2 rounded-lg bg-white hover:bg-slate-50 border text-[#22376D] transition flex items-center gap-1.5 shadow-sm whitespace-nowrap ring-2 ring-[#EC9123] border-[#EC9123] font-black">
                    <i data-lucide="car" class="w-4 h-4 text-[#EC9123]"></i> Mecánica
                </a>
                <a href="index.html" class="px-3.5 py-2 rounded-lg bg-white hover:bg-slate-50 text-[#22376D] border border-slate-200 transition flex items-center justify-center gap-1.5 shadow-sm whitespace-nowrap font-bold">
                    <i data-lucide="home" class="w-4 h-4 text-[#EC9123]"></i>
                </a>
            </nav>"""
        parsed_nav = BeautifulSoup(new_nav_html, 'html.parser')
        nav.replace_with(parsed_nav)
        print("[OK] Barra de navegación actualizada con nomenclatura estricta ('Industrial' y 'Mecánica').")

    # Actualizar Título y Hero
    title_tag = soup.find('title')
    if title_tag:
        title_tag.string = "Área de Mecánica | Escuela Técnica Superior - Fundación Kinal"

    hero_h1 = soup.find('h1', class_=re.compile(r'font-kinal-title'))
    if hero_h1:
        hero_h1.string = "Área de Mecánica"
        print("[OK] Título Hero actualizado a 'Área de Mecánica'")

    # Guardar en archivo temporal
    result_html = str(soup)
    with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
        f.write(result_html)

    print(f"\n[ÉXITO] Archivo temporal generado: {OUTPUT_HTML} ({len(result_html)} bytes)")


if __name__ == '__main__':
    transform_automotriz()
