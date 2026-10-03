import openpyxl
from pathlib import Path

excel_dir = Path('/Users/arqovalle/Library/CloudStorage/OneDrive-Personal/Software/Antigravity/Cuentas Kinal/Programas de Curso')
output_dir = Path('Revision_Temarios')

# -------------------------------------------------------------
# 3. ELECTROMECÁNICA AUTOMOTRIZ (2025_EMAM.xlsx)
# -------------------------------------------------------------
def generate_ema():
    wb = openpyxl.load_workbook(excel_dir / '2025_EMAM.xlsx', data_only=True)
    tm = wb['Temas Módulos']

    modules_data = []
    for c in range(1, tm.max_column + 1, 2):
        m_name = tm.cell(row=1, column=c).value
        m_num = tm.cell(row=2, column=c).value
        if m_name and str(m_name).strip() not in ['0', '#REF!']:
            topics = []
            for r in range(3, tm.max_row + 1):
                val = tm.cell(row=r, column=c).value
                if val and str(val).strip() and str(val).strip() not in ['0', '.']:
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
            category = 'Electromecánica Automotriz'
            badge = '🟢 Mantener'
            badge_color = 'bg-emerald-100 text-emerald-800'
            reason = 'Fundamento eléctrico y de cableado esencial para el diagnóstico y reparación de circuitos del automóvil.'

            t_lower = t.lower()
            if 'encendido de platinos' in t_lower:
                status = 'delete'
                badge = '🔴 Eliminar'
                badge_color = 'bg-red-100 text-red-800'
                category = 'Tecnología de Platinos Obsoleta'
                reason = '🔴 Eliminar: Los sistemas de encendido mecánico con platinos y condensador están descontinuados hace décadas en Guatemala; enfocar en bobinas transistorizadas COP (Coil-On-Plug).'
            elif 'el multímetro' in t_lower or 'componentes del multímetro' in t_lower:
                status = 'update'
                badge = '🟡 Actualizar'
                badge_color = 'bg-amber-100 text-amber-800'
                category = 'Instrumentación Digital'
                reason = '🟡 Actualizar: Mediciones de caída de tensión en miliVoltios bajo carga real, impedancia de entrada (> 10 MΩ para protección de ECUs) y pinzas amperimétricas DC.'
            elif 'la batería' in t_lower or 'baterías de plomo' in t_lower:
                status = 'update'
                badge = '🟡 Actualizar'
                badge_color = 'bg-amber-100 text-amber-800'
                category = 'Acumuladores Modernos'
                reason = '🟡 Actualizar: Diagnóstico con probadores de conductancia digital (Midtronics), baterías AGM/EFB para vehículos Start-Stop y control de estado de salud (SOH).'
            elif 'el motor de arranque' in t_lower or 'circuito eléctrico del motor de arranque' in t_lower:
                if 'módulo 6' in m_num.lower():
                    status = 'update'
                    badge = '🟡 Actualizar'
                    badge_color = 'bg-amber-100 text-amber-800'
                    category = 'Sistema de Carga Corregido'
                    reason = '🟡 Actualizar (Error del Excel Corregido): Este módulo se titulaba "Sistema de Carga" pero copió erróneamente los temas de arranque. Se debe instruir sobre el alternador, puente de diodos y regulador LIN/PWM.'
                else:
                    status = 'update'
                    badge = '🟡 Actualizar'
                    badge_color = 'bg-amber-100 text-amber-800'
                    category = 'Circuito de Arranque'
                    reason = '🟡 Actualizar: Pruebas de caída de tensión en línea positiva y de masa (< 0.5V), prueba de corriente pico con osciloscopio y solenoides integrados.'
            elif 'sistema de iluminación' in t_lower:
                status = 'update'
                badge = '🟡 Actualizar'
                badge_color = 'bg-amber-100 text-amber-800'
                category = 'Iluminación Inteligente'
                reason = '🟡 Actualizar: Faros LED de alta potencia, luces diurnas DRL, circuitos modulados por ancho de pulso (PWM) y control computarizado por módulo de carrocería (BCM).'
            elif 'encendido electrónico' in t_lower or 'la bobina' in t_lower:
                status = 'update'
                badge = '🟡 Actualizar'
                badge_color = 'bg-amber-100 text-amber-800'
                category = 'Encendido Estático'
                reason = '🟡 Actualizar: Bobinas independientes COP individuales por cilindro, módulos DIS, control de tiempo de saturación (Dwell) por la ECU y diagnóstico con osciloscopio.'

            mod_topics.append({
                'title': t,
                'status': status,
                'badge': badge,
                'badge_color': badge_color,
                'category': category,
                'reason': reason
            })

        if 'Sistema de Carga' in m_name:
            mod_topics.append({
                'title': '[NUEVO] Alternadores Inteligentes con Control LIN / PWM y Sensor de Batería IBS',
                'status': 'new',
                'badge': '🔵 Propuesta Nueva',
                'badge_color': 'bg-blue-100 text-blue-800',
                'category': 'Gestión Inteligente de Carga',
                'reason': '🔵 Propuesta Nueva: Comunicación digital del alternador con la ECU para regular el voltaje según la aceleración y carga regenerativa, y registro de batería nueva con escáner.'
            })
        if 'Interpretación de un Diagrama' in m_name:
            mod_topics.append({
                'title': '[NUEVO] Diagnóstico de Redes de Comunicación Multiplexadas CAN-Bus y LIN-Bus',
                'status': 'new',
                'badge': '🔵 Propuesta Nueva',
                'badge_color': 'bg-blue-100 text-blue-800',
                'category': 'Comunicaciones Multiplexadas',
                'reason': '🔵 Propuesta Nueva: Medición de voltajes diferenciales en pines 6 y 14 del conector OBDII con osciloscopio, comprobación de resistencias de 120 Ω y aislamiento de módulos en corto.'
            })
        if 'Batería o Acumuladores' in m_name:
            mod_topics.append({
                'title': '[NUEVO] Seguridad y Protocolos de Desenergización en Alta Tensión para Vehículos Híbridos (HEV)',
                'status': 'new',
                'badge': '🔵 Propuesta Nueva',
                'badge_color': 'bg-blue-100 text-blue-800',
                'category': 'Seguridad en Vehículos Híbridos',
                'reason': '🔵 Propuesta Nueva: Uso obligatorio de guantes dieléctricos Clase 0 (1,000 V), extracción del Service Plug de la batería híbrida y verificación de ausencia de tensión en el inversor.'
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
    <title>Auditoría Curricular y Propuesta: Electromecánica Automotriz | Kinal 2026</title>
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
                <a href="index.html" title="Ir al Portal Maestro" class="bg-red-600 hover:bg-red-500 text-white font-bold text-xs uppercase px-2.5 py-1 rounded transition cursor-pointer">Kinal ETS 2026</a>
                <span class="text-slate-500 text-sm hidden sm:inline">|</span>
                <h1 class="text-base sm:text-lg font-semibold tracking-tight text-white flex items-center gap-2">
                    <i data-lucide="zap" class="w-5 h-5 text-red-400"></i>
                    Electromecánica Automotriz
                </h1>
            </div>

            <div class="flex items-center gap-2 text-xs no-print">
                <a href="index.html" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition">Portal Maestro</a>
                <a href="Mecanica_Motores_Gasolina_Propuesta.html" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition">Motores</a>
                <a href="Mecanismos_del_Automovil_Propuesta.html" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition">Mecanismos</a>
                <span class="px-2.5 py-1.5 rounded-lg bg-red-600 text-white font-bold">EMA</span>
                <a href="Inyeccion_Electronica_Automotriz_Propuesta.html" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition">Inyección</a>
                <a href="Aire_Acondicionado_Automotriz_Propuesta.html" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition">Aire Acond.</a>
                <a href="Mecanica_de_Motocicletas_Propuesta.html" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition">Motos</a>
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
                <span>2025_EMAM.xlsx</span>
                <i data-lucide="chevron-right" class="w-3.5 h-3.5"></i>
                <span class="text-red-600 font-semibold">Auditoría Curricular & Propuesta 2026</span>
            </div>
            <h2 class="text-3xl font-extrabold text-slate-900 tracking-tight">
                Auditoría Curricular: Electromecánica Automotriz (180 Horas)
            </h2>
            <p class="text-slate-600 mt-2 text-base max-w-4xl">
                Modernización del diagnóstico eléctrico automotriz: Corrección estructural del sistema de carga, diagnóstico de redes multiplexadas <strong>CAN-Bus y LIN-Bus</strong> con osciloscopio, alternadores inteligentes controlados por ECU, baterías AGM/EFB para sistemas Start-Stop y <strong>Protocolos de Desenergización en Alta Tensión</strong> para vehículos híbridos (HEV).
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
                    <div class="text-xs font-medium text-red-600 uppercase tracking-wider">A Eliminar (Platinos Mecánicos)</div>
                </div>
            </div>

            <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm flex items-center gap-4">
                <div class="w-12 h-12 rounded-lg bg-amber-100 flex items-center justify-center text-amber-600 font-bold text-xl">
                    <i data-lucide="refresh-cw" class="w-6 h-6"></i>
                </div>
                <div>
                    <div class="text-2xl font-bold text-slate-900">{count_upd} Temas</div>
                    <div class="text-xs font-medium text-amber-600 uppercase tracking-wider">A Actualizar (Alternadores / AGM / Faros LED)</div>
                </div>
            </div>

            <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm flex items-center gap-4">
                <div class="w-12 h-12 rounded-lg bg-blue-100 flex items-center justify-center text-blue-600 font-bold text-xl">
                    <i data-lucide="plus-circle" class="w-6 h-6"></i>
                </div>
                <div>
                    <div class="text-2xl font-bold text-slate-900">{count_new} Temas</div>
                    <div class="text-xs font-medium text-blue-600 uppercase tracking-wider">Nuevos Propuestos (CAN-Bus / LIN / Híbridos)</div>
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
                <span class="text-xs font-bold uppercase tracking-wider text-red-600 bg-red-50 px-2.5 py-1 rounded-full border border-red-200">Sección 1</span>
                <h3 class="text-xl font-bold text-slate-900 mt-2 flex items-center gap-2">
                    <i data-lucide="trending-up" class="w-5 h-5 text-red-600"></i>
                    Contexto Industrial y Demanda Laboral en Guatemala (2026)
                </h3>
                <p class="text-slate-600 text-sm mt-1">
                    Transformación tecnológica del taller eléctrico automotriz frente a la arquitectura electrónica digital y la movilidad híbrida en Guatemala.
                </p>
            </div>

            <div class="grid md:grid-cols-3 gap-6 text-sm">
                <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 space-y-3">
                    <div class="font-bold text-slate-900 flex items-center gap-2 text-base">
                        <i data-lucide="network" class="w-5 h-5 text-red-600"></i>
                        Redes de Comunicación CAN-Bus y LIN-Bus
                    </div>
                    <p class="text-slate-600 text-xs leading-relaxed">
                        En los automóviles modernos, un foco que no enciende o un vidrio eléctrico inoperativo no se debe a un fusible quemado, sino a un fallo de comunicación en el bus de datos LIN o CAN. El técnico debe ser capaz de conectar el osciloscopio en el conector DLC y analizar voltajes espejo (CAN-H 2.5 a 3.5V, CAN-L 2.5 a 1.5V).
                    </p>
                </div>

                <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 space-y-3">
                    <div class="font-bold text-slate-900 flex items-center gap-2 text-base">
                        <i data-lucide="battery-charging" class="w-5 h-5 text-amber-600"></i>
                        Alternadores Inteligentes y Baterías Start-Stop
                    </div>
                    <p class="text-slate-600 text-xs leading-relaxed">
                        Los alternadores ya no cargan a un voltaje fijo de 14.2V; son gobernados por modulación PWM o bus LIN desde la ECU para desacoplar carga durante aceleraciones y recuperar energía en desaceleración. Instalar una batería convencional en un auto con sensor IBS sin reprogramar la ECU la destruye en pocos meses.
                    </p>
                </div>

                <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 space-y-3">
                    <div class="font-bold text-slate-900 flex items-center gap-2 text-base">
                        <i data-lucide="zap-off" class="w-5 h-5 text-emerald-600"></i>
                        Seguridad de Alta Tensión en Híbridos (HEV)
                    </div>
                    <p class="text-slate-600 text-xs leading-relaxed">
                        Con miles de híbridos rodando en Guatemala (Toyota Prius, Aqua, Camry, Hyundai Ioniq), un electromecánico que toque el cableado naranja de 200 a 650 VDC sin guantes dieléctricos Clase 0 y sin extraer el Service Plug de seguridad corre peligro mortal de electrocución por arco voltaico continuo.
                    </p>
                </div>
            </div>
        </section>

        <!-- SECCIÓN 2: Ficha Oficial de Venta y Diagnóstico Crítico -->
        <section class="bg-white rounded-2xl border border-slate-200 p-6 sm:p-8 shadow-sm space-y-6">
            <div class="border-b border-slate-100 pb-4">
                <span class="text-xs font-bold uppercase tracking-wider text-red-600 bg-red-50 px-2.5 py-1 rounded-full border border-red-200">Sección 2</span>
                <h3 class="text-xl font-bold text-slate-900 mt-2 flex items-center gap-2">
                    <i data-lucide="file-spreadsheet" class="w-5 h-5 text-red-600"></i>
                    Ficha Oficial de Venta ("Reporte") y Diagnóstico Crítico de Anomalías
                </h3>
            </div>

            <div class="grid md:grid-cols-2 gap-4 text-xs sm:text-sm text-slate-700 bg-slate-50 p-4 rounded-xl border border-slate-200">
                <div><strong>Programa Académico:</strong> Electromecánica Automotriz (2025_EMAM.xlsx)</div>
                <div><strong>Duración Total:</strong> 180 Horas distribuidas en 10 Módulos cronológicos</div>
                <div><strong>Jornadas:</strong> Matutina y Vespertina (Sábados de 8:00 a 12:30 y 13:00 a 17:30 hrs)</div>
                <div><strong>Acreditación:</strong> Diploma Técnico en Electromecánica Automotriz</div>
                <div class="md:col-span-2"><strong>Perfil de Ingreso:</strong> Tercer grado de educación básica, razonamiento lógico-deductivo e interés por la electricidad automotriz.</div>
                <div class="md:col-span-2"><strong>Perfil de Egreso:</strong> Competencia para diagnosticar y reparar sistemas de arranque, carga, iluminación, accesorios de confort y encendido electrónico en vehículos automotores.</div>
            </div>

            <div class="bg-amber-50 border border-amber-300 rounded-xl p-5 space-y-3">
                <h4 class="text-amber-900 font-bold text-sm flex items-center gap-2">
                    <i data-lucide="alert-triangle" class="w-5 h-5 text-amber-600"></i>
                    Diagnóstico Crítico / Anomalía Monumental Detectada en el Archivo Fuente (2025_EMAM.xlsx)
                </h4>
                <ul class="text-xs text-amber-950 space-y-2 list-disc list-inside leading-relaxed">
                    <li><strong>Módulo 6 Copiado Textualmente del Módulo 5 (Error Grave de Captura):</strong> En el Excel oficial, la columna del <em>Módulo 6 (Sistema de Carga)</em> contiene exactamente los mismos temas del <em>Módulo 5 (Sistema de Arranque)</em>: lista <em>"El motor de arranque"</em>, <em>"Relé de arranque o solenoide"</em>, etc. Los temas reales del alternador, puente de diodos y reguladores de voltaje fueron omitidos por un error de copia. Esta propuesta 2026 corrige integralmente dicha falla curricular.</li>
                    <li><strong>Contenido Obsoleto de Platinos:</strong> En el Módulo 10 se mantiene <em>"Encendido de platinos con ayuda electrónica"</em>, tecnología abandonada hace décadas.</li>
                    <li><strong>Ausencia de Redes Multiplexadas y Seguridad Híbrida:</strong> El temario no contemplaba las redes de comunicación CAN/LIN (que gestionan todo el cableado moderno del automóvil) ni los protocolos de seguridad vitales para desconectar baterías de alta tensión en vehículos híbridos.</li>
                </ul>
            </div>
        </section>

        <!-- SECCIÓN 3: Distribución Modular Detallada y Auditoría Tema por Tema -->
        <section class="bg-white rounded-2xl border border-slate-200 p-6 sm:p-8 shadow-sm space-y-6">
            <div class="flex flex-wrap justify-between items-center gap-4 border-b border-slate-100 pb-4">
                <div>
                    <span class="text-xs font-bold uppercase tracking-wider text-red-600 bg-red-50 px-2.5 py-1 rounded-full border border-red-200">Sección 3</span>
                    <h3 class="text-xl font-bold text-slate-900 mt-2 flex items-center gap-2">
                        <i data-lucide="list-checks" class="w-5 h-5 text-red-600"></i>
                        Distribución Modular y Auditoría Analítica Tema por Tema
                    </h3>
                    <p class="text-slate-600 text-sm mt-1">
                        Total de temas auditados en el pensum original: <strong>{total_orig} temas</strong> desglosados en sus 10 módulos oficiales corregidos.
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
                            <span class="w-7 h-7 rounded-lg bg-red-600 text-white font-bold text-xs flex items-center justify-center">{m_num.replace('Módulo ', '') if 'Módulo' in m_num else m_num}</span>
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
                <span class="text-xs font-bold uppercase tracking-wider text-red-600 bg-red-50 px-2.5 py-1 rounded-full border border-red-200">Sección 4</span>
                <h3 class="text-xl font-bold text-slate-900 mt-2 flex items-center gap-2">
                    <i data-lucide="arrow-left-right" class="w-5 h-5 text-red-600"></i>
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
                            <td class="p-3 font-bold text-slate-900 border border-slate-200">Sistema de Carga</td>
                            <td class="p-3 text-slate-600 border border-slate-200">Módulo 6 corrupto en el Excel con temas copiados de motor de arranque.</td>
                            <td class="p-3 text-slate-800 border border-slate-200 font-medium">Alternadores inteligentes con comunicación LIN / PWM con la ECU, sensores inteligentes de batería IBS y recuperación de energía.</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-bold text-slate-900 border border-slate-200">Baterías y Acumuladores</td>
                            <td class="p-3 text-slate-600 border border-slate-200">Prueba con hidrómetro y densímetro de ácido tradicional y carga lenta fija.</td>
                            <td class="p-3 text-slate-800 border border-slate-200 font-medium">Diagnóstico de conductancia con analizador Midtronics, baterías selladas AGM/EFB para Start-Stop y registro digital de batería.</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-bold text-slate-900 border border-slate-200">Redes de Comunicación</td>
                            <td class="p-3 text-slate-600 border border-slate-200">Cableado convencional punto a punto con interruptores directos de carga.</td>
                            <td class="p-3 text-slate-800 border border-slate-200 font-medium">Redes multiplexadas CAN-Bus (alta/baja velocidad) y LIN-Bus, módulos de carrocería (BCM) y diagnóstico con osciloscopio automotriz.</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-bold text-slate-900 border border-slate-200">Sistema de Encendido</td>
                            <td class="p-3 text-slate-600 border border-slate-200">Estudio residual de platinos y condensador con distribuidores centrífugos.</td>
                            <td class="p-3 text-slate-800 border border-slate-200 font-medium">Bobinas individuales COP (Coil-On-Plug) con transistor de potencia integrado y diagnóstico de primario/secundario por osciloscopio.</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-bold text-slate-900 border border-slate-200">Seguridad en Alta Tensión</td>
                            <td class="p-3 text-slate-600 border border-slate-200">Ausencia de protocolos para voltajes superiores a 12/24V.</td>
                            <td class="p-3 text-slate-800 border border-slate-200 font-medium">Protocolos de desenergización y comprobación de ausencia de tensión en sistemas de alto voltaje (200-650 VDC) de vehículos híbridos (HEV).</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </section>

        <!-- SECCIÓN 5: Innovación Tecnológica: Inteligencia Artificial Aplicada -->
        <section class="bg-gradient-to-r from-red-900 via-slate-900 to-indigo-950 text-white rounded-2xl p-6 sm:p-8 shadow-xl space-y-6">
            <div class="flex items-center gap-3 border-b border-white/10 pb-4">
                <div class="p-2.5 rounded-lg bg-red-500/20 text-red-300">
                    <i data-lucide="bot" class="w-6 h-6"></i>
                </div>
                <div>
                    <span class="bg-red-500/30 text-red-200 text-xs px-2.5 py-0.5 rounded-full font-bold uppercase tracking-wider border border-red-400/30">Módulo Adicional / Opcional</span>
                    <h3 class="text-xl font-bold text-white">Innovación Tecnológica: Inteligencia Artificial en Electromecánica Automotriz</h3>
                </div>
            </div>

            <div class="grid md:grid-cols-3 gap-6">
                <div class="bg-white/10 backdrop-blur rounded-xl p-5 border border-white/10 space-y-3">
                    <div class="text-red-300 font-bold text-sm flex items-center gap-2">
                        <i data-lucide="network" class="w-4 h-4"></i>
                        Decodificación y Análisis de Tramas CAN-Bus Asistida por IA
                    </div>
                    <p class="text-xs text-slate-200 leading-relaxed">
                        Software que captura el flujo binario en la red del vehículo y mediante algoritmos de Machine Learning identifica patrones de ruido, tramas corruptas o módulos que colisionan el bus de datos en microsegundos.
                    </p>
                    <div class="pt-2 border-t border-white/10 text-[11px] text-red-200 font-mono">
                        Herramienta: PicoScope Waveform AI / CAN-Bus Analyzer Copilot.
                    </div>
                </div>

                <div class="bg-white/10 backdrop-blur rounded-xl p-5 border border-white/10 space-y-3">
                    <div class="text-red-300 font-bold text-sm flex items-center gap-2">
                        <i data-lucide="camera" class="w-4 h-4"></i>
                        Termografía con IA para Detección de Fugas Parásitas y Puntos Calientes
                    </div>
                    <p class="text-xs text-slate-200 leading-relaxed">
                        Cámaras térmicas conectadas a modelos de visión que escanean la caja de fusibles con el vehículo en reposo, identificando al instante el fusible por donde se fuga corriente parásita descargando la batería.
                    </p>
                    <div class="pt-2 border-t border-white/10 text-[11px] text-red-200 font-mono">
                        Herramienta: FLIR ONE Pro Thermal Auto / Snap-on Diagnostic Thermal.
                    </div>
                </div>

                <div class="bg-white/10 backdrop-blur rounded-xl p-5 border border-white/10 space-y-3">
                    <div class="text-red-300 font-bold text-sm flex items-center gap-2">
                        <i data-lucide="file-text" class="w-4 h-4"></i>
                        Asistente RAG para Diagramas Eléctricos y Mapeo de Pines de ECU
                    </div>
                    <p class="text-xs text-slate-200 leading-relaxed">
                        Asistente interactivo que interpreta diagramas esquemáticos en PDF (Mitchell1, Identifix) y entrega al técnico la ruta de cableado, color de conductor, número de conector y prueba de voltaje exacta a realizar.
                    </p>
                    <div class="pt-2 border-t border-white/10 text-[11px] text-red-200 font-mono">
                        Herramienta: AutoElectrics Copilot / Identifix Direct-Hit AI.
                    </div>
                </div>
            </div>
        </section>

    </main>

    <footer class="bg-white border-t border-slate-200 mt-12 py-6 text-center text-xs text-slate-500">
        Fundación Kinal • Escuela Técnica Superior • Dirección Académica • Propuesta Curricular Electromecánica Automotriz 2026
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
    (output_dir / 'Electromecanica_Automotriz_Propuesta.html').write_text(html, encoding='utf-8')
    print('Generated Electromecanica_Automotriz_Propuesta.html')

generate_ema()
