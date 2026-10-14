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

def set_cell_margins(cell, top=70, bottom=70, left=90, right=90):
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

def style_p(p, space_before=0, space_after=6, line_spacing=1.15):
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = line_spacing

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

def generate_temario_doc():
    doc = docx.Document()

    for section in doc.sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)

    COLOR_PRIMARY = RGBColor(0, 51, 102)      # Azul Kinal
    COLOR_SECONDARY = RGBColor(74, 85, 104)    # Gris pizarra
    COLOR_DARK = RGBColor(26, 32, 44)         # Texto oscuro

    # ==========================================
    # ENCABEZADO INSTITUCIONAL
    # ==========================================
    title_p = doc.add_paragraph()
    style_p(title_p, space_before=0, space_after=6)
    run_title = title_p.add_run("Cableado Estructurado y Redes de Cobre y Fibra Óptica")
    run_title.font.name = "Calibri"
    run_title.font.size = Pt(20)
    run_title.font.bold = True
    run_title.font.color.rgb = COLOR_PRIMARY

    sub_p = doc.add_paragraph()
    style_p(sub_p, space_before=0, space_after=14)
    run_sub = sub_p.add_run("Programa Oficial de Formación y Temario Analítico Detallado  |  Duración: 80 Horas Formativas  |  20 Sesiones\nFundación Kinal — Escuela Técnica Superior | Nivel DQR 4 - 5 | Umbral Aprobatorio: 75/100 Puntos")
    run_sub.font.name = "Calibri"
    run_sub.font.size = Pt(11)
    run_sub.font.italic = True
    run_sub.font.color.rgb = COLOR_SECONDARY

    add_callout(doc, 
        "«the ability and readiness of the individual to use knowledge, skills and personal, social and methodological competences and to behave in a considered, individual and socially responsible manner. Competence is understood in this sense as the comprehensive ability to act». Este programa técnico garantiza el desarrollo de la competencia integral para ejecutar obras de telecomunicaciones de alta velocidad con apego absoluto a la física de transmisión, estética profesional («trabajo bien hecho») y estándares internacionales ANSI/TIA, ISO/IEC y NFPA.", 
        bold_prefix="Definición de Competencia DQR e Ideario Kinal:")

    # ==========================================
    # 1. OBJETIVOS FORMATIVOS Y COMPETENCIAS
    # ==========================================
    h1_1 = doc.add_paragraph()
    style_heading(h1_1, "1. Competencia General y Resultados de Aprendizaje por Módulo", level=1)

    p_cg = doc.add_paragraph()
    style_p(p_cg, space_before=0, space_after=6)
    r = p_cg.add_run("Competencia General del Programa:\n"
                     "El participante planifica, canaliza, tiende, remata, fusiona y certifica sistemas de cableado estructurado en cobre (Cat 6 / Cat 6A) y fibra óptica (Monomodo OS2 / Multimodo OM4), ejecutando el montaje pulcro de racks de 19 pulgadas y cuartos de telecomunicaciones, aterrizaje equipotencial bajo TIA-607, administración documental bajo TIA-606 y diagnóstico instrumental de enlaces con escáneres Fluke Networks, garantizando cero fallas de paradiafonía y cumplimiento del estándar institucional del trabajo bien hecho.")
    r.font.name = "Calibri"
    r.font.size = Pt(10)
    r.font.bold = True
    r.font.color.rgb = COLOR_PRIMARY

    mod_comps = [
        ("Módulo 1: Normas ANSI/TIA, Espacios y Canalizaciones Físicas", 
         "Calcula factores de ocupación de tuberías y charolas portacables según ANSI/TIA-569 y realiza el montaje mecánico y nivelación de racks de 19 pulgadas con distribución equilibrada de carga."),
        ("Módulo 2: Cableado de Cobre de Alto Rendimiento (Cat 6/6A) y Aterrizaje TIA-607", 
         "Conectoriza tomas de pared y patch panels de 24 puertos en Cat 6A con técnica de mínimo destrenzado (< 13 mm), peinado simétrico con cinchos de velcro e interconexión de barra TGB a tierra."),
        ("Módulo 3: Infraestructura de Fibra Óptica, Conectorización y Empalme por Fusión", 
         "Prepara, corta y empalma por fusión fibras ópticas monomodo y multimodo con fusionadora automática, logrando pérdidas inferiores a 0.05 dB y alojando acopladores LC/SC en bandejas ODF sin exceder radios de curvatura."),
        ("Módulo 4: Certificación Instrumental con Fluke, Rotulado TIA-606 y Proyecto As-Built", 
         "Ejecuta la certificación Tier 1 de enlaces permanentes con escáner Fluke Networks, diagnostica fallas de NEXT y Return Loss por reflectometría, rotula bajo TIA-606 y genera la carpeta técnica As-Built.")
    ]

    for m_tit, m_desc in mod_comps:
        p_m = doc.add_paragraph()
        style_p(p_m, space_before=2, space_after=4)
        p_m.paragraph_format.left_indent = Inches(0.2)
        r_b = p_m.add_run(f"• {m_tit}: ")
        r_b.font.name = "Calibri"
        r_b.font.size = Pt(9.5)
        r_b.font.bold = True
        r_b.font.color.rgb = COLOR_PRIMARY
        r_d = p_m.add_run(m_desc)
        r_d.font.name = "Calibri"
        r_d.font.size = Pt(9.5)
        r_d.font.color.rgb = COLOR_DARK

    # ==========================================
    # 2. TEMARIO ANALÍTICO DETALLADO POR MÓDULOS
    # ==========================================
    h1_2 = doc.add_paragraph()
    style_heading(h1_2, "2. Temario Analítico Jerárquico y Prácticas de Laboratorio", level=1)

    # -------------------------------------------------------------
    # MODULO 1
    # -------------------------------------------------------------
    h2_m1 = doc.add_paragraph()
    style_heading(h2_m1, "MÓDULO 1: NORMAS ANSI/TIA, ESPACIOS Y CANALIZACIONES FÍSICAS (TR, ER, RACKS) (20 Horas)", level=2)

    temas_m1 = [
        ("1.1 Normativa Internacional y Subsistemas del Cableado Estructurado", [
            "Evolución y alcance de los estándares: ANSI/TIA-568.0-E, TIA-568.1-E e ISO/IEC 11801.",
            "Concepto de cableado genérico e independencia de fabricantes y protocolos.",
            "Los 6 subsistemas fundamentales: Área de Trabajo (WA), Cableado Horizontal, Cableado de Backbone (Vertical), Cuarto de Telecomunicaciones (TR), Cuarto de Equipos (ER) y Entrada de Servicios (EF).",
            "Topología física en estrella jerárquica: distribución principal (MDF), distribución intermedia (IDF) y límites de distancia."
        ]),
        ("1.2 Espacios de Telecomunicaciones según ANSI/TIA-569-E", [
            "Requerimientos ambientales del TR y ER: climatización (HVAC), temperatura (18°C a 24°C), humedad relativa (30% a 55%) e iluminación sin sombra.",
            "Seguridad física: cerraduras de control de acceso, puertas batientes hacia afuera y pisos con tratamiento antiestático (ESD).",
            "Paredes tratadas con madera contrachapada de 3/4 pulgada con retardante de llama (pintura ignífuga) para montaje de equipos.",
            "Alimentación eléctrica regulada: circuitos dedicados para racks, tomacorrientes NEMA 5-20R y sistemas UPS de respaldo."
        ]),
        ("1.3 Canalizaciones Físicas y Bandejas Portacables", [
            "Tipos de canalizaciones horizontales: tubería conduit metálica EMT, charolas portacables tipo malla (canastilla) y canaletas perimetrales.",
            "Cálculo de factor de llenado de canalizaciones: regla del 40% inicial para permitir un 60% en expansiones futuras según TIA-569.",
            "Radios de curvatura en ductos: curvado de tubería EMT con doblador manual sin estrangular la sección transversal.",
            "Distancias de separación obligatorias entre cableado de telecomunicaciones y líneas de fuerza eléctrica (NFPA 70 / NEC) para mitigar EMI."
        ]),
        ("1.4 Bastidores de 19 Pulgadas y Organización de Gabinetes", [
            "Especificaciones mecánicas de racks según EIA-310-D: ancho de 19 pulgadas y Unidad de Rack (1U = 1.75 pulgadas / 44.45 mm).",
            "Diferencias de uso: Racks abiertos de piso (42U) para centros de cableado central vs Gabinetes de pared abatibles (9U a 12U) para IDFs de planta.",
            "Nivelación, aplomado y anclaje antisísmico al piso de concreto mediante taquetes expansivos.",
            "Distribución vertical del equipamiento: organizadores horizontales (1U/2U) tipo pasahilos y ductos verticales con dedos plásticos para ruteo ordenado."
        ]),
        ("1.5 Prácticas de Taller y Ensamble Mecánico", [
            "Práctica 1.1: Levantamiento de requerimientos y cálculo de tubería EMT para 24 puntos de red de oficina abierta.",
            "Práctica 1.2: Doblado manual de tubería conduit EMT de 3/4'' (curvas a 90° y monturas de salto) y fijación con abrazaderas tipo uña.",
            "Práctica 1.3: Armado, escuadrado, nivelación con nivel de burbuja y fijación mecánica de un rack abierto de 19'' (42U).",
            "Práctica 1.4: Instalación de charola tipo malla aérea con soportes trapecio y bajadas suaves en cascada hacia el bastidor.",
            "Práctica 1.5: Montaje de gabinete de pared abatible con organizadores y simulación de distribución de switches y patch panels."
        ])
    ]

    for sub_tit, sub_items in temas_m1:
        p_st = doc.add_paragraph()
        style_heading(p_st, sub_tit, level=3)
        for it in sub_items:
            p_it = doc.add_paragraph()
            style_p(p_it, space_before=1, space_after=2)
            p_it.paragraph_format.left_indent = Inches(0.25)
            r_b = p_it.add_run("• ")
            r_b.font.bold = True
            r_b.font.color.rgb = COLOR_PRIMARY
            r_txt = p_it.add_run(it)
            r_txt.font.name = "Calibri"
            r_txt.font.size = Pt(9.5)
            r_txt.font.color.rgb = COLOR_DARK

    # -------------------------------------------------------------
    # MODULO 2
    # -------------------------------------------------------------
    h2_m2 = doc.add_paragraph()
    style_heading(h2_m2, "MÓDULO 2: CABLEADO DE COBRE DE ALTO RENDIMIENTO (CAT 6 / CAT 6A) Y ATERRIZAJE TIA-607 (20 Horas)", level=2)

    temas_m2 = [
        ("2.1 Física del Par Trenzado Balanceado y Especificaciones ANSI/TIA-568.2-D", [
            "Estructura del cable de 4 pares: código de colores estándar (Blanco-Azul/Azul, Blanco-Naranja/Naranja, Blanco-Verde/Verde, Blanco-Marrón/Marrón).",
            "Principio de transmisión diferencial y rechazo en modo común; relación de pasos de torsión distintos por cada par.",
            "Comparativa de categorías: Cat 5e (100 MHz), Cat 6 (250 MHz) y Cat 6A (500 MHz / 10 Gbps a 100 metros).",
            "Construcción y apantallamiento: U/UTP (sin blindaje), F/UTP (pantalla general de lámina de aluminio) y S/FTP (malla general y pares apantallados).",
            "Conductores sólidos (AWG 23 para tendido horizontal permanente) vs conductores multifilares (AWG 24/26 flexibles para patch cords)."
        ]),
        ("2.2 Técnicas de Conectorización y Esquemas de Cableado T568A / T568B", [
            "Asignación de pines en conector RJ45 de 8 contactos según T568A y T568B; regla de consistencia en todo el proyecto.",
            "Conectorización de tomas de pared: módulos hembra tipo Keystone Jack Cat 6 y Cat 6A apantallados.",
            "Técnica de remate con herramienta de impacto (punch down tool) con cuchilla 110/Krone en un solo golpe limpio.",
            "Regla de oro del destrenzado: no desparear los conductores más de 0.5 pulgadas (13 mm) para evitar la degradación de NEXT.",
            "Uso de faceplates angulados y planos con ventanas de identificación y tapas guardapolvo."
        ]),
        ("2.3 Armado de Patch Panels y Gestión de Peinado en Rack", [
            "Estructura de patch panels de 24 y 48 puertos de 1U y 2U (modulares con jacks individuales vs bloques PCB fijos).",
            "Desforre de la chaqueta exterior sin marcar el aislamiento de los pares mediante peladores rotativos.",
            "Peinado prolijo en mazos simétricos de 12 o 24 cables con barras de alivio de tensión posteriores.",
            "Uso obligatorio de cinchos textiles de velcro (hook-and-loop): sujeción firme sin estrangular ni deformar la geometría del cable.",
            "Construcción y prueba de latiguillos de parcheo (patch cords) de precisión para verificación de canal."
        ]),
        ("2.4 Sistema de Puesta a Tierra y Unión para Telecomunicaciones (ANSI/TIA-607-D)", [
            "Propósito de la puesta a tierra en telecomunicaciones: equipotencialidad, disipación de descargas electrostáticas y drenaje de ruido EMI.",
            "Componentes del sistema: Barra Principal (TMGB), Barras Secundarias de Cuarto (TGB) y Barra de Puesta a Tierra del Rack (RGB).",
            "Conductor de unión de telecomunicaciones (BCT): cable de cobre estañado o aislado verde calibre 6 AWG.",
            "Aterrizaje de pantallas de cables F/UTP a través de patch panels apantallados y verificación de continuidad con multímetro (< 0.1 ohm)."
        ]),
        ("2.5 Alimentación Remota PoE++ (IEEE 802.3bt) y Calidad de Materiales", [
            "Estándares PoE: PoE (802.3af - 15.4W), PoE+ (802.3at - 30W) y PoE++ Tipo 3/4 (802.3bt - 60W y 90W sobre los 4 pares).",
            "Fenómeno térmico de disipación de calor ($I^2R$) en mazos de cables densos y reducción de la longitud máxima del canal.",
            "Riesgos del cable fraudulento CCA (aluminio cobrizado): alto sobrecalentamiento, riesgo de incendio y fatiga mecánica por fractura.",
            "Criterios de selección de cable 100% cobre electrolítico virgen con clasificación contra fuego (CMR Riser / CMP Plenum / LSZH)."
        ]),
        ("2.6 Prácticas de Taller y Ensamble de Cobre", [
            "Práctica 2.1: Conectorización de 4 módulos Keystone Jack Cat 6A bajo esquema T568B con verificación de destrenzado < 13 mm.",
            "Práctica 2.2: Armado y remate completo de un Patch Panel modular Cat 6A de 24 puertos con barra trasera de soporte.",
            "Práctica 2.3: Peinado estético de mazo de 24 cables en rack utilizando peines guía y sujeción exclusiva con velcro.",
            "Práctica 2.4: Instalación de barra TGB en rack de 19'' y conexionado equipotencial del bastidor con cable verde 6 AWG.",
            "Práctica 2.5: Prueba de continuidad y wiremap con comprobador digital verificando ausencia de pares divididos (split pairs)."
        ])
    ]

    for sub_tit, sub_items in temas_m2:
        p_st = doc.add_paragraph()
        style_heading(p_st, sub_tit, level=3)
        for it in sub_items:
            p_it = doc.add_paragraph()
            style_p(p_it, space_before=1, space_after=2)
            p_it.paragraph_format.left_indent = Inches(0.25)
            r_b = p_it.add_run("• ")
            r_b.font.bold = True
            r_b.font.color.rgb = COLOR_PRIMARY
            r_txt = p_it.add_run(it)
            r_txt.font.name = "Calibri"
            r_txt.font.size = Pt(9.5)
            r_txt.font.color.rgb = COLOR_DARK

    # -------------------------------------------------------------
    # MODULO 3
    # -------------------------------------------------------------
    h2_m3 = doc.add_paragraph()
    style_heading(h2_m3, "MÓDULO 3: INFRAESTRUCTURA DE FIBRA ÓPTICA, CONECTORIZACIÓN Y EMPALME POR FUSIÓN (20 Horas)", level=2)

    temas_m3 = [
        ("3.1 Principios de Transmisión Óptica y Tipos de Fibra (ANSI/TIA-568.3-D)", [
            "Naturaleza de la luz, índice de refracción, ley de Snell y principio de reflexión interna total.",
            "Estructura geométrica de la fibra óptica: núcleo de sílice dopado, revestimiento (*cladding* de 125 $\mu$m) y recubrimiento primario de acrilato (250 $\mu$m).",
            "Fibra Monomodo (SMF - OS1/OS2): núcleo de 9 $\mu$m, propagación de un único modo de luz, longitudes de onda de 1310 nm y 1550 nm para distancias de campus y metropolitanas.",
            "Fibra Multimodo (MMF - OM3/OM4/OM5): núcleo de 50 $\mu$m, índice graduado, optimizada para fuentes láser VCSEL a 850 nm y 1300 nm en backbones de edificio y Data Centers.",
            "Atenuación intrínseca: absorción, dispersión de Rayleigh y pérdidas por macro y microcurvatura."
        ]),
        ("3.2 Tipos Constructivos de Cables Ópticos", [
            "Cables de estructura ajustada (*tight buffer* de 900 $\mu$m): flexibles, ideales para distribución interna y conectorización directa en cuartos de telecomunicaciones.",
            "Cables de tubo holgado (*loose tube*): tubos de PBT con gel hidrófugo bloqueador de agua o hilos hinchables para tendidos exteriores en ducto o aéreo con fiador de acero/dieléctrico.",
            "Cables armados con cinta de acero corrugado para enterramiento directo y protección contra roedores.",
            "Cables dieléctricos autosoportados (ADSS) para vanos aéreos entre postes sin contacto con alta tensión."
        ]),
        ("3.3 Conectores Ópticos, Pulidos y Acopladores", [
            "Morfología de conectores estándar: LC (conector de factor de forma pequeño de 1.25 mm), SC (conector push-pull de 2.5 mm), ST y conectores multifibra MPO/MTP de 12 y 24 fibras.",
            "Tipos de pulido de la férula de cerámica zirconia: PC (*Physical Contact*), UPC (*Ultra Physical Contact* - color azul) con pérdida de retorno > -50 dB y APC (*Angled Physical Contact* a 8° - color verde) con pérdida de retorno > -65 dB.",
            "Inspección microscópica de caras terminales: estándar IEC 61300-3-35 para detección de rayaduras, picaduras y partículas de polvo.",
            "Limpieza profesional: plumas limpiadoras de un solo clic (*one-click cleaners*) y toallitas secas sin pelusa con disolvente óptico especializado."
        ]),
        ("3.4 Proceso de Empalme por Fusión con Arco Voltaico", [
            "Herramental de precisión: peladora de fibra de 3 muescas (chaqueta, búfer 900 $\mu$m y acrilato 250 $\mu$m), tijeras para Kevlar y cortadora de diamante (*cleaver*).",
            "Técnica de corte de precisión: importancia del ángulo de corte perpendicular (< 1° respecto al eje longitudinal).",
            "Principio de la fusionadora automática: alineación por ranura en V (*V-groove*) vs alineación por núcleo PAS (*Profile Alignment System*).",
            "Parámetros de fusión: arco de limpieza, electrodos de tungsteno, descarga principal de fusión y estimación automática de pérdida en dB (máx. 0.05 dB permitido).",
            "Protección del empalme: manguito termo-contráctil (*fusen*) con varilla de acero inoxidable y ciclo de contracción en el horno térmico integrado."
        ]),
        ("3.5 Bandejas Distribuidoras ODF y Normas de Bioseguridad", [
            "Bandejas de distribución óptica (ODF / Patch Panels de Fibra) de 1U: organización de casetes de empalme, peinado de pigtails y radios de curvatura mínimos (30 mm).",
            "Manejo seguro de residuos de fibra: uso obligatorio de contenedor hermético de eliminación; peligro letal de ingestión o incrustación en piel y ojos.",
            "Seguridad láser: no mirar directamente al extremo de conectores o fibras activas (la luz invisible de 1310/1550 nm produce quemaduras irreversibles en la retina).",
            "Verificación visual rápida de continuidad e identificación de fibras rotas con lápiz de luz roja (VFL de 650 nm)."
        ]),
        ("3.6 Prácticas de Taller y Fusión Óptica", [
            "Práctica 3.1: Deschaquetado seguro de cable óptico de 6 hilos, retiro de armadura y limpieza de gel con disolvente cítrico.",
            "Práctica 3.2: Práctica intensiva de pelado y corte con cleaver de precisión, verificando ángulos en pantalla de la fusionadora.",
            "Práctica 3.3: Ejecución de 4 empalmes por fusión entre fibras monomodo OS2 y pigtails LC con atenuación estimada < 0.03 dB.",
            "Práctica 3.4: Horneado de manguitos termo-retráctiles y acomodo ordenado en el casete de empalme respetando radios de curvatura.",
            "Práctica 3.5: Montaje de bandeja ODF de 1U con acopladores dúplex LC y prueba de continuidad visual con VFL."
        ])
    ]

    for sub_tit, sub_items in temas_m3:
        p_st = doc.add_paragraph()
        style_heading(p_st, sub_tit, level=3)
        for it in sub_items:
            p_it = doc.add_paragraph()
            style_p(p_it, space_before=1, space_after=2)
            p_it.paragraph_format.left_indent = Inches(0.25)
            r_b = p_it.add_run("• ")
            r_b.font.bold = True
            r_b.font.color.rgb = COLOR_PRIMARY
            r_txt = p_it.add_run(it)
            r_txt.font.name = "Calibri"
            r_txt.font.size = Pt(9.5)
            r_txt.font.color.rgb = COLOR_DARK

    # -------------------------------------------------------------
    # MODULO 4
    # -------------------------------------------------------------
    h2_m4 = doc.add_paragraph()
    style_heading(h2_m4, "MÓDULO 4: CERTIFICACIÓN INSTRUMENTAL CON FLUKE, ROTULADO TIA-606 Y PROYECTO AS-BUILT (20 Horas)", level=2)

    temas_m4 = [
        ("4.1 Certificación Tier 1 de Cobre con Escáner Fluke Networks", [
            "Diferencias técnicas entre Comprobación de Continuidad (Wiremap), Calificación de Ancho de Banda y **Certificación de Enlace**.",
            "Topologías de prueba estandarizadas: Enlace Permanente (*Permanent Link* máx. 90 m sin patch cords) vs Canal (*Channel* máx. 100 m incluyendo patch cords).",
            "Arquitectura del certificador Fluke Networks (DSX-5000 / DSX-8000): unidad principal (Main) y unidad remota (Remote).",
            "Configuración del proyecto en software: selección del estándar de prueba (TIA Cat 6A Permanent Link), tipo de cable y valor NVP (*Nominal Velocity of Propagation*)."
        ]),
        ("4.2 Análisis e Interpretación de Parámetros de Alta Frecuencia", [
            "Mapa de cableado (*Wiremap*): detección gráfica de pares abiertos, cortocircuitos, pares invertidos, pares cruzados y pares divididos (*split pairs*).",
            "Longitud física vs eléctrica y retardo de propagación (*Propagation Delay* y *Delay Skew*).",
            "Resistencia de bucle en corriente continua (DC Loop Resistance) y desbalance de resistencia para PoE++.",
            "Pérdida de Inserción (*Insertion Loss* / Atenuación): causas de falla por longitud excesiva o cable CCA de baja calidad.",
            "Paradiafonía en el extremo cercano (*NEXT* y *PS-NEXT*): causas de falla por destrenzado excesivo en el conector o daño mecánico.",
            "Pérdida de Retorno (*Return Loss*): reflejo de energía por cambios bruscos de impedancia característica debidos a aplastamiento con cinchos plásticos o dobleces agudos.",
            "Uso de herramientas de diagnóstico avanzado: reflectometría de dominio de tiempo para NEXT (TDNXT) y fallas de impedancia (TDR)."
        ]),
        ("4.3 Certificación Óptica Básica (Tier 1) de Enlaces de Fibra", [
            "Método de prueba con Fuente de Luz y Medidor de Potencia Óptica (LSPM / OPM) según TIA-526-14 / TIA-526-7.",
            "Establecimiento de referencia óptica: métodos de 1 puente, 2 puentes y 3 puentes de referencia (jumper cords de prueba de grado referencia).",
            "Cálculo del presupuesto de pérdida óptica admisible (*Optical Loss Budget*): atenuación de la fibra (dB/km) + atenuación de conectores (0.75 dB por par acoplado) + atenuación de empalmes (0.3 dB por fusión).",
            "Medición de pérdida de inserción total en dB en ambas direcciones y comparación frente al límite normado."
        ]),
        ("4.4 Administración y Rotulado Normalizado según ANSI/TIA-606-D", [
            "Clases de administración (Clase 1 para un solo TR hasta Clase 4 para campus multiedificio).",
            "Formato de nomenclatura alfanumérica estructurada: identificador de edificio, piso, cuarto de telecomunicaciones, rack, patch panel y puerto (ej. `1A-TR1-PP01-01` a `1A-WA01-01`).",
            "Código de colores opcional para campos de parcheo: azul para datos de usuario, blanco para primer nivel de backbone, verde para conexiones de red externa.",
            "Uso de rotuladoras industriales de transferencia térmica con etiquetas autolaminadas de vinil para cables y etiquetas de poliéster para faceplates y paneles."
        ]),
        ("4.5 Dossier Técnico As-Built y Garantía Extendida del Fabricante", [
            "Estructura formal de la carpeta de entrega técnica «As-Built» para entrega al cliente final.",
            "Planos arquitectónicos de planta con simbología normalizada de tomas de datos, rutas de canalización y ubicación de gabinetes.",
            "Tablas de interconexión y registros de parcheo (*Patching Schedule*).",
            "Gestión de reportes con el software Fluke LinkWare: exportación de certificados individuales en PDF y archivo de base de datos `.flw` para trámite de garantía de 25 años ante fabricantes."
        ]),
        ("4.6 Prácticas de Taller y Examen Práctico de Certificación", [
            "Práctica 4.1: Calibración y configuración completa de un equipo Fluke DSX para enlace permanente Cat 6A.",
            "Práctica 4.2: Certificación instrumental de los 24 enlaces del patch panel con guardado y exportación en LinkWare.",
            "Práctica 4.3: Certificación Tier 1 de enlace troncal de fibra óptica con OPM y fuente de luz calibrada.",
            "Práctica 4.4: Taller de Troubleshooting: diagnóstico y resolución de 3 enlaces fallidos inducidos por el docente (NEXT alto, par dividido y pérdida de retorno).",
            "Práctica 4.5: EXAMEN TERMINAL PRÁCTICO INDIVIDUAL: Certificación completa de un rack departamental, rotulado bajo TIA-606 y entrega del dossier As-Built (Umbral aprobatorio: 75/100 puntos)."
        ])
    ]

    for sub_tit, sub_items in temas_m4:
        p_st = doc.add_paragraph()
        style_heading(p_st, sub_tit, level=3)
        for it in sub_items:
            p_it = doc.add_paragraph()
            style_p(p_it, space_before=1, space_after=2)
            p_it.paragraph_format.left_indent = Inches(0.25)
            r_b = p_it.add_run("• ")
            r_b.font.bold = True
            r_b.font.color.rgb = COLOR_PRIMARY
            r_txt = p_it.add_run(it)
            r_txt.font.name = "Calibri"
            r_txt.font.size = Pt(9.5)
            r_txt.font.color.rgb = COLOR_DARK

    # ==========================================
    # 3. REFERENCIAS Y NORMAS TÉCNICAS
    # ==========================================
    h1_3 = doc.add_paragraph()
    style_heading(h1_3, "3. Normas Internacionales y Manuales Técnicos de Referencia", level=1)

    referencias = [
        ("ANSI/TIA-568.0-E / 568.1-E:", "Generic Telecommunications Cabling for Customer Premises. Telecommunications Industry Association."),
        ("ANSI/TIA-568.2-D:", "Balanced Twisted-Pair Telecommunications Cabling and Components Standard."),
        ("ANSI/TIA-568.3-D:", "Optical Fiber Cabling and Components Standard."),
        ("ANSI/TIA-569-E:", "Telecommunications Pathways and Spaces."),
        ("ANSI/TIA-606-D:", "Administration Standard for Telecommunications Infrastructure."),
        ("ANSI/TIA-607-D:", "Generic Grounding and Bonding for Telecommunications."),
        ("ISO/IEC 11801-1:", "Information technology — Generic cabling for customer premises — Part 1: General requirements."),
        ("NFPA 70 / NEC:", "National Electrical Code (Edición 2023). Artículos 770 (Fibra Óptica) y 800 (Circuitos de Comunicaciones)."),
        ("Fluke Networks:", "DSX CableAnalyzer Series User Manual & Versiv Copper and Fiber Certification Best Practices."),
        ("Fundación Kinal:", "Normativa de Convivencia, Asistencia y Evaluación de la Escuela Técnica Superior.")
    ]

    for org, det in referencias:
        p_r = doc.add_paragraph()
        style_p(p_r, space_before=1, space_after=2)
        p_r.paragraph_format.left_indent = Inches(0.2)
        r_b = p_r.add_run(f"• {org} ")
        r_b.font.name = "Calibri"
        r_b.font.size = Pt(9)
        r_b.font.bold = True
        r_b.font.color.rgb = COLOR_PRIMARY
        r_d = p_r.add_run(det)
        r_d.font.name = "Calibri"
        r_d.font.size = Pt(9)
        r_d.font.color.rgb = COLOR_DARK

    section = doc.sections[0]
    footer = section.footer
    footer_p = footer.paragraphs[0]
    style_p(footer_p, space_before=0, space_after=0)
    footer_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run_f = footer_p.add_run("Fundación Kinal | Cableado Estructurado y Redes de Cobre/Fibra — Temario Oficial")
    run_f.font.name = "Calibri"
    run_f.font.size = Pt(8.5)
    run_f.font.color.rgb = COLOR_SECONDARY

    out_dir = os.path.join("Cursos", "Cableado_Estructurado")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "Temario_Curso_Cableado_Estructurado_Kinal.docx")
    doc.save(out_path)
    print(f"Temario guardado con éxito en: {out_path}")

if __name__ == "__main__":
    generate_temario_doc()
