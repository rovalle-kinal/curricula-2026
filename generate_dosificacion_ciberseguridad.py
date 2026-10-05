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

def set_cell_margins(cell, top=60, bottom=60, left=80, right=80):
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

def generate_dosificacion_doc():
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
    # ENCABEZADO TÉCNICO INSTITUCIONAL
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
    r_esc = p_esc.add_run("Escuela Técnica Superior — Coordinación de Formación Continua y Empleabilidad")
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
    r_sub = p_sub.add_run("Ciberseguridad y Fundamentos de Seguridad de la Información (20 Sesiones de 4 Horas — 80 Horas)")
    r_sub.font.name = "Calibri"
    r_sub.font.size = Pt(12)
    r_sub.font.italic = True
    r_sub.font.color.rgb = COLOR_SECONDARY

    add_callout(doc, 
        "«El aprender en el proceso del trabajo es base y a la vez objetivo de la acción formativa». Las 80 horas corresponden a 20 encuentros de 240 minutos estructurados en 8 módulos progresivos. Cada sesión contempla 20 minutos de receso; por tanto, el tiempo de actividad formativa efectiva por encuentro es de 220 minutos (73 horas y 20 minutos en total). Las sesiones conectan cada concepto técnico con una empresa ficticia transversal (estaciones, red local, servidor, app web y SaaS). El calendario se organiza por sesiones consecutivas sin imponer fechas fijas de inicio. Nota mínima aprobatoria institucional: 75 puntos sobre 100.",
        bold_prefix="Organización Pedagógica Dual e Ideario Kinal:")

    # =========================================================================
    # 1. MATRIZ GENERAL CRONOLÓGICA DE LAS 20 SESIONES
    # =========================================================================
    h1_1 = doc.add_paragraph()
    style_heading(h1_1, "1. Matriz General de Dosificación de las 20 Sesiones (80 Horas)", level=1)

    sesiones_info = [
        ("Sesión 1", "Módulo 1: Sistemas y TI", "Fundamentos de seguridad: tríada CIA, activos, riesgos y clasificación", "Matriz CIA / Activos"),
        ("Sesión 2", "Módulo 1: Sistemas y TI", "Gestión de soporte ITIL: incidentes, solicitudes, cambios y SLAs", "Ticket ITIL con SLA"),
        ("Sesión 3", "Módulo 1: Sistemas y TI", "Redes, servidores, modelos IaaS/PaaS/SaaS y responsabilidad compartida", "Diagrama del Sistema"),
        ("Sesión 4", "Módulo 2: Identidad y Acceso", "Autenticación, validación, creación de sesión, expiración y revocación", "Flujo de Autenticación"),
        ("Sesión 5", "Módulo 2: Identidad y Acceso", "Autenticación multifactor (MFA), enrolamiento, fricción y phishing", "Procedimiento MFA"),
        ("Sesión 6", "Módulo 2: Identidad y Acceso", "SSO, federación, protocolos (SAML, LDAP, OAuth/OIDC) y matriz RBAC", "Matriz RBAC / Bajas"),
        ("Sesión 7", "Módulo 3: Controles y Resp.", "Mínimo privilegio, delimitación de alcance, fronteras y Zero Trust", "Ficha de Alcance / ZT"),
        ("Sesión 8", "Módulo 3: Controles y Resp.", "Segregación de funciones, matriz RACI, telemetría y lectura en SIEM", "Logs SIEM / Correlación"),
        ("Sesión 9", "Módulo 4: Comunicaciones Web", "Criptografía: simétrica, asimétrica, hashes, firmas y gestión de claves", "Tabla Criptográfica"),
        ("Sesión 10", "Módulo 4: Comunicaciones Web", "Protocolos HTTP vs HTTPS, handshake TLS y certificados X.509", "Inspección Certificado"),
        ("Sesión 11", "Módulo 4: Comunicaciones Web", "Cadena de CAs, proxies, componentes de red y seguridad en APIs REST", "Traza Web / Ficha API"),
        ("Sesión 12", "Módulo 5: Vulnerabilidades", "Ciclo de vida de hardware (EOL/EOS) y gestión de servicios SaaS", "Plan Ciclo de Vida"),
        ("Sesión 13", "Módulo 5: Vulnerabilidades", "Mantenimiento de servidores, parches de SO y software/dependencias", "Plan de Parches / Rollback"),
        ("Sesión 14", "Módulo 5: Vulnerabilidades", "Lectura de avisos CVE/CVSS, tratamiento y remediación de protocolos", "Ficha Tratamiento CVE"),
        ("Sesión 15", "Módulo 6: Documentación", "Jerarquía documental: políticas de seguridad corporativas y estándares", "Borrador de Política"),
        ("Sesión 16", "Módulo 6: Documentación", "Procedimientos SOP, evaluación de riesgos y aceptación temporal", "SOP Baja / Aceptación"),
        ("Sesión 17", "Módulo 7: Estándares", "Estándar PCI DSS (CDE) e ISO/IEC 27001 (SGSI y SoA)", "Cuadro Comparativo 1"),
        ("Sesión 18", "Módulo 7: Estándares", "Regulación HIPAA (ePHI) e informes de aseguramiento SOC 1 y SOC 2", "Cuadro Comparativo 2"),
        ("Sesión 19", "Módulo 8: Higiene e Incidentes", "Higiene digital, protección cotidiana, ingeniería social y phishing", "Reporte de Incidente"),
        ("Sesión 20", "Módulo 8: Higiene e Incidentes", "Proyecto Integrador: consolidación de expediente, defensa y clausura", "Expediente del Caso")
    ]

    tbl_matriz = doc.add_table(rows=len(sesiones_info) + 1, cols=4)
    tbl_matriz.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_matriz.autofit = False
    tbl_matriz.columns[0].width = Inches(1.1)
    tbl_matriz.columns[1].width = Inches(1.8)
    tbl_matriz.columns[2].width = Inches(2.3)
    tbl_matriz.columns[3].width = Inches(1.3)
    set_table_borders(tbl_matriz, color="CBD5E0", sz="4")

    hdr_m = tbl_matriz.rows[0]
    for c in hdr_m.cells:
        set_cell_background(c, "003366")
    headers_mat = ["Sesión (4h)", "Módulo Formativo", "Contenido Central del Encuentro", "Producto Observable"]
    for idx, text in enumerate(headers_mat):
        p = hdr_m.cells[idx].paragraphs[0]
        style_p(p, space_before=0, space_after=0)
        r = p.add_run(text)
        r.font.name = "Calibri"
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    for idx, (ses, mod, cont, prod) in enumerate(sesiones_info, start=1):
        row = tbl_matriz.rows[idx]
        if idx % 2 == 1:
            for c in row.cells:
                set_cell_background(c, "F7FAFC")
        for c_idx, val in enumerate([ses, mod, cont, prod]):
            cell = row.cells[c_idx]
            set_cell_margins(cell, top=45, bottom=45, left=55, right=55)
            p = cell.paragraphs[0]
            style_p(p, space_before=0, space_after=0)
            r = p.add_run(val)
            r.font.name = "Calibri"
            r.font.size = Pt(8)
            r.font.color.rgb = COLOR_DARK
            if c_idx in [0, 3]:
                r.font.bold = True

    doc.add_page_break()

    # =========================================================================
    # 2. MICRODISEÑO DIDÁCTICO DETALLADO DE LAS 20 SESIONES (MOMENTOS DIDÁCTICOS)
    # =========================================================================
    h1_2 = doc.add_paragraph()
    style_heading(h1_2, "2. Microdiseño Didáctico Detallado por Sesión (240 Minutos por Encuentro)", level=1)

    p_micro_intro = doc.add_paragraph()
    style_p(p_micro_intro, space_before=0, space_after=8)
    r = p_micro_intro.add_run("Cada una de las 20 sesiones formativas de 4 horas (240 minutos) se desglosa rigurosamente en tres momentos didácticos (Apertura 30 min, Desarrollo 160 min con Receso de 20 min, y Cierre 30 min), aplicando el principio del «trabajo bien hecho»:")
    r.font.name = "Calibri"
    r.font.size = Pt(10)
    r.font.color.rgb = COLOR_DARK

    sesiones_detalladas = [
        # MODULO 1
        ("Sesión 1", "Módulo 1: Sistemas y TI", "Fundamentos de Seguridad de la Información y Clasificación de Activos",
         "Distingue confidencialidad, integridad y disponibilidad en un caso laboral de la empresa ficticia.",
         "Presentación del curso, reglas de convivencia e ideario de Kinal. Planteamiento del caso de la empresa ficticia: fuga de información de clientes por correo.",
         "Exposición dialogada sobre la tríada CIA, amenazas y riesgos. Ejercicio guiado: inventario inicial de activos de la empresa ficticia y clasificación en pública, interna, confidencial y restringida.",
         "Puesta en común de clasificaciones. Registro en la Bitácora Berichtsheft sobre impacto de pérdida de integridad. Preguntas de verificación.",
         "Computadora, navegador, plantilla de inventario de activos, caso de estudio.",
         "Ficha de clasificación de activos con justificación de confidencialidad, integridad y disponibilidad."),

        ("Sesión 2", "Módulo 1: Sistemas y TI", "Soporte Técnico, Principios ITIL y Gestión de Servicios",
         "Clasifica una solicitud de servicio y documenta su atención con responsables y evidencia.",
         "Caso laboral: caída de servidor de facturación a fin de mes. Debate sobre impacto vs urgencia y diferencia entre falla técnica e incidente de seguridad.",
         "Principios ITIL aplicados al soporte: valor, colaboración y visibilidad. Flujo de mesa de servicio: solicitud, incidente, problema y cambio. Ejercicio: redacción de un ticket formal con SLA y escalamiento.",
         "Revisión de tickets en parejas. Registro en Berichtsheft sobre criterios de escalamiento. Reflexión ética sobre el compromiso de servicio.",
         "Plantilla de ticket de mesa de servicio, guía ITIL de Fundación Kinal.",
         "Ticket de mesa de servicio documentado con categoría, impacto, urgencia, responsable y evidencia de resolución."),

        ("Sesión 3", "Módulo 1: Sistemas y TI", "Redes, Sistemas Locales, Cloud y Modelo de Responsabilidad Compartida",
         "Lee y dibuja un diagrama básico explicando dependencias y límites de responsabilidad.",
         "Pregunta detonante: ¿si se cae el servicio SaaS de correo, de quién es la culpa? Discusión de responsabilidades.",
         "Análisis de servidores locales, virtuales, switches y enlaces WAN. Modelos IaaS, PaaS y SaaS. Ejercicio: diagramación lógica del sistema de la empresa ficticia delimitando qué gestiona la empresa y qué el proveedor.",
         "Inspección de diagramas de arquitectura. Registro en Berichtsheft de la matriz de responsabilidad compartida. Cierre del Módulo 1.",
         "Herramienta de diagramación (Draw.io / Lucidchart), ejemplos de arquitecturas cloud.",
         "Diagrama completo del sistema de la empresa ficticia con equipos, red, servidor y SaaS con delimitación de alcance."),

        # MODULO 2
        ("Sesión 4", "Módulo 2: Identidad y Acceso", "Autenticación, Validación y Ciclo de Vida de la Sesión",
         "Reconstruye el inicio, validación y cierre de una sesión, señalando quién valida cada paso.",
         "Caso real: usuario que dejó sesión abierta en equipo compartido y sufrió suplantación de identidad en sistema contable.",
         "Fases: identificación, prueba, validación, sesión, expiración y revocación. Roles del usuario, aplicación e IdP. Ejercicio: diagramar el ciclo de sesión distinguiendo que autenticar no otorga permiso universal.",
         "Revisión de flujos de sesión. Registro en Berichtsheft sobre directivas de expiración por inactividad. Verificación de comprensión.",
         "Diagramas de flujo de sesión, navegador web con consola de desarrollador (inspección de cookies de sesión sin credenciales reales).",
         "Flujo secuencial de ciclo de sesión documentado con eventos de expiración y revocación."),

        ("Sesión 5", "Módulo 2: Identidad y Acceso", "Autenticación Multifactor (MFA), Fricción y Resistencia a Phishing",
         "Compara factores y describe un procedimiento de enrolamiento y recuperación.",
         "Demostración de ataque de fatiga de MFA (MFA bombing) y por qué dos contraseñas no son dos factores.",
         "Análisis de factores: conocimiento, posesión e inherencia. Comparación de OTP, apps autenticadoras, push y llaves FIDO2. Ejercicio: redactar el procedimiento de enrolamiento y recuperación de factor perdido.",
         "Evaluación de procedimientos de recuperación. Registro en Berichtsheft sobre controles compensatorios ante pérdida de token.",
         "Aplicaciones autenticadoras de ejemplo, guías de enrolamiento MFA.",
         "Procedimiento operativo de enrolamiento y recuperación de MFA con controles sobre excepciones."),

        ("Sesión 6", "Módulo 2: Identidad y Acceso", "SSO, Federación, Protocolos de Acceso y Matriz RBAC",
         "Ubica protocolos (SAML, LDAP, OAuth, OIDC) y construye una matriz simple de roles y permisos.",
         "Dilema operativo: renuncia de un empleado clave con acceso a 10 sistemas SaaS. Riesgos de no tener SSO centralizado.",
         "Conceptos de SSO, SAML, LDAP, OAuth 2.0 y OIDC. Bearer tokens y flujo PKCE sin código. Matriz RBAC: usuario, grupo, rol y acción. Ejercicio: construir matriz RBAC y resolver baja inmediata de usuario.",
         "Inspección de matrices RBAC. Registro en Berichtsheft sobre revocación de tokens. Cierre formal del Módulo 2.",
         "Plantilla de matriz RBAC, diagramas de flujo OAuth/SAML.",
         "Matriz de roles y permisos RBAC y procedimiento de baja inmediata con revocación de sesiones."),

        # MODULO 3
        ("Sesión 7", "Módulo 3: Controles y Resp.", "Mínimo Privilegio, Fronteras de Confianza y Arquitectura Zero Trust",
         "Justifica cada permiso y redacta inclusiones, exclusiones y dependencias de un control.",
         "Discusión de la frase 'dar acceso total para que no dé problemas'. Consecuencias de roles genéricos excesivos.",
         "Principio de menor privilegio y regla deny by default. Separación de cuenta diaria y administrativa. Pilares de Zero Trust: verificación explícita y contexto. Ejercicio: definir el alcance y fronteras de un control.",
         "Revisión de redacción de controles: verificar que indiquen dónde actúan y su evidencia. Registro en Berichtsheft.",
         "Estándar NIST SP 800-207, plantilla de especificación de control.",
         "Ficha de diseño de control con alcance delimitado, exclusiones y justificación de mínimo privilegio."),

        ("Sesión 8", "Módulo 3: Controles y Resp.", "Segregación de Funciones, Matriz RACI y Trazabilidad en Logs y SIEM",
         "Lee registros básicos y correlaciona eventos para reconstruir un proceso, separando hechos de hipótesis.",
         "Presentación de un caso de fraude interno por autoaprobación de compras. Importancia de la segregación de funciones.",
         "Matriz RACI. Introducción a logs y SIEM: marcas de tiempo UTC, actor, origen, recurso, acción y resultado. Lectura práctica de registros de ejemplo: intentos fallidos 4625 seguidos de 4624, regla deny de firewall y error nómina.",
         "Construcción de la línea de tiempo del evento. Registro en Berichtsheft sobre la diferencia entre hecho e hipótesis. Cierre del Módulo 3.",
         "Registros de logs ficticios normalizados, plantilla de matriz RACI, visor de logs.",
         "Reconstrucción documentada de un incidente a partir de logs correlacionados y ticket de solicitud."),

        # MODULO 4
        ("Sesión 9", "Módulo 4: Comunicaciones Web", "Criptografía Aplicada, Algoritmos, Claves y Funciones Hash",
         "Distingue cifrado, hash y firma digital y explica el papel de la custodia de claves.",
         "Caso real: filtración de base de datos con contraseñas en texto claro vs contraseñas hasheadas con salt.",
         "Texto claro, algoritmo y clave. Cifrado simétrico (AES) vs asimétrico (RSA). Integridad con SHA-256. Demostración práctica con CyberChef: cálculo de hashes y cifrado. Aclaración: hash no es cifrado reversible.",
         "Comprobación de conceptos criptográficos. Registro en Berichtsheft sobre algoritmos recomendados vs obsoletos.",
         "Herramienta web CyberChef, generadores de hash, ejemplos de pares de claves.",
         "Tabla comparativa de primitivas criptográficas con casos de uso en tránsito y en reposo."),

        ("Sesión 10", "Módulo 4: Comunicaciones Web", "Protocolos HTTP, HTTPS, Handshake TLS y Certificados Digitales",
         "Describe el establecimiento conceptual de una conexión HTTPS e inspecciona un certificado.",
         "¿El candado verde en el navegador garantiza que el sitio web no es una estafa? Análisis crítico.",
         "Estructura HTTP (métodos, códigos de estado, cabeceras). Negociación TLS: autenticación de servidor y acuerdo de claves. Estructura del certificado X.509: dominio (SAN), emisor, vigencia y clave pública.",
         "Inspección guiada de certificados de sitios web autorizados. Registro en Berichtsheft sobre advertencias de certificados vencidos.",
         "Navegador web, visor de certificados X.509, capturas de handshake TLS en Wireshark.",
         "Ficha de análisis de un certificado digital identificando emisor, vigencia, SAN y validez."),

        ("Sesión 11", "Módulo 4: Comunicaciones Web", "Cadena de Confianza, Recorrido Web, Proxies y Seguridad en APIs",
         "Identifica componentes del recorrido web y propone controles básicos sobre un endpoint de API.",
         "Trazado del viaje de un paquete desde el navegador hasta la base de datos de un banco.",
         "Jerarquía de CAs (raíz, intermedia). Funciones de DNS, router, firewall y proxy (directo e inverso). Inspección de metadatos y terminación TLS. Seguridad en APIs: endpoints, tokens Bearer, Rate Limiting.",
         "Construcción del diagrama de recorrido web y ficha de control de API. Registro en Berichtsheft. Cierre del Módulo 4.",
         "Herramienta de diagramación, ejemplos de peticiones HTTP a APIs REST ficticias.",
         "Diagrama de recorrido web completo y especificación de controles sobre un endpoint de API expuesto."),

        # MODULO 5
        ("Sesión 12", "Módulo 5: Vulnerabilidades", "Ciclo de Vida de Activos de Hardware y Gestión de Servicios Tercerizados",
         "Define un ciclo de vida de hardware y establece compromisos de seguridad con proveedores SaaS.",
         "Caso laboral: conmutador de red de 10 años que deja de recibir parches de seguridad (End of Support).",
         "Etapas del hardware: adquisición, operación, mantenimiento, EOL y retiro seguro. Gestión de servicios SaaS: seguimiento de notas de versión, fechas de deprecación y exportación de datos al cancelar contrato.",
         "Revisión de planes de ciclo de vida. Registro en Berichtsheft sobre borrado seguro y disposición de discos.",
         "Plantilla de inventario de ciclo de vida de hardware y contratos SaaS de ejemplo.",
         "Plan de ciclo de vida de activos con fechas EOL/EOS y estrategia de retiro seguro documentada."),

        ("Sesión 13", "Módulo 5: Vulnerabilidades", "Servidores, Sistemas Operativos, Software y Dependencias",
         "Propone actualización o retiro según soporte y gestiona ventanas de cambios con plan de reversión.",
         "Caso real: actualización de servidor que dejó inoperativa la base de datos contable por falta de plan de reversión.",
         "Versiones de SO y estado de soporte. Gestión de cambios de parches: inventario, respaldo comprobado, pruebas en staging, ventana de mantenimiento y rollback. Software: bibliotecas y dependencias compartidas.",
         "Simulación de un plan de ventana de parcheo. Registro en Berichtsheft sobre requisitos de aprobación previa.",
         "Procedimiento estándar de gestión de cambios (ITIL), plantilla de plan de marcha atrás.",
         "Plan de aplicación de parches de servidor con verificación de respaldo y procedimiento de rollback."),

        ("Sesión 14", "Módulo 5: Vulnerabilidades", "Lectura y Tratamiento de Vulnerabilidades (CVE, CVSS y Avisos Oficiales)",
         "Interpreta un aviso CVE/CVSS y formula una acción técnica verificable para el activo afectado.",
         "Lectura guiada de un boletín de seguridad real de fabricante (ej. vulnerabilidad en servidor web o biblioteca).",
         "Estructura del CVE, métricas CVSS (base vs severidad real según exposición). Opciones de tratamiento: parche, mitigación temporal, ajuste de configuración o retiro. Caso TLS 1.0 como protocolo obsoleto.",
         "Elaboración del plan de tratamiento para el aviso asignado. Registro en Berichtsheft. Cierre del Módulo 5.",
         "Base de datos NIST NVD, avisos oficiales de seguridad de Microsoft y Apache.",
         "Ficha de tratamiento de vulnerabilidad CVE con severidad CVSS, mitigación justificada y prueba de validación."),

        # MODULO 6
        ("Sesión 15", "Módulo 6: Documentación", "Estructura Documental y Redacción de Políticas de Seguridad",
         "Redacta una regla de política con alcance, responsable y forma de verificar su cumplimiento.",
         "Análisis de políticas redactadas de forma ambigua ('los usuarios deben ser cuidadosos') y por qué no funcionan.",
         "Pirámide documental: políticas, estándares, SOPs y guías. Elementos mandatorios: propósito, alcance explícito, reglas obligatorias, responsables, excepciones y aprobación. Ejercicio: redactar política de accesos.",
         "Revisión cruzada de políticas entre estudiantes. Registro en Berichtsheft sobre control de versiones y aprobaciones.",
         "Plantilla institucional de política de seguridad de la información.",
         "Documento formal de Política de Control de Accesos con alcance, responsables y métricas de verificación."),

        ("Sesión 16", "Módulo 6: Documentación", "Procedimientos SOP, Evaluación de Riesgos y Aceptación Temporal",
         "Describe un SOP ejecutable y formula una solicitud de aceptación temporal para autoridad competente.",
         "Caso de estudio: servidor antiguo no actualizable que soporta una línea crítica de manufactura.",
         "Estructura de SOP: pasos secuenciales, roles y criterio de cierre. Matriz de riesgos: impacto, probabilidad, riesgo inherente y residual. Solicitud de aceptación de riesgo: motivo, controles compensatorios y vigencia.",
         "Inspección de SOPs y solicitudes de aceptación. Registro en Berichtsheft. Cierre formal del Módulo 6.",
         "Plantilla de SOP (Procedimiento Operativo Estándar), matriz de evaluación de riesgos.",
         "SOP de baja de usuarios y formato de solicitud de aceptación temporal de riesgo debidamente justificado."),

        # MODULO 7
        ("Sesión 17", "Módulo 7: Estándares", "Estándar PCI DSS (Datos de Tarjeta) y Sistema de Gestión ISO/IEC 27001",
         "Identifica datos de pago, delimita el entorno CDE y relaciona riesgos con los requisitos de ISO 27001.",
         "¿Toda empresa que acepta pagos con tarjeta debe certificarse en PCI DSS? Análisis de aplicabilidad.",
         "PCI DSS: protección de datos de tarjetahabiente, Entorno de Datos del Titular (CDE) y segmentación. ISO/IEC 27001:2022: estructura del SGSI, liderazgo, evaluación de riesgos, SoA y mejora continua (2h cada tema).",
         "Comparación de objetivos entre estándar técnico (PCI) y norma de gestión (ISO). Registro en Berichtsheft.",
         "Estándar PCI DSS v4.0 (resumen), norma ISO/IEC 27001:2022 (estructura de cláusulas y controles Anexo A).",
         "Matriz comparativa de aplicabilidad entre PCI DSS e ISO 27001 para la empresa ficticia."),

        ("Sesión 18", "Módulo 7: Estándares", "Regulación HIPAA (ePHI) e Informes de Aseguramiento SOC 1 y SOC 2",
         "Reconoce cuándo aplica HIPAA y distingue el objeto de un informe SOC 1 vs SOC 2 (Tipo I y Tipo II).",
         "Caso de empresa guatemalteca de software que brinda soporte a clínicas en EE.UU.: obligaciones de HIPAA y SOC.",
         "HIPAA: datos de salud protegidos (ePHI), salvaguardas administrativas, físicas y técnicas. Informes SOC: SOC 1 (financiero) vs SOC 2 (servicios de confianza); Tipo I (a una fecha) vs Tipo II (período de eficacia).",
         "Lectura guiada de extractos de un informe SOC 2 ficticio: opinión del auditor y excepciones. Registro en Berichtsheft. Cierre M7.",
         "Guía de la regla de seguridad de HIPAA, ejemplos de informes SOC 2 con datos simulados.",
         "Ficha de análisis de aplicabilidad de HIPAA y criterios de interpretación de un informe SOC 2 Tipo II."),

        # MODULO 8
        ("Sesión 19", "Módulo 8: Higiene e Incidentes", "Higiene Digital, Ingeniería Social, Phishing y Respuesta Inicial",
         "Identifica señales de ingeniería social, documenta un evento y ejecuta reporte inicial sin alterar evidencia.",
         "Simulación de correo electrónico fraudulento urgente solicitando cambio de cuenta bancaria de proveedor.",
         "Higiene digital: contraseñas, MFA y bloqueo de pantalla. Ingeniería social: phishing, smishing, vishing y quishing. Señales de alarma y verificación out-of-band. Protocolo de reporte inicial: qué, cuándo, quién y acciones.",
         "Simulación de llenado de reporte de incidente de seguridad. Registro en Berichtsheft. Preparación para sesión final.",
         "Muestras de correos phishing simulados, formato de reporte de incidentes de seguridad.",
         "Reporte formal de incidente de seguridad por intento de phishing con cadena de custodia inicial."),

        ("Sesión 20", "Módulo 8: Higiene e Incidentes", "Proyecto Integrador: Presentación del Expediente de Seguridad y Clausura",
         "Sustenta un conjunto coherente de controles con alcance, responsables y evidencias ante jurado evaluador.",
         "Apertura de la jornada final de evaluación. Presentación de los criterios de la rúbrica y bienvenida a autoridades de Kinal.",
         "Sustentación individual y por células del Expediente de Seguridad del Caso Transversal (diagramas, RBAC, logs, ciclo de vida, políticas, SOPs, riesgos y respuesta). Ronda de preguntas técnicas de justificación.",
         "Revisión final y firma oficial de la Bitácora Berichtsheft. Deliberación y entrega de notas finales (aprobatorio ≥ 75 pts). Acto de clausura y reflexión final sobre los valores de servicio y trabajo bien hecho.",
         "Expedientes de seguridad completos, rúbrica analítica del proyecto, bitácoras de taller Berichtsheft.",
         "Expediente de Seguridad del Caso aprobado y sustentado con nota mínima de suficiencia (≥ 75 / 100 puntos).")
    ]

    for ses in sesiones_detalladas:
        h2_s = doc.add_paragraph()
        style_heading(h2_s, f"{ses[0]}: {ses[2]} ({ses[1]})", level=2)

        tbl_s = doc.add_table(rows=6, cols=2)
        tbl_s.alignment = WD_TABLE_ALIGNMENT.CENTER
        tbl_s.autofit = False
        tbl_s.columns[0].width = Inches(1.8)
        tbl_s.columns[1].width = Inches(4.7)
        set_table_borders(tbl_s, color="CBD5E0", sz="4")

        filas_s = [
            ("Objetivo de la Sesión:", ses[3]),
            ("Apertura / Inicio (30 min):", ses[4]),
            ("Desarrollo Práctico (160 min):", f"{ses[5]}\n[Incluye Receso Formativo de 20 min intermedio]"),
            ("Cierre / Consolidación (30 min):", ses[6]),
            ("Recursos y Materiales:", ses[7]),
            ("Producto Observable:", ses[8])
        ]

        for r_idx, (etq, txt) in enumerate(filas_s):
            row = tbl_s.rows[r_idx]
            set_cell_background(row.cells[0], "F7FAFC")
            set_cell_margins(row.cells[0], top=50, bottom=50, left=70, right=70)
            set_cell_margins(row.cells[1], top=50, bottom=50, left=70, right=70)

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
    # 3. RÚBRICAS ANALÍTICAS DE EVALUACIÓN INSTITUCIONAL (≥ 75 PUNTOS)
    # =========================================================================
    h1_3 = doc.add_paragraph()
    style_heading(h1_3, "3. Instrumentos y Rúbricas Analíticas de Evaluación (Normativa Kinal)", level=1)

    p_rub_desc = doc.add_paragraph()
    style_p(p_rub_desc, space_before=0, space_after=8)
    r = p_rub_desc.add_run("Toda comprobación y entrega se califica sobre 100 puntos, con un umbral de aprobación técnica de 75 puntos. Los criterios analíticos oficiales del Proyecto Integrador son:")
    r.font.name = "Calibri"
    r.font.size = Pt(10)
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

    hdr_r = tbl_rub.rows[0]
    for c in hdr_r.cells:
        set_cell_background(c, "003366")
    headers_rub = ["Criterio Evaluado", "Sólido / Excelente\n(90 - 100 pts)", "Satisfactorio\n(80 - 89 pts)", "Parcial / Mínimo\n(75 - 79 pts)", "Insuficiente\n(< 75 pts)"]
    for idx, text in enumerate(headers_rub):
        p = hdr_r.cells[idx].paragraphs[0]
        style_p(p, space_before=0, space_after=0)
        r = p.add_run(text)
        r.font.name = "Calibri"
        r.font.size = Pt(8.5)
        r.font.bold = True
        r.font.color.rgb = RGBColor(255, 255, 255)

    criterios_rub = [
        ("Corrección Conceptual y Distinción de Funciones\n(Peso: 25%)", 
         "Distingue con total precisión identidad, acceso, transporte, hashing y cifrado sin confundir conceptos.", 
         "Distingue las funciones técnicas principales con mínimas precisiones requeridas en clase.", 
         "Comprensión básica de funciones pero requiere aclaración menor en protocolos o factores MFA.", 
         "Confunde autenticación con autorización, o hash con cifrado reversible de manera crítica."),
        
        ("Alcance Explícito y Coherencia Documental\n(Peso: 20%)", 
         "Delimita claramente qué cubre cada control y mantiene coherencia total entre diagramas, flujos y políticas.", 
         "Delimitación clara del alcance con coherencia adecuada entre los documentos del expediente.", 
         "Alcance delimitado pero con ambigüedades menores en límites con servicios de terceros.", 
         "Propone 'aplica a todo' sin inventario verificable o presenta documentos desarticulados e incoherentes."),
        
        ("Controles y Tratamiento de Riesgos Justificados\n(Peso: 25%)", 
         "Justifica de forma técnica y operativa cada control, escenario de riesgo y mitigación propuesta.", 
         "Justificación técnica sólida para la mayoría de controles y riesgos evaluados.", 
         "Propone controles pertinentes pero su justificación técnica de riesgo residual es esquemática.", 
         "Controles arbitrarios sin sustento de riesgo o acepta riesgos sin autoridad ni compensaciones."),
        
        ("Responsables y Evidencia de Trazabilidad\n(Peso: 20%)", 
         "Asigna roles RACI explícitos y define evidencias verificables (logs, tickets, hashes) para cada control.", 
         "Asigna responsables claros y describe evidencias observables suficientes para auditoría.", 
         "Indica responsables pero las evidencias propuestas son genéricas o de difícil verificación.", 
         "Controles sin responsable asignado o carentes de evidencia de comprobación y cierre."),
        
        ("Claridad en la Presentación y Respuestas\n(Peso: 10%)", 
         "Defensa técnica serena, fluida, profesional y respuestas precisas que demuestran dominio del caso.", 
         "Presentación clara y respuestas acertadas a las preguntas del panel evaluador.", 
         "Exposición entendible pero con dudas menores al justificar decisiones ante preguntas del jurado.", 
         "Incapaz de explicar el expediente presentado o evade responder sobre las evidencias técnicas.")
    ]

    for idx, (crit, sol, sat, par, ins) in enumerate(criterios_rub, start=1):
        row = tbl_rub.rows[idx]
        if idx % 2 == 1:
            for c in row.cells:
                set_cell_background(c, "F7FAFC")
        for c_idx, val in enumerate([crit, sol, sat, par, ins]):
            cell = row.cells[c_idx]
            set_cell_margins(cell, top=55, bottom=55, left=65, right=65)
            p = cell.paragraphs[0]
            style_p(p, space_before=0, space_after=0)
            r = p.add_run(val)
            r.font.name = "Calibri"
            r.font.size = Pt(8)
            r.font.color.rgb = COLOR_DARK
            if c_idx == 0:
                r.font.bold = True

    # =========================================================================
    # 4. FORMATO GUÍA DE LA BITÁCORA DEL APRENDIZ (BERICHTSHEFT)
    # =========================================================================
    h1_4 = doc.add_paragraph()
    style_heading(h1_4, "4. Formato Guía de la Bitácora del Aprendiz (Berichtsheft)", level=1)

    p_ber_desc = doc.add_paragraph()
    style_p(p_ber_desc, space_before=0, space_after=8)
    r = p_ber_desc.add_run("En cumplimiento del Sistema Dual de Kinal, el estudiante debe registrar cada sesión en su Bitácora de Aprendizaje y Trazabilidad (Berichtsheft), consolidando el hábito del trabajo bien hecho:")
    r.font.name = "Calibri"
    r.font.size = Pt(10)
    r.font.color.rgb = COLOR_DARK

    tbl_b_fmt = doc.add_table(rows=7, cols=2)
    tbl_b_fmt.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_b_fmt.autofit = False
    tbl_b_fmt.columns[0].width = Inches(2.2)
    tbl_b_fmt.columns[1].width = Inches(4.3)
    set_table_borders(tbl_b_fmt, color="CBD5E0", sz="4")

    formato_data = [
        ("Nombre del Estudiante y Carné:", "___________________________________________________________"),
        ("Sesión del Programa y Fecha:", "Sesión No. _____ (4 horas)  |  Fecha: _____ / _____ / 2026"),
        ("Módulo y Concepto Central:", "[ ] M1 Sistemas   [ ] M2 Identidad   [ ] M3 Controles   [ ] M4 Web   [ ] M5 Vulns   [ ] M6 Docs   [ ] M7 Normas   [ ] M8 Higiene"),
        ("Situación Laboral del Caso Analizada:", "Descripción del problema o requerimiento analizado sobre la empresa ficticia."),
        ("Controles Diseñados y Evidencias:", "Detalle de los controles propuestos, responsables asignados y pruebas de cierre."),
        ("Dificultad Superada («Trabajo Bien Hecho»):", "Registro de dudas conceptuales o técnicas resueltas durante el encuentro."),
        ("Firma del Estudiante y Vo.Bo. del Docente:", "Firma Estudiante: ___________________  |  Firma Docente: ___________________")
    ]

    for idx, (campo, lineas) in enumerate(formato_data):
        row = tbl_b_fmt.rows[idx]
        set_cell_background(row.cells[0], "F7FAFC")
        set_cell_margins(row.cells[0], top=55, bottom=55, left=75, right=75)
        set_cell_margins(row.cells[1], top=55, bottom=55, left=75, right=75)

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

    section = doc.sections[0]
    footer = section.footer
    footer_p = footer.paragraphs[0]
    style_p(footer_p, space_before=0, space_after=0)
    footer_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run_f = footer_p.add_run("Fundación Kinal | Ciberseguridad y Fundamentos de Seguridad de la Información — Dosificación Oficial")
    run_f.font.name = "Calibri"
    run_f.font.size = Pt(8.5)
    run_f.font.color.rgb = COLOR_SECONDARY

    out_dir = os.path.join("Cursos", "Ciberseguridad")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "Dosificacion_y_Secuencia_Didactica_Ciberseguridad.docx")
    doc.save(out_path)
    print(f"Dosificación guardada con éxito en: {out_path}")

if __name__ == "__main__":
    generate_dosificacion_doc()
