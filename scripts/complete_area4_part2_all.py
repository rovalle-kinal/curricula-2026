import openpyxl
from pathlib import Path

excel_dir = Path('/Users/arqovalle/Library/CloudStorage/OneDrive-Personal/Software/Antigravity/Cuentas Kinal/Programas de Curso')
output_dir = Path('Revision_Temarios')

# -------------------------------------------------------------
# 5. AIRE ACONDICIONADO AUTOMOTRIZ (2025_AAA.xlsx)
# -------------------------------------------------------------
def generate_aaa():
    wb = openpyxl.load_workbook(excel_dir / '2025_AAA.xlsx', data_only=True)
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
            category = 'Climatización y Termodinámica'
            badge = '🟢 Mantener'
            badge_color = 'bg-emerald-100 text-emerald-800'
            reason = 'Fundamento del ciclo frigorífico por compresión de vapor indispensable para la climatización vehicular.'

            t_lower = t.lower()
            if 'estructura atómica y cargas eléctricas' in t_lower:
                status = 'delete'
                badge = '🔴 Eliminar'
                badge_color = 'bg-red-100 text-red-800'
                category = 'Física Básica Escolar'
                reason = '🔴 Eliminar: Contenido de física escolar básica irrelevante para el trabajo en el taller de climatización; restar horas teóricas para ganar prácticas en compresores variables.'
            elif 'teoría del flujo eléctrico' in t_lower:
                status = 'delete'
                badge = '🔴 Eliminar'
                badge_color = 'bg-red-100 text-red-800'
                category = 'Teoría Redundante'
                reason = '🔴 Eliminar: Teoría abstracta redundante; enfocar directamente en la medición de caída de tensión en bobinas de clutch y sensores de temperatura.'
            elif 'teoría básica de enfriamiento' in t_lower or 'teoría de la transferencia de calor' in t_lower or 'el refrigerante 134a' in t_lower:
                status = 'update'
                badge = '🟡 Actualizar'
                badge_color = 'bg-amber-100 text-amber-800'
                category = 'Nuevos Refrigerantes HFO'
                reason = '🟡 Actualizar: Incorporar el nuevo gas refrigerante ecológico HFO-1234yf (clasificación A2L de bajo impacto ambiental GWP < 1) junto al tradicional R-134a.'
            elif 'el compresor' in t_lower or 'compresor de aire acondicionado' in t_lower or 'componentes del compresor' in t_lower:
                status = 'update'
                badge = '🟡 Actualizar'
                badge_color = 'bg-amber-100 text-amber-800'
                category = 'Compresores de Flujo Continuo'
                reason = '🟡 Actualizar: Diagnóstico de compresores de desplazamiento variable sin embrague magnético gobernados por válvula electrónica PWM y selección de aceite PAG 46/100.'
            elif 'el multímetro' in t_lower or 'componentes del multímetro' in t_lower or 'descripción de códigos' in t_lower or 'utilización del scanner' in t_lower:
                status = 'update'
                badge = '🟡 Actualizar'
                badge_color = 'bg-amber-100 text-amber-800'
                category = 'Climatronic y Sensores'
                reason = '🟡 Actualizar: Diagnóstico de climatizadores automáticos bi-zona con escáner, sensores de temperatura de evaporador, sensor solar y servomotores de compuertas paso a paso.'
            elif 'vacío' in t_lower or 'recicladora de gas' in t_lower or 'recuperadora de gas' in t_lower:
                status = 'update'
                badge = '🟡 Actualizar'
                badge_color = 'bg-amber-100 text-amber-800'
                category = 'Procedimiento Técnico SAE'
                reason = '🟡 Actualizar: Medición de vacío profundo con vacuómetro digital (< 500 micrones) para evaporar humedad y carga en fase líquida por peso exacto con báscula electrónica.'

            mod_topics.append({
                'title': t,
                'status': status,
                'badge': badge,
                'badge_color': badge_color,
                'category': category,
                'reason': reason
            })

        if 'Montaje y Funcionamiento' in m_name:
            mod_topics.append({
                'title': '[NUEVO] Servicio y Protocolos de Carga del Refrigerante Ecológico HFO-1234yf',
                'status': 'new',
                'badge': '🔵 Propuesta Nueva',
                'badge_color': 'bg-blue-100 text-blue-800',
                'category': 'Normativa Ambiental Global',
                'reason': '🔵 Propuesta Nueva: Manejo seguro de refrigerantes ligeramente inflamables A2L, detección de fugas por ultrasonido/óptica y estaciones de carga homologadas SAE J2843.'
            })
            mod_topics.append({
                'title': '[NUEVO] Compresores de Desplazamiento Variable con Válvula Electrónica PWM',
                'status': 'new',
                'badge': '🔵 Propuesta Nueva',
                'badge_color': 'bg-blue-100 text-blue-800',
                'category': 'Compresores de Última Generación',
                'reason': '🔵 Propuesta Nueva: Diagnóstico de señal de modulación PWM de la válvula de control de carrera con osciloscopio para evitar cambios innecesarios de compresores costosos.'
            })
        if 'Diagnóstico Eléctrico' in m_name:
            mod_topics.append({
                'title': '[NUEVO] Climatización Eléctrica de Alta Tensión en Vehículos Híbridos y Eléctricos (HEV/EV)',
                'status': 'new',
                'badge': '🔵 Propuesta Nueva',
                'badge_color': 'bg-blue-100 text-blue-800',
                'category': 'Sistemas de Alta Tensión Híbrida',
                'reason': '🔵 Propuesta Nueva: Compresores scroll herméticos accionados por inversor trifásico de alto voltaje (200-650 VDC) y uso exclusivo de aceite dieléctrico sintético POE.'
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
    <title>Auditoría Curricular y Propuesta: Aire Acondicionado Automotriz | Kinal 2026</title>
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
                    <i data-lucide="snowflake" class="w-5 h-5 text-cyan-400"></i>
                    Aire Acondicionado Automotriz
                </h1>
            </div>

            <div class="flex items-center gap-2 text-xs no-print">
                <a href="index.html" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition">Portal Maestro</a>
                <a href="Mecanica_Motores_Gasolina_Propuesta.html" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition">Motores</a>
                <a href="Mecanismos_del_Automovil_Propuesta.html" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition">Mecanismos</a>
                <a href="Electromecanica_Automotriz_Propuesta.html" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition">Electromecánica</a>
                <a href="Inyeccion_Electronica_Automotriz_Propuesta.html" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition">Inyección</a>
                <span class="px-2.5 py-1.5 rounded-lg bg-red-600 text-white font-bold">AAA</span>
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
                <span>2025_AAA.xlsx</span>
                <i data-lucide="chevron-right" class="w-3.5 h-3.5"></i>
                <span class="text-red-600 font-semibold">Auditoría Curricular & Propuesta 2026</span>
            </div>
            <h2 class="text-3xl font-extrabold text-slate-900 tracking-tight">
                Auditoría Curricular: Aire Acondicionado Automotriz (180 Horas)
            </h2>
            <p class="text-slate-600 mt-2 text-base max-w-4xl">
                Modernización integral de la climatización automotriz: Introducción del nuevo refrigerante ecológico <strong>HFO-1234yf</strong>, diagnóstico de <strong>compresores de desplazamiento variable gobernados por PWM</strong>, climatizadores automáticos bi-zona con escáner, y protocolos de servicio en <strong>compresores eléctricos de alto voltaje</strong> para vehículos híbridos y eléctricos (HEV/EV).
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
                    <div class="text-xs font-medium text-red-600 uppercase tracking-wider">A Eliminar (Física Escolar Básica)</div>
                </div>
            </div>

            <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm flex items-center gap-4">
                <div class="w-12 h-12 rounded-lg bg-amber-100 flex items-center justify-center text-amber-600 font-bold text-xl">
                    <i data-lucide="refresh-cw" class="w-6 h-6"></i>
                </div>
                <div>
                    <div class="text-2xl font-bold text-slate-900">{count_upd} Temas</div>
                    <div class="text-xs font-medium text-amber-600 uppercase tracking-wider">A Actualizar (R-1234yf / PWM / Climatronic)</div>
                </div>
            </div>

            <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm flex items-center gap-4">
                <div class="w-12 h-12 rounded-lg bg-blue-100 flex items-center justify-center text-blue-600 font-bold text-xl">
                    <i data-lucide="plus-circle" class="w-6 h-6"></i>
                </div>
                <div>
                    <div class="text-2xl font-bold text-slate-900">{count_new} Temas</div>
                    <div class="text-xs font-medium text-blue-600 uppercase tracking-wider">Nuevos Propuestos (R-1234yf / PWM / Híbridos)</div>
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
                    Exigencias medioambientales y tecnológicas en centros de servicio de climatización vehicular en Guatemala frente a la importación masiva de vehículos rodados y de agencia.
                </p>
            </div>

            <div class="grid md:grid-cols-3 gap-6 text-sm">
                <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 space-y-3">
                    <div class="font-bold text-slate-900 flex items-center gap-2 text-base">
                        <i data-lucide="leaf" class="w-5 h-5 text-emerald-600"></i>
                        Transición Obligatoria al Refrigerante HFO-1234yf
                    </div>
                    <p class="text-slate-600 text-xs leading-relaxed">
                        Todos los vehículos importados desde Estados Unidos y Europa modelo 2018 en adelante vienen cargados de fábrica con refrigerante R-1234yf. Es un gas ligeramente inflamable (A2L) que no debe mezclarse jamás con R-134a ni cargarse con manómetros contaminados; exige estaciones de servicio homologadas SAE J2843.
                    </p>
                </div>

                <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 space-y-3">
                    <div class="font-bold text-slate-900 flex items-center gap-2 text-base">
                        <i data-lucide="gauge" class="w-5 h-5 text-amber-600"></i>
                        Compresores de Desplazamiento Variable (Sin Clutch)
                    </div>
                    <p class="text-slate-600 text-xs leading-relaxed">
                        Más del 70% de los automóviles recientes ya no tienen embrague electromagnético que haga "clic" al encender el AC. Operan con un plato oscilante gobernado electrónicamente por una válvula de control PWM. Mecánicos no capacitados diagnostican erróneamente compresores dañados cuando el fallo es de control electrónico.
                    </p>
                </div>

                <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 space-y-3">
                    <div class="font-bold text-slate-900 flex items-center gap-2 text-base">
                        <i data-lucide="zap" class="w-5 h-5 text-blue-600"></i>
                        Climatización Eléctrica de Alta Tensión en Híbridos
                    </div>
                    <p class="text-slate-600 text-xs leading-relaxed">
                        En vehículos híbridos (Toyota Prius, Aqua, Honda Insight), el compresor de AC no lleva faja al motor térmico; funciona con un motor eléctrico trifásico alimentado por el banco de baterías de 200V+. Requiere estrictamente aceite dieléctrico POE (Polyolester); usar aceite PAG conductor provoca fuga a tierra y bloqueo del sistema híbrido.
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
                <div><strong>Programa Académico:</strong> Aire Acondicionado Automotriz (2025_AAA.xlsx)</div>
                <div><strong>Duración Total:</strong> 180 Horas distribuidas en 2 Fases modulares profundas (90 hrs c/u)</div>
                <div><strong>Jornadas:</strong> Matutina y Vespertina (Sábados de 8:00 a 12:30 y 13:00 a 17:30 hrs)</div>
                <div><strong>Acreditación:</strong> Diploma de Técnico en Aire Acondicionado Automotriz</div>
                <div class="md:col-span-2"><strong>Perfil de Ingreso:</strong> Mayor de edad, sexto grado de primaria como mínimo, interés en sistemas de refrigeración y climatización vehicular.</div>
                <div class="md:col-span-2"><strong>Perfil de Egreso:</strong> Competencia para reparar, ensamblar, realizar vacío técnico, recarga de refrigerante y diagnóstico electrónico en sistemas de climatización automotriz bajo normas medioambientales.</div>
            </div>

            <div class="bg-amber-50 border border-amber-300 rounded-xl p-5 space-y-3">
                <h4 class="text-amber-900 font-bold text-sm flex items-center gap-2">
                    <i data-lucide="alert-triangle" class="w-5 h-5 text-amber-600"></i>
                    Diagnóstico Crítico / Anomalías Detectadas en el Archivo Original (2025_AAA.xlsx)
                </h4>
                <ul class="text-xs text-amber-950 space-y-2 list-disc list-inside leading-relaxed">
                    <li><strong>Estructura Monolítica en Sólo 2 Módulos:</strong> El programa divide 180 horas en únicamente dos bloques gigantescos de 38 y 46 temas, lo que dificulta la dosificación pedagógica semanal y el seguimiento de competencias por hitos.</li>
                    <li><strong>Temas de Física Escolar Elemental:</strong> En la Fase 2 se dedican horas a <em>"Estructura atómica y cargas eléctricas"</em> y <em>"Teoría del flujo eléctrico"</em>, contenidos teóricos no aplicados que deben ser reemplazados por prácticas de diagnóstico en compresores variables y climatizadores automáticos.</li>
                    <li><strong>Omisión de Compresores Variables y Climatización de Híbridos:</strong> No se incluía el diagnóstico de la válvula de control electrónico PWM ni el compresor eléctrico hermético de alta tensión de vehículos híbridos.</li>
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
                        Total de temas auditados en el pensum original: <strong>{total_orig} temas</strong> desglosados en sus 2 fases modulares oficiales.
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
                            <td class="p-3 font-bold text-slate-900 border border-slate-200">Gases Refrigerantes</td>
                            <td class="p-3 text-slate-600 border border-slate-200">Enfoque 100% exclusivo en refrigerante R-134a sin consideraciones de inflamabilidad.</td>
                            <td class="p-3 text-slate-800 border border-slate-200 font-medium">Refrigerante ecológico HFO-1234yf (clasificación A2L de bajo impacto ambiental), normas de seguridad SAE J2843 y recuperación estricta.</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-bold text-slate-900 border border-slate-200">Tecnología de Compresores</td>
                            <td class="p-3 text-slate-600 border border-slate-200">Compresores mecánicos tradicionales con embrague electromagnético on/off de 12V.</td>
                            <td class="p-3 text-slate-800 border border-slate-200 font-medium">Compresores de cilindrada variable gobernados por modulación electrónica PWM sin clutch y compresores eléctricos scroll de alto voltaje en híbridos.</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-bold text-slate-900 border border-slate-200">Aceites y Lubricantes</td>
                            <td class="p-3 text-slate-600 border border-slate-200">Uso indistinto de aceite mineral o PAG genérico sin verificar viscosidad ni conductividad.</td>
                            <td class="p-3 text-slate-800 border border-slate-200 font-medium">Selección estricta de PAG 46/100 para HFO-1234yf y aceite dieléctrico POE de alta pureza aislante para compresores de autos híbridos.</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-bold text-slate-900 border border-slate-200">Proceso de Vacío y Carga</td>
                            <td class="p-3 text-slate-600 border border-slate-200">Vacío por tiempo con bomba básica y carga de gas aproximada por presión manométrica.</td>
                            <td class="p-3 text-slate-800 border border-slate-200 font-medium">Vacío profundo controlado con vacuómetro electrónico (< 500 micrones) y carga por peso exacto en gramos con báscula digital.</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-bold text-slate-900 border border-slate-200">Control Electrónico de Cabina</td>
                            <td class="p-3 text-slate-600 border border-slate-200">Perillas mecánicas con guayas de acero y resistencias en serie para velocidad de ventilador.</td>
                            <td class="p-3 text-slate-800 border border-slate-200 font-medium">Sistemas automáticos Climatronic, servomotores paso a paso de compuertas de mezcla, módulo de potencia PWM de soplador y diagnóstico con escáner.</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </section>

        <!-- SECCIÓN 5: Innovación Tecnológica: Inteligencia Artificial Aplicada -->
        <section class="bg-gradient-to-r from-cyan-950 via-slate-900 to-indigo-950 text-white rounded-2xl p-6 sm:p-8 shadow-xl space-y-6">
            <div class="flex items-center gap-3 border-b border-white/10 pb-4">
                <div class="p-2.5 rounded-lg bg-cyan-500/20 text-cyan-300">
                    <i data-lucide="bot" class="w-6 h-6"></i>
                </div>
                <div>
                    <span class="bg-cyan-500/30 text-cyan-200 text-xs px-2.5 py-0.5 rounded-full font-bold uppercase tracking-wider border border-cyan-400/30">Módulo Adicional / Opcional</span>
                    <h3 class="text-xl font-bold text-white">Innovación Tecnológica: Inteligencia Artificial en Climatización Automotriz</h3>
                </div>
            </div>

            <div class="grid md:grid-cols-3 gap-6">
                <div class="bg-white/10 backdrop-blur rounded-xl p-5 border border-white/10 space-y-3">
                    <div class="text-cyan-300 font-bold text-sm flex items-center gap-2">
                        <i data-lucide="sliders" class="w-4 h-4"></i>
                        Diagnóstico Termodinámico Inteligente de Presiones y Temperaturas
                    </div>
                    <p class="text-xs text-slate-200 leading-relaxed">
                        Manómetros digitales conectados por Bluetooth que transmiten las presiones de alta y baja simultáneamente con temperaturas de línea, calculando mediante IA el subenfriamiento y sobrecalentamiento para diagnosticar válvulas de expansión atascadas.
                    </p>
                    <div class="pt-2 border-t border-white/10 text-[11px] text-cyan-200 font-mono">
                        Herramienta: Testo Smart Probes AI / Fieldpiece HVAC Assistant.
                    </div>
                </div>

                <div class="bg-white/10 backdrop-blur rounded-xl p-5 border border-white/10 space-y-3">
                    <div class="text-cyan-300 font-bold text-sm flex items-center gap-2">
                        <i data-lucide="camera" class="w-4 h-4"></i>
                        Detección Óptica Asistida por IA de Microfugas con Tinte Fluorescente
                    </div>
                    <p class="text-xs text-slate-200 leading-relaxed">
                        Cámaras especiales con iluminación UV y filtros de visión artificial que detectan microfugas invisibles de refrigerante en condensadores y evaporadores ocultos detrás del tablero de instrumentos.
                    </p>
                    <div class="pt-2 border-t border-white/10 text-[11px] text-cyan-200 font-mono">
                        Herramienta: Tracerline UV Smart Vision / Snap-on LeakSeeker AI.
                    </div>
                </div>

                <div class="bg-white/10 backdrop-blur rounded-xl p-5 border border-white/10 space-y-3">
                    <div class="text-cyan-300 font-bold text-sm flex items-center gap-2">
                        <i data-lucide="database" class="w-4 h-4"></i>
                        Asistente RAG para Cargas Precisas de Gas (g) y Aceite (oz) OEM
                    </div>
                    <p class="text-xs text-slate-200 leading-relaxed">
                        Copilot de consulta rápida para talleres que proporciona al instante la cantidad exacta en gramos de gas R-134a / R-1234yf y el tipo de viscosidad de aceite requerido según el VIN del vehículo, evitando sobrepresiones destructivas.
                    </p>
                    <div class="pt-2 border-t border-white/10 text-[11px] text-cyan-200 font-mono">
                        Herramienta: HVAC Auto Data Copilot / Mitchell1 ProDemand HVAC.
                    </div>
                </div>
            </div>
        </section>

    </main>

    <footer class="bg-white border-t border-slate-200 mt-12 py-6 text-center text-xs text-slate-500">
        Fundación Kinal • Escuela Técnica Superior • Coordinación Académica • Propuesta Curricular Aire Acondicionado Automotriz 2026
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
    (output_dir / 'Aire_Acondicionado_Automotriz_Propuesta.html').write_text(html, encoding='utf-8')
    print('Generated Aire_Acondicionado_Automotriz_Propuesta.html')

# -------------------------------------------------------------
# 6. MECÁNICA DE MOTOCICLETAS (2026_MDMM.xlsx)
# -------------------------------------------------------------
def generate_mdm():
    wb = openpyxl.load_workbook(excel_dir / '2026_MDMM.xlsx', data_only=True)
    tm = wb['Temas Módulos']

    modules_data = []
    for c in range(1, tm.max_column + 1, 2):
        m_name = tm.cell(row=1, column=c).value
        m_num = tm.cell(row=2, column=c).value
        if m_name and str(m_name).strip() not in ['0', '#REF!'] and str(m_num).strip() != 'Módulo 10':
            topics = []
            for r in range(3, tm.max_row + 1):
                val = tm.cell(row=r, column=c).value
                if val and str(val).strip() and str(val).strip() not in ['0', '.', '#REF!']:
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
            category = 'Mecánica de Motocicletas'
            badge = '🟢 Mantener'
            badge_color = 'bg-emerald-100 text-emerald-800'
            reason = 'Fundamento técnico imprescindible para el mantenimiento y reparación integral de vehículos de 2 ruedas.'

            t_lower = t.lower()
            if 'motores de dos tiempos' in t_lower:
                status = 'delete'
                badge = '🔴 Eliminar'
                badge_color = 'bg-red-100 text-red-800'
                category = 'Tecnología 2T Descontinuada'
                reason = '🔴 Eliminar: Motores de dos tiempos descontinuados por regulaciones medioambientales de emisiones en Guatemala; enfocar en motores 4T e inyección electrónica.'
            elif 'lubricación de motores de 2 y 4 tiempos' in t_lower:
                status = 'delete'
                badge = '🔴 Eliminar'
                badge_color = 'bg-red-100 text-red-800'
                category = 'Enfoque Obsoleto'
                reason = '🔴 Eliminar: La mezcla manual de aceite 2T en gasolina está en desuso; concentrar el tiempo en aceites 4T normados JASO MA2 para embragues húmedos.'
            elif 'carburadores' in t_lower or 'sistema de combustible' in t_lower:
                status = 'update'
                badge = '🟡 Actualizar'
                badge_color = 'bg-amber-100 text-amber-800'
                category = 'Inyección Electrónica FI'
                reason = '🟡 Actualizar: Transición intensiva de carburadores hacia Inyección Electrónica (FI), bombas de combustible de alta presión y sensores integrados (TPS/MAP/IAT).'
            elif 'sistema de dirección' in t_lower or 'sistema de frenos' in t_lower or 'suspensión' in t_lower:
                status = 'update'
                badge = '🟡 Actualizar'
                badge_color = 'bg-amber-100 text-amber-800'
                category = 'Frenos ABS y Chasis'
                reason = '🟡 Actualizar: Sistemas antibloqueo ABS monocanal y frenado combinado (CBS), mantenimiento de horquillas telescópicas invertidas (USD) y rodamientos cónicos de dirección.'
            elif 'sistemas eléctricos' in t_lower or 'corrientes, voltajes' in t_lower:
                status = 'update'
                badge = '🟡 Actualizar'
                badge_color = 'bg-amber-100 text-amber-800'
                category = 'Electricidad y Magneto Trifásico'
                reason = '🟡 Actualizar: Pruebas de estator trifásico en corriente alterna, reguladores de voltaje con MOSFET, bobinas de encendido transistorizadas TCI y baterías de gel/AGM.'
            elif 'motores de combustión interna' in t_lower or 'sistema de refrigeración' in t_lower or 'tren de válvulas' in t_lower:
                status = 'update'
                badge = '🟡 Actualizar'
                badge_color = 'bg-amber-100 text-amber-800'
                category = 'Motor de 4 Tiempos Moderno'
                reason = '🟡 Actualizar: Calibración de holgura de válvulas por pastillas (shims) en motores DOHC de 4 válvulas, embrague multidisco bañado en aceite JASO MA2 y cajas secuenciales.'

            mod_topics.append({
                'title': t,
                'status': status,
                'badge': badge,
                'badge_color': badge_color,
                'category': category,
                'reason': reason
            })

        if 'alimentación de combustible' in m_name:
            mod_topics.append({
                'title': '[NUEVO] Inyección Electrónica de Motocicletas (FI) y Diagnóstico con Escáner de 2 Ruedas',
                'status': 'new',
                'badge': '🔵 Propuesta Nueva',
                'badge_color': 'bg-blue-100 text-blue-800',
                'category': 'Tecnología Electrónica de Motos',
                'reason': '🔵 Propuesta Nueva: Diagnóstico con escáner para motos (conectores Euro 4/Euro 5 de 4 y 6 pines), lectura de DTCs y calibración de cuerpo de aceleración en motos Bajaj, Honda y Yamaha.'
            })
        if 'Dirección, Suspensión y Frenos' in m_name:
            mod_topics.append({
                'title': '[NUEVO] Mantenimiento y Purga de Frenos con ABS y CBS en Motocicletas',
                'status': 'new',
                'badge': '🔵 Propuesta Nueva',
                'badge_color': 'bg-blue-100 text-blue-800',
                'category': 'Seguridad Activa en Dos Ruedas',
                'reason': '🔵 Propuesta Nueva: Sustitución de líquido de frenos DOT 4 sin descebar el modulador ABS electrohidráulico, verificación de sensores de rueda y purgado de sistemas CBS.'
            })
        if 'Sistema Eléctrico' in m_name:
            mod_topics.append({
                'title': '[NUEVO] Diagnóstico de Generación Eléctrica Trifásica y Encendido Digital TCI / CDI',
                'status': 'new',
                'badge': '🔵 Propuesta Nueva',
                'badge_color': 'bg-blue-100 text-blue-800',
                'category': 'Sistemas Electrónicos de Encendido',
                'reason': '🔵 Propuesta Nueva: Medición de voltaje pico (Peak Voltage) en bobinas captadoras con adaptador DVA, comprobación de diodos en reguladores y prueba de fuga de corriente parásita.'
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
    <title>Auditoría Curricular y Propuesta: Mecánica de Motocicletas | Kinal 2026</title>
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
                    <i data-lucide="bike" class="w-5 h-5 text-red-400"></i>
                    Mecánica de Motocicletas
                </h1>
            </div>

            <div class="flex items-center gap-2 text-xs no-print">
                <a href="index.html" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition">Portal Maestro</a>
                <a href="Mecanica_Motores_Gasolina_Propuesta.html" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition">Motores</a>
                <a href="Mecanismos_del_Automovil_Propuesta.html" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition">Mecanismos</a>
                <a href="Electromecanica_Automotriz_Propuesta.html" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition">Electromecánica</a>
                <a href="Inyeccion_Electronica_Automotriz_Propuesta.html" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition">Inyección</a>
                <a href="Aire_Acondicionado_Automotriz_Propuesta.html" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition">Aire Acond.</a>
                <span class="px-2.5 py-1.5 rounded-lg bg-red-600 text-white font-bold">Motos</span>
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
                <span>2026_MDMM.xlsx</span>
                <i data-lucide="chevron-right" class="w-3.5 h-3.5"></i>
                <span class="text-red-600 font-semibold">Auditoría Curricular & Propuesta 2026</span>
            </div>
            <h2 class="text-3xl font-extrabold text-slate-900 tracking-tight">
                Auditoría Curricular: Mecánica de Motocicletas (180 Horas)
            </h2>
            <p class="text-slate-600 mt-2 text-base max-w-4xl">
                Modernización integral orientada al parque de motocicletas en Guatemala: Transición hacia <strong>Inyección Electrónica de Combustible (FI)</strong>, diagnóstico con <strong>escáner para motos (Euro 4/5)</strong>, sistemas de frenado con <strong>ABS monocanal y frenado combinado (CBS)</strong>, y diagnóstico eléctrico de estatores trifásicos y encendido TCI.
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
                    <div class="text-xs font-medium text-red-600 uppercase tracking-wider">A Eliminar (Motores 2T Obsoletos)</div>
                </div>
            </div>

            <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm flex items-center gap-4">
                <div class="w-12 h-12 rounded-lg bg-amber-100 flex items-center justify-center text-amber-600 font-bold text-xl">
                    <i data-lucide="refresh-cw" class="w-6 h-6"></i>
                </div>
                <div>
                    <div class="text-2xl font-bold text-slate-900">{count_upd} Temas</div>
                    <div class="text-xs font-medium text-amber-600 uppercase tracking-wider">A Actualizar (Inyección FI / ABS / Shims)</div>
                </div>
            </div>

            <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm flex items-center gap-4">
                <div class="w-12 h-12 rounded-lg bg-blue-100 flex items-center justify-center text-blue-600 font-bold text-xl">
                    <i data-lucide="plus-circle" class="w-6 h-6"></i>
                </div>
                <div>
                    <div class="text-2xl font-bold text-slate-900">{count_new} Temas</div>
                    <div class="text-xs font-medium text-blue-600 uppercase tracking-wider">Nuevos Propuestos (Escáner FI / ABS / TCI)</div>
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
                    Crecimiento exponencial del parque de motocicletas en Guatemala (más de 2.5 millones de unidades registradas) y su acelerada tecnificación con inyección electrónica y frenado seguro.
                </p>
            </div>

            <div class="grid md:grid-cols-3 gap-6 text-sm">
                <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 space-y-3">
                    <div class="font-bold text-slate-900 flex items-center gap-2 text-base">
                        <i data-lucide="fuel" class="w-5 h-5 text-red-600"></i>
                        Masificación de la Inyección Electrónica (FI)
                    </div>
                    <p class="text-slate-600 text-xs leading-relaxed">
                        Marcas líderes en ventas en Guatemala (Bajaj Pulsar, Honda CB, Yamaha FZ, TVS Apache, Suzuki Gixxer) han migrado en un 70% sus modelos de baja y media cilindrada hacia inyección electrónica de combustible (FI). Los talleres empíricos que solo limpian carburadores pierden clientes por no contar con escáner para motos.
                    </p>
                </div>

                <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 space-y-3">
                    <div class="font-bold text-slate-900 flex items-center gap-2 text-base">
                        <i data-lucide="shield-check" class="w-5 h-5 text-amber-600"></i>
                        Seguridad Activa en Frenado (ABS / CBS)
                    </div>
                    <p class="text-slate-600 text-xs leading-relaxed">
                        Debido a normativas de seguridad vial y alta siniestralidad, cada vez más motocicletas de 150cc a 250cc incorporan frenos de disco con modulador ABS monocanal delantero y frenado combinado (CBS). Purgar estos sistemas sin conocer el protocolo adecuado bloquea la bomba y compromete la vida del conductor.
                    </p>
                </div>

                <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 space-y-3">
                    <div class="font-bold text-slate-900 flex items-center gap-2 text-base">
                        <i data-lucide="zap" class="w-5 h-5 text-emerald-600"></i>
                        Sistemas Eléctricos y Encendido Digital TCI
                    </div>
                    <p class="text-slate-600 text-xs leading-relaxed">
                        Las fallas de descarga de batería en motos con luces LED permanentes exigen diagnosticar el alternador magneto trifásico, probar caídas de tensión en diodos del regulador con calor y verificar el voltaje pico de la bobina de pulso con adaptador DVA.
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
                <div><strong>Programa Académico:</strong> Mecánica de Motocicletas (2026_MDMM.xlsx)</div>
                <div><strong>Duración Total:</strong> 180 Horas distribuidas en 6 Módulos de 30 hrs</div>
                <div><strong>Jornadas:</strong> Matutina y Vespertina (Sábados de 8:00 a 12:30 y 13:00 a 17:30 hrs)</div>
                <div><strong>Acreditación:</strong> Diploma de Certificación como Técnico en Mecánica de Motocicletas</div>
                <div class="md:col-span-2"><strong>Perfil de Ingreso:</strong> Personas mayores de 17 años con habilidades básicas de lectura y escritura, y actitud proactiva.</div>
                <div class="md:col-span-2"><strong>Perfil de Egreso:</strong> Competencia para diagnosticar, reparar y dar mantenimiento preventivo y correctivo al motor, frenos, suspensión, transmisión, sistemas eléctricos y de inyección en motocicletas.</div>
            </div>

            <div class="bg-amber-50 border border-amber-300 rounded-xl p-5 space-y-3">
                <h4 class="text-amber-900 font-bold text-sm flex items-center gap-2">
                    <i data-lucide="alert-triangle" class="w-5 h-5 text-amber-600"></i>
                    Diagnóstico Crítico / Anomalías Detectadas en el Archivo Original (2026_MDMM.xlsx)
                </h4>
                <ul class="text-xs text-amber-950 space-y-2 list-disc list-inside leading-relaxed">
                    <li><strong>Error de Fórmula #REF! en Cabecera:</strong> En la hoja de cálculo original, la columna correspondiente al Módulo 10 presenta el error de fórmula <code>#REF!</code> sin contenido válido, evidenciando una fila eliminada o referencia rota en Excel. El programa real se consolida en 6 módulos de 30 horas.</li>
                    <li><strong>Contenido Obsoleto de Motores 2 Tiempos:</strong> El Módulo 5 dedicaba clases a <em>"Motores de dos tiempos"</em> y su lubricación manual, tecnologías descontinuadas por normativas medioambientales en Guatemala.</li>
                    <li><strong>Omisión de Escáner y Frenos ABS en Dos Ruedas:</strong> No se mencionaba el uso de escáneres multimarca para motocicletas (OBD para motos con conectores Euro 4/5) ni los protocolos de servicio a módulos de frenos antibloqueo ABS.</li>
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
                        Total de temas auditados en el pensum original: <strong>{total_orig} temas</strong> desglosados en sus 6 módulos oficiales corregidos.
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
                            <td class="p-3 font-bold text-slate-900 border border-slate-200">Alimentación de Combustible</td>
                            <td class="p-3 text-slate-600 border border-slate-200">Carburadores mecánicos tradicionales de cortina y diafragma exclusivamente.</td>
                            <td class="p-3 text-slate-800 border border-slate-200 font-medium">Sistemas de Inyección Electrónica de Motocicletas (FI), diagnóstico de inyectores, bomba sumergida y sensor híbrido TPS/MAP/IAT.</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-bold text-slate-900 border border-slate-200">Diagnóstico Electrónico</td>
                            <td class="p-3 text-slate-600 border border-slate-200">Procedimientos empíricos basados en destello de códigos de luz de advertencia (Blink codes).</td>
                            <td class="p-3 text-slate-800 border border-slate-200 font-medium">Escáner de diagnóstico para motocicletas multimarca (Euro 4/5), lectura de línea de datos en vivo y aprendizaje de mariposa.</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-bold text-slate-900 border border-slate-200">Sistemas de Frenado</td>
                            <td class="p-3 text-slate-600 border border-slate-200">Frenos mecánicos de tambor y disco convencional sin asistencia electrónica.</td>
                            <td class="p-3 text-slate-800 border border-slate-200 font-medium">Frenos antibloqueo ABS monocanal y frenada combinada CBS, verificación de sensor de rueda y purgado seguro del líquido DOT 4.</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-bold text-slate-900 border border-slate-200">Calibración de Válvulas</td>
                            <td class="p-3 text-slate-600 border border-slate-200">Ajuste exclusivo de tornillo y contratuerca en motores varilleros o con balancines.</td>
                            <td class="p-3 text-slate-800 border border-slate-200 font-medium">Calibración por pastillas o monedas calibradas (shims) con micrómetro para motores modernos OHC y DOHC de altas revoluciones.</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-bold text-slate-900 border border-slate-200">Sistema Eléctrico y Carga</td>
                            <td class="p-3 text-slate-600 border border-slate-200">Pruebas estáticas con bombillo de prueba y multímetro sin simulación de carga.</td>
                            <td class="p-3 text-slate-800 border border-slate-200 font-medium">Medición de voltaje pico (Peak Voltage DVA) de bobina captadora, pruebas de alternador trifásico y comprobación de fuga parásita en mA.</td>
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
                    <h3 class="text-xl font-bold text-white">Innovación Tecnológica: Inteligencia Artificial en Mecánica de Motocicletas</h3>
                </div>
            </div>

            <div class="grid md:grid-cols-3 gap-6">
                <div class="bg-white/10 backdrop-blur rounded-xl p-5 border border-white/10 space-y-3">
                    <div class="text-red-300 font-bold text-sm flex items-center gap-2">
                        <i data-lucide="smartphone" class="w-4 h-4"></i>
                        Escáner Bluetooth IA para Motocicletas con Detección Automática
                    </div>
                    <p class="text-xs text-slate-200 leading-relaxed">
                        Interfaces de bolsillo conectadas al smartphone del mecánico que reconocen automáticamente el protocolo de comunicación de motos Bajaj, Honda, Yamaha o KTM, interpretando códigos de falla en lenguaje técnico comprensible.
                    </p>
                    <div class="pt-2 border-t border-white/10 text-[11px] text-red-200 font-mono">
                        Herramienta: MotoScan AI / OBDSTAR iScan AI.
                    </div>
                </div>

                <div class="bg-white/10 backdrop-blur rounded-xl p-5 border border-white/10 space-y-3">
                    <div class="text-red-300 font-bold text-sm flex items-center gap-2">
                        <i data-lucide="activity" class="w-4 h-4"></i>
                        Diagnóstico Acústico de Holgura de Válvulas y Cadena con Audio IA
                    </div>
                    <p class="text-xs text-slate-200 leading-relaxed">
                        Modelos de audio que escuchan el golpeteo metálico en la culata de la moto para indicar si la válvula de admisión o escape está descalibrada o si el tensor automático de cadena de distribución perdió tensión.
                    </p>
                    <div class="pt-2 border-t border-white/10 text-[11px] text-red-200 font-mono">
                        Herramienta: MotoAcoustic AI Diagnostic / SoundTuner Pro.
                    </div>
                </div>

                <div class="bg-white/10 backdrop-blur rounded-xl p-5 border border-white/10 space-y-3">
                    <div class="text-red-300 font-bold text-sm flex items-center gap-2">
                        <i data-lucide="file-text" class="w-4 h-4"></i>
                        Asistente RAG para Diagramas Eléctricos y Torques de Chasis
                    </div>
                    <p class="text-xs text-slate-200 leading-relaxed">
                        Copilot que entrega al instante diagramas de cableado a color, resistencia de bobinas en ohmios y torques de apriete para tuercas de eje y pernos de biela de motocicletas de marcas del mercado guatemalteco.
                    </p>
                    <div class="pt-2 border-t border-white/10 text-[11px] text-red-200 font-mono">
                        Herramienta: MotoData Copilot / Haynes Motorcycle AI.
                    </div>
                </div>
            </div>
        </section>

    </main>

    <footer class="bg-white border-t border-slate-200 mt-12 py-6 text-center text-xs text-slate-500">
        Fundación Kinal • Escuela Técnica Superior • Coordinación Académica • Propuesta Curricular Mecánica de Motocicletas 2026
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
    (output_dir / 'Mecanica_de_Motocicletas_Propuesta.html').write_text(html, encoding='utf-8')
    print('Generated Mecanica_de_Motocicletas_Propuesta.html')

generate_aaa()
generate_mdm()
