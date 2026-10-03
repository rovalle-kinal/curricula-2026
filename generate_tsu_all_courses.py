import os
import json

base_dir = "/Users/arqovalle/Library/CloudStorage/OneDrive-Personal/Software/Antigravity/Diseño Instruccional/TSU"
mybrain_dir = "/Users/arqovalle/Library/CloudStorage/OneDrive-Personal/MyBrain/MyBrain/01 - My Brain/Kinal/TSU"

os.makedirs(base_dir, exist_ok=True)
os.makedirs(mybrain_dir, exist_ok=True)

courses = [
    # BIMESTRE 1
    {
        "id": "b1_etica_general_1",
        "bimestre": "Bimestre 1",
        "periodo": "Periodo 1 (50 min)",
        "nombre": "Ética General 1",
        "eje": "Formación Humana y Ética",
        "icono": "🛡️",
        "actual": "Antropología básica abstracta y conceptos teóricos sobre 'capacidades para ser un buen técnico'.",
        "anular": "Discusiones metafísicas teóricas abstractas y casuística de salón sin relación con la planta industrial o el taller.",
        "actualizar": "El sentido trascendente del trabajo profesional (ideario Kinal): el trabajo como medio de realización personal, perfeccionamiento y servicio. Dignidad inalienable del operario por encima de la producción fabril y el capital.",
        "nuevo": "Inteligencia emocional, comunicación no violenta, liderazgo con espíritu de servicio en la supervisión de piso, templanza y manejo de la presión laboral.",
        "justificacion": "La industria guatemalteca (CIG) señala que la principal causa de despidos y rotación en mandos medios no es la falta de conocimiento técnico, sino las fallas en el trato humano, prepotencia o incapacidad de liderar con serenidad.",
        "temario_modernizado": [
            "La dignidad trascendente de la persona humana en el entorno laboral",
            "El trabajo como vocación, servicio y perfeccionamiento personal (Pilar Kinal)",
            "Liderazgo de piso: inteligencia emocional, escucha activa y respeto mutuo",
            "Resolución pacífica de fricciones operativas y comunicación asertiva"
        ]
    },
    {
        "id": "b1_fundamentos_administracion",
        "bimestre": "Bimestre 1",
        "periodo": "Periodo 2 (50 min)",
        "nombre": "Fundamentos de la Administración",
        "eje": "Gestión y Supervisión",
        "icono": "📋",
        "actual": "Escuelas clásicas de la administración (Taylor, Fayol, Weber), organigramas piramidales rígidos y manuales de puestos en papel.",
        "anular": "Memorización de biografías históricas de la administración y diseño de organigramas estáticos de papel no aplicables a plantas ágiles.",
        "actualizar": "Principios de administración moderna para mandos medios técnicos: estructuras celulares de trabajo, empoderamiento de cuadrillas operativas y rendición de cuentas (Accountability).",
        "nuevo": "Habilidades de supervisión moderna: delegación efectiva, retroalimentación constructiva (Feedback 1-on-1), gestión de la diversidad generacional en taller y el supervisor como mentor técnico bajo el ideario Kinal.",
        "justificacion": "Las plantas de manufactura en Guatemala requieren supervisores que no sean 'capataces de vigilancia', sino líderes ágiles capaces de alinear los objetivos del turno con los indicadores del negocio.",
        "temario_modernizado": [
            "El rol estratégico del supervisor técnico como mando medio en la empresa",
            "Estructuras organizacionales ágiles y células de manufactura autónomas",
            "Liderazgo operativo: delegación, retroalimentación y rendición de cuentas",
            "Gestión del cambio tecnológico y motivación del personal técnico"
        ]
    },
    {
        "id": "b1_planeacion_control_trabajo",
        "bimestre": "Bimestre 1",
        "periodo": "Periodo 3 (50 min)",
        "nombre": "Planeación y Control para el Trabajo",
        "eje": "Gestión y Supervisión",
        "icono": "⏱️",
        "actual": "Cronogramas manuales en papel, presupuestos estáticos de gasto y sistemas de control por amonestaciones punitivas.",
        "anular": "Gráficas de barras dibujadas a mano en cartulina y control punitivo por memorándums.",
        "actualizar": "Planificación operativa de turnos de trabajo, balanceo de cargas operativas y diagramas de Gantt digitales para paradas de planta y mantenimientos programados.",
        "nuevo": "Gestión visual mediante Tableros Kanban (físicos y digitales: Trello/Notion), cálculo de Eficiencia Global de Equipos (OEE - Overall Equipment Effectiveness = Disponibilidad × Rendimiento × Calidad) y software de gestión de tareas.",
        "justificacion": "Las paradas no programadas en líneas continuas (alimentos, bebidas, plásticos) cuestan miles de quetzales por hora; el supervisor debe dominar la métrica OEE para eliminar las 6 grandes pérdidas de los equipos.",
        "temario_modernizado": [
            "Planificación operativa y secuenciación de órdenes de trabajo en planta",
            "Gestión visual del flujo de trabajo mediante metodología Kanban",
            "Cálculo y análisis de Eficiencia Global de Equipos (OEE)",
            "Diagramas de Gantt dinámicos y software de gestión de proyectos técnicos"
        ]
    },
    {
        "id": "b1_matematica_basica_1",
        "bimestre": "Bimestre 1",
        "periodo": "Periodo 4 (50 min)",
        "nombre": "Matemática Básica 1",
        "eje": "Ciencias Exactas Aplicadas",
        "icono": "📐",
        "actual": "Jerarquía de operaciones básica, regla de tres simple escolar, fracciones manuales y leyes de exponentes abstractas.",
        "anular": "Repaso escolar de primero básico (fracciones manuales heterogéneas, mínimo común múltiplo abstracto sin contexto y regla de tres escolar).",
        "actualizar": "Aritmética cuantitativa y proporcionalidad técnica: razones, factores de escala en planos y especificaciones, porcentajes de variación relativa y absoluta, y cálculo de márgenes operativos.",
        "nuevo": "Modelado Cuantitativo en Hojas de Cálculo (Excel / Sheets): Automatización de fórmulas con referencias relativas y absolutas ($A$1), validación de datos, funciones condicionales y resolución de sistemas de ecuaciones lineales aplicados a balances de recursos y presupuestos.",
        "justificacion": "El supervisor de mando medio en cualquiera de las 7 especialidades necesita calcular rendimientos, presupuestos paramétricos y variaciones de costos sin errores aritméticos, automatizando sus plantillas de cálculo.",
        "temario_modernizado": [
            "Análisis dimensional y conversiones técnicas rigurosas (SI vs. Sistema Inglés)",
            "Proporcionalidad directa e inversa, porcentajes de variación y factores de escala",
            "Modelado y automatización de plantillas de cálculo en Excel (fórmulas y funciones)",
            "Sistemas de ecuaciones lineales aplicados a balance de recursos y presupuestos"
        ]
    },
    {
        "id": "b1_fisica_basica_1",
        "bimestre": "Bimestre 1",
        "periodo": "Periodo 5 (50 min)",
        "nombre": "Física Básica 1",
        "eje": "Física y Tecnología",
        "icono": "⚖️",
        "actual": "Cinemática y dinámica teórica idealizada (tiro parabólico de libro, planos inclinados sin fricción y fórmulas de bachillerato).",
        "anular": "Problemas de física idealizada sin rozamiento, memorización de fórmulas abstractas y análisis complejo de vibraciones mecánicas no aplicable a técnicos generales.",
        "actualizar": "Estática y equilibrio de fuerzas: vectores coplanares, diagramas de cuerpo libre, primera condición de equilibrio (sumatoria F = 0) y segunda condición de equilibrio: torque o momento de fuerza (sumatoria M = 0) para estabilidad de estructuras y equipos.",
        "nuevo": "Trabajo, Potencia y Máquinas Simples: Cálculo de trabajo mecánico (W = F·d), potencia (Watts y HP), rendimiento mecánico y aplicaciones de máquinas simples (poleas fijas/móviles, polipastos de izaje, palancas, planos inclinados y fricción real de anclajes).",
        "justificacion": "Todo mando medio técnico supervisa operaciones de izaje de cargas, fijación de soportes, apriete de pernos o traslado de equipos, donde el equilibrio de fuerzas y la ventaja mecánica son vitales para la seguridad y la integridad física.",
        "temario_modernizado": [
            "Estática de partículas y cuerpos rígidos: vectores de fuerza y equilibrio estático",
            "Momento de una fuerza (Torque): brazo de palanca, apriete seguro y estabilidad",
            "Trabajo mecánico, potencia (Watts / HP), energía y rendimiento mecánico",
            "Máquinas simples y ventaja mecánica: poleas, polipastos, palancas y fricción real"
        ]
    },

    # BIMESTRE 2
    {
        "id": "b2_etica_general_2",
        "bimestre": "Bimestre 2",
        "periodo": "Periodo 1 (50 min)",
        "nombre": "Ética General 2",
        "eje": "Formación Humana y Ética",
        "icono": "⚖️",
        "actual": "Normas básicas de convivencia escolar y repaso de reglamentos internos.",
        "anular": "Análisis superficial de reglamentos disciplinarios sin dilemas morales de ingeniería.",
        "actualizar": "Libertad personal responsable (valor Kinal): la responsabilidad moral, civil y penal de las firmas técnicas en bitácoras, órdenes de trabajo y planos.",
        "nuevo": "Compliance e Integridad Industrial: Prevención de sobornos de proveedores por repuestos genéricos defectuosos, conflicto de intereses en contrataciones y cultura de seguridad psicológica para reportar incidentes sin temor a represalias.",
        "justificacion": "La corrupción técnica (comisiones clandestinas por compra de repuestos de mala calidad) arriesga vidas y causa pérdidas millonarias. El sello ético Kinal forma mandos medios inquebrantables.",
        "temario_modernizado": [
            "Libertad responsable y consecuencias civiles y penales de las decisiones técnicas",
            "La verdad en los reportes: prohibición de falsedad en bitácoras de inspección",
            "Compliance industrial: prevención de sobornos, dádivas y conflicto de intereses",
            "Cultura de seguridad psicológica y reporte transparente de cuasi-accidentes"
        ]
    },
    {
        "id": "b2_herramientas_contables",
        "bimestre": "Bimestre 2",
        "periodo": "Periodo 2 (50 min)",
        "nombre": "Herramientas Contables para la Supervisión",
        "eje": "Gestión y Supervisión",
        "icono": "💰",
        "actual": "Contabilidad mercantil general (partidas dobles, libros diarios y balances para tiendas de comercio al por menor).",
        "anular": "Asientos contables fiscales de partida doble y elaboración de balances generales bancarios no aplicables a un supervisor de taller.",
        "actualizar": "Contabilidad de Costos Industriales: clasificación de costos en Materia Prima Directa (MPD), Mano de Obra Directa (MOD) y Costos Indirectos de Fabricación (CIF).",
        "nuevo": "Control de Costos de Planta: Cálculo del costo real por hora de máquina parada (Downtime Cost), costeo de órdenes de trabajo de mantenimiento y gestión de presupuestos operativos (OPEX de taller) en Excel.",
        "justificacion": "El supervisor de producción o mantenimiento debe ser capaz de justificar económicamente por qué una parada técnica de 2 horas costó Q50,000 en mermas y salarios no devengados.",
        "temario_modernizado": [
            "Estructura de costos industriales: MPD, MOD y Costos Indirectos de Fabricación",
            "Cálculo del costo horario de parada de máquina (Downtime Cost) y mermas",
            "Costeo de órdenes de trabajo de mantenimiento y servicios técnicos",
            "Elaboración y control de presupuestos operativos de área (OPEX) en Excel"
        ]
    },
    {
        "id": "b2_administracion_rrhh_sso",
        "bimestre": "Bimestre 2",
        "periodo": "Periodo 3 (50 min)",
        "nombre": "Administración de RRHH y SSO",
        "eje": "Gestión y Supervisión",
        "icono": "🦺",
        "actual": "Formatos de reclutamiento estándar y botiquín de primeros auxilios general.",
        "anular": "Teoría abstracta de psicología industrial y formatos de contratación de oficina sin base legal laboral guatemalteca.",
        "actualizar": "Legislación Laboral de Guatemala: Código de Trabajo (jornadas diurna, mixta y nocturna, horas extras, asuetos y libro de salarios). Liderazgo de cuadrillas operativas y gestión del clima laboral.",
        "nuevo": "Planillas y Cálculo del IGSS en Guatemala + SSO (Acuerdo 229-2014): Estructura salarial, cuota laboral del IGSS (4.83%), cuota patronal (10.67% IGSS + 1% IRTRA + 1% INTECAP = 12.67%), planilla electrónica (IGSS Digital), libro de salarios, cálculo de finiquitos y prestaciones irrenunciables (Bono 14, Aguinaldo, vacaciones, indemnización) y cumplimiento de SSO con Comités Bipartitos y Matriz IPERC.",
        "justificacion": "El supervisor técnico en Guatemala lidera personal directo y debe dominar la legislación laboral, el cálculo de las deducciones del IGSS y el Acuerdo 229-2014 para evitar multas del MINTRAB y accidentes de trabajo.",
        "temario_modernizado": [
            "Código de Trabajo de Guatemala: jornadas laborales, horas extras y libro de salarios",
            "Cálculo de salarios y planillas del IGSS (cuota laboral 4.83%, patronal 12.67% y finiquitos)",
            "Seguridad y Salud Ocupacional (SSO): Acuerdo Gubernativo 229-2014 y Comités Bipartitos",
            "Matriz IPERC: Identificación de Peligros, Evaluación de Riesgos y Protocolos Críticos"
        ]
    },
    {
        "id": "b2_matematica_basica_2",
        "bimestre": "Bimestre 2",
        "periodo": "Periodo 4 (50 min)",
        "nombre": "Matemática Básica 2",
        "eje": "Ciencias Exactas Aplicadas",
        "icono": "📉",
        "actual": "Factorización algebraica tradicional de trinomios, productos notables abstractos y geometría plana básica.",
        "anular": "Factorización algebraica manual intensiva sin contexto técnico y curvas de maquinaria no transversales.",
        "actualizar": "Modelado de funciones operativas en hojas de cálculo: funciones lineales aplicadas a cálculo de Punto de Equilibrio (Costos Fijos / Margen de Contribución) y funciones exponenciales para depreciación de activos fijos.",
        "nuevo": "Lógica Matemática, Tablas de Verdad y Algoritmos Básicos: Proposiciones lógicas, compuertas lógicas (AND, OR, NOT, XOR), tablas de verdad, funciones lógicas anidadas en Excel (SI, Y, O, BUSCARV/XLOOKUP) y diagramas de flujo normalizados (ANSI/ISO) para diagramación de procesos.",
        "justificacion": "La toma de decisiones de un supervisor técnico requiere modelar el punto de equilibrio de una operación y dominar la lógica formal booleana que sustenta tanto la formulación en Excel como la programación.",
        "temario_modernizado": [
            "Funciones lineales y cálculo de Punto de Equilibrio (Break-Even) en operaciones",
            "Funciones no lineales y modelado de depreciación y degradación en el tiempo",
            "Lógica matemática: proposiciones, tablas de verdad y operadores booleanos (AND/OR/NOT)",
            "Algoritmia básica y diagramación de flujos de procesos técnicos (ANSI/ISO)"
        ]
    },
    {
        "id": "b2_fisica_aplicada_1",
        "bimestre": "Bimestre 2",
        "periodo": "Periodo 5 (50 min)",
        "nombre": "Física Aplicada 1",
        "eje": "Física y Tecnología",
        "icono": "🧱",
        "actual": "Hidrostática básica (principio de Pascal, prensas hidráulicas ideales y vasos comunicantes).",
        "anular": "Temarios hiperespecializados de redes hidráulicas complejas, oleohidráulica pesada o cálculos de bombas no aplicables a carreras como desarrollo de software, construcción o telecomunicaciones.",
        "actualizar": "Física de Materiales y Esfuerzos Mecánicos: Tensión, compresión, cortante, flexión y torsión. Ley de Hooke, módulo de Young (elasticidad), límite elástico y coeficiente de seguridad admisible en proyectos técnicos.",
        "nuevo": "Propiedades Físico-Mecánicas, Térmicas y Dieléctricas: Dureza, tenacidad, fatiga de materiales, dilatación térmica lineal y juntas de expansión; propiedades eléctricas de conductores, aislantes y semiconductores, y criterios de prevención de corrosión.",
        "justificacion": "Todas las especialidades del TSU interactúan con materiales físicos: estructuras de soporte, carcasas de servidores, cables conductores, ductos, chasis o piezas mecánicas. Comprender el esfuerzo, la dilatación y el aislamiento previene fallas catastróficas.",
        "temario_modernizado": [
            "Esfuerzos mecánicos fundamentales (tensión, compresión, corte, torsión) y Ley de Hooke",
            "Propiedades mecánicas y térmicas: elasticidad, fatiga y dilatación térmica",
            "Propiedades eléctricas y dieléctricas de materiales conductores, aislantes y silicio",
            "Criterios de selección de materiales técnicos y prevención de corrosión y fallas"
        ]
    },

    # BIMESTRE 3
    {
        "id": "b3_etica_profesional_1",
        "bimestre": "Bimestre 3",
        "periodo": "Periodo 1 (50 min)",
        "nombre": "Ética Profesional 1",
        "eje": "Formación Humana y Ética",
        "icono": "🤖",
        "actual": "Códigos deontológicos genéricos tradicionales del técnico y reglamentación profesional estática.",
        "anular": "Textos teóricos del siglo XIX sin referencia a las tecnologías digitales ni al impacto del software en el empleo.",
        "actualizar": "La ética de la automatización y el futuro del trabajo: la transición justa. Reentrenamiento de operarios (Reskilling/Upskilling) frente al despido masivo por automatización. La máquina al servicio del ser humano.",
        "nuevo": "Ética en la Inteligencia Artificial Industrial: Detección de sesgos algorítmicos en evaluaciones de desempeño, límites éticos del monitoreo digital de operarios (biometría, cámaras inteligentes) y secreto industrial al usar herramientas de IA generativa.",
        "justificacion": "La adopción de visión artificial y software predictivo en plantas de Guatemala plantea dilemas de privacidad y desplazamiento laboral que el supervisor debe gestionar con criterio humanista.",
        "temario_modernizado": [
            "Automatización y empleo: la transición justa y el reentrenamiento del personal",
            "La primacía de la persona sobre la tecnología en la toma de decisiones fabriles",
            "Ética en IA industrial: sesgos algorítmicos y límites del monitoreo biométrico",
            "Confidencialidad, propiedad intelectual y uso responsable de IA generativa"
        ]
    },
    {
        "id": "b3_metodos_produccion",
        "bimestre": "Bimestre 3",
        "periodo": "Periodo 2 (50 min)",
        "nombre": "Métodos de Producción",
        "eje": "Gestión y Supervisión",
        "icono": "🏭",
        "actual": "Estudios de tiempos y movimientos con cronómetro tradicional y diagramas de operaciones analíticos (OPC).",
        "anular": "Cronometraje punitivo tradicional manual sin participación del operario y formatos estáticos de estudio de métodos.",
        "actualizar": "Balanceo de líneas de ensamble, cálculo de tiempo de ciclo (Takt Time / Cycle Time) y estandarización de procedimientos operativos de trabajo.",
        "nuevo": "Manufactura Esbelta (Lean Manufacturing Aplicado): Identificación y erradicación de los 8 desperdicios industriales (Mudas), Mapeo de Flujo de Valor (VSM - Value Stream Mapping), técnica SMED para cambio rápido de herramientas y talleres Kaizen en piso.",
        "justificacion": "Las multinacionales y exportadoras guatemaltecas (AGEXPORT) exigen estándares de manufactura de clase mundial (WCM) para competir internacionalmente.",
        "temario_modernizado": [
            "Filosofía Lean Manufacturing: identificación y erradicación de los 8 desperdicios",
            "Mapeo de Flujo de Valor (VSM): diagnóstico del estado actual y diseño del futuro",
            "Estandarización del trabajo, balanceo de líneas y sincronización con Takt Time",
            "Técnica SMED para reducción de tiempos de preparación y eventos Kaizen en piso"
        ]
    },
    {
        "id": "b3_servicio_cliente",
        "bimestre": "Bimestre 3",
        "periodo": "Periodo 3 (50 min)",
        "nombre": "Servicio al Cliente",
        "eje": "Gestión y Supervisión",
        "icono": "🤝",
        "actual": "Protocolos de cortesía telefónica, telemercadeo y atención en mostrador de ventas al menudeo.",
        "anular": "Técnicas de venta retail de mostrador, etiqueta telefónica de call center y persuasión comercial al menudeo.",
        "actualizar": "Gestión del Cliente Interno: relación de servicio y colaboración técnica entre el departamento de mantenimiento, ingeniería de planta y producción.",
        "nuevo": "Servicio Técnico Industrial B2B y SLAs: Acuerdos de Nivel de Servicio (Service Level Agreements), gestión de garantías de maquinaria, soporte técnico postventa y espíritu de servicio cristiano-social según Kinal.",
        "justificacion": "El cliente de un supervisor técnico es la gerencia de producción o el cliente corporativo B2B que adquiere maquinaria; la comunicación debe ser técnica y basada en acuerdos de disponibilidad.",
        "temario_modernizado": [
            "El concepto de cliente interno en la planta: sinergia mantenimiento-producción",
            "Acuerdos de Nivel de Servicio (SLA) para disponibilidad de maquinaria",
            "Servicio técnico industrial B2B: soporte postventa y gestión de garantías",
            "El espíritu de servicio en la práctica profesional como sello formativo Kinal"
        ]
    },
    {
        "id": "b3_matematica_aplicada_1",
        "bimestre": "Bimestre 3",
        "periodo": "Periodo 4 (50 min)",
        "nombre": "Matemática Aplicada 1",
        "eje": "Ciencias Exactas Aplicadas",
        "icono": "📊",
        "actual": "Cálculo manual de medias, medianas, modas y elaboración de gráficas de barras en papel.",
        "anular": "Cálculos matemáticos teóricos complejos de Seis Sigma avanzado, reglas de Western Electric de laboratorio y fórmulas estadísticas abstractas que sobrecargan al estudiante.",
        "actualizar": "Estadística Descriptiva Práctica en Hojas de Cálculo: medidas de tendencia central (media, mediana, moda), medidas de dispersión (desviación estándar, varianza) y percentiles aplicados a datos de tiempos, costos y mediciones en Excel.",
        "nuevo": "Análisis Operativo de Datos y Principio de Pareto (80/20): Tablas de distribución de frecuencias, histogramas, diagramas de Pareto para priorización de problemas/defectos, y diagramas de dispersión con líneas de tendencia lineal simple (R y R²) para proyecciones básicas.",
        "justificacion": "El supervisor no necesita estadística teórica universitaria pura, sino dominar la analítica descriptiva en Excel y la ley de Pareto para identificar rápidamente el 20% de las causas que generan el 80% de los retrasos o fallas.",
        "temario_modernizado": [
            "Estadística descriptiva práctica con hojas de cálculo (media, mediana, desviación estándar)",
            "Organización de datos: tablas de frecuencia, histogramas y diagramas de dispersión",
            "Principio de Pareto (Regla 80/20) y estratificación para priorización operativa",
            "Análisis de tendencias, correlación lineal simple (R y R²) y proyecciones básicas"
        ]
    },
    {
        "id": "b3_fisica_aplicada_2",
        "bimestre": "Bimestre 3",
        "periodo": "Periodo 5 (50 min)",
        "nombre": "Física Aplicada 2",
        "eje": "Física y Tecnología",
        "icono": "⚡",
        "actual": "Leyes de gases ideales teóricos (PV=nRT) y experimentos escolares de calorimetría de mezclas de agua.",
        "anular": "Termodinámica pesada de calderas industriales pirotubulares, tablas de vapor saturado y ciclos Rankine de plantas térmicas no aplicables a software, construcción, telecom o electrónica.",
        "actualizar": "Física de la Energía y Balances Operativos: Principio de conservación de la energía (Ein = Eout + Pérdidas), formas de energía (térmica, eléctrica, mecánica) y unidades prácticas de energía y potencia (Joules, BTU, kW y kWh).",
        "nuevo": "Eficiencia Energética, Facturación Eléctrica y Climatización Básica: Cálculo del consumo en kWh y análisis de tarifas eléctricas industriales de Guatemala (EEGSA/ENERGUATE); modos de transferencia de calor y climatización básica (HVAC / enfriamiento de equipos); y fundamentos de energía solar fotovoltaica.",
        "justificacion": "La energía es el principal costo operativo transversal en cualquier empresa técnica: climatización de cuartos de servidores, consumo de talleres, alimentación de radiobases o edificaciones eficientes.",
        "temario_modernizado": [
            "Principios de energía y balances energéticos de entrada y salida (Ein = Eout + Pérdidas)",
            "Potencia eléctrica, consumo en kWh y pliegos tarifarios industriales en Guatemala",
            "Transferencia de calor (conducción, convección, radiación) y climatización básica (HVAC)",
            "Eficiencia energética, fundamentos de energía solar fotovoltaica y sostenibilidad"
        ]
    },

    # BIMESTRE 4
    {
        "id": "b4_etica_profesional_2",
        "bimestre": "Bimestre 4",
        "periodo": "Periodo 1 (50 min)",
        "nombre": "Ética Profesional 2",
        "eje": "Formación Humana y Ética",
        "icono": "🧠",
        "actual": "Conclusiones generales de carrera y código ético de egreso formal.",
        "anular": "Discursos solemnes abstractos sin debate de casos reales de negligencia o impacto tecnológico.",
        "actualizar": "La excelencia moral del 'trabajo bien hecho' (Kinal): rechazo al facilismo del 'copia y pega' de respuestas de IA en memorias técnicas, veracidad de firmas en peritajes y ética ambiental (gestión de residuos peligrosos y e-waste).",
        "nuevo": "El Principio Human-in-the-Loop (HITL) en Operaciones Industriales: La responsabilidad ética y legal jamás se delega en un algoritmo o sistema autónomo. El supervisor humano como tomador de decisiones final en paradas de emergencia, seguridad y sanciones; superación del sesgo de automatización (Automation Bias).",
        "justificacion": "La inteligencia artificial y los algoritmos no van a la cárcel ni tienen conciencia moral. La ley y la ética exigen que haya siempre un ser humano profesionalmente responsable en el bucle de control.",
        "temario_modernizado": [
            "El principio Human-in-the-Loop (HITL): supervisión humana obligatoria en la era IA",
            "Superación del sesgo de automatización (Automation Bias) y juicio crítico técnico",
            "La ética del trabajo bien hecho: rechazo al plagio y honestidad profesional",
            "Responsabilidad ambiental: economía circular y gestión de residuos peligrosos"
        ]
    },
    {
        "id": "b4_control_calidad",
        "bimestre": "Bimestre 4",
        "periodo": "Periodo 2 (50 min)",
        "nombre": "Control de Calidad",
        "eje": "Gestión y Supervisión",
        "icono": "🎯",
        "actual": "Inspección final de piezas por muestreo al término de línea (detección reactiva de defectos a posteriori).",
        "anular": "Control reactivo de calidad que se limita a separar producto no conforme al final sin buscar causas raíz.",
        "actualizar": "Sistemas de Gestión de Calidad (ISO 9001:2015) y las 7 herramientas de Ishikawa: Diagrama Causa-Efecto, Diagrama de Pareto 80/20, estratificación y hojas de verificación.",
        "nuevo": "Aseguramiento de Calidad en la Fuente y Metodología Six Sigma (DMAIC): Dispositivos a prueba de errores (Poka-Yoke), auditorías internas de proceso, matrices AMFE (Análisis Modal de Fallos y Efectos) y estandarización para cero defectos.",
        "justificacion": "Las empresas guatemaltecas exportadoras certificadas en ISO exigen mandos medios que dominen herramientas para erradicar defectos en el origen, no inspectores que cuenten piezas dañadas.",
        "temario_modernizado": [
            "Sistemas de Gestión de Calidad ISO 9001:2015 y enfoque basado en riesgos",
            "Las 7 herramientas clásicas de la calidad para análisis de causas raíz",
            "Aseguramiento en la fuente y diseño de dispositivos Poka-Yoke",
            "Metodología Six Sigma (DMAIC) y Análisis Modal de Fallos y Efectos (AMFE)"
        ]
    },
    {
        "id": "b4_fundamentos_marketing",
        "bimestre": "Bimestre 4",
        "periodo": "Periodo 3 (50 min)",
        "nombre": "Fundamentos del Marketing",
        "eje": "Gestión y Supervisión",
        "icono": "📈",
        "actual": "Las 4 P tradicionales (Producto, Precio, Plaza, Promoción) para productos de consumo masivo de retail.",
        "anular": "Publicidad masiva para televisión, volantes o técnicas de venta de mostrador de supermercado. No tienen aplicación para un mando medio técnico.",
        "actualizar": "Marketing Estratégico B2B para Empresas Industriales: cotización de servicios técnicos, propuesta de valor técnica y compras corporativas.",
        "nuevo": "Business Intelligence y Analítica de Operaciones (Power BI): Sustituir el tiempo de publicidad por dashboards industriales en tiempo real que muestren métricas de producción, calidad y costos para la alta gerencia.",
        "justificacion": "El supervisor técnico interactúa con gerencia presentando informes de productividad; dominar Power BI para exponer datos duros de planta es la habilidad más cotizada hoy en Guatemala.",
        "temario_modernizado": [
            "Fundamentos de marketing industrial B2B y compras corporativas",
            "Diseño de propuestas técnicas de valor y cotización de proyectos",
            "Business Intelligence: conexión y modelado de datos de producción",
            "Construcción de Dashboards en Power BI con KPIs en tiempo real para gerencia"
        ]
    },
    {
        "id": "b4_matematica_aplicada_2",
        "bimestre": "Bimestre 4",
        "periodo": "Periodo 4 (50 min)",
        "nombre": "Matemática Aplicada 2 (Ingeniería Económica)",
        "eje": "Ciencias Exactas Aplicadas",
        "icono": "🏦",
        "actual": "Definiciones cualitativas del valor del dinero en el tiempo y fuentes de crédito bancario.",
        "anular": "Teoría monetaria macroeconómica que no incide en la toma de decisiones técnicas de taller.",
        "actualizar": "Tasas de interés nominales vs. efectivas (TEA), inflación y depreciación de activos fijos según la ley del ISR de Guatemala (línea recta).",
        "nuevo": "Interés Compuesto y Evaluación Financiera de Inversiones: Fórmulas de interés compuesto, valor futuro (VF), valor presente (VP), anualidades y tablas de amortización (método francés y alemán). Evaluación de proyectos de automatización: VPN (Valor Presente Neto), TIR (Tasa Interna de Retorno), Payback y análisis de reemplazo de maquinaria (¿reparar o sustituir?).",
        "justificacion": "Para que la gerencia apruebe la compra de un variador de frecuencia o un robot, el supervisor debe demostrar que el VPN es positivo y que el Payback es menor a 18 meses gracias al ahorro eléctrico.",
        "temario_modernizado": [
            "Interés compuesto, tasas nominales vs. efectivas y valor del dinero en el tiempo",
            "Anualidades y tablas de amortización de préstamos y leasing industrial",
            "Evaluación de proyectos técnicos: Valor Presente Neto (VPN) y TIR",
            "Análisis de reemplazo de maquinaria y Costo de Ciclo de Vida del Activo (LCC)"
        ]
    },
    {
        "id": "b4_fisica_aplicada_3",
        "bimestre": "Bimestre 4",
        "periodo": "Periodo 5 (50 min)",
        "nombre": "Física Aplicada 3",
        "eje": "Física y Tecnología",
        "icono": "💻",
        "actual": "Leyes de Ohm, Watts y Kirchhoff en circuitos simples de corriente continua (DC).",
        "anular": "Electricidad trifásica pesada especializada de subestaciones y telemetría compleja de vibraciones mecánicas que no aplica transversalmente a todas las especialidades.",
        "actualizar": "Fundamentos Físicos de Medición y Sensores Transversales: Principios de transductores para medición de variables físicas (sensores de temperatura, presencia/proximidad, nivel, presión y ópticos); lectura de entradas digitales y señales analógicas escaladas.",
        "nuevo": "Lógica de Programación Aplicada con Python: Sintaxis práctica de Python para técnicos (variables, condicionales if/else, bucles for/while, funciones), automatización de cálculos repetitivos, procesamiento de archivos de datos (CSV) y generación de gráficos técnicos con librerías estándar (matplotlib).",
        "justificacion": "La industria moderna 4.0 exige que todo mando medio técnico, sin importar su especialidad, posea pensamiento computacional, sepa interpretar datos de sensores y pueda escribir scripts básicos para automatizar tareas y reportes.",
        "temario_modernizado": [
            "Fundamentos físicos de medición: sensores y transductores transversales de planta",
            "Lógica de programación y sintaxis básica de Python (variables, condicionales, bucles)",
            "Automatización de cálculos técnicos, funciones y procesamiento de archivos CSV",
            "Visualización gráfica de datos técnicos (matplotlib) y scripts de automatización"
        ]
    }
]

