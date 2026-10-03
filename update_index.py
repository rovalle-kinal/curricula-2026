import os

base_dir = "/Users/arqovalle/Library/CloudStorage/OneDrive-Personal/Software/Antigravity/Diseño Instruccional/TSU"
mybrain_dir = "/Users/arqovalle/Library/CloudStorage/OneDrive-Personal/MyBrain/MyBrain/01 - My Brain/Kinal/TSU"

from generate_tsu_all_courses import courses

# Agrupar por bimestre
bimestres = {
    "Bimestre 1": [c for c in courses if c["bimestre"] == "Bimestre 1"],
    "Bimestre 2": [c for c in courses if c["bimestre"] == "Bimestre 2"],
    "Bimestre 3": [c for c in courses if c["bimestre"] == "Bimestre 3"],
    "Bimestre 4": [c for c in courses if c["bimestre"] == "Bimestre 4"],
}

html = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dictamen Curricular TSU 2026 (20 Cursos) | Fundación Kinal</title>
    <style>
        :root {
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
        }

        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            background-color: #f1f5f9;
            color: var(--text-dark);
            line-height: 1.6;
            padding: 24px;
        }
        .container {
            max-width: 1280px;
            margin: 0 auto;
            background: #ffffff;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.08);
            overflow: hidden;
            border: 1px solid var(--border-color);
        }
        header {
            background: linear-gradient(135deg, var(--kinal-blue) 0%, #1e3a8a 100%);
            color: #ffffff;
            padding: 36px 40px;
            border-bottom: 4px solid var(--kinal-accent);
        }
        .header-badge {
            display: inline-block;
            background: rgba(217, 119, 6, 0.25);
            color: #fef08a;
            border: 1px solid var(--kinal-accent);
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.85rem;
            font-weight: 600;
            letter-spacing: 0.5px;
            margin-bottom: 12px;
            text-transform: uppercase;
        }
        header h1 { font-size: 2.2rem; font-weight: 700; margin-bottom: 8px; }
        header p { color: #cbd5e1; font-size: 1.05rem; max-width: 900px; }

        nav.nav-bar {
            background: #0b1f3a;
            padding: 0 40px;
            display: flex;
            gap: 16px;
            overflow-x: auto;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }
        nav.nav-bar a {
            color: #94a3b8;
            text-decoration: none;
            padding: 14px 18px;
            font-weight: 600;
            font-size: 0.95rem;
            display: inline-block;
            border-bottom: 3px solid transparent;
            transition: all 0.2s;
            white-space: nowrap;
        }
        nav.nav-bar a:hover { color: #ffffff; border-bottom-color: var(--kinal-accent); }
        nav.nav-bar a.active { color: #ffffff; background: rgba(255,255,255,0.06); border-bottom-color: var(--kinal-accent); }

        main { padding: 40px; }

        .legend-card {
            background: var(--kinal-light);
            border: 1px solid var(--border-color);
            border-radius: 10px;
            padding: 24px;
            margin-bottom: 36px;
        }
        .legend-card h3 {
            font-size: 1.15rem;
            color: var(--kinal-blue);
            margin-bottom: 16px;
        }
        .legend-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 16px;
        }
        .legend-item {
            padding: 14px 18px;
            border-radius: 8px;
            font-size: 0.92rem;
            border-width: 1px;
            border-style: solid;
        }
        .legend-item.actualizar {
            background-color: var(--color-actualizar-bg);
            color: var(--color-actualizar-text);
            border-color: var(--color-actualizar-border);
        }
        .legend-item.anular {
            background-color: var(--color-anular-bg);
            color: var(--color-anular-text);
            border-color: var(--color-anular-border);
        }
        .legend-item.nuevo {
            background-color: var(--color-nuevo-bg);
            color: var(--color-nuevo-text);
            border-color: var(--color-nuevo-border);
        }

        .bimestre-section {
            margin-bottom: 40px;
        }
        .bimestre-title {
            font-size: 1.45rem;
            color: var(--kinal-blue);
            margin-bottom: 16px;
            padding-bottom: 8px;
            border-bottom: 2px solid #e2e8f0;
            display: flex;
            align-items: center;
            justify-content: space-between;
        }
        .bimestre-title span {
            font-size: 0.9rem;
            font-weight: 500;
            color: var(--text-muted);
        }

        .courses-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
            gap: 18px;
        }

        .course-card {
            background: #ffffff;
            border: 1px solid var(--border-color);
            border-radius: 8px;
            padding: 18px;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            transition: transform 0.2s, box-shadow 0.2s, border-color 0.2s;
            box-shadow: 0 1px 3px rgba(0,0,0,0.04);
        }
        .course-card:hover {
            transform: translateY(-3px);
            box-shadow: 0 6px 16px rgba(0,0,0,0.08);
            border-color: var(--kinal-blue);
        }
        .course-period {
            font-size: 0.78rem;
            font-weight: 700;
            color: var(--kinal-accent);
            text-transform: uppercase;
            margin-bottom: 4px;
        }
        .course-card h4 {
            font-size: 1.05rem;
            color: var(--kinal-blue);
            margin-bottom: 8px;
            line-height: 1.3;
        }
        .course-desc {
            font-size: 0.85rem;
            color: var(--text-muted);
            margin-bottom: 14px;
            flex-grow: 1;
        }
        .course-badges {
            display: flex;
            gap: 4px;
            flex-wrap: wrap;
            margin-bottom: 12px;
        }
        .badge-mini {
            font-size: 0.7rem;
            padding: 2px 6px;
            border-radius: 4px;
            font-weight: 700;
            text-transform: uppercase;
        }
        .card-link {
            display: block;
            text-align: center;
            background: #f8fafc;
            color: var(--kinal-blue);
            border: 1px solid var(--border-color);
            text-decoration: none;
            padding: 8px 12px;
            border-radius: 6px;
            font-size: 0.85rem;
            font-weight: 600;
            transition: all 0.2s;
        }
        .card-link:hover {
            background: var(--kinal-blue);
            color: #ffffff;
            border-color: var(--kinal-blue);
        }

        .callout {
            border-left: 4px solid var(--kinal-accent);
            background: #fffbeb;
            padding: 18px 24px;
            border-radius: 0 8px 8px 0;
            margin-bottom: 30px;
        }
        .callout h4 { color: #92400e; margin-bottom: 6px; font-size: 1.05rem; }
        .callout p { color: #78350f; font-size: 0.93rem; }

        footer {
            background: #0f172a;
            color: #94a3b8;
            padding: 24px 40px;
            font-size: 0.88rem;
            text-align: center;
        }
    </style>
</head>
<body>

<div class="container">
    <header>
        <span class="header-badge">Auditoría Curricular Integral 2026</span>
        <h1>TÉCNICO SUPERIOR UNIVERSITARIO (TSU)</h1>
        <p>Estructura Académica Consolidada de 20 Cursos (4 Bimestres) de la Escuela Técnica Superior de Fundación Kinal (Avalado por Universidad del Istmo - UNIS). Dictamen técnico de pertinencia para mandos medios en Guatemala.</p>
    </header>

    <nav class="nav-bar">
        <a href="index.html" class="active">Portal General (20 Cursos)</a>
        <a href="nueva_distribucion_tematica_tsu.html" style="color: #fef08a; font-weight: 700;">🌟 Nueva Distribución Temática 2026 (7 Especialidades + IA)</a>
        <a href="#bimestre-1">Bimestre 1</a>
        <a href="#bimestre-2">Bimestre 2</a>
        <a href="#bimestre-3">Bimestre 3</a>
        <a href="#bimestre-4">Bimestre 4</a>
    </nav>

    <main>
        <div class="callout">
            <h4>Estructura Operativa del Año Académico (3er Año TSU)</h4>
            <p>El año académico consta de <strong>4 bimestres</strong> (10 meses lectivos, febrero a noviembre). En cada bimestre se imparten simultáneamente <strong>5 asignaturas obligatorias</strong> en periodos de 50 minutos (Jornada Matutina: 8:00 a 12:30 hrs / Jornada Vespertina: 13:00 a 17:30 hrs). Total: 20 cursos en el año, 60 sesiones (270 horas). Nota mínima aprobatoria institucional: <strong>&ge; 75 puntos sobre 100</strong>.</p>
        </div>

        <div class="legend-card">
            <h3>Convención Visual de Revisión Curricular</h3>
            <div class="legend-grid">
                <div class="legend-item actualizar">
                    <strong>Amarillo: Contenidos a Actualizar</strong>
                    Conceptos vigentes pero que requieren modernización urgente con software, normas recientes e Industria 4.0.
                </div>
                <div class="legend-item anular">
                    <strong>Rojo: Contenidos a Anular</strong>
                    Contenidos obsoletos, redundancias de nivel básico/medio, teoría aislada o cálculos manuales improductivos.
                </div>
                <div class="legend-item nuevo">
                    <strong>Azul: Nuevos Conocimientos</strong>
                    Competencias emergentes demandadas por la industria guatemalteca (IA, programación, Lean, analítica y finanzas).
                </div>
            </div>
        </div>
"""

for b_name, b_courses in bimestres.items():
    b_id = b_name.lower().replace(" ", "-")
    html += f"""
        <div class="bimestre-section" id="{b_id}">
            <div class="bimestre-title">
                <h2>{b_name}</h2>
                <span>5 Asignaturas Obligatorias (50 min c/u)</span>
            </div>
            <div class="courses-grid">
    """
    for c in b_courses:
        html += f"""
                <div class="course-card">
                    <div>
                        <div class="course-period">{c["periodo"]}</div>
                        <h4><span>{c["icono"]}</span> {c["nombre"]}</h4>
                        <div class="course-desc"><strong>Eje:</strong> {c["eje"]}</div>
                        <div class="course-badges">
                            <span class="badge-mini" style="background:var(--color-anular-bg); color:var(--color-anular-text);">Anular</span>
                            <span class="badge-mini" style="background:var(--color-actualizar-bg); color:var(--color-actualizar-text);">Actualizar</span>
                            <span class="badge-mini" style="background:var(--color-nuevo-bg); color:var(--color-nuevo-text);">Nuevo</span>
                        </div>
                    </div>
                    <a href="{c["id"]}.html" class="card-link">Ver Dictamen Completo →</a>
                </div>
        """
    html += """
            </div>
        </div>
    """

html += """
        <div style="background: #e2e8f0; padding: 24px; border-radius: 8px; margin-top: 40px;">
            <h3 style="color: var(--kinal-blue); margin-bottom: 10px;">Acreditación y Salida Profesional</h3>
            <p style="font-size: 0.92rem; color: var(--text-dark); margin-bottom: 12px;">
                Al completar y aprobar satisfactoriamente los 4 bimestres (20 asignaturas con nota &ge; 75 pts) y certificar el nivel A2 en inglés (prueba ELASH II vía Kinal Language School), el egresado obtiene el <strong>Título de Técnico Superior Universitario en su Especialidad</strong> avalado por la <strong>Universidad del Istmo (UNIS)</strong> y Fundación Kinal, con equivalencia internacional a los niveles 5 y 6 del Marco Alemán de Cualificaciones (DQR).
            </p>
        </div>
    </main>

    <footer>
        Fundación Kinal • Escuela Técnica Superior • Pensum General del Técnico Superior Universitario (TSU) • Convenio Universidad del Istmo (UNIS) • Guatemala, 2026
    </footer>
</div>

</body>
</html>
"""

with open(os.path.join(base_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(html)

with open(os.path.join(mybrain_dir, "index.html"), "w", encoding="utf-8") as f:
    f.write(html)

print("index.html actualizado exitosamente con los 20 cursos y 4 bimestres.")
