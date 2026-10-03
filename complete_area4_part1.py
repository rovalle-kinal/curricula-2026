import openpyxl
from pathlib import Path

excel_dir = Path('/Users/arqovalle/Library/CloudStorage/OneDrive-Personal/Software/Antigravity/Cuentas Kinal/Programas de Curso')
output_dir = Path('Revision_Temarios')

# -------------------------------------------------------------
# 2. MECANISMOS DEL AUTOMÓVIL (2026_MAA.xlsx)
# -------------------------------------------------------------
def generate_maa():
    wb = openpyxl.load_workbook(excel_dir / '2026_MAA.xlsx', data_only=True)
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
            category = 'Chasis y Transmisión'
            badge = '🟢 Mantener'
            badge_color = 'bg-emerald-100 text-emerald-800'
            reason = 'Fundamento mecánico esencial del chasis, suspensión, frenos y tren de rodaje en el taller automotriz.'

            t_lower = t.lower()
            if 'definición de electricidad' in t_lower or 'materiales conductores' in t_lower:
                status = 'delete'
                badge = '🔴 Eliminar'
                badge_color = 'bg-red-100 text-red-800'
                category = 'Contenido Duplicado'
                reason = '🔴 Eliminar: Materia eléctrica que desvía el enfoque del curso de mecanismos de chasis; su espacio debe destinarse a cajas automáticas y frenos electrónicos.'
            elif 'freno de tambor' in t_lower or 'freno de disco' in t_lower or 'sistema hidráulico de frenos' in t_lower:
                status = 'update'
                badge = '🟡 Actualizar'
                badge_color = 'bg-amber-100 text-amber-800'
                category = 'Sistemas de Frenado Moderno'
                reason = '🟡 Actualizar: Diagnóstico de sistemas antibloqueo ABS y control de estabilidad ESP, sensores inductivos/Hall de rueda y rectificado bajo especificación micrométrica de alabeo.'
            elif 'mecanismo de dirección' in t_lower:
                status = 'update'
                badge = '🟡 Actualizar'
                badge_color = 'bg-amber-100 text-amber-800'
                category = 'Dirección Electroasistida'
                reason = '🟡 Actualizar: Transición de cremalleras hidráulicas convencionales a direcciones electroasistidas (EPS), diagnóstico del motor eléctrico y sensor de par.'
            elif 'mecanismo de suspensión' in t_lower:
                status = 'update'
                badge = '🟡 Actualizar'
                badge_color = 'bg-amber-100 text-amber-800'
                category = 'Geometría y Alineación 3D'
                reason = '🟡 Actualizar: Suspensión multibrazo independiente, amortiguadores presurizados con gas nitrógeno y alineación computarizada 3D con ajuste de convergencia, cámber y cáster.'
            elif 'caja de velocidades mecánica' in t_lower or 'transmisión mecánica' in t_lower:
                status = 'update'
                badge = '🟡 Actualizar'
                badge_color = 'bg-amber-100 text-amber-800'
                category = 'Tren de Transmisión'
                reason = '🟡 Actualizar: Sincronizadores de bronce y carbono, precarga de rodamientos cónicos y principios de funcionamiento de transmisiones automáticas y CVT.'

            mod_topics.append({
                'title': t,
                'status': status,
                'badge': badge,
                'badge_color': badge_color,
                'category': category,
                'reason': reason
            })

        if 'Sistema Hidráulico de Frenos' in m_name:
            mod_topics.append({
                'title': '[NUEVO] Diagnóstico de Frenos ABS / ESP y Procedimiento de Sangrado con Escáner',
                'status': 'new',
                'badge': '🔵 Propuesta Nueva',
                'badge_color': 'bg-blue-100 text-blue-800',
                'category': 'Seguridad Activa',
                'reason': '🔵 Propuesta Nueva: Ciclado de electroválvulas y bomba de retorno del módulo electrohidráulico ABS mediante escáner bidireccional para purga completa de aire.'
            })
        if 'Mecanismo de Dirección' in m_name:
            mod_topics.append({
                'title': '[NUEVO] Direcciones Asistidas Eléctricas (EPS) y Calibración de Sensor SAS',
                'status': 'new',
                'badge': '🔵 Propuesta Nueva',
                'badge_color': 'bg-blue-100 text-blue-800',
                'category': 'Dirección Inteligente',
                'reason': '🔵 Propuesta Nueva: Diagnóstico de sistemas EPS en columna y cremallera, reaprendizaje del sensor de ángulo de giro (Steering Angle Sensor) tras alineación de ruedas.'
            })
        if 'Transmisión Mecánica' in m_name:
            mod_topics.append({
                'title': '[NUEVO] Fundamentos y Mantenimiento de Cajas Automáticas y Transmisiones CVT',
                'status': 'new',
                'badge': '🔵 Propuesta Nueva',
                'badge_color': 'bg-blue-100 text-blue-800',
                'category': 'Transmisiones Automáticas',
                'reason': '🔵 Propuesta Nueva: Inspección de fluidos ATF y CVTF específicos, funcionamiento de convertidor de par con embrague lock-up y cuerpo de válvulas con solenoides PWM.'
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
    <title>Auditoría Curricular y Propuesta: Mecanismos del Automóvil | Kinal 2026</title>
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
                    <i data-lucide="shield" class="w-5 h-5 text-red-400"></i>
                    Mecanismos del Automóvil
                </h1>
            </div>

            <div class="flex items-center gap-2 text-xs no-print">
                <a href="index.html" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition">Portal Maestro</a>
                <a href="Mecanica_Motores_Gasolina_Propuesta.html" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition">Motores</a>
                <span class="px-2.5 py-1.5 rounded-lg bg-red-600 text-white font-bold">MAA</span>
                <a href="Electromecanica_Automotriz_Propuesta.html" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition">Electromecánica</a>
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
                <span>2026_MAA.xlsx</span>
                <i data-lucide="chevron-right" class="w-3.5 h-3.5"></i>
                <span class="text-red-600 font-semibold">Auditoría Curricular & Propuesta 2026</span>
            </div>
            <h2 class="text-3xl font-extrabold text-slate-900 tracking-tight">
                Auditoría Curricular: Mecanismos del Automóvil (180 Horas)
            </h2>
            <p class="text-slate-600 mt-2 text-base max-w-4xl">
                Modernización integral de los sistemas de seguridad activa del chasis: Frenos ABS/ESP con sangrado por escáner, Direcciones Asistidas Eléctricamente (EPS) con calibración de sensor de ángulo de volante (SAS), Suspensión Multibrazo con Alineación 3D e Introducción a Cajas Automáticas y CVT.
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
                    <div class="text-xs font-medium text-red-600 uppercase tracking-wider">A Eliminar (Electricidad Duplicada)</div>
                </div>
            </div>

            <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm flex items-center gap-4">
                <div class="w-12 h-12 rounded-lg bg-amber-100 flex items-center justify-center text-amber-600 font-bold text-xl">
                    <i data-lucide="refresh-cw" class="w-6 h-6"></i>
                </div>
                <div>
                    <div class="text-2xl font-bold text-slate-900">{count_upd} Temas</div>
                    <div class="text-xs font-medium text-amber-600 uppercase tracking-wider">A Actualizar (ABS / EPS / Alineación 3D)</div>
                </div>
            </div>

            <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm flex items-center gap-4">
                <div class="w-12 h-12 rounded-lg bg-blue-100 flex items-center justify-center text-blue-600 font-bold text-xl">
                    <i data-lucide="plus-circle" class="w-6 h-6"></i>
                </div>
                <div>
                    <div class="text-2xl font-bold text-slate-900">{count_new} Temas</div>
                    <div class="text-xs font-medium text-blue-600 uppercase tracking-wider">Nuevos Propuestos (ABS / EPS / CVT)</div>
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
                    Exigencias de diagnóstico en centros de frenado, talleres de alineación computarizada y agencias automotrices en Guatemala.
                </p>
            </div>

            <div class="grid md:grid-cols-3 gap-6 text-sm">
                <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 space-y-3">
                    <div class="font-bold text-slate-900 flex items-center gap-2 text-base">
                        <i data-lucide="disc" class="w-5 h-5 text-red-600"></i>
                        Electrónica Integrada al Frenado (ABS / ESP / EPB)
                    </div>
                    <p class="text-slate-600 text-xs leading-relaxed">
                        Los vehículos modernos ya no admiten el purgado manual por bombeo de pedal; la presencia de módulos ABS y frenos de estacionamiento eléctricos (EPB) exige el uso de escáner bidireccional para retraer calipers traseros y ciclar electroválvulas, evitando daños irreversibles en el bloque hidráulico.
                    </p>
                </div>

                <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 space-y-3">
                    <div class="font-bold text-slate-900 flex items-center gap-2 text-base">
                        <i data-lucide="compass" class="w-5 h-5 text-amber-600"></i>
                        Direcciones EPS y Sensor de Ángulo (SAS)
                    </div>
                    <p class="text-slate-600 text-xs leading-relaxed">
                        La bomba hidráulica de dirección impulsada por faja ha sido reemplazada en más del 80% del parque automotor guatemalteco por columnas de dirección electroasistidas (EPS). Un alineador que no restablezca a cero el sensor de ángulo de dirección (SAS) deja al vehículo con desvío y testigo de control de tracción encendido.
                    </p>
                </div>

                <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 space-y-3">
                    <div class="font-bold text-slate-900 flex items-center gap-2 text-base">
                        <i data-lucide="sliders" class="w-5 h-5 text-emerald-600"></i>
                        Proliferación de Cajas Automáticas y CVT
                    </div>
                    <p class="text-slate-600 text-xs leading-relaxed">
                        El parque vehicular guatemalteco es mayoritariamente automático (vehículos rodados de EE.UU. y nuevos de agencia). Limitar el curso a cajas manuales de 5 velocidades deja al mecánico desarmado ante fallas comunes de jaloneo en cajas CVT o patinamiento de embragues por fluidos incorrectos.
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
                <div><strong>Programa Académico:</strong> Mecanismos del Automóvil (2026_MAA.xlsx)</div>
                <div><strong>Duración Total:</strong> 180 Horas distribuidas en 10 Módulos prácticos</div>
                <div><strong>Jornadas:</strong> Matutina y Vespertina (Sábados de 8:00 a 12:30 y 13:00 a 17:30 hrs)</div>
                <div><strong>Acreditación:</strong> Diploma Técnico en Reparación de Mecanismos del Automóvil</div>
                <div class="md:col-span-2"><strong>Perfil de Ingreso:</strong> Tercer grado de educación básica, destreza motriz y gusto por la mecánica de chasis.</div>
                <div class="md:col-span-2"><strong>Perfil de Egreso:</strong> Competencia para desmontar, diagnosticar, calibrar y reparar sistemas de suspensión, dirección, frenos convencionales y antibloqueo, embragues y trenes de potencia motriz.</div>
            </div>

            <div class="bg-amber-50 border border-amber-300 rounded-xl p-5 space-y-3">
                <h4 class="text-amber-900 font-bold text-sm flex items-center gap-2">
                    <i data-lucide="alert-triangle" class="w-5 h-5 text-amber-600"></i>
                    Diagnóstico Crítico / Anomalías Detectadas en el Archivo Original (2026_MAA.xlsx)
                </h4>
                <ul class="text-xs text-amber-950 space-y-2 list-disc list-inside leading-relaxed">
                    <li><strong>Módulo Final Duplicado e Incongruente:</strong> El Módulo 10 se titula <em>"Principios de Electricidad Automotriz"</em> (conductores, aislantes, circuitos serie/paralelo). Este contenido es idéntico al Módulo 1 de Electromecánica Automotriz y consume 18 horas que deben dedicarse al diagnóstico de transmisiones automáticas y CVT.</li>
                    <li><strong>Desconexión Electrónica en Frenos y Dirección:</strong> Los Módulos 2, 3 y 5 tratan los frenos y la dirección desde una perspectiva puramente hidráulica y mecánica de los años 80, ignorando los sensores de rueda ABS, los módulos de control ESP y las direcciones electroasistidas EPS.</li>
                    <li><strong>Ausencia de Transmisiones Automáticas y CVT:</strong> El Módulo 7 se restringe a <em>"Transmisión Mecánica"</em> (cajas manuales), desatendiendo el tipo de transmisión que domina más del 70% de los automóviles en circulación en Guatemala.</li>
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
                            <td class="p-3 font-bold text-slate-900 border border-slate-200">Sistemas de Frenos</td>
                            <td class="p-3 text-slate-600 border border-slate-200">Enfoque limitado a bombas mecánicas, cilindros de rueda y purgado manual por pedal.</td>
                            <td class="p-3 text-slate-800 border border-slate-200 font-medium">Frenos antibloqueo ABS y control de estabilidad ESP, sensores de rueda inductivos/Hall y sangrado por escáner con apertura de válvulas solenoides.</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-bold text-slate-900 border border-slate-200">Sistemas de Dirección</td>
                            <td class="p-3 text-slate-600 border border-slate-200">Cremalleras de asistencia hidráulica con bomba accionada por polea mecánica.</td>
                            <td class="p-3 text-slate-800 border border-slate-200 font-medium">Direcciones electroasistidas (EPS), diagnóstico del motor brushless de asistencia y calibración del sensor de ángulo de volante (SAS).</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-bold text-slate-900 border border-slate-200">Suspensión y Geometría</td>
                            <td class="p-3 text-slate-600 border border-slate-200">Inspección visual de tijeras y amortiguadores y alineación óptica manual rudimentaria.</td>
                            <td class="p-3 text-slate-800 border border-slate-200 font-medium">Alineación computarizada 3D con cámaras de alta definición, diagnóstico de suspensión multibrazo y lectura de ángulos Cámber, Cáster y Convergencia.</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-bold text-slate-900 border border-slate-200">Cajas de Velocidades</td>
                            <td class="p-3 text-slate-600 border border-slate-200">Estudio exclusivo de cajas de engranajes mecánicos manuales de 5 velocidades.</td>
                            <td class="p-3 text-slate-800 border border-slate-200 font-medium">Transmisiones automáticas hidráulicas y cajas continuamente variables (CVT), convertidor de par con lock-up y fluidos sintéticos OEM.</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-bold text-slate-900 border border-slate-200">Aprovechamiento Horario</td>
                            <td class="p-3 text-slate-600 border border-slate-200">18 horas desperdiciadas al final del curso en teoría eléctrica básica repetida.</td>
                            <td class="p-3 text-slate-800 border border-slate-200 font-medium">Horas reasignadas por completo a prácticas reales de diagnóstico con escáner en frenos ABS y servicio de transmisiones automáticas.</td>
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
                    <h3 class="text-xl font-bold text-white">Innovación Tecnológica: Inteligencia Artificial en Mecanismos del Automóvil</h3>
                </div>
            </div>

            <div class="grid md:grid-cols-3 gap-6">
                <div class="bg-white/10 backdrop-blur rounded-xl p-5 border border-white/10 space-y-3">
                    <div class="text-red-300 font-bold text-sm flex items-center gap-2">
                        <i data-lucide="camera" class="w-4 h-4"></i>
                        Inspección Óptica de Neumáticos y Diagnóstico de Alineación con IA
                    </div>
                    <p class="text-xs text-slate-200 leading-relaxed">
                        Cámaras que fotografían el patrón de rodadura de los neumáticos y mediante visión artificial detectan desgaste en sierra o en hombros, diagnosticando si el problema reside en convergencia, cámber o amortiguadores vencidos.
                    </p>
                    <div class="pt-2 border-t border-white/10 text-[11px] text-red-200 font-mono">
                        Herramienta: Hunter Quick Check Drive AI / TreadReader Vision.
                    </div>
                </div>

                <div class="bg-white/10 backdrop-blur rounded-xl p-5 border border-white/10 space-y-3">
                    <div class="text-red-300 font-bold text-sm flex items-center gap-2">
                        <i data-lucide="activity" class="w-4 h-4"></i>
                        Detección Acústica de Fallas en Tren Motriz y Rodamientos
                    </div>
                    <p class="text-xs text-slate-200 leading-relaxed">
                        Sensores de vibración inalámbricos que analizan el sonido durante la prueba de ruta para diferenciar si el zumbido proviene de la bocallave delantera, la junta homocinética o el piñón y corona del diferencial.
                    </p>
                    <div class="pt-2 border-t border-white/10 text-[11px] text-red-200 font-mono">
                        Herramienta: ChassisEAR Wireless AI / Bosch NVH Diagnostic.
                    </div>
                </div>

                <div class="bg-white/10 backdrop-blur rounded-xl p-5 border border-white/10 space-y-3">
                    <div class="text-red-300 font-bold text-sm flex items-center gap-2">
                        <i data-lucide="sliders" class="w-4 h-4"></i>
                        Asistente RAG para Selección de Fluidos y Calibración de Transmisiones
                    </div>
                    <p class="text-xs text-slate-200 leading-relaxed">
                        Asistente técnico que indica el fluido de transmisión ATF/CVT exacto requerido por el fabricante (evitando mezclas destructivas) y la secuencia de aprendizaje adaptativo de marchas tras el cambio de aceite.
                    </p>
                    <div class="pt-2 border-t border-white/10 text-[11px] text-red-200 font-mono">
                        Herramienta: LubriData AI Assistant / Mitchell1 ProDemand.
                    </div>
                </div>
            </div>
        </section>

    </main>

    <footer class="bg-white border-t border-slate-200 mt-12 py-6 text-center text-xs text-slate-500">
        Fundación Kinal • Escuela Técnica Superior • Dirección Académica • Propuesta Curricular Mecanismos del Automóvil 2026
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
    (output_dir / 'Mecanismos_del_Automovil_Propuesta.html').write_text(html, encoding='utf-8')
    print('Generated Mecanismos_del_Automovil_Propuesta.html')

generate_maa()
