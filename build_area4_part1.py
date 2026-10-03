import openpyxl
from pathlib import Path

excel_dir = Path('/Users/arqovalle/Library/CloudStorage/OneDrive-Personal/Software/Antigravity/Cuentas Kinal/Programas de Curso')
output_dir = Path('Revision_Temarios')

# -------------------------------------------------------------
# 1. MECÁNICA DE MOTORES DE GASOLINA (2026_MMGM.xlsx)
# -------------------------------------------------------------
def generate_mmg():
    wb = openpyxl.load_workbook(excel_dir / '2026_MMGM.xlsx', data_only=True)
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
            category = 'Mecánica de Motores'
            badge = '🟢 Mantener'
            badge_color = 'bg-emerald-100 text-emerald-800'
            reason = 'Fundamento metrológico y reconstructivo indispensable para el ajuste y reacondicionamiento mecánico del bloque, culata y tren alternativo.'

            t_lower = t.lower()
            if 'principios de electromagnetismo' in t_lower and 'módulo 7' in m_num.lower():
                status = 'delete'
                badge = '🔴 Eliminar'
                badge_color = 'bg-red-100 text-red-800'
                category = 'Contenido Duplicado'
                reason = '🔴 Eliminar: Teoría física duplicada que corresponde al curso específico de Electromecánica Automotriz; en motores debe priorizarse el ajuste de válvulas y holguras.'
            elif 'componentes del encendido convencional' in t_lower and 'módulo 9' in m_num.lower():
                status = 'delete'
                badge = '🔴 Eliminar'
                badge_color = 'bg-red-100 text-red-800'
                category = 'Tecnología de Platinos Obsoleta'
                reason = '🔴 Eliminar: El encendido por distribuidor convencional y platinos está descontinuado en los vehículos del parque automotriz de Guatemala desde hace 30 años.'
            elif 'puesta a tiempo' in t_lower or 'cambio de faja o cadena' in t_lower:
                status = 'update'
                badge = '🟡 Actualizar'
                badge_color = 'bg-amber-100 text-amber-800'
                category = 'Distribución Variable (VVT)'
                reason = '🟡 Actualizar: Incorporar sincronización de árboles de levas con actuadores electrohidráulicos variables (VVT-i, VTEC, VANOS) y uso de trabadores de calado específicos por marca.'
            elif 'causas de pérdida de compresión' in t_lower or 'diagnóstico de fallas' in t_lower:
                status = 'update'
                badge = '🟡 Actualizar'
                badge_color = 'bg-amber-100 text-amber-800'
                category = 'Diagnóstico Moderno de Cilindros'
                reason = '🟡 Actualizar: Diagnóstico con probador neumático de fugas de cilindro (Cylinder Leakage Tester) con manómetro diferencial y prueba de compresión relativa con osciloscopio.'
            elif 'especificaciones de la culata' in t_lower or 'culata y empaque' in t_lower:
                status = 'update'
                badge = '🟡 Actualizar'
                badge_color = 'bg-amber-100 text-amber-800'
                category = 'Metrología de Precisión'
                reason = '🟡 Actualizar: Medición de planitud con regla de precisión y galgas de espesor (< 0.05 mm), rugosidad superficial (Ra) para empaques metálicos multicapa (MLS) y apriete angular con goniómetro (Torque-to-Yield).'
            elif 'función del cigüeñal' in t_lower or 'especificaciones del cigüeñal y bielas' in t_lower:
                status = 'update'
                badge = '🟡 Actualizar'
                badge_color = 'bg-amber-100 text-amber-800'
                category = 'Ajuste de Cojinetes'
                reason = '🟡 Actualizar: Medición de holgura de aceite con hilo plástico calibrado (Plastigage), alineación de bancadas y medición de ovalamiento y conicidad con micrómetro de exteriores.'

            mod_topics.append({
                'title': t,
                'status': status,
                'badge': badge,
                'badge_color': badge_color,
                'category': category,
                'reason': reason
            })

        if 'Sistema de Distribución' in m_name:
            mod_topics.append({
                'title': '[NUEVO] Diagnóstico y Calibración de Sistemas de Distribución Variable (VVT-i, VTEC, VANOS)',
                'status': 'new',
                'badge': '🔵 Propuesta Nueva',
                'badge_color': 'bg-blue-100 text-blue-800',
                'category': 'Tecnología de Distribución Dinámica',
                'reason': '🔵 Propuesta Nueva: Diagnóstico de válvulas solenoides de control de aceite (OCV), desgaste en piñones variadores de fase y códigos de desfasamiento P0011/P0016.'
            })
        if 'Diagnóstico de Fallas' in m_name:
            mod_topics.append({
                'title': '[NUEVO] Prueba de Fuga de Cilindros por Presión Diferencial y Compresión Relativa',
                'status': 'new',
                'badge': '🔵 Propuesta Nueva',
                'badge_color': 'bg-blue-100 text-blue-800',
                'category': 'Diagnóstico No Invasivo',
                'reason': '🔵 Propuesta Nueva: Localización exacta de fugas hacia válvulas de admisión, escape, anillos o empaque de culata mediante probador neumático y pinza amperimétrica.'
            })
        if 'Combustible Gasolina' in m_name:
            mod_topics.append({
                'title': '[NUEVO] Motores de Inyección Directa (GDI) y Motores de Ciclo Atkinson para Vehículos Híbridos',
                'status': 'new',
                'badge': '🔵 Propuesta Nueva',
                'badge_color': 'bg-blue-100 text-blue-800',
                'category': 'Eficiencia Térmica e Híbridos',
                'reason': '🔵 Propuesta Nueva: Particularidades mecánicas de motores GDI de alta compresión, descarbonización química de válvulas de admisión y gestión térmica en motores Atkinson (Toyota Prius/Corolla Hybrid).'
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
    <title>Auditoría Curricular y Propuesta: Mecánica de Motores de Gasolina | Kinal 2026</title>
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
                    <i data-lucide="cog" class="w-5 h-5 text-red-400"></i>
                    Mecánica de Motores de Gasolina
                </h1>
            </div>

            <div class="flex items-center gap-2 text-xs no-print">
                <a href="index.html" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition">Portal Maestro</a>
                <span class="px-2.5 py-1.5 rounded-lg bg-red-600 text-white font-bold">MMG</span>
                <a href="Mecanismos_del_Automovil_Propuesta.html" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition">Mecanismos</a>
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
                <span>2026_MMGM.xlsx</span>
                <i data-lucide="chevron-right" class="w-3.5 h-3.5"></i>
                <span class="text-red-600 font-semibold">Auditoría Curricular & Propuesta 2026</span>
            </div>
            <h2 class="text-3xl font-extrabold text-slate-900 tracking-tight">
                Auditoría Curricular: Mecánica de Motores de Gasolina (180 Horas)
            </h2>
            <p class="text-slate-600 mt-2 text-base max-w-4xl">
                Alineación con el parque vehicular moderno en Guatemala: Sistemas de Distribución Variable (VVT-i, VTEC, VANOS), diagnóstico diferencial de fugas de cilindro, metrología de culatas para empaques multicapa MLS, apriete angular por deformación plástica (TTY), inyección directa GDI y motores de ciclo Atkinson para vehículos híbridos.
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
                    <div class="text-xs font-medium text-red-600 uppercase tracking-wider">A Eliminar (Platinos / Duplicados)</div>
                </div>
            </div>

            <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm flex items-center gap-4">
                <div class="w-12 h-12 rounded-lg bg-amber-100 flex items-center justify-center text-amber-600 font-bold text-xl">
                    <i data-lucide="refresh-cw" class="w-6 h-6"></i>
                </div>
                <div>
                    <div class="text-2xl font-bold text-slate-900">{count_upd} Temas</div>
                    <div class="text-xs font-medium text-amber-600 uppercase tracking-wider">A Actualizar (VVT / Fugas / Plastigage)</div>
                </div>
            </div>

            <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm flex items-center gap-4">
                <div class="w-12 h-12 rounded-lg bg-blue-100 flex items-center justify-center text-blue-600 font-bold text-xl">
                    <i data-lucide="plus-circle" class="w-6 h-6"></i>
                </div>
                <div>
                    <div class="text-2xl font-bold text-slate-900">{count_new} Temas</div>
                    <div class="text-xs font-medium text-blue-600 uppercase tracking-wider">Nuevos Propuestos (VVT / GDI / Atkinson)</div>
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
                    Realidad técnica en talleres de servicio multimarca, agencias de vehículos y flotas comerciales en Guatemala frente a motores de alta eficiencia y bajas emisiones.
                </p>
            </div>

            <div class="grid md:grid-cols-3 gap-6 text-sm">
                <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 space-y-3">
                    <div class="font-bold text-slate-900 flex items-center gap-2 text-base">
                        <i data-lucide="refresh-cw" class="w-5 h-5 text-red-600"></i>
                        Sistemas de Sincronización Variable (VVT)
                    </div>
                    <p class="text-slate-600 text-xs leading-relaxed">
                        Prácticamente el 100% de los motores de gasolina que ingresan a talleres en Guatemala cuentan con sincronización variable de válvulas (VVT-i de Toyota, i-VTEC de Honda, Dual CVVT de Hyundai/Kia). Los mecánicos cometen graves errores al sincronizar a ojo sin trabadores especiales o al diagnosticar fallas de solenoides de aceite OCV como averías mecánicas mayores.
                    </p>
                </div>

                <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 space-y-3">
                    <div class="font-bold text-slate-900 flex items-center gap-2 text-base">
                        <i data-lucide="ruler" class="w-5 h-5 text-amber-600"></i>
                        Metrología Rigurosa y Empaques MLS
                    </div>
                    <p class="text-slate-600 text-xs leading-relaxed">
                        Los motores modernos con bloques y culatas de aluminio utilizan empaques de culata metálicos multicapa (MLS) que toleran cero deformación (< 0.05 mm) y exigen rugosidades superficiales de espejo. La práctica empírica de lijar culatas a mano o apretar pernos sin goniómetro angular causa soplado de empaque inmediato.
                    </p>
                </div>

                <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 space-y-3">
                    <div class="font-bold text-slate-900 flex items-center gap-2 text-base">
                        <i data-lucide="zap" class="w-5 h-5 text-emerald-600"></i>
                        Auge de Motores GDI y Ciclo Atkinson (Híbridos)
                    </div>
                    <p class="text-slate-600 text-xs leading-relaxed">
                        Con la masiva importación de vehículos híbridos (Toyota Prius, Corolla Cross, Hyundai Ioniq) y autos con inyección directa de gasolina (GDI), el mecánico debe dominar el retardo en el cierre de la válvula de admisión característico del ciclo Atkinson y los problemas de acumulación de carbón en válvulas.
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
                <div><strong>Programa Académico:</strong> Mecánica de Motores de Gasolina (2026_MMGM.xlsx)</div>
                <div><strong>Duración Total:</strong> 180 Horas distribuidas en 10 Módulos de taller práctico</div>
                <div><strong>Jornadas:</strong> Matutina y Vespertina (Sábados de 8:00 a 12:30 y 13:00 a 17:30 hrs)</div>
                <div><strong>Acreditación:</strong> Diploma Técnico en Reparación de Motores de Gasolina</div>
                <div class="md:col-span-2"><strong>Perfil de Ingreso:</strong> Tercer grado de educación básica, destreza manual y vocación por la reparación automotriz.</div>
                <div class="md:col-span-2"><strong>Perfil de Egreso:</strong> Competencia para diagnosticar, desarmar, evaluar desgastes por metrología, reconstruir y calibrar motores de combustión interna de 4 tiempos a gasolina.</div>
            </div>

            <div class="bg-amber-50 border border-amber-300 rounded-xl p-5 space-y-3">
                <h4 class="text-amber-900 font-bold text-sm flex items-center gap-2">
                    <i data-lucide="alert-triangle" class="w-5 h-5 text-amber-600"></i>
                    Diagnóstico Crítico / Anomalías Detectadas en el Archivo Original (2026_MMGM.xlsx)
                </h4>
                <ul class="text-xs text-amber-950 space-y-2 list-disc list-inside leading-relaxed">
                    <li><strong>Solapamiento Excesivo con Cursos Especializados:</strong> Los Módulos 7, 8, 9 y 10 (casi el 40% del tiempo) repiten conceptos de electricidad básica, conector OBDII y sistema de combustible que ya forman parte medular de los cursos <em>Electromecánica Automotriz</em> e <em>Inyección Electrónica</em>. Esto resta valiosas horas al mecanizado, metrología y ajuste fino de componentes internos del motor.</li>
                    <li><strong>Tecnología Anacrónica en Encendido:</strong> Módulo 9 lista <em>"Componentes del encendido convencional"</em>, cuando los distribuidores mecánicos de platinos y condensador no forman parte del parque automotor moderno en Guatemala.</li>
                    <li><strong>Omisión de la Distribución Variable (VVT) y Motores Híbridos:</strong> El temario original no mencionaba actuadores de fase de levas, válvulas OCV ni la creciente presencia de motores de ciclo Atkinson acoplados a transmisiones híbridas.</li>
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
                            <td class="p-3 font-bold text-slate-900 border border-slate-200">Distribución y Tiempo</td>
                            <td class="p-3 text-slate-600 border border-slate-200">Sincronización fija tradicional de árbol de levas único o doble sin actuadores dinámicos.</td>
                            <td class="p-3 text-slate-800 border border-slate-200 font-medium">Sistemas de distribución variable continua (VVT-i, VTEC, VANOS), diagnóstico de válvulas OCV y trabadores de bloqueo.</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-bold text-slate-900 border border-slate-200">Diagnóstico de Compresión</td>
                            <td class="p-3 text-slate-600 border border-slate-200">Manómetro de compresión simple con motor arrancado que no aísla el punto exacto de fuga.</td>
                            <td class="p-3 text-slate-800 border border-slate-200 font-medium">Prueba neumática de fuga de cilindros por presión diferencial y compresión relativa no invasiva mediante osciloscopio digital.</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-bold text-slate-900 border border-slate-200">Metrología de Culata</td>
                            <td class="p-3 text-slate-600 border border-slate-200">Inspección visual y torqueo tradicional en libras-pie con torquímetro de truene.</td>
                            <td class="p-3 text-slate-800 border border-slate-200 font-medium">Medición de planitud y rugosidad Ra para empaques MLS, apriete angular en grados (Torque-to-Yield) y tornillos elásticos nuevos.</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-bold text-slate-900 border border-slate-200">Ajuste de Cigüeñal</td>
                            <td class="p-3 text-slate-600 border border-slate-200">Armado empírico según tacto del mecánico al girar la polea.</td>
                            <td class="p-3 text-slate-800 border border-slate-200 font-medium">Verificación micrométrica de huelgo de película de aceite con Plastigage (0.025-0.050 mm) y verificación de holgura axial de bancada.</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-bold text-slate-900 border border-slate-200">Nuevas Tecnologías de Motor</td>
                            <td class="p-3 text-slate-600 border border-slate-200">Estudio exclusivo de motores multipunto convencionales MPFI de inyección indirecta.</td>
                            <td class="p-3 text-slate-800 border border-slate-200 font-medium">Motores de inyección directa GDI a alta presión y motores térmicos de ciclo Atkinson acoplados a trenes motrices híbridos.</td>
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
                    <h3 class="text-xl font-bold text-white">Innovación Tecnológica: Inteligencia Artificial en Motores de Gasolina</h3>
                </div>
            </div>

            <div class="grid md:grid-cols-3 gap-6">
                <div class="bg-white/10 backdrop-blur rounded-xl p-5 border border-white/10 space-y-3">
                    <div class="text-red-300 font-bold text-sm flex items-center gap-2">
                        <i data-lucide="camera" class="w-4 h-4"></i>
                        Inspección Endoscópica de Cilindros con Visión Artificial
                    </div>
                    <p class="text-xs text-slate-200 leading-relaxed">
                        Videoscopios articulados con IA que reconocen automáticamente rayaduras en la pared del cilindro, depósitos de carbón en válvulas de admisión GDI y huellas de pistoneo sin desmontar la culata.
                    </p>
                    <div class="pt-2 border-t border-white/10 text-[11px] text-red-200 font-mono">
                        Herramienta: Autel MaxiVideo AI / Bosch Borescope Vision.
                    </div>
                </div>

                <div class="bg-white/10 backdrop-blur rounded-xl p-5 border border-white/10 space-y-3">
                    <div class="text-red-300 font-bold text-sm flex items-center gap-2">
                        <i data-lucide="activity" class="w-4 h-4"></i>
                        Diagnóstico Acústico de Ruidos de Motor con Redes Neuronales
                    </div>
                    <p class="text-xs text-slate-200 leading-relaxed">
                        Aplicaciones en smartphone que graban el sonido del motor en ralentí y aceleración para diferenciar al instante un taqué hidráulico descargado, golpeteo de pasador de biela o cascabeleo de preignición.
                    </p>
                    <div class="pt-2 border-t border-white/10 text-[11px] text-red-200 font-mono">
                        Herramienta: Engine Sound AI Diagnostic / Škoda Sound Analyser.
                    </div>
                </div>

                <div class="bg-white/10 backdrop-blur rounded-xl p-5 border border-white/10 space-y-3">
                    <div class="text-red-300 font-bold text-sm flex items-center gap-2">
                        <i data-lucide="book-open" class="w-4 h-4"></i>
                        Asistente RAG para Especificaciones de Torque y Calado OEM
                    </div>
                    <p class="text-xs text-slate-200 leading-relaxed">
                        Copilot de consulta rápida conectado a bases de datos de fabricantes (AllData, Mitchell1, Autodata) para obtener en segundos secuencias exactas de apriete, tolerancias de pistón y diagramas de distribución.
                    </p>
                    <div class="pt-2 border-t border-white/10 text-[11px] text-red-200 font-mono">
                        Herramienta: Automotive Repair Copilot / Mitchell1 ProDemand AI.
                    </div>
                </div>
            </div>
        </section>

    </main>

    <footer class="bg-white border-t border-slate-200 mt-12 py-6 text-center text-xs text-slate-500">
        Fundación Kinal • Escuela Técnica Superior • Dirección Académica • Propuesta Curricular Mecánica de Motores de Gasolina 2026
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
    (output_dir / 'Mecanica_Motores_Gasolina_Propuesta.html').write_text(html, encoding='utf-8')
    print('Generated Mecanica_Motores_Gasolina_Propuesta.html')

generate_mmg()
