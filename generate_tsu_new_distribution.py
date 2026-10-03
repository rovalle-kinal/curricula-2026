import os

base_dir = "/Users/arqovalle/Library/CloudStorage/OneDrive-Personal/Software/Antigravity/Diseño Instruccional/TSU"
mybrain_dir = "/Users/arqovalle/Library/CloudStorage/OneDrive-Personal/MyBrain/MyBrain/01 - My Brain/Kinal/TSU"

os.makedirs(base_dir, exist_ok=True)
os.makedirs(mybrain_dir, exist_ok=True)

# Las 7 especialidades oficiales de Kinal UNIS
specialties = [
    {"name": "Construcción", "icon": "🏗️", "enfoque": "Supervisión de obras civiles, presupuestos de construcción, seguridad en andamios y calidad de materiales."},
    {"name": "Desarrollo de Aplicaciones Empresariales", "icon": "💻", "enfoque": "Liderazgo de proyectos de software, DevOps, arquitectura cloud, QA y gobernanza de datos."},
    {"name": "Electricidad Industrial", "icon": "⚡", "enfoque": "Distribución trifásica, subestaciones, factor de potencia, eficiencia energética y normativas NEC/AMM."},
    {"name": "Electrónica Industrial", "icon": "🔌", "enfoque": "Instrumentación, acondicionamiento de señales, PLCs, sistemas embebidos e interfaces IoT."},
    {"name": "Mecánica Automotriz", "icon": "🚗", "enfoque": "Diagnóstico electrónico OBD-II, electromovilidad, gestión de flotas y talleres de servicio automotriz."},
    {"name": "Mecánica Industrial", "icon": "⚙️", "enfoque": "Mantenimiento electromecánico, maquinado CNC, calderas, sistemas de bombeo y lubricación de plantas."},
    {"name": "Telecomunicaciones", "icon": "📡", "enfoque": "Redes de fibra óptica, enlaces inalámbricos, infraestructura de telecomunicaciones y ciberseguridad física."}
]

