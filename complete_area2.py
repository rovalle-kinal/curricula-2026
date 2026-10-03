import openpyxl
from pathlib import Path

excel_dir = Path('/Users/arqovalle/Library/CloudStorage/OneDrive-Personal/Software/Antigravity/Cuentas Kinal/Programas de Curso')
output_dir = Path('Revision_Temarios')

def generate_ai():
    wb = openpyxl.load_workbook(excel_dir / '2026_AIM.xlsx', data_only=True)
    tm = wb['Temas Módulos']

    modules_data = []
    for c in range(1, tm.max_column + 1, 2):
        m_name = tm.cell(row=1, column=c).value
        m_num = tm.cell(row=2, column=c).value
        if m_name:
            topics = []
            for r in range(3, tm.max_row + 1):
                val = tm.cell(row=r, column=c).value
                if val and str(val).strip() and str(val).strip() != '.':
                    topics.append(str(val).strip())
            modules_data.append({
                'num': str(m_num).strip(),
                'name': str(m_name).strip(),
                'topics': topics
            })

    classified_modules = []
    for mod in modules_data:
        m_num = mod['num']
        m_name = mod['name']
        mod_topics = []
        for t in mod['topics']:
            status = 'keep'
            category = 'Automatización Industrial'
            badge = '🟢 Mantener'
            badge_color = 'bg-emerald-100 text-emerald-800'
            reason = 'Eje técnico imprescindible para el diseño, cableado e implementación de sistemas de control en la industria guatemalteca.'

            t_lower = t.lower()
            if 'arduino como daq' in t_lower:
                status = 'delete'
                badge = '🔴 Eliminar'
                badge_color = 'bg-red-100 text-red-800'
                category = 'Hardware No Industrial'
                reason = '🔴 Eliminar: El uso de placas Arduino para adquisición de datos (DAQ) no cumple con aislamiento ni inmunidad al ruido industrial. Debe sustituirse por tarjetas I/O analógicas de PLC y transmisores 4-20mA.'
            elif 'networking local' in t_lower and 'módulo 5' in m_num.lower() and len([x for x in mod_topics if 'networking local' in x['title'].lower()]) > 0:
                status = 'delete'
                badge = '🔴 Eliminar'
                badge_color = 'bg-red-100 text-red-800'
                category = 'Tema Duplicado'
                reason = '🔴 Eliminar: Tema duplicado textualmente en el Módulo 5 (aparece en posición 1 y posición 12 del temario oficial).'
            elif 'sistemas de control (lazo abierto/lazo cerrado)' in t_lower or 'instrumentación industrial' in t_lower:
                status = 'update'
                badge = '🟡 Actualizar'
                badge_color = 'bg-amber-100 text-amber-800'
                category = 'Control Continuo de Procesos'
                reason = '🟡 Actualizar: Incorporar control en lazo cerrado PID, transmisores de presión diferencial y calibración de campo con protocolo HART.'
            elif 'herramientas de programación y simulación' in t_lower or 'procedimiento de apertura proyecto plc' in t_lower:
                status = 'update'
                badge = '🟡 Actualizar'
                badge_color = 'bg-amber-100 text-amber-800'
                category = 'Plataformas de Control'
                reason = '🟡 Actualizar: Utilización intensiva de Siemens TIA Portal V18/V19 (S7-1200 / S7-1500) y Rockwell Studio 5000, estándar dominante en el sector productivo guatemalteco.'
            elif 'grafcet vs diagramas de petri' in t_lower or 'diagramación secuencial' in t_lower:
                status = 'update'
                badge = '🟡 Actualizar'
                badge_color = 'bg-amber-100 text-amber-800'
                category = 'Metodología Secuencial'
                reason = '🟡 Actualizar: Implementación en Diagramas Funcionales de Secuencia (SFC / S7-GRAPH) y máquinas de estados en Texto Estructurado (SCL) para depuración rápida de fallas.'
            elif 'logo!' in t_lower:
                status = 'update'
                badge = '🟡 Actualizar'
                badge_color = 'bg-amber-100 text-amber-800'
                category = 'Relés Inteligentes y Pasarelas'
                reason = '🟡 Actualizar: Enfoque del LOGO! 8 como relé concentrador periférico o pasarela IoT para monitoreo web ligero (LWE), sin desplazar las prácticas con PLC de gama media.'
            elif 'node-red' in t_lower:
                status = 'update'
                badge = '🟡 Actualizar'
                badge_color = 'bg-amber-100 text-amber-800'
                category = 'IIoT e Industria 4.0'
                reason = '🟡 Actualizar: Despliegue de dashboards industriales con Node-RED, integración de brokers MQTT industriales y servidores OPC-UA conectados a bases de datos relacionales.'

            mod_topics.append({
                'title': t,
                'status': status,
                'badge': badge,
                'badge_color': badge_color,
                'category': category,
                'reason': reason
            })

        if 'Instrumentación Industrial' in m_name:
            mod_topics.append({
                'title': '[NUEVO] Control PID en Procesos Continuos y Sintonización de Lazos de Presión/Nivel',
                'status': 'new',
                'badge': '🔵 Propuesta Nueva',
                'badge_color': 'bg-blue-100 text-blue-800',
                'category': 'Ingeniería de Procesos',
                'reason': '🔵 Propuesta Nueva: Sintonización de algoritmos PID (métodos Ziegler-Nichols y curvas de reacción) para control de nivel en calderas, hornos y tanques de mezcla.'
            })
        if 'Programación Secuencial de PLC' in m_name:
            mod_topics.append({
                'title': '[NUEVO] Redes Industriales PROFINET e Integración de Sensores Inteligentes IO-Link',
                'status': 'new',
                'badge': '🔵 Propuesta Nueva',
                'badge_color': 'bg-blue-100 text-blue-800',
                'category': 'Comunicaciones Industriales',
                'reason': '🔵 Propuesta Nueva: Topologías en anillo MRP, conectorización RJ45 industrial apantallada Cat 6A y parametrización de maestros y dispositivos IO-Link.'
            })
        if 'Redes Industriales e IIOT' in m_name:
            mod_topics.append({
                'title': '[NUEVO] Arquitecturas SCADA con Ignition / WinCC y Conectividad OPC UA / MQTT',
                'status': 'new',
                'badge': '🔵 Propuesta Nueva',
                'badge_color': 'bg-blue-100 text-blue-800',
                'category': 'Supervisión Centralizada y SCADA',
                'reason': '🔵 Propuesta Nueva: Desarrollo de sistemas de supervisión y control (SCADA) con pantallas de tendencias históricas, gestión de alarmas ISA-18.2 y enlace a bases de datos SQL.'
            })

        classified_modules.append({
            'num': m_num,
            'name': m_name,
            'topics': mod_topics
        })

    total_orig = sum(len(m['topics']) for m in modules_data)
    count_del = sum(sum(1 for t in m['topics'] if t['status'] == 'delete') for m in classified_modules)
    count_upd = sum(sum(1 for t in m['topics'] if t['status'] == 'update') for m in classified_modules)
    count_new = sum(sum(1 for t in m['topics'] if t['status'] == 'new') for m in classified_modules)
    count_keep = sum(sum(1 for t in m['topics'] if t['status'] == 'keep') for m in classified_modules)

    html = f'''<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Auditoría Curricular y Propuesta: Automatización Industrial | Kinal 2026</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@500;700&display=swap');
        body {{ font-family: 'Inter', sans-serif; background-color: #f8fafc; color: #0f172a; }}
        h1, h2, h3, h4, .font-heading {{ font-family: 'Space Grotesk', sans-serif; }}
        .item-delete {{ background-color: #fef2f2; border-left: 4px solid #ef4444; color: #991b1b; }}
        .item-update {{ background-color: #fefce8; border-left: 4px solid #eab308; color: #854d0e; }}
        .item-new {{ background-color: #eff6ff; border-left: 4px solid #3b82f6; color: #1e40af; }}
        .item-keep {{ background-color: #f0fdf4; border-left: 4px solid #22c55e; color: #166534; }}
        @media print {{
            .no-print {{ display: none !important; }}
            body {{ background-color: white !important; font-size: 11pt; }}
            .shadow-lg, .shadow-md, .shadow-xl {{ box-shadow: none !important; }}
            .break-inside-avoid {{ break-inside: avoid; }}
        }}
    </style>
</head>
<body class="antialiased text-slate-800">

    <header class="bg-slate-900 text-white border-b border-slate-800 sticky top-0 z-50 shadow-md">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3 flex flex-wrap justify-between items-center gap-4">
            <div class="flex items-center gap-3">
                <a href="index.html" title="Ir al Portal Maestro" class="bg-amber-600 hover:bg-amber-500 text-white font-bold text-xs uppercase px-2.5 py-1 rounded transition cursor-pointer">Kinal ETS 2026</a>
                <span class="text-slate-500 text-sm hidden sm:inline">|</span>
                <h1 class="text-base sm:text-lg font-semibold tracking-tight text-white flex items-center gap-2">
                    <i data-lucide="network" class="w-5 h-5 text-amber-400"></i>
                    Automatización Industrial
                </h1>
            </div>

            <div class="flex items-center gap-2 text-xs no-print">
                <a href="index.html" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition">Portal Maestro</a>
                <a href="Instalaciones_Electricas_Generales_Propuesta.html" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition">Inst. Eléctricas</a>
                <a href="Controles_y_Maquinas_Electricas_Propuesta.html" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition">Controles y Máquinas</a>
                <a href="Electronica_Analogica_Propuesta.html" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition">Electrónica Analógica</a>
                <a href="Control_Industrial_Sistemas_Programables_Propuesta.html" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition">Sist. Programables</a>
                <span class="px-2.5 py-1.5 rounded-lg bg-amber-600 text-white font-bold">AI</span>
                <button onclick="window.print()" class="inline-flex items-center gap-1 px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 transition">
                    <i data-lucide="printer" class="w-3.5 h-3.5"></i> Imprimir
                </button>
            </div>
        </div>
    </header>

    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-10">

        <div>
            <div class="flex items-center gap-2 text-xs font-medium text-slate-500 mb-2">
                <span>Programas de Curso</span>
                <i data-lucide="chevron-right" class="w-3.5 h-3.5"></i>
                <span>2026_AIM.xlsx</span>
                <i data-lucide="chevron-right" class="w-3.5 h-3.5"></i>
                <span class="text-amber-600 font-semibold">Auditoría Curricular & Propuesta 2026</span>
            </div>
            <h2 class="text-3xl font-extrabold text-slate-900 tracking-tight">
                Auditoría Curricular: Automatización Industrial (180 Horas)
            </h2>
            <p class="text-slate-600 mt-2 text-base max-w-4xl">
                Estandarización bajo normas internacionales de automatización (IEC 61131-3): Control de procesos en lazo cerrado PID, instrumentación inteligente con protocolo HART, redes de campo PROFINET e IO-Link, supervisión SCADA y conectividad industrial IoT con OPC UA y MQTT.
            </p>
        </div>

        <!-- Metric Badges Overview -->
        <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
            <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm flex items-center gap-4">
                <div class="w-12 h-12 rounded-lg bg-red-100 flex items-center justify-center text-red-600 font-bold text-xl">
                    <i data-lucide="trash-2" class="w-6 h-6"></i>
                </div>
                <div>
                    <div class="text-2xl font-bold text-slate-900">{count_del} Temas</div>
                    <div class="text-xs font-medium text-red-600 uppercase tracking-wider">A Eliminar (Arduino DAQ / Duplicados)</div>
                </div>
            </div>

            <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm flex items-center gap-4">
                <div class="w-12 h-12 rounded-lg bg-amber-100 flex items-center justify-center text-amber-600 font-bold text-xl">
                    <i data-lucide="refresh-cw" class="w-6 h-6"></i>
                </div>
                <div>
                    <div class="text-2xl font-bold text-slate-900">{count_upd} Temas</div>
                    <div class="text-xs font-medium text-amber-600 uppercase tracking-wider">A Actualizar (PID / TIA Portal / Node-RED)</div>
                </div>
            </div>

            <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm flex items-center gap-4">
                <div class="w-12 h-12 rounded-lg bg-blue-100 flex items-center justify-center text-blue-600 font-bold text-xl">
                    <i data-lucide="plus-circle" class="w-6 h-6"></i>
                </div>
                <div>
                    <div class="text-2xl font-bold text-slate-900">{count_new} Temas</div>
                    <div class="text-xs font-medium text-blue-600 uppercase tracking-wider">Nuevos Propuestos (PID / PROFINET / SCADA)</div>
                </div>
            </div>

            <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm flex items-center gap-4">
                <div class="w-12 h-12 rounded-lg bg-emerald-100 flex items-center justify-center text-emerald-600 font-bold text-xl">
                    <i data-lucide="check-circle-2" class="w-6 h-6"></i>
                </div>
                <div>
                    <div class="text-2xl font-bold text-slate-900">{count_keep} Temas</div>
                    <div class="text-xs font-medium text-emerald-600 uppercase tracking-wider">Fundamentos Conservados</div>
                </div>
            </div>
        </div>

        <!-- SECCIÓN 1: Contexto Industrial y Demanda Laboral en Guatemala -->
        <section class="bg-white rounded-2xl border border-slate-200 p-6 sm:p-8 shadow-sm space-y-6">
            <div class="border-b border-slate-100 pb-4">
                <span class="text-xs font-bold uppercase tracking-wider text-amber-600 bg-amber-50 px-2.5 py-1 rounded-full border border-amber-200">Sección 1</span>
                <h3 class="text-xl font-bold text-slate-900 mt-2 flex items-center gap-2">
                    <i data-lucide="trending-up" class="w-5 h-5 text-amber-600"></i>
                    Contexto Industrial y Demanda Laboral en Guatemala (2026)
                </h3>
                <p class="text-slate-600 text-sm mt-1">
                    Panorama operativo en los principales ingenios azucareros de la Costa Sur, plantas cerveceras, cementeras y farmacéuticas de Guatemala que demandan técnicos en automatización con perfil 4.0.
                </p>
            </div>

            <div class="grid md:grid-cols-3 gap-6 text-sm">
                <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 space-y-3">
                    <div class="font-bold text-slate-900 flex items-center gap-2 text-base">
                        <i data-lucide="sliders" class="w-5 h-5 text-amber-600"></i>
                        Control PID de Procesos Continuos
                    </div>
                    <p class="text-slate-600 text-xs leading-relaxed">
                        En la industria de transformación y procesos continuos (alimentos, bebidas, molienda de cemento), el control ON/OFF no es viable. Se exige la sintonización precisa de lazos PID con válvulas modulantes, posicionadores neumáticos inteligentes y transmisores de flujo y temperatura con protocolo HART.
                    </p>
                </div>

                <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 space-y-3">
                    <div class="font-bold text-slate-900 flex items-center gap-2 text-base">
                        <i data-lucide="network" class="w-5 h-5 text-blue-600"></i>
                        Redes de Campo PROFINET e IO-Link
                    </div>
                    <p class="text-slate-600 text-xs leading-relaxed">
                        El cableado discreto punto a punto hilo por hilo ha sido reemplazado masivamente por redes Ethernet Industrial en tiempo real (PROFINET) y tecnología IO-Link. El egresado debe saber configurar switches industriales administrables, diagnosticar pérdidas de paquetes y parametrizar sensores ópticos inteligentes a través de la red.
                    </p>
                </div>

                <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 space-y-3">
                    <div class="font-bold text-slate-900 flex items-center gap-2 text-base">
                        <i data-lucide="database" class="w-5 h-5 text-emerald-600"></i>
                        Convergencia IT / OT y SCADA Industrial
                    </div>
                    <p class="text-slate-600 text-xs leading-relaxed">
                        Las empresas demandan supervisión de planta en tiempo real mediante sistemas SCADA (Ignition, WinCC) que no sólo muestren gráficos, sino que registren el tiempo medio entre fallas (MTBF), consumo energético por tonelada y alimenten sistemas ERP corporativos mediante protocolos abiertos OPC-UA y MQTT.
                    </p>
                </div>
            </div>
        </section>

        <!-- SECCIÓN 2: Ficha Oficial de Venta y Diagnóstico Crítico -->
        <section class="bg-white rounded-2xl border border-slate-200 p-6 sm:p-8 shadow-sm space-y-6">
            <div class="border-b border-slate-100 pb-4">
                <span class="text-xs font-bold uppercase tracking-wider text-amber-600 bg-amber-50 px-2.5 py-1 rounded-full border border-amber-200">Sección 2</span>
                <h3 class="text-xl font-bold text-slate-900 mt-2 flex items-center gap-2">
                    <i data-lucide="file-spreadsheet" class="w-5 h-5 text-amber-600"></i>
                    Ficha Oficial de Venta ("Reporte") y Diagnóstico Crítico de Anomalías
                </h3>
            </div>

            <div class="grid md:grid-cols-2 gap-4 text-xs sm:text-sm text-slate-700 bg-slate-50 p-4 rounded-xl border border-slate-200">
                <div><strong>Programa Académico:</strong> Automatización Industrial (2026_AIM.xlsx)</div>
                <div><strong>Duración Total:</strong> 180 Horas cronológicas distribuidas en 6 Módulos de 30 hrs</div>
                <div><strong>Jornadas:</strong> Matutina y Vespertina (Sábados de 8:00 a 12:30 y 13:00 a 17:30 hrs)</div>
                <div><strong>Acreditación:</strong> Diploma de Técnico en Automatización Industrial</div>
                <div class="md:col-span-2"><strong>Perfil de Ingreso:</strong> Bachillerato diversificado (preferible técnico o en computación), conocimientos de electricidad y electrónica, y competencias digitales.</div>
                <div class="md:col-span-2"><strong>Perfil de Egreso:</strong> Automatizar sistemas de control y procesos industriales, aplicando normas técnicas, programando software especializado e implementando redes de comunicación.</div>
            </div>

            <div class="bg-amber-50 border border-amber-300 rounded-xl p-5 space-y-3">
                <h4 class="text-amber-900 font-bold text-sm flex items-center gap-2">
                    <i data-lucide="alert-triangle" class="w-5 h-5 text-amber-600"></i>
                    Diagnóstico Crítico / Anomalías Detectadas en el Programa Original
                </h4>
                <ul class="text-xs text-amber-950 space-y-2 list-disc list-inside leading-relaxed">
                    <li><strong>Incongruencia Técnica en Adquisición de Datos:</strong> El Módulo 2 incluye <em>"Integración de instrumentos a ARDUINO como DAQ"</em>. En un curso superior de automatización industrial, el DAQ debe ejecutarse con módulos I/O analógicos de PLC de 16 bits y acondicionamiento industrial, nunca con tarjetas no industriales expuestas a ruido electromagnético.</li>
                    <li><strong>Tema Duplicado en Módulo 5:</strong> El tema <em>"Networking local"</em> se repite de forma redundante en las posiciones 1 y 12 del Módulo 5 por error en la captura del Excel original.</li>
                    <li><strong>Sobreénfasis en Relés Programables:</strong> El Módulo 5 dedica 30 horas completas al relé inteligente LOGO! 8, cuando un técnico en automatización de nivel 2026 requiere concentrar la carga horaria en controladores modulares avanzados como Siemens S7-1200 / S7-1500 y Allen Bradley CompactLogix.</li>
                </ul>
            </div>
        </section>

        <!-- SECCIÓN 3: Distribución Modular Detallada y Auditoría Tema por Tema -->
        <section class="bg-white rounded-2xl border border-slate-200 p-6 sm:p-8 shadow-sm space-y-6">
            <div class="flex flex-wrap justify-between items-center gap-4 border-b border-slate-100 pb-4">
                <div>
                    <span class="text-xs font-bold uppercase tracking-wider text-amber-600 bg-amber-50 px-2.5 py-1 rounded-full border border-amber-200">Sección 3</span>
                    <h3 class="text-xl font-bold text-slate-900 mt-2 flex items-center gap-2">
                        <i data-lucide="list-checks" class="w-5 h-5 text-amber-600"></i>
                        Distribución Modular y Auditoría Analítica Tema por Tema
                    </h3>
                    <p class="text-slate-600 text-sm mt-1">
                        Total de temas auditados en el pensum original: <strong>{total_orig} temas</strong> desglosados en sus 6 módulos oficiales.
                    </p>
                </div>

                <!-- Filtros Interactivos -->
                <div class="flex flex-wrap items-center gap-1.5 text-xs no-print">
                    <button onclick="filterItems('all')" id="btn-all" class="px-3 py-1.5 rounded-lg bg-slate-900 text-white font-medium hover:bg-slate-800 transition">Todos ({total_orig + count_new})</button>
                    <button onclick="filterItems('delete')" id="btn-delete" class="px-3 py-1.5 rounded-lg bg-red-100 text-red-800 font-medium hover:bg-red-200 transition">🔴 Eliminar ({count_del})</button>
                    <button onclick="filterItems('update')" id="btn-update" class="px-3 py-1.5 rounded-lg bg-amber-100 text-amber-800 font-medium hover:bg-amber-200 transition">🟡 Actualizar ({count_upd})</button>
                    <button onclick="filterItems('new')" id="btn-new" class="px-3 py-1.5 rounded-lg bg-blue-100 text-blue-800 font-medium hover:bg-blue-200 transition">🔵 Nuevos ({count_new})</button>
                    <button onclick="filterItems('keep')" id="btn-keep" class="px-3 py-1.5 rounded-lg bg-emerald-100 text-emerald-800 font-medium hover:bg-emerald-200 transition">🟢 Mantener ({count_keep})</button>
                </div>
            </div>

            <!-- Listado de Módulos y Temas -->
            <div class="space-y-8">
'''

    for mod in classified_modules:
        m_num = mod['num']
        m_name = mod['name']
        topics = mod['topics']
        html += f'''
                <div class="border border-slate-200 rounded-xl p-5 bg-slate-50/50 space-y-4">
                    <div class="flex items-center justify-between border-b border-slate-200 pb-3">
                        <div class="flex items-center gap-2">
                            <span class="w-7 h-7 rounded-lg bg-amber-600 text-white font-bold text-xs flex items-center justify-center">{m_num.replace('Módulo ', '') if 'Módulo' in m_num else m_num}</span>
                            <h4 class="font-bold text-slate-900 text-base">{m_name}</h4>
                        </div>
                        <span class="text-xs text-slate-500 font-medium">{len(topics)} temas analizados</span>
                    </div>

                    <div class="grid md:grid-cols-2 gap-3">
'''
        for t in topics:
            status_class = f"item-{t['status']}"
            html += f'''
                        <div class="content-item {status_class} p-3.5 rounded-lg text-xs space-y-1.5" data-status="{t['status']}">
                            <div class="flex justify-between items-start gap-2">
                                <span class="font-bold text-slate-900">{t['title']}</span>
                                <span class="px-2 py-0.5 rounded text-[10px] font-extrabold uppercase whitespace-nowrap {t['badge_color']}">{t['badge']}</span>
                            </div>
                            <div class="text-[11px] font-medium text-slate-500 uppercase tracking-wider">{t['category']}</div>
                            <p class="text-slate-700 leading-relaxed">{t['reason']}</p>
                        </div>
'''
        html += '''
                    </div>
                </div>
'''

    html += f'''
            </div>
        </section>

        <!-- SECCIÓN 4: Matriz Comparativa -->
        <section class="bg-white rounded-2xl border border-slate-200 p-6 sm:p-8 shadow-sm space-y-6">
            <div class="border-b border-slate-100 pb-4">
                <span class="text-xs font-bold uppercase tracking-wider text-amber-600 bg-amber-50 px-2.5 py-1 rounded-full border border-amber-200">Sección 4</span>
                <h3 class="text-xl font-bold text-slate-900 mt-2 flex items-center gap-2">
                    <i data-lucide="arrow-left-right" class="w-5 h-5 text-amber-600"></i>
                    Matriz Comparativa: Pensum Tradicional vs. Pensum Modernizado 2026
                </h3>
            </div>

            <div class="overflow-x-auto">
                <table class="w-full text-xs text-left border-collapse border border-slate-200 rounded-lg">
                    <thead class="bg-slate-100 text-slate-700 font-bold uppercase text-[11px]">
                        <tr>
                            <th class="p-3 border border-slate-200">Eje Temático</th>
                            <th class="p-3 border border-slate-200 text-red-800 bg-red-50/50">Enfoque Anterior (Obsolescencia / Brechas)</th>
                            <th class="p-3 border border-slate-200 text-emerald-800 bg-emerald-50/50">Enfoque Modernizado 2026 (Estándar Kinal ETS)</th>
                        </tr>
                    </thead>
                    <tbody class="divide-y divide-slate-200">
                        <tr>
                            <td class="p-3 font-bold text-slate-900 border border-slate-200">Control de Procesos</td>
                            <td class="p-3 text-slate-600 border border-slate-200">Enfoque centrado en control digital combinacional y secuencial ON/OFF de actuadores.</td>
                            <td class="p-3 text-slate-800 border border-slate-200 font-medium">Lazos de control cerrados PID con sintonización en tiempo real y válvulas proporcionales para flujo, presión y temperatura.</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-bold text-slate-900 border border-slate-200">Instrumentación de Campo</td>
                            <td class="p-3 text-slate-600 border border-slate-200">Uso experimental de tarjetas Arduino como sistema DAQ no apto para plantas.</td>
                            <td class="p-3 text-slate-800 border border-slate-200 font-medium">Módulos analógicos calibrados de PLC, transmisores industriales con protocolo digital HART y sensores IO-Link.</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-bold text-slate-900 border border-slate-200">Comunicaciones y Buses</td>
                            <td class="p-3 text-slate-600 border border-slate-200">Cableado discreto y redes locales simples sin tratamiento de redundancia industrial.</td>
                            <td class="p-3 text-slate-800 border border-slate-200 font-medium">Redes PROFINET con switches industriales administrables, topologías en anillo redundante (MRP) y conectores blindados M12/RJ45.</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-bold text-slate-900 border border-slate-200">Supervisión y SCADA</td>
                            <td class="p-3 text-slate-600 border border-slate-200">Visualización básica limitada a páginas web locales sencillas de relés inteligentes.</td>
                            <td class="p-3 text-slate-800 border border-slate-200 font-medium">Sistemas SCADA industriales con pantallas de tendencias históricas, gestión de alarmas según norma ISA-18.2 y servidores OPC UA.</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-bold text-slate-900 border border-slate-200">Internet de las Cosas (IIoT)</td>
                            <td class="p-3 text-slate-600 border border-slate-200">Introducción básica a Node-RED en entorno local de Windows.</td>
                            <td class="p-3 text-slate-800 border border-slate-200 font-medium">Integración integral IIoT: telemetría remota mediante brokers MQTT industriales, bases de datos SQL y nociones de ciberseguridad OT (IEC 62443).</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </section>

        <!-- SECCIÓN 5: Innovación Tecnológica: Inteligencia Artificial Aplicada -->
        <section class="bg-gradient-to-r from-amber-900 via-slate-900 to-indigo-950 text-white rounded-2xl p-6 sm:p-8 shadow-xl space-y-6">
            <div class="flex items-center gap-3 border-b border-white/10 pb-4">
                <div class="p-2.5 rounded-lg bg-amber-500/20 text-amber-300">
                    <i data-lucide="bot" class="w-6 h-6"></i>
                </div>
                <div>
                    <span class="bg-amber-500/30 text-amber-200 text-xs px-2.5 py-0.5 rounded-full font-bold uppercase tracking-wider border border-amber-400/30">Módulo Adicional / Opcional</span>
                    <h3 class="text-xl font-bold text-white">Innovación Tecnológica: Inteligencia Artificial en Automatización Industrial</h3>
                </div>
            </div>

            <div class="grid md:grid-cols-3 gap-6">
                <div class="bg-white/10 backdrop-blur rounded-xl p-5 border border-white/10 space-y-3">
                    <div class="text-amber-300 font-bold text-sm flex items-center gap-2">
                        <i data-lucide="sliders" class="w-4 h-4"></i>
                        Sintonización Adaptativa de Lazos PID con Algoritmos de Machine Learning
                    </div>
                    <p class="text-xs text-slate-200 leading-relaxed">
                        Controladores inteligentes que ajustan automáticamente las ganancias proporcional, integral y derivativa en procesos no lineales (como hornos o calderas), compensando perturbaciones externas sin requerir intervención manual constante.
                    </p>
                    <div class="pt-2 border-t border-white/10 text-[11px] text-amber-200 font-mono">
                        Herramienta: MATLAB AI Control Toolbox / Rockwell FactoryTalk AI.
                    </div>
                </div>

                <div class="bg-white/10 backdrop-blur rounded-xl p-5 border border-white/10 space-y-3">
                    <div class="text-amber-300 font-bold text-sm flex items-center gap-2">
                        <i data-lucide="camera" class="w-4 h-4"></i>
                        Visión Artificial Industrial para Control de Calidad en Banda Transportadora
                    </div>
                    <p class="text-xs text-slate-200 leading-relaxed">
                        Cámaras conectadas al PLC que procesan imágenes con redes neuronales convolucionales para inspeccionar botellas sin etiqueta, códigos de barra ilegibles o piezas defectuosas a velocidades superiores a 1,000 unidades por minuto.
                    </p>
                    <div class="pt-2 border-t border-white/10 text-[11px] text-amber-200 font-mono">
                        Herramienta: Cognex In-Sight ViDi AI / Omron Microscan AI.
                    </div>
                </div>

                <div class="bg-white/10 backdrop-blur rounded-xl p-5 border border-white/10 space-y-3">
                    <div class="text-amber-300 font-bold text-sm flex items-center gap-2">
                        <i data-lucide="network" class="w-4 h-4"></i>
                        Diagnóstico Inteligente de Tráfico en Redes PROFINET y Prevención de Paradas
                    </div>
                    <p class="text-xs text-slate-200 leading-relaxed">
                        Analizadores de red asistidos por IA que monitorean la fluctuación (jitter), errores CRC y congestión de paquetes en la red Ethernet de planta, anticipando cortes de comunicación antes de que detengan la línea de producción.
                    </p>
                    <div class="pt-2 border-t border-white/10 text-[11px] text-amber-200 font-mono">
                        Herramienta: Indu-Sol PROmesh AI / Siemens Sinec NMS AI.
                    </div>
                </div>
            </div>
        </section>

    </main>

    <footer class="bg-white border-t border-slate-200 mt-12 py-6 text-center text-xs text-slate-500">
        Fundación Kinal • Escuela Técnica Superior • Dirección Académica • Propuesta Curricular Automatización Industrial 2026
    </footer>

    <script>
        lucide.createIcons();

        function filterItems(status) {{
            const items = document.querySelectorAll('.content-item');
            const buttons = ['all', 'delete', 'update', 'new', 'keep'];

            buttons.forEach(btn => {{
                const buttonElement = document.getElementById('btn-' + btn);
                if (buttonElement) {{
                    if (btn === status) {{
                        buttonElement.classList.add('ring-2', 'ring-offset-2', 'ring-slate-900');
                    }} else {{
                        buttonElement.classList.remove('ring-2', 'ring-offset-2', 'ring-slate-900');
                    }}
                }}
            }});

            items.forEach(item => {{
                if (status === 'all') {{
                    item.style.display = 'block';
                }} else {{
                    if (item.getAttribute('data-status') === status) {{
                        item.style.display = 'block';
                    }} else {{
                        item.style.display = 'none';
                    }}
                }}
            }});
        }}
    </script>
</body>
</html>
'''
    (output_dir / 'Automatizacion_Industrial_Propuesta.html').write_text(html, encoding='utf-8')
    print('Generated Automatizacion_Industrial_Propuesta.html')

generate_ai()
