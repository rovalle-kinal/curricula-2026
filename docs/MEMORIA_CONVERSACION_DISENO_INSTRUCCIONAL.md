# MEMORIA TÉCNICA Y DE CONVERSACIÓN: DISEÑO INSTRUCCIONAL DE CURSOS TÉCNICOS
## Registro Histórico, Metodología Pedagógica y Evolución Curricular
### Fundación Kinal — Escuela Técnica Superior | Proyecto: Antigravity Instructional Design

---

## 1. Resumen Ejecutivo de la Conversación

Esta memoria técnica documenta el proceso completo de diseño curricular, adaptación metodológica, producción multiformato y personalización corporativa realizado en el proyecto de **Diseño Instruccional** dentro de Google Antigravity.

El objetivo fue concebir la arquitectura pedagógica y documental para el programa de formación técnica:
* **Fase 1 (Formación Abierta / Edificación):** *«Levantamiento de Planos y Diagramas para Proyectos»* (versión 40h extendida y versión 25h intensiva sabatina para noviembre 2026).
* **Fase 2 (Formación Corporativa a Medida):** *«Levantamiento e Interpretación de Diagramas y P&ID para Sistemas Industriales»* (versión 40h híbrida para cliente industrial, abordando agua de proceso/potable, búnker/diésel, aire comprimido y oleohidráulica).

---

## 2. Línea de Tiempo y Decisiones de Diseño Curricular

```text
┌────────────────────────────────────────────────────────────────────────────────────────┐
│               EVOLUCIÓN CRONOLÓGICA DE LA ARQUITECTURA DEL PROGRAMA                    │
└────────────────────────────────────────────────────────────────────────────────────────┘
                                            │
    ┌───────────────────────────────────────┴───────────────────────────────────────┐
    ▼                                                                               ▼
┌───────────────────────────────────┐                           ┌───────────────────────────────────┐
│ FASE 1: CURSO DE EDIFICACIÓN / CAD│                           │ FASE 2: ADAPTACIÓN CORPORATIVA    │
├───────────────────────────────────┤                           ├───────────────────────────────────┤
│ • 40h Presencial (Sabatina)       │                           │ • Cliente: 6 a 10 colaboradores   │
│ • Cintas rígidas, largas y láser  │                           │ • Mecánicos, electricistas,       │
│ • Croquis a mano alzada y tablet  │ ════════════════════════> │   instrumentistas y dibujante     │
│ • Erradicación de fotogrametría   │                           │ • Modalidad Híbrida (40h)         │
│ • Inclusión: Radiación y Triang.  │                           │ • 4 Sistemas: Agua, Búnker/Diésel,│
│ • Ajuste a 25h (31 Oct - 28 Nov)  │                           │   Neumática y Oleohidráulica      │
│ • Generación PDF 25h y PDF 40h    │                           │ • P&ID según ISA-5.1 e ISO 1219   │
└───────────────────────────────────┘                           └───────────────────────────────────┘
```

### Hito 1: Creación Inicial del Curso de Levantamiento de Planos
* **Requerimiento Original:** Curso 100% presencial de "Levantamiento de Planos y Diagramas para Proyectos" abordando AutoCAD, croquis en tablet, dibujo a mano alzada, cintas rígidas, cintas blandas y metro láser, bajo el ideario de Kinal.
* **Artefactos Creados:**
  1. Propuesta de Venta y Temario Técnico.
  2. Plan de Clase (Macroplanificación de 10 sesiones / 40 horas).
  3. Secuencia Didáctica (Microplanificación en 3 momentos pedagógicos: Apertura, Desarrollo y Cierre).
  4. Página web maquetada HTML con identidad visual Kinal.

### Hito 2: Refinamiento Técnico de AutoCAD y Erradicación de Fotogrametría
* **Ajuste del Usuario:** Eliminar la fotogrametría por falta de herramientas y ahondar exhaustivamente en AutoCAD 2D:
  * Configuración de unidades métricas (`UNITS` a 3 decimales `0.000 m`).
  * Herramientas de precisión: `OSNAP` completo y `Polar Tracking` (F10).
  * Referencias Externas (`XREFs` / `ATTACH` vs `OVERLAY`, rutas relativas y `XCLIP`).
  * Estilos de cota normalizados (`DIMSTYLE`, `DIMCONTINUE`, `DIMALIGNED`).
  * Bloques para instalaciones con atributos (`BLOCK`, `ATTDEF`, `BATTMAN`, `EATTEXT`).
  * Maquetación en *Paper Space / Layouts* con escalas (1:50, 1:20), cajetín oficial y plumillas `.CTB`.

