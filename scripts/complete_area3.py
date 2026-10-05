import openpyxl
from pathlib import Path

excel_dir = Path('/Users/arqovalle/Library/CloudStorage/OneDrive-Personal/Software/Antigravity/Cuentas Kinal/Programas de Curso')
output_dir = Path('Revision_Temarios')

# -------------------------------------------------------------
# 3. CALDERAS DE VAPOR (2025_CV.xlsx)
# -------------------------------------------------------------
def generate_cv():
    wb = openpyxl.load_workbook(excel_dir / '2025_CV.xlsx', data_only=True)
    tm = wb['Temas Módulos']

    modules_data = []
    for c in range(1, 11, 2):  # Only first 5 modules (cols 1, 3, 5, 7, 9)
        m_name = tm.cell(row=1, column=c).value
        m_num = tm.cell(row=2, column=c).value
        if m_name and str(m_name).strip() != '0':
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
            category = 'Operación y Termodinámica'
            badge = '🟢 Mantener'
            badge_color = 'bg-emerald-100 text-emerald-800'
            reason = 'Principio operativo y termodinámico esencial para la generación y aprovechamiento seguro del vapor industrial.'

            t_lower = t.lower()
            if 'método de la pluma' in t_lower:
                status = 'delete'
                badge = '🔴 Eliminar'
                badge_color = 'bg-red-100 text-red-800'
                category = 'Método Empírico Arcaico'
                reason = '🔴 Eliminar: Estimación visual subjetiva del humo en chimenea; sustituir por análisis digital estequiométrico con analizadores de gases (%O2, CO, ppm de NOx).'
            elif 'examen final de módulo' in t_lower:
                status = 'delete'
                badge = '🔴 Eliminar'
                badge_color = 'bg-red-100 text-red-800'
                category = 'Hito Administrativo'
                reason = '🔴 Eliminar: Hito de evaluación sumativa institucional que no constituye materia técnica de aprendizaje.'
            elif 'quemador y sus sistemas de control' in t_lower or 'modulación del fogueo' in t_lower:
                status = 'update'
                badge = '🟡 Actualizar'
                badge_color = 'bg-amber-100 text-amber-800'
                category = 'Combustión Electrónica'
                reason = '🟡 Actualizar: Quemadores modulantes con servomotores electrónicos independientes de aire/combustible (enlace digital Siemens LMV / Autoflame) y detección UV/IR de llama.'
            elif 'tratamiento interno del agua' in t_lower or 'análisis químico del agua' in t_lower or 'problemas de corrosión' in t_lower:
                status = 'update'
                badge = '🟡 Actualizar'
                badge_color = 'bg-amber-100 text-amber-800'
                category = 'Química del Agua ASME'
                reason = '🟡 Actualizar: Estándares ASME Consensus para agua de calderas: control de sulfitos (secuestrante de O2), fosfatos (dispersante de lodos), aminas neutralizantes y purga automática por conductividad.'
            elif 'análisis de combustión' in t_lower or 'eficiencia de la caldera' in t_lower:
                status = 'update'
                badge = '🟡 Actualizar'
                badge_color = 'bg-amber-100 text-amber-800'
                category = 'Eficiencia Térmica'
                reason = '🟡 Actualizar: Cálculo de rendimiento térmico por métodos directo e indirecto (ASME PTC 4) y optimización del exceso de aire con monitoreo continuo de oxígeno.'
            elif 'tipos de trampas de vapor' in t_lower or 'criterios para seleccionar una trampa' in t_lower or 'sistema de trampeo' in t_lower:
                status = 'update'
                badge = '🟡 Actualizar'
                badge_color = 'bg-amber-100 text-amber-800'
                category = 'Gestión de Condensados'
                reason = '🟡 Actualizar: Selección técnica de trampas mecánicas de flotador termostático (para intercambiadores) y termodinámicas (para líneas principales) y diagnóstico de golpe de ariete.'

            mod_topics.append({
                'title': t,
                'status': status,
                'badge': badge,
                'badge_color': badge_color,
                'category': category,
                'reason': reason
            })

        if 'Operación de calderas I' in m_name:
            mod_topics.append({
                'title': '[NUEVO] Marco Regulatorio y Legal de Calderas ante el MinTrab (Guatemala)',
                'status': 'new',
                'badge': '🔵 Propuesta Nueva',
                'badge_color': 'bg-blue-100 text-blue-800',
                'category': 'Regulación Legal Obligatoria',
                'reason': '🔵 Propuesta Nueva: Requisitos legales del Reglamento de Calderas del Ministerio de Trabajo: bitácora oficial foliada, inspecciones anuales, protocolos de prueba hidrostática y certificación de fogoneros.'
            })
        if 'Distribución de vapor' in m_name:
            mod_topics.append({
                'title': '[NUEVO] Diagnóstico por Ultrasonido y Termografía de Trampas de Vapor',
                'status': 'new',
                'badge': '🔵 Propuesta Nueva',
                'badge_color': 'bg-blue-100 text-blue-800',
                'category': 'Auditoría Energética de Vapor',
                'reason': '🔵 Propuesta Nueva: Detección en tiempo real de trampas falladas abiertas (pérdida masiva de vapor vivo en kg/h) y trampas cerradas (acumulación de condensado frío y riesgo de explosión por ariete).'
            })
        if 'Eficiencia energética' in m_name:
            mod_topics.append({
                'title': '[NUEVO] Recuperación de Calor de Purga y Economizadores en Chimenea',
                'status': 'new',
                'badge': '🔵 Propuesta Nueva',
                'badge_color': 'bg-blue-100 text-blue-800',
                'category': 'Descarbonización y Ahorro de Combustible',
                'reason': '🔵 Propuesta Nueva: Dimensionamiento de economizadores para aumentar la temperatura del agua de alimentación en 5 °C por cada 1% de combustible ahorrado y tanques flash de purga continua.'
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
    <title>Auditoría Curricular y Propuesta: Calderas de Vapor | Kinal 2026</title>
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
                <a href="index.html" title="Ir al Portal Maestro" class="bg-blue-600 hover:bg-blue-500 text-white font-bold text-xs uppercase px-2.5 py-1 rounded transition cursor-pointer">Kinal ETS 2026</a>
                <span class="text-slate-500 text-sm hidden sm:inline">|</span>
                <h1 class="text-base sm:text-lg font-semibold tracking-tight text-white flex items-center gap-2">
                    <i data-lucide="gauge" class="w-5 h-5 text-blue-400"></i>
                    Calderas de Vapor
                </h1>
            </div>

            <div class="flex items-center gap-2 text-xs no-print">
                <a href="index.html" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition">Portal Maestro</a>
                <a href="Mantenimiento_Mecanico_Industrial_Propuesta.html" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition">Mant. Mecánico</a>
                <a href="Soldadura_Industrial_Propuesta.html" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition">Soldadura Ind.</a>
                <span class="px-2.5 py-1.5 rounded-lg bg-blue-600 text-white font-bold">CV</span>
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
                <span>2025_CV.xlsx</span>
                <i data-lucide="chevron-right" class="w-3.5 h-3.5"></i>
                <span class="text-blue-600 font-semibold">Auditoría Curricular & Propuesta 2026</span>
            </div>
            <h2 class="text-3xl font-extrabold text-slate-900 tracking-tight">
                Auditoría Curricular: Calderas de Vapor (180 Horas)
            </h2>
            <p class="text-slate-600 mt-2 text-base max-w-4xl">
                Alineación rigurosa con el <strong>Reglamento de Calderas del MinTrab</strong> (Guatemala), tratamiento químico de agua bajo estándar <strong>ASME Consensus</strong>, combustión electrónica con quemadores modulantes, auditoría acústica/térmica de trampas de vapor y recuperación de calor de purgas.
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
                    <div class="text-xs font-medium text-red-600 uppercase tracking-wider">A Eliminar (Pluma / Evaluaciones)</div>
                </div>
            </div>

            <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm flex items-center gap-4">
                <div class="w-12 h-12 rounded-lg bg-amber-100 flex items-center justify-center text-amber-600 font-bold text-xl">
                    <i data-lucide="refresh-cw" class="w-6 h-6"></i>
                </div>
                <div>
                    <div class="text-2xl font-bold text-slate-900">{count_upd} Temas</div>
                    <div class="text-xs font-medium text-amber-600 uppercase tracking-wider">A Actualizar (Modulación/ASME/Trampas)</div>
                </div>
            </div>

            <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm flex items-center gap-4">
                <div class="w-12 h-12 rounded-lg bg-blue-100 flex items-center justify-center text-blue-600 font-bold text-xl">
                    <i data-lucide="plus-circle" class="w-6 h-6"></i>
                </div>
                <div>
                    <div class="text-2xl font-bold text-slate-900">{count_new} Temas</div>
                    <div class="text-xs font-medium text-blue-600 uppercase tracking-wider">Nuevos Propuestos (MinTrab / Ultrasonido / Flash)</div>
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
                <span class="text-xs font-bold uppercase tracking-wider text-blue-600 bg-blue-50 px-2.5 py-1 rounded-full border border-blue-200">Sección 1</span>
                <h3 class="text-xl font-bold text-slate-900 mt-2 flex items-center gap-2">
                    <i data-lucide="trending-up" class="w-5 h-5 text-blue-600"></i>
                    Contexto Industrial y Demanda Laboral en Guatemala (2026)
                </h3>
                <p class="text-slate-600 text-sm mt-1">
                    Operación crítica de generación de vapor en plantas textiles, ingenios azucareros, industria de alimentos, farmacéutica, bebidas y beneficio de café en Guatemala.
                </p>
            </div>

            <div class="grid md:grid-cols-3 gap-6 text-sm">
                <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 space-y-3">
                    <div class="font-bold text-slate-900 flex items-center gap-2 text-base">
                        <i data-lucide="scale" class="w-5 h-5 text-blue-600"></i>
                        Cumplimiento Legal MinTrab (Inspección y Fogoneros)
                    </div>
                    <p class="text-slate-600 text-xs leading-relaxed">
                        El Ministerio de Trabajo y Previsión Social de Guatemala exige mediante su Reglamento de Calderas que toda caldera cuente con operadores certificados (fogoneros), bitácora de operación diaria foliada, pruebas hidrostáticas periódicas y válvulas de seguridad calibradas. No cumplir acarrea clausura inmediata y responsabilidad penal.
                    </p>
                </div>

                <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 space-y-3">
                    <div class="font-bold text-slate-900 flex items-center gap-2 text-base">
                        <i data-lucide="droplet" class="w-5 h-5 text-amber-600"></i>
                        Química del Agua y Prevención de Explosiones
                    </div>
                    <p class="text-slate-600 text-xs leading-relaxed">
                        Un espesor de solo 1 mm de incrustación calcárea en los tubos incrementa el consumo de combustible en un 5% y provoca el sobrecalentamiento del metal hasta la rotura explosiva. Se demanda formación analítica en pruebas de campo diarias de dureza, alcalinidad, fosfatos y ciclos de concentración.
                    </p>
                </div>

                <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 space-y-3">
                    <div class="font-bold text-slate-900 flex items-center gap-2 text-base">
                        <i data-lucide="dollar-sign" class="w-5 h-5 text-emerald-600"></i>
                        Auditoría Energética de Redes de Vapor y Trampas
                    </div>
                    <p class="text-slate-600 text-xs leading-relaxed">
                        Una sola trampa de vapor termodinámica abierta en un ramal de 100 psi puede desperdiciar más de USD $8,000 anuales en combustible búnker/diésel. Los técnicos deben dominar la auditoría por ultrasonido y cámaras térmicas para certificar el retorno de condensado caliente al desaireador.
                    </p>
                </div>
            </div>
        </section>

        <!-- SECCIÓN 2: Ficha Oficial de Venta y Diagnóstico Crítico -->
        <section class="bg-white rounded-2xl border border-slate-200 p-6 sm:p-8 shadow-sm space-y-6">
            <div class="border-b border-slate-100 pb-4">
                <span class="text-xs font-bold uppercase tracking-wider text-blue-600 bg-blue-50 px-2.5 py-1 rounded-full border border-blue-200">Sección 2</span>
                <h3 class="text-xl font-bold text-slate-900 mt-2 flex items-center gap-2">
                    <i data-lucide="file-spreadsheet" class="w-5 h-5 text-blue-600"></i>
                    Ficha Oficial de Venta ("Reporte") y Diagnóstico Crítico de Anomalías
                </h3>
            </div>

            <div class="grid md:grid-cols-2 gap-4 text-xs sm:text-sm text-slate-700 bg-slate-50 p-4 rounded-xl border border-slate-200">
                <div><strong>Programa Académico:</strong> Calderas de Vapor (2025_CV.xlsx)</div>
                <div><strong>Duración Total:</strong> 180 Horas distribuidas en 5 Unidades modulares de 36 hrs</div>
                <div><strong>Jornadas:</strong> Matutina y Vespertina (Sábados de 8:00 a 12:30 y 13:00 a 17:30 hrs)</div>
                <div><strong>Acreditación:</strong> Diploma Técnico en Calderas de Vapor / Operador Certificado</div>
                <div class="md:col-span-2"><strong>Perfil de Ingreso:</strong> Tercer grado de educación básica, interés en plantas térmicas, física del calor y operaciones de sala de máquinas.</div>
                <div class="md:col-span-2"><strong>Perfil de Egreso:</strong> Competencia para operar calderas pirotubulares y acuotubulares, supervisar el tratamiento químico del agua, realizar mantenimiento preventivo y optimizar la combustión con seguridad.</div>
            </div>

            <div class="bg-amber-50 border border-amber-300 rounded-xl p-5 space-y-3">
                <h4 class="text-amber-900 font-bold text-sm flex items-center gap-2">
                    <i data-lucide="alert-triangle" class="w-5 h-5 text-amber-600"></i>
                    Diagnóstico Crítico / Anomalías Detectadas en el Archivo Original (2025_CV.xlsx)
                </h4>
                <ul class="text-xs text-amber-950 space-y-2 list-disc list-inside leading-relaxed">
                    <li><strong>Estructura Incompleta en el Excel Original:</strong> El archivo presenta los Módulos 6 al 10 con casillas numéricas <code>0</code> sin contenido, lo que confundía el conteo modular. En realidad, la materia se dosifica en 5 módulos profundos de 36 horas cada uno para completar las 180 horas totales.</li>
                    <li><strong>Método Obsoleto de Estimación de Emisiones:</strong> En el Módulo 4 se incluye <em>"Cálculos de pérdidas: método de la pluma"</em>, una técnica visual que ha sido completamente reemplazada por analizadores digitales de combustión con celdas electroquímicas que miden ppm de CO y exceso de aire.</li>
                    <li><strong>Omisión del Marco Jurídico MinTrab:</strong> No se explicitaba el estudio detallado del Reglamento de Calderas del Ministerio de Trabajo de Guatemala, esencial para que el operador conozca las responsabilidades penales de la operación y el registro en bitácora foliada.</li>
                </ul>
            </div>
        </section>

        <!-- SECCIÓN 3: Distribución Modular Detallada y Auditoría Tema por Tema -->
        <section class="bg-white rounded-2xl border border-slate-200 p-6 sm:p-8 shadow-sm space-y-6">
            <div class="flex flex-wrap justify-between items-center gap-4 border-b border-slate-100 pb-4">
                <div>
                    <span class="text-xs font-bold uppercase tracking-wider text-blue-600 bg-blue-50 px-2.5 py-1 rounded-full border border-blue-200">Sección 3</span>
                    <h3 class="text-xl font-bold text-slate-900 mt-2 flex items-center gap-2">
                        <i data-lucide="list-checks" class="w-5 h-5 text-blue-600"></i>
                        Distribución Modular y Auditoría Analítica Tema por Tema
                    </h3>
                    <p class="text-slate-600 text-sm mt-1">
                        Total de temas auditados en el pensum original: <strong>{total_orig} temas</strong> desglosados en sus 5 módulos oficiales.
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
                            <span class="w-7 h-7 rounded-lg bg-blue-600 text-white font-bold text-xs flex items-center justify-center">{m_num.replace('Módulo ', '') if 'Módulo' in m_num else m_num}</span>
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
                <span class="text-xs font-bold uppercase tracking-wider text-blue-600 bg-blue-50 px-2.5 py-1 rounded-full border border-blue-200">Sección 4</span>
                <h3 class="text-xl font-bold text-slate-900 mt-2 flex items-center gap-2">
                    <i data-lucide="arrow-left-right" class="w-5 h-5 text-blue-600"></i>
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
                            <td class="p-3 font-bold text-slate-900 border border-slate-200">Marco Legal y Seguridad</td>
                            <td class="p-3 text-slate-600 border border-slate-200">Instrucciones generales de operación sin respaldo normativo local.</td>
                            <td class="p-3 text-slate-800 border border-slate-200 font-medium">Cumplimiento del Reglamento de Calderas del MinTrab, bitácora foliada legal y protocolos para prueba hidrostática periódica.</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-bold text-slate-900 border border-slate-200">Control de Combustión</td>
                            <td class="p-3 text-slate-600 border border-slate-200">Varillaje mecánico tradicional de levas con descalibración continua y estimación visual por "método de la pluma".</td>
                            <td class="p-3 text-slate-800 border border-slate-200 font-medium">Quemadores con modulación electrónica mediante servomotores independientes (aire/combustible) y analizador digital de gases (%O2, CO).</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-bold text-slate-900 border border-slate-200">Tratamiento Químico del Agua</td>
                            <td class="p-3 text-slate-600 border border-slate-200">Pruebas aisladas de dureza sin correlación con ciclos de concentración ni control de gases corrosivos.</td>
                            <td class="p-3 text-slate-800 border border-slate-200 font-medium">Parámetros ASME Consensus: control estricto de sulfitos residuales, alcalinidad cáustica, fosfatos y purga automática por conductividad.</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-bold text-slate-900 border border-slate-200">Distribución y Trampeo</td>
                            <td class="p-3 text-slate-600 border border-slate-200">Instalación básica de trampas sin metodología de diagnóstico de fallas.</td>
                            <td class="p-3 text-slate-800 border border-slate-200 font-medium">Auditoría con ultrasonido y termografía de trampas de vapor para evitar pérdida de vapor vivo en kg/h y golpe de ariete destructor.</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-bold text-slate-900 border border-slate-200">Eficiencia Térmica</td>
                            <td class="p-3 text-slate-600 border border-slate-200">Retorno de condensado simple sin recuperación de energía de purgas.</td>
                            <td class="p-3 text-slate-800 border border-slate-200 font-medium">Economizadores de gases de chimenea, tanques flash de revaporizado para purga continua y aislamiento térmico de alta densidad.</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </section>

        <!-- SECCIÓN 5: Innovación Tecnológica: Inteligencia Artificial Aplicada -->
        <section class="bg-gradient-to-r from-blue-900 via-slate-900 to-indigo-950 text-white rounded-2xl p-6 sm:p-8 shadow-xl space-y-6">
            <div class="flex items-center gap-3 border-b border-white/10 pb-4">
                <div class="p-2.5 rounded-lg bg-blue-500/20 text-blue-300">
                    <i data-lucide="bot" class="w-6 h-6"></i>
                </div>
                <div>
                    <span class="bg-blue-500/30 text-blue-200 text-xs px-2.5 py-0.5 rounded-full font-bold uppercase tracking-wider border border-blue-400/30">Módulo Adicional / Opcional</span>
                    <h3 class="text-xl font-bold text-white">Innovación Tecnológica: Inteligencia Artificial en Calderas de Vapor</h3>
                </div>
            </div>

            <div class="grid md:grid-cols-3 gap-6">
                <div class="bg-white/10 backdrop-blur rounded-xl p-5 border border-white/10 space-y-3">
                    <div class="text-blue-300 font-bold text-sm flex items-center gap-2">
                        <i data-lucide="sliders" class="w-4 h-4"></i>
                        Optimización Predictiva de la Relación Aire/Combustible con ML
                    </div>
                    <p class="text-xs text-slate-200 leading-relaxed">
                        Algoritmos que analizan la temperatura ambiente, humedad del aire y la señal de oxígeno en chimenea para ajustar la curva de combustión del quemador en tiempo real, maximizando la eficiencia térmica del generador.
                    </p>
                    <div class="pt-2 border-t border-white/10 text-[11px] text-blue-200 font-mono">
                        Herramienta: Combustion Copilot AI / Yokogawa TDLS AI.
                    </div>
                </div>

                <div class="bg-white/10 backdrop-blur rounded-xl p-5 border border-white/10 space-y-3">
                    <div class="text-blue-300 font-bold text-sm flex items-center gap-2">
                        <i data-lucide="camera" class="w-4 h-4"></i>
                        Auditoría de Aislamiento y Redes de Vapor con Termografía Asistida por IA
                    </div>
                    <p class="text-xs text-slate-200 leading-relaxed">
                        Cámaras térmicas con reconocimiento de patrones que escanean kilómetros de tubería de vapor y calculan automáticamente los dólares perdidos por radiación en válvulas sin chaqueta térmica aislante.
                    </p>
                    <div class="pt-2 border-t border-white/10 text-[11px] text-blue-200 font-mono">
                        Herramienta: FLIR Thermal Studio AI / Spirax Sarco Steam Energy Monitor.
                    </div>
                </div>

                <div class="bg-white/10 backdrop-blur rounded-xl p-5 border border-white/10 space-y-3">
                    <div class="text-blue-300 font-bold text-sm flex items-center gap-2">
                        <i data-lucide="droplet" class="w-4 h-4"></i>
                        Dosificación Química Inteligente y Predicción de Incrustación
                    </div>
                    <p class="text-xs text-slate-200 leading-relaxed">
                        Modelos de machine learning conectados a sondas de conductividad y pH que ajustan automáticamente la inyección de dispersantes y purga de lodos, previniendo arrastres corrosivos de vapor húmedo a la planta.
                    </p>
                    <div class="pt-2 border-t border-white/10 text-[11px] text-blue-200 font-mono">
                        Herramienta: Nalco Water 3D TRASAR AI / Kurita Water Predictor.
                    </div>
                </div>
            </div>
        </section>

    </main>

    <footer class="bg-white border-t border-slate-200 mt-12 py-6 text-center text-xs text-slate-500">
        Fundación Kinal • Escuela Técnica Superior • Coordinación Académica • Propuesta Curricular Calderas de Vapor 2026
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
    (output_dir / 'Calderas_de_Vapor_Propuesta.html').write_text(html, encoding='utf-8')
    print('Generated Calderas_de_Vapor_Propuesta.html')

generate_cv()
