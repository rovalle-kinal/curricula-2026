import openpyxl
from pathlib import Path

excel_dir = Path('/Users/arqovalle/Library/CloudStorage/OneDrive-Personal/Software/Antigravity/Cuentas Kinal/Programas de Curso')
output_dir = Path('Revision_Temarios')

def generate_cme():
    wb = openpyxl.load_workbook(excel_dir / '2025_CMEM.xlsx', data_only=True)
    tm = wb['Temas Módulos']

    # Extract all topics per module
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

    # Classifications for CME
    # Total topics: ~102 clean topics + 3 new topics
    classified_modules = []
    
    for mod in modules_data:
        m_num = mod['num']
        m_name = mod['name']
        mod_topics = []
        for t in mod['topics']:
            status = 'keep'
            category = 'Fundamento Esencial'
            badge = '🟢 Mantener'
            badge_color = 'bg-emerald-100 text-emerald-800'
            reason = 'Concepto electrotécnico fundamental indispensable para la formación de técnicos electricistas industriales en Guatemala.'

            t_lower = t.lower()
            if 'generadores de corriente continua' in t_lower:
                status = 'delete'
                badge = '🔴 Eliminar'
                badge_color = 'bg-red-100 text-red-800'
                category = 'Tecnología en Desuso'
                reason = '🔴 Eliminar: Los generadores de CC (dinamos) están completamente obsoletos en la matriz eléctrica industrial de Guatemala; han sido reemplazados por alternadores de CA sincrónicos y rectificadores de potencia.'
            elif 'bombas monofásicas periféricas domiciliarias' in t_lower:
                status = 'delete'
                badge = '🔴 Eliminar'
                badge_color = 'bg-red-100 text-red-800'
                category = 'Incongruencia de Nivel'
                reason = '🔴 Eliminar: Contenido fontanero/residencial básico desalineado con los objetivos técnicos de un curso de máquinas trifásicas y mandos industriales de alta potencia.'
            elif 'arranque estrella-delta manual' in t_lower:
                status = 'delete'
                badge = '🔴 Eliminar'
                badge_color = 'bg-red-100 text-red-800'
                category = 'Maniobra Insegura'
                reason = '🔴 Eliminar: Los conmutadores manuales estrella-delta presentan alto riesgo de arco eléctrico y fatiga de contactos; se sustituyen por mandos automáticos por contactores y arrancadores de estado sólido.'
            elif 'sistemas trifásicos' in t_lower or 'fundamentos de sistemas' in t_lower:
                status = 'update'
                badge = '🟡 Actualizar'
                badge_color = 'bg-amber-100 text-amber-800'
                category = 'Alineación Normativa CNEE'
                reason = '🟡 Actualizar: Incorporar código de colores normado por el NEC/NTDOID de la CNEE para conductores de fase, neutro y tierra en sistemas 208/120V y 480/277V en Guatemala.'
            elif 'triángulo de potencias' in t_lower or 'potencia trifásica' in t_lower:
                status = 'update'
                badge = '🟡 Actualizar'
                badge_color = 'bg-amber-100 text-amber-800'
                category = 'Gestión Energética'
                reason = '🟡 Actualizar: Calcular penalizaciones por bajo factor de potencia (< 0.90) según el pliego tarifario de grandes usuarios de EEGSA y Energuate, y dimensionar bancos de condensadores.'
            elif 'plantas eléctricas de emergencia' in t_lower or 'conmutación o transferencia' in t_lower:
                status = 'update'
                badge = '🟡 Actualizar'
                badge_color = 'bg-amber-100 text-amber-800'
                category = 'Modernización de Control'
                reason = '🟡 Actualizar: Enfatizar controladores automáticos de transferencia (ATS) microprocesados (Deep Sea / ComAp), precalentadores de motor y monitoreo de baterías.'
            elif 'transformadores trifásicos' in t_lower or 'conexiones de transformadores' in t_lower:
                status = 'update'
                badge = '🟡 Actualizar'
                badge_color = 'bg-amber-100 text-amber-800'
                category = 'Ingeniería de Distribución'
                reason = '🟡 Actualizar: Grupos de conexión (Dyn5, Ynd11), desbalance de neutro, análisis de gases disueltos (DGA) y factor K para cargas con armónicos.'
            elif 'motores trifásicos' in t_lower:
                status = 'update'
                badge = '🟡 Actualizar'
                badge_color = 'bg-amber-100 text-amber-800'
                category = 'Eficiencia Energética'
                reason = '🟡 Actualizar: Normativa de eficiencia IE3/IE4 (Premium Efficiency), interpretación de placas NEMA/IEC y pruebas de aislamiento de devanados con megóhmetro (IEEE 43).'
            elif 'protecciones de sobrecarga' in t_lower:
                status = 'update'
                badge = '🟡 Actualizar'
                badge_color = 'bg-amber-100 text-amber-800'
                category = 'Aparamenta de Protección'
                reason = '🟡 Actualizar: Guardamotores magnetotérmicos de alta capacidad de corte, relés electrónicos de sobrecarga con clase de disparo seleccionable y protección contra pérdida de fase.'
            elif 'arrancadores suaves' in t_lower:
                status = 'update'
                badge = '🟡 Actualizar'
                badge_color = 'bg-amber-100 text-amber-800'
                category = 'Electrónica de Potencia'
                reason = '🟡 Actualizar: Parametrización de tiristores anti-paralelo, control de par en aceleración/desaceleración para bombas (golpe de ariete) y cableado de contactor de bypass.'
            elif 'variador' in t_lower or 'variadores' in t_lower:
                status = 'update'
                badge = '🟡 Actualizar'
                badge_color = 'bg-amber-100 text-amber-800'
                category = 'Accionamientos Modernos'
                reason = '🟡 Actualizar: Programación de rampas, control vectorial sin sensor (Sensorless Vector), entradas multifunción 4-20mA/0-10V, redes de comunicación Modbus/Profinet y frenado dinámico.'
            elif 'sensores' in t_lower or 'lógicas pnp' in t_lower:
                status = 'update'
                badge = '🟡 Actualizar'
                badge_color = 'bg-amber-100 text-amber-800'
                category = 'Instrumentación Discreta'
                reason = '🟡 Actualizar: Conexión segura de sensores industriales inductivos, fotoeléctricos y capacitivos de 2, 3 y 4 hilos NPN/PNP con fuentes conmutadas de 24VDC.'
            elif 'plc' in t_lower:
                status = 'update'
                badge = '🟡 Actualizar'
                badge_color = 'bg-amber-100 text-amber-800'
                category = 'Controladores Lógicos'
                reason = '🟡 Actualizar: Implementación en Siemens LOGO! 8 y S7-1200, cableado de señales sourcing/sinking y mapeo de I/O en tableros industriales.'

            mod_topics.append({
                'title': t,
                'status': status,
                'badge': badge,
                'badge_color': badge_color,
                'category': category,
                'reason': reason
            })
        
        # Add new topics to specific modules
        if 'Variadores de Frecuencia' in m_name:
            mod_topics.append({
                'title': '[NUEVO] Corrección Automática de Factor de Potencia con Bancos de Capacitores y Filtros de Armónicos',
                'status': 'new',
                'badge': '🔵 Propuesta Nueva',
                'badge_color': 'bg-blue-100 text-blue-800',
                'category': 'Calidad de Energía y Normativa CNEE',
                'reason': '🔵 Propuesta Nueva: Evitar multas severas de EEGSA/Energuate por factor de potencia menor a 0.90 mediante reguladores automáticos de pasos capacitivos y reactancias desintonizadas.'
            })
            mod_topics.append({
                'title': '[NUEVO] Análisis de Firmas de Corriente en Motores (MCSA) y Termografía en Tableros CCM',
                'status': 'new',
                'badge': '🔵 Propuesta Nueva',
                'badge_color': 'bg-blue-100 text-blue-800',
                'category': 'Mantenimiento Predictivo 4.0',
                'reason': '🔵 Propuesta Nueva: Detección temprana de barras rotas en el rotor, excentricidad de entrehierro y sobrecalentamiento en bornes sin interrumpir la operación de la planta.'
            })
        if 'Relevación Industrial I' in m_name:
            mod_topics.append({
                'title': '[NUEVO] Seguridad Eléctrica y Mitigación de Arc Flash (NFPA 70E / OSHA)',
                'status': 'new',
                'badge': '🔵 Propuesta Nueva',
                'badge_color': 'bg-blue-100 text-blue-800',
                'category': 'Seguridad Operacional',
                'reason': '🔵 Propuesta Nueva: Procedimientos LOTO de bloqueo/etiquetado, cálculo de distancia de aproximación y uso de equipo de protección personal (EPP) calificado para maniobras de fuerza.'
            })

        classified_modules.append({
            'num': m_num,
            'name': m_name,
            'topics': mod_topics
        })

    # Counts
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
    <title>Auditoría Curricular y Propuesta: Controles y Máquinas Eléctricas | Kinal 2026</title>
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
                    <i data-lucide="zap" class="w-5 h-5 text-amber-400"></i>
                    Controles y Máquinas Eléctricas
                </h1>
            </div>

            <div class="flex items-center gap-2 text-xs no-print">
                <a href="index.html" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition">Portal Maestro</a>
                <a href="Instalaciones_Electricas_Generales_Propuesta.html" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition">Inst. Eléctricas</a>
                <span class="px-2.5 py-1.5 rounded-lg bg-amber-600 text-white font-bold">CME</span>
                <a href="Electronica_Analogica_Propuesta.html" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition">Electrónica Analógica</a>
                <a href="Control_Industrial_Sistemas_Programables_Propuesta.html" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition">Sist. Programables</a>
                <a href="Automatizacion_Industrial_Propuesta.html" class="px-2.5 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 transition">Automatización Ind.</a>
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
                <span>2025_CMEM.xlsx</span>
                <i data-lucide="chevron-right" class="w-3.5 h-3.5"></i>
                <span class="text-amber-600 font-semibold">Auditoría Curricular & Propuesta 2026</span>
            </div>
            <h2 class="text-3xl font-extrabold text-slate-900 tracking-tight">
                Auditoría Curricular: Controles y Máquinas Eléctricas (180 Horas)
            </h2>
            <p class="text-slate-600 mt-2 text-base max-w-4xl">
                Modernización integral orientada a la industria manufacturera, agroindustria y generación en Guatemala: Variadores de Frecuencia (VFD), Arrancadores Suaves (Soft Starters), corrección de factor de potencia bajo normativa <strong>CNEE (NTDOID)</strong>, mantenimiento predictivo con termografía y análisis MCSA, y seguridad eléctrica frente a arco eléctrico bajo estándar <strong>NFPA 70E</strong>.
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
                    <div class="text-xs font-medium text-red-600 uppercase tracking-wider">A Eliminar (Dinamos/Bombas Residenciales)</div>
                </div>
            </div>

            <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm flex items-center gap-4">
                <div class="w-12 h-12 rounded-lg bg-amber-100 flex items-center justify-center text-amber-600 font-bold text-xl">
                    <i data-lucide="refresh-cw" class="w-6 h-6"></i>
                </div>
                <div>
                    <div class="text-2xl font-bold text-slate-900">{count_upd} Temas</div>
                    <div class="text-xs font-medium text-amber-600 uppercase tracking-wider">A Actualizar (VFD/CNEE/Guardamotores)</div>
                </div>
            </div>

            <div class="bg-white p-5 rounded-xl border border-slate-200 shadow-sm flex items-center gap-4">
                <div class="w-12 h-12 rounded-lg bg-blue-100 flex items-center justify-center text-blue-600 font-bold text-xl">
                    <i data-lucide="plus-circle" class="w-6 h-6"></i>
                </div>
                <div>
                    <div class="text-2xl font-bold text-slate-900">{count_new} Temas</div>
                    <div class="text-xs font-medium text-blue-600 uppercase tracking-wider">Nuevos Propuestos (FP Activo / NFPA 70E)</div>
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
                    Exigencias operativas y regulatorias que impactan directamente el montaje, mantenimiento y control de motores eléctricos en el parque industrial guatemalteco.
                </p>
            </div>

            <div class="grid md:grid-cols-3 gap-6 text-sm">
                <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 space-y-3">
                    <div class="font-bold text-slate-900 flex items-center gap-2 text-base">
                        <i data-lucide="shield-alert" class="w-5 h-5 text-amber-600"></i>
                        Regulación CNEE y Calidad de Red (NTDOID)
                    </div>
                    <p class="text-slate-600 text-xs leading-relaxed">
                        Las empresas distribuidoras en Guatemala (EEGSA, Deorsa, Deocsa) aplican severos recargos económicos por factor de potencia inductivo inferior a 0.90 y exigen límites estrictos a la inyección de armónicos (IEEE 519). El técnico egresado debe saber dimensionar bancos de condensadores automáticos con reactancias anti-resonantes.
                    </p>
                </div>

                <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 space-y-3">
                    <div class="font-bold text-slate-900 flex items-center gap-2 text-base">
                        <i data-lucide="gauge" class="w-5 h-5 text-blue-600"></i>
                        Transición de Arranque Directo a VFD / Soft Starter
                    </div>
                    <p class="text-slate-600 text-xs leading-relaxed">
                        Los picos de corriente del arranque directo (hasta 7-8 veces la corriente nominal) provocan caídas de tensión inaceptables en líneas de producción y fatiga mecánica en bombas y molinos. El mercado laboral demanda técnicos capaces de comisionar variadores vectoriales con frenado dinámico y rampas suaves de desaceleración.
                    </p>
                </div>

                <div class="p-5 rounded-xl bg-slate-50 border border-slate-200 space-y-3">
                    <div class="font-bold text-slate-900 flex items-center gap-2 text-base">
                        <i data-lucide="hard-hat" class="w-5 h-5 text-emerald-600"></i>
                        Seguridad frente a Arc Flash (NFPA 70E / MinTrab)
                    </div>
                    <p class="text-slate-600 text-xs leading-relaxed">
                        En cumplimiento del Reglamento de Salud y Seguridad Ocupacional (Acuerdo Gubernativo 229-2014), las plantas multinacionales y corporaciones locales exigen procedimientos estrictos de desenergización, prueba de ausencia de tensión, bloqueo/etiquetado (LOTO) y uso de caretas y trajes contra arco eléctrico en tableros CCM.
                    </p>
                </div>
            </div>
        </section>

        <!-- SECCIÓN 2: Ficha de Venta Original y Diagnóstico Crítico de Anomalías -->
        <section class="bg-white rounded-2xl border border-slate-200 p-6 sm:p-8 shadow-sm space-y-6">
            <div class="border-b border-slate-100 pb-4">
                <span class="text-xs font-bold uppercase tracking-wider text-amber-600 bg-amber-50 px-2.5 py-1 rounded-full border border-amber-200">Sección 2</span>
                <h3 class="text-xl font-bold text-slate-900 mt-2 flex items-center gap-2">
                    <i data-lucide="file-spreadsheet" class="w-5 h-5 text-amber-600"></i>
                    Ficha Oficial de Venta ("Reporte") y Diagnóstico Crítico de Anomalías
                </h3>
            </div>

            <div class="grid md:grid-cols-2 gap-4 text-xs sm:text-sm text-slate-700 bg-slate-50 p-4 rounded-xl border border-slate-200">
                <div><strong>Programa Académico:</strong> Controles y Máquinas Eléctricas (2025_CMEM.xlsx)</div>
                <div><strong>Duración Total:</strong> 180 Horas cronológicas distribuidas en 10 Módulos</div>
                <div><strong>Jornadas:</strong> Matutina y Vespertina (Sábados de 8:00 a 12:30 y 13:00 a 17:30 hrs)</div>
                <div><strong>Acreditación:</strong> Diploma de Técnico en Electricidad Industrial</div>
                <div class="md:col-span-2"><strong>Perfil de Ingreso:</strong> Tercer grado de educación básica, conocimientos del curso de instalaciones eléctricas generales, habilidades lógicas y manuales.</div>
                <div class="md:col-span-2"><strong>Perfil de Egreso:</strong> Competencias para desempeñarse en la industria como técnico electricista industrial en conexión de máquinas de CA, circuitos de control, mando y reparación de averías.</div>
            </div>

            <!-- Diagnóstico Crítico -->
            <div class="bg-amber-50 border border-amber-300 rounded-xl p-5 space-y-3">
                <h4 class="text-amber-900 font-bold text-sm flex items-center gap-2">
                    <i data-lucide="alert-triangle" class="w-5 h-5 text-amber-600"></i>
                    Diagnóstico Crítico / Anomalías Detectadas en el Programa Original
                </h4>
                <ul class="text-xs text-amber-950 space-y-2 list-disc list-inside leading-relaxed">
                    <li><strong>Tecnología Anacrónica:</strong> Módulo 2 incluye <em>"Generadores de corriente continua"</em>, una tecnología que no se instala en ninguna industria moderna guatemalteca desde hace décadas, consumiendo horas que debieran asignarse a plantas generadoras diésel y alternadores síncronos con ATS.</li>
                    <li><strong>Contenido Fontanero Residencial Fuera de Contexto:</strong> Módulo 4 incluye <em>"Bombas monofásicas periféricas domiciliarias"</em>, lo cual desentona por completo con el perfil de un técnico electricista industrial enfocado en bombas trifásicas centrifugas y sumergibles industriales.</li>
                    <li><strong>Riesgo Operativo en Métodos Obsoletos:</strong> Módulo 6 lista <em>"Arranque estrella-delta manual"</em>, maniobra mecánica altamente propensa a quemar contactos por tiempo indebido de conmutación del operario y generar arcos eléctricos peligrosos.</li>
                    <li><strong>Omisión de Factor de Potencia y Armónicos:</strong> Pese a ser el principal motivo de sanciones económicas de las distribuidoras eléctricas en Guatemala, el temario no contemplaba bancos automáticos de capacitores ni filtros de armónicos.</li>
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

        <!-- SECCIÓN 4: Matriz Comparativa (Temario Tradicional vs. Temario Modernizado 2026) -->
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
                            <td class="p-3 font-bold text-slate-900 border border-slate-200">Generación y Transferencia</td>
                            <td class="p-3 text-slate-600 border border-slate-200">Estudio teórico de dinamos de corriente continua y sincronoscopio manual analógico en desuso.</td>
                            <td class="p-3 text-slate-800 border border-slate-200 font-medium">Grupos electrógenos diésel de emergencia, controladores ATS microprocesados (Deep Sea / ComAp) y sincronización automática.</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-bold text-slate-900 border border-slate-200">Arranque de Motores</td>
                            <td class="p-3 text-slate-600 border border-slate-200">Énfasis excesivo en arranques estrella-delta mecánicos manuales y bombas periféricas domésticas.</td>
                            <td class="p-3 text-slate-800 border border-slate-200 font-medium">Arrancadores suaves (Soft Starters) con bypass interno y control de bombas, y variadores de frecuencia vectoriales.</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-bold text-slate-900 border border-slate-200">Calidad de Energía y Normativa</td>
                            <td class="p-3 text-slate-600 border border-slate-200">Cálculo básico de potencia trifásica sin consideración de penalizaciones comerciales ni armónicos.</td>
                            <td class="p-3 text-slate-800 border border-slate-200 font-medium">Bancos automáticos de capacitores con reactancias de desintonización bajo normativa NTDOID de la CNEE (FP > 0.90).</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-bold text-slate-900 border border-slate-200">Seguridad Operacional</td>
                            <td class="p-3 text-slate-600 border border-slate-200">Normas generales de seguridad sin protocolos cuantitativos de arco eléctrico ni bloqueo de energía.</td>
                            <td class="p-3 text-slate-800 border border-slate-200 font-medium">Estándar NFPA 70E para prevención de Arc Flash, distancias de aproximación límite y protocolos LOTO certificados.</td>
                        </tr>
                        <tr>
                            <td class="p-3 font-bold text-slate-900 border border-slate-200">Mantenimiento Predictivo</td>
                            <td class="p-3 text-slate-600 border border-slate-200">Mantenimiento reactivo tras fallo de bobinado o disparo térmico del contactor.</td>
                            <td class="p-3 text-slate-800 border border-slate-200 font-medium">Monitoreo predictivo con termografía infrarroja de tableros CCM y análisis de firma de corriente (MCSA) para rodamientos y entrehierro.</td>
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
                    <h3 class="text-xl font-bold text-white">Innovación Tecnológica: Inteligencia Artificial en Controles y Máquinas Eléctricas</h3>
                </div>
            </div>

            <div class="grid md:grid-cols-3 gap-6">
                <div class="bg-white/10 backdrop-blur rounded-xl p-5 border border-white/10 space-y-3">
                    <div class="text-amber-300 font-bold text-sm flex items-center gap-2">
                        <i data-lucide="activity" class="w-4 h-4"></i>
                        Diagnóstico Predictivo de Fallas en Motores con Visión y Audio IA
                    </div>
                    <p class="text-xs text-slate-200 leading-relaxed">
                        Modelos de IA en dispositivos móviles que analizan el espectro acústico y térmico de un motor en funcionamiento para identificar soltura mecánica, desalineación o cavitación antes de que ocurra la falla catastrófica.
                    </p>
                    <div class="pt-2 border-t border-white/10 text-[11px] text-amber-200 font-mono">
                        Herramienta: ABB Ability Smart Sensor AI / Fluke Acoustic Imager AI.
                    </div>
                </div>

                <div class="bg-white/10 backdrop-blur rounded-xl p-5 border border-white/10 space-y-3">
                    <div class="text-amber-300 font-bold text-sm flex items-center gap-2">
                        <i data-lucide="cpu" class="w-4 h-4"></i>
                        Optimización de Parámetros de VFD Asistida por Copilot
                    </div>
                    <p class="text-xs text-slate-200 leading-relaxed">
                        Asistentes basados en LLMs entrenados con manuales de Siemens, Danfoss y Schneider Electric para generar listas de parámetros de comisionamiento rápido según las características de la placa del motor y tipo de carga (bombas, transportadores).
                    </p>
                    <div class="pt-2 border-t border-white/10 text-[11px] text-amber-200 font-mono">
                        Herramienta: VFD Copilot / Schneider EcoStruxure Automation Advisor.
                    </div>
                </div>

                <div class="bg-white/10 backdrop-blur rounded-xl p-5 border border-white/10 space-y-3">
                    <div class="text-amber-300 font-bold text-sm flex items-center gap-2">
                        <i data-lucide="zap" class="w-4 h-4"></i>
                        Análisis de Curvas de Demanda y Deslastre Inteligente de Cargas
                    </div>
                    <p class="text-xs text-slate-200 leading-relaxed">
                        Algoritmos de aprendizaje automático que predicen la potencia punta en la factura eléctrica de la planta y desconectan de forma secuencial cargas no críticas para evitar saltar al siguiente escalón tarifario penalizado.
                    </p>
                    <div class="pt-2 border-t border-white/10 text-[11px] text-amber-200 font-mono">
                        Herramienta: Energy Management AI / Siemens Sentron Powercenter.
                    </div>
                </div>
            </div>
        </section>

    </main>

    <footer class="bg-white border-t border-slate-200 mt-12 py-6 text-center text-xs text-slate-500">
        Fundación Kinal • Escuela Técnica Superior • Coordinación Académica • Propuesta Curricular Controles y Máquinas Eléctricas 2026
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
    (output_dir / 'Controles_y_Maquinas_Electricas_Propuesta.html').write_text(html, encoding='utf-8')
    print('Generated Controles_y_Maquinas_Electricas_Propuesta.html')

generate_cme()
