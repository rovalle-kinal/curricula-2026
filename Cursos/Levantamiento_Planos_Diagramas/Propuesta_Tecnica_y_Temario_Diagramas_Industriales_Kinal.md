# PROPUESTA TÉCNICA FORMATIVA Y TEMARIO CORPORATIVO
## Interpretación y Levantamiento de Diagramas P&ID
### Fundamentos Normativos (Simbología Técnica Normada, ISO 10628, ISO 1219), Relevamiento en Campo y Dibujo en AutoCAD 2D
### Modalidad Híbrida (Virtual Sincrónico + Taller Presencial de Campo y Laboratorio CAD) | Fundación Kinal — Escuela Técnica Superior

---

> [!NOTE]
> **Propuesta Técnica Corporativa Dirigida a Empresa / Sector Industrial.**  
> Diseñada para la homologación de competencias de **6 a 10 colaboradores técnicos** (Mecánicos, Electricistas, Técnicos en Instrumentación y Control, y Dibujantes Técnicos).  
> Calendario de Ejecución Propuesto: **Diciembre 2026 o Enero 2027**, dentro de la jornada laboral habitual del cliente.

---

## 1. Ficha Técnica del Programa Corporativo

| Parámetro | Especificación de la Capacitación |
| :--- | :--- |
| **Nombre del Programa** | **Interpretación y Levantamiento de Diagramas P&ID** |
| **Cliente / Destinatario** | Equipo Técnico Multidisciplinario de Planta (Grupo cerrado corporativo) |
| **Cantidad de Participantes** | **6 a 10 colaboradores** (Cupo optimizado para seguimiento personalizado y prácticas de campo) |
| **Perfil de los Colaboradores** | Técnicos mecánicos, electricistas, técnicos en instrumentación y control, y dibujantes técnicos |
| **Carga Horaria Total** | **40 horas pedagógicas** (10 sesiones de 4 horas / 240 minutos cada una) |
| **Modalidad de Impartición** | **Modalidad Híbrida de Alto Rendimiento:**<br>• **20% Virtual Sincrónico (8 Horas / 2 sesiones):** Fundamentación de qué es un P&ID, simbología técnica normada internacional, ISO 10628, ISO 1219 y técnicas de lectura de planos en Microsoft Teams.<br>• **80% Presencial Práctico (32 Horas / 8 sesiones):** Levantamiento in situ en planta/talleres (inspección de campo, croquizado, medición de tuberías y tags) y dibujo en Laboratorio CAD de Kinal. |
| **Horario y Días Sugeridos** | Adaptado a la jornada de la empresa (Lunes a Jueves 07:00 a 16:00 hrs / Viernes 07:00 a 15:00 hrs):<br>• **Opción 1:** Martes y Jueves de 07:30 a 11:30 hrs (o 12:00 a 16:00 hrs) — 5 semanas.<br>• **Opción 2:** 1 jornada semanal intensiva los días Viernes de 07:30 a 11:30 y 12:00 a 15:00 hrs. |
| **Fechas Propuestas de Inicio** | **Opción Diciembre 2026:** Inicio 01 o 08 de Diciembre de 2026.<br>**Opción Enero 2027:** Inicio 12 o 19 de Enero de 2027. |
| **Sede y Entornos** | Laboratorios CAD de Alta Gama de Fundación Kinal, Aulas Virtuales Microsoft Teams e Instalaciones de Planta del Cliente |
| **Ecosistema Digital** | **Microsoft Teams / M365** para sesiones remotas y **Moodle (Kinal.academy)** para bibliotecas DWG y normativas |
| **Umbral Aprobatorio** | **75 puntos sobre 100** (Evaluación práctica por suficiencia de competencias técnicas) |
| **Acreditación Oficial** | Diploma de Especialización Técnica Profesional emitido por **Fundación Kinal** |

---

## 2. ¿Qué es un Diagrama P&ID (*Piping and Instrumentation Diagram*)?

Un **P&ID** (Diagrama de Tuberías e Instrumentación, por sus siglas en inglés) es el documento gráfico maestro de ingeniería que describe de forma esquemática la interconexión funcional de un proceso industrial. No es un plano arquitectónico ni un dibujo a escala geográfica; es el **mapa esquemático de funcionamiento y control de una planta**.

