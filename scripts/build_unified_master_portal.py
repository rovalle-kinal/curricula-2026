#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
build_unified_master_portal.py
Integra completamente la revisión de temarios de Revision_Temarios (20 cursos técnicos de especialidad ETS)
con el portal unificado del TSU (Técnico Superior Universitario 3er Año Kinal/UNIS).
Genera una sola landing page maestra completa, autocontenida y con la misma identidad gráfica.
Resguarda todas las páginas individuales no utilizadas en sus carpetas 'historico'.
"""

import os
import shutil
import re
import json

base_dir = "/Users/arqovalle/Library/CloudStorage/OneDrive-Personal/Software/Antigravity/Diseño Instruccional"
tsu_dir = os.path.join(base_dir, "TSU")
rev_dir = os.path.join(base_dir, "Revision_Temarios")
mybrain_base = "/Users/arqovalle/Library/CloudStorage/OneDrive-Personal/MyBrain/MyBrain/01 - My Brain/Kinal"
mybrain_tsu = os.path.join(mybrain_base, "TSU")
mybrain_rev = os.path.join(mybrain_base, "Revision_Temarios")

rev_historico = os.path.join(rev_dir, "historico")
os.makedirs(rev_historico, exist_ok=True)
os.makedirs(mybrain_rev, exist_ok=True)
os.makedirs(os.path.join(mybrain_rev, "historico"), exist_ok=True)

# -------------------------------------------------------------
# 1. PARSEAR LOS 20 CURSOS TÉCNICOS DE REVISION_TEMARIOS
# -------------------------------------------------------------

technical_courses_meta = [
    # Área 1: Construcción, Topografía y Modelado BIM
    {
        "file": "Fundamentos_de_la_Construccion_Propuesta.html",
        "id": "fundamentos_construccion",
        "area": 1,
        "area_name": "Construcción, Topografía y BIM",
        "name": "Fundamentos de la Construcción",
        "hours": 180,
        "modules": 5,
        "badge_color": "amber",
        "icon": "hard-hat",
        "short_desc": "Interpretación de planos, normas AGIES NSE-4, sistemas livianos (drywall), PPR termofusión e introducción a AutoCAD.",
        "ia_highlight": "IA: Visión artificial para EPP y fotogrametría móvil LiDAR."
    },
    {
        "file": "Administracion_de_Obras_Propuesta.html",
        "id": "administracion_obras",
        "area": 1,
        "area_name": "Construcción, Topografía y BIM",
        "name": "Administración de Obras",
        "hours": 180,
        "modules": 4,
        "badge_color": "blue",
        "icon": "clipboard-check",
        "short_desc": "Plan de SSO (Acuerdo Gub. 229-2014), introducción a Revit BIM, Carta Gantt, APU y leyes laborales de Guatemala.",
        "ia_highlight": "IA: Predicción de retrasos en ruta crítica y bitácoras automáticas."
    },
    {
        "file": "AutoCAD_Propuesta.html",
        "id": "autocad",
        "area": 1,
        "area_name": "Construcción, Topografía y BIM",
        "name": "AutoCAD 2D & 3D",
        "hours": 90,
        "modules": 4,
        "badge_color": "red",
        "icon": "compass",
        "short_desc": "Capas bajo norma AIA, layouts anotativos, interoperabilidad CAD-BIM, AutoCAD Web/Mobile y planos As-Built.",
        "ia_highlight": "IA: Autodesk AI Markup Assist y generación de AutoLISP."
    },
    {
        "file": "Revit_Architecture_Propuesta.html",
        "id": "revit_architecture",
        "area": 1,
        "area_name": "Construcción, Topografía y BIM",
        "name": "Autodesk Revit Architecture",
        "hours": 90,
        "modules": 5,
        "badge_color": "teal",
        "icon": "box",
        "short_desc": "Estándar BIM Forum GT, familias paramétricas, fases de demolición/nuevo y tablas dinámicas de cómputo métrico.",
        "ia_highlight": "IA: Renders instantáneos con Veras AI y Dynamo con LLMs."
    },
    {
        "file": "Revit_Structure_MEP_Propuesta.html",
        "id": "revit_structure_mep",
        "area": 1,
        "area_name": "Construcción, Topografía y BIM",
        "name": "Revit Structure & MEP",
        "hours": 90,
        "modules": 6,
        "badge_color": "orange",
        "icon": "layers",
        "short_desc": "Armado sísmico AGIES, despiece automático de varilla, ruteo hidrosanitario y Clash Detection con Navisworks.",
        "ia_highlight": "IA: Ruteo generativo de tuberías y matriz de colisiones."
    },
    {
        "file": "Civil_3D_Propuesta.html",
        "id": "civil_3d",
        "area": 1,
        "area_name": "Construcción, Topografía y BIM",
        "name": "Autodesk Civil 3D",
        "hours": 90,
        "modules": 4,
        "badge_color": "sky",
        "icon": "map",
        "short_desc": "Diseño vial según manual DGC Guatemala, peraltes, nubes de puntos LiDAR de drones y redes de drenaje.",
        "ia_highlight": "IA: Filtrado de terreno LiDAR y rasante de balance cero."
    },

    # Área 2: Electricidad Industrial, Electrónica y Automatización
    {
        "file": "Instalaciones_Electricas_Generales_Propuesta.html",
        "id": "instalaciones_electricas",
        "area": 2,
        "area_name": "Electricidad y Automatización",
        "name": "Instalaciones Eléctricas Generales",
        "hours": 180,
        "modules": 10,
        "badge_color": "yellow",
        "icon": "zap",
        "short_desc": "Normativa EEGSA/Energuate, malla de tierra con telurómetro, protecciones GFCI y sistemas solares On-Grid.",
        "ia_highlight": "IA: Termografía predictiva de tableros y balance inteligente."
    },
    {
        "file": "Controles_y_Maquinas_Electricas_Propuesta.html",
        "id": "controles_maquinas",
        "area": 2,
        "area_name": "Electricidad y Automatización",
        "name": "Controles y Máquinas Eléctricas",
        "hours": 180,
        "modules": 10,
        "badge_color": "yellow",
        "icon": "cpu",
        "short_desc": "Variadores de frecuencia (VFD), arrancadores suaves, corrección de factor de potencia y megado de motores.",
        "ia_highlight": "IA: Análisis de firma de corriente (MCSA) para fallas de rotor."
    },
    {
        "file": "Electronica_Analogica_Propuesta.html",
        "id": "electronica_analogica",
        "area": 2,
        "area_name": "Electricidad y Automatización",
        "name": "Electrónica Analógica",
        "hours": 180,
        "modules": 10,
        "badge_color": "cyan",
        "icon": "activity",
        "short_desc": "Fuentes conmutadas (SMPS), amplificadores operacionales 4-20mA, reparación de tarjetas y optoacopladores.",
        "ia_highlight": "IA: Detección visual de componentes SMD quemados en PCB."
    },
    {
        "file": "Control_Industrial_Sistemas_Programables_Propuesta.html",
        "id": "control_programables",
        "area": 2,
        "area_name": "Electricidad y Automatización",
        "name": "Control Industrial con Sistemas Programables",
        "hours": 180,
        "modules": 3,
        "badge_color": "emerald",
        "icon": "terminal",
        "short_desc": "PLC Siemens S7-1200 en TIA Portal, pantallas táctiles HMI, electroneumática y redes Modbus TCP.",
        "ia_highlight": "IA: Generación de código Structured Text (ST) con LLMs."
    },
    {
        "file": "Automatizacion_Industrial_Propuesta.html",
        "id": "automatizacion_industrial",
        "area": 2,
        "area_name": "Electricidad y Automatización",
        "name": "Automatización Industrial",
        "hours": 180,
        "modules": 6,
        "badge_color": "indigo",
        "icon": "sliders",
        "short_desc": "Lazos PID de control continuo, transmisores HART (4-20mA), SCADA (Ignition / Node-RED) y redes Profinet.",
        "ia_highlight": "IA: Visión industrial para control de calidad y PID autónomo."
    },

    # Área 3: Mecánica Industrial, Soldadura y Calderas de Vapor
    {
        "file": "Mantenimiento_Mecanico_Industrial_Propuesta.html",
        "id": "mantenimiento_mecanico",
        "area": 3,
        "area_name": "Mecánica Industrial y Calderas",
        "name": "Mantenimiento Mecánico Industrial",
        "hours": 180,
        "modules": 10,
        "badge_color": "slate",
        "icon": "tool",
        "short_desc": "Alineación láser de ejes, calentadores de inducción para rodamientos, tribología y detección de fugas por ultrasonido.",
        "ia_highlight": "IA: Análisis de vibraciones mecánicas IoT prescriptivo."
    },
    {
        "file": "Soldadura_Industrial_Propuesta.html",
        "id": "soldadura_industrial",
        "area": 3,
        "area_name": "Mecánica Industrial y Calderas",
        "name": "Soldadura Industrial",
        "hours": 180,
        "modules": 10,
        "badge_color": "red",
        "icon": "flame",
        "short_desc": "Calificación según AWS D1.1 y ASME IX, procesos GMAW/FCAW pesados, TIG sanitario en acero inoxidable y líquidos penetrantes.",
        "ia_highlight": "IA: Inspección de cordones por visión artificial y simuladores VR."
    },
    {
        "file": "Calderas_de_Vapor_Propuesta.html",
        "id": "calderas_vapor",
        "area": 3,
        "area_name": "Mecánica Industrial y Calderas",
        "name": "Calderas de Vapor",
        "hours": 180,
        "modules": 5,
        "badge_color": "amber",
        "icon": "gauge",
        "short_desc": "Tratamiento químico de agua, quemadores modulantes, retorno de condensados y cumplimiento del Reglamento de Calderas MinTrab.",
        "ia_highlight": "IA: Optimización de combustión y monitoreo de trampas de vapor."
    },

    # Área 4: Tecnología Automotriz y Motocicletas
    {
        "file": "Mecanica_Motores_Gasolina_Propuesta.html",
        "id": "motores_gasolina",
        "area": 4,
        "area_name": "Tecnología Automotriz y Motos",
        "name": "Mecánica de Motores Gasolina",
        "hours": 180,
        "modules": 10,
        "badge_color": "red",
        "icon": "disc",
        "short_desc": "Distribución variable (VVT), probador de fugas de cilindro con manómetro, inyección directa GDI y motores ciclo Atkinson.",
        "ia_highlight": "IA: Diagnóstico acústico de golpeteo de biela y boroscopio IA."
    },
    {
        "file": "Mecanismos_del_Automovil_Propuesta.html",
        "id": "mecanismos_automovil",
        "area": 4,
        "area_name": "Tecnología Automotriz y Motos",
        "name": "Mecanismos del Automóvil",
        "hours": 180,
        "modules": 10,
        "badge_color": "emerald",
        "icon": "settings",
        "short_desc": "Frenos ABS/ESP con ciclado electrónico, dirección eléctrica EPS, cajas automáticas/CVT y alineación 3D láser.",
        "ia_highlight": "IA: Reconocimiento visual de desgaste de neumáticos y calibración SAS."
    },
    {
        "file": "Electromecanica_Automotriz_Propuesta.html",
        "id": "electromecanica_automotriz",
        "area": 4,
        "area_name": "Tecnología Automotriz y Motos",
        "name": "Electromecánica Automotriz",
        "hours": 180,
        "modules": 10,
        "badge_color": "blue",
        "icon": "zap",
        "short_desc": "Redes multiplexadas CAN-Bus/LIN, alternadores pilotados, baterías AGM y protocolos de seguridad en alta tensión para híbridos.",
        "ia_highlight": "IA: Decodificación asistida de tramas CAN y diagramas dinámicos."
    },
    {
        "file": "Inyeccion_Electronica_Automotriz_Propuesta.html",
        "id": "inyeccion_electronica",
        "area": 4,
        "area_name": "Tecnología Automotriz y Motos",
        "name": "Inyección Electrónica Automotriz",
        "hours": 180,
        "modules": 10,
        "badge_color": "purple",
        "icon": "radio",
        "short_desc": "Osciloscopio automotriz de 4 canales, sensores A/F de banda ancha, análisis de Fuel Trims y diésel Common Rail ligero.",
        "ia_highlight": "IA: Comparación automática de señales de osciloscopio y DTCs."
    },
    {
        "file": "Aire_Acondicionado_Automotriz_Propuesta.html",
        "id": "aire_acondicionado",
        "area": 4,
        "area_name": "Tecnología Automotriz y Motos",
        "name": "Aire Acondicionado Automotriz",
        "hours": 180,
        "modules": 2,
        "badge_color": "cyan",
        "icon": "wind",
        "short_desc": "Transición a gas R-1234yf, detección de fugas con Nitrógeno UV, compresores de cilindrada variable PWM y HVAC híbrido.",
        "ia_highlight": "IA: Termografía asistida de condensadores y dosificación por VIN."
    },
    {
        "file": "Mecanica_de_Motocicletas_Propuesta.html",
        "id": "mecanica_motocicletas",
        "area": 4,
        "area_name": "Tecnología Automotriz y Motos",
        "name": "Mecánica de Motocicletas",
        "hours": 180,
        "modules": 6,
        "badge_color": "orange",
        "icon": "navigation",
        "short_desc": "Sistemas de inyección electrónica en motos (FI), frenos ABS de rueda, escáner multimarca para 2 ruedas y CVT de scooters.",
        "ia_highlight": "IA: Diagnóstico por sonido de punterías y cruce de repuestos."
    }
]

print(f"Procesando {len(technical_courses_meta)} cursos técnicos de Revision_Temarios...")

technical_courses_html_dict = {}

for meta in technical_courses_meta:
    fpath = os.path.join(rev_dir, meta["file"])
    if not os.path.exists(fpath):
        # Look in historico if already moved
        fpath = os.path.join(rev_historico, meta["file"])
    
    with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    # Extract main
    main_match = re.search(r'<main[^>]*>(.*?)</main>', content, re.DOTALL)
    if not main_match:
        print(f"ADVERTENCIA: No se encontró <main> en {meta['file']}")
        continue
    
    main_body = main_match.group(1)
    
    # Sanitize IDs that might collide (e.g. id="propuesta" -> id="propuesta_{meta['id']}")
    main_body = re.sub(r'id=[\"\']propuesta[\"\']', f'id="propuesta_{meta["id"]}"', main_body)
    main_body = re.sub(r'id=[\"\']btn-all[\"\']', f'id="btn-all-{meta["id"]}"', main_body)
    main_body = re.sub(r'id=[\"\']btn-delete[\"\']', f'id="btn-delete-{meta["id"]}"', main_body)
    main_body = re.sub(r'id=[\"\']btn-update[\"\']', f'id="btn-update-{meta["id"]}"', main_body)
    main_body = re.sub(r'id=[\"\']btn-new[\"\']', f'id="btn-new-{meta["id"]}"', main_body)
    main_body = re.sub(r'id=[\"\']btn-keep[\"\']', f'id="btn-keep-{meta["id"]}"', main_body)
    
    # Adapt onclick calls to pass course id: filterItems('status') -> filterEtsItems('status', '{meta["id"]}')
    main_body = re.sub(r'onclick=[\"\']filterItems\(([\'\"].*?[\'\"])\)[\"\']', f"onclick=\"filterEtsItems(\\1, '{meta['id']}')\"", main_body)
    
    technical_courses_html_dict[meta["id"]] = main_body

print(f"Extraídos con éxito {len(technical_courses_html_dict)} cursos técnicos.")

# Generar lista de opciones para el selector rápido de cursos técnicos
ets_options_html = ""
for meta in technical_courses_meta:
    ets_options_html += f'<option value="{meta["id"]}">Área {meta["area"]}: {meta["name"]} ({meta["hours"]}h)</option>\n'

# Generar tarjetas de selección de curso por área
def build_area_cards(area_num):
    cards_html = ""
    for meta in technical_courses_meta:
        if meta["area"] == area_num:
            cards_html += f"""
            <div class="ets-card group bg-white p-5 rounded-2xl border border-slate-200 hover:border-blue-600 hover:shadow-lg transition cursor-pointer flex flex-col justify-between"
                 onclick="openEtsCourse('{meta["id"]}')" data-course-id="{meta["id"]}">
                <div class="space-y-3">
                    <div class="flex justify-between items-start">
                        <span class="px-2.5 py-1 rounded-full bg-slate-100 text-slate-700 font-bold text-[11px] uppercase tracking-wider">
                            {meta["hours"]} Horas • {meta["modules"]} Módulos
                        </span>
                        <div class="w-8 h-8 rounded-lg bg-blue-50 text-blue-700 flex items-center justify-center group-hover:bg-blue-600 group-hover:text-white transition">
                            <i data-lucide="{meta["icon"]}" class="w-4 h-4"></i>
                        </div>
                    </div>
                    <div>
                        <h4 class="text-base font-bold text-slate-900 group-hover:text-blue-700 transition">
                            {meta["name"]}
                        </h4>
                        <p class="text-xs text-slate-600 mt-1.5 leading-relaxed line-clamp-3">
                            {meta["short_desc"]}
                        </p>
                    </div>
                </div>
                <div class="pt-3 mt-4 border-t border-slate-100 flex items-center justify-between text-xs">
                    <span class="text-purple-700 font-medium flex items-center gap-1">
                        <i data-lucide="bot" class="w-3.5 h-3.5"></i> IA Aplicada
                    </span>
                    <span class="text-blue-600 font-bold group-hover:translate-x-0.5 transition flex items-center gap-0.5">
                        Ver Auditoría <i data-lucide="chevron-right" class="w-3.5 h-3.5"></i>
                    </span>
                </div>
            </div>
            """
    return cards_html

area1_cards = build_area_cards(1)
area2_cards = build_area_cards(2)
area3_cards = build_area_cards(3)
area4_cards = build_area_cards(4)

# Generar contenedores de detalle para cada uno de los 20 cursos
ets_detail_containers_html = ""
for idx, meta in enumerate(technical_courses_meta):
    cid = meta["id"]
    body = technical_courses_html_dict.get(cid, "<p>Contenido no disponible</p>")
    is_active = (idx == 0)
    display_style = "block" if is_active else "none"
    
    ets_detail_containers_html += f"""
    <div id="ets-detail-{cid}" class="ets-course-detail-pane" style="display: {display_style};">
        <!-- Barra de navegación interna del curso -->
        <div class="bg-slate-900 text-white p-4 rounded-t-2xl flex flex-wrap justify-between items-center gap-4">
            <div class="flex items-center gap-3">
                <span class="px-2.5 py-1 rounded bg-blue-600 text-white text-xs font-bold uppercase">Área {meta["area"]}</span>
                <span class="text-slate-400">|</span>
                <span class="text-slate-200 font-bold text-sm sm:text-base flex items-center gap-2">
                    <i data-lucide="{meta["icon"]}" class="w-4 h-4 text-blue-400"></i>
                    {meta["name"]} ({meta["hours"]} Horas)
                </span>
            </div>
            <div class="flex items-center gap-2">
                <button onclick="scrollToEtsSelector()" class="text-xs bg-slate-800 hover:bg-slate-700 text-slate-300 px-3 py-1.5 rounded-lg border border-slate-700 transition flex items-center gap-1.5">
                    <i data-lucide="layout-grid" class="w-3.5 h-3.5"></i> Cambiar Curso
                </button>
            </div>
        </div>
        
        <!-- Cuerpo del informe de auditoría -->
        <div class="bg-white border-x border-b border-slate-200 rounded-b-2xl p-6 sm:p-8 space-y-8">
            {body}
        </div>
    </div>
    """

print("Bloques HTML de ETS construidos con éxito.")

# -------------------------------------------------------------
# 2. DEFINIR LA SECCIÓN DE REVISIÓN DE TEMARIOS (ETS)
# -------------------------------------------------------------

# Obtenemos los componentes ya afinados del TSU:
# - Header y nav
# - Sección 1: Resumen y especialidades
# - Sección 2: Mapa Curricular & Red SVG
# - Sección 3: Temarios por línea
# - Sección 4: Auditoría y dictamen TSU
# - Sección 5: Bimestres

# Construimos la SECCIÓN DE ETS COMPLETA:
seccion_ets_completa = f"""
<!-- ======================================================== -->
<!-- SECCIÓN: AUDITORÍA CURRICULAR DE ESPECIALIDADES TÉCNICAS (ETS 2026) -->
<!-- ======================================================== -->
<section id="seccion-ets-auditoria" class="space-y-8 pt-8 border-t border-slate-200">
    <div class="text-center space-y-3 max-w-4xl mx-auto">
        <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-50 border border-blue-200 text-blue-800 text-xs font-semibold">
            <i data-lucide="sparkles" class="w-3.5 h-3.5 text-blue-600"></i> Escuela Técnica Superior (ETS) • Ciclo Académico 2026
        </div>
        <h2 class="text-3xl sm:text-4xl font-black text-slate-900 tracking-tight">
            Auditoría Curricular de Especialidades Técnicas & Ecosistema IA
        </h2>
        <p class="text-slate-600 text-sm sm:text-base leading-relaxed">
            Modernización profunda de los <strong>20 programas técnicos de especialidad</strong> frente a las exigencias industriales reales de Guatemala 
            (CGC, AGIES, CNEE, MinTrab 229-2014, AWS, ASME y sector automotriz), complementado con <strong>módulos aplicados de Inteligencia Artificial</strong> en cada especialidad técnica.
        </p>
    </div>

    <!-- Global Stats Cards -->
    <div class="grid grid-cols-2 md:grid-cols-4 gap-4">
        <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-1">
            <div class="text-xs uppercase font-bold text-slate-500">Programas Técnicos</div>
            <div class="text-3xl font-black text-slate-900">20 Cursos</div>
            <div class="text-xs text-blue-600 font-medium">4 Áreas • 3,240 Horas de Taller</div>
        </div>
        <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-1">
            <div class="text-xs uppercase font-bold text-slate-500">Módulos con IA</div>
            <div class="text-3xl font-black text-purple-700">20 Módulos</div>
            <div class="text-xs text-purple-600 font-medium">60 Casos Prácticos de IA</div>
        </div>
        <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-1">
            <div class="text-xs uppercase font-bold text-slate-500">Temas Auditados</div>
            <div class="text-3xl font-black text-amber-600">1,276 Temas</div>
            <div class="text-xs text-slate-500 font-medium">50 Del • 271 Upd • 81 New • 874 Keep</div>
        </div>
        <div class="bg-white p-5 rounded-2xl border border-slate-200 shadow-sm space-y-1">
            <div class="text-xs uppercase font-bold text-slate-500">Alineación Normativa</div>
            <div class="text-3xl font-black text-emerald-600">100% Legal</div>
            <div class="text-xs text-emerald-700 font-medium">AGIES, MinTrab 229, CNEE, AWS</div>
        </div>
    </div>

    <!-- Metodología de Código de Color -->
    <div class="p-6 rounded-2xl bg-white border border-slate-200 shadow-sm space-y-3">
        <h3 class="text-sm font-bold text-slate-800 uppercase tracking-wider flex items-center gap-2">
            <i data-lucide="info" class="w-4 h-4 text-blue-600"></i> Metodología y Código de Color de Auditoría
        </h3>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3 text-xs">
            <div class="p-3 rounded-xl bg-red-50 border border-red-200 text-red-900">
                <strong class="text-red-700 block mb-1">🔴 ROJO (Eliminar)</strong>
                Contenidos obsoletos en el mercado actual (ej. rotulado manual a lápiz, render 3D primitivo por CPU, temas teóricos sin aplicación en taller).
            </div>
            <div class="p-3 rounded-xl bg-amber-50 border border-amber-200 text-amber-900">
                <strong class="text-amber-700 block mb-1">🟡 AMARILLO (Actualizar)</strong>
                Temas existentes que requieren modernización técnica (normas AGIES sísmicas, PPR termofusión, capas AIA, variación de frecuencia).
            </div>
            <div class="p-3 rounded-xl bg-blue-50 border border-blue-200 text-blue-900">
                <strong class="text-blue-700 block mb-1">🔵 AZUL (Propuesta Nueva)</strong>
                Competencias prioritarias demandadas en Guatemala (Plan de SSO 229-2014, energía solar fotovoltaica, drywall, Navisworks, As-Built).
            </div>
            <div class="p-3 rounded-xl bg-purple-50 border border-purple-200 text-purple-900">
                <strong class="text-purple-700 block mb-1">🟣 PÚRPURA (Innovación IA)</strong>
                Apartado adicional de herramientas de Inteligencia Artificial generativa, predictiva y de visión computacional aplicadas a cada oficio.
            </div>
        </div>
    </div>

    <!-- Controles de Exploración: Selector de Área y Buscador -->
    <div id="ets-selector-anchor" class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm space-y-6">
        <div class="flex flex-wrap justify-between items-center gap-4">
            <div>
                <h3 class="text-lg font-bold text-slate-900 flex items-center gap-2">
                    <i data-lucide="layers" class="w-5 h-5 text-blue-600"></i>
                    Explorador de Programas Técnicos por Área Industrial
                </h3>
                <p class="text-xs text-slate-500 mt-0.5">
                    Selecciona un área técnica para ver sus cursos o utiliza el buscador para saltar directamente a cualquier especialidad.
                </p>
            </div>
            <!-- Buscador Rápido -->
            <div class="relative w-full sm:w-80">
                <i data-lucide="search" class="w-4 h-4 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2"></i>
                <input type="text" id="ets-search-input" onkeyup="filterEtsCards()" placeholder="Buscar curso técnico (ej. Revit, Soldadura, PLC...)" 
                       class="w-full pl-9 pr-4 py-2 rounded-xl bg-slate-50 border border-slate-300 text-xs text-slate-800 placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-600">
            </div>
        </div>

        <!-- Botones de Pestañas de Área -->
        <div class="flex flex-wrap gap-2 pt-2 border-t border-slate-100">
            <button onclick="switchEtsArea(1)" id="btn-ets-area-1" class="ets-area-tab px-4 py-2.5 rounded-xl font-bold text-xs flex items-center gap-2 bg-blue-900 text-white shadow-sm transition">
                <i data-lucide="hard-hat" class="w-4 h-4"></i> 1. Construcción & BIM (6 Cursos)
            </button>
            <button onclick="switchEtsArea(2)" id="btn-ets-area-2" class="ets-area-tab px-4 py-2.5 rounded-xl font-bold text-xs flex items-center gap-2 bg-slate-100 text-slate-700 hover:bg-slate-200 transition">
                <i data-lucide="zap" class="w-4 h-4"></i> 2. Electricidad & Automatización (5 Cursos)
            </button>
            <button onclick="switchEtsArea(3)" id="btn-ets-area-3" class="ets-area-tab px-4 py-2.5 rounded-xl font-bold text-xs flex items-center gap-2 bg-slate-100 text-slate-700 hover:bg-slate-200 transition">
                <i data-lucide="wrench" class="w-4 h-4"></i> 3. Mecánica & Soldadura (3 Cursos)
            </button>
            <button onclick="switchEtsArea(4)" id="btn-ets-area-4" class="ets-area-tab px-4 py-2.5 rounded-xl font-bold text-xs flex items-center gap-2 bg-slate-100 text-slate-700 hover:bg-slate-200 transition">
                <i data-lucide="car" class="w-4 h-4"></i> 4. Automotriz & Motos (6 Cursos)
            </button>
        </div>

        <!-- Grids de Cursos por Área -->
        <div id="ets-area-panel-1" class="ets-area-panel grid md:grid-cols-2 lg:grid-cols-3 gap-4">
            {area1_cards}
        </div>
        <div id="ets-area-panel-2" class="ets-area-panel grid md:grid-cols-2 lg:grid-cols-3 gap-4" style="display: none;">
            {area2_cards}
        </div>
        <div id="ets-area-panel-3" class="ets-area-panel grid md:grid-cols-2 lg:grid-cols-3 gap-4" style="display: none;">
            {area3_cards}
        </div>
        <div id="ets-area-panel-4" class="ets-area-panel grid md:grid-cols-2 lg:grid-cols-3 gap-4" style="display: none;">
            {area4_cards}
        </div>
    </div>

    <!-- Visor Detallado del Curso Activo -->
    <div id="ets-detail-viewer-wrapper" class="space-y-4">
        <div class="flex flex-wrap justify-between items-center gap-3">
            <div class="text-xs uppercase font-extrabold tracking-wider text-slate-500 flex items-center gap-1.5">
                <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse"></span>
                Informe de Auditoría Completa del Curso Seleccionado
            </div>
            <div class="flex items-center gap-2 text-xs">
                <label for="ets-quick-select" class="text-slate-600 font-semibold">Selector Rápido:</label>
                <select id="ets-quick-select" onchange="openEtsCourse(this.value)" class="bg-white border border-slate-300 rounded-lg px-3 py-1.5 text-xs text-slate-800 font-medium focus:ring-2 focus:ring-blue-600">
                    {ets_options_html}
                </select>
            </div>
        </div>

        <!-- Render de los 20 Contenedores de Curso -->
        {ets_detail_containers_html}
    </div>