### Hito 3: Ajuste de Calendario (25 Horas vs. 40 Horas) y Métodos Topográficos
* **Consulta de Fechas:** Finalizar el 28 de noviembre de 2026 iniciando el 31 de octubre (5 sábados exactos).
* **Solución Adoptada:**
  * **Modalidad Activa 2026 (25 Horas):** 5 sábados de 5 horas (08:00 a 13:00 hrs).
  * **Modalidad Proyección 2027 (40 Horas):** 10 sesiones de 4 horas (en 2 días semanales o 10 sábados regulares).
  * **Inclusión metodológica:** Se agregaron formalmente el **Método de Triangulación y Trilateración** (resolución de esquinas y ángulos no rectos mediante diagonales cruzadas y líneas de amarre; comprobación 3-4-5) y el **Método de Radiación de Campo** (medición radial desde estación base con distanciómetro láser hacia columnas y vértices).
  * **Simplificación de AutoCAD:** Enfoque ágil sin teoría excesiva, directo a la práctica del levantamiento.

### Hito 4: Ajustes Conceptuales y Generación de PDFs
* **Solicitud:** Eliminar el bloque de "Formación profesional dual", traducir el concepto de competencia del DQR al español de forma breve y entendible indicando la competencia diseñada, reflejar en la web la opción de 40 horas y generar PDFs independientes.
* **Ejecución:**
  * Traducción y contextualización en español de la competencia DQR.
  * Generación de `programa_formativo_levantamiento_planos_25h.pdf` y `programa_formativo_levantamiento_planos_40h.pdf` utilizando ReportLab con el escudo oficial de Kinal y numeración de dos pasadas (*NumberedCanvas*).

### Hito 5: Nueva Propuesta Corporativa a Medida para Cliente Industrial
* **Solicitud del Cliente:**
  * **Colaboradores:** 6 a 10 personas.
  * **Perfiles:** Mecánicos, electricistas, instrumentistas y dibujante.
  * **Horario empresa:** Lunes a jueves de 07:00 a 16:00 hrs y viernes de 07:00 a 15:00 hrs.
  * **Fechas de inicio:** Diciembre 2026 o Enero 2027.
  * **Modalidad:** Híbrida (Virtual sincrónico + Presencial de taller/campo).
  * **Objetivo:** Levantamiento e interpretación de diagramas para sistemas de agua, combustibles, neumática e hidráulica.
* **Solución Implementada:**
  * Preservación de la versión previa en `Historico_Edificacion_Sabatina_2026/`.
  * Generación de la primera versión del paquete corporativo P&ID híbrido de 40h.

### Hito 6: Reenfoque Pedagógico: Interpretación y Dibujo de Planos P&ID
* **Ajuste y Actualización Solicitada:**
  * **Nombre acortado y sin código:** Se elimina el código alfanumérico y se formaliza el nombre como: **«Interpretación y Levantamiento de Diagramas P&ID»**.
  * **Definición de P&ID:** Se integra una explicación exhaustiva de qué es un P&ID (*Piping and Instrumentation Diagram*) y cómo representa la lógica funcional entre equipos de proceso, red de tuberías (NPS/Schedule), válvulas manuales/automáticas e instrumentación y lazos de control (norma ANSI/ISA-5.1).
  * **Reorientación del Contenido:** Se reduce la teoría química/termodinámica pesada sobre búnker/diésel/viscosidades y se centra el 100% del programa en **lectura analítica, recorrido de campo (*walkdown*), metrología dimensional con calibrador vernier, croquizado a mano alzada/tablet, capas normalizadas en AutoCAD, bloques con atributos editables (`ATTDEF`), esquemas de fluidos ISO 1219, tablas automáticas (`EATTEXT`) y maquetación ejecutiva**.
  * **Actualización del Principio del «Trabajo Bien Hecho»:** Se reformula vinculándolo a la exactitud dimensional, fidelidad del dibujo a la realidad de planta (*as-built* real sin inventar componentes), prolijidad gráfica CAD, prevención de accidentes en consignaciones LOTO y servicio colaborativo multidisciplinario.