`	ext
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                        ARQUITECTURA Y ALCANCE DE UN DIAGRAMA P&ID                      │
└────────────────────────────────────────────────────────────────────────────────────────┘
                                            │
     ┌──────────────────────┬───────────────┴───────────────┬──────────────────────┐
     ▼                      ▼                               ▼                      ▼
┌──────────────────┐  ┌──────────────────┐    ┌──────────────────┐  ┌──────────────────┐
│ 1. EQUIPOS DE    │  │ 2. RED DE        │    │ 3. ELEMENTOS DE  │  │ 4. LAZOS DE      │
│    PROCESO       │  │    TUBERÍAS      │    │    CONTROL/VÁLV. │  │    INSTRUMENTOS  │
├──────────────────┤  ├──────────────────┤    ├──────────────────┤  ├──────────────────┤
│ • Tanques /      │  │ • Diámetro (NPS) │    │ • Válvulas man.  │  │ • Sensores y tags│
│   Recipientes    │  │ • Cédula / Sch.  │    │   (globo, comp.) │  │   (PI, TT, LT)   │
│ • Bombas / HPUs  │  │ • Código servicio│    │ • Válvulas auto. │  │ • Líneas señal:  │
│ • Compresores    │  │ • Sentido flujo  │    │   (solenoide, CV)│  │   eléc., neum.,  │
│ • Intercambiad.  │  │ • Aislamiento    │    │ • Válvulas PSV   │  │   bus de datos   │
└──────────────────┘  └──────────────────┘    └──────────────────┘  └──────────────────┘
`

En un P&ID se integran cuatro componentes esenciales:
1. **Equipos de proceso:** Representación esquemática normalizada de recipientes, tanques, intercambiadores de calor, bombas centrífugas, bombas de desplazamiento positivo y compresores.
2. **Red de tuberías y líneas de servicio:** Líneas de proceso y servicios auxiliares (agua, vapor, aire comprimido, fluidos hidráulicos) con su código de tubería (*Line Numbering*), diámetro nominal, cédula, sentido de flujo y accesorios.
3. **Válvulas y elementos de maniobra:** Simbología precisa de válvulas manuales (compuerta, globo, bola, mariposa, retención/check) y válvulas automáticas con actuadores neumáticos, eléctricos o solenoides, indicando su posición de falla segura (*Fail Open / Fail Close*).
4. **Instrumentación y lazos de control:** Símbolos y globos normalizados de identificación que identifican la variable medida (Presión, Temperatura, Nivel, Flujo) y la función del instrumento (Transmisor, Indicador, Controlador, Switch, Válvula), interconectados mediante líneas de señal normalizadas.

---

## 3. Marco Filosófico e Ideario Institucional de Fundación Kinal

La capacitación técnica en Fundación Kinal vincula las habilidades operativas con una cultura de integridad, servicio y excelencia profesional:

> [!IMPORTANT]
> **Misión Institucional de Fundación Kinal:**  
> *«Formar a jóvenes y adultos a través de una educación integral, con énfasis en las áreas técnicas y tecnológicas, influyendo positivamente en su trabajo, su familia y la sociedad»*.

> [!IMPORTANT]
> **Valores Nucleares de Fundación Kinal:**  
> *«Visión cristiana de la vida. Respeto a la dignidad de la persona. Espíritu de servicio. Trabajo bien hecho. Libertad personal responsable»*.

### 3.1 El Principio del «Trabajo Bien Hecho» en la Interpretación y Dibujo de Planos
En el entorno industrial, un plano no es un esquema decorativo; es el documento técnico y legal sobre el cual se ejecutan maniobras operativas, mantenimientos y bloqueos de seguridad. Un error en la interpretación de un plano o un dibujo impreciso puede provocar maniobras indebidas, sobrepresiones, derrames o accidentes en procedimientos de consignación LOTO (*Lockout/Tagout*).

En este programa, el principio del **trabajo bien hecho** se materializa en cuatro pilares:
* **Fidelidad y Verdad Técnica (*As-Built* Real):** Compromiso ético de reflejar en el dibujo exactamente lo que existe en campo. Cero tolerancia a adivinar trayectorias, omitir válvulas de purga o suponer la ubicación de instrumentos.
* **Prolijidad Gráfica y Estandarización CAD:** Dibujo limpio y estructurado, empleo riguroso de capas normalizadas por servicio, bloques con atributos homogéneos, textos nítidos y cumplimiento estricto de las normas gráficas internacionales (**simbología técnica normada e ingeniería gráfica (ISO 10628, ISO 1219)**).
* **Cultura de Seguridad y Protección de Vidas:** El dibujante y el técnico comprenden que un diagrama claro protege la vida de los operadores y personal de mantenimiento, permitiendo intervenciones seguras y confiables.
* **Espíritu de Servicio y Comunicación Multidisciplinaria:** El plano técnico es un puente de colaboración. Un diagrama bien dibujado facilita el trabajo del mecánico, del instrumentista, del electricista y de los supervisores, promoviendo el trabajo en equipo y la eficiencia de planta.