</section>
"""

# -------------------------------------------------------------
# 3. ENSAMBLAR LA LANDING PAGE MAESTRA COMPLETA
# -------------------------------------------------------------

# Leemos la landing page base de TSU
tsu_index_path = os.path.join(tsu_dir, "index.html")
with open(tsu_index_path, "r", encoding="utf-8") as f:
    full_html = f.read()

# Actualizar el header de navegación para incluir el botón de ETS
nav_original = '<a href="#seccion-auditoria" class="nav-item">Dictamen</a>'
nav_nuevo = """<a href="#seccion-auditoria" class="nav-item">Auditoría TSU</a>
               <a href="#seccion-ets-auditoria" class="nav-item" style="color: #d97706; font-weight: 700;">ETS: 20 Cursos Técnicos</a>"""

full_html = full_html.replace(nav_original, nav_nuevo)

# Insertar la sección de ETS justo antes de la sección de bimestres
pos_bimestres = full_html.find('<!-- SECCIÓN 5: DOSIFICACIÓN Y OPERACIÓN BIMESTRAL -->')
if pos_bimestres != -1:
    full_html = full_html[:pos_bimestres] + seccion_ets_completa + "\n\n" + full_html[pos_bimestres:]
else:
    # Si no se encuentra exactamente, insertamos antes de </main>
    full_html = full_html.replace('</main>', seccion_ets_completa + '\n</main>')

# Agregar los scripts de ETS al bloque <script>
ets_scripts_js = """
// -------------------------------------------------------------
// FUNCIONES DE CONTROL INTERACTIVO DE ETS (REVISIÓN DE TEMARIOS)
// -------------------------------------------------------------