---

## 3. Principios Inmutables y Reglas de Negocio Institucionales

Cualquier curso diseñado bajo este marco debe cumplir obligatoriamente:
1. **Misión de Kinal:** Cita textual e inmutable:  
   *«Formar a jóvenes y adultos a través de una educación integral, con énfasis en las áreas técnicas y tecnológicas, influyendo positivamente en su trabajo, su familia y la sociedad»*.
2. **Valores Nucleares de Kinal:** Cita textual e inmutable:  
   *«Visión cristiana de la vida. Respeto a la dignidad de la persona. Espíritu de servicio. Trabajo bien hecho. Libertad personal responsable»*.
3. **El Principio del «Trabajo Bien Hecho»:** Rigor dimensional, verdad métrica (cero tolerancia a planos falsificados o cotas redondeadas), prolijidad gráfica y estricta seguridad industrial (LOTO, EPP, manejo de fluidos peligrosos).
4. **Umbral Aprobatorio:** Calificación mínima de **75 puntos sobre 100** para aprobación de cursos y exámenes de suficiencia.
5. **Ecosistema Digital:** Plataformas corporativas de Microsoft (Teams, M365) y Moodle (**Kinal.academy**). No se utilizan referencias a Google Meet ni Classroom.
6. **Estructura Didáctica por Momentos:** Toda sesión se divide en **Apertura / Inicio** (30-35 min), **Desarrollo / Laboratorio Práctico** (170-225 min) y **Cierre / Consolidación** (40 min).
7. **Ciclo de la Acción Completa:** 6 fases: *Informar &rarr; Planificar &rarr; Decidir &rarr; Ejecutar &rarr; Controlar &rarr; Valorar*.

---

## 4. Mapa de Entregables Generados en el Repositorio

```text
Cursos/Levantamiento_Planos_Diagramas/
├── Historico_Edificacion_Sabatina_2026/           [Resguardo histórico versión edificación]
│   ├── Plan_de_Clase_Levantamiento_Planos_Kinal.md
│   ├── Propuesta_Venta_y_Temario_Levantamiento_Planos_Kinal.md
│   ├── Secuencia_Didactica_Levantamiento_Planos_Kinal.md
│   ├── programa_formativo_levantamiento_planos.html
│   ├── programa_formativo_levantamiento_planos_25h.pdf
│   └── programa_formativo_levantamiento_planos_40h.pdf
│
├── Propuesta_Tecnica_y_Temario_Diagramas_Industriales_Kinal.md   [Propuesta cliente industrial]
├── Plan_de_Clase_Diagramas_Industriales_Kinal.md                 [Macroplanificación híbrida 40h]
├── Secuencia_Didactica_Diagramas_Industriales_Kinal.md           [Microplanificación 10 sesiones]
├── programa_formativo_diagramas_industriales.html                [Maqueta web responsive]
└── programa_formativo_diagramas_industriales.pdf                 [PDF oficial para el cliente]
```

### Actualización Reciente: Presentación Ejecutiva y Neutralidad Normativa
- **Eliminación de Referencias Específicas a ISA / ANSI:** Se reemplazaron términos como ISA-5.1 o bridas ANSI por terminología técnica normalizada e industrial estandarizada (*simbología técnica normada*, *bridas estandarizadas Clase 150/300 RF/FF*).
- **Estructuración del PDF en 3 Páginas:** 
  1. *Página 1:* Presentación integral del curso en una sola hoja, incorporando el Temario Curricular Resumido con textos centrados verticalmente (VALIGN: MIDDLE) y suprimiendo la explicación teórica redundante de P&ID.
  2. *Página 2:* Planificación y dosificación de las 10 sesiones en su propia hoja independiente.
  3. *Página 3:* Sistema de evaluación y rúbrica analítica terminal.
- **Estructura Renovada del README:** Incorporación de descripción ejecutiva en menos de 5 líneas, prompts listos para replicación en cualquier agente o arnés de IA, árbol jerárquico depurado y formalización de reglas mandatorias de Kinal.
