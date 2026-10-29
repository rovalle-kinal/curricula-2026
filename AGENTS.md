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

## 3. Estructura de Entregables y Organización del Repositorio
- **Carpeta Oficial de Cursos (Cursos/<Nombre_Curso>/):** 
  - **No utilizar la carpeta output/**. Todos los artefactos generados para un curso deben alojarse exclusivamente en su subcarpeta dedicada dentro de [Cursos/](./Cursos/).
  - Para cada curso diseñado se genera y almacena en su carpeta respectiva el paquete completo:
    1. Propuesta Técnica y Temario en Markdown / Word (.md / .docx).
    2. Plan de Clase y Macroplanificación (.md / .docx).
    3. Secuencia Didáctica en 3 momentos y Rúbrica Analítica (.md / .docx).
    4. Página Web Maquetada y Responsiva (.html).
    5. Documento PDF institucional de alta fidelidad compilado con ReportLab (.pdf).
- **Revisiones Curriculares (Revisiones_Curriculares/):**
  - Todas las revisiones, mallas, temarios y auditorías curriculares se centralizan en [Revisiones_Curriculares/](./Revisiones_Curriculares/):
    - CET/: Pensum y actualizaciones del Centro Educativo Técnico (Electrónica e Informática).
    - TSU/: Pensum, auditorías y planes de clase del Técnico Superior Universitario.
    - Carreras_Tecnicas/: Temarios y mallas de carreras técnicas (Automotriz, Construcción, Electricidad, Mecánica, Topografía).
    - PDFs/: Compilaciones y auditorías oficiales en formato PDF.
