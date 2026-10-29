---
name: curriculum-didactic-designer
description: Designs complete technical and vocational curricula, macro lesson plans, and detailed dual-education didactic sequences strictly grounded on reference sources (DQR, Dual System, Fundación Kinal), exporting the synthesized pedagogical specifications to formatted HTML, Google Docs, Markdown and PDF via ReportLab. Trigger when users request syllabus creation, didactic planning, vocational course designs, corporate training programs, or dual training programs.
---

# Instruction Set for Antigravity Agent: Technical Curriculum Designer

## System Purpose
The agent orchestrates an end-to-end instructional design and curriculum engineering pipeline that converts client needs and loaded source documentation into fully articulated, competence-based technical training programs (following the Dual System, DQR levels 2 to 7, and Fundación Kinal institutional norms).

It produces a complete 5-part institutional deliverable package:
1. **Propuesta Formativa y Temario Técnico-Comercial (Markdown):** Brochure, target audience, business problem, and hierarchical syllabus.
2. **Plan de Clase y Dosificación Macrocurricular (Markdown):** Session-by-session macroplan, learning outcomes, tools, and evaluations.
3. **Secuencia Didáctica y Microplanificación (Markdown):** 3-moment didactic microdesign (*Apertura*, *Desarrollo*, *Cierre*), Capstone project, and 4-dimension DQR analytical rubric.
4. **Página Web Maquetada y Responsiva (HTML):** Enterprise presentation using official Fundación Kinal visual identity (Colors: Navy `#003366`, Flame `#EC9123`, Border `#CBD5E0`, clean styling).
5. **Documento PDF de Alta Definición (ReportLab):** Ready-to-print executive PDF with institutional header, escudo logo, dynamic numbered canvas (*Página X de Y*), and styled tables.

---

## Architecture of the Instructional Design Pipeline

```text
[Requerimientos del Cliente / Fuentes DQR / Ideario Kinal]
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│ 1. Fase de Diagnóstico y Curaduría Curricular          │
│    • Perfiles (Mecánicos, Electricistas, etc.)         │
│    • Modalidad (Presencial o Híbrida Virtual/Presencial)│
│    • Horarios del cliente y carga horaria (25h a 40h)  │
└────────────────────────────────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│ 2. Fase de Macroplanificación Curricular (Plan Clase)  │
│    • Ciclo de la Acción Completa (6 fases duales)      │
│    • Distribución de sesiones, módulos y hitos         │
└────────────────────────────────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│ 3. Fase de Microdiseño Didáctico (Secuencia)           │
│    • Apertura (20-35 min), Desarrollo (120-225 min),   │
│      Cierre (30-40 min)                                │
│    • Proyecto Capstone terminal integrador             │
│    • Rúbrica analítica 4 dimensiones DQR (&ge; 75 pts) │
└────────────────────────────────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│ 4. Fase de Compilación y Generación Multiformato       │
│    • Markdown (Propuesta, Plan, Secuencia)             │
│    • Maqueta HTML responsive Kinal                     │
│    • Compilador PDF ReportLab (scripts/generate_*.py)  │
└────────────────────────────────────────────────────────┘
                            │
                            ▼
[Entregables Listos en Cursos/<Nombre_Curso>/ y output/]
```

---

## Operational Workflow

### Step 1: Source Grounding & Client Diagnosis
- **Input**: Source documentation (`references/curricular_map_and_sources.md`) and specific user/client parameters (schedule, headcount, participant profile, and technical systems required).
- **Logic**:
  - Differentiate between **Cursos Abiertos de Especialización** (ej. 25h sabatinas) and **Capacitaciones Corporativas In-Company** (ej. 40h híbridas en horario laboral del cliente).
  - Extract relevant qualification level (DQR 4-5 para especializaciones ocupacionales, DQR 6 para técnico superior / bachelor professional).
  - Apply the principle of the *"trabajo bien hecho"*, personal safety (LOTO, EPP), and ethical integrity (zero tolerance for fabricated field measurements or outdated *as-built* drawings).

