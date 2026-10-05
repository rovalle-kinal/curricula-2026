import os
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import parse_xml
from docx.oxml.ns import nsdecls

def set_cell_background(cell, fill_hex):
    tcPr = cell._element.get_or_add_tcPr()
    shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{fill_hex}"/>')
    tcPr.append(shd)

def set_cell_margins(cell, top=80, bottom=80, left=100, right=100):
    tcPr = cell._element.get_or_add_tcPr()
    tcMar = parse_xml(
        f'<w:tcMar {nsdecls("w")}>'
        f'<w:top w:w="{top}" w:type="dxa"/>'
        f'<w:bottom w:w="{bottom}" w:type="dxa"/>'
        f'<w:left w:w="{left}" w:type="dxa"/>'
        f'<w:right w:w="{right}" w:type="dxa"/>'
        f'</w:tcMar>'
    )
    tcPr.append(tcMar)

def set_table_borders(table, color="CBD5E0", sz="4"):
    tblPr = table._element.xpath('w:tblPr')
    if tblPr:
        borders = parse_xml(
            f'<w:tblBorders {nsdecls("w")}>'
            f'<w:top w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'<w:bottom w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'<w:insideH w:val="single" w:sz="{sz}" w:space="0" w:color="{color}"/>'
            f'<w:insideV w:val="none"/>'
            f'<w:left w:val="none"/>'
            f'<w:right w:val="none"/>'
            f'</w:tblBorders>'
        )
        tblPr[0].append(borders)

def style_p(p, space_before=0, space_after=4, line_spacing=1.15):
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = line_spacing

def style_heading(p, text, level=1, color=RGBColor(0, 51, 102)):
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    r.font.name = "Calibri"
    r.font.bold = True
    r.font.color.rgb = color
    if level == 1:
        p.paragraph_format.space_before = Pt(16)
        p.paragraph_format.space_after = Pt(6)
        r.font.size = Pt(15)
    elif level == 2:
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(4)
        r.font.size = Pt(13)
    elif level == 3:
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(2)
        r.font.size = Pt(11)

def add_callout(doc, text, bold_prefix="", fill_hex="F7FAFC", border_color="003366"):
    tbl = doc.add_table(rows=1, cols=1)
    tbl.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl.autofit = False
    tbl.columns[0].width = Inches(6.5)
    
    cell = tbl.cell(0, 0)
    set_cell_background(cell, fill_hex)
    set_cell_margins(cell, top=120, bottom=120, left=180, right=120)
    
    tcPr = cell._element.get_or_add_tcPr()
    borders = parse_xml(
        f'<w:tcBorders {nsdecls("w")}>'
        f'<w:left w:val="single" w:sz="24" w:space="0" w:color="{border_color}"/>'
        f'<w:top w:val="none"/>'
        f'<w:bottom w:val="none"/>'
        f'<w:right w:val="none"/>'
        f'</w:tcBorders>'
    )
    tcPr.append(borders)
    
    p = cell.paragraphs[0]
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    p.paragraph_format.line_spacing = 1.15
    
    if bold_prefix:
        r_pre = p.add_run(bold_prefix + " ")
        r_pre.font.name = "Calibri"
        r_pre.font.size = Pt(10)
        r_pre.font.bold = True
        r_pre.font.color.rgb = RGBColor(0, 51, 102)
        
    r_txt = p.add_run(text)
    r_txt.font.name = "Calibri"
    r_txt.font.size = Pt(10)
    r_txt.font.italic = True
    r_txt.font.color.rgb = RGBColor(45, 55, 72)
    
    p_post = doc.add_paragraph()
    style_p(p_post, space_before=0, space_after=6)

