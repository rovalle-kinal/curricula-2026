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
    # ENCABEZADO / # Nombre del curso
    # ==========================================
    title_p = doc.add_paragraph()
    style_p(title_p, space_before=0, space_after=6)
    run_title = title_p.add_run("Ciberseguridad y Fundamentos de Seguridad de la Información")
    run_title.font.name = "Calibri"
    run_title.font.size = Pt(22)
    run_title.font.bold = True
    run_title.font.color.rgb = COLOR_PRIMARY

    sub_p = doc.add_paragraph()
    style_p(sub_p, space_before=0, space_after=14)
    run_sub = sub_p.add_run("Programa de formación y temario  |  Duración total 80 horas  |  Modalidad híbrida  |  20 sesiones de 4 horas\nFundación Kinal — Escuela Técnica Superior | Nivel DQR 4 - 5")
    run_sub.font.name = "Calibri"
    run_sub.font.size = Pt(11)
    run_sub.font.italic = True
    run_sub.font.color.rgb = COLOR_SECONDARY

    border_p = doc.add_paragraph()
    style_p(border_p, space_before=0, space_after=12)
    pPr = border_p._element.get_or_add_pPr()
    pBdr = parse_xml(f'<w:pBdr {nsdecls("w")}><w:bottom w:val="single" w:sz="12" w:space="4" w:color="003366"/></w:pBdr>')
    pPr.append(pBdr)

    # ==========================================
    # ## Misión de Kinal
    # ==========================================
    h2_mision = doc.add_paragraph()
    style_p(h2_mision, space_before=8, space_after=4)
    run_h2_mision = h2_mision.add_run("Misión de Kinal")
    run_h2_mision.font.name = "Calibri"
    run_h2_mision.font.size = Pt(13)
    run_h2_mision.font.bold = True
    run_h2_mision.font.color.rgb = COLOR_PRIMARY

    p_mision = doc.add_paragraph()
    style_p(p_mision, space_before=0, space_after=10)
    run_mision = p_mision.add_run("«Formar a jóvenes y adultos a través de una educación integral, con énfasis en las áreas técnicas y tecnológicas, influyendo positivamente en su trabajo, su familia y la sociedad».")
    run_mision.font.name = "Calibri"
    run_mision.font.size = Pt(10.5)
    run_mision.font.italic = True
    run_mision.font.color.rgb = COLOR_DARK

    # ==========================================
    # ## Visión de Kinal
    # ==========================================
    h2_vision = doc.add_paragraph()
    style_p(h2_vision, space_before=8, space_after=4)
    run_h2_vision = h2_vision.add_run("Visión de Kinal")
    run_h2_vision.font.name = "Calibri"
    run_h2_vision.font.size = Pt(13)
    run_h2_vision.font.bold = True
    run_h2_vision.font.color.rgb = COLOR_PRIMARY

    p_vision = doc.add_paragraph()
    style_p(p_vision, space_before=0, space_after=10)
    run_vision = p_vision.add_run("Ser líderes en la formación técnica, tecnológica y humana de la región, propiciando la superación personal, laboral y social de nuestros estudiantes con un alto sentido ético y excelencia profesional.")
    run_vision.font.name = "Calibri"
    run_vision.font.size = Pt(10.5)
    run_vision.font.color.rgb = COLOR_DARK

    # ==========================================
    # ## Competencia del curso y Ficha Técnica
    # ==========================================
    h2_comp = doc.add_paragraph()
    style_p(h2_comp, space_before=10, space_after=6)
    run_h2_comp = h2_comp.add_run("Competencia del curso")
    run_h2_comp.font.name = "Calibri"
    run_h2_comp.font.size = Pt(13)
    run_h2_comp.font.bold = True
    run_h2_comp.font.color.rgb = COLOR_PRIMARY

    items_generales = [
        ("Competencia general:", "Interpretar sistemas, redes, aplicaciones y servicios desde la perspectiva de la seguridad de la información, para delimitar alcances, reconocer riesgos, diseñar controles básicos, gestionar accesos y ciclos de vida, y documentar decisiones y evidencias con criterio técnico y responsabilidad."),
        ("Duración total en horas:", "80 horas pedagógicas totales (organizadas en 20 sesiones de 4 horas / 240 minutos cada una, con 20 minutos de receso por encuentro, sumando 73 horas y 20 minutos de actividad formativa efectiva)."),
        ("Horario:", "Por convenir institucionalmente (el calendario se organiza por sesiones consecutivas, sin imponer días u horas fijas de inicio)."),
        ("Modalidad:", "Modalidad híbrida (80% virtual y 20% presencial; la coordinación de encuentros virtuales y talleres en laboratorios de Fundación Kinal se define institucionalmente)."),
        ("Perfil de ingreso y orientación laboral:", "Dirigido a personas de 18 a 45 años desempleadas con conocimientos previos de informática que buscan fortalecer su preparación para funciones iniciales de soporte, operación tecnológica y apoyo a seguridad de la información. Requiere manejo de computadora, navegador y documentos; no requiere programación."),
        ("Perfil de egreso:", "El egresado delimita alcances y riesgos en sistemas locales y cloud, diseña controles de mínimo privilegio y autenticación, correlaciona eventos en SIEM, gestiona el ciclo de vida de vulnerabilidades y documenta incidentes bajo normativas de la industria y el ideario del trabajo bien hecho de Kinal.")
    ]

    for label, text in items_generales:
        p_item = doc.add_paragraph()
        style_p(p_item, space_before=0, space_after=5)
        run_lbl = p_item.add_run(f"**{label}** ")
        run_lbl.font.name = "Calibri"
        run_lbl.font.size = Pt(10.5)
        run_lbl.font.bold = True
        run_lbl.font.color.rgb = COLOR_PRIMARY

        run_txt = p_item.add_run(text)
        run_txt.font.name = "Calibri"
        run_txt.font.size = Pt(10.5)
        run_txt.font.color.rgb = COLOR_DARK

    # Alcance de la formación y Metodología
    add_callout(doc,
        "Alcance y Metodología Transversal: El curso parte de sistemas y servicios para comprender qué se protege, quién es responsable y cómo se demuestra que un control funciona. Combina teoría, demostraciones y casos de análisis, diagramación y documentación. Desarrolla criterio para interpretar, comunicar y escalar problemas de seguridad; no acredita especialización en pentesting ni ingeniería de redes. Las actividades prácticas se articulan sobre una empresa ficticia transversal (estaciones, red local, servidor, aplicación web y servicios SaaS). Las demostraciones se ejecutan sobre entornos autorizados sin explotar vulnerabilidades.",
        bold_prefix="Alcance Formativo y Caso Práctico Transversal:")

    # Resultados al finalizar
    p_res = doc.add_paragraph()
    style_p(p_res, space_before=6, space_after=4)
    r_res = p_res.add_run("Resultados de Aprendizaje al Finalizar (Learning Outcomes):")
    r_res.font.name = "Calibri"
    r_res.font.size = Pt(11)
    r_res.font.bold = True
    r_res.font.color.rgb = COLOR_PRIMARY

    outcomes = [
        "Representar componentes, flujos, dependencias y fronteras de un sistema.",
        "Explicar identidad, acceso y protección del transporte sin confundir sus funciones.",
        "Construir controles con alcance, responsables, procedimientos y evidencia.",
        "Interpretar vulnerabilidades y justificar su tratamiento y validación.",
        "Preparar documentación de seguridad y reportar señales de incidente."
    ]
    for out in outcomes:
        p_o = doc.add_paragraph()
        style_p(p_o, space_before=1, space_after=2)
        p_o.paragraph_format.left_indent = Inches(0.25)
        r_b = p_o.add_run("• ")
        r_b.font.bold = True
        r_b.font.color.rgb = COLOR_PRIMARY
        r_t = p_o.add_run(out)
        r_t.font.name = "Calibri"
        r_t.font.size = Pt(10)
        r_t.font.color.rgb = COLOR_DARK

    # Tabla Distribución del programa
    p_dt = doc.add_paragraph()
    style_p(p_dt, space_before=10, space_after=4)
    r_dt = p_dt.add_run("Distribución Modular del Programa (80 Horas — 20 Sesiones):")
    r_dt.font.name = "Calibri"
    r_dt.font.size = Pt(11)
    r_dt.font.bold = True
    r_dt.font.color.rgb = COLOR_PRIMARY

    tbl_dist = doc.add_table(rows=10, cols=4)
    tbl_dist.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_dist.autofit = False
    tbl_dist.columns[0].width = Inches(1.1)
    tbl_dist.columns[1].width = Inches(3.4)
    tbl_dist.columns[2].width = Inches(0.9)
    tbl_dist.columns[3].width = Inches(1.1)
    set_table_borders(tbl_dist, color="CBD5E0", sz="4")

    hdr_d = tbl_dist.rows[0]
    for c in hdr_d.cells:
        set_cell_background(c, "003366")
    for idx, text in enumerate(["Módulo", "Área de Formación", "Horas", "Sesiones"]):
        p = hdr_d.cells[idx].paragraphs[0]
        style_p(p, space_before=0, space_after=0)
        r = p.add_run(text)
        r.font.name = "Calibri"
        r.font.size = Pt(9)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    dist_data = [
        ("Módulo 1", "Sistemas y gestión informática para la seguridad", "12 h", "Sesiones 1 a 3"),
        ("Módulo 2", "Identidad y control de acceso en aplicaciones", "12 h", "Sesiones 4 a 6"),
        ("Módulo 3", "Diseño de controles y responsabilidades de seguridad", "8 h", "Sesiones 7 a 8"),
        ("Módulo 4", "Seguridad de comunicaciones web y APIs", "12 h", "Sesiones 9 a 11"),
        ("Módulo 5", "Ciclo de vida y gestión de vulnerabilidades", "12 h", "Sesiones 12 a 14"),
        ("Módulo 6", "Documentación y gestión del riesgo de seguridad", "8 h", "Sesiones 15 a 16"),
        ("Módulo 7", "Estándares, regulaciones e informes de aseguramiento", "8 h", "Sesiones 17 a 18"),
        ("Módulo 8", "Higiene digital y respuesta inicial a incidentes", "8 h", "Sesiones 19 a 20"),
        ("TOTAL", "8 Módulos de Especialización Técnica", "80 h", "20 Sesiones")
    ]

    for idx, (m, a, h, s) in enumerate(dist_data, start=1):
        row = tbl_dist.rows[idx]
        if idx == 9:
            for c in row.cells:
                set_cell_background(c, "EDF2F7")
        elif idx % 2 == 1:
            for c in row.cells:
                set_cell_background(c, "F7FAFC")
        for c_idx, val in enumerate([m, a, h, s]):
            cell = row.cells[c_idx]
            set_cell_margins(cell, top=50, bottom=50, left=60, right=60)
            p = cell.paragraphs[0]
            style_p(p, space_before=0, space_after=0)
            r = p.add_run(val)
            r.font.name = "Calibri"
            r.font.size = Pt(8.5)
            r.font.color.rgb = COLOR_DARK
            if idx == 9 or c_idx in [0, 2]:
                r.font.bold = True

    doc.add_page_break()

    # ==========================================
    # ## Temario: (Los 8 Módulos Detallados)
    # ==========================================
    h2_temario = doc.add_paragraph()
    style_p(h2_temario, space_before=10, space_after=8)
    run_h2_temario = h2_temario.add_run("Temario Detallado del Programa:")
    run_h2_temario.font.name = "Calibri"
    run_h2_temario.font.size = Pt(16)
    run_h2_temario.font.bold = True
    run_h2_temario.font.color.rgb = COLOR_PRIMARY

    modulos = [
        {
            "num": "1",
            "nombre": "Sistemas y gestión informática para la seguridad (12 Horas | 3 Sesiones: 1 a 3)",
            "objetivo": "Identificar activos, servicios, dependencias y responsables para delimitar el impacto de una falla o un riesgo de seguridad.",
            "temas": [
                {
                    "titulo": "1.1 Fundamentos de seguridad de la información",
                    "indicador": "Distingue confidencialidad, integridad y disponibilidad en un caso laboral.",
                    "subtemas": [
                        "Información, datos y activos esenciales de una organización",
                        "Conceptos clave: amenaza, vulnerabilidad, riesgo, control e incidente",
                        "Ejemplos reales de exposición, alteración e interrupción de servicios",
                        "Clasificación inicial de la información: pública, interna, confidencial y restringida"
                    ]
                },
                {
                    "titulo": "1.2 Soporte técnico y gestión de servicios",
                    "indicador": "Clasifica una solicitud y documenta su atención con responsables y evidencia.",
                    "subtemas": [
                        "Principios fundamentales de ITIL aplicados al soporte: valor, colaboración, visibilidad, mejora y simplicidad",
                        "Mesa de servicio: incidente, solicitud de servicio, problema y gestión de cambios",
                        "Matriz de prioridad por impacto y urgencia; acuerdos de nivel de servicio (SLA), aprobaciones y cierre",
                        "Diferenciación técnica entre incidente operativo de servicio e incidente de seguridad de la información"
                    ]
                },
                {
                    "titulo": "1.3 Redes y sistemas locales y en la nube",
                    "indicador": "Lee y dibuja un diagrama básico explicando qué depende de qué.",
                    "subtemas": [
                        "Componentes de infraestructura: servidor físico/virtual, sistema operativo, cliente, base de datos y almacenamiento",
                        "Topologías de red: LAN, WAN, Internet, switches, puntos de acceso inalámbrico y enlaces de comunicación",
                        "Flujos fundamentales: transporte, procesamiento y almacenamiento de datos",
                        "Entornos on-premises y nube: diagramación lógica, dirección de flujos, dependencias y límites del sistema"
                    ]
                },
                {
                    "titulo": "1.4 Software y servicios digitales",
                    "indicador": "Delimita las capacidades de un servicio y las responsabilidades del cliente y del proveedor.",
                    "subtemas": [
                        "Diferencias entre programa local, aplicación corporativa y servicio digital consumido",
                        "Modelos de servicio en la nube: IaaS, PaaS y SaaS; experiencia del usuario final",
                        "Relación operativa entre disponibilidad, desempeño y seguridad de la información",
                        "Servicios auxiliares: identidad, correo, respaldo, protección de endpoint (EDR) y monitoreo; matriz de responsabilidad compartida"
                    ]
                }
            ],
            "evidencia": "Dibujar el sistema de una empresa ficticia con equipos, red, servidor y SaaS; delimitar su alcance y registrar un incidente con impacto, responsable y evidencia."
        },
        {
            "num": "2",
            "nombre": "Identidad y control de acceso en aplicaciones (12 Horas | 3 Sesiones: 4 a 6)",
            "objetivo": "Explicar el flujo de acceso de una aplicación y distinguir autenticación, autorización, sesión y federación.",
            "temas": [
                {
                    "titulo": "2.1 Autenticación y ciclo de sesión",
                    "indicador": "Reconstruye el inicio, validación y cierre de una sesión, señalando quién valida cada paso.",
                    "subtemas": [
                        "Fases del ciclo: identificación, prueba de identidad, validación, creación de sesión, expiración, cierre y revocación",
                        "Entidades del flujo: aplicación cliente, proveedor de identidad (IdP) y dueño del recurso",
                        "Políticas de registro, recuperación de cuenta, protección de credenciales y límites de intentos fallidos",
                        "Principio de separación: la autenticación exitosa no equivale a autorización para todas las acciones"
                    ]
                },
                {
                    "titulo": "2.2 Autenticación multifactor (MFA)",
                    "indicador": "Compara factores y describe un procedimiento de enrolamiento y recuperación.",
                    "subtemas": [
                        "Factores estándar: conocimiento (lo que sé), posesión (lo que tengo) e inherencia (lo que soy)",
                        "Mecanismos comunes: contraseñas de un solo uso (OTP), aplicaciones autenticadoras, notificaciones push y llaves físicas FIDO2",
                        "Análisis de fricción, ataques de phishing a MFA y fatiga de aprobación de notificaciones",
                        "Métodos resistentes al phishing, protocolos de pérdida de factor, recuperación de cuenta y control de excepciones"
                    ]
                },
                {
                    "titulo": "2.3 SSO y federación de identidad",
                    "indicador": "Compara un acceso local con un acceso mediante un proveedor de identidad.",
                    "subtemas": [
                        "Single Sign-On (SSO): reutilización centralizada de una autenticación entre múltiples aplicaciones",
                        "Flujo de interacción: usuario, aplicación consumidora (SP) y proveedor de identidad (IdP)",
                        "Relaciones de confianza y manejo de sesiones independientes",
                        "Beneficios de administración centralizada y riesgos de concentración; análisis del cierre de sesión (Single Logout)"
                    ]
                },
                {
                    "titulo": "2.4 Protocolos y credenciales de acceso",
                    "indicador": "Ubica cada tecnología en su función sin tratarlas como equivalentes.",
                    "subtemas": [
                        "SAML 2.0: intercambio de aserciones XML para federación empresarial",
                        "LDAP: protocolo de acceso a directorios para consulta y validación de credenciales",
                        "OAuth 2.0 (delegación de autorización) vs. OpenID Connect (capa de identidad y autenticación)",
                        "Bearer Tokens: credenciales de portador, transporte seguro TLS, alcance (scope), expiración y flujo PKCE sin código"
                    ]
                },
                {
                    "titulo": "2.5 RBAC y gestión de usuarios",
                    "indicador": "Construye una matriz simple de roles y permisos coherente con las tareas.",
                    "subtemas": [
                        "Control de Acceso Basado en Roles (RBAC): usuario, grupo, rol, recurso protegido y acción permitida",
                        "Ciclo de vida del usuario: altas (onboarding), modificaciones de puesto y bajas inmediatas (offboarding)",
                        "Tipos de cuenta: personales, administrativas, cuentas de servicio técnico y cuentas de emergencia (break-glass)",
                        "Propietario responsable de cada cuenta, revisiones periódicas de acceso, cálculo de permisos efectivos y revocación"
                    ]
                }
            ],
            "evidencia": "Representar un inicio de sesión local y uno federado; construir una matriz de permisos y resolver la baja de un usuario con sesiones activas."
        },
        {
            "num": "3",
            "nombre": "Diseño de controles y responsabilidades de seguridad (8 Horas | 2 Sesiones: 7 a 8)",
            "objetivo": "Convertir principios de seguridad en controles delimitados, asignados y verificables.",
            "temas": [
                {
                    "titulo": "3.1 Mínimo privilegio construido",
                    "indicador": "Justifica cada permiso y propone una verificación de acceso efectivo.",
                    "subtemas": [
                        "Definición precisa: tareas laborales, recursos requeridos, acciones autorizadas y ventana de tiempo",
                        "Regla de denegación por defecto (deny by default) y concesión explícita de accesos justificados",
                        "Separación estricta entre cuenta de uso diario no privilegiada y cuenta con privilegios administrativos",
                        "Permisos temporales (Just-in-Time), flujos de aprobación y eliminación de roles genéricos excesivos"
                    ]
                },
                {
                    "titulo": "3.2 Delimitación del alcance y fronteras de confianza",
                    "indicador": "Redacta inclusiones, exclusiones y dependencias de un control.",
                    "subtemas": [
                        "Definición del perímetro: objeto protegido, usuarios, datos sensibles, sistemas, ambientes (dev/prod) y acciones",
                        "Identificación de puntos de entrada, interfaces de comunicación, proveedores terceros y límites de confianza",
                        "Criterio de verificabilidad: un control debe especificar exactamente dónde actúa y qué evidencia demuestra su cobertura",
                        "Riesgos de la presunción 'aplica a todo' sin un inventario formal y verificable de activos"
                    ]
                },
                {
                    "titulo": "3.3 Arquitectura Zero Trust",
                    "indicador": "Explica una decisión de acceso basada en identidad, recurso y contexto.",
                    "subtemas": [
                        "Evolución de la seguridad: superación de la confianza implícita basada únicamente en la ubicación de red interna",
                        "Pilares fundamentales: verificación explícita, mínimo privilegio y asunción de brecha de seguridad",
                        "Evaluación contextual en tiempo real: estado del dispositivo, identidad del usuario, criticidad del recurso y sesión",
                        "Microsegmentación y contención del movimiento lateral; aclaración: Zero Trust es un marco arquitectónico, no un producto"
                    ]
                },
                {
                    "titulo": "3.4 Segregación de funciones y responsabilidad compartida",
                    "indicador": "Distribuye planeación, aprobación, ejecución, cumplimiento y auditoría evitando autoaprobación.",
                    "subtemas": [
                        "Identificación de funciones incompatibles en los flujos organizacionales y necesidad de revisión independiente",
                        "Aplicación de la Matriz RACI (Responsable, Aprobador, Consultado, Informado) y controles compensatorios en equipos pequeños",
                        "Distinción entre segregación de funciones interna y matriz de responsabilidad compartida con proveedores de nube",
                        "Criterio de control: pertenecer al mismo departamento tecnológico no elimina la obligación de separar funciones críticas"
                    ]
                },
                {
                    "titulo": "3.5 Trazabilidad de extremo a extremo mediante logs y SIEM",
                    "indicador": "Lee registros básicos y correlaciona eventos para reconstruir un proceso, separando hechos de hipótesis.",
                    "subtemas": [
                        "Naturaleza de los logs: registros de eventos en fuentes de identidad, servidores, aplicaciones, firewalls y nube",
                        "Campos de lectura universal: marca de tiempo y zona horaria (UTC), actor, IP origen, recurso destino, acción y resultado",
                        "Definición y función de un SIEM (Security Information and Event Management): centralización, normalización y correlación",
                        "Diferenciación conceptual clave: evento (registro neutral), alerta (anomalía detectada) e incidente (daño confirmado)",
                        "Requisitos de telemetría: integridad de logs, retención normada, sincronización NTP y cobertura de fuentes",
                        "Lectura práctica de logs de autenticación Windows (Event IDs 4625 y 4624), denegaciones de firewall y denegaciones de aplicación"
                    ]
                }
            ],
            "evidencia": "Diseñar un acceso temporal con roles separados y reconstruirlo mediante ticket y logs correlacionados. Identificar campos faltantes, fuentes necesarias y una alerta que todavía requiere investigación."
        },
        {
            "num": "4",
            "nombre": "Seguridad de comunicaciones web y APIs (12 Horas | 3 Sesiones: 9 a 11)",
            "objetivo": "Explicar cómo se transporta y protege una comunicación web, qué valida TLS y dónde permanecen los riesgos.",
            "temas": [
                {
                    "titulo": "4.1 Criptografía y protección de datos",
                    "indicador": "Distingue cifrado, hash y firma y explica el papel de las claves.",
                    "subtemas": [
                        "Conceptos fundamentales: texto en claro, algoritmo criptográfico, clave de seguridad, cifrado y descifrado",
                        "Cifrado simétrico (AES) vs. asimétrico (RSA/ECC), intercambio de claves Diffie-Hellman y firmas digitales",
                        "Protección de datos en tránsito (TLS) y datos en reposo (cifrado de discos y bases de datos); gestión de claves",
                        "Aclaraciones técnicas: una función hash no es cifrado reversible; cifrar no garantiza disponibilidad ni autorización"
                    ]
                },
                {
                    "titulo": "4.2 HTTP, HTTPS, TLS y certificados",
                    "indicador": "Describe el establecimiento conceptual de una conexión HTTPS.",
                    "subtemas": [
                        "Estructura del protocolo HTTP: solicitud y respuesta, URL, métodos (GET, POST), códigos de estado (200, 401, 403, 500) y cabeceras",
                        "Funcionamiento de HTTPS sobre TLS: negociación de parámetros (handshake), autenticación del servidor y acuerdo de claves",
                        "Estructura del certificado digital X.509: vinculación de identidad con clave pública, nombre de dominio (SAN), emisor y vigencia",
                        "Criterio de seguridad: la presencia de un certificado SSL/TLS no prueba que el contenido del sitio web sea legítimo u honesto"
                    ]
                },
                {
                    "titulo": "4.3 Cadena de confianza y autoridades certificadoras",
                    "indicador": "Explica por qué un certificado es aceptado o rechazado por un cliente.",
                    "subtemas": [
                        "Jerarquía de confianza: Autoridad Certificadora (CA) raíz, CAs intermedias y almacén de certificados de confianza del sistema",
                        "Criterios de validación del cliente: coincidencia exacta del nombre de host, periodo de vigencia y listas de revocación (CRL/OCSP)",
                        "Certificados públicos comerciales vs. certificados autofirmados de laboratorio; configuración de confianza",
                        "Gestión de certificados: emisión, renovación programada y riesgo operacional de ignorar advertencias del navegador"
                    ]
                },
                {
                    "titulo": "4.4 Exposición y componentes del recorrido web",
                    "indicador": "Identifica la función de cada componente y los datos que puede observar.",
                    "subtemas": [
                        "Direccionamiento y resolución: direcciones IP públicas y privadas (RFC 1918), servidores DNS y registros A, AAAA y CNAME",
                        "Dispositivos de borde: router (enrutamiento), firewall perimetral (control de tráfico) y proxy (intermediación de solicitudes)",
                        "Diferencias entre Proxy directo (Forward Proxy) y Proxy inverso (Reverse Proxy), traducción de direcciones NAT y WAN",
                        "Visibilidad de metadatos: la información que TLS no oculta (SNI, IP destino) y la inspección de contenido en terminación TLS"
                    ]
                },
                {
                    "titulo": "4.5 APIs y límites de seguridad",
                    "indicador": "Reconoce un recurso expuesto y propone controles básicos sobre su uso.",
                    "subtemas": [
                        "Arquitectura de APIs REST: endpoints, métodos HTTP, peticiones con parámetros y cuerpos en formato JSON",
                        "Mecanismos de control: autenticación por API keys/tokens Bearer, autorización a nivel de función y de objeto",
                        "Validación de entradas, límites de tasa de consumo (Rate Limiting) y registro de actividad",
                        "Vulnerabilidades comunes: fuga de tokens, exposición excesiva de datos; HTTPS protege el canal pero no la lógica de acceso"
                    ]
                }
            ],
            "evidencia": "Trazar navegador, DNS, router, firewall, proxy y servidor; revisar un certificado y una petición de API de ejemplo sin usar credenciales reales."
        },
        {
            "num": "5",
            "nombre": "Ciclo de vida y gestión de vulnerabilidades (12 Horas | 3 Sesiones: 12 a 14)",
            "objetivo": "Relacionar inventario, soporte, cambios y hallazgos para decidir entre actualizar, mitigar, sustituir o retirar.",
            "temas": [
                {
                    "titulo": "5.1 Activos de hardware",
                    "indicador": "Define un ciclo de vida con propietario, fechas y criterios de retiro.",
                    "subtemas": [
                        "Gestión del inventario de activos físicos: criticidad para el negocio, ubicación geográfica y custodio asignado",
                        "Etapas del ciclo de vida del hardware: adquisición, recepción formal, puesta en operación, mantenimiento y retiro",
                        "Fechas críticas del fabricante: Fin de Venta (End of Sale), Fin de Vida Útil (EOL) y Fin de Soporte (EOS)",
                        "Criterio de análisis: antigüedad no equivale automáticamente a vulnerabilidad; protocolos de borrado seguro y desecho"
                    ]
                },
                {
                    "titulo": "5.2 Servicios tercerizados",
                    "indicador": "Establece seguimiento de cambios y compromisos de seguridad del proveedor.",
                    "subtemas": [
                        "Gestión de proveedores de tecnología: evaluación de seguridad previa, contratación, seguimiento de cambios y salida",
                        "Monitoreo de notas de versión (release notes), avisos de seguridad y calendarios de deprecación de funciones",
                        "Desafíos de la nube: falta de control sobre cuándo actualiza el proveedor SaaS; evaluación de impacto en la operación",
                        "Estrategias de salida: exportación íntegra de datos, eliminación certificada de respaldos y revocación de accesos"
                    ]
                },
                {
                    "titulo": "5.3 Servidores y sistemas operativos",
                    "indicador": "Propone actualización o retiro según soporte, exposición y dependencias.",
                    "subtemas": [
                        "Inventario de sistemas operativos, versiones de compilación, estado de soporte del fabricante y servicios expuestos",
                        "Distinción técnica entre actualización menor, parche de seguridad crítico y actualización mayor de versión",
                        "Gestión de cambios de parches: inventario, verificación de respaldos previos, pruebas en ambiente no productivo y ventana de despliegue",
                        "Planes de reversión (rollback); retiro seguro de servidores antiguos sin dejar registros DNS huérfanos o cuentas abandonadas"
                    ]
                },
                {
                    "titulo": "5.4 Software y dependencias",
                    "indicador": "Identifica componentes cuyo mantenimiento afecta la seguridad de una aplicación.",
                    "subtemas": [
                        "Inventario de aplicaciones autorizadas, licencias activas y dependencias de software instalado",
                        "Componentes invisibles: bibliotecas compartidas, módulos de terceros, complementos (plugins) y agentes de gestión",
                        "Protocolos de desinstalación limpia y remoción de permisos residuales en el sistema operativo",
                        "Criterio de verificación: instalar una versión nueva no garantiza por sí sola la corrección de un hallazgo si la configuración sigue vulnerable"
                    ]
                },
                {
                    "titulo": "5.5 Lectura y tratamiento de vulnerabilidades",
                    "indicador": "Interpreta un registro y formula una acción verificable para el activo afectado.",
                    "subtemas": [
                        "Estructura del identificador CVE (Common Vulnerabilities and Exposures), descripción del fallo y productos afectados",
                        "Métricas de severidad CVSS (Common Vulnerability Scoring System): vector base frente a prioridad real por exposición del activo",
                        "Diferenciación entre parche definitivo, mitigación temporal, ajuste de configuración y retiro del servicio",
                        "Caso de estudio: protocolos obsoletos (TLS 1.0/1.1) habilitados en un servicio y procedimiento de remediación sin parche específico"
                    ]
                }
            ],
            "evidencia": "Completar inventario y plan de ciclo de vida; leer un aviso real preparado por el docente y justificar tratamiento, pruebas, reversión y evidencia de cierre."
        },
        {
            "num": "6",
            "nombre": "Documentación y gestión del riesgo de seguridad (8 Horas | 2 Sesiones: 15 a 16)",
            "objetivo": "Redactar documentos de seguridad utilizables y justificar decisiones sobre riesgos con responsabilidades y evidencia.",
            "temas": [
                {
                    "titulo": "6.1 Políticas y estructura documental",
                    "indicador": "Redacta una regla con alcance, responsable y forma de verificarla.",
                    "subtemas": [
                        "Pirámide documental de seguridad: políticas corporativas, estándares técnicos, procedimientos operativos y guías",
                        "Elementos obligatorios de una política: propósito, alcance explícito, reglas mandatorias, responsables, excepciones y revisión",
                        "Criterio de redacción: una declaración general abstracta no es un control si carece de especificaciones operativas verificables"
                    ]
                },
                {
                    "titulo": "6.2 Procedimientos operativos estándar (SOP)",
                    "indicador": "Describe pasos ejecutables con condiciones de inicio y cierre.",
                    "subtemas": [
                        "Estructura de un SOP: objetivo, alcance, prerrequisitos, roles intervinientes, pasos secuenciales y caminos de decisión",
                        "Manejo de excepciones, puntos de escalamiento a niveles superiores, evidencia generada y criterios de cierre exitoso",
                        "Regla de oro de usabilidad: un procedimiento debe permitir que cualquier técnico calificado lo ejecute sin necesidad de adivinar",
                        "Control de versiones, fechas de vigencia y trazabilidad de cambios en la documentación técnica"
                    ]
                },
                {
                    "titulo": "6.3 Evaluación y tratamiento de riesgos",
                    "indicador": "Documenta un escenario sustentado y distingue riesgo inherente y residual.",
                    "subtemas": [
                        "Construcción del escenario de riesgo: activo e información involucrada, amenaza latente y vulnerabilidad explotable",
                        "Criterios de valoración: estimación de impacto en el negocio y probabilidad de ocurrencia según controles existentes",
                        "Diferenciación conceptual: riesgo inherente (sin controles) vs. riesgo residual (remanente tras aplicar salvaguardas)",
                        "Opciones de tratamiento: evitar el riesgo, mitigarlo mediante controles, transferirlo (seguros) o aceptarlo formalmente"
                    ]
                },
                {
                    "titulo": "6.4 Aceptación del riesgo",
                    "indicador": "Formula una aceptación temporal para decisión de la autoridad competente.",
                    "subtemas": [
                        "Estructura de una solicitud formal de aceptación: justificación del riesgo residual, análisis de alternativas y controles compensatorios",
                        "Nivel de autoridad: el técnico que implementa no tiene facultades para aceptar riesgos en nombre de la organización",
                        "Temporalidad y condiciones: vigencia delimitada, fecha de revisión obligatoria y causales de revocación inmediata",
                        "Límites legales y éticos: la aceptación interna del riesgo no exime a la entidad del cumplimiento de normativas ni leyes vigentes"
                    ]
                }
            ],
            "evidencia": "Preparar una política de accesos, un SOP de baja de usuario, una evaluación de riesgo y una solicitud de aceptación temporal relacionadas con el mismo caso."
        },
        {
            "num": "7",
            "nombre": "Estándares, regulaciones e informes de aseguramiento (8 Horas | 2 Sesiones: 17 a 18)",
            "objetivo": "Distinguir finalidad, alcance y evidencia de PCI DSS, ISO/IEC 27001, HIPAA y los informes SOC.",
            "temas": [
                {
                    "titulo": "7.1 Estándar PCI DSS",
                    "indicador": "Identifica datos de pago y delimita conceptualmente el entorno que debe revisarse.",
                    "subtemas": [
                        "Payment Card Industry Data Security Standard: objetivo de protección de datos de titulares de tarjetas de pago",
                        "Delimitación del Entorno de Datos del Titular (CDE): sistemas que almacenan, procesan, transmiten o influyen en la seguridad del CDE",
                        "Requisitos fundamentales de acceso, cifrado, monitoreo de redes y preservación de registros de auditoría",
                        "Nociones de validación del cumplimiento: cuestionarios de autoevaluación (SAQ) y auditorías formales (introducción de 2 horas)"
                    ]
                },
                {
                    "titulo": "7.2 ISO/IEC 27001 y la familia 27000",
                    "indicador": "Relaciona riesgos, controles y mejora con un sistema de gestión.",
                    "subtemas": [
                        "Estructura del Sistema de Gestión de Seguridad de la Información (SGSI): ISO/IEC 27001:2022 y guía de controles ISO/IEC 27002",
                        "Requisitos normativos: contexto organizacional, liderazgo gerencial, evaluación y tratamiento de riesgos y mejora continua",
                        "Declaración de Aplicabilidad (SoA): selección justificada de controles aplicables y exclusiones documentadas",
                        "Alcance de la certificación: la norma certifica un alcance o proceso específico, no a toda la empresa como entidad universal (2 horas)"
                    ]
                },
                {
                    "titulo": "7.3 Regulación HIPAA",
                    "indicador": "Reconoce cuándo requiere revisión de aplicabilidad y qué información protege.",
                    "subtemas": [
                        "Health Insurance Portability and Accountability Act de EE.UU.: protección de información de salud protegida electrónica (ePHI)",
                        "Entidades cubiertas (proveedores de salud, planes médicos) y socios comerciales tecnológicos (Business Associates)",
                        "Reglas de HIPAA: Regla de Privacidad, Regla de Seguridad (salvaguardas administrativas, físicas y técnicas) y Regla de Notificación de Brechas",
                        "Criterio de aplicabilidad en empresas tecnológicas guatemaltecas que prestan servicios offshore al sector salud de EE.UU. (2 horas)"
                    ]
                },
                {
                    "titulo": "7.4 Informes de aseguramiento SOC 1 y SOC 2",
                    "indicador": "Distingue el objeto del informe y su tipo antes de usarlo como evidencia.",
                    "subtemas": [
                        "Diferenciación de objetivos: SOC 1 (controles sobre reportes financieros) vs. SOC 2 (criterios de confianza: seguridad, disponibilidad, integridad)",
                        "Diferenciación de tipos de informe: Tipo I (diseño de controles a una fecha fija) vs. Tipo II (diseño y efectividad operativa durante un período)",
                        "Lectura crítica de un informe SOC: opinión del auditor independiente, excepciones encontradas, subcontratistas y controles del cliente",
                        "Criterio de interpretación: un informe SOC es una opinión de aseguramiento independiente, no una certificación automática de infalibilidad (2 horas)"
                    ]
                }
            ],
            "evidencia": "Comparar una empresa que procesa pagos, un proveedor de servicios y una operación con ePHI; justificar qué referencia revisar y qué evidencia pedir. Cada caso requiere comprobar aplicabilidad."
        },
        {
            "num": "8",
            "nombre": "Higiene digital y respuesta inicial a incidentes (8 Horas | 2 Sesiones: 19 a 20)",
            "objetivo": "Aplicar hábitos de protección e identificar y reportar señales de riesgo de manera oportuna y documentada.",
            "temas": [
                {
                    "titulo": "8.1 Credenciales, identidad y equipos",
                    "indicador": "Asocia cada actividad con un usuario responsable y protege sus credenciales.",
                    "subtemas": [
                        "Buenas prácticas en el uso de contraseñas: prohibición de notas adhesivas, contraseñas únicas y uso de gestores autorizados",
                        "Uso seguro de MFA: prohibición estricta de compartir códigos temporales o aceptar solicitudes push no generadas por el usuario",
                        "Responsabilidad de cuentas: uso obligatorio de cuentas individuales y asignación formal de custodio para cuentas técnicas",
                        "Higiene en estaciones de trabajo: bloqueo automático de pantalla, permisos de usuario estándar y separación de actividades personales"
                    ]
                },
                {
                    "titulo": "8.2 Protección cotidiana de la información",
                    "indicador": "Decide cómo almacenar, compartir y recuperar información según su sensibilidad.",
                    "subtemas": [
                        "Canales corporativos autorizados, verificación de destinatarios legítimos y asignación de permisos de lectura/edición en documentos",
                        "Importancia de la instalación oportuna de actualizaciones del sistema operativo y herramientas de seguridad del endpoint",
                        "Control de medios de almacenamiento extraíbles (USB) y prohibición de software no autorizado",
                        "Rutinas de respaldo de datos, verificación periódica de restauración y política de escritorio limpio para información física"
                    ]
                },
                {
                    "titulo": "8.3 Ingeniería social y comunicaciones sospechosas",
                    "indicador": "Identifica señales y verifica una solicitud por un canal independiente.",
                    "subtemas": [
                        "Vectores de ataque: Phishing por correo electrónico, Smishing (SMS), Vishing (llamadas telefónicas), códigos QR maliciosos (Quishing) y suplantación",
                        "Indicadores de sospecha: incoherencias en dirección de remitente, sentido de urgencia desmedido, enlaces ofuscados y solicitudes de pagos o credenciales",
                        "Desmitificación técnica: la presencia de candado HTTPS y una redacción impecable no garantizan que el mensaje sea genuino",
                        "Protocolo de verificación fuera de banda (out-of-band) utilizando números telefónicos o canales previamente conocidos y validados"
                    ]
                },
                {
                    "titulo": "8.4 Reporte y respuesta inicial",
                    "indicador": "Documenta el evento y escala sin destruir evidencia ni investigar fuera de su rol.",
                    "subtemas": [
                        "Información indispensable en un reporte: qué ocurrió, cuándo ocurrió (hora y fecha), quién lo detectó, activo afectado y acciones inmediatas",
                        "Canales formales de escalamiento hacia la mesa de ayuda o el equipo de seguridad; preservación intacta del mensaje y evidencias",
                        "Protocolo de emergencia ante compromiso de credenciales: reporte urgente, activación de revocación de sesiones y cambio de contraseña",
                        "Límites de actuación del personal inicial: contención según instrucciones recibidas, sin realizar indagaciones invasivas que alteren registros"
                    ]
                },
                {
                    "titulo": "8.5 Proyecto integrador de ciberseguridad",
                    "indicador": "Sustenta un conjunto coherente de controles con alcance, responsables y evidencias.",
                    "subtemas": [
                        "Consolidación integral del expediente de seguridad del caso transversal desarrollado durante el curso",
                        "Revisión de consistencia: diagrama de arquitectura, matriz RBAC, trazabilidad en logs, inventario de ciclo de vida, política y SOP",
                        "Justificación razonada de la selección de marcos de cumplimiento y protocolo de respuesta ante una comunicación sospechosa",
                        "Exposición técnica oral individual o en célula ante jurado evaluador de Fundación Kinal, rondas de preguntas y retroalimentación final"
                    ]
                }
            ],
            "evidencia": "Analizar mensajes ficticios, simular un reporte y presentar el expediente de seguridad construido durante el curso con sus límites y evidencias."
        }
    ]

    for mod in modulos:
        h3_mod = doc.add_paragraph()
        style_p(h3_mod, space_before=14, space_after=3)
        run_h3 = h3_mod.add_run(f"Módulo {mod['num']}: {mod['nombre']}")
        run_h3.font.name = "Calibri"
        run_h3.font.size = Pt(12.5)
        run_h3.font.bold = True
        run_h3.font.color.rgb = COLOR_PRIMARY

        p_obj = doc.add_paragraph()
        style_p(p_obj, space_before=0, space_after=6)
        r_ol = p_obj.add_run("**Objetivo del módulo:** ")
        r_ol.font.name = "Calibri"
        r_ol.font.size = Pt(10.5)
        r_ol.font.bold = True
        r_ol.font.color.rgb = COLOR_SECONDARY
        r_ot = p_obj.add_run(mod["objetivo"])
        r_ot.font.name = "Calibri"
        r_ot.font.size = Pt(10.5)
        r_ot.font.color.rgb = COLOR_DARK

        for t in mod["temas"]:
            p_tema = doc.add_paragraph()
            style_p(p_tema, space_before=4, space_after=2)
            p_tema.paragraph_format.left_indent = Inches(0.2)
            run_t_bullet = p_tema.add_run("• Tema: ")
            run_t_bullet.font.name = "Calibri"
            run_t_bullet.font.size = Pt(11)
            run_t_bullet.font.bold = True
            run_t_bullet.font.color.rgb = COLOR_PRIMARY

            run_t_title = p_tema.add_run(t["titulo"])
            run_t_title.font.name = "Calibri"
            run_t_title.font.size = Pt(11)
            run_t_title.font.bold = True
            run_t_title.font.color.rgb = COLOR_DARK

            p_ind = doc.add_paragraph()
            style_p(p_ind, space_before=1, space_after=2)
            p_ind.paragraph_format.left_indent = Inches(0.4)
            run_ind_lbl = p_ind.add_run("**Indicador de logro:** ")
            run_ind_lbl.font.name = "Calibri"
            run_ind_lbl.font.size = Pt(10)
            run_ind_lbl.font.bold = True
            run_ind_lbl.font.color.rgb = COLOR_SECONDARY

            run_ind_txt = p_ind.add_run(t["indicador"])
            run_ind_txt.font.name = "Calibri"
            run_ind_txt.font.size = Pt(10)
            run_ind_txt.font.color.rgb = COLOR_DARK

            for sub in t["subtemas"]:
                p_sub = doc.add_paragraph()
                style_p(p_sub, space_before=1, space_after=1)
                p_sub.paragraph_format.left_indent = Inches(0.6)
                run_sub_dash = p_sub.add_run("– ")
                run_sub_dash.font.name = "Calibri"
                run_sub_dash.font.size = Pt(9.5)
                run_sub_dash.font.color.rgb = COLOR_SECONDARY

                run_sub_txt = p_sub.add_run(sub)
                run_sub_txt.font.name = "Calibri"
                run_sub_txt.font.size = Pt(9.5)
                run_sub_txt.font.color.rgb = COLOR_DARK

        p_evi = doc.add_paragraph()
        style_p(p_evi, space_before=4, space_after=10)
        p_evi.paragraph_format.left_indent = Inches(0.2)
        r_el = p_evi.add_run("**Aplicación y evidencia del módulo:** ")
        r_el.font.name = "Calibri"
        r_el.font.size = Pt(10)
        r_el.font.bold = True
        r_el.font.color.rgb = COLOR_PRIMARY
        r_et = p_evi.add_run(mod["evidencia"])
        r_et.font.name = "Calibri"
        r_et.font.size = Pt(10)
        r_et.font.italic = True
        r_et.font.color.rgb = COLOR_DARK

    # ==========================================
    # ## Evaluación y Proyecto Integrador
    # ==========================================
    doc.add_page_break()

    h2_ev = doc.add_paragraph()
    style_p(h2_ev, space_before=10, space_after=6)
    run_h2_ev = h2_ev.add_run("Evaluación del Aprendizaje y Proyecto Integrador")
    run_h2_ev.font.name = "Calibri"
    run_h2_ev.font.size = Pt(15)
    run_h2_ev.font.bold = True
    run_h2_ev.font.color.rgb = COLOR_PRIMARY

    p_ev_txt = doc.add_paragraph()
    style_p(p_ev_txt, space_before=0, space_after=8)
    r = p_ev_txt.add_run("La evaluación valora la comprensión conceptual y la capacidad práctica de convertirla en acciones delimitadas y verificables bajo el principio institucional del «trabajo bien hecho». Conforme a la normativa de Fundación Kinal, la nota mínima de aprobación es de 75 puntos sobre 100:")
    r.font.name = "Calibri"
    r.font.size = Pt(10.5)
    r.font.color.rgb = COLOR_DARK

    tbl_ponderacion = doc.add_table(rows=4, cols=3)
    tbl_ponderacion.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_ponderacion.autofit = False
    tbl_ponderacion.columns[0].width = Inches(2.3)
    tbl_ponderacion.columns[1].width = Inches(1.1)
    tbl_ponderacion.columns[2].width = Inches(3.1)
    set_table_borders(tbl_ponderacion, color="CBD5E0", sz="4")

    hdr_p = tbl_ponderacion.rows[0]
    for c in hdr_p.cells:
        set_cell_background(c, "003366")
    for idx, text in enumerate(["Componente de Evaluación", "Peso", "Evidencia y Criterio"]):
        p = hdr_p.cells[idx].paragraphs[0]
        style_p(p, space_before=0, space_after=0)
        r = p.add_run(text)
        r.font.name = "Calibri"
        r.font.size = Pt(9)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    pond_data = [
        ("Comprobaciones de aprendizaje", "20%", "Respuestas breves, interpretación de flujos y defensa de decisiones en clase."),
        ("Productos de los módulos", "40%", "Diagramas de arquitectura, matrices RBAC, fichas y documentos revisados."),
        ("Proyecto integrador (Expediente)", "40%", "Expediente de seguridad coherente y presentación sustentada del caso.")
    ]

    for idx, (comp, pes, evid) in enumerate(pond_data, start=1):
        row = tbl_ponderacion.rows[idx]
        if idx % 2 == 1:
            for c in row.cells:
                set_cell_background(c, "F7FAFC")
        for c_idx, val in enumerate([comp, pes, evid]):
            cell = row.cells[c_idx]
            set_cell_margins(cell, top=60, bottom=60, left=70, right=70)
            p = cell.paragraphs[0]
            style_p(p, space_before=0, space_after=0)
            r = p.add_run(val)
            r.font.name = "Calibri"
            r.font.size = Pt(8.5)
            r.font.color.rgb = COLOR_DARK
            if c_idx in [0, 1]:
                r.font.bold = True

    # Rúbrica del proyecto integrador
    p_rub_tit = doc.add_paragraph()
    style_p(p_rub_tit, space_before=12, space_after=4)
    r_rt = p_rub_tit.add_run("Rúbrica Analítica del Proyecto Integrador:")
    r_rt.font.name = "Calibri"
    r_rt.font.size = Pt(11)
    r_rt.font.bold = True
    r_rt.font.color.rgb = COLOR_PRIMARY

    tbl_rub = doc.add_table(rows=6, cols=2)
    tbl_rub.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_rub.autofit = False
    tbl_rub.columns[0].width = Inches(4.5)
    tbl_rub.columns[1].width = Inches(2.0)
    set_table_borders(tbl_rub, color="CBD5E0", sz="4")

    hdr_r = tbl_rub.rows[0]
    for c in hdr_r.cells:
        set_cell_background(c, "003366")
    for idx, text in enumerate(["Criterio Técnico Evaluado", "Peso en el Proyecto"]):
        p = hdr_r.cells[idx].paragraphs[0]
        style_p(p, space_before=0, space_after=0)
        r = p.add_run(text)
        r.font.name = "Calibri"
        r.font.size = Pt(9)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    rub_data = [
        ("Corrección conceptual y distinción rigurosa de funciones técnicas", "25%"),
        ("Alcance explícito y coherencia entre componentes, flujos y documentos", "20%"),
        ("Controles y tratamiento del riesgo debidamente justificados", "25%"),
        ("Asignación de responsables y evidencia de verificación y trazabilidad", "20%"),
        ("Claridad, serenidad y solvencia en la presentación oral y respuestas", "10%")
    ]

    for idx, (crit, pes) in enumerate(rub_data, start=1):
        row = tbl_rub.rows[idx]
        if idx % 2 == 1:
            for c in row.cells:
                set_cell_background(c, "F7FAFC")
        for c_idx, val in enumerate([crit, pes]):
            cell = row.cells[c_idx]
            set_cell_margins(cell, top=60, bottom=60, left=70, right=70)
            p = cell.paragraphs[0]
            style_p(p, space_before=0, space_after=0)
            r = p.add_run(val)
            r.font.name = "Calibri"
            r.font.size = Pt(8.5)
            r.font.color.rgb = COLOR_DARK
            if c_idx == 1:
                r.font.bold = True

    # ==========================================
    # ## Recursos, Herramientas y Precios
    # ==========================================
    doc.add_page_break()

    h2_rec = doc.add_paragraph()
    style_p(h2_rec, space_before=10, space_after=6)
    run_h2_rec = h2_rec.add_run("Recursos de Aprendizaje, Herramientas y Esquema de Precios")
    run_h2_rec.font.name = "Calibri"
    run_h2_rec.font.size = Pt(15)
    run_h2_rec.font.bold = True
    run_h2_rec.font.color.rgb = COLOR_PRIMARY

    p_rec_intro = doc.add_paragraph()
    style_p(p_rec_intro, space_before=0, space_after=6)
    r = p_rec_intro.add_run("El curso emplea computadoras, navegadores web, editores de documentos y herramientas de diagramación. Todos los ejercicios utilizan datos ficticios y no solicitan contraseñas reales. Para garantizar viabilidad económica a personas desempleadas, el software seleccionado es prioritariamente Open Source ($0.00) y de acceso académico oficial a través de la membresía de Fundación Kinal como Cisco Networking Academy:")
    r.font.name = "Calibri"
    r.font.size = Pt(10)
    r.font.color.rgb = COLOR_DARK

    tbl_her = doc.add_table(rows=8, cols=4)
    tbl_her.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_her.autofit = False
    tbl_her.columns[0].width = Inches(1.8)
    tbl_her.columns[1].width = Inches(1.5)
    tbl_her.columns[2].width = Inches(1.4)
    tbl_her.columns[3].width = Inches(1.8)
    set_table_borders(tbl_her, color="CBD5E0", sz="4")

    hdr_h = tbl_her.rows[0]
    for c in hdr_h.cells:
        set_cell_background(c, "003366")
    headers_h = ["Herramienta Tecnológica", "Tipo / Licencia", "Costo Mensual / Anual", "Función en el Programa"]
    for idx, text in enumerate(headers_h):
        p = hdr_h.cells[idx].paragraphs[0]
        style_p(p, space_before=0, space_after=0)
        r = p.add_run(text)
        r.font.name = "Calibri"
        r.font.size = Pt(9)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    her_data = [
        ("Wazuh SIEM & XDR", "Open Source (GPL)", "$0.00 / mes (Gratuito)", "Recolección y correlación de logs, detección y triaje en Módulo 3"),
        ("Wireshark & tcpdump", "Open Source (GPL)", "$0.00 / mes (Gratuito)", "Captura e inspección de protocolos web, TLS y DNS en Módulo 4"),
        ("Greenbone (OpenVAS)", "Open Source", "$0.00 / mes (Gratuito)", "Escaneo de vulnerabilidades y lectura de avisos en Módulo 5"),
        ("Oracle VirtualBox / VMs", "Open Source (GPL)", "$0.00 / mes (Gratuito)", "Despliegue de servidores Linux/Windows para prácticas de laboratorio"),
        ("Cisco Packet Tracer", "Cisco NetAcad", "$0.00 / mes (Gratuito)", "Simulación de topologías de red, switches y firewalls corporativos"),
        ("Cisco Snort IDS/IPS", "Cisco Talos (GPL)", "$0.00 / mes (Gratuito)", "Detección de tráfico de intrusión basada en firmas (reglas comunitarias)"),
        ("Cisco Modeling Labs (CML)\n[Herramienta Opcional]", "Cisco Comercial", "$199.00 USD / año\n(~$16.58 USD / mes)", "Emulación avanzada para instructor (no requerida para alumnos)")
    ]

    for idx, (nom, tip, cos, fun) in enumerate(her_data, start=1):
        row = tbl_her.rows[idx]
        if idx % 2 == 1:
            for c in row.cells:
                set_cell_background(c, "F7FAFC")
        for c_idx, val in enumerate([nom, tip, cos, fun]):
            cell = row.cells[c_idx]
            set_cell_margins(cell, top=60, bottom=60, left=70, right=70)
            p = cell.paragraphs[0]
            style_p(p, space_before=0, space_after=0)
            r = p.add_run(val)
            r.font.name = "Calibri"
            r.font.size = Pt(8.5)
            r.font.color.rgb = COLOR_DARK
            if c_idx == 0:
                r.font.bold = True

    # ==========================================
    # ## Referencias Oficiales
    # ==========================================
    h2_ref = doc.add_paragraph()
    style_p(h2_ref, space_before=12, space_after=4)
    run_h2_ref = h2_ref.add_run("Referencias Oficiales para la Preparación Docente:")
    run_h2_ref.font.name = "Calibri"
    run_h2_ref.font.size = Pt(12)
    run_h2_ref.font.bold = True
    run_h2_ref.font.color.rgb = COLOR_PRIMARY

    referencias = [
        ("Microsoft Learn:", "SIEM y registros de seguridad de Windows — https://learn.microsoft.com/en-us/azure/sentinel/overview"),
        ("NIST SP 800-207:", "Zero Trust Architecture — https://www.nist.gov/publications/zero-trust-architecture"),
        ("PeopleCert:", "Prácticas de gestión de servicios de ITIL — https://www.peoplecert.org/browse-certifications/it-governance-and-service-management/itil-practice-manager"),
        ("IETF RFC 6749 y RFC 9700:", "OAuth 2.0 y Security Best Current Practice — https://www.rfc-editor.org/rfc/rfc9700.html"),
        ("OpenID Foundation:", "OpenID Connect Core 1.0 — https://openid.net/specs/openid-connect-core-1_0.html"),
        ("IETF RFC 8996:", "Deprecating TLS 1.0 and TLS 1.1 — https://www.rfc-editor.org/rfc/rfc8996"),
        ("NIST NVD:", "Vulnerability Detail Pages — https://nvd.nist.gov/vuln/Vulnerability-Detail-Pages"),
        ("PCI SSC:", "PCI DSS y biblioteca de documentos — https://www.pcisecuritystandards.org/standards/pci-dss/"),
        ("ISO:", "ISO/IEC 27001:2022 Information Security Management — https://www.iso.org/standard/27001"),
        ("HHS:", "Summary of the HIPAA Security Rule — https://www.hhs.gov/hipaa/for-professionals/security/laws-regulations/index.html"),
        ("AICPA y CIMA:", "SOC Suite of Services (SOC 1 y SOC 2) — https://www.aicpa-cima.com/resources/landing/system-and-organization-controls-soc-suite-of-services")
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
    run_f = footer_p.add_run("Fundación Kinal | Ciberseguridad y Fundamentos de Seguridad de la Información — Temario Oficial")
    run_f.font.name = "Calibri"
    run_f.font.size = Pt(8.5)
    run_f.font.color.rgb = COLOR_SECONDARY

    out_dir = os.path.join("Cursos", "Ciberseguridad")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "Temario_Curso_Ciberseguridad_Kinal.docx")
    doc.save(out_path)
    print(f"Temario guardado con éxito en: {out_path}")

if __name__ == "__main__":
    generate_temario_doc()
