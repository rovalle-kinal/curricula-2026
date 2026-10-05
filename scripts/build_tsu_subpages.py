#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_tsu_subpages.py
Genera:
1. TSU/temarios_por_linea.html: Sub-página interactiva para visualizar todos los temarios organizados por temática o línea de estudio.
2. TSU/mapa_curricular.html: Mapa curricular interactivo con Rejilla Curricular Matriz Y Red de Correlatividades SVG interactiva.
3. Actualización de navbars en TSU/index.html y TSU/nueva_distribucion_tematica_tsu.html.
"""

import os
import json

base_dir = "/Users/arqovalle/Library/CloudStorage/OneDrive-Personal/Software/Antigravity/Diseño Instruccional/TSU"
mybrain_dir = "/Users/arqovalle/Library/CloudStorage/OneDrive-Personal/MyBrain/MyBrain/01 - My Brain/Kinal/TSU"

os.makedirs(base_dir, exist_ok=True)
os.makedirs(mybrain_dir, exist_ok=True)

# -------------------------------------------------------------
# DEFINICIÓN EXHAUSTIVA DE LAS LÍNEAS DE ESTUDIO Y CURSOS
# -------------------------------------------------------------
lineas_estudio = [
    {
        "id": "linea-etica",
        "nombre": "Formación Humana, Ética Profesional y Gobernanza IA",
        "icono": "🛡️",
        "color_accent": "#0284c7",
        "color_bg": "#f0f9ff",
        "color_border": "#bae6fd",
        "descripcion": "Eje transversal axiológico centrado en la dignidad inalienable de la persona, la libertad responsable, la cultura de compliance y la supervisión humana indelegable (Human-in-the-Loop) en sistemas autónomos, fundamentado en el ideario de Kinal.",
        "cursos_ids": ["b1_etica_general_1", "b2_etica_general_2", "b3_etica_profesional_1", "b4_etica_profesional_2"]
    },
    {
        "id": "linea-gestion",
        "nombre": "Gestión de Operaciones, Supervisión y Productividad Industrial",
        "icono": "📋",
        "color_accent": "#d97706",
        "color_bg": "#fffbeb",
        "color_border": "#fde68a",
        "descripcion": "Eje de liderazgo y administración técnica de mandos medios: planificación con gestión visual (Kanban/OEE), legislación laboral guatemalteca (IGSS/Acuerdo 229-2014), costos industriales, manufactura esbelta (Lean/5S), calidad Six Sigma y Business Intelligence con Power BI.",
        "cursos_ids": [
            "b1_fundamentos_administracion", "b1_planeacion_control_trabajo",
            "b2_herramientas_contables", "b2_administracion_rrhh_sso",
            "b3_metodos_produccion", "b3_servicio_cliente",
            "b4_control_calidad", "b4_fundamentos_marketing"
        ]
    },
    {
        "id": "linea-matematica",
        "nombre": "Ciencias Exactas Aplicadas y Analítica Cuantitativa",
        "icono": "📐",
        "color_accent": "#16a34a",
        "color_bg": "#f0fdf4",
        "color_border": "#bbf7d0",
        "descripcion": "Eje de razonamiento cuantitativo e instrumental: desde la proporcionalidad y modelado automatizado en Excel, pasando por el punto de equilibrio y lógica booleana, hasta la analítica descriptiva (Pareto) y la ingeniería económica (VPN, TIR, Payback) para sustentar inversiones de capital.",
        "cursos_ids": ["b1_matematica_basica_1", "b2_matematica_basica_2", "b3_matematica_aplicada_1", "b4_matematica_aplicada_2"]
    },
    {
        "id": "linea-fisica",
        "nombre": "Física Aplicada, Energía, Tecnología e Industria 4.0",
        "icono": "⚡",
        "color_accent": "#7c3aed",
        "color_bg": "#f5f3ff",
        "color_border": "#ddd6fe",
        "descripcion": "Eje de fundamentación física transversal e Industria 4.0: estática e izaje seguro, física de materiales y esfuerzos mecánicos, balances energéticos y tarifas industriales (EEGSA/ENERGUATE), hasta sensores industriales y programación técnica con Python.",
        "cursos_ids": ["b1_fisica_basica_1", "b2_fisica_aplicada_1", "b3_fisica_aplicada_2", "b4_fisica_aplicada_3"]
    }
]

cursos_data = {
    "b1_etica_general_1": {
        "id": "b1_etica_general_1",
        "codigo": "B1-C1",
        "nombre": "Ética General 1",
        "subtitulo": "Antropología y Sentido Trascendente del Trabajo",
        "bimestre": "Bimestre 1",
        "bimestre_num": 1,
        "periodo": "Periodo 1 (50 min)",
        "linea_id": "linea-etica",
        "eje": "Formación Humana y Ética",
        "icono": "🛡️",
        "horas": "13.5 hrs (15 sesiones)",
        "prerequisitos": [],
        "prerequisitos_texto": "Ingreso al 3er Año TSU (2 años previos de especialidad técnica)",
        "habilita": ["b2_etica_general_2", "b2_administracion_rrhh_sso"],
        "habilita_texto": "Ética General 2 (B2-C1) y base axiológica para Administración de RRHH y SSO (B2-C3)",
        "objetivo_transversal": "Forjar el carácter ético del supervisor técnico bajo el ideario de Kinal: la persona en el centro de la operación y el trabajo bien hecho como medio de superación personal y servicio a la sociedad.",
        "unidades": [
            {
                "num": "Unidad 1",
                "titulo": "La Dignidad Inalienable de la Persona Humana en el Entorno Laboral",
                "temas": [
                    "Fundamentación antropológica: la persona como fin supremo y nunca como mero recurso o engranaje de producción",
                    "Diferencia cualitativa entre el trabajo humano y la operación mecánica automatizada",
                    "Respeto a la integridad física, psicológica y moral del trabajador en taller y obra civil",
                    "El deber de crear condiciones de trabajo seguras, justas y humanizadoras"
                ]
            },
            {
                "num": "Unidad 2",
                "titulo": "El Trabajo como Vocación, Perfeccionamiento y Servicio (Ideario Kinal)",
                "temas": [
                    "El trabajo bien hecho: principio de excelencia, cuidado de los detalles y superación de la mediocridad",
                    "El sentido de servicio al prójimo: transformar la tarea diaria en aportación social constructiva",
                    "Santificación de las tareas ordinarias: convertir el quehacer técnico en escuela de virtudes humanas",
                    "Laboriosidad, puntualidad, orden y custodia de herramientas como manifestaciones de respeto personal"
                ]
            },
            {
                "num": "Unidad 3",
                "titulo": "Inteligencia Emocional, Autodominio y Templanza en la Supervisión",
                "temas": [
                    "Autoconocimiento y gestión de emociones bajo la presión de entregas, paradas de planta y emergencias",
                    "Templanza y serenidad del mando medio frente a la frustración y los contratiempos operacionales",
                    "Erradicación del autoritarismo, el trato despectivo y el abuso verbal en cuadrillas de trabajo",
                    "Empatía operativa: escuchar las circunstancias personales del personal a cargo sin descuidar el objetivo"
                ]
            },
            {
                "num": "Unidad 4",
                "titulo": "Comunicación Asertiva y Resolución Pacífica de Conflictos",
                "temas": [
                    "Principios de comunicación no violenta aplicados al diálogo entre jefaturas y operarios",
                    "Técnicas de mediación y arbitraje en discrepancias técnicas entre departamentos de soporte y producción",
                    "Conversaciones difíciles: cómo corregir el error técnico preservando intacta la dignidad de la persona",
                    "Fomento de un clima de fraternidad laboral y colaboración interdepartamental en la empresa"
                ]
            }
        ],
        "subtema_ia": "Sesgos cognitivos humanos frente a sesgos en modelos de IA: el papel irremplazable de la conciencia moral y el juicio prudencial que ninguna máquina o algoritmo predictivo puede replicar.",
        "herramientas": "Casos de estudio de dilemas éticos industriales, matriz de resolución pacífica de fricciones operativas, protocolos de retroalimentación constructiva.",
        "aplicabilidad_7": "Permite resolver con templanza y justicia disputas en cuadrillas de albañiles en construcción, mecánicos bajo estrés por entrega de flota en taller automotriz, desarrolladores con plazos límite de software o brigadas de electricistas en turno nocturno.",
        "dictamen_link": "b1_etica_general_1.html"
    },

    "b1_fundamentos_administracion": {
        "id": "b1_fundamentos_administracion",
        "codigo": "B1-C2",
        "nombre": "Fundamentos de la Administración",
        "subtitulo": "Liderazgo Ágil de Mandos Medios y Coordinación de Equipos",
        "bimestre": "Bimestre 1",
        "bimestre_num": 1,
        "periodo": "Periodo 2 (50 min)",
        "linea_id": "linea-gestion",
        "eje": "Gestión y Supervisión",
        "icono": "📋",
        "horas": "13.5 hrs (15 sesiones)",
        "prerequisitos": [],
        "prerequisitos_texto": "Ingreso al 3er Año TSU",
        "habilita": ["b1_planeacion_control_trabajo", "b2_herramientas_contables", "b2_administracion_rrhh_sso", "b3_metodos_produccion"],
        "habilita_texto": "Planeación y Control (B1-C3), Herramientas Contables (B2-C2), Administración de RRHH y SSO (B2-C3) y Métodos de Producción (B3-C2)",
        "objetivo_transversal": "Dotar al técnico de competencias de supervisión moderna y liderazgo ágil para articular el puente operativo entre la alta gerencia y el personal de piso.",
        "unidades": [
            {
                "num": "Unidad 1",
                "titulo": "El Rol Estratégico del Supervisor Técnico de Mando Medio",
                "temas": [
                    "De ejecutor técnico a coordinador de personas y procesos: el cambio de paradigma profesional",
                    "El supervisor como canal de doble vía: traducir directrices gerenciales a lenguaje técnico y viceversa",
                    "Definición y seguimiento de metas SMART en áreas operativas y técnicas",
                    "Rendición de cuentas (Accountability): asumir la responsabilidad por los resultados del equipo"
                ]
            },
            {
                "num": "Unidad 2",
                "titulo": "Estructuras Organizacionales Ágiles y Células de Trabajo",
                "temas": [
                    "Superación del organigrama piramidal rígido: organizaciones orientadas al flujo de valor",
                    "Células de trabajo autónomas y equipos multifuncionales en manufactura y servicios técnicos",
                    "Matrices de asignación de responsabilidades RACI (Responsable, Aprobador, Consultado, Informado)",
                    "Coordinación interfuncional entre mantenimiento, calidad, compras y operaciones"
                ]
            },
            {
                "num": "Unidad 3",
                "titulo": "Delegación Efectiva y Retroalimentación Constructiva (Feedback)",
                "temas": [
                    "Niveles de delegación: desde la instrucción paso a paso hasta la autonomía guiada",
                    "Superación de la trampa del micromanagement: supervisar objetivos y entregables, no minutos",
                    "Estructura de sesiones individuales de retroalimentación (Feedback 1-on-1)",
                    "El supervisor como mentor técnico y formador de aprendices bajo la filosofía dual de Kinal"
                ]
            },
            {
                "num": "Unidad 4",
                "titulo": "Gestión del Cambio Tecnológico y Diversidad Generacional",
                "temas": [
                    "Resistencia al cambio: causas psicológicas y operacionales frente a la digitalización",
                    "Técnicas de gestión del cambio (Modelo Kotter adaptado a entornos de planta y obra)",
                    "Convivencia y sinergia entre técnicos experimentados tradicionales y jóvenes nativos digitales",
                    "Clima organizacional positivo y motivación intrínseca orientada al trabajo bien hecho"
                ]
            }
        ],
        "subtema_ia": "Uso de asistentes de IA generativa (Copilots) para redacción ejecutiva de descriptores de puestos, actas técnicas de reunión, políticas operativas y minutas de seguimiento.",
        "herramientas": "Matrices RACI, plataformas de documentación (Notion / Confluence), plantillas de feedback 1-on-1, tableros de objetivos SMART.",
        "aplicabilidad_7": "Habilita coordinar cuadrillas de construcción civil, células Scrum de desarrollo de software, brigadas de mantenimiento eléctrico y líneas de ensamble mecánico.",
        "dictamen_link": "b1_fundamentos_administracion.html"
    },

    "b1_planeacion_control_trabajo": {
        "id": "b1_planeacion_control_trabajo",
        "codigo": "B1-C3",
        "nombre": "Planeación y Control para el Trabajo",
        "subtitulo": "Metodología Visual Kanban, Cronogramas Gantt y Eficiencia OEE",
        "bimestre": "Bimestre 1",
        "bimestre_num": 1,
        "periodo": "Periodo 3 (50 min)",
        "linea_id": "linea-gestion",
        "eje": "Gestión y Supervisión",
        "icono": "⏱️",
        "horas": "13.5 hrs (15 sesiones)",
        "prerequisitos": ["b1_fundamentos_administracion"],
        "prerequisitos_texto": "Fundamentos de la Administración (B1-C2) [simultáneo o correlativo]",
        "habilita": ["b3_metodos_produccion", "b4_control_calidad"],
        "habilita_texto": "Métodos de Producción / Lean Manufacturing (B3-C2) y Control de Calidad / Six Sigma (B4-C2)",
        "objetivo_transversal": "Capacitar en la planificación operativa de órdenes de servicio mediante gestión visual, control riguroso de tiempos de ciclo y maximización del indicador OEE.",
        "unidades": [
            {
                "num": "Unidad 1",
                "titulo": "Secuenciación y Balanceo de Órdenes de Trabajo (OT)",
                "temas": [
                    "Flujo de órdenes de trabajo (OT) desde su emisión hasta el cierre y auditoría de campo",
                    "Priorización operativa de tareas técnicas: matrices de impacto vs. urgencia (Eisenhower)",
                    "Balanceo de cargas horarias entre cuadrillas operativas para evitar cuellos de botella",
                    "Gestión de imprevistos y reprogramación ágil sin comprometer compromisos de entrega"
                ]
            },
            {
                "num": "Unidad 2",
                "titulo": "Gestión Visual del Flujo de Trabajo mediante Metodología Kanban",
                "temas": [
                    "Principios de gestión visual: hacer visible lo invisible para transparentar el avance",
                    "Estructura de tableros Kanban: Por Hacer (To Do), En Proceso (In Progress), En Validación, Completado",
                    "Límites de Trabajo en Proceso (WIP Limits): cómo reducir el multitargeting ineficiente",
                    "Implementación de tableros Kanban físicos en taller y digitales (Trello / Notion / ClickUp)"
                ]
            },
            {
                "num": "Unidad 3",
                "titulo": "Eficiencia Global de Equipos (OEE - Overall Equipment Effectiveness)",
                "temas": [
                    "Los tres factores del OEE: Disponibilidad × Rendimiento × Calidad",
                    "Las 6 grandes pérdidas de la maquinaria industrial y equipos de soporte",
                    "Cálculo práctico de pérdidas por paradas no planificadas, microparadas y piezas defectuosas",
                    "Estrategias de planta para elevar el OEE de niveles mediocres (<60%) a clase mundial (>85%)"
                ]
            },
            {
                "num": "Unidad 4",
                "titulo": "Cronogramas Gantt Dinámicos y Software de Proyectos Técnicos",
                "temas": [
                    "Estructura de Desglose del Trabajo (EDT / WBS) para proyectos y mantenimientos mayores",
                    "Construcción de diagramas de Gantt con dependencias (Fin a Inicio, Inicio a Inicio)",
                    "Identificación de la Ruta Crítica (CPM) y holguras operativas",
                    "Uso de software de gestión de proyectos (MS Project / GanttProject / Excel avanzado)"
                ]
            }
        ],
        "subtema_ia": "Algoritmos de IA para estimación predictiva de duración de tareas técnicas basadas en registros históricos y detección temprana de cuellos de botella en cronogramas complejos.",
        "herramientas": "Trello, ClickUp, plantillas automatizadas de OEE en Excel, MS Project / GanttProject.",
        "aplicabilidad_7": "Monitoreo de tiempos de bahía en taller automotriz, avance semanal de obra civil, planificación de sprints de software, paradas de mantenimiento mayor en plantas mecánicas e instalaciones de enlaces telecom.",
        "dictamen_link": "b1_planeacion_control_trabajo.html"
    },

    "b1_matematica_basica_1": {
        "id": "b1_matematica_basica_1",
        "codigo": "B1-C4",
        "nombre": "Matemática Básica 1",
        "subtitulo": "Aritmética Cuantitativa, Proporcionalidad y Modelado en Hojas de Cálculo",
        "bimestre": "Bimestre 1",
        "bimestre_num": 1,
        "periodo": "Periodo 4 (50 min)",
        "linea_id": "linea-matematica",
        "eje": "Ciencias Exactas Aplicadas",
        "icono": "📐",
        "horas": "13.5 hrs (15 sesiones)",
        "prerequisitos": [],
        "prerequisitos_texto": "Bachillerato / Perito Técnico en especialidad",
        "habilita": ["b2_matematica_basica_2", "b2_herramientas_contables", "b1_fisica_basica_1"],
        "habilita_texto": "Matemática Básica 2 (B2-C4), Herramientas Contables (B2-C2) y Física Básica 1 (B1-C5)",
        "objetivo_transversal": "Desarrollar el razonamiento cuantitativo y proporcional para estimar rendimientos, calcular factores de escala y automatizar hojas de cálculo técnicas sin errores conceptuales ni de redondeo.",
        "unidades": [
            {
                "num": "Unidad 1",
                "titulo": "Análisis Dimensional y Conversiones Técnicas Rigurosas",
                "temas": [
                    "Coexistencia de sistemas en la industria guatemalteca: Sistema Internacional (SI) vs. Sistema Inglés",
                    "Factores de conversión para presión (PSI, bar, kPa), caudal (GPM, L/min, m³/h) y potencia (HP, kW, BTU/h)",
                    "Análisis dimensional para verificación de consistencia en ecuaciones técnicas y fórmulas de campo",
                    "Cálculo riguroso de tolerancias mecánicas y eléctricas: porcentajes de error admisible"
                ]
            },
            {
                "num": "Unidad 2",
                "titulo": "Proporcionalidad, Razones, Porcentajes y Escalas de Planos",
                "temas": [
                    "Proporcionalidad directa e inversa aplicada a mezclas industriales, dosificaciones y rendimientos",
                    "Cálculo de variaciones porcentuales relativas y absolutas en costos, tiempos y mermas",
                    "Factores de escala en planos arquitectónicos, mecánicos y diagramas unifilares (1:50, 1:100, 1:20)",
                    "Regla de tres compuesta aplicada a rendimientos de cuadrillas y tiempos de mecanizado"
                ]
            },
            {
                "num": "Unidad 3",
                "titulo": "Modelado Cuantitativo y Automatización en Hojas de Cálculo (Excel)",
                "temas": [
                    "Estructura profesional de plantillas de cálculo: celdas de entrada, fórmulas y reportes ejecutivos",
                    "Dominio de referencias relativas, absolutas ($A$1) y mixtas ($A1, A$1)",
                    "Funciones matemáticas, estadísticas básicas y funciones lógicas anidadas (SI, Y, O)",
                    "Validación de datos, formato condicional para alertas de límites técnicos y auditoría de fórmulas"
                ]
            },
            {
                "num": "Unidad 4",
                "titulo": "Sistemas de Ecuaciones Lineales Aplicados a Recursos y Presupuestos",
                "temas": [
                    "Formulación matemática de problemas operativos con múltiples restricciones de recursos",
                    "Resolución de sistemas lineales de 2 y 3 incógnitas aplicados a balance de materiales y mezclas",
                    "Uso de matrices básicas y herramientas de cálculo en hoja electrónica (función MINVERSA, MMULT)",
                    "Resolución gráfica y analítica de equilibrios operativos y asignación de personal"
                ]
            }
        ],
        "subtema_ia": "Uso de asistentes de IA generativa para formulación, depuración y explicación de fórmulas matriciales complejas en Excel y detección automática de errores de sintaxis y circularidad.",
        "herramientas": "Microsoft Excel / Google Sheets avanzado, plantillas paramétricas de cálculo técnico.",
        "aplicabilidad_7": "Cálculo de rendimientos y cubicajes en construcción, estimación de horas/costos por sprint en software, balance de cargas en electricidad y telecomunicaciones, presupuestos de reparación mecánica y automotriz.",
        "dictamen_link": "b1_matematica_basica_1.html"
    },

    "b1_fisica_basica_1": {
        "id": "b1_fisica_basica_1",
        "codigo": "B1-C5",
        "nombre": "Física Básica 1",
        "subtitulo": "Estática, Equilibrio de Fuerzas, Torque, Trabajo y Máquinas Simples",
        "bimestre": "Bimestre 1",
        "bimestre_num": 1,
        "periodo": "Periodo 5 (50 min)",
        "linea_id": "linea-fisica",
        "eje": "Física y Tecnología",
        "icono": "⚖️",
        "horas": "13.5 hrs (15 sesiones)",
        "prerequisitos": [],
        "prerequisitos_texto": "Conocimientos básicos de ciencias y matemáticas",
        "habilita": ["b2_fisica_aplicada_1"],
        "habilita_texto": "Física Aplicada 1 / Resistencia de Materiales (B2-C5)",
        "objetivo_transversal": "Comprender los principios físicos del equilibrio de fuerzas, momento de torsión, trabajo mecánico y ventaja mecánica aplicados a la seguridad de izaje y estabilidad de equipos.",
        "unidades": [
            {
                "num": "Unidad 1",
                "titulo": "Estática y Primera Condición de Equilibrio (Sumatoria F = 0)",
                "temas": [
                    "Vectores coplanares: suma de fuerzas por componentes rectangulares y método del polígono",
                    "Diagramas de Cuerpo Libre (DCL): aislamiento riguroso de nodos, estructuras y cargas",
                    "Primera condición de equilibrio traslacional en sistemas de anclaje, cables y soportes",
                    "Fuerza de fricción estática y dinámica: coeficientes reales de rozamiento entre metales, concreto y suelo"
                ]
            },
            {
                "num": "Unidad 2",
                "titulo": "Momento de una Fuerza (Torque) y Segunda Condición de Equilibrio (Sumatoria M = 0)",
                "temas": [
                    "Concepto físico de torque (tau = F × d × sin theta): brazo de palanca y dirección del giro",
                    "Segunda condición de equilibrio rotacional aplicada a vigas de soporte y grúas de izaje",
                    "Centro de gravedad y estabilidad de maquinaria pesada, andamios y gabinetes industriales",
                    "Especificaciones de apriete: uso correcto del torquímetro en pernos estructurales y mecánicos"
                ]
            },
            {
                "num": "Unidad 3",
                "titulo": "Trabajo Mecánico, Potencia y Eficiencia Energética",
                "temas": [
                    "Definición técnica de trabajo (W = F · d): trabajo positivo, resistente y neto",
                    "Potencia mecánica: relación entre trabajo y tiempo en Watts, Kilowatts y Caballos de Fuerza (HP)",
                    "Energía cinética y potencial gravitatoria en traslados verticales y pendientes",
                    "Rendimiento mecánico (Eficiencia = P_salida / P_entrada): cuantificación de pérdidas por fricción"
                ]
            },
            {
                "num": "Unidad 4",
                "titulo": "Máquinas Simples y Ventaja Mecánica en Maniobras Técnicas",
                "temas": [
                    "Palancas de primer, segundo y tercer género: ventaja mecánica ideal vs. real",
                    "Sistemas de poleas fijas, móviles y polipastos industriales (aparejos) para izaje de cargas",
                    "Plano inclinado, cuña y tornillo de potencia: fuerzas requeridas para elevación de maquinaria",
                    "Cálculo de factores de seguridad mínimos (FS >= 3 a 5) en eslingas, cables de acero y grilletes"
                ]
            }
        ],
        "subtema_ia": "Herramientas de visión artificial en dispositivos móviles para medición digital de ángulos de eslingado, nivelación de maquinaria y cálculo óptico de distancias en campo.",
        "herramientas": "Dinamómetros, torquímetros calibrados, eslingas, apps de nivelación y medición óptica por visión artificial.",
        "aplicabilidad_7": "Cálculo de carga admisible en andamios (construcción), torque en culatas y pernos (automotriz/mecánica), izaje seguro de racks de telecomunicaciones y servidores (software/telecom), flecha y tensión en tendidos eléctricos.",
        "dictamen_link": "b1_fisica_basica_1.html"
    },

    # BIMESTRE 2
    "b2_etica_general_2": {
        "id": "b2_etica_general_2",
        "codigo": "B2-C1",
        "nombre": "Ética General 2",
        "subtitulo": "Libertad Responsable, Compliance e Integridad Industrial",
        "bimestre": "Bimestre 2",
        "bimestre_num": 2,
        "periodo": "Periodo 1 (50 min)",
        "linea_id": "linea-etica",
        "eje": "Formación Humana y Ética",
        "icono": "⚖️",
        "horas": "13.5 hrs (15 sesiones)",
        "prerequisitos": ["b1_etica_general_1"],
        "prerequisitos_texto": "Ética General 1 (B1-C1)",
        "habilita": ["b3_etica_profesional_1"],
        "habilita_texto": "Ética Profesional 1 (B3-C1)",
        "objetivo_transversal": "Interiorizar la responsabilidad civil, penal y moral de las firmas técnicas y forjar una cultura de integridad empresarial inquebrantable frente a presiones económicas.",
        "unidades": [
            {
                "num": "Unidad 1",
                "titulo": "Libertad Personal Responsable y Alcance Legal de las Firmas Técnicas",
                "temas": [
                    "La libertad personal vinculada a la responsabilidad: toda decisión técnica genera consecuencias",
                    "Implicaciones civiles y penales de firmar bitácoras de obra, memorias técnicas y órdenes de trabajo",
                    "Negligencia técnica, imprudencia e impericia: marco legal guatemalteco de responsabilidad profesional",
                    "El deber ineludible de negarse a autorizar trabajos que amenacen la vida o seguridad colectiva"
                ]
            },
            {
                "num": "Unidad 2",
                "titulo": "Veracidad en Bitácoras, Informes Técnicos y Ensayos de Calidad",
                "temas": [
                    "La verdad como principio no negociable: prohibición estricta de falsear lecturas o peritajes",
                    "Consecuencias catastróficas de alterar resultados de resistencia de concreto, frenos o aislamiento",
                    "Trazabilidad documental: el valor probatorio de bitácoras físicas foliadas y registros digitales inalterables",
                    "Honestidad técnica ante el error: reportar incidentes oportunamente en lugar de encubrirlos"
                ]
            },
            {
                "num": "Unidad 3",
                "titulo": "Compliance Industrial: Prevención de Sobornos y Conflicto de Intereses",
                "temas": [
                    "El flagelo de la corrupción en compras industriales y contrataciones públicas/privadas",
                    "Dádivas, comisiones ilícitas (kickbacks) de proveedores y conflicto de intereses en la selección de marcas",
                    "El costo oculto de repuestos falsificados o subestándar: paradas prematuras y accidentes fatales",
                    "El sello ético Kinal: reputación profesional intachable como el activo más valioso del egresado"
                ]
            },
            {
                "num": "Unidad 4",
                "titulo": "Seguridad Psicológica y Canales de Denuncia Ética (Whistleblowing)",
                "temas": [
                    "Construcción de un entorno de seguridad psicológica en el taller y cuadrilla",
                    "Protocolos para levantar la mano ante prácticas peligrosas o ilícitas sin temor a represalias",
                    "Canales éticos de denuncia interna en corporaciones guatemaltecas e internacionales",
                    "Dilemas éticos reales: lealtad mal entendida hacia compañeros frente a la lealtad con la verdad y la vida"
                ]
            }
        ],
        "subtema_ia": "Auditoría ética de sistemas de decisión algorítmica: prevención de sesgos discriminatorios en compras automatizadas y selección algorítmica de personal técnico.",
        "herramientas": "Matrices de conflicto de intereses, protocolos de compliance industrial, simulaciones de dilemas éticos de firma técnica.",
        "aplicabilidad_7": "Rechazo de compras de repuestos genéricos defectuosos en mecánica y electricidad, rechazo de concreto adulterado en construcción civil, rechazo de software sin licencias corporativas.",
        "dictamen_link": "b2_etica_general_2.html"
    },

    "b2_herramientas_contables": {
        "id": "b2_herramientas_contables",
        "codigo": "B2-C2",
        "nombre": "Herramientas Contables para la Supervisión",
        "subtitulo": "Costos Industriales (MPD-MOD-CIF), Downtime Cost y Presupuestos OPEX",
        "bimestre": "Bimestre 2",
        "bimestre_num": 2,
        "periodo": "Periodo 2 (50 min)",
        "linea_id": "linea-gestion",
        "eje": "Gestión y Supervisión",
        "icono": "💰",
        "horas": "13.5 hrs (15 sesiones)",
        "prerequisitos": ["b1_fundamentos_administracion", "b1_matematica_basica_1"],
        "prerequisitos_texto": "Fundamentos de la Administración (B1-C2) y Matemática Básica 1 (B1-C4)",
        "habilita": ["b4_fundamentos_marketing", "b4_matematica_aplicada_2"],
        "habilita_texto": "Fundamentos del Marketing / Power BI (B4-C3) y Matemática Aplicada 2 / Ing. Económica (B4-C4)",
        "objetivo_transversal": "Habilitar al supervisor para costear operaciones, justificar inversiones y administrar presupuestos de mantenimiento u obra en lenguaje financiero corporativo.",
        "unidades": [
            {
                "num": "Unidad 1",
                "titulo": "Estructura de Costos Industriales: MPD, MOD y CIF",
                "temas": [
                    "Clasificación de costos de producción: Materia Prima Directa (MPD) y Mano de Obra Directa (MOD)",
                    "Costos Indirectos de Fabricación (CIF): energía eléctrica, lubricantes, depreciación y supervisión",
                    "Costos fijos vs. costos variables en plantas de producción y empresas de servicios técnicos",
                    "Asignación de costos indirectos a órdenes de trabajo específicas mediante tasas de reparto"
                ]
            },
            {
                "num": "Unidad 2",
                "titulo": "Cuantificación del Costo de Parada No Planificada (Downtime Cost)",
                "temas": [
                    "Impacto financiero de una parada imprevista: mano de obra ociosa, mermas de materia prima y costos fijos",
                    "Cálculo del costo por minuto y hora de parada en líneas continuas (embotelladoras, molinos, prensas)",
                    "Justificación financiera del mantenimiento preventivo frente al mantenimiento reactivo de emergencia",
                    "Cálculo de penalizaciones contractuales por retrasos en entregas de proyectos de obra o software"
                ]
            },
            {
                "num": "Unidad 3",
                "titulo": "Costeo de Órdenes de Trabajo (OT) y Presupuestos Técnicos",
                "temas": [
                    "Formulación de presupuestos de reparación, mantenimiento y remodelación técnica",
                    "Determinación del factor de sobrecosto (Overhead) y margen de utilidad deseado",
                    "Elaboración de cotizaciones profesionales desglosadas para clientes internos o externos",
                    "Control de desvíos entre el costo presupuestado y el costo real ejecutado en campo"
                ]
            },
            {
                "num": "Unidad 4",
                "titulo": "Elaboración y Control de Presupuestos Operativos (OPEX)",
                "temas": [
                    "Diferencia estratégica entre presupuesto operativo (OPEX) y presupuesto de capital (CAPEX)",
                    "Estructuración del presupuesto anual de repuestos, consumibles y herramientas de área",
                    "Seguimiento mensual de ejecución presupuestaria mediante hojas de cálculo en Excel",
                    "Análisis de variaciones presupuestarias y formulación de planes de contención de gastos"
                ]
            }
        ],
        "subtema_ia": "Modelos de IA para escaneo inteligente de facturas y recibos (OCR avanzado), clasificación automática de gastos operativos y detección temprana de desvíos presupuestarios.",
        "herramientas": "Plantillas de costeo MPD-MOD-CIF en Excel, calculadoras de Downtime Cost, sistemas ERP básicos (módulo de compras y órdenes).",
        "aplicabilidad_7": "Presupuestos de remodelaciones en construcción, costos de reparación mayor en talleres mecánicos y automotrices, costos de infraestructura cloud en software, tendidos de fibra óptica en telecom.",
        "dictamen_link": "b2_herramientas_contables.html"
    },

    "b2_administracion_rrhh_sso": {
        "id": "b2_administracion_rrhh_sso",
        "codigo": "B2-C3",
        "nombre": "Administración de RRHH y SSO",
        "subtitulo": "Código de Trabajo de Guatemala, Planillas del IGSS y Acuerdo Gubernativo 229-2014",
        "bimestre": "Bimestre 2",
        "bimestre_num": 2,
        "periodo": "Periodo 3 (50 min)",
        "linea_id": "linea-gestion",
        "eje": "Gestión y Supervisión",
        "icono": "🦺",
        "horas": "13.5 hrs (15 sesiones)",
        "prerequisitos": ["b1_fundamentos_administracion"],
        "prerequisitos_texto": "Fundamentos de la Administración (B1-C2)",
        "habilita": ["b3_servicio_cliente", "b4_control_calidad"],
        "habilita_texto": "Servicio al Cliente (B3-C3) y Control de Calidad (B4-C2)",
        "objetivo_transversal": "Dominar la legislación laboral guatemalteca, el cálculo riguroso de planillas e IGSS, y liderar la seguridad ocupacional para lograr cero accidentes en planta u obra.",
        "unidades": [
            {
                "num": "Unidad 1",
                "titulo": "Código de Trabajo de Guatemala: Jornadas, Descansos y Salarios",
                "temas": [
                    "Marco legal de las jornadas laborales en Guatemala: diurna (8h/44h), mixta (7h/42h) y nocturna (6h/36h)",
                    "Cálculo y autorización legal de horas extraordinarias (tiempo y medio) y descansos semanales",
                    "Asuetos oficiales con goce de salario y normativas del Libro de Salarios ante el MINTRAB",
                    "Régimen disciplinario laboral: amonestaciones verbales, escritas y actas administrativas sin vicios de ley"
                ]
            },
            {
                "num": "Unidad 2",
                "titulo": "Cálculo de Planillas de Pago, Retenciones del IGSS y Prestaciones",
                "temas": [
                    "Estructura del salario base, bonificación incentivo de ley (Decreto 37-2001) y viáticos",
                    "Cálculo de la cuota laboral del IGSS (4.83%) y cuota patronal (10.67% IGSS + 1% IRTRA + 1% INTECAP = 12.67%)",
                    "Manejo de la plataforma electrónica IGSS Digital para declaración mensual de trabajadores",
                    "Cálculo de liquidaciones laborales y finiquitos: Aguinaldo, Bono 14, vacaciones no gozadas e indemnización"
                ]
            },
            {
                "num": "Unidad 3",
                "titulo": "Seguridad y Salud Ocupacional (SSO): Acuerdo Gubernativo 229-2014",
                "temas": [
                    "Reglamento de Salud y Seguridad Ocupacional: obligaciones patronales y del trabajador técnico",
                    "Conformación, funciones y registro de los Comités Bipartitos de SSO en empresas de más de 10 trabajadores",
                    "Monitores de SSO y elaboración del Plan de Salud y Seguridad Ocupacional avalado por médico colegiado",
                    "Sanciones del Ministerio de Trabajo y del IGSS por incumplimiento de medidas preventivas"
                ]
            },
            {
                "num": "Unidad 4",
                "titulo": "Matriz IPERC y Protocolos Críticos de Seguridad en Planta y Obra",
                "temas": [
                    "Metodología de Identificación de Peligros, Evaluación de Riesgos y Control (Matriz IPERC)",
                    "Jerarquía de controles: Eliminación, Sustitución, Controles de Ingeniería, Administrativos y EPP",
                    "Protocolos de Bloqueo y Etiquetado de Energía Cero (LOTO - Lockout/Tagout) en electricidad y máquinas",
                    "Permisos de trabajo de alto riesgo: trabajos en alturas (>1.80m), espacios confinados y trabajos en caliente"
                ]
            }
        ],
        "subtema_ia": "Automatización de procesos (RPA) y asistentes de IA para verificación cruzada de consistencia en el cálculo de planillas de pago, horas extras y retenciones laborales del IGSS.",
        "herramientas": "Plataforma IGSS Digital, matrices IPERC, formatos de permisos de trabajo de alto riesgo (LOTO, alturas), hojas de cálculo de planillas.",
        "aplicabilidad_7": "Universal: todo supervisor técnico en las 7 especialidades lidera personal de cuadrilla o taller, debiendo verificar horas extras, liquidaciones, descuentos del IGSS y velar por el cumplimiento de las normas de SSO.",
        "dictamen_link": "b2_administracion_rrhh_sso.html"
    },

    "b2_matematica_basica_2": {
        "id": "b2_matematica_basica_2",
        "codigo": "B2-C4",
        "nombre": "Matemática Básica 2",
        "subtitulo": "Punto de Equilibrio, Modelado de Funciones y Lógica Booleana",
        "bimestre": "Bimestre 2",
        "bimestre_num": 2,
        "periodo": "Periodo 4 (50 min)",
        "linea_id": "linea-matematica",
        "eje": "Ciencias Exactas Aplicadas",
        "icono": "📉",
        "horas": "13.5 hrs (15 sesiones)",
        "prerequisitos": ["b1_matematica_basica_1"],
        "prerequisitos_texto": "Matemática Básica 1 (B1-C4)",
        "habilita": ["b3_matematica_aplicada_1", "b4_matematica_aplicada_2", "b4_fisica_aplicada_3"],
        "habilita_texto": "Matemática Aplicada 1 / Estadística (B3-C4), Ing. Económica (B4-C4) y Física Aplicada 3 / Python (B4-C5)",
        "objetivo_transversal": "Modelar el punto de equilibrio operativo de servicios técnicos y dominar la lógica booleana y la algoritmia para estructurar procesos y hojas de cálculo avanzadas.",
        "unidades": [
            {
                "num": "Unidad 1",
                "titulo": "Funciones Lineales y Análisis de Punto de Equilibrio Operativo",
                "temas": [
                    "La ecuación de la recta (y = mx + b) aplicada a funciones de ingresos y costos totales",
                    "Cálculo del Punto de Equilibrio (Break-Even Point = Costos Fijos / Margen de Contribución)",
                    "Modelado en Excel del volumen mínimo de producción o servicios para no generar pérdidas",
                    "Análisis de sensibilidad: impacto del cambio en el precio de venta o costos variables unitarios"
                ]
            },
            {
                "num": "Unidad 2",
                "titulo": "Funciones No Lineales, Depreciación y Modelos de Tendencia",
                "temas": [
                    "Funciones polinomiales de segundo grado aplicadas a trayectorias y optimización de áreas",
                    "Funciones exponenciales y logarítmicas: degradación de aislamiento y curvas de enfriamiento",
                    "Modelos matemáticos de depreciación de activos fijos: línea recta (ley ISR Guatemala) y suma de dígitos",
                    "Interpolación lineal y ajuste de curvas características de sensores y bombas en Excel"
                ]
            },
            {
                "num": "Unidad 3",
                "titulo": "Lógica Matemática, Proposiciones y Operadores Booleanos",
                "temas": [
                    "Proposiciones lógicas simples y compuestas: negación, conjunción (AND), disyunción (OR)",
                    "Tablas de verdad y compuertas lógicas (AND, OR, NOT, XOR, NAND, NOR)",
                    "Leyes del Álgebra de Boole y simplificación de condiciones lógicas operacionales",
                    "Formulación de condiciones lógicas complejas anidadas en Excel (SI, Y, O, ESERROR, BUSCARX)"
                ]
            },
            {
                "num": "Unidad 4",
                "titulo": "Algoritmia Básica y Diagramación de Flujo Normalizada (ANSI/ISO)",
                "temas": [
                    "Concepto de algoritmo: precisión, finitud y estructura de pasos lógicos",
                    "Simbología estándar de diagramas de flujo según normas ANSI e ISO 5807",
                    "Estructuras de control: secuencial, condicional (if/else) y cíclica/iterativa (bucles de control)",
                    "Diagramación estructurada de procedimientos operativos y protocolos de diagnóstico de fallas"
                ]
            }
        ],
        "subtema_ia": "Asistentes de IA para traducción de reglas de negocio operativas complejas a diagramas de flujo estructurados y validación automática de tablas de verdad booleanas.",
        "herramientas": "Microsoft Excel avanzado (Solver, funciones lógicas), software de diagramación (Lucidchart / Draw.io / Visio).",
        "aplicabilidad_7": "Cálculo de rentabilidad en obra civil, lógica de programación en software, interbloqueos de seguridad en electricidad y electrónica, diagnóstico estructurado de fallas en talleres mecánicos y conmutación en telecomunicaciones.",
        "dictamen_link": "b2_matematica_basica_2.html"
    },

    "b2_fisica_aplicada_1": {
        "id": "b2_fisica_aplicada_1",
        "codigo": "B2-C5",
        "nombre": "Física Aplicada 1",
        "subtitulo": "Física de Materiales, Resistencia Mecánica y Propiedades Térmico-Dieléctricas",
        "bimestre": "Bimestre 2",
        "bimestre_num": 2,
        "periodo": "Periodo 5 (50 min)",
        "linea_id": "linea-fisica",
        "eje": "Física y Tecnología",
        "icono": "🧱",
        "horas": "13.5 hrs (15 sesiones)",
        "prerequisitos": ["b1_fisica_basica_1", "b1_matematica_basica_1"],
        "prerequisitos_texto": "Física Básica 1 (B1-C5) y Matemática Básica 1 (B1-C4)",
        "habilita": ["b3_fisica_aplicada_2", "b4_control_calidad"],
        "habilita_texto": "Física Aplicada 2 / Energía (B3-C5) y Control de Calidad / AMFE (B4-C2)",
        "objetivo_transversal": "Comprender el comportamiento mecánico, térmico y dieléctrico de los materiales técnicos bajo esfuerzos reales para garantizar factores de seguridad adecuados y prevención de fallas catastróficas.",
        "unidades": [
            {
                "num": "Unidad 1",
                "titulo": "Esfuerzos Mecánicos Fundamentales y Ley de Hooke",
                "temas": [
                    "Definición de esfuerzo (sigma = F / A) y deformación unitaria (epsilon = delta L / L0)",
                    "Tipos de esfuerzo: tensión pura, compresión axial, cortante directo, flexión y torsión en ejes",
                    "Diagrama esfuerzo-deformación: zona elástica, límite proporcional, fluencia y esfuerzo de rotura",
                    "Ley de Hooke (sigma = E · epsilon): Módulo de Elasticidad (Young) de aceros, aluminio, cobre y concreto"
                ]
            },
            {
                "num": "Unidad 2",
                "titulo": "Propiedades Mecánicas y Comportamiento Térmico de Materiales",
                "temas": [
                    "Ductilidad, fragilidad, resiliencia y tenacidad al impacto (pruebas Charpy)",
                    "Dureza de materiales: escalas Brinell, Rockwell y Vickers para selección de herramientas",
                    "Fatiga de materiales por cargas cíclicas vibratorias y curva S-N de vida útil",
                    "Dilatación térmica lineal, superficial y volumétrica: cálculo de juntas de expansión en tuberías y ductos"
                ]
            },
            {
                "num": "Unidad 3",
                "titulo": "Propiedades Eléctricas, Dieléctricas y Disipación Térmica",
                "temas": [
                    "Estructura atómica: materiales conductores (cobre, aluminio), aislantes (polímeros, cerámica) y semiconductores",
                    "Resistividad eléctrica (rho), conductividad y variación de la resistencia con la temperatura",
                    "Rigidez dieléctrica (kV/mm) de aislamientos y ruptura dieléctrica por sobretensión o humedad",
                    "Disipación térmica en componentes: resistencia térmica y dimensionamiento de disipadores de calor"
                ]
            },
            {
                "num": "Unidad 4",
                "titulo": "Criterios de Selección de Materiales y Prevención de Corrosión",
                "temas": [
                    "Criterios de selección técnica de materiales según condiciones ambientales y mecánicas de operación",
                    "Mecanismos de corrosión galvánica, química y atmosférica en estructuras y conexiones eléctricas",
                    "Métodos de protección anticorrosiva: galvanizado, recubrimientos epóxicos y ánodos de sacrificio",
                    "Ensayos no destructivos (NDT): tintas penetrantes, ultrasonido básico e inspección visual de fisuras"
                ]
            }
        ],
        "subtema_ia": "Modelos de IA y herramientas analíticas para búsqueda y comparación rápida de propiedades de materiales en bases de datos técnicas internacionales (CES EduPack / MatWeb).",
        "herramientas": "Tablas técnicas de resistencia de materiales, durómetros, ensayos no destructivos básicos, cámaras termográficas.",
        "aplicabilidad_7": "Resistencia de probetas de concreto y acero (construcción), disipadores térmicos para servidores y racks (software/hardware), esfuerzos en chasis y fatiga en frenos (automotriz), tensión en tendidos eléctricos y ductos.",
        "dictamen_link": "b2_fisica_aplicada_1.html"
    },

    # BIMESTRE 3
    "b3_etica_profesional_1": {
        "id": "b3_etica_profesional_1",
        "codigo": "B3-C1",
        "nombre": "Ética Profesional 1",
        "subtitulo": "Automatización, Inteligencia Artificial y la Transición Justa",
        "bimestre": "Bimestre 3",
        "bimestre_num": 3,
        "periodo": "Periodo 1 (50 min)",
        "linea_id": "linea-etica",
        "eje": "Formación Humana y Ética",
        "icono": "🤖",
        "horas": "13.5 hrs (15 sesiones)",
        "prerequisitos": ["b2_etica_general_2"],
        "prerequisitos_texto": "Ética General 2 (B2-C1)",
        "habilita": ["b4_etica_profesional_2"],
        "habilita_texto": "Ética Profesional 2 (B4-C1)",
        "objetivo_transversal": "Liderar con sensibilidad ética la transformación digital y automatización de procesos, promoviendo el reentrenamiento del personal antes que el despido masivo.",
        "unidades": [
            {
                "num": "Unidad 1",
                "titulo": "Automatización y el Futuro del Empleo en Guatemala: La Transición Justa",
                "temas": [
                    "El impacto de la robótica, la IA y los sistemas automatizados en el mercado laboral guatemalteco",
                    "El imperativo ético de la transición justa: humanizar la tecnología en vez de considerarla pretexto para recortes",
                    "La persona como principio y fin de la actividad económica: la primacía del trabajo sobre el capital",
                    "Evaluación del impacto social previo a la implementación de proyectos de automatización"
                ]
            },
            {
                "num": "Unidad 2",
                "titulo": "Reskilling y Upskilling: El Deber Formativo del Supervisor Técnico",
                "temas": [
                    "El rol del supervisor como educador: diseñar rutas de aprendizaje para elevar el nivel del operario",
                    "Estrategias de reentrenamiento técnico (Reskilling) frente a tareas obsoletas de bajo valor",
                    "Especialización y aumento de capacidades (Upskilling) en herramientas digitales y diagnóstico",
                    "La formación continua como deber de justicia social y reciprocidad con el trabajador leal"
                ]
            },
            {
                "num": "Unidad 3",
                "titulo": "Ética en la Inteligencia Artificial Industrial y Vigilancia Digital",
                "temas": [
                    "Sesgos algorítmicos en sistemas automatizados de asignación de turnos y evaluación del rendimiento",
                    "Límites éticos y legales del monitoreo biométrico, cámaras inteligentes y software de rastreo",
                    "Derecho a la desconexión laboral y preservación de la intimidad del trabajador en planta y home office",
                    "Transparencia en la toma de decisiones asistidas por IA: el trabajador tiene derecho a saber cómo se le evalúa"
                ]
            },
            {
                "num": "Unidad 4",
                "titulo": "Confidencialidad, Propiedad Intelectual y Secretos Industriales con IA",
                "temas": [
                    "Riesgos de fuga de información confidencial al ingresar datos corporativos en herramientas de IA pública",
                    "Protección de fórmulas, planos, códigos fuente y recetas de producción de la empresa",
                    "Propiedad intelectual de soluciones técnicas desarrolladas con asistencia de algoritmos",
                    "Políticas corporativas de uso seguro y responsable de IA generativa en el entorno de trabajo"
                ]
            }
        ],
        "subtema_ia": "Uso responsable de herramientas de IA generativa en la empresa: directrices de confidencialidad de datos (Data Privacy), propiedad intelectual y prevención de fugas de secretos industriales.",
        "herramientas": "Casos de estudio de transición tecnológica en plantas industriales, guías de gobernanza de datos y privacidad en IA.",
        "aplicabilidad_7": "Esencial para el supervisor que introduce brazos robóticos en una línea de ensamble, automatiza pruebas de software, digitaliza talleres mecánicos o moderniza radiobases de telecomunicaciones.",
        "dictamen_link": "b3_etica_profesional_1.html"
    },

    "b3_metodos_produccion": {
        "id": "b3_metodos_produccion",
        "codigo": "B3-C2",
        "nombre": "Métodos de Producción",
        "subtitulo": "Lean Manufacturing, Estandarización 5S y Mapeo de Flujo de Valor (VSM)",
        "bimestre": "Bimestre 3",
        "bimestre_num": 3,
        "periodo": "Periodo 2 (50 min)",
        "linea_id": "linea-gestion",
        "eje": "Gestión y Supervisión",
        "icono": "🏭",
        "horas": "13.5 hrs (15 sesiones)",
        "prerequisitos": ["b1_planeacion_control_trabajo", "b1_fundamentos_administracion"],
        "prerequisitos_texto": "Planeación y Control para el Trabajo (B1-C3) y Fundamentos de la Administración (B1-C2)",
        "habilita": ["b4_control_calidad"],
        "habilita_texto": "Control de Calidad / Six Sigma (B4-C2)",
        "objetivo_transversal": "Aplicar la filosofía Lean y las 5S de Kinal para erradicar desperdicios, balancear líneas operativas y maximizar la productividad del área a cargo.",
        "unidades": [
            {
                "num": "Unidad 1",
                "titulo": "Filosofía Lean Manufacturing y Erradicación de los 8 Desperdicios (Mudas)",
                "temas": [
                    "Orígenes del Sistema de Producción Toyota (TPS) y su adaptación a la industria guatemalteca",
                    "Identificación en campo de los 8 desperdicios: Sobreproducción, Esperas, Transporte innecesario, Sobreprocesamiento, Exceso de inventario, Movimientos improductivos, Defectos y Talento humano no aprovechado",
                    "Paseos Gemba (Gemba Walk): ir al lugar real de los hechos para observar los procesos",
                    "Cultura Kaizen: mejora continua basada en pequeñas acciones cotidianas del personal de piso"
                ]
            },
            {
                "num": "Unidad 2",
                "titulo": "Implementación de 5S en Taller y Oficina como Hábito Kinal",
                "temas": [
                    "Las 5 fases de las 5S: Seiri (Clasificar), Seiton (Ordenar), Seiso (Limpiar), Seiketsu (Estandarizar), Shitsuke (Disciplina)",
                    "Campaña de tarjetas rojas para desecho de materiales obsoletos o dañados",
                    "Gestión visual del orden: demarcación de pisos, sombras de herramientas y paneles de control",
                    "Auditorías periódicas de 5S con listas de verificación e indicadores visuales de cumplimiento"
                ]
            },
            {
                "num": "Unidad 3",
                "titulo": "Mapeo de Flujo de Valor (VSM - Value Stream Mapping)",
                "temas": [
                    "Diferenciación entre actividades que agregan valor (VA), no agregan valor pero son necesarias (NNVA) y puro desperdicio (NVA)",
                    "Construcción del mapa del estado actual (Current State VSM): flujo de materiales e información",
                    "Identificación del tiempo de entrega total (Lead Time) vs. tiempo de procesamiento real",
                    "Diseño del mapa del estado futuro (Future State VSM) orientado al flujo continuo"
                ]
            },
            {
                "num": "Unidad 4",
                "titulo": "Estandarización del Trabajo, Takt Time y Técnica SMED",
                "temas": [
                    "Cálculo del Takt Time (Tiempo disponible / Demanda del cliente) para sincronizar la operación",
                    "Balanceo de líneas de ensamble y células de trabajo para eliminar tiempos muertos",
                    "Hojas de Trabajo Estandarizado (SWIS): definición del método seguro, ordenado y repetible",
                    "Técnica SMED (Single-Minute Exchange of Die) para reducción drástica de tiempos de cambio de herramientas y formato"
                ]
            }
        ],
        "subtema_ia": "Optimización de rutas de producción y balanceo de líneas mediante algoritmos genéticos y modelos de investigación de operaciones con Inteligencia Artificial.",
        "herramientas": "Plantillas VSM, cronómetros de Takt Time, formatos de auditoría 5S, matrices SMED, hojas de trabajo estandarizado.",
        "aplicabilidad_7": "Optimización del patio de materiales en construcción, reducción de tiempos en bahías de taller automotriz, flujo de tickets de soporte en telecomunicaciones y sprints de desarrollo ágil en software.",
        "dictamen_link": "b3_metodos_produccion.html"
    },

    "b3_servicio_cliente": {
        "id": "b3_servicio_cliente",
        "codigo": "B3-C3",
        "nombre": "Servicio al Cliente",
        "subtitulo": "Gestión de Clientes B2B, Acuerdos SLA y Calidad en Servicios Técnicos",
        "bimestre": "Bimestre 3",
        "bimestre_num": 3,
        "periodo": "Periodo 3 (50 min)",
        "linea_id": "linea-gestion",
        "eje": "Gestión y Supervisión",
        "icono": "🤝",
        "horas": "13.5 hrs (15 sesiones)",
        "prerequisitos": ["b1_fundamentos_administracion", "b2_administracion_rrhh_sso"],
        "prerequisitos_texto": "Fundamentos de la Administración (B1-C2) y Administración de RRHH (B2-C3)",
        "habilita": ["b4_fundamentos_marketing"],
        "habilita_texto": "Fundamentos del Marketing B2B (B4-C3)",
        "objetivo_transversal": "Desarrollar una mentalidad de servicio profesional tanto hacia el cliente interno (producción/ingeniería) como hacia clientes externos corporativos en entornos industriales B2B.",
        "unidades": [
            {
                "num": "Unidad 1",
                "titulo": "El Concepto de Cliente Interno en Organizaciones Técnicas",
                "temas": [
                    "Sinergia entre departamentos de soporte (mantenimiento, TI, infraestructura) y operaciones",
                    "Cadena interna de valor: el siguiente puesto de trabajo es tu cliente prioritario",
                    "Eliminación de la cultura de silos organizacionales y culpas interdepartamentales",
                    "Establecimiento de acuerdos de cooperación y metas conjuntas de productividad"
                ]
            },
            {
                "num": "Unidad 2",
                "titulo": "Acuerdos de Nivel de Servicio (SLA - Service Level Agreements)",
                "temas": [
                    "Definición y estructura técnica de un Acuerdo de Nivel de Servicio (SLA)",
                    "Métricas clave de servicio: Tiempo de Respuesta, Tiempo Medio de Reparación (MTTR) y Disponibilidad (Uptime)",
                    "Establecimiento de compromisos de disponibilidad (99%, 99.9%) y penalizaciones por incumplimiento",
                    "Monitoreo de SLAs mediante plataformas digitales de mesa de ayuda y ticketing"
                ]
            },
            {
                "num": "Unidad 3",
                "titulo": "Servicio Técnico Industrial B2B, Garantías y Manejo de Reclamos",
                "temas": [
                    "Particularidades de la relación comercial B2B: compras técnicas basadas en confianza y soporte continuo",
                    "Procedimientos de gestión de garantías de repuestos, maquinaria e instalaciones",
                    "Protocolos de atención a reclamos críticos de clientes corporativos sin perder la compostura",
                    "Análisis de causas de inconformidad técnica y planes de acción correctiva inmediata"
                ]
            },
            {
                "num": "Unidad 4",
                "titulo": "El Espíritu de Servicio Cristiano como Diferenciador Profesional Kinal",
                "temas": [
                    "El servicio no como servilismo, sino como vocación de grandeza y generosidad profesional",
                    "Cortesía en el lenguaje técnico, puntualidad rigurosa en entregas y limpieza en el área de trabajo intervenida",
                    "Superación de expectativas del cliente: la milla extra técnica en cada servicio prestado",
                    "Fidelización y retención de clientes corporativos mediante la excelencia en el soporte postventa"
                ]
            }
        ],
        "subtema_ia": "Agentes conversacionales inteligentes de soporte técnico de primer nivel y análisis automático de sentimiento en tickets y reportes de servicio postventa.",
        "herramientas": "Formatos de SLAs técnicos, plataformas de ticketing (Jira Service Desk / Zendesk), protocolos de atención de quejas B2B.",
        "aplicabilidad_7": "Soporte postventa de maquinaria industrial, acuerdos de uptime en redes de telecomunicaciones, garantías de obra civil entregada o contratos de soporte de software (SLA 99.9%).",
        "dictamen_link": "b3_servicio_cliente.html"
    },

    "b3_matematica_aplicada_1": {
        "id": "b3_matematica_aplicada_1",
        "codigo": "B3-C4",
        "nombre": "Matemática Aplicada 1",
        "subtitulo": "Estadística Práctica Aplicada, Principio de Pareto y Análisis de Variabilidad",
        "bimestre": "Bimestre 3",
        "bimestre_num": 3,
        "periodo": "Periodo 4 (50 min)",
        "linea_id": "linea-matematica",
        "eje": "Ciencias Exactas Aplicadas",
        "icono": "📊",
        "horas": "13.5 hrs (15 sesiones)",
        "prerequisitos": ["b2_matematica_basica_2", "b1_matematica_basica_1"],
        "prerequisitos_texto": "Matemática Básica 2 (B2-C4) y Matemática Básica 1 (B1-C4)",
        "habilita": ["b4_control_calidad", "b4_fundamentos_marketing", "b4_matematica_aplicada_2"],
        "habilita_texto": "Control de Calidad / Six Sigma (B4-C2), Fundamentos del Marketing / Power BI (B4-C3) y Matemática Aplicada 2 / Ing. Económica (B4-C4)",
        "objetivo_transversal": "Utilizar la analítica descriptiva en hojas de cálculo y la ley de Pareto para identificar la dispersión de mediciones y priorizar las causas de fallas y mermas operativas.",
        "unidades": [
            {
                "num": "Unidad 1",
                "titulo": "Estadística Descriptiva Práctica en Hojas de Cálculo",
                "temas": [
                    "Población y muestra: muestreo representativo aleatorio y estratificado en planta",
                    "Medidas de tendencia central: media aritmética, mediana y moda en datos de tiempos y tolerancias",
                    "Medidas de dispersión: varianza, desviación estándar poblacional y muestral, y rango",
                    "Cálculo e interpretación de percentiles y cuartiles para auditoría de límites de servicio"
                ]
            },
            {
                "num": "Unidad 2",
                "titulo": "Organización y Visualización Gráfica de Datos Técnicos",
                "temas": [
                    "Construcción de tablas de distribución de frecuencias e intervalos de clase en Excel",
                    "Histogramas de frecuencias: interpretación de la forma de la distribución (sesgos y dispersión)",
                    "Diagramas de caja y bigotes (Boxplots) para detección visual de datos atípicos (outliers)",
                    "Uso del complemento Herramientas para Análisis de Datos (Analysis ToolPak) en Excel"
                ]
            },
            {
                "num": "Unidad 3",
                "titulo": "Principio de Pareto (Regla 80/20) y Estratificación Operativa",
                "temas": [
                    "Fundamentación del principio de Pareto: el 20% de las causas genera el 80% de los problemas o costos",
                    "Elaboración paso a paso de diagramas de Pareto (frecuencias absolutas y porcentajes acumulados)",
                    "Estratificación de datos por cuadrilla, turno, máquina, proveedor y tipo de defecto",
                    "Priorización objetiva de proyectos de mejora para enfocar recursos escasos en los problemas vitales"
                ]
            },
            {
                "num": "Unidad 4",
                "titulo": "Tendencias Operacionales, Correlación Lineal Simple y Proyecciones",
                "temas": [
                    "Diagramas de dispersión para analizar la relación entre dos variables operativas (ej. temperatura vs. desgaste)",
                    "Cálculo e interpretación del Coeficiente de Correlación de Pearson (r)",
                    "Ecuación de la recta de regresión lineal (mínimos cuadrados) y Coeficiente de Determinación (R²)",
                    "Uso cauteloso de proyecciones lineales simples para estimación de consumos y desgaste de componentes"
                ]
            }
        ],
        "subtema_ia": "Herramientas de IA para análisis exploratorio de datos (Code Interpreter / Data Analysis) para procesar tablas de datos CSV masivos y generar resúmenes estadísticos automáticos en segundos.",
        "herramientas": "Microsoft Excel (Analysis ToolPak, tablas dinámicas), diagramas de Pareto e histogramas automáticos.",
        "aplicabilidad_7": "Dispersión de resistencia en probetas de concreto (construcción), métricas de latencia y tiempos de respuesta (software), historial de variaciones de voltaje (electricidad), control de tolerancias (electrónica), tiempos de bahía en taller (automotriz), frecuencia de fallas de máquinas (mecánica), disponibilidad de enlaces (telecom).",
        "dictamen_link": "b3_matematica_aplicada_1.html"
    },

    "b3_fisica_aplicada_2": {
        "id": "b3_fisica_aplicada_2",
        "codigo": "B3-C5",
        "nombre": "Física Aplicada 2",
        "subtitulo": "Energía, Eficiencia Energética, Tarifas Industriales y Sostenibilidad",
        "bimestre": "Bimestre 3",
        "bimestre_num": 3,
        "periodo": "Periodo 5 (50 min)",
        "linea_id": "linea-fisica",
        "eje": "Física y Tecnología",
        "icono": "⚡",
        "horas": "13.5 hrs (15 sesiones)",
        "prerequisitos": ["b2_fisica_aplicada_1", "b1_matematica_basica_1"],
        "prerequisitos_texto": "Física Aplicada 1 (B2-C5) y Matemática Básica 1 (B1-C4)",
        "habilita": ["b4_matematica_aplicada_2", "b4_fisica_aplicada_3"],
        "habilita_texto": "Matemática Aplicada 2 / Ing. Económica (B4-C4) y Física Aplicada 3 / Sensores y Python (B4-C5)",
        "objetivo_transversal": "Comprender los balances energéticos, la estructura de costos de la energía eléctrica industrial en Guatemala y las tecnologías de climatización y energía solar para reducir costos y huella ambiental.",
        "unidades": [
            {
                "num": "Unidad 1",
                "titulo": "Principios de Energía y Balances Operativos de Entrada y Salida",
                "temas": [
                    "Formas de energía presentes en la industria: mecánica, térmica, eléctrica y química",
                    "Principio de conservación de la energía: E_entrada = E_útil + Pérdidas disipadas",
                    "Unidades técnicas y factores de equivalencia: Joules, Kilovatios-hora (kWh), BTU y Calorías",
                    "Diagramas de Sankey para visualización de flujos de energía y pérdidas en plantas de producción"
                ]
            },
            {
                "num": "Unidad 2",
                "titulo": "Potencia Eléctrica, Consumo en kWh y Tarifas Industriales de Guatemala",
                "temas": [
                    "Potencia activa (kW), potencia reactiva (kVAR) y potencia aparente (kVA): el triángulo de potencia",
                    "Factor de potencia (cos phi): penalizaciones de las distribuidoras por bajo factor de potencia (<0.90)",
                    "Estructura tarifaria de EEGSA y ENERGUATE: tarifas de baja y media tensión con cargos por potencia máxima y consumo",
                    "Auditoría básica de facturas eléctricas industriales y detección de cargos por demanda punta"
                ]
            },
            {
                "num": "Unidad 3",
                "titulo": "Transferencia de Calor y Climatización Básica de Espacios Técnicos (HVAC)",
                "temas": [
                    "Mecanismos de transferencia de calor: conducción (ley de Fourier), convección (ley de Newton) y radiación térmica",
                    "Aislamiento térmico de tuberías, ductos y techos industriales para reducción de pérdidas",
                    "Ciclo de refrigeración mecánica por compresión de vapor: compresor, condensador, válvula y evaporador",
                    "Cálculo de cargas térmicas básicas para climatización de salas de servidores, laboratorios y áreas de producción"
                ]
            },
            {
                "num": "Unidad 4",
                "titulo": "Eficiencia Energética, Sistemas Solares Fotovoltaicos y Descarbonización",
                "temas": [
                    "Medidas de ahorro energético sin inversión (No-cost) y con baja inversión en motores e iluminación LED",
                    "Fundamentos de energía solar fotovoltaica: radiación solar, paneles monocristalinos/policristalinos e inversores",
                    "Sistemas solares interconectados a red (Grid-tie) con medición neta y sistemas aislados con almacenamiento en baterías",
                    "Cálculo de reducción de emisiones de CO2 y huella de carbono como ventaja competitiva exportadora"
                ]
            }
        ],
        "subtema_ia": "Algoritmos de IA para análisis de curvas de carga eléctrica en tiempo real y detección automática de consumos parásitos o desvíos energéticos en equipos de planta.",
        "herramientas": "Analizadores de redes eléctricas, pliegos tarifarios oficiales CNEE / EEGSA, software de dimensionamiento solar fotovoltaico básico.",
        "aplicabilidad_7": "Aislamiento térmico en edificaciones (construcción), climatización y refrigeración de centros de datos (software), auditorías eléctricas y tarifas en plantas (electricidad), disipación de calor en tableros (electrónica), aire acondicionado vehicular (automotriz), optimización de compresores (mecánica), radiobases con respaldo solar (telecom).",
        "dictamen_link": "b3_fisica_aplicada_2.html"
    },

    # BIMESTRE 4
    "b4_etica_profesional_2": {
        "id": "b4_etica_profesional_2",
        "codigo": "B4-C1",
        "nombre": "Ética Profesional 2",
        "subtitulo": "Principio Human-in-the-Loop (HITL), Juicio Crítico y el Trabajo Bien Hecho",
        "bimestre": "Bimestre 4",
        "bimestre_num": 4,
        "periodo": "Periodo 1 (50 min)",
        "linea_id": "linea-etica",
        "eje": "Formación Humana y Ética",
        "icono": "🧠",
        "horas": "13.5 hrs (15 sesiones)",
        "prerequisitos": ["b3_etica_profesional_1"],
        "prerequisitos_texto": "Ética Profesional 1 (B3-C1)",
        "habilita": [],
        "habilita_texto": "Graduación y Titulación TSU (UNIS / Kinal) y supervisión ética integral de la práctica profesional",
        "objetivo_transversal": "Consagrar el principio de que la responsabilidad moral y legal de la supervisión técnica es indelegable a las máquinas, coronando la formación con el ideal del trabajo bien hecho de Kinal.",
        "unidades": [
            {
                "num": "Unidad 1",
                "titulo": "El Principio Human-in-the-Loop (HITL) en Operaciones Industriales",
                "temas": [
                    "Definición técnica y jurídica de Human-in-the-Loop: supervisión humana obligatoria en sistemas autónomos e IA",
                    "Por qué la responsabilidad legal y ética no se delega en algoritmos, software predictivo ni robots",
                    "Protocolos de autorización humana en decisiones críticas: paradas de emergencia, seguridad de vidas y sanciones",
                    "Límites de la autonomía de los sistemas: diseño a prueba de fallos con mando manual prioritario"
                ]
            },
            {
                "num": "Unidad 2",
                "titulo": "Superación del Sesgo de Automatización y Juicio Crítico Profesional",
                "temas": [
                    "Sesgo de automatización (Automation Bias): la tendencia errónea a confiar ciegamente en datos digitales",
                    "El deber de contrastar las sugerencias de la IA con la física real, las inspecciones visuales y el sentido común",
                    "Desarrollo del pensamiento crítico técnico: dudar metódicamente de lecturas anómalas de sensores y diagnósticos automáticos",
                    "La experiencia y el juicio prudencial del supervisor humano como salvaguarda ante alucinaciones algorítmicas"
                ]
            },
            {
                "num": "Unidad 3",
                "titulo": "El Trabajo Bien Hecho Kinal: Honestidad Académica y Profesional",
                "temas": [
                    "El rechazo frontal al facilismo del 'copia y pega' de respuestas de IA en memorias de cálculo y peritajes",
                    "Rigor técnico, pulcritud en los detalles y comprobación exhaustiva antes de firmar cualquier entregable",
                    "La propiedad moral del esfuerzo: el orgullo del técnico por la obra que lleva su impronta de calidad",
                    "El ideario de Kinal como brújula de vida: transformar el entorno mediante la excelencia profesional silenciosa"
                ]
            },
            {
                "num": "Unidad 4",
                "titulo": "Responsabilidad Ambiental, Economía Circular y Manejo de Residuos",
                "temas": [
                    "El impacto ambiental de las operaciones técnicas: custodia de la creación para las futuras generaciones",
                    "Gestión ética y disposición certificada de residuos peligrosos (aceites usados, refrigerantes, solventes)",
                    "Manejo de residuos de aparatos eléctricos y electrónicos (RAEE / e-waste) y baterías de litio",
                    "Transición del modelo lineal (extraer-fabricar-tirar) al modelo de economía circular en la industria"
                ]
            }
        ],
        "subtema_ia": "Gobernanza de sistemas autónomos: protocolos institucionales para garantizar que en decisiones críticas que afecten vidas humanas, seguridad industrial o empleo siempre decida una persona responsable.",
        "herramientas": "Protocolos de gobernanza HITL, normativas MARN de disposición de residuos peligrosos, guías de integridad técnica.",
        "aplicabilidad_7": "Universal: ninguna IA debe autorizar una excavación riesgosa en construcción, liberar código bancario a producción en software, energizar una subestación eléctrica o diagnosticar el sistema de frenos de un autobús.",
        "dictamen_link": "b4_etica_profesional_2.html"
    },

    "b4_control_calidad": {
        "id": "b4_control_calidad",
        "codigo": "B4-C2",
        "nombre": "Control de Calidad",
        "subtitulo": "Sistemas de Gestión ISO 9001:2015, Metodología Six Sigma (DMAIC) y AMFE",
        "bimestre": "Bimestre 4",
        "bimestre_num": 4,
        "periodo": "Periodo 2 (50 min)",
        "linea_id": "linea-gestion",
        "eje": "Gestión y Supervisión",
        "icono": "🎯",
        "horas": "13.5 hrs (15 sesiones)",
        "prerequisitos": ["b3_metodos_produccion", "b3_matematica_aplicada_1"],
        "prerequisitos_texto": "Métodos de Producción (B3-C2) y Matemática Aplicada 1 / Estadística (B3-C4)",
        "habilita": [],
        "habilita_texto": "Graduación TSU y certificación de calidad de procesos industriales",
        "objetivo_transversal": "Implementar sistemas de gestión de calidad orientados a la prevención en la fuente y dominar la resolución estructurada de problemas mediante el ciclo DMAIC.",
        "unidades": [
            {
                "num": "Unidad 1",
                "titulo": "Sistemas de Gestión de Calidad bajo Norma ISO 9001:2015",
                "temas": [
                    "Evolución del concepto: de la inspección final reactiva al aseguramiento de calidad en los procesos",
                    "Estructura de alto nivel de la norma ISO 9001:2015 y enfoque basado en riesgos",
                    "Gestión documental de la calidad: procedimientos, instrucciones de trabajo, registros y auditorías internas",
                    "El ciclo PHVA (Planificar, Hacer, Verificar, Actuar) como motor de la mejora continua"
                ]
            },
            {
                "num": "Unidad 2",
                "titulo": "Las 7 Herramientas Clásicas de la Calidad para Análisis de Causa Raíz",
                "temas": [
                    "Diagrama Causa-Efecto (Espina de Pescado / Ishikawa) y el método de las 6M (Mano de obra, Maquinaria, etc.)",
                    "La técnica de los 5 Porqués (5 Whys) para profundizar más allá de los síntomas aparentes",
                    "Hojas de verificación estructuradas (Checksheets) y estratificación de defectos en planta",
                    "Cartas de Control Estadístico de Procesos (SPC) básicas para variables y atributos"
                ]
            },
            {
                "num": "Unidad 3",
                "titulo": "Aseguramiento de Calidad en la Fuente y Dispositivos Poka-Yoke",
                "temas": [
                    "El principio de calidad en la fuente: no aceptar, no fabricar y no enviar productos defectuosos",
                    "Diseño e implementación de mecanismos a prueba de errores (Poka-Yoke) mecánicos, eléctricos y lógicos",
                    "Parada de línea con señalización visual (Andon) ante anomalías en el proceso",
                    "Auditorías de puesto de trabajo escalonadas (Layered Process Audits - LPA)"
                ]
            },
            {
                "num": "Unidad 4",
                "titulo": "Metodología Six Sigma: Ciclo DMAIC y Matrices AMFE",
                "temas": [
                    "Fundamentos de Seis Sigma: reducción de la variabilidad del proceso (3.4 defectos por millón de oportunidades)",
                    "El ciclo DMAIC: Definir el problema, Medir el estado actual, Analizar causas, Mejorar el proceso, Controlar resultados",
                    "Análisis Modal de Fallos y Efectos (AMFE / FMEA): cálculo del Número de Prioridad de Riesgo (NPR = S × O × D)",
                    "Formulación de acciones preventivas para mitigar fallos potenciales de alto riesgo"
                ]
            }
        ],
        "subtema_ia": "Visión artificial con redes neuronales convolucionales (CNN) para inspección automática de defectos superficiales y control dimensional de piezas a alta velocidad en líneas de producción.",
        "herramientas": "Matrices AMFE, diagramas de Ishikawa, cartas de control estadístico (SPC), formatos de auditoría ISO 9001, modelos de visión artificial en línea.",
        "aplicabilidad_7": "Control de fisuras en soldaduras o concreto, inspección de piezas mecanizadas, revisión estática de código (linters con IA en software), calidad de crimpado de cables o empaque en telecomunicaciones.",
        "dictamen_link": "b4_control_calidad.html"
    },

    "b4_fundamentos_marketing": {
        "id": "b4_fundamentos_marketing",
        "codigo": "B4-C3",
        "nombre": "Fundamentos del Marketing",
        "subtitulo": "Business Intelligence (Power BI), Marketing Industrial B2B y Dashboards",
        "bimestre": "Bimestre 4",
        "bimestre_num": 4,
        "periodo": "Periodo 3 (50 min)",
        "linea_id": "linea-gestion",
        "eje": "Gestión y Supervisión",
        "icono": "📈",
        "horas": "13.5 hrs (15 sesiones)",
        "prerequisitos": ["b2_herramientas_contables", "b3_servicio_cliente", "b3_matematica_aplicada_1"],
        "prerequisitos_texto": "Herramientas Contables (B2-C2), Servicio al Cliente (B3-C3) y Matemática Aplicada 1 / Estadística (B3-C4)",
        "habilita": [],
        "habilita_texto": "Presentación ejecutiva ante juntas directivas y sustentación de proyectos de graduación",
        "objetivo_transversal": "Transformar la materia de marketing en inteligencia de negocios B2B y diseño de cuadros de mando (Dashboards en Power BI) para comunicar resultados de planta a la alta gerencia.",
        "unidades": [
            {
                "num": "Unidad 1",
                "titulo": "Marketing Industrial B2B y Propuesta de Valor Técnica",
                "temas": [
                    "Diferencias fundamentales entre marketing de consumo masivo (B2C) y marketing técnico industrial (B2B)",
                    "El proceso de compra en comités corporativos: gerencia general, financiera, mantenimiento y compras",
                    "Construcción de la Propuesta de Valor Técnica: ahorro energético, reducción de paradas y retorno de inversión",
                    "Diseño de licitaciones y cotizaciones técnicas estructuradas que comunican valor y no solo precio"
                ]
            },
            {
                "num": "Unidad 2",
                "titulo": "Business Intelligence (BI): Conexión, Limpieza y Modelado de Datos",
                "temas": [
                    "Introducción al Business Intelligence: transformar datos crudos de operaciones en decisiones estratégicas",
                    "Conexión a orígenes de datos técnicos en Microsoft Power BI (archivos Excel, CSV, bases de datos SQL)",
                    "Extracción, Transformación y Carga (ETL) mediante Power Query: limpieza de columnas, filtros y uniones",
                    "Modelado de datos relacional: tablas de hechos (órdenes, fallas) y tablas de dimensiones (fechas, máquinas, turnos)"
                ]
            },
            {
                "num": "Unidad 3",
                "titulo": "Creación de Cuadros de Mando (Dashboards en Power BI)",
                "temas": [
                    "Definición y selección de Indicadores Clave de Desempeño (KPIs): MTBF, MTTR, OEE, costos y mermas",
                    "Diseño de tarjetas de KPIs con objetivos y semáforos de cumplimiento",
                    "Uso de fórmulas DAX básicas (SUM, AVERAGE, CALCULATE, DIVIDE)",
                    "Visualizaciones interactivas: gráficos de barras comparativos, líneas de tendencia, mapas y matrices de datos"
                ]
            },
            {
                "num": "Unidad 4",
                "titulo": "Storytelling con Datos y Presentación Ejecutiva a Comités",
                "temas": [
                    "Principios de diseño visual y usabilidad en paneles de control (Dashboards): evitar la sobrecarga cognitiva",
                    "Storytelling con datos técnicos: estructurar la narrativa para la gerencia (Problema, Datos, Solución, Retorno)",
                    "Técnicas de oratoria y exposición ejecutiva ante comités de dirección y juntas de inversionistas",
                    "Defensa técnica y económica de solicitudes presupuestarias frente al director financiero"
                ]
            }
        ],
        "subtema_ia": "Analítica predictiva de demanda y herramientas de procesamiento de lenguaje natural (NLP) para generar resúmenes ejecutivos automáticos de reportes de planta para gerencia.",
        "herramientas": "Microsoft Power BI Desktop, Power Query, DAX básico, plantillas de dashboards industriales.",
        "aplicabilidad_7": "Presentación de avance físico-financiero de obra civil en construcción, métricas de fallas de flotas en mecánica automotriz, indicadores MTBF/MTTR de maquinaria industrial, disponibilidad de software en la nube (uptime) y tráfico en telecomunicaciones.",
        "dictamen_link": "b4_fundamentos_marketing.html"
    },

    "b4_matematica_aplicada_2": {
        "id": "b4_matematica_aplicada_2",
        "codigo": "B4-C4",
        "nombre": "Matemática Aplicada 2",
        "subtitulo": "Ingeniería Económica, Interés Compuesto y Evaluación de Inversiones (VPN/TIR)",
        "bimestre": "Bimestre 4",
        "bimestre_num": 4,
        "periodo": "Periodo 4 (50 min)",
        "linea_id": "linea-matematica",
        "eje": "Ciencias Exactas Aplicadas",
        "icono": "🏦",
        "horas": "13.5 hrs (15 sesiones)",
        "prerequisitos": ["b2_herramientas_contables", "b2_matematica_basica_2", "b3_matematica_aplicada_1"],
        "prerequisitos_texto": "Herramientas Contables (B2-C2), Matemática Básica 2 (B2-C4) y Matemática Aplicada 1 (B3-C4)",
        "habilita": [],
        "habilita_texto": "Justificación financiera de inversiones de capital (CAPEX) y proyectos de graduación",
        "objetivo_transversal": "Dominar el interés compuesto y las herramientas de evaluación económica para justificar financieramente compras de maquinaria, reemplazos y proyectos de automatización técnica.",
        "unidades": [
            {
                "num": "Unidad 1",
                "titulo": "El Valor del Dinero en el Tiempo e Interés Compuesto",
                "temas": [
                    "Concepto fundamental: el valor del dinero en el tiempo, inflación y costo de oportunidad del capital",
                    "Interés simple vs. interés compuesto: capitalización discreta (mensual, trimestral, anual) y continua",
                    "Tasas de interés nominales vs. Tasas Efectivas Anuales (TEA) en el sistema financiero guatemalteco",
                    "Fórmulas financieras en Excel: Valor Futuro (VF), Valor Presente (VP), Tasa y Número de periodos (NPER)"
                ]
            },
            {
                "num": "Unidad 2",
                "titulo": "Anualidades y Tablas de Amortización de Financiamiento y Leasing",
                "temas": [
                    "Concepto de anualidad ordinaria y anticipada: cuotas constantes de pago",
                    "Construcción en Excel de tablas de amortización de préstamos comerciales: Método Francés (cuota fija) y Alemán",
                    "Desglose de cuotas en amortización de capital, intereses e IVA",
                    "Análisis financiero del Arrendamiento Operativo y Financiero (Leasing) para adquisición de maquinaria pesada"
                ]
            },
            {
                "num": "Unidad 3",
                "titulo": "Evaluación Financiera de Proyectos Técnicos: VPN y TIR",
                "temas": [
                    "Construcción de Flujos de Caja Libres (FCL) de proyectos técnicos: inversión inicial, ahorros y gastos operativos",
                    "Determinación de la Tasa Mínima Aceptable de Rendimiento (TMAR / WACC) de la empresa",
                    "Cálculo e interpretación del Valor Presente Neto (VPN / VNA en Excel): regla de decisión de aceptación",
                    "Cálculo de la Tasa Interna de Retorno (TIR): comparación con la TMAR para evaluar rentabilidad"
                ]
            },
            {
                "num": "Unidad 4",
                "titulo": "Periodo de Recuperación (Payback) y Análisis de Reemplazo de Equipos",
                "temas": [
                    "Cálculo del Periodo de Recuperación de la Inversión simple y descontado (Payback)",
                    "Análisis de reemplazo de maquinaria: ¿reparar la máquina existente o comprar equipo moderno automatizado?",
                    "Costo Anual Uniforme Equivalente (CAUE) y Costo de Ciclo de Vida del Activo (Life Cycle Cost - LCC)",
                    "Sustentación financiera formal para la aprobación de compras de capital (CAPEX) ante comités de inversión"
                ]
            }
        ],
        "subtema_ia": "Simulaciones estocásticas de Monte Carlo asistidas por IA para análisis de riesgo e incertidumbre en presupuestos de inversión técnica y variación de precios de insumos.",
        "herramientas": "Funciones financieras avanzadas en Excel (VNA, TIR, PAGO, TASA), simuladores de flujos de caja y modelos de reemplazo LCC.",
        "aplicabilidad_7": "Justificar la compra de una retroexcavadora en construcción, un escáner automotriz avanzado de última generación, un torno CNC industrial, la migración a servidores en la nube o un analizador de espectro de telecomunicaciones.",
        "dictamen_link": "b4_matematica_aplicada_2.html"
    },

    "b4_fisica_aplicada_3": {
        "id": "b4_fisica_aplicada_3",
        "codigo": "B4-C5",
        "nombre": "Física Aplicada 3",
        "subtitulo": "Sensores Transversales, Instrumentación y Programación Aplicada con Python",
        "bimestre": "Bimestre 4",
        "bimestre_num": 4,
        "periodo": "Periodo 5 (50 min)",
        "linea_id": "linea-fisica",
        "eje": "Física y Tecnología",
        "icono": "💻",
        "horas": "13.5 hrs (15 sesiones)",
        "prerequisitos": ["b3_fisica_aplicada_2", "b2_matematica_basica_2", "b1_matematica_basica_1"],
        "prerequisitos_texto": "Física Aplicada 2 (B3-C5), Matemática Básica 2 / Lógica (B2-C4) y Matemática Básica 1 (B1-C4)",
        "habilita": [],
        "habilita_texto": "Industria 4.0, automatización de scripts técnicos y titulación TSU",
        "objetivo_transversal": "Comprender los principios físicos de sensores y transductores de planta y dominar la programación en Python para automatizar cálculos técnicos, procesar datos y generar reportes.",
        "unidades": [
            {
                "num": "Unidad 1",
                "titulo": "Fundamentos Físicos de Medición y Sensores Transversales de Planta",
                "temas": [
                    "Concepto de transductor: conversión de variable física a señal eléctrica medible (voltaje, corriente, resistencia)",
                    "Sensores de temperatura: termocuplas (efecto Seebeck), RTD (Pt100) y termistores (NTC/PTC)",
                    "Sensores de proximidad y presencia: inductivos, capacitivos, fotoeléctricos e interruptores mecánicos de límite",
                    "Sensores de presión y nivel: galgas extensiométricas, piezoeléctricos, ultrasonido y radar",
                    "Estandarización de señales analógicas de planta: bucles de corriente 4-20 mA y 0-10 VDC"
                ]
            },
            {
                "num": "Unidad 2",
                "titulo": "Lógica de Programación y Sintaxis Básica de Python para Técnicos",
                "temas": [
                    "Entorno de trabajo en Python: instalación de Python 3, uso de Jupyter Notebooks y editores (VS Code)",
                    "Tipos de datos fundamentales: enteros (int), decimales (float), cadenas de texto (str) y booleanos (bool)",
                    "Operadores aritméticos, de comparación y lógicos (and, or, not) aplicados a cálculos técnicos",
                    "Estructuras condicionales de decisión: if, elif, else para validación de rangos admisibles de operación"
                ]
            },
            {
                "num": "Unidad 3",
                "titulo": "Bucles de Control, Funciones Modulares y Procesamiento de Archivos CSV",
                "temas": [
                    "Estructuras iterativas: bucles for y bucles while para procesamiento repetitivo de mediciones",
                    "Colecciones de datos: listas, tuplas y diccionarios para estructurar parámetros de maquinaria",
                    "Definición de funciones modulares (def) para reutilización de fórmulas técnicas y modularidad",
                    "Lectura y escritura de archivos planos de datos (CSV / TXT): carga de registros históricos de máquinas"
                ]
            },
            {
                "num": "Unidad 4",
                "titulo": "Visualización Gráfica de Variables Físicas con Matplotlib y Automatización",
                "temas": [
                    "Introducción a la librería matplotlib.pyplot para graficación técnica profesional",
                    "Generación de gráficos de dispersión, líneas de tendencia temporal e histogramas de variables físicas",
                    "Etiquetado técnico de ejes con unidades, títulos, leyendas y cuadrículas de lectura",
                    "Desarrollo de un script integral de automatización que procesa un archivo CSV de lecturas de sensores y emite un informe gráfico de anomalías"
                ]
            }
        ],
        "subtema_ia": "Asistentes de codificación con Inteligencia Artificial (Copilot / ChatGPT) para generación, explicación y depuración de scripts en Python a partir de instrucciones en lenguaje natural.",
        "herramientas": "Python 3, Jupyter Notebook / VS Code, bibliotecas matplotlib y pandas básico, sensores industriales transversales.",
        "aplicabilidad_7": "Script en Python para cubicaje y cálculo de materiales (construcción), integración con APIs y backend (software), cálculo automatizado de caídas de tensión (electricidad), adquisición de datos de instrumentación (electrónica), procesamiento de registros OBD-II (automotriz), bitácoras de fallas de maquinaria (mecánica), scripts de monitoreo continuo de conectividad de red (telecomunicaciones).",
        "dictamen_link": "b4_fisica_aplicada_3.html"
    }
}

print(f"Total cursos cargados: {len(cursos_data)}")

# -------------------------------------------------------------
# GENERADOR 1: TSU/temarios_por_linea.html
# -------------------------------------------------------------
def generate_temarios_por_linea_html():
    nav_links = """
        <a href="index.html">Portal General (20 Cursos)</a>
        <a href="mapa_curricular.html">🗺️ Mapa y Red Curricular</a>
        <a href="temarios_por_linea.html" class="active">📚 Temarios por Línea de Estudio</a>
        <a href="nueva_distribucion_tematica_tsu.html" style="color: #fef08a; font-weight: 700;">🌟 Distribución Temática 2026</a>
    """

    lineas_html = ""
    for linea in lineas_estudio:
        cursos_en_linea = [cursos_data[cid] for cid in linea["cursos_ids"]]
        total_cursos = len(cursos_en_linea)
        total_horas = total_cursos * 13.5
        
        cards_html = ""
        for c in cursos_en_linea:
            unidades_html = ""
            for u in c["unidades"]:
                temas_li = "".join([f"<li>{t}</li>" for t in u["temas"]])
                unidades_html += f"""
                <div class="unidad-box">
                    <div class="unidad-title">
                        <span class="unidad-badge">{u["num"]}</span>
                        <h4>{u["titulo"]}</h4>
                    </div>
                    <ul class="unidad-temas">
                        {temas_li}
                    </ul>
                </div>
                """

            prereq_badges = ""
            if c["prerequisitos"]:
                prereq_badges = " ".join([f'<a href="#{pr}" class="conn-pill prereq-pill">{cursos_data[pr]["codigo"]} • {cursos_data[pr]["nombre"]}</a>' for pr in c["prerequisitos"]])
            else:
                prereq_badges = '<span class="conn-pill no-prereq">Ingreso TSU (Sin prerrequisito previo de 3er año)</span>'

            habilita_badges = ""
            if c["habilita"]:
                habilita_badges = " ".join([f'<a href="#{hb}" class="conn-pill habilita-pill">{cursos_data[hb]["codigo"]} • {cursos_data[hb]["nombre"]}</a>' for hb in c["habilita"]])
            else:
                habilita_badges = '<span class="conn-pill final-curso">Culminación del Plan / Graduación TSU</span>'

            cards_html += f"""
            <article class="temario-card" id="{c["id"]}" data-bimestre="{c["bimestre_num"]}" data-linea="{linea["id"]}">
                <div class="temario-header">
                    <div class="temario-meta">
                        <span class="badge-bimestre">{c["bimestre"]}</span>
                        <span class="badge-periodo">{c["periodo"]}</span>
                        <span class="badge-code">{c["codigo"]}</span>
                        <span class="badge-horas">⏱️ {c["horas"]}</span>
                    </div>
                    <div class="temario-title-bar">
                        <h3><span>{c["icono"]}</span> {c["nombre"]}</h3>
                        <a href="{c["dictamen_link"]}" class="btn-dictamen" title="Ver auditoría comparativa completa">Auditoría Individual →</a>
                    </div>
                    <div class="temario-subtitulo">{c["subtitulo"]}</div>
                </div>

                <div class="temario-body">
                    <div class="temario-callout">
                        <strong>🎯 Objetivo Curricular Transversal:</strong> {c["objetivo_transversal"]}
                    </div>

                    <div class="correlatividades-box">
                        <div class="corr-item">
                            <span class="corr-label">⬅️ Prerrequisito Requerido:</span>
                            <div class="corr-links">{prereq_badges}</div>
                        </div>
                        <div class="corr-item">
                            <span class="corr-label">➡️ Habilita a / Da Paso a:</span>
                            <div class="corr-links">{habilita_badges}</div>
                        </div>
                    </div>

                    <div class="unidades-container">
                        <div class="unidades-header">
                            <h5>📖 Contenido y Unidades Temáticas Modernizadas (Pensum 2026)</h5>
                            <button class="btn-toggle-unidades" onclick="toggleUnidades('{c["id"]}')">Desplegar / Ocultar Temas</button>
                        </div>
                        <div class="unidades-content" id="unidades-{c["id"]}">
                            {unidades_html}
                        </div>
                    </div>

                    <div class="ia-box">
                        <div class="ia-header">
                            <span class="ia-badge">🤖 Subtema de Inteligencia Artificial (IA)</span>
                        </div>
                        <p>{c["subtema_ia"]}</p>
                    </div>

                    <div class="temario-footer-grid">
                        <div class="footer-block">
                            <strong>🛠️ Herramientas, Software y Normas Aplicadas:</strong>
                            <p>{c["herramientas"]}</p>
                        </div>
                        <div class="footer-block">
                            <strong>🏗️ Aplicabilidad a las 7 Especialidades de Kinal:</strong>
                            <p>{c["aplicabilidad_7"]}</p>
                        </div>
                    </div>
                </div>
            </article>
            """

        lineas_html += f"""
        <section class="linea-section" id="{linea["id"]}">
            <div class="linea-header" style="border-left-color: {linea["color_accent"]};">
                <div class="linea-header-info">
                    <span class="linea-badge" style="background: {linea["color_bg"]}; color: {linea["color_accent"]}; border-color: {linea["color_border"]};">
                        Línea de Estudio Especializada
                    </span>
                    <h2><span>{linea["icono"]}</span> {linea["nombre"]}</h2>
                    <p class="linea-desc">{linea["descripcion"]}</p>
                </div>
                <div class="linea-stats">
                    <div class="stat-pill"><strong>{total_cursos}</strong> Cursos</div>
                    <div class="stat-pill"><strong>{total_horas}</strong> Horas</div>
                    <div class="stat-pill"><strong>B1 a B4</strong></div>
                </div>
            </div>
            
            <div class="linea-courses-list">
                {cards_html}
            </div>
        </section>
        """

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Temarios por Línea de Estudio | Técnico Superior Universitario (TSU) Kinal</title>
    <style>
        :root {{
            --kinal-blue: #0f2d59;
            --kinal-blue-dark: #0b1f3a;
            --kinal-accent: #d97706;
            --kinal-light: #f8fafc;
            --text-dark: #1e293b;
            --text-muted: #64748b;
            --border-color: #cbd5e1;
            --border-light: #e2e8f0;
            --color-actualizar-bg: #fef9c3;
            --color-actualizar-text: #854d0e;
            --color-anular-bg: #fee2e2;
            --color-anular-text: #991b1b;
            --color-nuevo-bg: #dbeafe;
            --color-nuevo-text: #1e40af;
            --color-ia: #6366f1;
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
            max-width: 1320px;
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
            padding: 4px 14px;
            border-radius: 20px;
            font-size: 0.82rem;
            font-weight: 700;
            letter-spacing: 0.5px;
            margin-bottom: 12px;
            text-transform: uppercase;
        }}
        header h1 {{ font-size: 2.1rem; font-weight: 700; margin-bottom: 8px; }}
        header p {{ color: #cbd5e1; font-size: 1.02rem; max-width: 950px; }}

        nav.nav-bar {{
            background: var(--kinal-blue-dark);
            padding: 0 40px;
            display: flex;
            gap: 16px;
            overflow-x: auto;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }}
        nav.nav-bar a {{
            color: #94a3b8;
            text-decoration: none;
            padding: 14px 18px;
            font-weight: 600;
            font-size: 0.92rem;
            display: inline-block;
            border-bottom: 3px solid transparent;
            transition: all 0.2s;
            white-space: nowrap;
        }}
        nav.nav-bar a:hover {{ color: #ffffff; border-bottom-color: var(--kinal-accent); }}
        nav.nav-bar a.active {{ color: #ffffff; background: rgba(255,255,255,0.08); border-bottom-color: var(--kinal-accent); }}

        main {{ padding: 36px 40px; }}

        /* CONTROLES Y SELECTOR DE LÍNEA */
        .controls-panel {{
            background: #f8fafc;
            border: 1px solid var(--border-color);
            border-radius: 10px;
            padding: 20px 24px;
            margin-bottom: 32px;
            display: flex;
            flex-direction: column;
            gap: 16px;
        }}
        .controls-top {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 12px;
        }}
        .controls-top h3 {{
            font-size: 1.15rem;
            color: var(--kinal-blue);
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .search-box {{
            flex-grow: 1;
            max-width: 360px;
            position: relative;
        }}
        .search-input {{
            width: 100%;
            padding: 8px 14px 8px 36px;
            border: 1px solid var(--border-color);
            border-radius: 6px;
            font-size: 0.9rem;
            outline: none;
            transition: border-color 0.2s;
        }}
        .search-input:focus {{
            border-color: var(--kinal-accent);
            box-shadow: 0 0 0 2px rgba(217, 119, 6, 0.2);
        }}
        .search-icon {{
            position: absolute;
            left: 10px;
            top: 50%;
            transform: translateY(-50%);
            color: var(--text-muted);
            font-size: 0.9rem;
        }}

        .linea-tabs {{
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }}
        .tab-btn {{
            background: #ffffff;
            border: 1px solid var(--border-color);
            padding: 9px 16px;
            border-radius: 6px;
            font-size: 0.88rem;
            font-weight: 600;
            color: var(--text-dark);
            cursor: pointer;
            transition: all 0.2s;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .tab-btn:hover {{
            background: #f1f5f9;
            border-color: var(--kinal-blue);
        }}
        .tab-btn.active {{
            background: var(--kinal-blue);
            color: #ffffff;
            border-color: var(--kinal-blue);
            box-shadow: 0 2px 6px rgba(15, 45, 89, 0.25);
        }}
        .tab-count {{
            background: rgba(0,0,0,0.08);
            padding: 2px 6px;
            border-radius: 10px;
            font-size: 0.75rem;
        }}
        .tab-btn.active .tab-count {{
            background: rgba(255,255,255,0.25);
            color: #ffffff;
        }}

        .filter-actions {{
            display: flex;
            gap: 10px;
            align-items: center;
            flex-wrap: wrap;
            padding-top: 10px;
            border-top: 1px solid var(--border-light);
            font-size: 0.85rem;
            color: var(--text-muted);
        }}
        .action-link {{
            background: none;
            border: none;
            color: var(--kinal-blue);
            font-weight: 600;
            cursor: pointer;
            text-decoration: underline;
            padding: 0 4px;
        }}

        /* SECCIONES POR LÍNEA */
        .linea-section {{
            margin-bottom: 48px;
            scroll-margin-top: 30px;
        }}
        .linea-header {{
            background: #ffffff;
            border: 1px solid var(--border-color);
            border-left: 6px solid var(--kinal-blue);
            border-radius: 8px;
            padding: 22px 28px;
            margin-bottom: 24px;
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            flex-wrap: wrap;
            gap: 16px;
            box-shadow: 0 2px 6px rgba(0,0,0,0.03);
        }}
        .linea-header-info {{ flex: 1; min-width: 280px; }}
        .linea-badge {{
            display: inline-block;
            padding: 3px 10px;
            border-radius: 4px;
            font-size: 0.78rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            border: 1px solid;
            margin-bottom: 8px;
        }}
        .linea-header h2 {{
            font-size: 1.45rem;
            color: var(--kinal-blue);
            margin-bottom: 6px;
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        .linea-desc {{
            color: var(--text-muted);
            font-size: 0.94rem;
            line-height: 1.5;
        }}
        .linea-stats {{
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }}
        .stat-pill {{
            background: #f1f5f9;
            border: 1px solid var(--border-color);
            padding: 6px 12px;
            border-radius: 6px;
            font-size: 0.85rem;
            color: #334155;
            white-space: nowrap;
        }}

        /* TARJETAS DE TEMARIO DE CURSO */
        .linea-courses-list {{
            display: flex;
            flex-direction: column;
            gap: 24px;
        }}
        .temario-card {{
            background: #ffffff;
            border: 1px solid var(--border-color);
            border-radius: 10px;
            overflow: hidden;
            box-shadow: 0 2px 8px rgba(0,0,0,0.04);
            transition: transform 0.2s, box-shadow 0.2s;
            scroll-margin-top: 40px;
        }}
        .temario-card:hover {{
            box-shadow: 0 4px 14px rgba(0,0,0,0.07);
        }}
        .temario-header {{
            background: #f8fafc;
            padding: 20px 24px;
            border-bottom: 1px solid var(--border-color);
        }}
        .temario-meta {{
            display: flex;
            gap: 8px;
            align-items: center;
            flex-wrap: wrap;
            margin-bottom: 8px;
        }}
        .badge-bimestre {{
            background: #e2e8f0;
            color: #1e293b;
            padding: 3px 8px;
            border-radius: 4px;
            font-size: 0.78rem;
            font-weight: 700;
        }}
        .badge-periodo {{
            background: #fef3c7;
            color: #92400e;
            padding: 3px 8px;
            border-radius: 4px;
            font-size: 0.78rem;
            font-weight: 600;
        }}
        .badge-code {{
            background: var(--kinal-blue);
            color: #ffffff;
            padding: 3px 8px;
            border-radius: 4px;
            font-size: 0.78rem;
            font-weight: 700;
        }}
        .badge-horas {{
            background: #e0f2fe;
            color: #0369a1;
            padding: 3px 8px;
            border-radius: 4px;
            font-size: 0.78rem;
            font-weight: 600;
        }}

        .temario-title-bar {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 12px;
            margin-bottom: 4px;
        }}
        .temario-title-bar h3 {{
            font-size: 1.25rem;
            color: var(--kinal-blue);
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        .btn-dictamen {{
            color: var(--kinal-blue);
            text-decoration: none;
            font-size: 0.85rem;
            font-weight: 600;
            padding: 5px 12px;
            border: 1px solid var(--border-color);
            border-radius: 6px;
            background: #ffffff;
            transition: all 0.2s;
        }}
        .btn-dictamen:hover {{
            background: var(--kinal-blue);
            color: #ffffff;
            border-color: var(--kinal-blue);
        }}
        .temario-subtitulo {{
            font-size: 0.95rem;
            color: var(--text-muted);
            font-weight: 500;
        }}

        .temario-body {{ padding: 24px; }}

        .temario-callout {{
            background: #eff6ff;
            border-left: 4px solid #3b82f6;
            padding: 12px 18px;
            border-radius: 0 6px 6px 0;
            font-size: 0.92rem;
            color: #1e3a8a;
            margin-bottom: 18px;
        }}

        /* CORRELATIVIDADES */
        .correlatividades-box {{
            background: #f8fafc;
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 14px 18px;
            margin-bottom: 20px;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 12px;
        }}
        .corr-item {{
            display: flex;
            flex-direction: column;
            gap: 6px;
        }}
        .corr-label {{
            font-size: 0.78rem;
            font-weight: 700;
            text-transform: uppercase;
            color: var(--text-muted);
            letter-spacing: 0.4px;
        }}
        .corr-links {{
            display: flex;
            gap: 6px;
            flex-wrap: wrap;
        }}
        .conn-pill {{
            display: inline-block;
            padding: 4px 10px;
            border-radius: 6px;
            font-size: 0.8rem;
            font-weight: 600;
            text-decoration: none;
            transition: all 0.2s;
        }}
        .prereq-pill {{
            background: #ecfdf5;
            color: #065f46;
            border: 1px solid #a7f3d0;
        }}
        .prereq-pill:hover {{
            background: #d1fae5;
            border-color: #059669;
        }}
        .habilita-pill {{
            background: #fdf4ff;
            color: #86198f;
            border: 1px solid #f5d0fe;
        }}
        .habilita-pill:hover {{
            background: #fae8ff;
            border-color: #c026d3;
        }}
        .no-prereq {{
            background: #f1f5f9;
            color: #64748b;
            border: 1px solid #cbd5e1;
            font-size: 0.78rem;
        }}
        .final-curso {{
            background: #fef3c7;
            color: #92400e;
            border: 1px solid #fde68a;
            font-size: 0.78rem;
        }}

        /* UNIDADES TEMÁTICAS */
        .unidades-container {{
            margin-bottom: 20px;
        }}
        .unidades-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 12px;
        }}
        .unidades-header h5 {{
            font-size: 1rem;
            color: var(--kinal-blue);
            font-weight: 700;
        }}
        .btn-toggle-unidades {{
            background: none;
            border: 1px solid var(--border-color);
            padding: 4px 10px;
            border-radius: 4px;
            font-size: 0.78rem;
            color: var(--text-dark);
            cursor: pointer;
            font-weight: 600;
        }}
        .btn-toggle-unidades:hover {{
            background: #f1f5f9;
        }}
        .unidades-content {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 14px;
        }}
        .unidad-box {{
            background: #ffffff;
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 14px 16px;
        }}
        .unidad-title {{
            display: flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 10px;
            padding-bottom: 6px;
            border-bottom: 1px solid var(--border-light);
        }}
        .unidad-badge {{
            background: #f1f5f9;
            color: var(--kinal-blue);
            font-size: 0.72rem;
            font-weight: 800;
            padding: 2px 6px;
            border-radius: 4px;
            text-transform: uppercase;
        }}
        .unidad-title h4 {{
            font-size: 0.88rem;
            color: var(--kinal-blue);
            line-height: 1.3;
        }}
        .unidad-temas {{
            padding-left: 18px;
            font-size: 0.82rem;
            color: #334155;
            line-height: 1.45;
        }}
        .unidad-temas li {{
            margin-bottom: 6px;
        }}

        /* IA Y FOOTER */
        .ia-box {{
            background: var(--color-ia-bg);
            border-left: 4px solid var(--color-ia);
            padding: 14px 18px;
            border-radius: 0 8px 8px 0;
            margin-bottom: 18px;
        }}
        .ia-header {{ margin-bottom: 4px; }}
        .ia-badge {{
            font-size: 0.75rem;
            font-weight: 800;
            color: var(--color-ia);
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        .ia-box p {{
            font-size: 0.88rem;
            color: #312e81;
            margin: 0;
        }}

        .temario-footer-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 14px;
            padding-top: 14px;
            border-top: 1px solid var(--border-light);
            font-size: 0.86rem;
        }}
        .footer-block strong {{
            display: block;
            color: var(--kinal-blue);
            margin-bottom: 4px;
            font-size: 0.82rem;
            text-transform: uppercase;
            letter-spacing: 0.3px;
        }}
        .footer-block p {{
            color: var(--text-dark);
            line-height: 1.45;
        }}

        footer {{
            background: var(--kinal-blue-dark);
            color: #94a3b8;
            padding: 24px 40px;
            font-size: 0.88rem;
            text-align: center;
        }}

        @media (max-width: 768px) {{
            body {{ padding: 12px; }}
            header {{ padding: 24px 20px; }}
            main {{ padding: 20px 16px; }}
            .unidades-content {{ grid-template-columns: 1fr; }}
            .controls-top {{ flex-direction: column; align-items: stretch; }}
            .search-box {{ max-width: 100%; }}
        }}
    </style>
</head>
<body>

<div class="container">
    <header>
        <span class="header-badge">Sub-Portal de Programas Curriculares TSU</span>
        <h1>TEMARIOS POR LÍNEA DE ESTUDIO</h1>
        <p>Visualización exhaustiva de los temarios modernizados de las 4 líneas formativas transversales del Técnico Superior Universitario (TSU) de Fundación Kinal (Avalado por Universidad del Istmo - UNIS). Incluye competencias DQR 5/6, integración de IA y aplicación práctica a las 7 especialidades técnicas.</p>
    </header>

    <nav class="nav-bar">
        {nav_links}
    </nav>

    <main>
        <div class="controls-panel">
            <div class="controls-top">
                <h3><span>🔍</span> Explorador de Temarios por Eje Formativo</h3>
                <div class="search-box">
                    <span class="search-icon">🔎</span>
                    <input type="text" id="searchInput" class="search-input" placeholder="Buscar por tema, software, código (ej. Python, OEE, B2-C4)..." onkeyup="filterTemarios()">
                </div>
            </div>

            <div class="linea-tabs">
                <button class="tab-btn active" onclick="filterByLinea('all', this)">
                    <span>🌐</span> Todas las Líneas <span class="tab-count">20</span>
                </button>
                <button class="tab-btn" onclick="filterByLinea('linea-etica', this)">
                    <span>🛡️</span> Formación Humana y Ética <span class="tab-count">4</span>
                </button>
                <button class="tab-btn" onclick="filterByLinea('linea-gestion', this)">
                    <span>📋</span> Gestión y Supervisión <span class="tab-count">8</span>
                </button>
                <button class="tab-btn" onclick="filterByLinea('linea-matematica', this)">
                    <span>📐</span> Ciencias Exactas y Analítica <span class="tab-count">4</span>
                </button>
                <button class="tab-btn" onclick="filterByLinea('linea-fisica', this)">
                    <span>⚡</span> Física y Tecnología 4.0 <span class="tab-count">4</span>
                </button>
            </div>

            <div class="filter-actions">
                <span>Acciones rápidas:</span>
                <button class="action-link" onclick="toggleAllUnidades(true)">Expandir todas las unidades</button> • 
                <button class="action-link" onclick="toggleAllUnidades(false)">Colapsar todas las unidades</button> • 
                <a href="mapa_curricular.html" style="color: var(--kinal-accent); font-weight: 700; text-decoration: none;">🗺️ Ver Flujograma y Red en el Mapa Curricular →</a>
            </div>
        </div>

        {lineas_html}

    </main>

    <footer>
        Fundación Kinal • Escuela Técnica Superior • Pensum TSU 2026 • Convenio Universidad del Istmo (UNIS) • Guatemala, 2026
    </footer>
</div>

<script>
    function filterByLinea(lineaId, btn) {{
        document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
        if (btn) btn.classList.add('active');

        const sections = document.querySelectorAll('.linea-section');
        sections.forEach(sec => {{
            if (lineaId === 'all' || sec.id === lineaId) {{
                sec.style.display = 'block';
            }} else {{
                sec.style.display = 'none';
            }}
        }});
    }}

    function filterTemarios() {{
        const query = document.getElementById('searchInput').value.toLowerCase().trim();
        const cards = document.querySelectorAll('.temario-card');

        cards.forEach(card => {{
            const text = card.innerText.toLowerCase();
            if (text.includes(query)) {{
                card.style.display = 'block';
            }} else {{
                card.style.display = 'none';
            }}
        }});
    }}

    function toggleUnidades(id) {{
        const content = document.getElementById('unidades-' + id);
        if (content) {{
            if (content.style.display === 'none') {{
                content.style.display = 'grid';
            }} else {{
                content.style.display = 'none';
            }}
        }}
    }}

    function toggleAllUnidades(expand) {{
        document.querySelectorAll('.unidades-content').forEach(content => {{
            content.style.display = expand ? 'grid' : 'none';
        }});
    }}
</script>

</body>
</html>
"""
    return html

