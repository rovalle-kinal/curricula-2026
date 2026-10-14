#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador del Archivo Temporal 'mecanica_temporal.html'
Alinea la maquetación gráfica de los pensums de Mecánica con el estándar de Construcción:
- Una tarjeta por módulo en cuadrícula de 2 columnas (grid lg:grid-cols-2 gap-8 pt-4).
- Cada tarjeta de módulo con encabezado oscuro (bg-slate-900 text-white), logro esperado y duración.
- Todos los temas del módulo apilados dentro de la tarjeta de ese módulo.
- Filtros interactivos funcionales para cada curso.
"""

from bs4 import BeautifulSoup
import re
import os

SOURCE_HTML = r"D:\OneDrive\Software\Antigravity\Diseño Instruccional\mecanica.html"
OUTPUT_HTML = r"D:\OneDrive\Software\Antigravity\Diseño Instruccional\mecanica_temporal.html"

# Metadata pedagógica de los módulos
MODULE_METADATA = {
    "mantenimiento_mecanico": [
        {
            "num": 1,
            "weeks": "Semanas 1 a 4",
            "hours": "18 Horas",
            "logro": "Aplicar metrología dimensional con pie de rey, micrómetro y reloj comparador según sistema métrico e inglés, reconociendo los tipos de mantenimiento industrial."
        },
        {
            "num": 2,
            "weeks": "Semanas 5 a 8",
            "hours": "18 Horas",
            "logro": "Inspeccionar, desmontar y seleccionar tornillería de alta resistencia (grado 5 y 8), chavetas, pasadores y resortes según esfuerzos de tracción y cizallamiento."
        },
        {
            "num": 3,
            "weeks": "Semanas 9 a 12",
            "hours": "18 Horas",
            "logro": "Montar, alinear con emisor láser y tensar sistemas de transmisión por fajas en V, sincronizadas y cadenas de rodillos bajo normas ISO/RMA."
        },
        {
            "num": 4,
            "weeks": "Semanas 13 a 16",
            "hours": "18 Horas",
            "logro": "Determinar relaciones de transmisión, holgura entre dientes (backlash) y patrones de contacto en engranajes rectos, helicoidales y reductores de velocidad."
        },
        {
            "num": 5,
            "weeks": "Semanas 17 a 20",
            "hours": "18 Horas",
            "logro": "Seleccionar aceites y grasas industriales según grado ISO VG, viscosidad cSt y compatibilidad de espesantes, elaborando cartas de lubricación de planta."
        },
        {
            "num": 6,
            "weeks": "Semanas 21 a 24",
            "hours": "18 Horas",
            "logro": "Instalar rodamientos mediante calentador de inducción térmica magnética y alinear acoplamientos rígidos y flexibles con reloj palpador y tecnología láser."
        },
        {
            "num": 7,
            "weeks": "Semanas 25 a 28",
            "hours": "18 Horas",
            "logro": "Desarmar, evaluar cavitación, balancear impulsores y reemplazar empaquetaduras y sellos mecánicos en bombas centrífugas de procesos industriales."
        },
        {
            "num": 8,
            "weeks": "Semanas 29 a 32",
            "hours": "18 Horas",
            "logro": "Ejecutar protocolos de bloqueo y etiquetado (LOTO / OSHA 1910.147), análisis de riesgos en caliente y uso normado de EPP según Acuerdo Gub. 229-2014."
        },
        {
            "num": 9,
            "weeks": "Semanas 33 a 36",
            "hours": "18 Horas",
            "logro": "Gestionar órdenes de trabajo digitales en software CMMS/EAM, calculando indicadores MTBF, MTTR y disponibilidad mecánica de líneas de producción."
        },
        {
            "num": 10,
            "weeks": "Semanas 37 a 40",
            "hours": "18 Horas",
            "logro": "Implementar pilares de Mantenimiento Autónomo (TPM), inspección por análisis de vibraciones y optimización de OEE en celdas de manufactura."
        }
    ],
    "soldadura_industrial": [
        {
            "num": 1,
            "weeks": "Semanas 1 a 4",
            "hours": "18 Horas",
            "logro": "Configurar equipos oxiacetilénicos con válvulas arrestallamas, regular presiones de trabajo y ejecutar soldaduras autógenas con varilla de aporte en taller."
        },
        {
            "num": 2,
            "weeks": "Semanas 5 a 8",
            "hours": "18 Horas",
            "logro": "Operar sopletes de oxicorte y equipos de corte por plasma CNC/manual para biselado y dimensionamiento de planchas de acero estructural según AWS C4.1."
        },
        {
            "num": 3,
            "weeks": "Semanas 9 a 12",
            "hours": "18 Horas",
            "logro": "Dominar encendido de arco, control de longitud de arco y polaridades DCEP/DCEN con electrodos revestidos celulósicos y básicos (E6010, E6011 y E7018)."
        },
        {
            "num": 4,
            "weeks": "Semanas 13 a 16",
            "hours": "18 Horas",
            "logro": "Depositar cordones de filete en juntas en T y traslape en posiciones plana (1F) y horizontal (2F) con garganta uniforme y sin socavaciones."
        },
        {
            "num": 5,
            "weeks": "Semanas 17 a 20",
            "hours": "18 Horas",
            "logro": "Ejecutar pases de raíz, relleno y presentación en placas biseladas en V en posición 1G, cumpliendo criterios de inspección visual AWS D1.1."
        },
        {
            "num": 6,
            "weeks": "Semanas 21 a 24",
            "hours": "18 Horas",
            "logro": "Controlar el baño de fusión en progresión ascendente vertical (3G) y horizontal (2G) evitando descuelgue de escoria y porosidades internas."
        },
        {
            "num": 7,
            "weeks": "Semanas 25 a 28",
            "hours": "18 Horas",
            "logro": "Realizar cordones de soldadura de filete en posiciones de alta dificultad operativa (3F vertical ascendente y 4F sobrecabeza) bajo norma estructural."
        },
        {
            "num": 8,
            "weeks": "Semanas 29 a 32",
            "hours": "18 Horas",
            "logro": "Seleccionar electrodos inoxidables (E308L, E316L), precalentamiento para fundición gris con electrodos de níquel y soldadura TIG/SMAW de aleaciones especiales."
        },
        {
            "num": 9,
            "weeks": "Semanas 33 a 36",
            "hours": "18 Horas",
            "logro": "Calibrar voltaje, velocidad de alimentación de alambre y mezcla de gas (Ar/CO2) en fuentes MIG/MAG y alambre tubular FCAW para alta productividad fabril."
        },
        {
            "num": 10,
            "weeks": "Semanas 37 a 40",
            "hours": "18 Horas",
            "logro": "Soldar estructuras pesadas en posiciones forzadas con alambre sólido y tubular, aplicando ensayos no destructivos visuales (VT) y líquidos penetrantes (PT)."
        }
    ],
    "calderas_vapor": [
        {
            "num": 1,
            "weeks": "Semanas 1 a 8",
            "hours": "36 Horas",
            "logro": "Identificar componentes pirotubulares y acuotubulares, operar quemadores de búnker/GLP y verificar columnas de nivel y presostatos bajo código ASME Sección I."
        },
        {
            "num": 2,
            "weeks": "Semanas 9 a 16",
            "hours": "36 Horas",
            "logro": "Ejecutar secuencias seguras de purga de fondo y superficie, calibración de válvulas de seguridad ASME y respuesta ante emergencias de bajo nivel de agua."
        },
        {
            "num": 3,
            "weeks": "Semanas 17 a 24",
            "hours": "36 Horas",
            "logro": "Monitorear dureza, pH, sílice, fosfatos y oxígeno disuelto, dosificando secuestrantes y operando descalcificadores y desaireadores térmicos."
        },
        {
            "num": 4,
            "weeks": "Semanas 25 a 32",
            "hours": "36 Horas",
            "logro": "Evaluar pérdidas térmicas por gases de combustión con analizador electrónico (O2, CO, CO2), optimizar exceso de aire y calcular rendimiento térmico."
        },
        {
            "num": 5,
            "weeks": "Semanas 33 a 40",
            "hours": "36 Horas",
            "logro": "Diagnosticar trampas de vapor (mecánicas, termodinámicas y termostáticas), aislamientos de tuberías y recuperación de condensados hacia el tanque de alimentación."
        }
    ]
}


def build_module_card_html(mod_meta, mod_title, items):
    """
    Construye la tarjeta de módulo idéntica a la de construccion.html.
    """
    topics_html_list = []
    for idx, item in enumerate(items, 1):
        status = item.get('data-status', 'keep')
        # Title of topic
        title_span = item.find('span', class_=re.compile(r'font-bold'))
        raw_title = title_span.get_text(strip=True) if title_span else ""
        # Remove any existing leading number if present
        clean_title = re.sub(r'^\d+[\.\)]\s*', '', raw_title)
        
        # Badge
        badge_span = item.find('span', class_=re.compile(r'rounded'))
        badge_text = badge_span.get_text(strip=True) if badge_span else "🟢"
        
        # Color style
        if status == 'delete':
            item_cls = 'item-delete'
            badge_cls = 'bg-red-100 text-red-800'
        elif status == 'update':
            item_cls = 'item-update'
            badge_cls = 'bg-amber-100 text-amber-800'
        elif status == 'new':
            item_cls = 'item-new'
            badge_cls = 'bg-blue-100 text-blue-700'
        else: # keep
            item_cls = 'item-keep'
            badge_cls = 'bg-emerald-100 text-emerald-800'

        # Description / text
        p_desc = item.find('p')
        desc_text = p_desc.decode_contents() if p_desc else ""

        # Category / Linea formativa
        cat_div = item.find('div', class_=re.compile(r'uppercase'))
        cat_html = ""
        if cat_div:
            cat_html = f'<div class="text-[11px] font-medium text-slate-500 uppercase tracking-wider">{cat_div.get_text(strip=True)}</div>'

        topic_card = f"""
                            <div class="content-item {item_cls} p-3 rounded text-xs space-y-1" data-status="{status}">
                                <div class="flex justify-between items-center font-bold">
                                    <span>{idx}. {clean_title}</span>
                                    <span class="px-2 py-0.5 rounded text-xs font-bold whitespace-nowrap {badge_cls}">{badge_text}</span>
                                </div>
                                {cat_html}
                                <p class="text-slate-700 leading-relaxed">{desc_text}</p>
                            </div>"""
        topics_html_list.append(topic_card)

    all_topics_joined = "\n".join(topics_html_list)

    card_html = f"""
                    <!-- MÓDULO {mod_meta['num']} -->
                    <div class="bg-white rounded-xl border border-slate-300 shadow-sm overflow-hidden flex flex-col">
                        <div class="bg-slate-900 text-white p-4 border-b border-slate-800">
                            <div class="flex justify-between items-center text-xs text-amber-400 font-semibold mb-1">
                                <span>MÓDULO {mod_meta['num']} ({mod_meta['weeks']})</span>
                                <span>Duración: ~{mod_meta['hours']}</span>
                            </div>
                            <h4 class="text-lg font-bold">{mod_title}</h4>
                            <p class="text-xs text-slate-300 mt-1">
                                <strong>Logro esperado:</strong> {mod_meta['logro']}
                            </p>
                        </div>
                        <div class="p-5 divide-y divide-slate-100 flex-1 space-y-2">
{all_topics_joined}
                        </div>
                    </div>"""
    return card_html


def transform_mecanica():
    print(f"Leyendo archivo fuente: {SOURCE_HTML}")
    with open(SOURCE_HTML, 'r', encoding='utf-8') as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, 'html.parser')

    courses_config = [
        ("mantenimiento_mecanico", "Mantenimiento Mecánico Industrial", "propuesta_mantenimiento_mecanico"),
        ("soldadura_industrial", "Soldadura Industrial y Procesos de Unión", "propuesta_soldadura_industrial"),
        ("calderas_vapor", "Operación y Eficiencia Energética en Calderas de Vapor", "propuesta_calderas_vapor")
    ]

    for c_key, c_name, sec_id in courses_config:
        pane = soup.find('div', id=f'course-pane-{c_key}')
        if not pane:
            print(f"[WARN] No se encontró pane: course-pane-{c_key}")
            continue

        print(f"\nProcesando curso: {c_name} (pane: course-pane-{c_key})")
        
        # 1. Encontrar la Sección 3
        # Buscamos el h3 de sección 3
        sec3_heading = None
        for h3 in pane.find_all('h3'):
            if 'Distribución Modular' in h3.get_text():
                sec3_heading = h3
                break

        if not sec3_heading:
            print(f"[WARN] No se encontró encabezado de Sección 3 en {c_key}")
            continue

        sec3_tag = sec3_heading.find_parent('section')
        if not sec3_tag:
            # Si el h3 no está dentro de section, buscar su contenedor
            sec3_tag = sec3_heading.find_parent('div', class_=re.compile(r'bg-white rounded-2xl'))
        
        print(f"Sección 3 encontrada para {c_key}")

        # Extraer todos los módulos actuales
        mod_divs = []
        for div in pane.find_all('div', class_=re.compile(r'bg-slate-50/50')):
            h4 = div.find('h4')
            if h4:
                mod_divs.append((div, h4))

        print(f"Módulos detectados en {c_key}: {len(mod_divs)}")

        mod_metas = MODULE_METADATA.get(c_key, [])
        new_module_cards = []

        for idx, (mod_div, h4) in enumerate(mod_divs):
            mod_title = h4.get_text(strip=True)
            # Extraer topics
            items = mod_div.find_all('div', class_=re.compile(r'\bcontent-item\b'))
            
            # Metadata correspondiente
            if idx < len(mod_metas):
                meta = mod_metas[idx]
            else:
                meta = {
                    "num": idx + 1,
                    "weeks": f"Semanas {idx*4+1} a {(idx+1)*4}",
                    "hours": "18 Horas",
                    "logro": f"Dominio teórico y práctico de {mod_title} conforme a los estándares de la industria guatemalteca."
                }

            card_html = build_module_card_html(meta, mod_title, items)
            new_module_cards.append(card_html)

        # Construir la nueva Sección 3 idéntica a construccion.html
        # Contadores de items para los botones de filtro
        all_items = pane.find_all('div', class_=re.compile(r'\bcontent-item\b'))
        cnt_all = len(all_items)
        cnt_del = len([it for it in all_items if it.get('data-status') == 'delete'])
        cnt_upd = len([it for it in all_items if it.get('data-status') == 'update'])
        cnt_new = len([it for it in all_items if it.get('data-status') == 'new'])
        cnt_keep = len([it for it in all_items if it.get('data-status') == 'keep'])

        legend_html = """
                <!-- Código de Leyenda Explicativo -->
                <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3 text-xs">
                    <div class="p-3 rounded-lg border border-red-200 bg-red-50 text-red-900 flex items-start gap-2">
                        <span class="inline-block w-3 h-3 rounded-full bg-red-500 mt-0.5 shrink-0"></span>
                        <div>
                            <strong>Color Rojo (Eliminar):</strong> Temas o prácticas desfasadas retiradas para optimizar el tiempo de taller.
                        </div>
                    </div>
                    <div class="p-3 rounded-lg border border-yellow-300 bg-yellow-50 text-yellow-900 flex items-start gap-2">
                        <span class="inline-block w-3 h-3 rounded-full bg-yellow-500 mt-0.5 shrink-0"></span>
                        <div>
                            <strong>Color Amarillo (Actualizar):</strong> Temas existentes modernizados conforme a normas y tecnologías vigentes.
                        </div>
                    </div>
                    <div class="p-3 rounded-lg border border-blue-200 bg-blue-50 text-blue-900 flex items-start gap-2">
                        <span class="inline-block w-3 h-3 rounded-full bg-blue-500 mt-0.5 shrink-0"></span>
                        <div>
                            <strong>Color Azul (Nuevo Propuesto):</strong> Competencias altamente demandadas por empresas y plantas en Guatemala.
                        </div>
                    </div>
                    <div class="p-3 rounded-lg border border-emerald-200 bg-emerald-50 text-emerald-900 flex items-start gap-2">
                        <span class="inline-block w-3 h-3 rounded-full bg-emerald-500 mt-0.5 shrink-0"></span>
                        <div>
                            <strong>Color Verde (Mantener):</strong> Fundamentos mecánicos y operativos que conservan plena vigencia práctica.
                        </div>
                    </div>
                </div>"""

        new_sec3_html = f"""
        <!-- SECCIÓN 3: PROPUESTA CURRICULAR CON CÓDIGO DE COLOR -->
        <section id="{sec_id}" class="space-y-6">
            <div class="bg-white rounded-2xl border border-slate-200 p-6 sm:p-8 shadow-sm space-y-6">
                <div class="flex flex-wrap items-center justify-between gap-4 border-b border-slate-100 pb-4">
                    <div class="flex items-center gap-3">
                        <div class="p-2.5 rounded-lg bg-indigo-50 text-indigo-700">
                            <i data-lucide="git-merge" class="w-6 h-6"></i>
                        </div>
                        <div>
                            <h3 class="text-xl font-bold text-slate-900">
                                3. Distribución Modular Auditada con Código de Color
                            </h3>
                            <p class="text-sm text-slate-500">
                                Visualización interactiva que resalta exactamente qué eliminar, qué actualizar y qué incorporar según la demanda industrial.
                            </p>
                        </div>
                    </div>

                    <!-- Botones de Filtro -->
                    <div class="flex flex-wrap items-center gap-2 text-xs font-semibold no-print">
                        <button onclick="filterEtsItems('all', '{c_key}')" id="btn-all-{c_key}" class="px-3 py-1.5 rounded-lg bg-slate-900 text-white shadow-sm transition">Todos ({cnt_all})</button>
                        <button onclick="filterEtsItems('delete', '{c_key}')" id="btn-delete-{c_key}" class="px-3 py-1.5 rounded-lg bg-red-100 text-red-700 hover:bg-red-200 transition">🔴 Solo Eliminar ({cnt_del})</button>
                        <button onclick="filterEtsItems('update', '{c_key}')" id="btn-update-{c_key}" class="px-3 py-1.5 rounded-lg bg-amber-100 text-amber-800 hover:bg-amber-200 transition">🟡 Solo Actualizar ({cnt_upd})</button>
                        <button onclick="filterEtsItems('new', '{c_key}')" id="btn-new-{c_key}" class="px-3 py-1.5 rounded-lg bg-blue-100 text-blue-700 hover:bg-blue-200 transition">🔵 Solo Nuevos ({cnt_new})</button>
                        <button onclick="filterEtsItems('keep', '{c_key}')" id="btn-keep-{c_key}" class="px-3 py-1.5 rounded-lg bg-emerald-100 text-emerald-800 hover:bg-emerald-200 transition">🟢 Mantener ({cnt_keep})</button>
                    </div>
                </div>

                {legend_html}

                <!-- Cuadrícula Modular de Temarios (1 tarjeta por módulo) -->
                <div class="grid lg:grid-cols-2 gap-8 pt-4">
{''.join(new_module_cards)}
                </div>
            </div>
        </section>"""

        # Reemplazar la sección antigua por la nueva
        parsed_sec3 = BeautifulSoup(new_sec3_html, 'html.parser')
        sec3_tag.replace_with(parsed_sec3)
        print(f"[OK] Reemplazada exitosamente Sección 3 para {c_key}")

    # Guardar en archivo temporal
    result_html = str(soup)
    with open(OUTPUT_HTML, 'w', encoding='utf-8') as f:
        f.write(result_html)

    print(f"\n[ÉXITO] Archivo temporal generado: {OUTPUT_HTML} ({len(result_html)} bytes)")


if __name__ == '__main__':
    transform_mecanica()