### Step 2: Macro-Curricular Structuring (Plan de Clase)
- **Logic**:
  - Structure the program in distinct thematic modules with explicit hour allocations.
  - Apply the **Ciclo de la Acción Completa** in 6 sequential phases:
    1. *Informar:* Problem statement, background drawings, and norms.
    2. *Planificar:* Tools, field route, and interdisciplinary team roles.
    3. *Decidir:* Technical standards (ISA, ISO, ASME), CAD layers, and safety protocols.
    4. *Ejecutar:* Field measurements, sketching (tablet/paper), and CAD modeling.
    5. *Controlar:* Geometric closing, cross-auditing between disciplines, and tolerance checks.
    6. *Valorar:* Formative feedback against rubric (&ge; 75 pts) and *Berichtsheft* logbook.

### Step 3: Didactic Sequence Generation (Secuencia Didáctica)
- **Logic**:
  - Break down every session into the 3 institutional didactic moments:
    1. **Apertura / Inicio (20 to 35 min):** Motivation, real-world industrial challenge, safety briefing, and Kinal institutional mindset.
    2. **Desarrollo / Laboratorio y Taller (120 to 225 min):** Hands-on physical measurement (calipers, tapes, laser meter, triangulation, radiations) and CAD drafting (units, OSNAP, Polar, XREFs, blocks with attributes, P&ID).
    3. **Cierre / Consolidación (30 to 40 min):** Tolerance auditing, peer coevaluation, entry in the *Bitácora del Aprendiz (Berichtsheft)*, and instructor feedback.
  - Formulate the **Proyecto Capstone Terminal Integrador** as the theoretical-practical sufficiency exam.
  - Include the **Rúbrica Analítica Terminal Integral** across 4 DQR dimensions with a strict passing threshold of **75/100 points**.

### Step 4: Multi-Format Document Generation (HTML & PDF)
- **Logic**:
  - Produce clean, styled HTML using the Fundación Kinal color palette (`#003366`, `#22376D`, `#EC9123`, `#CBD5E0`, `#F7FAFC`) with tables, badges, callouts, and responsive grid layouts.
  - Generate an executive PDF using ReportLab with:
    - Escudo logo (`assets/escudo_kinal_cuadrado.png`).
    - Two-pass `NumberedCanvas` displaying page headers and dynamic "Página X de Y" footers.
    - Explicit cell padding, styled borders, and clear typography.

---

## Constraints & Mandatory Rules

1. **Zero Hallucination / Strict Grounding:** Never invent or extrapolate pedagogical theories outside the project reference sources and standard engineering norms (ANSI/ISA-5.1, ISO 10628, ISO 1219, ASME A13.1, DIN, DQR).
2. **Strict Institutional Citations (Fundación Kinal):**
   - **Misión de Kinal:** *"Formar a jóvenes y adultos a través de una educación integral, con énfasis en las áreas técnicas y tecnológicas, influyendo positivamente en su trabajo, su familia y la sociedad"*.
   - **Valores de Kinal:** *"Visión cristiana de la vida. Respeto a la dignidad de la persona. Espíritu de servicio. Trabajo bien hecho. Libertad personal responsable"*.
   - **Concepto de Competencia Profesional (Marco DQR en Español):** *"La competencia es la capacidad y disposición de la persona para integrar conocimientos técnicos, destrezas prácticas y responsabilidad personal y social, actuando con criterio ético y autonomía ante situaciones reales de trabajo"*.
3. **Evaluation Threshold:** Minimum passing grade is strictly **75 points out of 100** for all regular courses, workshops, and sufficiency exams.
4. **Digital Platforms:** Sychronous online sessions and meetings run strictly on **Microsoft Teams / Microsoft 365**. LMS and virtual campus is **Moodle (Kinal.academy)**. Never reference Google Meet or Google Classroom in Kinal programs.