def generate_dosificacion():
    doc = docx.Document()
    
    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    COLOR_PRIMARY = RGBColor(0, 51, 102)
    COLOR_SECONDARY = RGBColor(74, 85, 104)
    COLOR_DARK = RGBColor(26, 32, 44)

    # =========================================================================
    # PORTADA / ENCABEZADO TÉCNICO
    # =========================================================================
    p_inst = doc.add_paragraph()
    style_p(p_inst, space_before=20, space_after=2)
    r_inst = p_inst.add_run("FUNDACIÓN KINAL")
    r_inst.font.name = "Calibri"
    r_inst.font.size = Pt(14)
    r_inst.font.bold = True
    r_inst.font.color.rgb = COLOR_PRIMARY

    p_esc = doc.add_paragraph()
    style_p(p_esc, space_before=0, space_after=20)
    r_esc = p_esc.add_run("Escuela Técnica Superior — Coordinación de Formación Continua e Innovación")
    r_esc.font.name = "Calibri"
    r_esc.font.size = Pt(11)
    r_esc.font.color.rgb = COLOR_SECONDARY

    p_tit = doc.add_paragraph()
    style_p(p_tit, space_before=10, space_after=8)
    r_tit = p_tit.add_run("DOSIFICACIÓN CURRICULAR Y SECUENCIA DIDÁCTICA DETALLADA")
    r_tit.font.name = "Calibri"
    r_tit.font.size = Pt(20)
    r_tit.font.bold = True
    r_tit.font.color.rgb = COLOR_PRIMARY

    p_sub = doc.add_paragraph()
    style_p(p_sub, space_before=0, space_after=18)
    r_sub = p_sub.add_run("Mecatrónica Industrial y Fabricación Digital Aplicada (20 Sesiones Sabatinas / 90 Horas)")
    r_sub.font.name = "Calibri"
    r_sub.font.size = Pt(12)
    r_sub.font.italic = True
    r_sub.font.color.rgb = COLOR_SECONDARY

    add_callout(doc, 
        "«El aprender en el proceso del trabajo es base y a la vez objetivo de la acción formativa». Cada sesión sabatina de 4.5 horas (270 minutos) se articula en tres momentos pedagógicos rigurosos: Apertura (30 min - activación, seguridad y ética Kinal), Desarrollo (210 min - ejecución práctica en banco y maquinaria) y Cierre (30 min - Berichtsheft, reflexión de calidad y orden 5S). Umbral institucional aprobatorio: 75 puntos sobre 100.",
        bold_prefix="Marco Metodológico Dual de Fundación Kinal:")

    # =========================================================================
    # 1. MATRIZ GENERAL DE DOSIFICACIÓN (TABLA RESUMEN DE 20 SESIONES)
    # =========================================================================
    h1_1 = doc.add_paragraph()
    style_heading(h1_1, "1. Matriz General de Dosificación Cronológica (Febrero - Junio)", level=1)

    tbl_cron = doc.add_table(rows=21, cols=5)
    tbl_cron.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_cron.autofit = False
    tbl_cron.columns[0].width = Inches(0.8)
    tbl_cron.columns[1].width = Inches(1.0)
    tbl_cron.columns[2].width = Inches(1.2)
    tbl_cron.columns[3].width = Inches(2.2)
    tbl_cron.columns[4].width = Inches(1.3)
    set_table_borders(tbl_cron, color="CBD5E0", sz="4")

    # Header
    hdr = tbl_cron.rows[0]
    for c in hdr.cells:
        set_cell_background(c, "003366")
    headers = ["Sesión", "Mes / Horas", "Módulo", "Contenido Central de Taller", "Equipamiento Kinal"]
    for idx, text in enumerate(headers):
        p = hdr.cells[idx].paragraphs[0]
        style_p(p, space_before=0, space_after=0)
        r = p.add_run(text)
        r.font.name = "Calibri"
        r.font.size = Pt(9)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    cron_data = [
        ("S-01", "Feb (4.5h)", "M1: CAD / Láser", "Fundamentos mecatrónicos, EPP, metrología y croquis CAD 3D", "CAD / Metrología"),
        ("S-02", "Feb (4.5h)", "M1: CAD / Láser", "Ingeniería inversa, compensación de corte (kerf) y finger joints", "CAD / Vernier"),
        ("S-03", "Feb (4.5h)", "M1: CAD / Láser", "Alistamiento, capas de grabado/corte y parametrización láser", "Cortadora Láser CO2"),
        ("S-04", "Feb (4.5h)", "M1: CAD / Láser", "Ensamble de gabinete, fixture y evaluación práctica M1 (≥ 75 pts)", "Láser / Herramientas"),
        ("S-05", "Mar (4.5h)", "M2: 3D FDM", "Cinemática de engranes, poleas GT2 y ciencia de polímeros", "CAD / Cálculos"),
        ("S-06", "Mar (4.5h)", "M2: 3D FDM", "DFAM, orientación contra líneas de esfuerzo y perfiles en Slicer", "Laminador / Impresora 3D"),
        ("S-07", "Mar (4.5h)", "M2: 3D FDM", "Tolerancias Print-in-Place, insertos roscados y calibración", "Impresora 3D / Cautín"),
        ("S-08", "Mar (4.5h)", "M2: 3D FDM", "Montaje de garra robótica y evaluación práctica M2 (≥ 75 pts)", "Impresora 3D / Banco"),
        ("S-09", "Abr (4.5h)", "M3: Fresado CNC", "Cinemática CNC, ejes coordenados, Código G y sujeción segura", "Simulador CNC / G-Code"),
        ("S-10", "Abr (4.5h)", "M3: Fresado CNC", "Estrategias CAM: planeado, cajeras, contorneado y taladrado", "Software CAM / PC"),
        ("S-11", "Abr (4.5h)", "M3: Fresado CNC", "Montaje de boquillas ER, fresas de carburo y puesta a cero (WCS)", "Router CNC / Sonda Z"),
        ("S-12", "Abr (4.5h)", "M3: Fresado CNC", "Maquinado de bancada mecatrónica y evaluación M3 (≥ 75 pts)", "Router CNC / Micrómetro"),
        ("S-13", "May (4.5h)", "M4: Sensórica", "Transducción industrial, sensores PNP/NPN y finales de carrera", "Sensores / Banco"),
        ("S-14", "May (4.5h)", "M4: Control Ejes", "Motores a pasos NEMA, drivers industriales y microstepping", "Drivers / Motores NEMA"),
        ("S-15", "May (4.5h)", "M4: Cableado IEC", "Electroválvulas neumáticas, ductos ranurados, ferrules y rotulado", "Tablero / Ferrules / IEC"),
        ("S-16", "May (4.5h)", "M4: Control Ejes", "Rampas trapezoidales, parada segura y evaluación M4 (≥ 75 pts)", "Eje Lineal / Multímetro"),
        ("S-17", "Jun (4.5h)", "M5: Integración", "Arquitectura de integración, paneles HMI y diagramas FSM", "Tablero / PC / Botoneras"),
        ("S-18", "Jun (4.5h)", "M5: Ensamble", "Ensamble final: bancada CNC, partes 3D, gabinete láser y cables", "Banco Ensamble / EPP"),
        ("S-19", "Jun (4.5h)", "M5: Puesta Marcha", "Carga de programa, calibración, pruebas en seco y troubleshooting", "Toda la Infraestructura"),
        ("S-20", "Jun (4.5h)", "M5: Capstone", "Evaluación Terminal Integrada, defensa pública y clausura", "Jurado / Berichtsheft")
    ]

    for idx, (ses, mes, mod, cont, eq) in enumerate(cron_data, start=1):
        row = tbl_cron.rows[idx]
        if idx % 2 == 1:
            for c in row.cells:
                set_cell_background(c, "F7FAFC")
        for c_idx, val in enumerate([ses, mes, mod, cont, eq]):
            cell = row.cells[c_idx]
            set_cell_margins(cell, top=50, bottom=50, left=60, right=60)
            p = cell.paragraphs[0]
            style_p(p, space_before=0, space_after=0)
            r = p.add_run(val)
            r.font.name = "Calibri"
            r.font.size = Pt(8.5)
            r.font.color.rgb = COLOR_DARK
            if c_idx in [0, 1]:
                r.font.bold = True

    doc.add_page_break()

    # =========================================================================
    # 2. MICRODISEÑO DIDÁCTICO DETALLADO SESIÓN POR SESIÓN (20 SESIONES)
    # =========================================================================
    h1_2 = doc.add_paragraph()
    style_heading(h1_2, "2. Microdiseño Didáctico Detallado por Sesión Sabatina", level=1)

    p_micro_intro = doc.add_paragraph()
    style_p(p_micro_intro, space_before=0, space_after=10)
    r = p_micro_intro.add_run("A continuación se describe la secuencia didáctica microestructurada de cada una de las 20 sesiones de 4.5 horas (270 minutos), respetando los tres momentos pedagógicos de la formación técnica dual:")
    r.font.name = "Calibri"
    r.font.size = Pt(10.5)
    r.font.color.rgb = COLOR_DARK

    # Módulos y sus 4 sesiones
    modulos_detalle = [
        {
            "nombre": "MÓDULO 1: Diseño CAD 3D, Metrología de Taller y Prototipado con Cortadora Láser (Febrero)",
            "sesiones": [
                {
                    "num": "Sesión 1",
                    "tema": "Fundamentos de Mecatrónica Industrial, Seguridad y CAD Paramétrico",
                    "objetivo": "Comprender la sinergia mecatrónica, aplicar normas de seguridad de taller Kinal y modelar piezas básicas mediante restricciones geométricas y metrología.",
                    "apertura": "Inducción al taller Kinal, verificación de EPP obligatorio y protocolo 5S. Presentación de un caso real: falla de un soporte en línea embotelladora guatemalteca por mala medición. Activación de conocimientos en unidades milimétricas.",
                    "desarrollo": "Práctica con pie de rey digital y micrómetro sobre muestras industriales. Introducción al software CAD: croquizado 2D paramétrico, cotas, restricciones de simetría/tangencia y operaciones de extrusión y vaciado 3D. Modelado guiado de placa base.",
                    "cierre": "Verificación dimensional de planos en CAD. Apertura de la Bitácora de Taller (Berichtsheft): registro de lecturas de medición. Limpieza del laboratorio bajo criterio 5S y reflexión sobre el trabajo pulcro.",
                    "recursos": "Calibradores vernier digitales, micrómetros, computadoras con software CAD, proyector.",
                    "evaluacion": "Verificación de plano CAD paramétrico acotado con tolerancia ≤ ±0.1 mm."
                },
                {
                    "num": "Sesión 2",
                    "tema": "Ingeniería Inversa y Diseño para Manufactura por Corte Láser (DFM)",
                    "objetivo": "Replicar piezas industriales existentes y diseñar gabinetes mecatrónicos con juntas mecánicas autoblocantes compensando la sangría de corte (kerf).",
                    "apertura": "Exhibición de piezas plásticas quebradas de plantas de alimentos. Análisis de falla y discusión del concepto de sangría de corte (kerf) en láser CO2 (0.15 - 0.25 mm) y su impacto en el ensamble a presión.",
                    "desarrollo": "Toma de medidas de tarjetas electrónicas y fuentes de poder. Modelado CAD de un gabinete con ranuras y lengüetas (finger joints) y encastres de pestaña a presión (snap-fits). Exportación de croquis limpios a formato vectorial DXF/SVG.",
                    "cierre": "Revisión cruzada entre parejas de estudiantes: verificación de compatibilidad de sangría en ensambles. Registro en la bitácora Berichtsheft sobre cálculo de compensación dimensional.",
                    "recursos": "Piezas mecánicas muestra, software CAD, guías de diseño de uniones para corte láser.",
                    "evaluacion": "Archivo vectorial DXF estructurado en capas con compensación kerf calculada."
                },
                {
                    "num": "Sesión 3",
                    "tema": "Operación Práctica, Parametrización y Seguridad en Cortadora Láser CO2",
                    "objetivo": "Calibrar y operar la cortadora láser CO2 de Kinal bajo normas de seguridad industrial, configurando potencias y velocidades por material.",
                    "apertura": "Charla técnica de seguridad: riesgos ópticos del láser CO2 Clase 4, obligatoriedad del sistema de extracción de gases y asistencia de aire comprimido (air assist). Consignación de seguridad.",
                    "desarrollo": "Importación de archivos DXF al software de control láser (LightBurn/LaserCAD). Configuración de capas: grabado superficial, marcado lineal y corte vectorial. Calibración manual de distancia focal mediante galga de enfoque. Pruebas de corte en acrílico cristal (3 y 5 mm), Delrin y MDF técnico.",
                    "cierre": "Inspección de bordes cortados: descarte de rebabas o quemado excesivo. Registro de parámetros óptimos (velocidad/potencia) en la bitácora de taller. Limpieza de óptica y bandeja de residuos.",
                    "recursos": "Cortadora Láser CO2 Kinal, extractor de humos, acrílico de 3 mm y 5 mm, MDF técnico, galga focal.",
                    "evaluacion": "Probeta de corte limpia sin quemaduras y verificación de bordes a 90°."
                },
                {
                    "num": "Sesión 4",
                    "tema": "Ensamble de Gabinete Mecatrónico y Evaluación Práctica del Módulo 1",
                    "objetivo": "Fabricar, ensamblar y verificar un gabinete industrial para control mecatrónico con tolerancias mecánicas estrictas según especificación.",
                    "apertura": "Presentación del reto de evaluación del Módulo 1: fabricación y montaje de gabinete para riel DIN y nido fixture en acrílico/Delrin. Criterios de evaluación y umbral aprobatorio de 75 puntos.",
                    "desarrollo": "Corte de piezas definitivas en la máquina láser Kinal. Desbarbado, retiro de película protectora y ensamble mecánico de paneles. Instalación de bisagras, soportes para riel DIN y orificios para pasamuros y ventiladores. Ajuste mecánico a presión.",
                    "cierre": "Evaluación formal con rúbrica analítica individual. Prueba de rigidez mecánica e inserción de componentes reales. Asignación de nota de módulo y retroalimentación personalizada.",
                    "recursos": "Cortadora láser, tornillería métrica M3, riel DIN, paneles de acrílico cortados, rúbrica M1.",
                    "evaluacion": "Proyecto Práctico Módulo 1 calificado con rúbrica analítica (Aprobatorio ≥ 75 pts)."
                }
            ]
        },
        {
            "nombre": "MÓDULO 2: Fabricación Aditiva Avanzada (Impresión 3D FDM) para Mecanismos (Marzo)",
            "sesiones": [
                {
                    "num": "Sesión 5",
                    "tema": "Cinemática de Mecanismos y Ciencia de Polímeros para FDM",
                    "objetivo": "Calcular y diseñar engranajes y transmisiones por banda sincrónica seleccionando el polímero técnico adecuado según esfuerzos dinámicos.",
                    "apertura": "Problema industrial: desgaste prematuro de piñones en maquinaria de empaque en Escuintla. Análisis comparativo de materiales plásticos industriales: PLA+, PETG, ABS, Nylon y TPU.",
                    "desarrollo": "Cálculo cinemático de módulo, paso circular y relación de transmisión ($i = Z_1 / Z_2$). Modelado CAD de engranes rectos de perfil involuta y poleas GT2. Análisis de arquitectura de impresoras 3D (CoreXY vs cartesiana) y tipos de extrusión.",
                    "cierre": "Revisión de perfiles de dientes generados en CAD. Registro en la bitácora Berichtsheft sobre propiedades de tracción y flexión de polímeros. Orden y limpieza 5S.",
                    "recursos": "Computadoras con CAD, muestras físicas de filamentos fracturados por tracción/impacto.",
                    "evaluacion": "Ensamble CAD de tren de engranajes con acoplamiento tangencial correcto."
                },
                {
                    "num": "Sesión 6",
                    "tema": "Diseño para Fabricación Aditiva (DFAM) y Parámetros del Laminador",
                    "objetivo": "Optimizar geometrías para impresión 3D orientando capas contra líneas de esfuerzo y parametrizando el software laminador industrial.",
                    "apertura": "Demostración de rotura por delaminación de capas en eje Z vs resistencia en plano X-Y (anisotropía). Regla de los 45° para voladizos sin soportes.",
                    "desarrollo": "Uso avanzado de software laminador (PrusaSlicer / Cura / Bambu Studio). Configuración de número de paredes/perímetros, capas sólidas superior/inferior y densidad/patrón de relleno estructural (giroide, cúbico). Generación de soportes orgánicos tipo árbol. Estimación de tiempos de impresión y consumo de filamento en gramos.",
                    "cierre": "Inspección de trayectorias en vista de capas previa a la impresión. Documentación en Berichtsheft de la relación entre densidad de relleno y resistencia mecánica.",
                    "recursos": "Software laminador, modelos STL de piezas mecánicas, computadoras de taller.",
                    "evaluacion": "Archivo G-code optimizado con cero desperdicio de material y orientación estructural ideal."
                },
                {
                    "num": "Sesión 7",
                    "tema": "Tolerancias Print-in-Place e Integración de Insertos Roscados",
                    "objetivo": "Calibrar impresoras 3D, fabricar mecanismos con holguras dinámicas ensamblados en cama e instalar insertos roscados de latón en caliente.",
                    "apertura": "Discusión sobre la debilidad de enroscar tornillos directamente en plástico en entornos con vibración industrial. Introducción al uso de insertos térmicos de latón (heat-set inserts).",
                    "desarrollo": "Nivelación de camas térmicas de la granja Kinal y calibración del Z-offset. Impresión de piezas con tolerancia dinámica de 0.2, 0.3 y 0.4 mm para probar articulaciones print-in-place. Uso de cautín termorregulado con punta especial para insertar insertos M3 y M4 en piezas impresas en PETG.",
                    "cierre": "Prueba de torque sobre insertos instalados: verificación de resistencia al barrido. Registro en Berichtsheft de las holguras mínimas efectivas para la máquina Kinal.",
                    "recursos": "Granja de impresoras 3D Kinal, filamento PETG, cautines con puntas de inserción, insertos de latón.",
                    "evaluacion": "Inserto térmico instalado perfectamente coaxial sin rebabas superficiales."
                },
                {
                    "num": "Sesión 8",
                    "tema": "Montaje de Subensambles Mecánicos y Evaluación Práctica del Módulo 2",
                    "objetivo": "Ensamblar, ajustar y evaluar una garra robótica articulada de dos dedos con engranes, insertos térmicos y soporte para servomotor.",
                    "apertura": "Presentación de los criterios de evaluación del Módulo 2: suavidad de movimiento, resistencia mecánica al agarre, estética de piezas impresas y tolerancia dimensional.",
                    "desarrollo": "Extracción y post-procesamiento de piezas impresas de la garra. Instalación de baleros en miniatura, pasadores de acero y tornillería métrica. Ensamble de cremallera y piñón actuador. Lubricación con grasa sintética para engranes plásticos y verificación de carrera completa.",
                    "cierre": "Evaluación individual mediante rúbrica analítica (≥ 75 pts). Prueba de agarre de objetos de diferentes geometrías (cilíndricos y prismáticos). Registro final de sesión en la bitácora.",
                    "recursos": "Piezas impresas en 3D, servomotores, tornillería M3, grasa de teflón, calibradores, rúbrica M2.",
                    "evaluacion": "Proyecto Práctico Módulo 2 evaluado con rúbrica técnica oficial (Aprobatorio ≥ 75 pts)."
                }
            ]
        },
        {
            "nombre": "MÓDULO 3: Mecanizado Sustractivo y Fresado CNC: CAM y Código G (Abril)",
            "sesiones": [
                {
                    "num": "Sesión 9",
                    "tema": "Cinemática CNC, Sistemas Coordenados y Estructura del Código G",
                    "objetivo": "Identificar los ejes de una fresadora CNC, interpretar la sintaxis de Código G/M y comprender los métodos de sujeción segura de material.",
                    "apertura": "Visita e inspección técnica del Router/Fresadora CNC de Kinal. Riesgos mecánicos de colisión de husillo a altas RPM. Concepto de sistemas de coordenadas: máquina (G53) vs pieza (G54).",
                    "desarrollo": "Análisis de comandos modales G: G00 (avance rápido), G01 (interpolación lineal con avance F), G02/G03 (interpolación circular) y comandos M (M03 giro de husillo, M05 paro, M08 refrigeración). Programación manual guiada de una trayectoria cuadrangular con arcos y simulación en PC.",
                    "cierre": "Detección de errores sintácticos en bloques de código. Registro en la bitácora de taller Berichtsheft sobre precauciones para evitar colisiones en eje Z.",
                    "recursos": "Router CNC Kinal, simulador de Código G en computadora, tableros de control.",
                    "evaluacion": "Programa manual de Código G simulado sin alertas de colisión ni errores sintácticos."
                },
                {
                    "num": "Sesión 10",
                    "tema": "Programación CAM: Estrategias de Desbaste, Acabado y Taladrado",
                    "objetivo": "Generar trayectorias CAM 2.5D seleccionando herramientas de corte, avances y velocidades acordes al material mecanizable.",
                    "apertura": "Física del corte de metales y polímeros: cálculo de velocidad de corte ($V_c$), avance por diente ($f_z$) y evacuación de viruta para evitar recalentamiento del cortador.",
                    "desarrollo": "Uso del software CAM (Fusion 360 CAM / VCarve). Definición de dimensiones de bloque bruto (stock). Creación de operaciones: 1) Planeado superior (Face), 2) Cajeras adaptativas (Adaptive Clearing) para vaciados de rodamientos, 3) Contorneado exterior 2D con pestañas de sujeción (tabs), 4) Taladrado ciclado (Peck Drilling). Post-procesamiento a Código G.",
                    "cierre": "Simulación cinemática en CAM con verificación de tiempo de ciclo y colisiones de vástago de herramienta. Registro de cálculos en bitácora Berichtsheft.",
                    "recursos": "Computadoras con módulo CAM, catálogos técnicos de herramientas de fresado de carburo.",
                    "evaluacion": "Archivo CAM post-procesado con parámetros validados según tipo de material."
                },
                {
                    "num": "Sesión 11",
                    "tema": "Alistamiento, Montaje de Herramientas y Puesta a Cero en CNC Kinal",
                    "objetivo": "Montar herramientas en boquillas ER, fijar material con bridas y establecer ceros de pieza (WCS) mediante sonda electrónica en la máquina CNC.",
                    "apertura": "Protocolo riguroso de seguridad antes de energizar CNC: parada de emergencia accesible, protección visual y auditiva obligatoria, comprobación de ausencia de llaves en husillo.",
                    "desarrollo": "Montaje de boquilla ER y fresa plana de carburo de 2 filos; comprobación de excentricidad (runout). Fijación mecánica de placa de Delrin/aluminio a la mesa de ranuras T con bridas y pernos. Conducción manual por jog de ejes. Determinación de origen X=0, Y=0 con palpador de bordes y calibración electrónica de Z=0 mediante sonda táctil.",
                    "cierre": "Comprobación de alturas de seguridad y prueba de simulación en el aire (Dry Run a Z +20 mm). Registro de coordenadas G54 en bitácora de taller. Orden y limpieza de virutas.",
                    "recursos": "Router CNC Kinal, boquillas ER, fresas de carburo, bridas de sujeción, sonda Z electrónica.",
                    "evaluacion": "Puesta a punto y ceros de pieza fijados en la máquina CNC con error dimensional < 0.05 mm."
                },
                {
                    "num": "Sesión 12",
                    "tema": "Mecanizado Práctico, Metrología de Verificación y Evaluación Módulo 3",
                    "objetivo": "Ejecutar el maquinado real de la bancada mecatrónica, verificar tolerancias geométricas con micrómetro y superar la evaluación del Módulo 3.",
                    "apertura": "Inicio de la jornada de evaluación práctica: revisión de condiciones de lubricación por niebla de aire y aspiración de viruta. Criterios de calidad y umbral mínimo de 75 puntos.",
                    "desarrollo": "Ejecución del fresado CNC de la bancada portante con cajeras para baleros y guías lineales. Monitoreo constante del sonido de corte y formación de viruta. Retiro de la pieza, desbarbado manual con raspador de bordes e inspección dimensional de cajeras con micrómetro de interiores.",
                    "cierre": "Calificación analítica individual con rúbrica oficial Kinal. Prueba de ensamble de rodamiento en la cajera mecanizada (ajuste de transición suave H7). Registro final en Berichtsheft.",
                    "recursos": "Router CNC, material de mecanizado (Delrin/aluminio), micrómetros, fresas, rúbrica M3.",
                    "evaluacion": "Proyecto Práctico Módulo 3 calificado con rúbrica analítica oficial (Aprobatorio ≥ 75 pts)."
                }
            ]
        },
        {
            "nombre": "MÓDULO 4: Sensórica Industrial, Actuación y Control de Ejes (Mayo)",
            "sesiones": [
                {
                    "num": "Sesión 13",
                    "tema": "Transducción, Sensores Industriales PNP/NPN y Acondicionamiento",
                    "objetivo": "Conectar, probar y calibrar sensores discretos industriales de 24 VDC identificando la lógica de conmutación de tres hilos.",
                    "apertura": "Falla común en industria guatemalteca: daño de entradas de PLC por cortocircuito al confundir conexiones PNP (sourcing) con NPN (sinking). Análisis de hoja técnica.",
                    "desarrollo": "Práctica de banco con multímetro y fuente de 24 VDC. Identificación de código de colores industrial: Café (+24V), Azul (0V) y Negro (Señal). Cableado y ensayo de detección de: 1) Sensores inductivos ante metales ferrosos y no ferrosos, 2) Sensores capacitivos para nivel de líquidos y polvos, 3) Sensores fotoeléctricos réflex con ajuste de sensibilidad.",
                    "cierre": "Verificación de histéresis de conmutación y conexionado de cargas a relevador de estado sólido. Registro en la bitácora Berichtsheft sobre diagramas de cableado PNP vs NPN.",
                    "recursos": "Fuentes conmutadas 24 VDC, sensores inductivos/capacitivos/ópticos, multímetros, relevadores.",
                    "evaluacion": "Circuito de detección multisensores operativo sin cortocircuitos ni inversión de polaridad."
                },
                {
                    "num": "Sesión 14",
                    "tema": "Control de Movimiento: Motores a Pasos, Drivers Industriales y Servos",
                    "objetivo": "Configurar drivers bipolares industriales (corriente y microstepping) y gobernar motores a pasos NEMA para control de posición preciso.",
                    "apertura": "Problema mecánico: pérdida de pasos y sobrecalentamiento de motores por ajuste erróneo de corriente en líneas automatizadas. Explicación de las curvas de torque-velocidad.",
                    "desarrollo": "Identificación de devanados en motores bipolares de 4 cables (fases A+, A-, B+, B-). Configuración de interruptores DIP en drivers industriales (tipo TB6600/DM542) para corriente nominal y microstepping (1/4, 1/8, 1/16). Cableado de señales lógicas de control: Pulso (PUL), Dirección (DIR) y Habilitación (ENA). Pruebas de movimiento con generador de pulsos.",
                    "cierre": "Medición de temperatura del motor en régimen estacionario y dinámico. Registro en Berichtsheft de la relación entre micropasos y resolución de desplazamiento en milímetros.",
                    "recursos": "Motores NEMA 17 y NEMA 23, drivers bipolares, fuentes 24 VDC, generadores de señal.",
                    "evaluacion": "Motor a pasos girando a velocidades controladas sin vibraciones excesivas ni pérdida de pasos."
                },
                {
                    "num": "Sesión 15",
                    "tema": "Actuación Electroneumática y Cableado Estético bajo Normas Kinal (IEC)",
                    "objetivo": "Conectar circuitos electroneumáticos y construir tableros de control estéticos aplicando ferrules, canaletas ranuradas y rotulado alfanumérico.",
                    "apertura": "El ideario Kinal del «trabajo bien hecho» en tableros eléctricos: prohibición de hilos desnudos sueltos. Importancia de la confiabilidad eléctrica para evitar paros no programados.",
                    "desarrollo": "Conexión de electroválvulas neumáticas 5/2 monoestables y biestables a cilindros de doble efecto con silenciadores y reguladores de flujo. Montaje de tablero sobre riel DIN: peinado de cables en canaleta ranurada plástica, uso de ponchadora con terminales tubulares aislados (ferrules), separación de potencia y control, y rotulado de cables según IEC 60617.",
                    "cierre": "Inspección estética y mecánica de tracción en terminales ponchados. Registro en la bitácora Berichtsheft sobre normas de codificación de planos eléctricos industriales.",
                    "recursos": "Electroválvulas 5/2, cilindros neumáticos, manguera PU, ferrules, ponchadora, canaleta, riel DIN.",
                    "evaluacion": "Tablero eléctrico canalizado con 100% de terminales en ferrules y rotulado alfanumérico."
                },
                {
                    "num": "Sesión 16",
                    "tema": "Programación de Perfiles de Movimiento y Evaluación Práctica Módulo 4",
                    "objetivo": "Programar rutinas de ciclo continuo para un eje lineal motorizado con rampas de velocidad y superar la evaluación práctica del Módulo 4.",
                    "apertura": "Inicio de la evaluación práctica del Módulo 4: integración de motor NEMA, husillo con tuerca antibacklash, driver industrial, sensores inductivos de home/límite y parada de emergencia.",
                    "desarrollo": "Programación de la secuencia de movimiento: 1) Rutina de homing al energizar, 2) Ciclo de vaivén automático entre posiciones programadas con rampas de aceleración suaves, 3) Interrupción inmediata y desenergización segura al oprimir botón de paro de emergencia.",
                    "cierre": "Evaluación formal con rúbrica analítica (≥ 75 pts). Verificación de repetibilidad dimensional del carro de transporte. Asignación de notas de módulo y retroalimentación técnica.",
                    "recursos": "Ejes lineales de prueba, motores a pasos, sensores de fin de carrera, botoneras, rúbrica M4.",
                    "evaluacion": "Proyecto Práctico Módulo 4 evaluado con rúbrica técnica oficial (Aprobatorio ≥ 75 pts)."
                }
            ]
        },
        {
            "nombre": "MÓDULO 5: Integración de Celda Mecatrónica y Proyecto Capstone Industrial (Junio)",
            "sesiones": [
                {
                    "num": "Sesión 17",
                    "tema": "Arquitectura de Integración Mecatrónica, Paneles HMI y Diagramas FSM",
                    "objetivo": "Diseñar la arquitectura integral de la mini-celda mecatrónica modelando la lógica mediante autómatas de estado finito y tableros de mando.",
                    "apertura": "Presentación del Proyecto Capstone Final: Mini-Celda Mecatrónica Automatizada de Clasificación y Manipulación para líneas de producción. Requerimientos de integración total.",
                    "desarrollo": "Diseño de diagramas de estados finitos (FSM) para coordinar: detección de pieza en tolva, avance del eje lineal mecanizado en CNC, sujeción con garra impresa en 3D, y conteo en panel de operador cortado en láser. Cableado de botonera industrial: Pulsador Verde (Start), Rojo (Stop), Selector Manual/Auto, Pilotos y Parada de Emergencia.",
                    "cierre": "Validación lógica del diagrama de estados en pizarra y simulación de contingencias. Registro de la arquitectura global en la bitácora de taller Berichtsheft.",
                    "recursos": "Controladores industriales/microcontroladores, botoneras de 22 mm, lámparas piloto, pizarra.",
                    "evaluacion": "Diagrama de flujo FSM completo que contempla todas las condiciones de falla y rearme."
                },
                {
                    "num": "Sesión 18",
                    "tema": "Ensamble Mecánico Integral y Cableado Definitivo de la Celda",
                    "objetivo": "Ensamblar los subsistemas mecánicos (CNC, 3D, Láser) y ejecutar el conexionado eléctrico definitivo con verificación de continuidad y aislamiento.",
                    "apertura": "Planificación del ensamble por estaciones de trabajo. Verificación de herramientas de precisión y repaso de normas de seguridad previas a la primera energización del sistema.",
                    "desarrollo": "Montaje de la bancada fresada en CNC sobre el chasis cortado en láser. Acoplamiento de la garra articulada impresa en 3D sobre el carro deslizante del eje motorizado. Tendido y fijación de cadenas portacables (drag chains). Cableado de señales de sensores y potencia de actuadores hacia el gabinete central. Verificación punto a punto con multímetro.",
                    "cierre": "Comprobación estática de ausencia de cortocircuitos a tierra y libre movimiento de mecanismos sin roce. Registro del avance de ensamble en la bitácora Berichtsheft.",
                    "recursos": "Todos los componentes manufacturados, tornillería, cadenas portacables, multímetros, banco.",
                    "evaluacion": "Estructura mecatrónica ensamblada con alineación mecánica rígida y cableado 100% verificado."
                },
                {
                    "num": "Sesión 19",
                    "tema": "Puesta en Marcha, Sincronización y Diagnóstico Sistemático (Troubleshooting)",
                    "objetivo": "Cargar el programa de control secuencial, calibrar tiempos de ciclo y ejecutar protocolos de localización y resolución de averías inducidas.",
                    "apertura": "Metodología de puesta en marcha industrial: pruebas en vacío (dry run), pruebas paso a paso y marcha automática continua. Protocolo de diagnóstico de fallas (troubleshooting).",
                    "desarrollo": "Carga de rutina secuencial. Calibración de sensibilidad en detección de piezas (metálicas vs no metálicas). Ajuste fino de tiempos de agarre y posicionamiento. Prueba de esfuerzo: simulación por el instructor de averías inducidas (sensor desalineado, corte de señal, atasco simulado); los aprendices aplican aislamiento lógico de fallas con multímetro.",
                    "cierre": "Optimización del tiempo de ciclo total de la celda. Documentación de las fallas resueltas y lecciones aprendidas en la bitácora Berichtsheft. Preparación para la evaluación terminal.",
                    "recursos": "Celda mecatrónica completa, instrumental de diagnóstico, cronómetro de planta.",
                    "evaluacion": "Resolución autónoma de una falla eléctrica/mecánica inducida en un tiempo inferior a 15 minutos."
                },
                {
                    "num": "Sesión 20",
                    "tema": "Evaluación Terminal Integrada (Capstone), Defensa Pública y Clausura",
                    "objetivo": "Demostrar la competencia mecatrónica integral mediante la operación autónoma y defensa técnica del Proyecto Capstone ante jurado evaluador.",
                    "apertura": "Instalación de las celdas mecatrónicas en el taller central de Kinal. Bienvenida al jurado evaluador (instructores y directivos técnicos). Explicación de la dinámica de defensa.",
                    "desarrollo": "Ejecución de la Evaluación Terminal Integrada (Theorie und Praxis integrierende Prüfung): cada estudiante/equipo opera su celda en ciclo continuo automático (mínimo 10 ciclos completos sin atasco ni intervención manual). Defensa técnica oral: justificación de selección de materiales, Código G utilizado, tolerancias y lógica de control. Respuesta a preguntas técnicas del jurado.",
                    "cierre": "Revisión final y firma oficial de la Bitácora de Taller (Berichtsheft). Deliberación de notas finales (umbral aprobatorio de 75 puntos). Acto de clausura, balance pedagógico institucional y felicitación a los participantes bajo el ideario de Kinal.",
                    "recursos": "Celdas mecatrónicas en operación, rúbrica terminal analítica, bitácoras de taller completas.",
                    "evaluacion": "Proyecto Capstone e informe técnico final evaluados y aprobados con nota ≥ 75 / 100 puntos."
                }
            ]
        }
    ]

    for mod in modulos_detalle:
        h2_mod = doc.add_paragraph()
        style_heading(h2_mod, mod["nombre"], level=2)

        for s in mod["sesiones"]:
            h3_ses = doc.add_paragraph()
            style_heading(h3_ses, f"{s['num']}: {s['tema']}", level=3)

            tbl_s = doc.add_table(rows=6, cols=2)
            tbl_s.alignment = WD_TABLE_ALIGNMENT.CENTER
            tbl_s.autofit = False
            tbl_s.columns[0].width = Inches(1.8)
            tbl_s.columns[1].width = Inches(4.7)
            set_table_borders(tbl_s, color="CBD5E0", sz="4")

            filas_s = [
                ("Objetivo de Aprendizaje:", s["objetivo"]),
                ("Momento 1: Apertura (30 min):", s["apertura"]),
                ("Momento 2: Desarrollo (210 min):", s["desarrollo"]),
                ("Momento 3: Cierre (30 min):", s["cierre"]),
                ("Recursos y Maquinaria:", s["recursos"]),
                ("Evidencia de Desempeño:", s["evaluacion"])
            ]

            for r_idx, (etq, txt) in enumerate(filas_s):
                row = tbl_s.rows[r_idx]
                set_cell_background(row.cells[0], "F7FAFC")
                set_cell_margins(row.cells[0], top=60, bottom=60, left=80, right=80)
                set_cell_margins(row.cells[1], top=60, bottom=60, left=80, right=80)

                p0 = row.cells[0].paragraphs[0]
                style_p(p0, space_before=0, space_after=0)
                r0 = p0.add_run(etq)
                r0.font.name = "Calibri"
                r0.font.size = Pt(8.5)
                r0.font.bold = True
                r0.font.color.rgb = COLOR_PRIMARY

                p1 = row.cells[1].paragraphs[0]
                style_p(p1, space_before=0, space_after=0)
                r1 = p1.add_run(txt)
                r1.font.name = "Calibri"
                r1.font.size = Pt(8.5)
                r1.font.color.rgb = COLOR_DARK
                if r_idx == 5:
                    r1.font.bold = True

            p_sp = doc.add_paragraph()
            style_p(p_sp, space_before=0, space_after=6)

    doc.add_page_break()

    # =========================================================================
    # 3. RÚBRICAS ANALÍTICAS DE EVALUACIÓN TÉCNICA INSTITUCIONAL (≥ 75 PUNTOS)
    # =========================================================================
    h1_3 = doc.add_paragraph()
    style_heading(h1_3, "3. Instrumentos y Rúbricas Analíticas de Evaluación (Normativa Kinal)", level=1)

    p_rub_desc = doc.add_paragraph()
    style_p(p_rub_desc, space_before=0, space_after=8)
    r = p_rub_desc.add_run("Toda evaluación práctica se califica sobre una escala de 100 puntos, donde la nota mínima de aprobación institucional es de 75 puntos. A continuación se detallan los criterios de la Rúbrica Analítica de Taller para Proyectos Mecatrónicos:")
    r.font.name = "Calibri"
    r.font.size = Pt(10.5)
    r.font.color.rgb = COLOR_DARK

    tbl_rub = doc.add_table(rows=6, cols=5)
    tbl_rub.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_rub.autofit = False
    tbl_rub.columns[0].width = Inches(1.5)
    tbl_rub.columns[1].width = Inches(1.2)
    tbl_rub.columns[2].width = Inches(1.3)
    tbl_rub.columns[3].width = Inches(1.3)
    tbl_rub.columns[4].width = Inches(1.2)
    set_table_borders(tbl_rub, color="CBD5E0", sz="4")

    # Header
    hdr_r = tbl_rub.rows[0]
    for c in hdr_r.cells:
        set_cell_background(c, "003366")
    headers_rub = ["Criterio Técnico Evaluado", "Excelente\n(90 - 100 pts)", "Muy Bueno\n(80 - 89 pts)", "Aprobado Mínimo\n(75 - 79 pts)", "No Aprobado\n(< 75 pts)"]
    for idx, text in enumerate(headers_rub):
        p = hdr_r.cells[idx].paragraphs[0]
        style_p(p, space_before=0, space_after=0)
        r = p.add_run(text)
        r.font.name = "Calibri"
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    criterios_rub = [
        ("Precisión Dimensional y Tolerancias Mecánicas\n(Peso: 25%)", 
         "Error dimensional < ±0.1 mm. Encajes perfectos sin holguras ni desalineación.", 
         "Error dimensional entre ±0.1 y ±0.2 mm. Ensamble suave con mínimo ajuste.", 
         "Error dimensional entre ±0.2 y ±0.3 mm. Requiere ajuste manual leve pero ensambla.", 
         "Error > ±0.4 mm. Piezas no encajan o quedan con holguras inaceptables."),
        
        ("Calidad de Acabados y «Trabajo Bien Hecho»\n(Peso: 25%)", 
         "Superficies limpias, sin quemaduras en láser ni rebabas en CNC. Piezas 3D sin hilos. Estética industrial sobresaliente.", 
         "Bordes limpios con desbarbado correcto. Piezas 3D uniformes y sin deformaciones térmicas visibles.", 
         "Acabado aceptable con marcas leves de maquinado o pequeñas rebabas no críticas corregidas en taller.", 
         "Piezas sucias, quemadas, con rebabas cortantes o defectos graves de impresión/corte."),
        
        ("Integración Operativa y Funcionamiento\n(Peso: 25%)", 
         "Movimiento suave, cinemática 100% coordinada, cero atascos en 10 ciclos continuos. Detección impecable de sensores.", 
         "Ciclo continuo completado satisfactoriamente con mínimas vibraciones mecánicas.", 
         "El mecanismo opera y cumple la función pero presenta pequeñas fluctuaciones de velocidad o vibración.", 
         "El mecanismo se traba, no responde a la lógica programada o presenta colisión mecánica."),
        
        ("Seguridad, Cableado IEC y Orden 5S\n(Peso: 15%)", 
         "100% casquillos ferrules aislados, rotulado alfanumérico, canaleta cerrada, uso impecable de EPP y puesto de trabajo pulcro.", 
         "Cableado ordenado con ferrules y canalización correcta. Respeto permanente a las normas de seguridad y EPP.", 
         "Cableado funcional pero con rotulado incompleto o desorden menor en canaleta corregido durante la sesión.", 
         "Conductores desnudos sueltos, omisión de EPP, desorden grave en taller o violación de protocolos LOTO."),
        
        ("Bitácora de Taller (Berichtsheft)\n(Peso: 10%)", 
         "Memoria técnica completa, diagramas eléctricos normados, cálculos cinemáticos y firma al día con pulcritud.", 
         "Registro técnico claro con esquemas de conexión y descripciones precisas de las actividades prácticas.", 
         "Registro con datos esenciales y diagramas básicos pero con redacción esquemática mínima.", 
         "Bitácora incompleta, sin diagramas técnicos, con atrasos de registro o datos erróneos.")
    ]

    for idx, (crit, exc, mb, ap, nap) in enumerate(criterios_rub, start=1):
        row = tbl_rub.rows[idx]
        if idx % 2 == 1:
            for c in row.cells:
                set_cell_background(c, "F7FAFC")
        for c_idx, val in enumerate([crit, exc, mb, ap, nap]):
            cell = row.cells[c_idx]
            set_cell_margins(cell, top=60, bottom=60, left=70, right=70)
            p = cell.paragraphs[0]
            style_p(p, space_before=0, space_after=0)
            r = p.add_run(val)
            r.font.name = "Calibri"
            r.font.size = Pt(8)
            r.font.color.rgb = COLOR_DARK
            if c_idx == 0:
                r.font.bold = True

    # =========================================================================
    # 4. FORMATO GUÍA DE LA BITÁCORA DE TALLER DEL APRENDIZ (BERICHTSHEFT)
    # =========================================================================
    h1_4 = doc.add_paragraph()
    style_heading(h1_4, "4. Formato Guía de la Bitácora de Taller del Aprendiz (Berichtsheft)", level=1)

    p_ber_desc = doc.add_paragraph()
    style_p(p_ber_desc, space_before=0, space_after=8)
    r = p_ber_desc.add_run("En concordancia con el Sistema Dual de Formación en Alternancia y la normativa de Fundación Kinal, el aprendiz debe registrar obligatoriamente cada sábado el desarrollo de sus actividades técnicas en su Bitácora de Taller (Berichtsheft):")
    r.font.name = "Calibri"
    r.font.size = Pt(10.5)
    r.font.color.rgb = COLOR_DARK

    tbl_b_fmt = doc.add_table(rows=7, cols=2)
    tbl_b_fmt.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_b_fmt.autofit = False
    tbl_b_fmt.columns[0].width = Inches(2.2)
    tbl_b_fmt.columns[1].width = Inches(4.3)
    set_table_borders(tbl_b_fmt, color="CBD5E0", sz="4")

    formato_data = [
        ("Nombre del Estudiante y Carné:", "___________________________________________________________"),
        ("Sesión Sabatina y Fecha:", "Sesión No. _____  |  Fecha: _____ / _____ / 2026"),
        ("Módulo Formativo y Máquinas Usadas:", "[ ] Cortadora Láser   [ ] Impresora 3D   [ ] Router CNC   [ ] Banco Automatización"),
        ("Parámetros Técnicos y Mediciones:", "Velocidades, potencias, espesores, tolerancias obtenidas, herramientas usadas."),
        ("Descripción de Actividades Realizadas:", "Detalle secuencial de preparación, manufactura, cableado y programación."),
        ("Dificultades y Solución («Trabajo Bien Hecho»):", "Registro de averías o fallas presentadas y método técnico aplicado para resolverlas."),
        ("Firma del Estudiante y Vo.Bo. del Instructor:", "Firma Estudiante: ___________________  |  Firma Instructor: ___________________")
    ]

    for idx, (campo, lineas) in enumerate(formato_data):
        row = tbl_b_fmt.rows[idx]
        set_cell_background(row.cells[0], "F7FAFC")
        set_cell_margins(row.cells[0], top=60, bottom=60, left=80, right=80)
        set_cell_margins(row.cells[1], top=60, bottom=60, left=80, right=80)

        p0 = row.cells[0].paragraphs[0]
        style_p(p0, space_before=0, space_after=0)
        r0 = p0.add_run(campo)
        r0.font.name = "Calibri"
        r0.font.size = Pt(9)
        r0.font.bold = True
        r0.font.color.rgb = COLOR_PRIMARY

        p1 = row.cells[1].paragraphs[0]
        style_p(p1, space_before=0, space_after=0)
        r1 = p1.add_run(lineas)
        r1.font.name = "Calibri"
        r1.font.size = Pt(9)
        r1.font.color.rgb = COLOR_DARK

    # Footer
    section = doc.sections[0]
    footer = section.footer
    footer_p = footer.paragraphs[0]
    style_p(footer_p, space_before=0, space_after=0)
    footer_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run_f = footer_p.add_run("Fundación Kinal | Dosificación y Secuencia Didáctica Oficial — Mecatrónica Industrial")
    run_f.font.name = "Calibri"
    run_f.font.size = Pt(9)
    run_f.font.color.rgb = COLOR_SECONDARY

    out_dir = os.path.join("Cursos", "Mecatrónica")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "Dosificacion_y_Secuencia_Didactica_Mecatronica_Kinal.docx")
    doc.save(out_path)
    print(f"Dosificación guardada con éxito en: {out_path}")

if __name__ == "__main__":
    generate_dosificacion()