# Estructura de los 20 cursos con su nueva distribución temática transversal y subtema de IA
curriculum_distribution = [
    # BIMESTRE 1
    {
        "bimestre": "Bimestre 1",
        "cursos": [
            {
                "codigo": "B1-C1",
                "nombre": "Ética General 1: Antropología y Sentido Trascendente del Trabajo",
                "eje": "Formación Humana y Ética",
                "icono": "🛡️",
                "objetivo_transversal": "Forjar el carácter ético del supervisor técnico bajo el ideario de Kinal: la persona en el centro de la operación y el trabajo bien hecho como medio de superación.",
                "unidades": [
                    "1. La dignidad inalienable de la persona humana en el entorno laboral",
                    "2. El trabajo como vocación, servicio al prójimo y santificación de la vida ordinaria",
                    "3. Inteligencia emocional, autodominio y templanza bajo la presión de planta u obra",
                    "4. Comunicación no violenta y resolución de conflictos en cuadrillas de trabajo"
                ],
                "subtema_ia": "Sesgos cognitivos humanos frente a sesgos en modelos de IA: el papel de la conciencia moral que ninguna máquina puede replicar.",
                "aplicabilidad_7": "Aplica a resolver disputas entre albañiles en obra, técnicos de taller automotriz, programadores bajo estrés de entregas o electricistas en turno nocturno."
            },
            {
                "codigo": "B1-C2",
                "nombre": "Fundamentos de la Administración: Liderazgo Ágil de Mandos Medios",
                "eje": "Gestión y Supervisión",
                "icono": "📋",
                "objetivo_transversal": "Dotar al técnico de habilidades de supervisión moderna para coordinar equipos multidisciplinarios con enfoque ágil y orientado a resultados.",
                "unidades": [
                    "1. El supervisor técnico como puente estratégico entre la alta gerencia y la operación",
                    "2. Estructuras organizacionales horizontales y células de trabajo autónomas",
                    "3. Técnicas de delegación efectiva y retroalimentación constructiva (Feedback 1-on-1)",
                    "4. Gestión del cambio tecnológico y motivación de personal de diferentes generaciones"
                ],
                "subtema_ia": "Uso de asistentes de IA generativa (Copilots) para redacción ejecutiva de descriptores de puestos, actas técnicas y políticas operativas.",
                "aplicabilidad_7": "Permite organizar cuadrillas de obra civil, células Scrum de desarrollo, equipos de mantenimiento de redes de telecom o brigadas eléctricas."
            },
            {
                "codigo": "B1-C3",
                "nombre": "Planeación y Control para el Trabajo: Metodología Visual y OEE",
                "eje": "Gestión y Supervisión",
                "icono": "⏱️",
                "objetivo_transversal": "Capacitar en la planificación temporal de proyectos y órdenes de servicio mediante gestión visual y medición de la eficiencia global de equipos.",
                "unidades": [
                    "1. Secuenciación y balanceo de órdenes de trabajo (OT) en entornos de producción y servicios",
                    "2. Gestión visual del flujo operativo mediante tableros Kanban físicos y digitales (Trello/Notion)",
                    "3. Eficiencia Global de Equipos (OEE): Disponibilidad, Rendimiento y Calidad",
                    "4. Diagramas de Gantt dinámicos y software de cronogramas para proyectos técnicos"
                ],
                "subtema_ia": "Algoritmos de IA para estimación predictiva de duración de tareas y detección temprana de cuellos de botella en cronogramas.",
                "aplicabilidad_7": "Monitorea tiempos de atención en taller automotriz, avance de construcción en obra, sprints de software o paradas de maquinaria industrial."
            },
            {
                "codigo": "B1-C4",
                "nombre": "Matemática Básica 1: Aritmética Cuantitativa y Modelado en Hojas de Cálculo",
                "eje": "Ciencias Exactas Aplicadas",
                "icono": "📐",
                "objetivo_transversal": "Desarrollar el razonamiento cuantitativo y proporcional para estimar rendimientos, calcular factores de escala y automatizar hojas de cálculo técnicas sin errores.",
                "unidades": [
                    "1. Análisis dimensional y conversiones técnicas rigurosas (Sistema Internacional vs. Inglés)",
                    "2. Proporcionalidad directa e inversa, razones, porcentajes de variación y factores de escala en planos",
                    "3. Formulación y modelado de plantillas técnicas automatizadas en hojas de cálculo (Excel)",
                    "4. Sistemas de ecuaciones lineales aplicados a balances de recursos y estimación de presupuestos"
                ],
                "subtema_ia": "Uso de asistentes de IA generativa para formulación, depuración y explicación de fórmulas complejas en hojas de cálculo y detección de errores de sintaxis.",
                "aplicabilidad_7": "Cálculo de rendimientos y cubicajes (Construcción), estimación de costos y horas por sprint (Software), balance de cargas (Electricidad/Telecom), presupuestos de reparación (Automotriz/Mecánica), escalado de circuitos (Electrónica)."
            },
            {
                "codigo": "B1-C5",
                "nombre": "Física Básica 1: Estática, Fuerzas, Trabajo y Máquinas Simples",
                "eje": "Física y Tecnología",
                "icono": "⚖️",
                "objetivo_transversal": "Comprender los principios físicos del equilibrio de fuerzas, momento de torsión, trabajo mecánico y ventaja mecánica aplicados a la seguridad de izaje y estabilidad de equipos.",
                "unidades": [
                    "1. Estática de partículas y cuerpos rígidos: vectores de fuerza coplanares y primera condición de equilibrio (sumatoria F = 0)",
                    "2. Momento de una fuerza (Torque): brazo de palanca, segunda condición de equilibrio (sumatoria M = 0), apriete seguro y estabilidad",
                    "3. Trabajo mecánico (W = F·d), potencia (Watts y HP), energía y rendimiento/eficiencia mecánica",
                    "4. Máquinas simples y ventaja mecánica: poleas fijas/móviles, polipastos de izaje, palancas, planos inclinados y fricción real de anclajes"
                ],
                "subtema_ia": "Herramientas de visión artificial en dispositivos móviles para medición digital de ángulos, nivelación y cálculo óptico de distancias en campo.",
                "aplicabilidad_7": "Capacidad de carga y estabilidad de andamios (Construcción), torque seguro en pernos y culatas (Automotriz/Mecánica), izaje seguro de racks y servidores (Software/Telecom), tensión y flecha en cables y postes (Electricidad/Telecom), montaje y sujeción de gabinetes (Electrónica)."
            }
        ]
    },

    # BIMESTRE 2
    {
        "bimestre": "Bimestre 2",
        "cursos": [
            {
                "codigo": "B2-C1",
                "nombre": "Ética General 2: Libertad Responsable, Compliance e Integridad",
                "eje": "Formación Humana y Ética",
                "icono": "⚖️",
                "objetivo_transversal": "Interiorizar la responsabilidad jurídica y moral de las firmas técnicas y desarrollar una cultura de integridad empresarial inquebrantable.",
                "unidades": [
                    "1. Libertad personal responsable: la responsabilidad civil y penal de las firmas técnicas",
                    "2. La verdad en las bitácoras: prohibición de falsedad en inspecciones y memorias de cálculo",
                    "3. Compliance industrial: prevención de sobornos, dádivas de proveedores y conflicto de intereses",
                    "4. Seguridad psicológica y canales de denuncia de irregularidades técnicas o ambientales"
                ],
                "subtema_ia": "Auditoría ética de sistemas de decisión algorítmica: prevención de sesgos en compras automatizadas y contrataciones de personal.",
                "aplicabilidad_7": "Rechazo de compras de repuestos genéricos peligrosos en mecánica/electricidad, rechazo de materiales de mala calidad en construcción o licencias piratas en software."
            },
            {
                "codigo": "B2-C2",
                "nombre": "Herramientas Contables: Costos Industriales y Presupuestos Operativos",
                "eje": "Gestión y Supervisión",
                "icono": "💰",
                "objetivo_transversal": "Habilitar al supervisor para costear operaciones, justificar inversiones y administrar presupuestos de mantenimiento u obra en lenguaje financiero.",
                "unidades": [
                    "1. Estructura de costos: Materia Prima Directa (MPD), Mano de Obra (MOD) y Costos Indirectos (CIF)",
                    "2. Cuantificación del costo horario de parada no planificada de equipos (Downtime Cost)",
                    "3. Costeo de órdenes de trabajo (OT), presupuestos de obra y servicios técnicos",
                    "4. Elaboración y control de presupuestos operativos de área (OPEX) y capital (CAPEX básico)"
                ],
                "subtema_ia": "Modelos de IA para escaneo inteligente de facturas (OCR avanzado), clasificación automática de gastos y detección de desvíos presupuestarios.",
                "aplicabilidad_7": "Presupuestos de remodelaciones en construcción, costos de reparación mayor en talleres mecánicos, costos de hosting cloud en software o tendido de fibra en telecom."
            },
            {
                "codigo": "B2-C3",
                "nombre": "Administración de RRHH y SSO: Código de Trabajo, Planillas de IGSS y Acuerdo 229-2014",
                "eje": "Gestión y Supervisión",
                "icono": "🦺",
                "objetivo_transversal": "Dominar la legislación laboral guatemalteca, el cálculo de planillas y retenciones del IGSS, y liderar la seguridad ocupacional para lograr cero accidentes en planta u obra.",
                "unidades": [
                    "1. Código de Trabajo de Guatemala: jornadas diurna, mixta y nocturna, horas extras y libro de salarios",
                    "2. Cálculo de Salarios, Planillas y Retenciones del IGSS (cuota laboral 4.83%, patronal 12.67% y finiquitos)",
                    "3. Seguridad y Salud Ocupacional (SSO): marco legal del Acuerdo Gubernativo 229-2014 y Comités Bipartitos",
                    "4. Identificación de Peligros, Evaluación de Riesgos y Control (Matriz IPERC) y protocolos críticos (LOTO, alturas, EPP)"
                ],
                "subtema_ia": "Automatización de procesos (RPA) y asistentes de IA para verificación de consistencia en el cálculo de planillas de pago, horas extras y retenciones laborales.",
                "aplicabilidad_7": "Universal: todo supervisor técnico en las 7 carreras lidera personal de cuadrilla o taller, debiendo verificar horas extras, liquidaciones, descuentos del IGSS y velar por el cumplimiento de las normas de SSO."
            },
            {
                "codigo": "B2-C4",
                "nombre": "Matemática Básica 2: Punto de Equilibrio, Modelado de Funciones y Lógica Matemática",
                "eje": "Ciencias Exactas Aplicadas",
                "icono": "📉",
                "objetivo_transversal": "Modelar el punto de equilibrio operativo de servicios técnicos y dominar la lógica booleana y la algoritmia para estructurar procesos y hojas de cálculo avanzadas.",
                "unidades": [
                    "1. Funciones lineales y análisis de punto de equilibrio operativo (Punto de Equilibrio = CF / Margen Contribución) en Excel",
                    "2. Funciones no lineales y modelado de tendencias: depreciación de activos fijos y degradación temporal de equipos",
                    "3. Lógica matemática y operadores booleanos: proposiciones, tablas de verdad (AND, OR, NOT, XOR) y funciones condicionales en Excel",
                    "4. Algoritmia básica y diagramación de flujo de procesos estandarizados bajo normas ANSI/ISO"
                ],
                "subtema_ia": "Asistentes de IA para traducción de reglas de negocio operativas a diagramas de flujo y árboles de decisión lógica estructurados.",
                "aplicabilidad_7": "Cálculo de rentabilidad y flujos de procesos en obra civil (Construcción), lógica de programación directa (Software), interbloqueos y condiciones de seguridad (Electricidad/Electrónica), diagnóstico estructurado de fallas en taller (Automotriz/Mecánica), diagramas de conmutación de red (Telecomunicaciones)."
            },
            {
                "codigo": "B2-C5",
                "nombre": "Física Aplicada 1: Física de Materiales, Resistencia y Propiedades Físico-Mecánicas",
                "eje": "Física y Tecnología",
                "icono": "🧱",
                "objetivo_transversal": "Comprender el comportamiento mecánico, térmico y dieléctrico de los materiales técnicos bajo esfuerzos reales, garantizando factores de seguridad adecuados y prevención de fallas.",
                "unidades": [
                    "1. Esfuerzos mecánicos fundamentales (tensión, compresión, cortante, flexión, torsión) y Ley de Hooke",
                    "2. Propiedades mecánicas y térmicas: elasticidad, plasticidad, tenacidad, fatiga de materiales y dilatación térmica lineal",
                    "3. Propiedades eléctricas y dieléctricas: materiales conductores, aislantes, semiconductores y disipación térmica",
                    "4. Criterios técnicos de selección de materiales y prevención de corrosión, degradación ambiental y fallas"
                ],
                "subtema_ia": "Modelos de IA y herramientas analíticas para búsqueda y comparación automática de propiedades de materiales en bases de datos técnicas.",
                "aplicabilidad_7": "Resistencia de probetas de concreto y acero (Construcción), aleaciones y disipadores térmicos para servidores y racks (Software/Hardware), tensión en tendidos y rigidez de aisladores (Electricidad/Telecom), esfuerzos en chasis y fatiga en frenos (Automotriz), pernos de sujeción y fatiga de ejes (Mecánica), dieléctricos y pistas en PCB (Electrónica)."
            }
        ]
    },

    # BIMESTRE 3
    {
        "bimestre": "Bimestre 3",
        "cursos": [
            {
                "codigo": "B3-C1",
                "nombre": "Ética Profesional 1: Automatización, IA y la Transición Justa",
                "eje": "Formación Humana y Ética",
                "icono": "🤖",
                "objetivo_transversal": "Liderar con sensibilidad ética la transformación digital y automatización de procesos, promoviendo el reentrenamiento del personal antes que el despido masivo.",
                "unidades": [
                    "1. Automatización y el futuro del empleo en Guatemala: el imperativo moral de la transición justa",
                    "2. Reskilling y Upskilling: el deber de elevar las competencias del operario técnico",
                    "3. Ética en IA industrial: prevención de sesgos algorítmicos en evaluaciones de desempeño",
                    "4. Privacidad del trabajador: límites éticos al monitoreo biométrico y software espía"
                ],
                "subtema_ia": "Uso responsable de herramientas de IA generativa en la empresa: confidencialidad de datos, propiedad intelectual y prevención de fugas de secretos industriales.",
                "aplicabilidad_7": "Esencial para el supervisor que instala robots en una línea de ensamble, automatiza pruebas de software, o moderniza maquinaria desplazando mano de obra no calificada."
            },
            {
                "codigo": "B3-C2",
                "nombre": "Métodos de Producción: Lean Manufacturing y Estandarización 5S",
                "eje": "Gestión y Supervisión",
                "icono": "🏭",
                "objetivo_transversal": "Aplicar la filosofía Lean y las 5S de Kinal para erradicar desperdicios, balancear líneas operativas y maximizar la productividad del área a cargo.",
                "unidades": [
                    "1. Los 8 desperdicios industriales (Mudas): sobreproducción, tiempos de espera, defectos y mermas",
                    "2. Implementación de 5S en taller y oficina (Seiri, Seiton, Seiso, Seiketsu, Shitsuke) como hábito Kinal",
                    "3. Mapeo de Flujo de Valor (VSM - Value Stream Mapping) del estado actual y futuro",
                    "4. Estandarización de operaciones, tiempo de ciclo (Takt Time) y técnica SMED para cambios rápidos"
                ],
                "subtema_ia": "Optimización de rutas de producción y balanceo de líneas mediante algoritmos genéticos y modelos de investigación de operaciones con IA.",
                "aplicabilidad_7": "Optimización del patio de materiales en construcción, reducción de tiempos de servicio en bahías de taller automotriz, flujo de tickets de telecom o sprints ágiles de software."
            },
            {
                "codigo": "B3-C3",
                "nombre": "Servicio al Cliente: Gestión de Clientes B2B y Acuerdos SLA",
                "eje": "Gestión y Supervisión",
                "icono": "🤝",
                "objetivo_transversal": "Desarrollar una mentalidad de servicio profesional tanto hacia el cliente interno (producción/ingeniería) como hacia clientes externos corporativos.",
                "unidades": [
                    "1. El concepto de cliente interno en organizaciones técnicas: sinergia mantenimiento-producción",
                    "2. Acuerdos de Nivel de Servicio (SLA - Service Level Agreements) para disponibilidad técnica",
                    "3. Gestión de garantías de maquinaria, soporte técnico postventa y manejo de reclamos B2B",
                    "4. El espíritu de servicio cristiano como diferenciador de excelencia profesional del egresado Kinal"
                ],
                "subtema_ia": "Agentes conversacionales inteligentes de soporte técnico de primer nivel y análisis automático de sentimiento en tickets de servicio postventa.",
                "aplicabilidad_7": "Soporte postventa de maquinaria industrial, acuerdos de uptime en redes de telecomunicaciones, garantías de obra civil o contratos de soporte de software (SLA 99.9%)."
            },
            {
                "codigo": "B3-C4",
                "nombre": "Matemática Aplicada 1: Estadística Práctica Aplicada y Análisis de Datos Operativos",
                "eje": "Ciencias Exactas Aplicadas",
                "icono": "📊",
                "objetivo_transversal": "Utilizar la analítica descriptiva en hojas de cálculo y la ley de Pareto para identificar la dispersión de mediciones y priorizar las causas de fallas y mermas operativas.",
                "unidades": [
                    "1. Estadística descriptiva práctica en hojas de cálculo: media, mediana, moda, desviación estándar y percentiles en Excel",
                    "2. Organización y visualización de datos: tablas de frecuencia, histogramas y diagramas de caja para detección de variabilidad",
                    "3. Principio de Pareto (Regla 80/20) y estratificación para priorización operativa de problemas, defectos o quejas",
                    "4. Tendencias operacionales y correlación lineal simple: diagramas de dispersión, coeficiente de correlación (R) y proyecciones"
                ],
                "subtema_ia": "Herramientas de IA para análisis exploratorio de datos (Code Interpreter / Data Analysis) para procesar tablas CSV y generar resúmenes estadísticos automáticos.",
                "aplicabilidad_7": "Dispersión de resistencia en probetas de obra (Construcción), métricas de latencia y tiempos de respuesta (Software), historial de variaciones de voltaje (Electricidad), control de tolerancias de componentes (Electrónica), tiempos de servicio en taller (Automotriz), frecuencia de fallas de máquinas (Mecánica), latencia y disponibilidad de enlaces (Telecom)."
            },
            {
                "codigo": "B3-C5",
                "nombre": "Física Aplicada 2: Energía, Eficiencia Energética y Sostenibilidad Operativa",
                "eje": "Física y Tecnología",
                "icono": "⚡",
                "objetivo_transversal": "Comprender los balances energéticos, el costo de la energía eléctrica industrial en Guatemala y las tecnologías de climatización y energía solar para reducir costos y huella de carbono.",
                "unidades": [
                    "1. Principios de energía y balances operativos: formas de energía, principio de conservación (Ein = Eout + Pérdidas) y unidades prácticas (J, BTU, kWh)",
                    "2. Potencia eléctrica, consumo en kWh y facturación de energía industrial en Guatemala (pliegos tarifarios EEGSA / ENERGUATE)",
                    "3. Transferencia de calor (conducción, convección, radiación) y climatización básica (HVAC / enfriamiento de espacios técnicos)",
                    "4. Eficiencia energética, fundamentos de energía solar fotovoltaica (paneles, inversores, baterías) y reducción de huella de carbono"
                ],
                "subtema_ia": "Algoritmos de IA para análisis de curvas de carga eléctrica y detección automática de consumos parásitos o desvíos energéticos.",
                "aplicabilidad_7": "Aislamiento térmico y ahorro energético en edificaciones (Construcción), consumo y refrigeración de centros de datos (Software), auditorías energéticas y tarifas industriales (Electricidad), disipación de calor en gabinetes (Electrónica), eficiencia térmica en motores y aire acondicionado vehicular (Automotriz), optimización de compresores (Mecánica), radiobases con respaldo solar (Telecom)."
            }
        ]
    },

    # BIMESTRE 4
    {
        "bimestre": "Bimestre 4",
        "cursos": [
            {
                "codigo": "B4-C1",
                "nombre": "Ética Profesional 2: Principio Human-in-the-Loop y el Trabajo Bien Hecho",
                "eje": "Formación Humana y Ética",
                "icono": "🧠",
                "objetivo_transversal": "Consagrar el principio de que la responsabilidad moral y legal de la supervisión técnica es indelegable a las máquinas, coronando la formación con el ideal del trabajo bien hecho.",
                "unidades": [
                    "1. El principio Human-in-the-Loop (HITL): supervisión humana obligatoria en sistemas automatizados e IA",
                    "2. Superación del sesgo de automatización (Automation Bias) y desarrollo del juicio crítico profesional",
                    "3. El trabajo bien hecho Kinal: rechazo al plagio, al 'copia y pega' de IA y veracidad en peritajes",
                    "4. Responsabilidad ambiental, economía circular y gestión ética de residuos peligrosos (e-waste)"
                ],
                "subtema_ia": "Gobernanza de sistemas autónomos: protocolos para garantizar que en paradas de emergencia, seguridad de vidas o despidos siempre decida una persona.",
                "aplicabilidad_7": "Universal: ninguna IA debe autorizar una excavación riesgosa, liberar un código bancario a producción, encender una subestación o diagnosticar frenos sin firma humana responsable."
            },
            {
                "codigo": "B4-C2",
                "nombre": "Control de Calidad: Sistemas ISO 9001:2015 y Metodología Six Sigma",
                "eje": "Gestión y Supervisión",
                "icono": "🎯",
                "objetivo_transversal": "Implementar sistemas de gestión de calidad orientados a la prevención en la fuente y dominar la resolución estructurada de problemas mediante el ciclo DMAIC.",
                "unidades": [
                    "1. Sistemas de Gestión de Calidad bajo norma ISO 9001:2015 y enfoque basado en riesgos",
                    "2. Las 7 herramientas clásicas de la calidad para análisis de causas raíz (Ishikawa, Pareto 80/20)",
                    "3. Aseguramiento de calidad en la fuente y diseño de dispositivos a prueba de errores (Poka-Yoke)",
                    "4. Metodología Six Sigma: ciclo DMAIC (Definir, Medir, Analizar, Mejorar, Controlar) y matrices AMFE"
                ],
                "subtema_ia": "Visión artificial con redes neuronales convolucionales (CNN) para inspección automática de defectos superficiales y control dimensional a alta velocidad.",
                "aplicabilidad_7": "Control de fisuras en soldaduras o concreto, inspección de piezas mecanizadas, revisión automática de código (linter con IA), calidad de crimpado de cables o empaque."
            },
            {
                "codigo": "B4-C3",
                "nombre": "Fundamentos del Marketing: Business Intelligence y Analítica con Power BI",
                "eje": "Gestión y Supervisión",
                "icono": "📈",
                "objetivo_transversal": "Transformar la materia de marketing en inteligencia de negocios B2B y diseño de cuadros de mando (Dashboards) para comunicar resultados de planta a gerencia.",
                "unidades": [
                    "1. Fundamentos de marketing industrial B2B, propuesta de valor técnica y compras corporativas",
                    "2. Business Intelligence (BI): conexión, modelado y limpieza de datos operativos de planta",
                    "3. Creación de Cuadros de Mando (Dashboards en Power BI): visualización de KPIs de producción y costos",
                    "4. Técnicas de presentación ejecutiva de resultados técnicos ante comités de gerencia y dirección"
                ],
                "subtema_ia": "Analítica predictiva de demanda y herramientas de procesamiento de lenguaje natural (NLP) para generar resúmenes automáticos de reportes de planta.",
                "aplicabilidad_7": "Presentación de avance físico-financiero de obra, métricas de fallas vehiculares de flota, indicadores de tiempo medio entre fallas (MTBF/MTTR) o disponibilidad de software."
            },
            {
                "codigo": "B4-C4",
                "nombre": "Matemática Aplicada 2: Ingeniería Económica, Interés Compuesto y Proyectos",
                "eje": "Ciencias Exactas Aplicadas",
                "icono": "🏦",
                "objetivo_transversal": "Dominar el interés compuesto y las herramientas de evaluación económica para justificar financieramente compras de maquinaria, reemplazos y proyectos técnicos.",
                "unidades": [
                    "1. Interés compuesto, capitalización discreta/continua, tasas nominales vs. efectivas (TEA) e inflación",
                    "2. Anualidades y tablas de amortización de préstamos comerciales y arrendamiento (Leasing) de equipo",
                    "3. Evaluación financiera de inversiones técnicas: Valor Presente Neto (VPN) y Tasa Interna de Retorno (TIR)",
                    "4. Periodo de recuperación (Payback) y análisis de reemplazo de maquinaria (reparar vs. comprar nuevo)"
                ],
                "subtema_ia": "Simulaciones estocásticas de Monte Carlo asistidas por IA para análisis de riesgo e incertidumbre en presupuestos de inversión técnica.",
                "aplicabilidad_7": "Justificar compra de una retroexcavadora en construcción, un escáner automotriz avanzado, un torno CNC, un servidor en la nube o un analizador de espectro telecom."
            },
            {
                "codigo": "B4-C5",
                "nombre": "Física Aplicada 3: Tecnología, Sensores y Programación Aplicada con Python",
                "eje": "Física y Tecnología",
                "icono": "💻",
                "objetivo_transversal": "Comprender los principios físicos de sensores y transductores de planta y dominar la lógica de programación en Python para automatizar cálculos técnicos, procesar datos y generar reportes.",
                "unidades": [
                    "1. Fundamentos físicos de medición: sensores y transductores de planta (temperatura, proximidad, ópticos, interruptores y presión)",
                    "2. Lógica de programación y sintaxis básica de Python para técnicos (variables, condicionales if/else, bucles for/while)",
                    "3. Automatización de cálculos técnicos, creación de funciones modulares y procesamiento de archivos de datos (CSV)",
                    "4. Visualización gráfica de variables físicas y tendencias (librería matplotlib) y desarrollo de scripts de validación técnica"
                ],
                "subtema_ia": "Asistentes de codificación con Inteligencia Artificial (Copilot / ChatGPT) para generación y depuración de scripts en Python a partir de instrucciones en lenguaje natural.",
                "aplicabilidad_7": "Script en Python para cubicaje y cálculo de materiales (Construcción), integración de scripts con APIs y lógica de backend (Software), cálculo automatizado de caídas de tensión y calibres (Electricidad), adquisición de datos de instrumentación (Electrónica), procesamiento de registros de escáner automotriz OBD-II (Automotriz), análisis de bitácoras de fallas de maquinaria (Mecánica), scripts de monitoreo continuo de conectividad de red (Telecom)."
            }
        ]
    }
]