---

## 4. Justificación y Necesidad Operativa

El personal técnico de planta a menudo se enfrenta a:
1. **Planos Desactualizados:** Modificaciones de tuberías, reubicación de válvulas o sustitución de instrumentos que se ejecutaron en campo pero nunca se documentaron en los archivos CAD de ingeniería.
2. **Brecha en la Lectura Técnica:** Mecánicos y electricistas que operan los equipos pero tienen dificultades para interpretar la simbología de instrumentos normada, los lazos de control o los códigos de línea.
3. **Falta de Métodos de Levantamiento:** Ausencia de una técnica metódica para realizar recorridos de campo (*walkdowns*), tomar medidas dimensionales precisas y elaborar croquis estructurados que el dibujante pueda plasmar sin ambigüedades.
4. **Dibujos CAD sin Estandarización:** Planos elaborados en una sola capa, sin bloques inteligentes, con símbolos no normalizados y sin tablas de equipos asociadas.

**Solución Kinal:** Unificar al equipo técnico en un entrenamiento centrado en la **lectura analítica, el levantamiento en sitio y la diagramación profesional en AutoCAD 2D**, convirtiendo a los técnicos en intérpretes expertos y al equipo de diseño en garantes del dibujo estandarizado.

---

## 5. Objetivo General del Programa

> [!IMPORTANT]
> **Objetivo de Aprendizaje:**  
> Desarrollar competencias teórico-prácticas en el equipo multidisciplinario (mecánicos, electricistas, instrumentistas y dibujantes) para **interpretar con fluidez, relevar en campo y dibujar en AutoCAD 2D diagramas de tuberías e instrumentación (P&ID) y esquemas funcionales de fluidos**, aplicando normas internacionales de representación gráfica (normas y estándares gráficos internacionales (ISO 10628, ISO 1219 y simbología técnica normada)), con librerías de bloques inteligentes, capas normalizadas y tablas de equipos, bajo el sello del *«trabajo bien hecho»* de Fundación Kinal.

---

## 6. Perfil de Ingreso y Egreso

### Perfil de Ingreso
* Colaboradores técnicos de planta en áreas de mantenimiento mecánico, eléctrico, instrumentación/control y dibujantes o proyectistas CAD.
* Experiencia práctica en plantas industriales, cuartos de máquinas, talleres o salas de control.
* Interés en la estandarización gráfica, la lectura de planos y la seguridad operacional.

### Perfil de Egreso
Al egresar, el participante:
1. **Interpreta y decodifica** diagramas P&ID industriales identificando tags y códigos estandarizados de instrumentos, tipos de líneas de señal, válvulas, equipos y sentidos de flujo.
2. **Ejecuta levantamientos de campo (*walkdowns*)** aplicando técnicas de croquizado a mano alzada y en tablet, midiendo diámetros de tubería (NPS/Schedule) y registrando accesorios in situ.
3. **Aplica simbología normalizada** según simbología técnica normada e ingeniería gráfica (ISO 10628, ISO 1219) para sistemas de proceso (agua, vapor, aire comprimido y fluidos hidráulicos).
4. **Dibuja planos P&ID en AutoCAD 2D** estructurados en capas normalizadas, con librerías de bloques dinámicos y atributos editables.
5. **Genera tablas automáticas de equipos e instrumentos** (*Equipment & Valve Schedules*) y maqueta planos ejecutivos listos para impresión y entrega oficial en PDF.

---

## 7. Temario Curricular Estructurado (40 Horas)

### Módulo 1: Fundamentos de P&ID, Simbología Técnica Normada y Lectura de Diagramas (8 Horas — Virtual Sincrónico / Teams)
* **Tema 1.1: El Diagrama P&ID en la Ingeniería de Plantas:**
  * Concepto, propósito y jerarquía: Diferencias entre Diagrama de Bloques (BFD), Diagrama de Flujo de Proceso (PFD) y Diagrama de Tuberías e Instrumentación (P&ID).
  * Anatomía de un plano P&ID: área de dibujo, cajetín, notas generales, referencias cruzadas (*off-page connectors*) y leyendas de simbología.
  * Código de identificación de tuberías (*Line Numbering*): Diámetro nominal - Servicio de fluido - Número de línea - Especificación de material - Aislamiento térmico.
  * Código de colores y rotulación según **ASME A13.1**.
