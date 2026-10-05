import openpyxl
from pathlib import Path

excel_dir = Path('/Users/arqovalle/Library/CloudStorage/OneDrive-Personal/Software/Antigravity/Cuentas Kinal/Programas de Curso')
output_dir = Path('Revision_Temarios')

# -------------------------------------------------------------
# 4. INYECCIÓN ELECTRÓNICA AUTOMOTRIZ (2026_IEAM.xlsx)
# -------------------------------------------------------------
def generate_iea():
    wb = openpyxl.load_workbook(excel_dir / '2026_IEAM.xlsx', data_only=True)
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
            category = 'Inyección y Sensores'
            badge = '🟢 Mantener'
            badge_color = 'bg-emerald-100 text-emerald-800'
            reason = 'Fundamento indispensable para la comprensión del control de inyección, sensores y actuadores del motor.'

            t_lower = t.lower()
            if 'introducción a inyección vortec' in t_lower:
                status = 'delete'
                badge = '🔴 Eliminar'
                badge_color = 'bg-red-100 text-red-800'
                category = 'Sistema Central Antiguo'
                reason = '🔴 Eliminar: Sistema Spider central de inyección de GM de los años 90 descontinuado; el tiempo debe asignarse a inyección directa GDI moderna.'
            elif 'sistema de encendido convencional' in t_lower:
                status = 'delete'
                badge = '🔴 Eliminar'
                badge_color = 'bg-red-100 text-red-800'
                category = 'Tecnología Obsoleta'
                reason = '🔴 Eliminar: Encendido mecánico con platinos descontinuado; enfocar en bobinas COP y transistores integrados.'
            elif 'inyección multipunto' in t_lower:
                status = 'update'
                badge = '🟡 Actualizar'
                badge_color = 'bg-amber-100 text-amber-800'
                category = 'Inyección Multipunto y GDI'
                reason = '🟡 Actualizar: Comparar inyección indirecta secuencial multipunto (SFI) frente a inyección directa de gasolina (GDI) con presiones de hasta 250 bar.'
            elif 'sensores y actuadores' in t_lower or 'medición y comprobación' in t_lower:
                status = 'update'
                badge = '🟡 Actualizar'
                badge_color = 'bg-amber-100 text-amber-800'
                category = 'Diagnóstico con Osciloscopio'
                reason = '🟡 Actualizar: Medición gráfica de formas de onda en sensores inductivos y Hall (CKP/CMP), cuerpos de aceleración motorizados (TAC) y sensores MAP/MAF.'
            elif 'diagnóstico del automóvil obd ii' in t_lower or 'modos de diagnóstico' in t_lower:
                status = 'update'
                badge = '🟡 Actualizar'
                badge_color = 'bg-amber-100 text-amber-800'
                category = 'Modos Globales OBDII'
                reason = '🟡 Actualizar: Interpretación de los 10 modos de diagnóstico OBDII, monitores de emisiones Readiness, freeze frames y ajustes de combustible a corto y largo plazo (STFT/LTFT).'

            mod_topics.append({
                'title': t,
                'status': status,
                'badge': badge,
                'badge_color': badge_color,
                'category': category,
                'reason': reason
            })

        if 'Sistemas de Inyección Electrónica' in m_name:
            mod_topics.append({
                'title': '[NUEVO] Diagnóstico de Inyección Directa de Gasolina (GDI) y Diésel Common Rail',
                'status': 'new',
                'badge': '🔵 Propuesta Nueva',
                'badge_color': 'bg-blue-100 text-blue-800',
                'category': 'Inyección de Alta Presión',
                'reason': '🔵 Propuesta Nueva: Bombas mecánicas de alta presión de combustible accionadas por árbol de levas, sensor de presión de riel FRP e inyectores de alta impedancia y piezoeléctricos.'
            })
        if 'Sensores y Actuadores II' in m_name:
            mod_topics.append({
                'title': '[NUEVO] Análisis de Formas de Onda con Osciloscopio Automotriz de 4 Canales',
                'status': 'new',
                'badge': '🔵 Propuesta Nueva',
                'badge_color': 'bg-blue-100 text-blue-800',
                'category': 'Diagnóstico de Alta Velocidad',
                'reason': '🔵 Propuesta Nueva: Sincronismo gráfico entre CKP y CMP para detectar cadenas de distribución estiradas, tiempo de apertura de inyectores y picos inductivos de bobinas COP.'
            })
        if 'Uso y Funcionamiento del Scanner' in m_name:
            mod_topics.append({
                'title': '[NUEVO] Sensores de Banda Ancha A/F y Diagnóstico de Ajustes de Combustible (STFT / LTFT)',
                'status': 'new',
                'badge': '🔵 Propuesta Nueva',
                'badge_color': 'bg-blue-100 text-blue-800',
                'category': 'Control Estequiométrico',
                'reason': '🔵 Propuesta Nueva: Diagnóstico con escáner de sensores Air-Fuel Ratio midiendo corriente en microamperios (μA) y corrección de mezclas ricas o pobres mediante tablas de STFT/LTFT.'
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
    <title>Auditoría Curricular y Propuesta: Inyección Electrónica Automotriz | Kinal 2026</title>
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
                    <i data-lucide="cpu" class="w-5 h-5 text-red-400"></i>
                    Inyección Electrónica Automotriz
                </h1>
            </div>

            <div class="flex items-center gap-2 text-xs no-print">
                <a href="index.html" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition">Portal Maestro</a>
                <a href="Mecanica_Motores_Gasolina_Propuesta.html" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition">Motores</a>
                <a href="Mecanismos_del_Automovil_Propuesta.html" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition">Mecanismos</a>
                <a href="Electromecanica_Automotriz_Propuesta.html" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition">Electromecánica</a>
                <span class="px-2.5 py-1.5 rounded-lg bg-red-600 text-white font-bold">IEA</span>
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
                <span>2026_IEAM.xlsx</span>
                <i data-lucide="chevron-right" class="w-3.5 h-3.5"></i>
                <span class="text-red-600 font-semibold">Auditoría Curricular & Propuesta 2026</span>
            </div>
            <h2 class="text-3xl font-extrabold text-slate-900 tracking-tight">
                Auditoría Curricular: Inyección Electrónica Automotriz (180 Horas)
            </h2>
            <p class="text-slate-600 mt-2 text-base max-w-4xl">
                Diagnóstico electrónico computarizado avanzado: Uso intensivo de <strong>osciloscopio automotriz de 4 canales</strong> para captura de señales CKP/CMP, sensores de oxígeno de banda ancha <strong>(Air/Fuel Ratio A/F)</strong>, interpretación analítica de ajustes de combustible <strong>STFT / LTFT</strong>, e introducción a la <strong>Inyección Directa de Gasolina (GDI)</strong> y Diésel Common Rail.
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
                    <div class="text-xs font-medium text-red-600 uppercase tracking-wider">A Eliminar (Vortec Spider / Platinos)</div>
                </div>
            </div>

            <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm flex items-center gap-4">
                <div class="w-12 h-12 rounded-lg bg-amber-100 flex items-center justify-center text-amber-600 font-bold text-xl">
                    <i data-lucide="refresh-cw" class="w-6 h-6"></i>
                </div>
                <div>
                    <div class="text-2xl font-bold text-slate-900">{count_upd} Temas</div>
                    <div class="text-xs font-medium text-amber-600 uppercase tracking-wider">A Actualizar (GDI / Osciloscopio / STFT)</div>
                </div>
            </div>

            <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm flex items-center gap-4">
                <div class="w-12 h-12 rounded-lg bg-blue-100 flex items-center justify-center text-blue-600 font-bold text-xl">
                    <i data-lucide="plus-circle" class="w-6 h-6"></i>
                </div>
                <div>
                    <div class="text-2xl font-bold text-slate-900">{count_new} Temas</div>
                    <div class="text-xs font-medium text-blue-600 uppercase tracking-wider">Nuevos Propuestos (Osciloscopio / A/F / GDI)</div>
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
                    Creciente complejidad de la gestión electrónica del motor en talleres especializados y centros de diagnóstico computarizado en Guatemala.
                </p>
            </div>

            <div class="grid md:grid-cols-3 gap-6 text-sm">
                <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 space-y-3">
                    <div class="font-bold text-slate-900 flex items-center gap-2 text-base">
                        <i data-lucide="activity" class="w-5 h-5 text-red-600"></i>
                        Imprescindibilidad del Osciloscopio Automotriz
                    </div>
                    <p class="text-xs text-slate-600 leading-relaxed">
                        El escáner automotriz ya no es suficiente; sólo reporta lo que la computadora del motor interpreta. Para fallas intermitentes de encendido, pérdida de potencia o cadenas de tiempo estiradas, el técnico debe diagnosticar con osciloscopio capturando la forma de onda de voltaje en microsegundos sin cambiar piezas a ciegas.
                    </p>
                </div>

                <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 space-y-3">
                    <div class="font-bold text-slate-900 flex items-center gap-2 text-base">
                        <i data-lucide="sliders" class="w-5 h-5 text-amber-600"></i>
                        Ajustes de Combustible (STFT / LTFT) y Sensores A/F
                    </div>
                    <p class="text-xs text-slate-600 leading-relaxed">
                        Los códigos de falla P0171 (mezcla pobre) y P0172 (mezcla rica) son los más comunes en Guatemala por combustible sucio y fugas de vacío. El diagnóstico profesional exige interpretar las desviaciones en porcentaje de los ajustes a corto y largo plazo y comprobar sensores de oxígeno de banda ancha (A/F Ratio).
                    </p>
                </div>

                <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 space-y-3">
                    <div class="font-bold text-slate-900 flex items-center gap-2 text-base">
                        <i data-lucide="fuel" class="w-5 h-5 text-emerald-600"></i>
                        Inyección Directa GDI y Common Rail
                    </div>
                    <p class="text-xs text-slate-600 leading-relaxed">
                        La mayoría de SUVs y sedanes modernos en circulación incorporan inyección GDI (Ford EcoBoost, Hyundai GDI, VW TSI). Operan a presiones peligrosas superiores a 2,000 PSI; los técnicos requieren formación en despresurización segura del riel y prueba electrónica de solenoides de dosificación.
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
                <div><strong>Programa Académico:</strong> Inyección Electrónica Automotriz (2026_IEAM.xlsx)</div>
                <div><strong>Duración Total:</strong> 180 Horas distribuidas en 10 Módulos prácticos</div>
                <div><strong>Jornadas:</strong> Matutina y Vespertina (Sábados de 8:00 a 12:30 y 13:00 a 17:30 hrs)</div>
                <div><strong>Acreditación:</strong> Diploma Técnico en Inyección Electrónica Automotriz</div>
                <div class="md:col-span-2"><strong>Perfil de Ingreso:</strong> Tercer grado de educación básica, conocimientos previos de electricidad y motores.</div>
                <div class="md:col-span-2"><strong>Perfil de Egreso:</strong> Competencia para analizar y corregir fallas en el sistema de inyección electrónica, sensores, actuadores, encendido y diagnóstico por computadora OBDII.</div>
            </div>

            <div class="bg-amber-50 border border-amber-300 rounded-xl p-5 space-y-3">
                <h4 class="text-amber-900 font-bold text-sm flex items-center gap-2">
                    <i data-lucide="alert-triangle" class="w-5 h-5 text-amber-600"></i>
                    Diagnóstico Crítico / Anomalías Detectadas en el Archivo Original (2026_IEAM.xlsx)
                </h4>
                <ul class="text-xs text-amber-950 space-y-2 list-disc list-inside leading-relaxed">
                    <li><strong>Mención de Sistemas Centrales Obsoletos:</strong> El Módulo 2 lista <em>"Introducción a inyección vortec"</em>, un diseño de inyector central multipunto de General Motors de los años 90 sin vigencia en el mercado actual.</li>
                    <li><strong>Uso Superficial del Escáner (Lectura Básica de Códigos):</strong> El Módulo 10 limitaba el uso del escáner a "recuperación de códigos de avería", cuando la competencia real demandada por los talleres es la interpretación de la línea de datos en vivo (Live Data), gráficas PID y pruebas bidireccionales de actuadores.</li>
                    <li><strong>Omisión del Osciloscopio Automotriz y Sensores A/F:</strong> El temario no contemplaba la herramienta reina del diagnóstico moderno (osciloscopio) ni la tecnología de sensores de relación aire-combustible de banda ancha.</li>
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
                        Total de temas auditados en el pensum original: <strong>{total_orig} temas</strong> desglosados en sus 10 módulos oficiales.
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
                            <td class="p-3 font-bold text-slate-900 border border-slate-200">Instrumental de Diagnóstico</td>
                            <td class="p-3 text-slate-600 border border-slate-200">Uso exclusivo de multímetro digital básico incapaz de registrar fallas transitorias.</td>
                            <td class="p-3 text-slate-800 border border-slate-200 font-medium">Osciloscopio automotriz de 4 canales: correlación gráfica de señales CKP vs. CMP y tiempo de saturación de bobinas.</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-bold text-slate-900 border border-slate-200">Control de Mezcla</td>
                            <td class="p-3 text-slate-600 border border-slate-200">Sondas de oxígeno tradicionales de circonio de salto binario (0.1V a 0.9V).</td>
                            <td class="p-3 text-slate-800 border border-slate-200 font-medium">Sensores de banda ancha A/F (Air-Fuel Ratio) lineales, interpretación de corriente en μA y cálculo de Lambda con escáner.</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-bold text-slate-900 border border-slate-200">Ajustes de Combustible</td>
                            <td class="p-3 text-slate-600 border border-slate-200">Cambio empírico de sensores tras lectura de códigos P0171 o P0172.</td>
                            <td class="p-3 text-slate-800 border border-slate-200 font-medium">Diagnóstico diferencial analítico de compensación de combustible STFT y LTFT para aislar fugas de vacío de bombas deficientes.</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-bold text-slate-900 border border-slate-200">Sistemas de Inyección</td>
                            <td class="p-3 text-slate-600 border border-slate-200">Enfoque centrado en inyección multipunto antigua y sistemas Vortec Spider.</td>
                            <td class="p-3 text-slate-800 border border-slate-200 font-medium">Inyección Directa de Gasolina (GDI), presiones de hasta 250 bar, bombas de alta presión e inyección Diésel Common Rail.</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-bold text-slate-900 border border-slate-200">Manejo del Escáner</td>
                            <td class="p-3 text-slate-600 border border-slate-200">Lectura y borrado superficial de códigos de avería DTC.</td>
                            <td class="p-3 text-slate-800 border border-slate-200 font-medium">Pruebas activas bidireccionales (corte de cilindro, activación de EVAP, cuerpo de aceleración) y análisis de Monitores Readiness.</td>
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
                    <h3 class="text-xl font-bold text-white">Innovación Tecnológica: Inteligencia Artificial en Inyección Electrónica</h3>
                </div>
            </div>

            <div class="grid md:grid-cols-3 gap-6">
                <div class="bg-white/10 backdrop-blur rounded-xl p-5 border border-white/10 space-y-3">
                    <div class="text-red-300 font-bold text-sm flex items-center gap-2">
                        <i data-lucide="cpu" class="w-4 h-4"></i>
                        Diagnóstico Predictivo de Códigos DTC con Modelos LLM
                    </div>
                    <p class="text-xs text-slate-200 leading-relaxed">
                        Sistemas que analizan el cuadro congelado (Freeze Frame) y los códigos DTC combinados con la marca y kilometraje, sugiriendo el árbol de diagnóstico de mayor probabilidad de éxito según estadísticas de millones de reparaciones.
                    </p>
                    <div class="pt-2 border-t border-white/10 text-[11px] text-red-200 font-mono">
                        Herramienta: Bosch ESI[tronic] AI Copilot / Snap-on Fast-Track AI.
                    </div>
                </div>

                <div class="bg-white/10 backdrop-blur rounded-xl p-5 border border-white/10 space-y-3">
                    <div class="text-red-300 font-bold text-sm flex items-center gap-2">
                        <i data-lucide="activity" class="w-4 h-4"></i>
                        Reconocimiento Automático de Formas de Onda Anómalas
                    </div>
                    <p class="text-xs text-slate-200 leading-relaxed">
                        Algoritmos integrados en el osciloscopio que comparan la señal capturada del sensor con la base de datos de referencia dorada (Golden Waveform), señalando fallas de ruido eléctrico o atenuación en pantalla.
                    </p>
                    <div class="pt-2 border-t border-white/10 text-[11px] text-red-200 font-mono">
                        Herramienta: PicoScope AI Waveform Assistant / Autel LabScope AI.
                    </div>
                </div>

                <div class="bg-white/10 backdrop-blur rounded-xl p-5 border border-white/10 space-y-3">
                    <div class="text-red-300 font-bold text-sm flex items-center gap-2">
                        <i data-lucide="sliders" class="w-4 h-4"></i>
                        Asistente RAG para Calibraciones y Aprendizajes Adaptativos
                    </div>
                    <p class="text-xs text-slate-200 leading-relaxed">
                        Copilot de taller que entrega al instante las condiciones previas exactas (temperatura de motor, RPM, marcha) requeridas por la ECU para ejecutar con éxito el aprendizaje del cuerpo de aceleración electrónico y sensores CKP.
                    </p>
                    <div class="pt-2 border-t border-white/10 text-[11px] text-red-200 font-mono">
                        Herramienta: Launch SmartLink Copilot / Identifix AI Assistant.
                    </div>
                </div>
            </div>
        </section>

    </main>

    <footer class="bg-white border-t border-slate-200 mt-12 py-6 text-center text-xs text-slate-500">
        Fundación Kinal • Escuela Técnica Superior • Coordinación Académica • Propuesta Curricular Inyección Electrónica Automotriz 2026
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
    (output_dir / 'Inyeccion_Electronica_Automotriz_Propuesta.html').write_text(html, encoding='utf-8')
    print('Generated Inyeccion_Electronica_Automotriz_Propuesta.html')

generate_iea()