function switchEtsArea(areaNum) {
    // Actualizar botones de área
    for (let i = 1; i <= 4; i++) {
        const btn = document.getElementById(`btn-ets-area-${i}`);
        const panel = document.getElementById(`ets-area-panel-${i}`);
        if (btn && panel) {
            if (i === areaNum) {
                btn.className = 'ets-area-tab px-4 py-2.5 rounded-xl font-bold text-xs flex items-center gap-2 bg-blue-900 text-white shadow-sm transition';
                panel.style.display = 'grid';
            } else {
                btn.className = 'ets-area-tab px-4 py-2.5 rounded-xl font-bold text-xs flex items-center gap-2 bg-slate-100 text-slate-700 hover:bg-slate-200 transition';
                panel.style.display = 'none';
            }
        }
    }
}

function openEtsCourse(courseId) {
    // Ocultar todos los paneles de detalle
    document.querySelectorAll('.ets-course-detail-pane').forEach(el => {
        el.style.display = 'none';
    });
    
    // Mostrar el curso solicitado
    const target = document.getElementById(`ets-detail-${courseId}`);
    if (target) {
        target.style.display = 'block';
    }
    
    // Actualizar selector rápido
    const sel = document.getElementById('ets-quick-select');
    if (sel) {
        sel.value = courseId;
    }
    
    // Smooth scroll hacia el visor de detalle
    const viewer = document.getElementById('ets-detail-viewer-wrapper');
    if (viewer) {
        viewer.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
    
    // Refrescar iconos Lucide
    if (window.lucide) {
        lucide.createIcons();
    }
}

function scrollToEtsSelector() {
    const el = document.getElementById('ets-selector-anchor');
    if (el) {
        el.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
}

function filterEtsCards() {
    const q = document.getElementById('ets-search-input').value.toLowerCase().trim();
    const cards = document.querySelectorAll('.ets-card');
    
    // Si hay búsqueda, mostramos todos los paneles para que no queden ocultos por pestaña
    for (let i = 1; i <= 4; i++) {
        const panel = document.getElementById(`ets-area-panel-${i}`);
        if (panel) {
            if (q.length > 0) {
                panel.style.display = 'grid';
            } else {
                // Volver a la pestaña activa
                const btn1 = document.getElementById('btn-ets-area-1');
                const isBtn1Active = btn1 && btn1.classList.contains('bg-blue-900');
                if (i === 1 && isBtn1Active) panel.style.display = 'grid';
                else if (i !== 1 && isBtn1Active) panel.style.display = 'none';
            }
        }
    }
    
    cards.forEach(card => {
        const text = card.textContent.toLowerCase();
        if (text.includes(q)) {
            card.style.display = 'flex';
        } else {
            card.style.display = 'none';
        }
    });
}

function filterEtsItems(status, courseId) {
    const pane = document.getElementById(`ets-detail-${courseId}`);
    if (!pane) return;
    
    const items = pane.querySelectorAll('.content-item');
    items.forEach(item => {
        if (status === 'all') {
            item.style.display = 'block';
        } else {
            if (item.getAttribute('data-status') === status) {
                item.style.display = 'block';
            } else {
                item.style.display = 'none';
            }
        }
    });
    
    // Actualizar estilos de los botones de filtro dentro de este curso
    const buttons = {
        'all': document.getElementById(`btn-all-${courseId}`),
        'delete': document.getElementById(`btn-delete-${courseId}`),
        'update': document.getElementById(`btn-update-${courseId}`),
        'new': document.getElementById(`btn-new-${courseId}`),
        'keep': document.getElementById(`btn-keep-${courseId}`)
    };
    
    Object.values(buttons).forEach(btn => {
        if (btn) btn.classList.remove('ring-2', 'ring-offset-2', 'ring-slate-900', 'font-black');
    });
    
    if (buttons[status]) {
        buttons[status].classList.add('ring-2', 'ring-offset-2', 'ring-slate-900', 'font-black');
    }
}
"""

full_html = full_html.replace('lucide.createIcons();', f'lucide.createIcons();\n{ets_scripts_js}')

# -------------------------------------------------------------
# 4. GUARDAR ARCHIVOS UNIFICADOS Y MOVER HISTÓRICOS
# -------------------------------------------------------------

# Guardar en TSU/index.html
tsu_index = os.path.join(tsu_dir, "index.html")
with open(tsu_index, "w", encoding="utf-8") as f:
    f.write(full_html)
print(f"Landing page unificada escrita en: {tsu_index} ({len(full_html)/1024:.1f} KB)")

# Guardar en raíz index.html
root_index = os.path.join(base_dir, "index.html")
with open(root_index, "w", encoding="utf-8") as f:
    f.write(full_html)
print(f"Landing page unificada escrita en: {root_index}")

# Guardar en Revision_Temarios/index.html
rev_index = os.path.join(rev_dir, "index.html")
# Resguardar el index anterior de Revision_Temarios en historico
rev_ant_hist = os.path.join(rev_historico, "index_anterior.html")
if os.path.exists(rev_index) and not os.path.exists(rev_ant_hist):
    shutil.copy2(rev_index, rev_ant_hist)
    print(f"Index anterior de Revision_Temarios resguardado en: {rev_ant_hist}")

with open(rev_index, "w", encoding="utf-8") as f:
    f.write(full_html)
print(f"Landing page unificada escrita en: {rev_index}")

# Mover las 20 páginas individuales *_Propuesta.html a Revision_Temarios/historico/
for meta in technical_courses_meta:
    src = os.path.join(rev_dir, meta["file"])
    dst = os.path.join(rev_historico, meta["file"])
    if os.path.exists(src):
        shutil.move(src, dst)
print(f"Las 20 páginas de propuesta técnica fueron movidas a: {rev_historico}")

# -------------------------------------------------------------
# 5. SINCRONIZAR A MYBRAIN
# -------------------------------------------------------------
print("Sincronizando con MyBrain...")
mybrain_tsu_index = os.path.join(mybrain_tsu, "index.html")
shutil.copy2(tsu_index, mybrain_tsu_index)

mybrain_rev_index = os.path.join(mybrain_rev, "index.html")
shutil.copy2(rev_index, mybrain_rev_index)

# Sincronizar historicos de Revision_Temarios
for f in os.listdir(rev_historico):
    src_f = os.path.join(rev_historico, f)
    dst_f = os.path.join(mybrain_rev, "historico", f)
    if os.path.isfile(src_f):
        shutil.copy2(src_f, dst_f)

print("Sincronización completada con éxito en MyBrain.")