# -------------------------------------------------------------
# GENERADOR 2: TSU/mapa_curricular.html
# -------------------------------------------------------------
def generate_mapa_curricular_html():
    nav_links = """
        <a href="index.html">Portal General (20 Cursos)</a>
        <a href="mapa_curricular.html" class="active">🗺️ Mapa y Red Curricular</a>
        <a href="temarios_por_linea.html">📚 Temarios por Línea de Estudio</a>
        <a href="nueva_distribucion_tematica_tsu.html" style="color: #fef08a; font-weight: 700;">🌟 Distribución Temática 2026</a>
    """

    # Construir la Rejilla Curricular (Bimestre 1 a 4 x 4 Líneas)
    grid_rows_html = ""
    for linea in lineas_estudio:
        cursos_linea = [cursos_data[cid] for cid in linea["cursos_ids"]]
        b_cols = {1: [], 2: [], 3: [], 4: []}
        for c in cursos_linea:
            b_cols[c["bimestre_num"]].append(c)

        cols_html = ""
        for b_num in range(1, 5):
            c_list = b_cols[b_num]
            cards_in_col = ""
            for c in c_list:
                prereqs_str = ",".join(c["prerequisitos"])
                habilita_str = ",".join(c["habilita"])
                
                cards_in_col += f"""
                <div class="node-card" id="node-{c["id"]}" 
                     data-id="{c["id"]}" 
                     data-codigo="{c["codigo"]}"
                     data-linea="{c["linea_id"]}"
                     data-prereq="{prereqs_str}" 
                     data-habilita="{habilita_str}"
                     onclick="selectCourseNode('{c["id"]}')"
                     onmouseenter="highlightNodeRuta('{c["id"]}')"
                     onmouseleave="clearHighlightNode()">
                    <div class="node-badge-row">
                        <span class="node-code">{c["codigo"]}</span>
                        <span class="node-period">{c["periodo"].split()[0]} {c["periodo"].split()[1]}</span>
                    </div>
                    <div class="node-title">
                        <span class="node-icon">{c["icono"]}</span>
                        <strong>{c["nombre"]}</strong>
                    </div>
                    <div class="node-sub">{c["subtitulo"]}</div>
                    <div class="node-conn-summary">
                        <span class="conn-count in" title="Prerrequisitos previos">⬅️ {len(c["prerequisitos"])}</span>
                        <span class="conn-count out" title="Cursos que desbloquea">➡️ {len(c["habilita"])}</span>
                    </div>
                </div>
                """
            cols_html += f"""
            <div class="grid-cell bimestre-col-{b_num}">
                {cards_in_col}
            </div>
            """

        grid_rows_html += f"""
        <div class="grid-linea-row" id="row-{linea["id"]}">
            <div class="grid-linea-label" style="border-left-color: {linea["color_accent"]};">
                <span class="linea-row-icon">{linea["icono"]}</span>
                <div>
                    <strong>{linea["nombre"]}</strong>
                    <div class="linea-row-sub">{len(cursos_linea)} Asignaturas • {len(cursos_linea)*13.5} hrs</div>
                </div>
            </div>
            <div class="grid-linea-cols">
                {cols_html}
            </div>
        </div>
        """

    # Construir el Grafo SVG de la Red Curricular
    # Coordenadas de los centros de los 20 nodos
    col_x = {1: 125, 2: 375, 3: 625, 4: 875}
    row_y = {
        # Bimestre 1
        "b1_etica_general_1": 80,
        "b1_fundamentos_administracion": 200,
        "b1_planeacion_control_trabajo": 320,
        "b1_matematica_basica_1": 450,
        "b1_fisica_basica_1": 580,
        # Bimestre 2
        "b2_etica_general_2": 80,
        "b2_herramientas_contables": 200,
        "b2_administracion_rrhh_sso": 320,
        "b2_matematica_basica_2": 450,
        "b2_fisica_aplicada_1": 580,
        # Bimestre 3
        "b3_etica_profesional_1": 80,
        "b3_metodos_produccion": 200,
        "b3_servicio_cliente": 320,
        "b3_matematica_aplicada_1": 450,
        "b3_fisica_aplicada_2": 580,
        # Bimestre 4
        "b4_etica_profesional_2": 80,
        "b4_control_calidad": 200,
        "b4_fundamentos_marketing": 320,
        "b4_matematica_aplicada_2": 450,
        "b4_fisica_aplicada_3": 580,
    }

    # Color de borde/acento de cada línea
    linea_color_map = {
        "linea-etica": "#0284c7",
        "linea-gestion": "#d97706",
        "linea-matematica": "#16a34a",
        "linea-fisica": "#7c3aed"
    }

    node_w = 170
    node_h = 60

    # 1. Rutas SVG (Edges con flechas dirigidas)
    svg_edges_html = ""
    for cid, c in cursos_data.items():
        x1 = col_x[c["bimestre_num"]] + (node_w / 2)
        y1 = row_y[cid]
        linea_id = c["linea_id"]
        base_color = linea_color_map[linea_id]

        for h_id in c["habilita"]:
            if h_id in cursos_data:
                target = cursos_data[h_id]
                x2 = col_x[target["bimestre_num"]] - (node_w / 2)
                y2 = row_y[h_id]

                dx = x2 - x1
                # Curva cúbica suave
                cx1 = x1 + dx * 0.45
                cx2 = x2 - dx * 0.45

                edge_id = f"svg-edge-{cid}-{h_id}"
                is_cross = (c["linea_id"] != target["linea_id"])
                dash_attr = 'stroke-dasharray="4 3"' if is_cross else ''

                svg_edges_html += f"""
                <path id="{edge_id}" 
                      class="svg-edge edge-source-{cid} edge-target-{h_id} edge-linea-{linea_id}"
                      data-source="{cid}" data-target="{h_id}"
                      d="M {x1} {y1} C {cx1} {y1}, {cx2} {y2}, {x2} {y2}" 
                      fill="none" 
                      stroke="{base_color}" 
                      stroke-width="2.2" 
                      stroke-opacity="0.65"
                      {dash_attr}
                      marker-end="url(#marker-{linea_id})" />
                """

    # 2. Nodos SVG
    svg_nodes_html = ""
    for cid, c in cursos_data.items():
        cx = col_x[c["bimestre_num"]]
        cy = row_y[cid]
        rx = cx - (node_w / 2)
        ry = cy - (node_h / 2)
        color = linea_color_map[c["linea_id"]]

        svg_nodes_html += f"""
        <g id="svg-node-{cid}" class="svg-node-group" data-id="{cid}" data-linea="{c["linea_id"]}"
           onclick="selectCourseNode('{cid}')" 
           onmouseenter="highlightNodeRuta('{cid}')" 
           onmouseleave="clearHighlightNode()"
           style="cursor: pointer;">
            <!-- Rectángulo de fondo -->
            <rect id="svg-rect-{cid}" class="svg-node-rect" 
                  x="{rx}" y="{ry}" width="{node_w}" height="{node_h}" rx="8" ry="8"
                  fill="#ffffff" stroke="{color}" stroke-width="2" />
            
            <!-- Franja izquierda de color de línea -->
            <path d="M {rx} {ry+8} A 8 8 0 0 1 {rx+8} {ry} L {rx+10} {ry} L {rx+10} {ry+node_h} L {rx+8} {ry+node_h} A 8 8 0 0 1 {rx} {ry+node_h-8} Z" fill="{color}" />

            <!-- Código y Bimestre -->
            <text x="{rx + 18}" y="{ry + 18}" font-size="10" font-weight="800" fill="#475569">{c["codigo"]}</text>
            <text x="{rx + node_w - 12}" y="{ry + 18}" text-anchor="end" font-size="9" font-weight="600" fill="#94a3b8">{c["periodo"].split()[0]} {c["periodo"].split()[1]}</text>

            <!-- Título del Curso -->
            <text x="{rx + 18}" y="{ry + 36}" font-size="11.5" font-weight="700" fill="#0f2d59">{c["icono"]} {c["nombre"]}</text>
            
            <!-- Resumen de subtítulo -->
            <text x="{rx + 18}" y="{ry + 50}" font-size="8.5" fill="#64748b">{c["subtitulo"][:26]}...</text>
        </g>
        """

    # Construir listado de relaciones para el panel JS
    relaciones_json = {}
    for cid, c in cursos_data.items():
        relaciones_json[cid] = {
            "id": c["id"],
            "codigo": c["codigo"],
            "nombre": c["nombre"],
            "subtitulo": c["subtitulo"],
            "bimestre": c["bimestre"],
            "periodo": c["periodo"],
            "linea_id": c["linea_id"],
            "eje": c["eje"],
            "icono": c["icono"],
            "horas": c["horas"],
            "prerequisitos": c["prerequisitos"],
            "prerequisitos_nombres": [f"{cursos_data[p]['codigo']} • {cursos_data[p]['nombre']}" for p in c["prerequisitos"]],
            "habilita": c["habilita"],
            "habilita_nombres": [f"{cursos_data[h]['codigo']} • {cursos_data[h]['nombre']}" for h in c["habilita"]],
            "objetivo": c["objetivo_transversal"],
            "subtema_ia": c["subtema_ia"],
            "herramientas": c["herramientas"],
            "dictamen_link": c["dictamen_link"]
        }

    relaciones_str = json.dumps(relaciones_json, ensure_ascii=False)

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mapa Curricular y Red de Prerrequisitos | TSU Kinal 2026</title>
    <style>
        :root {{
            --kinal-blue: #0f2d59;
            --kinal-blue-dark: #0b1f3a;
            --kinal-accent: #d97706;
            --kinal-light: #f8fafc;
            --text-dark: #1e293b;
            --text-muted: #64748b;
            --border-color: #cbd5e1;
            --border-light: #e2e8f0;
            --color-actualizar-bg: #fef9c3;
            --color-actualizar-text: #854d0e;
            --color-nuevo-bg: #dbeafe;
            --color-nuevo-text: #1e40af;
            --color-ia: #6366f1;
            /* Colores de rutas interactivas */
            --color-node-selected: #0f2d59;
            --color-node-prereq: #059669;
            --color-node-habilita: #d97706;
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
            max-width: 1420px;
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
            padding: 4px 14px;
            border-radius: 20px;
            font-size: 0.82rem;
            font-weight: 700;
            letter-spacing: 0.5px;
            margin-bottom: 12px;
            text-transform: uppercase;
        }}
        header h1 {{ font-size: 2.1rem; font-weight: 700; margin-bottom: 8px; }}
        header p {{ color: #cbd5e1; font-size: 1.02rem; max-width: 980px; }}

        nav.nav-bar {{
            background: var(--kinal-blue-dark);
            padding: 0 40px;
            display: flex;
            gap: 16px;
            overflow-x: auto;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }}
        nav.nav-bar a {{
            color: #94a3b8;
            text-decoration: none;
            padding: 14px 18px;
            font-weight: 600;
            font-size: 0.92rem;
            display: inline-block;
            border-bottom: 3px solid transparent;
            transition: all 0.2s;
            white-space: nowrap;
        }}
        nav.nav-bar a:hover {{ color: #ffffff; border-bottom-color: var(--kinal-accent); }}
        nav.nav-bar a.active {{ color: #ffffff; background: rgba(255,255,255,0.08); border-bottom-color: var(--kinal-accent); }}

        main {{ padding: 36px 40px; }}

        /* CONTROLES Y LEYENDA */
        .map-instructions {{
            background: #fffbeb;
            border-left: 4px solid var(--kinal-accent);
            padding: 18px 24px;
            border-radius: 0 8px 8px 0;
            margin-bottom: 24px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 16px;
        }}
        .map-instructions-text h4 {{
            color: #92400e;
            font-size: 1.05rem;
            margin-bottom: 4px;
        }}
        .map-instructions-text p {{
            color: #78350f;
            font-size: 0.92rem;
            margin: 0;
        }}

        .legend-bar {{
            display: flex;
            gap: 12px;
            flex-wrap: wrap;
            background: #ffffff;
            padding: 8px 14px;
            border-radius: 6px;
            border: 1px solid #fde68a;
            font-size: 0.82rem;
        }}
        .legend-chip {{
            display: flex;
            align-items: center;
            gap: 6px;
            font-weight: 600;
        }}
        .chip-dot {{
            width: 12px;
            height: 12px;
            border-radius: 3px;
            display: inline-block;
        }}
        .chip-selected {{ background: var(--color-node-selected); }}
        .chip-prereq {{ background: var(--color-node-prereq); }}
        .chip-habilita {{ background: var(--color-node-habilita); }}

        /* SELECTOR DE MODO DE VISUALIZACIÓN */
        .view-controls {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 14px;
            background: #f8fafc;
            border: 1px solid var(--border-color);
            padding: 14px 20px;
            border-radius: 8px;
            margin-bottom: 24px;
        }}
        .mode-buttons {{
            display: flex;
            gap: 10px;
        }}
        .mode-btn {{
            background: #ffffff;
            border: 1px solid var(--border-color);
            padding: 9px 18px;
            border-radius: 6px;
            font-size: 0.9rem;
            font-weight: 700;
            color: var(--text-dark);
            cursor: pointer;
            transition: all 0.2s;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .mode-btn:hover {{
            background: #f1f5f9;
            border-color: var(--kinal-blue);
        }}
        .mode-btn.active {{
            background: var(--kinal-blue);
            color: #ffffff;
            border-color: var(--kinal-blue);
            box-shadow: 0 2px 6px rgba(15, 45, 89, 0.2);
        }}

        .filter-linea-select {{
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 0.88rem;
            color: var(--text-muted);
            font-weight: 600;
        }}
        .filter-linea-select select {{
            padding: 6px 12px;
            border-radius: 6px;
            border: 1px solid var(--border-color);
            font-size: 0.88rem;
            outline: none;
            background: #ffffff;
            color: var(--text-dark);
            font-weight: 500;
        }}

        /* LAYOUT PRINCIPAL: REJILLA/GRAFO + PANEL DETALLE */
        .map-layout {{
            display: grid;
            grid-template-columns: 1fr 340px;
            gap: 24px;
            align-items: start;
        }}

        /* CONTENEDOR VISTA REJILLA */
        .curriculum-grid-container {{
            background: #ffffff;
            border: 1px solid var(--border-color);
            border-radius: 10px;
            overflow-x: auto;
            box-shadow: 0 2px 8px rgba(0,0,0,0.03);
        }}
        .grid-header-row {{
            display: grid;
            grid-template-columns: 240px repeat(4, minmax(210px, 1fr));
            background: var(--kinal-blue-dark);
            color: #ffffff;
            font-weight: 700;
            font-size: 0.92rem;
            border-bottom: 2px solid var(--kinal-accent);
        }}
        .grid-header-cell {{
            padding: 14px 16px;
            text-align: center;
            border-right: 1px solid rgba(255,255,255,0.1);
        }}
        .grid-header-cell:first-child {{
            text-align: left;
        }}
        .grid-header-cell:last-child {{
            border-right: none;
        }}

        .grid-linea-row {{
            display: grid;
            grid-template-columns: 240px 1fr;
            border-bottom: 1px solid var(--border-color);
        }}
        .grid-linea-row:last-child {{
            border-bottom: none;
        }}

        .grid-linea-label {{
            background: #f8fafc;
            border-right: 1px solid var(--border-color);
            border-left: 5px solid var(--kinal-blue);
            padding: 18px 16px;
            display: flex;
            align-items: center;
            gap: 12px;
        }}
        .linea-row-icon {{
            font-size: 1.6rem;
            line-height: 1;
        }}
        .grid-linea-label strong {{
            font-size: 0.92rem;
            color: var(--kinal-blue);
            line-height: 1.3;
            display: block;
        }}
        .linea-row-sub {{
            font-size: 0.78rem;
            color: var(--text-muted);
            margin-top: 2px;
        }}

        .grid-linea-cols {{
            display: grid;
            grid-template-columns: repeat(4, minmax(210px, 1fr));
        }}
        .grid-cell {{
            padding: 12px;
            border-right: 1px solid var(--border-color);
            display: flex;
            flex-direction: column;
            gap: 10px;
            background: #fafbfc;
        }}
        .grid-cell:last-child {{
            border-right: none;
        }}
        .grid-cell:nth-child(even) {{
            background: #ffffff;
        }}

        /* TARJETAS DE NODO (EN REJILLA) */
        .node-card {{
            background: #ffffff;
            border: 2px solid var(--border-color);
            border-radius: 8px;
            padding: 12px;
            cursor: pointer;
            transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            box-shadow: 0 1px 3px rgba(0,0,0,0.04);
        }}
        .node-card:hover {{
            transform: translateY(-2px);
            border-color: var(--kinal-blue);
            box-shadow: 0 4px 10px rgba(0,0,0,0.08);
        }}

        .node-badge-row {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 6px;
        }}
        .node-code {{
            background: #e2e8f0;
            color: #1e293b;
            font-weight: 800;
            font-size: 0.72rem;
            padding: 2px 6px;
            border-radius: 4px;
        }}
        .node-period {{
            font-size: 0.72rem;
            color: var(--text-muted);
            font-weight: 600;
        }}

        .node-title {{
            display: flex;
            align-items: flex-start;
            gap: 6px;
            margin-bottom: 4px;
        }}
        .node-icon {{ font-size: 1rem; line-height: 1.2; }}
        .node-title strong {{
            font-size: 0.88rem;
            color: var(--kinal-blue);
            line-height: 1.25;
        }}
        .node-sub {{
            font-size: 0.76rem;
            color: var(--text-muted);
            line-height: 1.3;
            margin-bottom: 8px;
            display: -webkit-box;
            -webkit-line-clamp: 2;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }}

        .node-conn-summary {{
            display: flex;
            gap: 8px;
            font-size: 0.7rem;
            border-top: 1px solid var(--border-light);
            padding-top: 6px;
        }}
        .conn-count {{
            padding: 2px 6px;
            border-radius: 4px;
            font-weight: 700;
        }}
        .conn-count.in {{ background: #ecfdf5; color: #065f46; }}
        .conn-count.out {{ background: #fffbeb; color: #92400e; }}

        /* ESTILOS DE RESALTADO DE RUTA (INTERACTIVIDAD EN REJILLA) */
        .node-card.selected {{
            border-color: var(--color-node-selected) !important;
            background: #eff6ff !important;
            box-shadow: 0 0 0 3px rgba(15, 45, 89, 0.3) !important;
            transform: scale(1.02);
            z-index: 10;
        }}
        .node-card.prereq-active {{
            border-color: var(--color-node-prereq) !important;
            background: #ecfdf5 !important;
            box-shadow: 0 0 0 2px rgba(5, 150, 105, 0.4) !important;
            z-index: 5;
        }}
        .node-card.prereq-active::after {{
            content: "⬅️ PRERREQUISITO";
            position: absolute;
            top: -9px;
            right: 8px;
            background: var(--color-node-prereq);
            color: #ffffff;
            font-size: 0.62rem;
            font-weight: 800;
            padding: 1px 5px;
            border-radius: 3px;
        }}

        .node-card.habilita-active {{
            border-color: var(--color-node-habilita) !important;
            background: #fffbeb !important;
            box-shadow: 0 0 0 2px rgba(217, 119, 6, 0.4) !important;
            z-index: 5;
        }}
        .node-card.habilita-active::after {{
            content: "➡️ HABILITA A";
            position: absolute;
            top: -9px;
            right: 8px;
            background: var(--color-node-habilita);
            color: #ffffff;
            font-size: 0.62rem;
            font-weight: 800;
            padding: 1px 5px;
            border-radius: 3px;
        }}

        .node-card.dimmed {{
            opacity: 0.32;
            filter: grayscale(40%);
        }}

        /* CONTENEDOR VISTA RED SVG */
        .network-svg-container {{
            display: none;
            background: #ffffff;
            border: 1px solid var(--border-color);
            border-radius: 10px;
            padding: 20px;
            overflow-x: auto;
            box-shadow: 0 2px 8px rgba(0,0,0,0.03);
        }}
        .svg-canvas {{
            width: 100%;
            min-width: 980px;
            height: 680px;
            display: block;
        }}

        /* ESTILOS SVG */
        .svg-edge {{
            transition: stroke 0.2s, stroke-width 0.2s, stroke-opacity 0.2s;
        }}
        .svg-edge.edge-prereq-active {{
            stroke: #059669 !important;
            stroke-width: 3.5 !important;
            stroke-opacity: 1 !important;
            marker-end: url(#marker-prereq) !important;
        }}
        .svg-edge.edge-habilita-active {{
            stroke: #d97706 !important;
            stroke-width: 3.5 !important;
            stroke-opacity: 1 !important;
            marker-end: url(#marker-habilita) !important;
        }}
        .svg-edge.dimmed {{
            stroke-opacity: 0.1 !important;
        }}

        .svg-node-rect {{
            transition: stroke 0.2s, fill 0.2s, stroke-width 0.2s, filter 0.2s;
        }}
        .svg-node-group:hover .svg-node-rect {{
            stroke-width: 3;
            filter: drop-shadow(0 4px 6px rgba(0,0,0,0.12));
        }}
        .svg-node-group.selected .svg-node-rect {{
            fill: #eff6ff !important;
            stroke: #0f2d59 !important;
            stroke-width: 3.5 !important;
            filter: drop-shadow(0 4px 10px rgba(15, 45, 89, 0.25));
        }}
        .svg-node-group.prereq-active .svg-node-rect {{
            fill: #ecfdf5 !important;
            stroke: #059669 !important;
            stroke-width: 3 !important;
        }}
        .svg-node-group.habilita-active .svg-node-rect {{
            fill: #fffbeb !important;
            stroke: #d97706 !important;
            stroke-width: 3 !important;
        }}
        .svg-node-group.dimmed {{
            opacity: 0.35;
        }}

        /* PANEL LATERAL DE DETALLE */
        .side-detail-panel {{
            background: #ffffff;
            border: 1px solid var(--border-color);
            border-radius: 10px;
            padding: 24px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.05);
            position: sticky;
            top: 24px;
        }}
        .side-detail-header {{
            padding-bottom: 14px;
            border-bottom: 1px solid var(--border-color);
            margin-bottom: 16px;
        }}
        .side-detail-badge {{
            display: inline-block;
            background: var(--kinal-blue);
            color: #ffffff;
            padding: 2px 8px;
            border-radius: 4px;
            font-size: 0.75rem;
            font-weight: 800;
            margin-bottom: 8px;
        }}
        .side-detail-header h3 {{
            font-size: 1.15rem;
            color: var(--kinal-blue);
            line-height: 1.3;
            margin-bottom: 4px;
        }}
        .side-detail-sub {{
            font-size: 0.85rem;
            color: var(--text-muted);
        }}

        .side-section {{
            margin-bottom: 16px;
        }}
        .side-section-title {{
            font-size: 0.76rem;
            font-weight: 800;
            text-transform: uppercase;
            color: var(--text-muted);
            letter-spacing: 0.4px;
            margin-bottom: 6px;
        }}
        .side-list {{
            list-style: none;
            padding: 0;
            margin: 0;
            display: flex;
            flex-direction: column;
            gap: 6px;
        }}
        .side-list li {{
            font-size: 0.82rem;
            padding: 6px 10px;
            border-radius: 6px;
            cursor: pointer;
            transition: all 0.15s;
        }}
        .side-list-prereq li {{
            background: #ecfdf5;
            color: #065f46;
            border: 1px solid #a7f3d0;
        }}
        .side-list-prereq li:hover {{
            background: #d1fae5;
        }}
        .side-list-habilita li {{
            background: #fffbeb;
            color: #92400e;
            border: 1px solid #fde68a;
        }}
        .side-list-habilita li:hover {{
            background: #fef3c7;
        }}

        .side-callout {{
            background: #f8fafc;
            border: 1px solid var(--border-light);
            padding: 12px;
            border-radius: 6px;
            font-size: 0.82rem;
            color: #334155;
            line-height: 1.4;
            margin-bottom: 16px;
        }}

        .btn-side-action {{
            display: block;
            width: 100%;
            text-align: center;
            background: var(--kinal-blue);
            color: #ffffff;
            text-decoration: none;
            padding: 10px;
            border-radius: 6px;
            font-size: 0.88rem;
            font-weight: 600;
            transition: all 0.2s;
            margin-bottom: 8px;
        }}
        .btn-side-action:hover {{
            background: #1e3a8a;
        }}
        .btn-side-alt {{
            display: block;
            width: 100%;
            text-align: center;
            background: #f1f5f9;
            color: var(--kinal-blue);
            text-decoration: none;
            padding: 8px;
            border-radius: 6px;
            font-size: 0.82rem;
            font-weight: 600;
            border: 1px solid var(--border-color);
        }}
        .btn-side-alt:hover {{
            background: #e2e8f0;
        }}

        /* SECCIÓN DE RUTAS TRANSVERSALES ESTRATÉGICAS */
        .transversal-routes {{
            margin-top: 40px;
            background: #ffffff;
            border: 1px solid var(--border-color);
            border-radius: 10px;
            padding: 28px;
        }}
        .transversal-routes h3 {{
            color: var(--kinal-blue);
            font-size: 1.3rem;
            margin-bottom: 8px;
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        .transversal-routes p {{
            color: var(--text-muted);
            font-size: 0.94rem;
            margin-bottom: 20px;
        }}

        .routes-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(310px, 1fr));
            gap: 16px;
        }}
        .route-card {{
            background: #f8fafc;
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 18px;
            border-top: 4px solid var(--kinal-blue);
        }}
        .route-card h4 {{
            font-size: 0.98rem;
            color: var(--kinal-blue);
            margin-bottom: 6px;
        }}
        .route-card p {{
            font-size: 0.85rem;
            color: var(--text-dark);
            margin-bottom: 12px;
        }}
        .route-steps {{
            display: flex;
            flex-direction: column;
            gap: 6px;
        }}
        .route-step-item {{
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 0.82rem;
            padding: 4px 8px;
            background: #ffffff;
            border: 1px solid var(--border-light);
            border-radius: 4px;
        }}
        .step-arrow {{ color: var(--kinal-accent); font-weight: 700; }}

        footer {{
            background: var(--kinal-blue-dark);
            color: #94a3b8;
            padding: 24px 40px;
            font-size: 0.88rem;
            text-align: center;
            margin-top: 40px;
        }}

        @media (max-width: 1024px) {{
            .map-layout {{ grid-template-columns: 1fr; }}
            .side-detail-panel {{ position: static; }}
        }}
    </style>
</head>
<body>

<div class="container">
    <header>
        <span class="header-badge">Malla Curricular y Flujo de Competencias</span>
        <h1>MAPA CURRICULAR Y RED DE PRERREQUISITOS (TSU)</h1>
        <p>Estructura relacional e interactiva de los 20 cursos del Técnico Superior Universitario (Fundación Kinal / Universidad del Istmo - UNIS). Alterna entre la <strong>Rejilla Curricular Matricial</strong> y el <strong>Grafo de Red con Flechas Dirigidas</strong> para descubrir qué curso conduce a cuál otro en la progresión hacia mandos medios industriales.</p>
    </header>

    <nav class="nav-bar">
        {nav_links}
    </nav>

    <main>
        <!-- Llamado de Instrucciones -->
        <div class="map-instructions">
            <div class="map-instructions-text">
                <h4>💡 Interacción con el Mapa y Detección de Rutas</h4>
                <p>Haz <strong>clic o pasa el ratón</strong> sobre cualquier tarjeta o nodo para iluminar su <strong>Ruta Crítica</strong>: se resaltarán en verde sus prerrequisitos requeridos y en ámbar los cursos que desbloquea. La ficha lateral mostrará el detalle curricular completo.</p>
            </div>
            <div class="legend-bar">
                <div class="legend-chip"><span class="chip-dot chip-selected"></span> Curso Seleccionado</div>
                <div class="legend-chip"><span class="chip-dot chip-prereq"></span> Prerrequisito Requerido</div>
                <div class="legend-chip"><span class="chip-dot chip-habilita"></span> Curso que Habilita</div>
            </div>
        </div>

        <!-- Barra de Control de Modos de Vista -->
        <div class="view-controls">
            <div class="mode-buttons">
                <button class="mode-btn active" id="btnModeGrid" onclick="switchViewMode('grid')">
                    <span>📊</span> Rejilla Curricular (Matriz 4x4)
                </button>
                <button class="mode-btn" id="btnModeNetwork" onclick="switchViewMode('network')">
                    <span>🕸️</span> Red de Correlatividades (Grafo con Flechas)
                </button>
            </div>

            <div class="filter-linea-select">
                <span>Filtrar por Línea de Estudio:</span>
                <select id="lineaFilterSelect" onchange="filterMapByLinea(this.value)">
                    <option value="all">Todas las 4 Líneas de Estudio</option>
                    <option value="linea-etica">🛡️ Formación Humana y Ética</option>
                    <option value="linea-gestion">📋 Gestión y Supervisión</option>
                    <option value="linea-matematica">📐 Ciencias Exactas y Analítica</option>
                    <option value="linea-fisica">⚡ Física y Tecnología 4.0</option>
                </select>
            </div>
        </div>

        <!-- Layout con Rejilla Curricular / Grafo SVG + Ficha Lateral -->
        <div class="map-layout">
            
            <!-- VISTA 1: REJILLA / MATRIZ CURRICULAR -->
            <div class="curriculum-grid-container" id="gridContainer">
                <div class="grid-header-row">
                    <div class="grid-header-cell">Línea Formativa / Eje</div>
                    <div class="grid-header-cell">Bimestre 1<br><small style="font-weight:400; opacity:0.8;">Fundamentos y Estática</small></div>
                    <div class="grid-header-cell">Bimestre 2<br><small style="font-weight:400; opacity:0.8;">Costos, SSO y Materiales</small></div>
                    <div class="grid-header-cell">Bimestre 3<br><small style="font-weight:400; opacity:0.8;">Lean, SLAs y Analítica</small></div>
                    <div class="grid-header-cell">Bimestre 4<br><small style="font-weight:400; opacity:0.8;">Calidad, BI, Finanzas y Python</small></div>
                </div>

                {grid_rows_html}
            </div>

            <!-- VISTA 2: RED DE CORRELATIVIDADES (GRAFO SVG) -->
            <div class="network-svg-container" id="networkContainer">
                <svg class="svg-canvas" viewBox="0 0 1020 660">
                    <defs>
                        <!-- Marcadores de Flechas para las Rutas -->
                        <marker id="marker-linea-etica" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                            <path d="M 0 1 L 10 5 L 0 9 z" fill="#0284c7" />
                        </marker>
                        <marker id="marker-linea-gestion" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                            <path d="M 0 1 L 10 5 L 0 9 z" fill="#d97706" />
                        </marker>
                        <marker id="marker-linea-matematica" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                            <path d="M 0 1 L 10 5 L 0 9 z" fill="#16a34a" />
                        </marker>
                        <marker id="marker-linea-fisica" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
                            <path d="M 0 1 L 10 5 L 0 9 z" fill="#7c3aed" />
                        </marker>
                        <!-- Marcadores activos de interacción -->
                        <marker id="marker-prereq" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
                            <path d="M 0 1 L 10 5 L 0 9 z" fill="#059669" />
                        </marker>
                        <marker id="marker-habilita" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
                            <path d="M 0 1 L 10 5 L 0 9 z" fill="#d97706" />
                        </marker>
                    </defs>

                    <!-- Columnas de Fondo de Bimestre -->
                    <rect x="30" y="10" width="190" height="640" rx="8" fill="#f8fafc" stroke="#e2e8f0" />
                    <text x="125" y="32" text-anchor="middle" font-size="12" font-weight="800" fill="#0f2d59">BIMESTRE 1</text>

                    <rect x="280" y="10" width="190" height="640" rx="8" fill="#fafbfc" stroke="#e2e8f0" />
                    <text x="375" y="32" text-anchor="middle" font-size="12" font-weight="800" fill="#0f2d59">BIMESTRE 2</text>

                    <rect x="530" y="10" width="190" height="640" rx="8" fill="#f8fafc" stroke="#e2e8f0" />
                    <text x="625" y="32" text-anchor="middle" font-size="12" font-weight="800" fill="#0f2d59">BIMESTRE 3</text>

                    <rect x="780" y="10" width="190" height="640" rx="8" fill="#fafbfc" stroke="#e2e8f0" />
                    <text x="875" y="32" text-anchor="middle" font-size="12" font-weight="800" fill="#0f2d59">BIMESTRE 4</text>

                    <!-- Rutas y Flechas Dirigidas -->
                    <g id="svgEdgesGroup">
                        {svg_edges_html}
                    </g>

                    <!-- Nodos de Cursos -->
                    <g id="svgNodesGroup">
                        {svg_nodes_html}
                    </g>
                </svg>
            </div>

            <!-- PANEL LATERAL DE FICHA TÉCNICA -->
            <aside class="side-detail-panel" id="sideDetailPanel">
                <div class="side-detail-header">
                    <span class="side-detail-badge" id="sideBadge">B1-C1</span>
                    <h3 id="sideTitle">🛡️ Ética General 1</h3>
                    <div class="side-detail-sub" id="sideSub">Antropología y Sentido Trascendente del Trabajo</div>
                </div>

                <div class="side-section">
                    <div class="side-section-title">⬅️ Prerrequisitos de Entrada</div>
                    <ul class="side-list side-list-prereq" id="sidePrereqList">
                        <li>Ingreso al 3er Año TSU</li>
                    </ul>
                </div>

                <div class="side-section">
                    <div class="side-section-title">➡️ Asignaturas que Habilita</div>
                    <ul class="side-list side-list-habilita" id="sideHabilitaList">
                        <li>B2-C1 • Ética General 2</li>
                        <li>B2-C3 • Administración de RRHH y SSO</li>
                    </ul>
                </div>

                <div class="side-section">
                    <div class="side-section-title">🎯 Objetivo Transversal</div>
                    <div class="side-callout" id="sideObjetivo">
                        Forjar el carácter ético del supervisor técnico bajo el ideario de Kinal: la persona en el centro de la operación y el trabajo bien hecho como medio de superación.
                    </div>
                </div>

                <div class="side-section">
                    <div class="side-section-title">🤖 Integración con Inteligencia Artificial</div>
                    <div class="side-callout" id="sideIA" style="background: #eef2ff; color: #3730a3; border-color: #c7d2fe;">
                        Sesgos cognitivos humanos frente a sesgos en modelos de IA: el papel de la conciencia moral que ninguna máquina puede replicar.
                    </div>
                </div>

                <div style="margin-top: 18px;">
                    <a href="b1_etica_general_1.html" class="btn-side-action" id="sideLinkDictamen">Ver Dictamen y Auditoría →</a>
                    <a href="temarios_por_linea.html#b1_etica_general_1" class="btn-side-alt" id="sideLinkTemario">Ver Temario Completo en Líneas</a>
                </div>
            </aside>

        </div>

        <!-- RUTAS TRANSVERSALES ESTRATÉGICAS (CONEXIONES ENTRE EJES) -->
        <div class="transversal-routes">
            <h3><span>🔗</span> Conexiones Curriculares Inter-Ejes (Rutas Críticas Transversales)</h3>
            <p>El pensum del TSU no opera en silos aislados: las habilidades cuantitativas y físicas sustentan directamente las decisiones operativas, financieras y éticas de los mandos medios.</p>

            <div class="routes-grid">
                <!-- Ruta Cuantitativa Financiera -->
                <div class="route-card" style="border-top-color: #16a34a;">
                    <h4>Ruta Cuantitativa & Financiera de Operaciones</h4>
                    <p>De la aritmética de escala a la justificación de inversiones de capital (CAPEX) en planta:</p>
                    <div class="route-steps">
                        <div class="route-step-item"><span>📐</span> B1-C4 Matemática Básica 1 (Excel y Proporciones)</div>
                        <div class="route-step-item"><span class="step-arrow">↓</span> 💰 B2-C2 Herramientas Contables (Costos MPD/MOD/CIF)</div>
                        <div class="route-step-item"><span class="step-arrow">↓</span> 📊 B3-C4 Matemática Aplicada 1 (Estadística y Pareto)</div>
                        <div class="route-step-item"><span class="step-arrow">↓</span> 🏦 B4-C4 Matemática Aplicada 2 (Ing. Económica VPN/TIR)</div>
                    </div>
                </div>

                <!-- Ruta de Procesos y Calidad -->
                <div class="route-card" style="border-top-color: #d97706;">
                    <h4>Ruta de Procesos, Lean & Six Sigma</h4>
                    <p>De la secuenciación de turnos al aseguramiento de cero defectos en la fuente:</p>
                    <div class="route-steps">
                        <div class="route-step-item"><span>📋</span> B1-C2 Fundamentos de la Administración</div>
                        <div class="route-step-item"><span class="step-arrow">↓</span> ⏱️ B1-C3 Planeación y Control (OEE & Kanban)</div>
                        <div class="route-step-item"><span class="step-arrow">↓</span> 🏭 B3-C2 Métodos de Producción (Lean & VSM)</div>
                        <div class="route-step-item"><span class="step-arrow">↓</span> 🎯 B4-C2 Control de Calidad (Six Sigma DMAIC & AMFE)</div>
                    </div>
                </div>

                <!-- Ruta Tecnológica e Industria 4.0 -->
                <div class="route-card" style="border-top-color: #7c3aed;">
                    <h4>Ruta de Tecnología, Datos e Industria 4.0</h4>
                    <p>De la lógica formal a la analítica de datos en Power BI y automatización con Python:</p>
                    <div class="route-steps">
                        <div class="route-step-item"><span>📉</span> B2-C4 Matemática Básica 2 (Lógica Booleana)</div>
                        <div class="route-step-item"><span class="step-arrow">↓</span> ⚡ B3-C5 Física Aplicada 2 (Energía y Curvas de Carga)</div>
                        <div class="route-step-item"><span class="step-arrow">↓</span> 📈 B4-C3 Marketing & Business Intelligence (Power BI)</div>
                        <div class="route-step-item"><span class="step-arrow">↓</span> 💻 B4-C5 Física Aplicada 3 (Sensores & Python)</div>
                    </div>
                </div>

                <!-- Ruta Ética y Factor Humano -->
                <div class="route-card" style="border-top-color: #0284c7;">
                    <h4>Ruta Ética, Legislación y Gobernanza Humana</h4>
                    <p>Del respeto inalienable a la supervisión humana indelegable (HITL):</p>
                    <div class="route-steps">
                        <div class="route-step-item"><span>🛡️</span> B1-C1 Ética General 1 (Dignidad y Sentido del Trabajo)</div>
                        <div class="route-step-item"><span class="step-arrow">↓</span> 🦺 B2-C3 Administración de RRHH & SSO (Código de Trabajo e IGSS)</div>
                        <div class="route-step-item"><span class="step-arrow">↓</span> 🤖 B3-C1 Ética Profesional 1 (Transición Justa & Reskilling)</div>
                        <div class="route-step-item"><span class="step-arrow">↓</span> 🧠 B4-C1 Ética Profesional 2 (Principio Human-in-the-Loop)</div>
                    </div>
                </div>
            </div>
        </div>

    </main>

    <footer>
        Fundación Kinal • Escuela Técnica Superior • Pensum TSU 2026 • Convenio Universidad del Istmo (UNIS) • Guatemala, 2026
    </footer>
</div>

<script>
    const cursosData = {relaciones_str};
    let selectedCourseId = "b1_etica_general_1";
    let currentViewMode = "grid";

    function switchViewMode(mode) {{
        currentViewMode = mode;
        const btnGrid = document.getElementById('btnModeGrid');
        const btnNet = document.getElementById('btnModeNetwork');
        const gridContainer = document.getElementById('gridContainer');
        const netContainer = document.getElementById('networkContainer');

        if (mode === 'grid') {{
            btnGrid.classList.add('active');
            btnNet.classList.remove('active');
            gridContainer.style.display = 'block';
            netContainer.style.display = 'none';
        }} else {{
            btnGrid.classList.remove('active');
            btnNet.classList.add('active');
            gridContainer.style.display = 'none';
            netContainer.style.display = 'block';
        }}

        // Re-aplicar selección en el modo activo
        renderActiveRuta(selectedCourseId);
    }}

    function filterMapByLinea(lineaId) {{
        // Filtrar en la rejilla
        const rows = document.querySelectorAll('.grid-linea-row');
        rows.forEach(r => {{
            if (lineaId === 'all' || r.id === 'row-' + lineaId) {{
                r.style.display = 'grid';
            }} else {{
                r.style.display = 'none';
            }}
        }});

        // Filtrar en el grafo SVG
        const svgNodes = document.querySelectorAll('.svg-node-group');
        const svgEdges = document.querySelectorAll('.svg-edge');

        svgNodes.forEach(node => {{
            const nLinea = node.getAttribute('data-linea');
            if (lineaId === 'all' || nLinea === lineaId) {{
                node.style.display = 'block';
            }} else {{
                node.style.display = 'none';
            }}
        }});

        svgEdges.forEach(edge => {{
            if (lineaId === 'all' || edge.classList.contains('edge-linea-' + lineaId)) {{
                edge.style.display = 'block';
            }} else {{
                edge.style.display = 'none';
            }}
        }});
    }}

    function selectCourseNode(courseId) {{
        selectedCourseId = courseId;
        renderActiveRuta(courseId);
        updateSidePanel(courseId);
    }}

    function highlightNodeRuta(courseId) {{
        renderActiveRuta(courseId);
    }}

    function clearHighlightNode() {{
        renderActiveRuta(selectedCourseId);
    }}

    function renderActiveRuta(courseId) {{
        const course = cursosData[courseId];
        if (!course) return;

        const activeIds = [courseId, ...course.prerequisitos, ...course.habilita];

        // 1. Manejo en Vista Rejilla
        const allGridNodes = document.querySelectorAll('.node-card');
        allGridNodes.forEach(node => {{
            node.classList.remove('selected', 'prereq-active', 'habilita-active', 'dimmed');
            const nId = node.getAttribute('data-id');
            if (nId === courseId) {{
                node.classList.add('selected');
            }} else if (course.prerequisitos.includes(nId)) {{
                node.classList.add('prereq-active');
            }} else if (course.habilita.includes(nId)) {{
                node.classList.add('habilita-active');
            }} else {{
                node.classList.add('dimmed');
            }}
        }});

        // 2. Manejo en Vista Grafo SVG
        const allSvgNodes = document.querySelectorAll('.svg-node-group');
        allSvgNodes.forEach(node => {{
            node.classList.remove('selected', 'prereq-active', 'habilita-active', 'dimmed');
            const nId = node.getAttribute('data-id');
            if (nId === courseId) {{
                node.classList.add('selected');
            }} else if (course.prerequisitos.includes(nId)) {{
                node.classList.add('prereq-active');
            }} else if (course.habilita.includes(nId)) {{
                node.classList.add('habilita-active');
            }} else {{
                node.classList.add('dimmed');
            }}
        }});

        // Manejo de aristas SVG
        const allSvgEdges = document.querySelectorAll('.svg-edge');
        allSvgEdges.forEach(edge => {{
            edge.classList.remove('edge-prereq-active', 'edge-habilita-active', 'dimmed');
            const src = edge.getAttribute('data-source');
            const tgt = edge.getAttribute('data-target');

            if (tgt === courseId && course.prerequisitos.includes(src)) {{
                edge.classList.add('edge-prereq-active');
            }} else if (src === courseId && course.habilita.includes(tgt)) {{
                edge.classList.add('edge-habilita-active');
            }} else {{
                edge.classList.add('dimmed');
            }}
        }});
    }}

    function updateSidePanel(courseId) {{
        const course = cursosData[courseId];
        if (!course) return;

        document.getElementById('sideBadge').innerText = course.codigo + ' • ' + course.bimestre;
        document.getElementById('sideTitle').innerHTML = course.icono + ' ' + course.nombre;
        document.getElementById('sideSub').innerText = course.subtitulo;
        document.getElementById('sideObjetivo').innerText = course.objetivo;
        document.getElementById('sideIA').innerText = course.subtema_ia;

        // Prerrequisitos list
        const prereqList = document.getElementById('sidePrereqList');
        prereqList.innerHTML = '';
        if (course.prerequisitos.length > 0) {{
            course.prerequisitos.forEach(pId => {{
                const pInfo = cursosData[pId];
                const li = document.createElement('li');
                li.innerText = '⬅️ ' + pInfo.codigo + ' • ' + pInfo.nombre;
                li.onclick = () => selectCourseNode(pId);
                prereqList.appendChild(li);
            }});
        }} else {{
            const li = document.createElement('li');
            li.style.background = '#f1f5f9';
            li.style.color = '#64748b';
            li.style.borderColor = '#cbd5e1';
            li.innerText = 'Ingreso al 3er Año TSU (Sin prerrequisito previo de 3er año)';
            prereqList.appendChild(li);
        }}

        // Habilita list
        const habilitaList = document.getElementById('sideHabilitaList');
        habilitaList.innerHTML = '';
        if (course.habilita.length > 0) {{
            course.habilita.forEach(hId => {{
                const hInfo = cursosData[hId];
                const li = document.createElement('li');
                li.innerText = '➡️ ' + hInfo.codigo + ' • ' + hInfo.nombre;
                li.onclick = () => selectCourseNode(hId);
                habilitaList.appendChild(li);
            }});
        }} else {{
            const li = document.createElement('li');
            li.style.background = '#fef3c7';
            li.style.color = '#92400e';
            li.style.borderColor = '#fde68a';
            li.innerText = 'Culminación del Plan / Graduación TSU';
            habilitaList.appendChild(li);
        }}

        // Links
        document.getElementById('sideLinkDictamen').href = course.dictamen_link;
        document.getElementById('sideLinkTemario').href = 'temarios_por_linea.html#' + course.id;
    }}

    document.addEventListener('DOMContentLoaded', () => {{
        selectCourseNode('b1_etica_general_1');
    }});
</script>

</body>
</html>
"""
    return html

# -------------------------------------------------------------
# EJECUCIÓN Y GENERACIÓN
# -------------------------------------------------------------
temarios_html = generate_temarios_por_linea_html()
temarios_path = os.path.join(base_dir, "temarios_por_linea.html")
with open(temarios_path, "w", encoding="utf-8") as f:
    f.write(temarios_html)
print(f"✓ Generado exitosamente: {temarios_path}")

mybrain_temarios_path = os.path.join(mybrain_dir, "temarios_por_linea.html")
try:
    with open(mybrain_temarios_path, "w", encoding="utf-8") as f:
        f.write(temarios_html)
    print(f"✓ Mirror MyBrain temarios: {mybrain_temarios_path}")
except Exception as e:
    print(f"Nota MyBrain mirror: {e}")

mapa_html = generate_mapa_curricular_html()
mapa_path = os.path.join(base_dir, "mapa_curricular.html")
with open(mapa_path, "w", encoding="utf-8") as f:
    f.write(mapa_html)
print(f"✓ Generado exitosamente: {mapa_path}")

mybrain_mapa_path = os.path.join(mybrain_dir, "mapa_curricular.html")
try:
    with open(mybrain_mapa_path, "w", encoding="utf-8") as f:
        f.write(mapa_html)
    print(f"✓ Mirror MyBrain mapa: {mybrain_mapa_path}")
except Exception as e:
    print(f"Nota MyBrain mirror: {e}")

# Actualizar index.html nav
index_path = os.path.join(base_dir, "index.html")
if os.path.exists(index_path):
    with open(index_path, "r", encoding="utf-8") as f:
        index_content = f.read()
    
    old_nav = """    <nav class="nav-bar">
        <a href="index.html" class="active">Portal General (20 Cursos)</a>
        <a href="nueva_distribucion_tematica_tsu.html" style="color: #fef08a; font-weight: 700;">🌟 Nueva Distribución Temática 2026 (7 Especialidades + IA)</a>
        <a href="#bimestre-1">Bimestre 1</a>
        <a href="#bimestre-2">Bimestre 2</a>
        <a href="#bimestre-3">Bimestre 3</a>
        <a href="#bimestre-4">Bimestre 4</a>
    </nav>"""
    
    new_nav = """    <nav class="nav-bar">
        <a href="index.html" class="active">Portal General (20 Cursos)</a>
        <a href="mapa_curricular.html" style="color: #67e8f9; font-weight: 700;">🗺️ Mapa y Red Curricular</a>
        <a href="temarios_por_linea.html" style="color: #a7f3d0; font-weight: 700;">📚 Temarios por Línea de Estudio</a>
        <a href="nueva_distribucion_tematica_tsu.html" style="color: #fef08a; font-weight: 700;">🌟 Nueva Distribución 2026</a>
        <a href="#bimestre-1">B1</a>
        <a href="#bimestre-2">B2</a>
        <a href="#bimestre-3">B3</a>
        <a href="#bimestre-4">B4</a>
    </nav>"""
    
    if old_nav in index_content:
        index_content = index_content.replace(old_nav, new_nav)
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(index_content)
        print("✓ Actualizado navbar de TSU/index.html")

print("Generación completada exitosamente.")
