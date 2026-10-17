#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para alinear y estandarizar las tarjetas modulares de electricidad.html
idéntico a la maqueta dorada de construccion.html.
Moderniza los 29 módulos de:
- Controles y Máquinas Eléctricas (10 módulos)
- Electrónica Analógica y Digital (10 módulos)
- Controladores Lógicos Programables (3 módulos)
- Automatización Industrial (6 módulos)
"""

import re
import os

WORKSPACE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TARGET_FILE = os.path.join(WORKSPACE_DIR, "electricidad.html")

MODULE_METADATA = {
    "controles_maquinas": {
        1: {"weeks": "1 a 4", "hours": "18", "achievement": "Analizar y calcular tensiones, corrientes y potencia en sistemas trifásicos equilibrados y desequilibrados en configuraciones estrella y delta bajo normativa CNEE/NEC."},
        2: {"weeks": "5 a 8", "hours": "18", "achievement": "Operar, mantener y diagnosticar generadores sincrónicos y asincrónicos industriales, verificando sincronización, regulación de voltaje y acoplamiento mecánico seguro."},
        3: {"weeks": "9 a 12", "hours": "18", "achievement": "Ejecutar pruebas de polaridad, relación de transformación, aislamiento y conexión de bancos de transformadores monofásicos y trifásicos en subestaciones."},
        4: {"weeks": "13 a 16", "hours": "18", "achievement": "Conectar, parametrizar y proteger motores de inducción jaula de ardilla y rotor devanado conforme a placas características, clases de aislamiento y régimen de servicio."},
        5: {"weeks": "17 a 20", "hours": "18", "achievement": "Diseñar, cablear y verificar tableros de control electromagnético con contactores, relés auxiliares, botoneras e indicadores para arranques directos e inversiones de giro."},
        6: {"weeks": "21 a 24", "hours": "18", "achievement": "Implementar sistemas de arranque a tensión reducida (estrella-triángulo, autotransformador, arrancadores suaves) y circuitos de frenado dinámico y protección térmica."},
        7: {"weeks": "25 a 28", "hours": "18", "achievement": "Parametrizar, comisionar y diagnosticar convertidores de frecuencia (VFD) para control vectorial y escalar de velocidad, rampas de aceleración y enlaces de comunicación industrial."},
        8: {"weeks": "29 a 32", "hours": "18", "achievement": "Seleccionar, conectar y calibrar sensores discretos y analógicos (inductivos, capacitivos, ópticos, ultrasónicos) integrándolos a etapas de entrada de control."},
        9: {"weeks": "33 a 36", "hours": "18", "achievement": "Desarrollar e implementar programas de automatización en micro y nano autómatas (LOGO!, Zelio) mediante lógica de bloques (FBD) y contactos (LADDER)."},
        10: {"weeks": "37 a 40", "hours": "18", "achievement": "Estructurar rutinas avanzadas de control en autómatas programables industriales gestionando señales analógicas, contadores, temporizadores y alarmas operativas."}
    },
    "electronica_analogica": {
        1: {"weeks": "1 a 4", "hours": "18", "achievement": "Aplicar cálculo fasorial, trigonometría y números complejos en el análisis de ondas senoidales, armónicos y respuestas en frecuencia de circuitos de CA."},
        2: {"weeks": "5 a 8", "hours": "18", "achievement": "Medir con exactitud tensión, corriente, desfase y frecuencia utilizando osciloscopios digitales de almacenamiento, multímetros True-RMS y generadores de señales."},
        3: {"weeks": "9 a 12", "hours": "18", "achievement": "Resolver redes resistivas complejas y circuitos lineales mediante teoremas de Thevenin, Norton, superposición y máxima transferencia de potencia."},
        4: {"weeks": "13 a 16", "hours": "18", "achievement": "Analizar la respuesta transitoria y en régimen permanente de condensadores en circuitos RC, filtros de potencia y compensación reactiva industrial."},
        5: {"weeks": "17 a 20", "hours": "18", "achievement": "Evaluar el comportamiento electromagnético de bobinas, reactancias y núcleos ferromagnéticos en circuitos RL y filtros supresores de transitorios."},
        6: {"weeks": "21 a 24", "hours": "18", "achievement": "Diseñar y comprobar circuitos rectificadores monofásicos y trifásicos, recortadores y fijadores basados en diodos de silicio, Schottky y Zener."},
        7: {"weeks": "25 a 28", "hours": "18", "achievement": "Construir y calibrar fuentes reguladas lineales y conmutadas (SMPS) con protecciones contra sobrecorriente, cortocircuito y rizado residual."},
        8: {"weeks": "29 a 32", "hours": "18", "achievement": "Implementar configuraciones inversoras, no inversoras, sumadoras, comparadoras e instrumentación con Op-Amps para acondicionamiento de señales de precisión."},
        9: {"weeks": "33 a 36", "hours": "18", "achievement": "Acondicionar y linealizar señales de transductores resistivos, piezoeléctricos y termopares mediante puentes de Wheatstone y convertidores A/D."},
        10: {"weeks": "37 a 40", "hours": "18", "achievement": "Controlar cargas de alta potencia en CA y CC empleando SCR, TRIACs, MOSFETs de potencia e IGBTs con módulos de disparo aislados por optoacopladores."}
    },
    "control_programables": {
        1: {"weeks": "1 a 13", "hours": "60", "achievement": "Desarrollar sistemas embebidos de adquisición y procesamiento de datos utilizando puertos de E/S, buses I2C/SPI y conversión analógica-digital en tiempo real."},
        2: {"weeks": "14 a 27", "hours": "60", "achievement": "Programar y configurar autómatas industriales mediante lenguajes IEC 61131-3 (LADDER, FBD, ST) integrando direccionamiento modular y subrutinas operativas."},
        3: {"weeks": "28 a 40", "hours": "60", "achievement": "Integrar sistemas electroneumáticos y electrohidráulicos secuenciales accionados por salidas de PLC aplicando sensores de proximidad y válvulas distribuidoras."}
    },
    "automatizacion_industrial": {
        1: {"weeks": "1 a 7", "hours": "30", "achievement": "Proyectar, ensamblar y validar cuadros de automatización industrial combinando lógica electromagnética cableada con normas internacionales de seguridad funcional."},
        2: {"weeks": "8 a 14", "hours": "30", "achievement": "Calibrar transmisores de presión, nivel, flujo y temperatura con lazo de corriente estándar 4-20 mA y protocolo HART en bancos de prueba certificados."},
        3: {"weeks": "15 a 21", "hours": "30", "achievement": "Resolver algoritmos de lógica combinacional, enclavamientos y matrices booleanas para control seguro de maquinaria industrial en lenguajes IEC 61131-3."},
        4: {"weeks": "22 a 28", "hours": "30", "achievement": "Modelar y programar procesos continuos y secuenciales mediante Diagramas de Función Secuencial (GRAFCET/SFC) y máquinas de estados deterministas."},
        5: {"weeks": "29 a 34", "hours": "30", "achievement": "Configurar relés de control inteligente y relés de seguridad SIL/PL para paradas de emergencia, barreras ópticas y resguardos perimetrales de planta."},
        6: {"weeks": "35 a 40", "hours": "30", "achievement": "Interconectar equipos de planta mediante buses de campo y Ethernet Industrial (Modbus TCP, PROFINET), supervisándolos a través de interfaces HMI/SCADA e IIoT."}
    }
}

mod_pattern = re.compile(
    r'<div class=\"border border-slate-200 rounded-xl p-5 bg-slate-50/50 space-y-4\">'
    r'\s*<div class=\"flex items-center justify-between border-b border-slate-200 pb-3\">'
    r'\s*<div class=\"flex items-center gap-2\">'
    r'\s*<span class=\"w-7 h-7 rounded-lg bg-amber-600[^\"]*\">(\d+)</span>'
    r'\s*<h4[^>]*>(.*?)</h4>'
    r'\s*</div>'
    r'\s*<span[^>]*>.*?</span>'
    r'\s*</div>'
    r'\s*<div class=\"grid md:grid-cols-2 gap-3\">(.*?)</div>\s*</div>',
    re.DOTALL
)

def run():
    with open(TARGET_FILE, "r", encoding="utf-8") as f:
        html = f.read()

    original_len = len(html)
    original_items = len(re.findall(r'item-(?:keep|update|new|delete)', html))
    print(f"Original file length: {original_len}, items: {original_items}")

    panes = ['controles_maquinas', 'electronica_analogica', 'control_programables', 'automatizacion_industrial']

    for p in panes:
        meta = MODULE_METADATA[p]
        pane_id_str = f'id="course-pane-{p}"'
        pos = html.find(pane_id_str)
        if pos == -1:
            print(f"ERROR: {p} not found!")
            continue

        end = html.find('id="course-pane-', pos + len(pane_id_str))
        if end == -1:
            # last pane, find closing section or footer
            end = len(html)

        pane_text = html[pos:end]

        list_marker = '<!-- Listado de Módulos y Temas -->'
        m_idx = pane_text.find(list_marker)
        if m_idx == -1:
            print(f"ERROR: list_marker not found in {p}!")
            continue

        mods = list(mod_pattern.finditer(pane_text))
        print(f"Pane {p}: {len(mods)} modules found (expected {len(meta)})")
        if len(mods) != len(meta):
            print(f"Mismatch in {p}!")
            continue

        last_mod = mods[-1]
        # find closing </div> of space-y-8 after last_mod
        close_div_idx = pane_text.find('</div>', last_mod.end()) + len('</div>')

        cards_html = []
        for m in mods:
            num = int(m.group(1))
            title = m.group(2).strip()
            items = m.group(3).strip()
            # Standardize item styling to match construccion.html
            items = re.sub(
                r'class=\"content-item\s+item-([a-z]+)\s+p-3(?:\.5)?\s+rounded(?:-lg)?\s+text-xs\s+space-y-(?:1|1\.5)\"',
                r'class="content-item item-\1 p-3 rounded text-xs space-y-1"',
                items
            )

            info = meta[num]
            card = f"""                <div class="bg-white rounded-xl border border-slate-300 shadow-sm overflow-hidden flex flex-col">
                        <div class="bg-slate-900 text-white p-4 border-b border-slate-800">
                            <div class="flex justify-between items-center text-xs text-amber-400 font-semibold mb-1">
                                <span>MÓDULO {num} (Semanas {info['weeks']})</span>
                                <span>Duración: ~{info['hours']} Horas</span>
                            </div>
                            <h4 class="text-lg font-bold">{title}</h4>
                            <p class="text-xs text-slate-300 mt-1">
                                <strong>Logro esperado:</strong> {info['achievement']}
                            </p>
                        </div>
                        <div class="p-5 divide-y divide-slate-100 flex-1 space-y-2">

                            {items}

                        </div>
                </div>"""
            cards_html.append(card)

        cards_joined = "\n\n".join(cards_html)
        new_block = f"""<!-- Distribución Modular del Temario -->
            <div class="grid lg:grid-cols-2 gap-8 pt-4">

