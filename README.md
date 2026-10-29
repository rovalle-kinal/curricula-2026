# Ecosistema de Diseño Instruccional y Curricular Técnico-Profesional
## Metodología Dual, Marco DQR y Modelo Institucional de Fundación Kinal
### Proyecto de Automatización y Generación Multiformato para Google Antigravity

---

Este repositorio contiene la arquitectura completa para el **diseño curricular, didáctico e instruccional de cursos y programas técnicos profesionales**, desarrollado bajo los estándares del **Marco Alemán de Cualificaciones (DQR Nivel 2 a 7)**, el **Sistema Dual de Formación en Alternancia** y los lineamientos ético-pedagógicos de **Fundación Kinal**.

El sistema permite generar de forma automatizada y coherente el paquete documental completo de cualquier curso técnico:
1. **Propuesta Formativa y Temario Técnico-Comercial (Brochure / Promesa de Venta en Markdown).**
2. **Plan de Clase y Dosificación Macrocurricular (Macroplanificación por sesiones en Markdown).**
3. **Secuencia Didáctica y Microplanificación Minuto a Minuto (Tres momentos didácticos + Proyecto Capstone + Rúbrica Analítica).**
4. **Página Web Maquetada y Responsiva (HTML oficial con la identidad visual corporativa de Kinal).**
5. **Documento PDF de Alta Definición para Impresión y Entrega (Generado con ReportLab, membrete institucional dinámico y numeración formal).**

---

## 1. Estructura del Repositorio

`	ext
├── .agents/
│   └── skills/
│       └── curriculum-didactic-designer/           # SKILL PORTABLE PARA ANTIGRAVITY
│           ├── SKILL.md                            # Manifiesto y reglas operativas de la Skill
│           ├── references/
│           │   └── curricular_map_and_sources.md   # Base inmutable de conocimiento y citas
│           └── resources/
│               └── document_templates.html         # Plantillas visuales HTML y tablas maestras
│
├── Cursos/                                         # CARPETA CENTRAL DE TODOS LOS CURSOS
│   ├── Automatizacion/                             # Paquete formativo Automatización Industrial
│   ├── Cableado_Estructurado/                      # Paquete formativo Cableado Estructurado
│   ├── Capacitacion_Instructores_IA/               # Formación de formadores en IA
│   ├── Ciberseguridad/                             # Paquete formativo Ciberseguridad
│   ├── Historico_Dual_DQR6/                        # Resguardo histórico versión Dual DQR6
│   ├── Inteligencia_Artificial/                    # Paquete formativo Inteligencia Artificial
│   ├── IoT_Domotica/                               # Paquete formativo IoT y Domótica
│   ├── Levantamiento_Planos_Diagramas/             # Diagramas Industriales P&ID y Planos
│   ├── Mecatronica/                                # Paquete formativo Mecatrónica Industrial
│   ├── Productividad_Universitaria/                # Productividad y metodologías de estudio
│   ├── Talento_Tecnico/                            # Gestión del Talento Técnico y Mandos Medios
│   ├── Taller_NotebookLM/                          # Taller práctico de NotebookLM
│   └── Webinar_Copiloto_IA/                        # Webinar Copiloto de Negocios con IA
│
├── Revisiones_Curriculares/                        # AUDITORÍAS Y MALLAS CURRICULARES KINAL
│   ├── CET/                                        # Pensum Centro Educativo Técnico (Electrónica/Informática)
│   ├── TSU/                                        # Pensum y auditorías Técnico Superior Universitario
│   ├── Carreras_Tecnicas/                          # Temarios y mallas de Carreras Técnicas (Mecánica, Auto, etc.)
│   └── PDFs/                                       # Compilaciones oficiales y auditorías en PDF
│
├── docs/                                           # MEMORIAS Y REGISTROS HISTÓRICOS
│   └── MEMORIA_CONVERSACION_DISENO_INSTRUCCIONAL.md
│
├── scripts/                                        # MOTORES ACTIVOS DE GENERACIÓN Y PDF
│   ├── generate_pdf_diagramas_industriales.py       # Compilador PDF ReportLab para P&ID
│   ├── generate_dual_course_pdfs.py                 # Compilador PDF para cursos 25h y 40h
│   ├── generate_career_audit_pdfs.py                # Compilador de auditorías curriculares
│   ├── generate_single_course_pdfs.py               # Compilador de fichas de cursos
│   ├── build_talento_tecnico_page.py                # Generador de página web Talento Técnico
│   └── vendor/                                      # Dependencias portables (ReportLab, Pillow)
│
├── AGENTS.md                                        # Reglas mandatorias del workspace
└── README.md                                        # Guía de importación y uso
`

---

## 2. Guía de Importación en Otra Instancia de Antigravity

Para replicar y diseñar cursos con este mismo estándar de calidad en cualquier otra máquina o instancia de **Google Antigravity**:

