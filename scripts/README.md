# Scripts de Automatización y Generación Curricular

Este directorio centraliza los scripts en Python utilizados para la extracción de datos desde Excel, la generación de documentos Word (.docx), la creación de portales web interactivos y la distribución temática de los programas formativos.

---

## 1. Clasificación de Scripts

### A. Ecosistema de Portales Web y TSU (Técnico Superior Universitario)
| Script | Descripción |
| :--- | :--- |
| [`generate_portal_ecosystem.py`](./generate_portal_ecosystem.py) | Genera el ecosistema completo de portales: Raíz (`index.html`), Portal TSU (`TSU/index.html`) y Hub de Revisión (`Revision_Temarios/index.html`). |
| [`build_unified_master_portal.py`](./build_unified_master_portal.py) | Compilador maestro que consolida la navegación e interfaces del portal unificado de TSU y áreas técnicas. |
| [`unify_tsu_portal.py`](./unify_tsu_portal.py) | Genera la landing page interactiva de TSU y archiva las versiones previas en `TSU/historico/`. |
| [`build_tsu_subpages.py`](./build_tsu_subpages.py) | Genera las subpáginas temáticas por línea curricular (Ética, Matemáticas, Física, Administración) y el mapa curricular. |
| [`generate_tsu_all_courses.py`](./generate_tsu_all_courses.py) | Genera las 20 páginas HTML detalladas de las asignaturas de los 4 bimestres de TSU. |
| [`generate_tsu_new_distribution.py`](./generate_tsu_new_distribution.py) | Genera la propuesta y visualización de la Nueva Distribución Temática 2026 de TSU (HTML y Markdown). |
| [`update_index.py`](./update_index.py) | Script de utilidad para actualizar la botonera y enlaces a los 20 cursos en `TSU/index.html`. |

### B. Generación de Propuestas Curriculares desde Excel (`Revision_Temarios/`)
Estos scripts leen los libros de Excel de los programas de curso (`.xlsx`) y generan propuestas curriculares modernizadas con formato HTML en `Revision_Temarios/`:

| Script | Especialidad / Curso Generado |
| :--- | :--- |
| [`build_area2_proposals.py`](./build_area2_proposals.py) | Controles y Máquinas Eléctricas (Área Electricidad / Electrónica) |
| [`complete_area2.py`](./complete_area2.py) | Automatización Industrial (Área Electricidad / Electrónica) |
| [`build_area3_proposals.py`](./build_area3_proposals.py) | Mantenimiento Mecánico Industrial (Área Mecánica Industrial) |
| [`complete_area3.py`](./complete_area3.py) | Calderas de Vapor (Área Mecánica Industrial) |
| [`build_area4_part1.py`](./build_area4_part1.py) | Mecánica de Motores a Gasolina (Área Mecánica Automotriz) |
| [`complete_area4_part1.py`](./complete_area4_part1.py) | Mecanismos del Automóvil (Área Mecánica Automotriz) |
| [`complete_area4_ema.py`](./complete_area4_ema.py) | Electromecánica Automotriz (Área Mecánica Automotriz) |
| [`complete_area4_part2.py`](./complete_area4_part2.py) | Inyección Electrónica Automotriz (Área Mecánica Automotriz) |
| [`complete_area4_part2_all.py`](./complete_area4_part2_all.py) | Aire Acondicionado Automotriz y Mecánica de Motocicletas |

### C. Generación de Documentos Word (`.docx`)
| Script | Salida Generada |
| :--- | :--- |
| [`generate_dosificacion_word.py`](./generate_dosificacion_word.py) | Genera `Cursos/Mecatrónica/Dosificacion_y_Secuencia_Didactica_Mecatronica_Kinal.docx`. |
| [`generate_propuesta_word.py`](./generate_propuesta_word.py) | Genera `Cursos/Mecatrónica/Propuesta_Curso_Mecatronica_Kinal.docx`. |
| [`generate_temario_word.py`](./generate_temario_word.py) | Genera `output/Temario_Curso_Mecatronica_Kinal.docx`. |

---

## 2. Forma de Ejecución

Se recomienda ejecutar los scripts desde la raíz del proyecto para preservar las rutas relativas predeterminadas:

```bash
# Ejemplo: Generar el ecosistema de portales
python scripts/generate_portal_ecosystem.py

# Ejemplo: Generar documentos Word de Mecatrónica
python scripts/generate_dosificacion_word.py
python scripts/generate_propuesta_word.py
python scripts/generate_temario_word.py

# Ejemplo: Generar propuesta técnica desde Excel
python scripts/complete_area2.py
```