* **Tema 1.2: Norma simbología técnica normada — Identificación e Instrumentación:**
  * Globos o círculos de instrumentos: instrumentos de campo, montados en panel principal, panel auxiliar y sistemas DCS/PLC.
  * Letras de identificación estandarizadas: primera letra (Variable de proceso: P, T, F, L, V) y letras sucesivas (Función: I, C, T, V, S, A).
  * Líneas de señal de control: señal eléctrica (discontinua), señal neumática (línea con dobles marcas), enlace digital/software, capilar e hidráulica.
  * Modos de falla de válvulas automáticas: Falla Abierta (FO), Falla Cerrada (FC), Falla Bloqueada (FL).
  * Taller práctico virtual: Decodificación y lectura de 20 lazos de control cerrados en planos industriales de muestra.

---

### Módulo 2: Simbología de Válvulas, Accesorios y Equipos en Planos P&ID (8 Horas — Virtual Sincrónico / Teams)
* **Tema 2.1: Simbología Normalizada de Válvulas y Actuadores (ISO 10628 y simbología técnica normada):**
  * Válvulas de seccionamiento y regulación: compuerta, globo, bola, mariposa, aguja y diafragma.
  * Válvulas de retención (*check*): oscilante, de disco y de doble clapeta.
  * Válvulas de alivio y seguridad: PSV (seguridad por sobrepresión) y PRV (reductora de presión).
  * Tipos de actuadores gráficos: manual (palanca/volante), diafragma neumático, cilindro, motor eléctrico y solenoide.
* **Tema 2.2: Representación Gráfica de Equipos y Accesorios de Tubería:**
  * Equipos dinámicos: bombas centrífugas (horizontales, verticales), bombas de desplazamiento positivo (engranajes, tornillo), compresores y ventiladores.
  * Equipos estáticos: recipientes a presión, tanques atmosféricos, torres, intercambiadores de calor (tubo y coraza, placas).
  * Accesorios de línea: filtros en Y, filtros canasta tipo dúplex, trampas de vapor, juntas de expansión y carreteles de desmontaje.
  * Ejercicios de rastreo de líneas de proceso (*Line Tracing*) desde suministro hasta destino e identificación de puntos de muestreo y venteos.

---

### Módulo 3: Levantamiento de Campo (*Walkdown*), Metrología y Croquizado Técnico (8 Horas — Presencial: Planta / Taller Kinal)
* **Tema 3.1: Metodología del Levantamiento de Campo (*Field Walkdown*):**
  * Planificación de la ruta de relevamiento: identificación de límites de batería, puntos de ingreso y distribución.
  * Seguridad durante el levantamiento: protocolos EPP, áreas clasificadas y precauciones en líneas calientes o presurizadas.
  * Metrología dimensional aplicada a tuberías: medición de diámetro exterior (OD) con calibrador vernier y cinta perimétrica; determinación del diámetro nominal (NPS / DN) y cédula (*Schedule 40/80*) mediante tablas normalizadas.
  * Identificación física de accesorios: tipo de bridas estandarizadas (Clase 150/300, cara levantada RF / cara plana FF), conexiones roscadas NPT y uniones soldadas.
* **Tema 3.2: Técnicas de Croquizado a Mano Alzada y en Tablet:**
  * Principios de croquizado rápido esquemático: proporción visual, alineación ortogonal y uso de cuadrícula.
  * Registro de información en sitio: asignación de tags, diámetros, sentidos de flujo y elevaciones relativas.
  * Práctica de campo: levantamiento físico guiado de un sistema de proceso en planta/taller (estación de bombeo, filtración o distribución).
  * Elaboración del croquis borrador consolidado y validación de datos entre los integrantes de la brigada.

---