{cards_joined}

            </div>"""

        new_pane = pane_text[:m_idx] + new_block + pane_text[close_div_idx:]
        html = html[:pos] + new_pane + html[end:]

    new_len = len(html)
    new_items = len(re.findall(r'item-(?:keep|update|new|delete)', html))
    new_cards = len(re.findall(r'bg-white rounded-xl border border-slate-300 shadow-sm overflow-hidden flex flex-col', html))
    new_headers = len(re.findall(r'bg-slate-900 text-white p-4 border-b border-slate-800', html))

    print(f"Updated file length: {new_len}, items: {new_items} (original: {original_items})")
    print(f"Total cards: {new_cards}, Total headers: {new_headers}")

    if new_items != original_items:
        print("ERROR: Item count mismatch! File NOT written.")
        return

    if new_cards != 39 or new_headers != 39:
        print("ERROR: Expected 39 cards and headers! File NOT written.")
        return

    with open(TARGET_FILE, "w", encoding="utf-8") as f:
        f.write(html)
    print("SUCCESS: electricidad.html saved successfully.")

    # Replicate to mirror folders
    mirrors = [
        os.path.join(WORKSPACE_DIR, "Revision_Temarios", "electricidad.html"),
        os.path.join(WORKSPACE_DIR, "curricula-2026", "Revision_Temarios", "electricidad.html")
    ]
    for mir in mirrors:
        if os.path.exists(os.path.dirname(mir)):
            with open(mir, "w", encoding="utf-8") as f:
                f.write(html)
            print(f"Replicated to {mir}")

if __name__ == "__main__":
    run()