# GENERAR ARCHIVO HTML DE LA NUEVA DISTRIBUCIÓN
html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nueva Distribución Temática TSU 2026 | Fundación Kinal</title>
    <style>
        :root {{
            --kinal-blue: #0f2d59;
            --kinal-accent: #d97706;
            --kinal-light: #f8fafc;
            --text-dark: #1e293b;
            --text-muted: #64748b;
            --border-color: #cbd5e1;
            --color-ia: #4f46e5;
            --color-ia-bg: #eef2ff;
        }}
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background-color: #f1f5f9;
            color: var(--text-dark);
            line-height: 1.6;
            padding: 24px;
        }}
        .container {{
            max-width: 1300px;
            margin: 0 auto;
            background: #ffffff;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.08);
            overflow: hidden;
            border: 1px solid var(--border-color);
        }}
        header {{
            background: linear-gradient(135deg, var(--kinal-blue) 0%, #1e3a8a 100%);
            color: #ffffff;
            padding: 36px 40px;
            border-bottom: 4px solid var(--kinal-accent);
        }}
        .header-badge {{
            display: inline-block;
            background: rgba(217, 119, 6, 0.25);
            color: #fef08a;
            border: 1px solid var(--kinal-accent);
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 600;
            letter-spacing: 0.5px;
            margin-bottom: 12px;
            text-transform: uppercase;
        }}
        header h1 {{ font-size: 2.2rem; font-weight: 700; margin-bottom: 8px; }}
        header p {{ color: #cbd5e1; font-size: 1.05rem; max-width: 950px; }}
        
        main {{ padding: 40px; }}

        .callout-gold {{
            border-left: 4px solid var(--kinal-accent);
            background: #fffbeb;
            padding: 20px 24px;
            border-radius: 0 8px 8px 0;
            margin-bottom: 30px;
        }}
        .callout-gold h4 {{ color: #92400e; margin-bottom: 6px; font-size: 1.1rem; }}
        .callout-gold p {{ color: #78350f; font-size: 0.95rem; }}

        .specialties-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
            gap: 16px;
            margin: 20px 0 36px 0;
        }}
        .spec-card {{
            background: #f8fafc;
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 16px 18px;
            display: flex;
            align-items: flex-start;
            gap: 14px;
        }}
        .spec-icon {{ font-size: 2rem; line-height: 1; }}
        .spec-title {{ font-weight: 700; color: var(--kinal-blue); font-size: 0.98rem; margin-bottom: 4px; }}
        .spec-desc {{ font-size: 0.85rem; color: var(--text-muted); }}

        .bimestre-block {{
            margin-bottom: 48px;
            border: 1px solid var(--border-color);
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        }}
        .bimestre-header {{
            background: #0b1f3a;
            color: #ffffff;
            padding: 16px 24px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .bimestre-header h2 {{ font-size: 1.35rem; font-weight: 700; color: #fef08a; }}
        .bimestre-header span {{ font-size: 0.88rem; color: #94a3b8; }}

        .course-row {{
            padding: 24px;
            border-bottom: 1px solid #e2e8f0;
            background: #ffffff;
        }}
        .course-row:last-child {{ border-bottom: none; }}
        .course-row:nth-child(even) {{ background: #fafbfc; }}

        .course-title-bar {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 10px;
            margin-bottom: 12px;
        }}
        .course-title-bar h3 {{
            font-size: 1.2rem;
            color: var(--kinal-blue);
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        .badge-code {{
            background: #e2e8f0;
            color: #334155;
            padding: 3px 8px;
            border-radius: 4px;
            font-size: 0.78rem;
            font-weight: 700;
        }}
        .badge-eje {{
            background: #e0f2fe;
            color: #0369a1;
            padding: 3px 8px;
            border-radius: 4px;
            font-size: 0.78rem;
            font-weight: 600;
        }}

        .course-obj {{
            font-size: 0.93rem;
            color: #334155;
            margin-bottom: 14px;
            background: #f1f5f9;
            padding: 10px 14px;
            border-radius: 6px;
            border-left: 3px solid var(--kinal-blue);
        }}

        .content-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            margin-top: 14px;
        }}
        @media (max-width: 860px) {{
            .content-grid {{ grid-template-columns: 1fr; }}
        }}

        .units-box {{
            background: #ffffff;
            border: 1px solid var(--border-color);
            border-radius: 6px;
            padding: 14px 18px;
        }}
        .units-box h4 {{
            font-size: 0.92rem;
            color: var(--kinal-blue);
            margin-bottom: 8px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        .units-box ul {{
            padding-left: 18px;
            font-size: 0.88rem;
            color: var(--text-dark);
        }}
        .units-box li {{ margin-bottom: 4px; }}

        .ia-box {{
            background: var(--color-ia-bg);
            border: 1px solid #c7d2fe;
            border-radius: 6px;
            padding: 14px 18px;
        }}
        .ia-box h4 {{
            font-size: 0.92rem;
            color: var(--color-ia);
            margin-bottom: 6px;
            display: flex;
            align-items: center;
            gap: 6px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        .ia-box p {{
            font-size: 0.88rem;
            color: #3730a3;
            margin-bottom: 8px;
        }}
        .spec-relevance {{
            font-size: 0.82rem;
            color: #4338ca;
            background: rgba(255,255,255,0.7);
            padding: 6px 10px;
            border-radius: 4px;
            border-left: 2px solid var(--color-ia);
        }}

        footer {{
            background: #0f172a;
            color: #94a3b8;
            padding: 24px 40px;
            font-size: 0.88rem;
            text-align: center;
        }}
    </style>
</head>
<body>

<div class="container">
    <header>
        <span class="header-badge">Propuesta de Rediseño Curricular Integral 2026</span>
        <h1>Nueva Distribución Temática: Año Académico TSU</h1>
        <p>Estructura transversal unificada para los 20 cursos del 3er año académico de la Escuela Técnica Superior de Fundación Kinal (Avalado por Universidad del Istmo - UNIS), integrando Inteligencia Artificial como competencia estratégica común a las 7 especialidades.</p>
    </header>

    <nav style="background: #0b1f3a; padding: 0 40px; display: flex; gap: 16px; overflow-x: auto; border-bottom: 1px solid rgba(255,255,255,0.1);">
        <a href="index.html" style="color: #cbd5e1; text-decoration: none; padding: 14px 18px; font-weight: 600; font-size: 0.95rem; display: inline-block;">← Ver Dictamen Detallado de los 20 Cursos (Auditoría Original vs. Modernizada)</a>
        <a href="nueva_distribucion_tematica_tsu.html" style="color: #fef08a; text-decoration: none; padding: 14px 18px; font-weight: 700; font-size: 0.95rem; display: inline-block; border-bottom: 3px solid var(--kinal-accent);">🌟 Nueva Distribución Temática 2026</a>
    </nav>

    <main>
        <div class="callout-gold">
            <h4>El Reto de la Transversalidad: El Año Académico Común</h4>
            <p>El 3er Año Académico del TSU se imparte en común para estudiantes de <strong>7 especialidades técnicas diferentes</strong> que ya completaron sus 2 primeros años de especialidad práctica. Por lo tanto, el contenido no debe encerrarse en una sola especialidad técnica, sino consolidar las <strong>competencias transversales de supervisión, rigor cuantitativo, optimización de recursos, transformación digital con IA y ética profesional</strong> que exige la industria guatemalteca para puestos de jefatura y mandos medios.</p>
        </div>

        <h2 style="color: var(--kinal-blue); margin-bottom: 14px;">Las 7 Especialidades del TSU Integradas</h2>
        <div class="specialties-grid">
"""

for s in specialties:
    html += f"""
            <div class="spec-card">
                <div class="spec-icon">{s["icon"]}</div>
                <div>
                    <div class="spec-title">{s["name"]}</div>
                    <div class="spec-desc">{s["enfoque"]}</div>
                </div>
            </div>
    """

html += """
        </div>

        <h2 style="color: var(--kinal-blue); margin-bottom: 20px;">Distribución Temática de los 20 Cursos (Bimestres 1 al 4)</h2>
"""

for b in curriculum_distribution:
    html += f"""
        <div class="bimestre-block">
            <div class="bimestre-header">
                <h2>{b["bimestre"]}</h2>
                <span>5 Cursos Obligatorios (50 min c/u) • 60 Sesiones Anuales</span>
            </div>
    """
    for c in b["cursos"]:
        units_li = "".join([f"<li>{u}</li>" for u in c["unidades"]])
        html += f"""
            <div class="course-row">
                <div class="course-title-bar">
                    <h3><span>{c["icono"]}</span> {c["nombre"]}</h3>
                    <div>
                        <span class="badge-code">{c["codigo"]}</span>
                        <span class="badge-eje">{c["eje"]}</span>
                    </div>
                </div>
                <div class="course-obj">
                    <strong>Objetivo de Supervisión Transversal:</strong> {c["objetivo_transversal"]}
                </div>
                <div class="content-grid">
                    <div class="units-box">
                        <h4>Unidades Temáticas Principales</h4>
                        <ul>
                            {units_li}
                        </ul>
                    </div>
                    <div class="ia-box">
                        <h4>🤖 Subtema de Inteligencia Artificial (IA)</h4>
                        <p>{c["subtema_ia"]}</p>
                        <div class="spec-relevance">
                            <strong>Aplicabilidad a las 7 especialidades:</strong> {c["aplicabilidad_7"]}
                        </div>
                    </div>
                </div>
            </div>
        """
    html += """
        </div>
    """

html += """
        <div style="background: #e2e8f0; padding: 24px; border-radius: 8px; margin-top: 30px;">
            <h3 style="color: var(--kinal-blue); margin-bottom: 8px;">Alineación Normativa y Pedagógica Kinal</h3>
            <ul style="padding-left: 20px; font-size: 0.92rem; color: var(--text-dark);">
                <li><strong>Ideario Institucional:</strong> Fomento del principio del <em>"trabajo bien hecho"</em>, espíritu de servicio y respeto incondicional a la dignidad humana.</li>
                <li><strong>Nota Mínima Aprobatoria:</strong> Rigurosamente fijada en <strong>&ge; 75 puntos sobre 100</strong> en todas las evaluaciones formativas y suficiencias.</li>
                <li><strong>Acreditación de Inglés:</strong> Certificación obligatoria de nivel <strong>A2</strong> en la prueba estandarizada <strong>ELASH II</strong>.</li>
            </ul>
        </div>
    </main>

    <footer>
        Fundación Kinal • Escuela Técnica Superior • Propuesta de Distribución Temática TSU • Guatemala, 2026
    </footer>
</div>

</body>
</html>
"""

# GUARDAR HTML
with open(os.path.join(base_dir, "nueva_distribucion_tematica_tsu.html"), "w", encoding="utf-8") as f:
    f.write(html)
with open(os.path.join(mybrain_dir, "nueva_distribucion_tematica_tsu.html"), "w", encoding="utf-8") as f:
    f.write(html)

print("nueva_distribucion_tematica_tsu.html generada exitosamente.")

# GENERAR RESUMEN MARKDOWN
md_content = """# Propuesta de Nueva Distribución Temática: Año Académico TSU 2026
### Escuela Técnica Superior de Fundación Kinal (Avalado por Universidad del Istmo - UNIS)

---

## 1. Fundamentación y Principio de Transversalidad

El 3er Año Académico del **Técnico Superior Universitario (TSU)** se cursa en común para estudiantes provenientes de **7 especialidades técnicas** que ya completaron sus 2 primeros años de especialidad práctica:
1. **Construcción**
2. **Desarrollo de Aplicaciones Empresariales**
3. **Electricidad Industrial**
4. **Electrónica Industrial**
5. **Mecánica Automotriz**
6. **Mecánica Industrial**
7. **Telecomunicaciones**

Por tanto, el temario no debe encerrarse en una sola especialidad técnica, sino consolidar las **competencias de supervisión, rigor cuantitativo, finanzas operativas, transformación digital con Inteligencia Artificial y ética profesional** requeridas por la industria guatemalteca (CIG / AGEXPORT) para mandos medios y jefaturas.

---

## 2. Matriz Curricular Consolidada de los 20 Cursos

"""

for b in curriculum_distribution:
    md_content += f"\n### {b['bimestre']}\n\n"
    for c in b["cursos"]:
        md_content += f"#### {c['codigo']} • {c['icono']} {c['nombre']}\n"
        md_content += f"* **Eje Curricular:** {c['eje']}\n"
        md_content += f"* **Objetivo Transversal:** {c['objetivo_transversal']}\n"
        md_content += "* **Unidades Temáticas:**\n"
        for u in c["unidades"]:
            md_content += f"  * {u}\n"
        md_content += f"* **🤖 Subtema de Inteligencia Artificial (IA):** {c['subtema_ia']}\n"
        md_content += f"* **Aplicabilidad a las 7 Especialidades:** {c['aplicabilidad_7']}\n\n"

md_content += """---

## 3. Parámetros Institucionales Inmutables de Kinal
* **Nota Mínima Aprobatoria:** **75 puntos sobre 100**.
* **Ideario:** Visión cristiana, dignidad de la persona, espíritu de servicio y el *trabajo bien hecho*.
* **Inglés:** Certificación nivel **A2** en prueba ELASH II.
"""

with open(os.path.join(base_dir, "NUEVA_DISTRIBUCION_TEMATICA_TSU.md"), "w", encoding="utf-8") as f:
    f.write(md_content)
with open(os.path.join(mybrain_dir, "NUEVA_DISTRIBUCION_TEMATICA_TSU.md"), "w", encoding="utf-8") as f:
    f.write(md_content)

print("NUEVA_DISTRIBUCION_TEMATICA_TSU.md generada exitosamente.")