# TEMPLATE HTML BASE
def generate_course_html(course, all_courses):
    # Generar links de navegación rápida
    nav_links = ""
    for c in all_courses:
        active_class = 'class="active"' if c["id"] == course["id"] else ""
        nav_links += f'<a href="{c["id"]}.html" {active_class}>{c["bimestre"]}: {c["nombre"]}</a>\n'

    temario_items = "".join([f"<li>{item}</li>" for item in course["temario_modernizado"]])

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{course["nombre"]} ({course["bimestre"]}) | Dictamen Curricular TSU Kinal</title>
    <style>
        :root {{
            --kinal-blue: #0f2d59;
            --kinal-accent: #d97706;
            --kinal-light: #f8fafc;
            --text-dark: #1e293b;
            --text-muted: #64748b;
            --border-color: #cbd5e1;
            --color-actualizar-bg: #fef9c3;
            --color-actualizar-text: #854d0e;
            --color-actualizar-border: #facc15;
            --color-anular-bg: #fee2e2;
            --color-anular-text: #991b1b;
            --color-anular-border: #f87171;
            --color-nuevo-bg: #dbeafe;
            --color-nuevo-text: #1e40af;
            --color-nuevo-border: #60a5fa;
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
            max-width: 1200px;
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
            padding: 32px 40px;
            border-bottom: 4px solid var(--kinal-accent);
        }}
        .header-meta {{
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
            margin-bottom: 12px;
        }}
        .header-badge {{
            display: inline-block;
            background: rgba(217, 119, 6, 0.25);
            color: #fef08a;
            border: 1px solid var(--kinal-accent);
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.82rem;
            font-weight: 600;
            letter-spacing: 0.5px;
            text-transform: uppercase;
        }}
        .header-badge-alt {{
            display: inline-block;
            background: rgba(255, 255, 255, 0.15);
            color: #ffffff;
            border: 1px solid rgba(255,255,255,0.3);
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.82rem;
            font-weight: 600;
        }}
        header h1 {{ font-size: 2rem; font-weight: 700; margin-bottom: 6px; display: flex; align-items: center; gap: 12px; }}
        header p {{ color: #cbd5e1; font-size: 0.98rem; }}
        nav.nav-bar {{
            background: #0b1f3a;
            padding: 0 40px;
            display: flex;
            gap: 12px;
            overflow-x: auto;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }}
        nav.nav-bar a {{
            color: #94a3b8;
            text-decoration: none;
            padding: 12px 14px;
            font-weight: 600;
            font-size: 0.85rem;
            display: inline-block;
            border-bottom: 3px solid transparent;
            transition: all 0.2s;
            white-space: nowrap;
        }}
        nav.nav-bar a:hover {{ color: #ffffff; border-bottom-color: var(--kinal-accent); }}
        nav.nav-bar a.active {{ color: #ffffff; background: rgba(255,255,255,0.08); border-bottom-color: var(--kinal-accent); }}
        
        main {{ padding: 36px 40px; }}

        .tag-pill {{
            display: inline-block;
            padding: 4px 10px;
            border-radius: 4px;
            font-size: 0.8rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.4px;
        }}
        .tag-actualizar {{ background: var(--color-actualizar-bg); color: var(--color-actualizar-text); border: 1px solid var(--color-actualizar-border); }}
        .tag-anular {{ background: var(--color-anular-bg); color: var(--color-anular-text); border: 1px solid var(--color-anular-border); }}
        .tag-nuevo {{ background: var(--color-nuevo-bg); color: var(--color-nuevo-text); border: 1px solid var(--color-nuevo-border); }}

        .table-dictamen {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
            font-size: 0.92rem;
            box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        }}
        .table-dictamen th, .table-dictamen td {{
            padding: 14px 16px;
            border: 1px solid var(--border-color);
            vertical-align: top;
            text-align: left;
        }}
        .table-dictamen th {{
            background: #f8fafc;
            color: var(--kinal-blue);
            font-weight: 700;
        }}

        .callout-box {{
            padding: 16px 20px;
            border-radius: 8px;
            margin: 18px 0;
            font-size: 0.92rem;
        }}
        .callout-yellow {{ background: var(--color-actualizar-bg); border-left: 4px solid var(--color-actualizar-border); color: var(--color-actualizar-text); }}
        .callout-red {{ background: var(--color-anular-bg); border-left: 4px solid var(--color-anular-border); color: var(--color-anular-text); }}
        .callout-blue {{ background: var(--color-nuevo-bg); border-left: 4px solid var(--color-nuevo-border); color: var(--color-nuevo-text); }}

        .proposito-card {{
            background: #f8fafc;
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 24px;
            margin: 24px 0;
        }}
        .proposito-card h3 {{
            color: var(--kinal-blue);
            margin-bottom: 12px;
            font-size: 1.15rem;
        }}
        .proposito-card ul {{
            padding-left: 20px;
            color: var(--text-dark);
        }}
        .proposito-card li {{
            margin-bottom: 8px;
        }}

        .pagination-bar {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 36px;
            padding-top: 20px;
            border-top: 1px solid #e2e8f0;
        }}
        .pagination-bar a {{
            color: var(--kinal-blue);
            text-decoration: none;
            font-weight: 600;
            font-size: 0.9rem;
            padding: 8px 16px;
            border-radius: 6px;
            border: 1px solid var(--border-color);
            background: #ffffff;
            transition: all 0.2s;
        }}
        .pagination-bar a:hover {{
            background: var(--kinal-blue);
            color: #ffffff;
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
        <div class="header-meta">
            <span class="header-badge">{course["bimestre"]}</span>
            <span class="header-badge-alt">{course["periodo"]}</span>
            <span class="header-badge-alt">{course["eje"]}</span>
        </div>
        <h1><span>{course["icono"]}</span> {course["nombre"]}</h1>
        <p>Dictamen curricular técnico, pertinencia para mandos medios en Guatemala y propuesta modernizada conforme al ideario de Fundación Kinal.</p>
    </header>

    <nav class="nav-bar">
        <a href="index.html">← Menú Principal TSU</a>
        <a href="mapa_curricular.html" style="color: #67e8f9; font-weight: 700;">🗺️ Mapa Curricular</a>
        <a href="temarios_por_linea.html" style="color: #a7f3d0; font-weight: 700;">📚 Temarios por Línea</a>
        <a href="nueva_distribucion_tematica_tsu.html" style="color: #fef08a; font-weight: 700;">🌟 Nueva Distribución 2026</a>
        {nav_links}
    </nav>

    <main>
        <h2 style="color: var(--kinal-blue); margin-bottom: 16px;">Auditoría Curricular y Matriz de Actualización</h2>
        
        <table class="table-dictamen">
            <thead>
                <tr>
                    <th style="width: 25%;">Dimensión Curricular</th>
                    <th style="width: 15%;">Dictamen</th>
                    <th style="width: 60%;">Contenido y Diagnóstico</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td><strong>Contenido Original (Pensum 2026)</strong></td>
                    <td><span class="tag-pill" style="background:#e2e8f0; color:#334155;">Original</span></td>
                    <td>{course["actual"]}</td>
                </tr>
                <tr style="background: #fff5f5;">
                    <td><strong>Lo que vale la pena Anular</strong></td>
                    <td><span class="tag-pill tag-anular">Anular</span></td>
                    <td>
                        <div class="callout-box callout-red" style="margin: 0; padding: 10px 14px;">
                            <strong>Eliminación justificada:</strong> {course["anular"]}
                        </div>
                    </td>
                </tr>
                <tr style="background: #fefce8;">
                    <td><strong>Contenidos a Actualizar</strong></td>
                    <td><span class="tag-pill tag-actualizar">Actualizar</span></td>
                    <td>
                        <div class="callout-box callout-yellow" style="margin: 0; padding: 10px 14px;">
                            <strong>Modernización técnica:</strong> {course["actualizar"]}
                        </div>
                    </td>
                </tr>
                <tr style="background: #eff6ff;">
                    <td><strong>Nuevos Conocimientos</strong></td>
                    <td><span class="tag-pill tag-nuevo">Nuevo</span></td>
                    <td>
                        <div class="callout-box callout-blue" style="margin: 0; padding: 10px 14px;">
                            <strong>Innovación y Demanda 2026:</strong> {course["nuevo"]}
                        </div>
                    </td>
                </tr>
            </tbody>
        </table>

        <div class="callout-box callout-blue">
            <strong>Justificación y Demanda del Mercado Guatemalteco (CIG / AGEXPORT):</strong><br>
            {course["justificacion"]}
        </div>

        <div class="proposito-card">
            <h3>Temario Modernizado Propuesto (Propuesta Curricular Kinal 2026)</h3>
            <ul>
                {temario_items}
            </ul>
        </div>

        <div style="background: #f1f5f9; padding: 18px 24px; border-radius: 8px; font-size: 0.9rem; color: #475569;">
            <strong>Alineación con el Ideario Kinal:</strong> El curso fomenta el principio del <em>"trabajo bien hecho"</em>, el espíritu de servicio y el rigor técnico. Nota mínima aprobatoria institucional: <strong>&ge; 75 puntos sobre 100</strong>.
        </div>

        <div class="pagination-bar">
            <a href="index.html">← Volver al Portal General TSU</a>
            <span style="font-size: 0.88rem; color: var(--text-muted);">{course["bimestre"]} • {course["nombre"]}</span>
        </div>
    </main>

    <footer>
        Fundación Kinal • Escuela Técnica Superior • Técnico Superior Universitario (TSU) • Convenio Universidad del Istmo (UNIS) • Guatemala, 2026
    </footer>
</div>

</body>
</html>
"""
    return html

# GENERAR LOS 20 ARCHIVOS HTML
for course in courses:
    html_content = generate_course_html(course, courses)
    file_path = os.path.join(base_dir, f"{course['id']}.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    # Mirror en MyBrain
    mybrain_path = os.path.join(mybrain_dir, f"{course['id']}.html")
    with open(mybrain_path, "w", encoding="utf-8") as f:
        f.write(html_content)

print(f"Generados exitosamente los 20 cursos en {base_dir}")