### Paso 1: Clonar o Copiar este Repositorio
```bash
git clone https://github.com/rovalle-kinal/instructional_design.git
cd instructional_design
```
*(O copia las carpetas `.agents/skills/curriculum-didactic-designer/` y `AGENTS.md` dentro de la raíz de cualquier proyecto nuevo de Antigravity).*

### Paso 2: Detección Automática de la Skill
Antigravity detecta automáticamente las habilidades ubicadas en `.agents/skills/`. Puedes verificar que la skill esté activa ejecutando:
* En el chat de Antigravity: `¿Qué skills tienes disponibles para diseño instruccional?`
* El agente responderá identificando **`curriculum-didactic-designer`**.

### Paso 3: Motor de Generación de PDFs (ReportLab)
El repositorio incluye las dependencias necesarias en `scripts/vendor/`, por lo que **no se requiere instalar paquetes en el sistema global**. Si deseas ejecutar los scripts de PDF:
```bash
python3 scripts/generate_pdf_diagramas_industriales.py
```

### Paso 4: Prompt Templates para Diseñar un Curso Nuevo
Copia y pega cualquiera de estos prompts en el chat de Antigravity para iniciar el diseño de un nuevo curso:

#### Prompt 1: Curso Abierto / Especialización Técnica
```text
Activa la skill curriculum-didactic-designer. Con base en el ideario de Fundación Kinal y el marco DQR, 
ayúdame a diseñar el paquete formativo completo para un curso presencial de [NOMBRE DEL CURSO] de [X HORAS] 
(distribuido en [Y SESIONES]). Genera: 
1) Propuesta y Temario Técnico en Markdown, 
2) Plan de Clase / Macroplanificación, 
3) Secuencia Didáctica en 3 momentos (Apertura, Desarrollo y Cierre), 
4) Documento HTML maquetado con identidad Kinal, y 
5) Script de compilación en PDF.
```

#### Prompt 2: Capacitación Corporativa In-Company a Medida
```text
Activa la skill curriculum-didactic-designer. Tenemos una solicitud de capacitación cerrada para una empresa con los siguientes parámetros:
- Población: [6 a 10 colaboradores / Perfiles: Mecánicos, Electricistas, etc.]
- Modalidad: [Híbrida: X horas virtuales Teams + Y horas presenciales de taller/planta]
- Horario de la empresa: [Días y horas de jornada laboral]
- Objetivo y temas solicitados: [Detallar los sistemas o tecnologías]
Genera la propuesta técnica corporativa, el plan de clase híbrido, la secuencia didáctica detallada, la página HTML y el PDF oficial con el escudo de Kinal.
```

---

## 3. Normativa y Reglas Mandatorias de Negocio (Kinal y DQR)

1. **Cero Alucinación / Grounding Estricto:** Toda propuesta se fundamenta en las fuentes oficiales del proyecto y normativas internacionales (ANSI/ISA, ISO, ASME, DIN, DQR).
2. **Citas Textuales Obligatorias:**
   * **Misión de Kinal:** *«Formar a jóvenes y adultos a través de una educación integral, con énfasis en las áreas técnicas y tecnológicas, influyendo positivamente en su trabajo, su familia y la sociedad»*.
   * **Valores Nucleares de Kinal:** *«Visión cristiana de la vida. Respeto a la dignidad de la persona. Espíritu de servicio. Trabajo bien hecho. Libertad personal responsable»*.
   * **Concepto de Competencia Profesional (Marco DQR):** *«La competencia es la capacidad y disposición de la persona para integrar conocimientos técnicos, destrezas prácticas y responsabilidad personal y social, actuando con criterio ético y autonomía ante situaciones reales de trabajo»*.
3. **Umbral Aprobatorio:** Nota mínima de **75 puntos sobre 100** para aprobación de cursos, prácticas de taller y exámenes de suficiencia.
4. **Ecosistema Digital:** Clases sincrónicas en **Microsoft Teams / M365** y gestión académica en Moodle (**Kinal.academy**).
5. **Estructura Pedagógica de Sesión:**
   * **Apertura (20 - 35 min):** Activación, caso real de obra/planta, normas de seguridad y alineación con el ideario Kinal.
   * **Desarrollo (120 - 225 min):** Ejecución práctica en taller/campo y laboratorio CAD aplicando el Ciclo de la Acción Completa.
   * **Cierre (30 - 40 min):** Control de calidad de tolerancias, coevaluación entre pares, registro en la Bitácora del Aprendiz (*Berichtsheft*) y feedback formativo.

---

## 4. Memoria de Conversación y Documentación Histórica

Para consultar el registro detallado de cómo evolucionó el programa de levantamiento de planos (de edificación a diagramas industriales P&ID, ajuste de 40h a 25h, eliminación de fotogrametría, inclusión de triangulación y radiaciones, y adaptación para clientes corporativos), revisa:  
👉 **[`docs/MEMORIA_CONVERSACION_DISENO_INSTRUCCIONAL.md`](./docs/MEMORIA_CONVERSACION_DISENO_INSTRUCCIONAL.md)**
