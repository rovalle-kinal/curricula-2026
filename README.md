# Ecosistema de Diseño Curricular e Instruccional Técnico-Profesional
## Sistema Dual de Alternancia, Marco DQR y Modelo Formativo de Fundación Kinal

Repositorio y motor de diseño curricular, instruccional y didáctico para la formación técnica y profesional de Fundación Kinal. Fundamentado en el Marco Alemán de Cualificaciones (DQR) y el Sistema Dual de Formación en Alternancia, automatiza la creación de propuestas técnicas, planes de clase, secuencias didácticas de tres momentos, páginas web maquetadas y documentos PDF oficiales de alta fidelidad compilados con ReportLab.

---

## 1. Prompts de Importación y Operación en Agentes de IA

Para importar y operar este repositorio en cualquier instancia de **Google Antigravity**, **Claude Code**, **ChatGPT**, **Cursor** o cualquier arnés/agente de inteligencia artificial:

### Clonación del Repositorio
```bash
git clone https://github.com/rovalle-kinal/instructional_design.git
cd instructional_design
```

### Prompt 1: Inicialización y Contextualización en Cualquier Agente
Copia y pega este prompt al iniciar sesión en un nuevo entorno o instancia:

```text
Actúa como Diseñador Curricular e Instruccional Técnico-Profesional de Fundación Kinal.
He clonado el repositorio https://github.com/rovalle-kinal/instructional_design.git.
Toma como directrices mandatorias el archivo AGENTS.md y la skill oficial en .agents/skills/curriculum-didactic-designer/SKILL.md.
Asegura estricto apego al Marco Alemán de Cualificaciones (DQR), el Sistema Dual de Alternancia, las citas textuales oficiales de Kinal, la nota mínima aprobatoria de 75/100 puntos y el ecosistema Microsoft Teams / Moodle (Kinal.academy).
Queda estrictamente prohibido utilizar la carpeta output/; cada curso nuevo debe residir en su propia carpeta en Cursos/<Nombre_Curso>/ generando el paquete quíntuple (Propuesta MD, Plan de Clase MD, Secuencia Didáctica MD, Página Web HTML y PDF compilado con ReportLab).
Confirma que has asimilado las directrices y preséntame el catálogo actual de cursos.
```

### Prompt 2: Diseño de un Nuevo Curso Técnico o Capacitación Corporativa
```text
Activa la skill curriculum-didactic-designer. Con base en el ideario de Fundación Kinal y el marco DQR, 
diseña el paquete formativo completo para el curso [NOMBRE DEL CURSO] con una duración de [X HORAS] 
distribuidas en [Y SESIONES] en modalidad [PRESENCIAL / HÍBRIDA (Xh Teams + Yh Práctica en Planta o Taller)].
Población objetivo: [PERFILES: MECÁNICOS, ELECTRICISTAS, DIBUJANTES TÉCNICOS, MANDOS MEDIOS, ETC.].
Requisitos específicos: [ENFOQUE PRÁCTICO, SIMBOLOGÍA NORMADA, METROLOGÍA, BLOQUES CAD, ETC.].

Genera dentro de Cursos/[Nombre_Curso]/:
1. Propuesta Técnica y Temario en Markdown (.md).
2. Plan de Clase y Macroplanificación por sesiones (.md).
3. Secuencia Didáctica de 3 momentos (Apertura, Desarrollo y Cierre) con Rúbrica Analítica Terminal (.md).
4. Página Web Maquetada y Responsiva (.html) con identidad visual Kinal.
5. Script compilador en Python con ReportLab y documento PDF oficial (.pdf).
```

---

## 2. Estructura Organizada del Repositorio

