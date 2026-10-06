# Reglas y Guías para Agentes: Diseñador e Instruccional Curricular

Este proyecto está dedicado al **Diseño Curricular y Didáctico Técnico-Profesional y Dual**, basado en los estándares del **Marco Alemán de Cualificaciones (DQR)**, el **Sistema Dual de Formación en Alternancia** y los lineamientos institucionales de **Fundación Kinal**.

---

## 1. Skill Principal de Proyecto
- Toda solicitud sobre diseño curricular, secuencias didácticas, dosificación macro/micro o elaboración de programas formativos debe alinearse con la skill del proyecto: [`.agents/skills/curriculum-didactic-designer/SKILL.md`](./.agents/skills/curriculum-didactic-designer/SKILL.md).
- La base inmutable de conocimiento pedagógico reside en [`.agents/skills/curriculum-didactic-designer/references/curricular_map_and_sources.md`](./.agents/skills/curriculum-didactic-designer/references/curricular_map_and_sources.md).

---

## 2. Reglas Mandatorias de Negocio y Operación
1. **Cero Alucinación / Grounding Estricto:** No inventar ni extrapolar marcos pedagógicos externos fuera de las fuentes definidas en el proyecto (DQR, Sistema Dual, Sajonia y Kinal).
2. **Citas Textuales Obligatorias:** Preservar las definiciones oficiales para:
   - **Formación Profesional Dual:** *"concepto de aprendizaje para jóvenes que tiene como objetivo preparar a los aprendices para su vida profesional, por lo que la formación se realiza en régimen de alternancia entre la escuela o el centro de formación y la empresa. El aprender en el proceso del trabajo es base y a la vez objetivo de la acción formativa"*.
   - **Competencia según DQR:** *"the ability and readiness of the individual to use knowledge, skills and personal, social and methodological competences and to behave in a considered, individual and socially responsible manner. Competence is understood in this sense as the comprehensive ability to act"*.
   - **Valores de Kinal:** *"Visión cristiana de la vida. Respeto a la dignidad de la persona. Espíritu de servicio. Trabajo bien hecho. Libertad personal responsable"*.
   - **Misión de Kinal:** *"Formar a jóvenes y adultos a través de una educación integral, con énfasis en las áreas técnicas y tecnológicas, influyendo positivamente en su trabajo, su familia y la sociedad"*.
3. **Umbral Aprobatorio:** Nota mínima de **75 puntos sobre 100** para cursos regulares y exámenes por suficiencia.
4. **Cargas Horarias DQR:** DQR 5 ($\ge 400$ hrs), DQR 6 ($\ge 1,200$ hrs), DQR 7 ($\ge 1,600$ hrs).
5. **Ecosistema Digital y Plataformas Institucionales:** En Fundación Kinal las clases sincrónicas en línea y la plataforma escolar se operan sobre el ecosistema **Microsoft (Microsoft Teams y Microsoft 365)**. La plataforma LMS oficial de gestión de cursos y contenidos virtuales es **Moodle (Kinal.academy)**. No utilizar referencias a Google Meet ni Google Classroom en los programas de Kinal.

---

## 3. Pipeline Multi-Agente y Entregables
- Mantener la separación de artefactos en la carpeta [`pipeline/`](./pipeline/):
  - `curated_curriculum_spec.json` (Fase 1: Curaduría)
  - `macro_curriculum_plan.json` (Fase 2: Macroplanificación)
  - `detailed_didactic_sequences.json` (Fase 3: Dosificación de secuencias didácticas)
- Formatear los entregables finales en la carpeta [`output/`](./output/):
  - Documento maquetado HTML en [`output/programa_formativo_dual_dqr6.html`](./output/programa_formativo_dual_dqr6.html) siguiendo las plantillas en `resources/document_templates.html`.
  - Documento Markdown en [`output/PROGRAMA_FORMATIVO_DUAL_DQR6.md`](./output/PROGRAMA_FORMATIVO_DUAL_DQR6.md).