### Módulo 4: Dibujo y Digitalización de Diagramas P&ID en AutoCAD 2D (8 Horas — Presencial: Laboratorio CAD)
* **Tema 4.1: Entorno de Trabajo y Estructuración de Capas Normalizadas:**
  * Configuración de la plantilla de dibujo P&ID Kinal (.DWT): unidades, límites y estilos de texto normalizados.
  * Sistema de capas (*Layers*) por fluido y disciplina: L-PROCESO, L-SERVICIOS, E-EQUIPOS, E-VALVULAS, I-INSTRUMENTOS, I-SENALES, TEXTOS, COTAS.
  * Herramientas de dibujo de precisión esquemática: OSNAP (cuadrante, centro, intersección, perpendicular) y rastreo polar (Polar Tracking).
  * Inserción del croquis de campo como referencia de calco y trazado vectorial de líneas principales y secundarias.
* **Tema 4.2: Creación de Bloques Inteligentes con Atributos:**
  * Creación y gestión de bloques para P&ID: símbolos de bombas, intercambiadores, tanques y válvulas.
  * Inserción de atributos editables (ATTDEF y BATTMAN) para tags y códigos estandarizados de instrumentos (TAG-LOOP, TAG-NUM, RANGO).
  * Cruce de tuberías: técnicas de trazado con puente/arco (*jumper*) vs. cruce limpio sin conexión; derivaciones en T con punto de conexión.
  * Digitalización completa del croquis de campo levantado en el Módulo 3.

---

### Módulo 5: Esquemas ISO 1219, Extracción de Datos, Maquetación y Capstone (8 Horas — Presencial: Laboratorio CAD)
* **Tema 5.1: Esquematización de Circuitos de Potencia Fluida (Norma ISO 1219):**
  * Simbología gráfica neumática e hidráulica: unidades FRL, válvulas direccionales (3/2, 5/2, 4/3), reguladores de caudal unidireccional y cilindros.
  * Diferencias de representación entre un diagrama P&ID de proceso y un esquema funcional de potencia fluida ISO 1219.
  * Trazado en AutoCAD de circuitos neumáticos e hidráulicos básicos integrados al sistema de planta.
* **Tema 5.2: Extracción de Datos, Maquetación y Sustentación Capstone:**
  * Uso de comandos de extracción de datos (EATTEXT): generación automática en el plano de listas de instrumentos (*Instrument Schedule*) y tablas de válvulas (*Valve List*).
  * Maquetación en espacio papel (*Layouts*): ajuste de láminas (A3 / Doble Carta), ventana gráfica (*Viewport*), cajetín institucional con atributos y asignación de plumillas monocromáticas .CTB.
  * **Sustentación del Proyecto Capstone:** Presentación grupal del juego de planos P&ID definitivo levantado en planta, con su lista de equipos y especificaciones, defendido ante el panel evaluador de Kinal.

---

## 8. Esquema de Evaluación y Acreditación Institucional

El modelo de evaluación de **Fundación Kinal** se basa en la demostración práctica de competencias en condiciones reales:

* **Nota Mínima Aprobatoria:** **75 puntos sobre 100** en todas las evidencias y proyectos.

| Componente Evaluativo | Ponderación | Modalidad | Criterios e Instrumentos de Medición |
| :--- | :---: | :---: | :--- |
| **Evaluación Teórico-Normativa**<br>(Simbología Normada, ISO 10628, ISO 1219) | **15%** | Virtual (Teams) | Cuestionario técnico de decodificación de tags estandarizados de instrumentación, simbología de válvulas y lectura de lazos. |
| **Práctica de Levantamiento en Campo**<br>(Walkdown y Croquizado) | **25%** | Presencial (Planta) | Croquis técnico proporcional, identificación rigurosa de diámetros, accesorios y tags in situ. |
| **Laboratorios de Dibujo CAD I y II**<br>(Trazado P&ID y Bloques con Atributos) | **25%** | Presencial (CAD) | Precisión en trazado vectorial, uso correcto de capas, inserción de bloques estandarizados de instrumentación y rotulado de tags. |
| **Esquemas de Potencia Fluida ISO 1219**<br>(Circuitos Neumáticos/Hidráulicos) | **15%** | Presencial (CAD) | Modelado de circuitos funcionales de potencia fluida bajo norma ISO 1219 en AutoCAD. |
| **Proyecto Capstone Final Integrador**<br>(Plano P&ID Maquetado y Tabla de Equipos) | **20%** | Presencial (Panel) | Juego de planos P&ID terminado con cajetín, tablas de equipos (EATTEXT), PDF exportado y defensa grupal. |
| **Total** | **100%** | **Híbrido** | **Umbral Institucional de Aprobación: &ge; 75 Puntos** |