```text
instructional_design/
├── .agents/
│   └── skills/
│       └── curriculum-didactic-designer/        # Skill portable de diseño curricular para Antigravity
│           ├── SKILL.md                         # Reglas operativas, prompts y metodologías pedagógicas
│           ├── references/
│           │   └── curricular_map_and_sources.md# Base inmutable de conocimiento (DQR, Dual, Sajonia, Kinal)
│           └── resources/
│               └── document_templates.html      # Plantillas visuales y maquetación web institucional
│
├── Cursos/                                      # CARPETA CENTRAL DE PAQUETES FORMATIVOS
│   ├── Automatizacion/                          # Automatización Industrial, PLCs y control
│   ├── Cableado_Estructurado/                   # Redes, fibra óptica e infraestructura TI
│   ├── Capacitacion_Instructores_IA/            # Formación de formadores docentes en IA
│   ├── Ciberseguridad/                          # Seguridad perimetral y redes operativas
│   ├── Historico_Dual_DQR6/                     # Histórico curricular versión Dual DQR 6
│   ├── Inteligencia_Artificial/                 # Inteligencia Artificial para productividad técnica
│   ├── IoT_Domotica/                            # Internet de las Cosas e instrumentación conectada
│   ├── Levantamiento_Planos_Diagramas/          # P&ID, simbología normada, relevamiento y AutoCAD 2D
│   ├── Liderazgo_Factor_Humano_Gerentes/        # Liderazgo gerencial, factor humano y mandos medios (TSU)
│   ├── Mecatronica/                             # Sistemas electromecánicos, sensores y accionamientos
│   ├── Productividad_Universitaria/             # Hábitos de estudio, gestión del tiempo y metodologías
│   ├── Talento_Tecnico/                         # Fidelización y desarrollo de mandos medios técnicos
│   ├── Taller_NotebookLM/                       # Taller interactivo de investigación con NotebookLM
│   ├── Web/                                     # Maquetación frontend, HTML5/CSS3 y accesibilidad
│   └── Webinar_Copiloto_IA/                     # Webinar ejecutivo de copilotos de inteligencia artificial
│
├── Revisiones_Curriculares/                     # AUDITORÍAS Y MALLAS CURRICULARES INSTITUCIONALES
│   ├── Carreras_Tecnicas/                       # Automotriz, Construcción, Electricidad, Mecánica, Topografía
│   ├── CET/                                     # Centro Educativo Técnico (Electrónica e Informática)
│   ├── PDFs/                                    # Compilaciones de auditorías y mallas en PDF de alta fidelidad
│   └── TSU/                                     # Pensum y auditorías del Técnico Superior Universitario
│
├── docs/                                        # MEMORIAS Y REGISTROS DE TRAZABILIDAD
│   └── MEMORIA_CONVERSACION_DISENO_INSTRUCCIONAL.md # Bitácora de evolución curricular y decisiones de diseño
│
├── scripts/                                     # MOTORES DE COMPILACIÓN Y AUTOMATIZACIÓN EN PDF
│   ├── generate_pdf_diagramas_industriales.py    # Compilador ReportLab del curso Diagramas P&ID
│   ├── generate_career_audit_pdfs.py            # Generador PDF de auditorías de carreras técnicas
│   ├── generate_dual_course_pdfs.py              # Generador PDF para programas de 25h y 40h
│   ├── generate_single_course_pdfs.py            # Generador PDF de fichas curriculares
│   ├── build_talento_tecnico_page.py             # Generador de página web corporativa
│   └── vendor/                                  # Dependencias embebidas portables (ReportLab, etc.)
│
├── AGENTS.md                                    # Reglas mandatorias del workspace para agentes
└── README.md                                    # Documento maestro de arquitectura y guía de uso
```

---

## 3. Normativa y Reglas Mandatorias de Negocio

Todo diseño generado en este repositorio debe respetar estrictamente las siguientes reglas operativas:

1. **Cero Alucinación / Grounding Estricto:** Toda propuesta técnica se basa exclusivamente en las fuentes oficiales del proyecto y marcos estandarizados (DQR, Sistema Dual, Sajonia y lineamientos Kinal). No extrapolar marcos ajenos.
2. **Citas Textuales Obligatorias e Inmutables:**
   * **Formación Profesional Dual:** *«concepto de aprendizaje para jóvenes que tiene como objetivo preparar a los aprendices para su vida profesional, por lo que la formación se realiza en régimen de alternancia entre la escuela o el centro de formación y la empresa. El aprender en el proceso del trabajo es base y a la vez objetivo de la acción formativa»*.
   * **Competencia según DQR:** *«the ability and readiness of the individual to use knowledge, skills and personal, social and methodological competences and to behave in a considered, individual and socially responsible manner. Competence is understood in this sense as the comprehensive ability to act»*.
   * **Misión de Kinal:** *«Formar a jóvenes y adultos a través de una educación integral, con énfasis en las áreas técnicas y tecnológicas, influyendo positivamente en su trabajo, su familia y la sociedad»*.
   * **Valores Nucleares de Kinal:** *«Visión cristiana de la vida. Respeto a la dignidad de la persona. Espíritu de servicio. Trabajo bien hecho. Libertad personal responsable»*.
3. **Umbral Mínimo Aprobatorio:** Calificación mínima de **75 puntos sobre 100** tanto para evaluaciones de desempeño y proyectos como para exámenes por suficiencia técnica.
4. **Cargas Horarias según Niveles DQR:**
   * DQR Nivel 5: $\ge 400$ horas pedagógicas.
   * DQR Nivel 6: $\ge 1,200$ horas pedagógicas.
   * DQR Nivel 7: $\ge 1,600$ horas pedagógicas.
5. **Ecosistema Digital Institucional:**
   * Sesiones virtuales sincrónicas operadas exclusivamente en **Microsoft Teams** y suite **Microsoft 365**.
   * Gestión de aprendizaje y aulas virtuales alojadas en plataforma LMS Moodle oficial (**Kinal.academy**).
   * Prohibido hacer referencias a herramientas no institucionales (Google Meet / Classroom).
6. **Simbología Técnica Estandarizada:**
   * En diagramas de instrumentación y tuberías, utilizar denominaciones genéricas y neutrales (*«simbología técnica normada»*, *«simbología industrial estandarizada»*, *«etiquetas de instrumentos normadas»*, *«bridas estandarizadas Clase 150/300»*), prescindiendo de marcas o menciones a normas específicas como ISA o ANSI.
7. **Política Estricta de Entregables:**
   * **No utilizar la carpeta `output/`**. Todos los productos generados para un curso se almacenan de manera definitiva en su subcarpeta dedicada dentro de `Cursos/<Nombre_Curso>/`.

---

## 4. Memoria de Conversación y Trazabilidad Histórica

Para verificar la bitácora cronológica completa, el desglose de decisiones didácticas, los cambios solicitados por la dirección institucional y la evolución de los programas formativos:
* 👉 Consulte la memoria oficial en: [`docs/MEMORIA_CONVERSACION_DISENO_INSTRUCCIONAL.md`](./docs/MEMORIA_CONVERSACION_DISENO_INSTRUCCIONAL.md).
