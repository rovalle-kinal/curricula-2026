#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
generate_portal_ecosystem.py
Reorganiza el ecosistema curricular de Kinal en:
1. Página Principal Raíz (index.html): Portal Maestro para elegir entre TSU o Áreas Técnicas.
2. TSU (TSU/index.html): Página dedicada al año académico del TSU con mapa, red SVG, temarios, auditoría y bimestres.
3. Áreas Técnicas (Revision_Temarios/):
   - Revision_Temarios/index.html (Hub de Especialidades ETS)
   - Revision_Temarios/construccion.html (Área 1: 6 cursos)
   - Revision_Temarios/electricidad.html (Área 2: 5 cursos)
   - Revision_Temarios/mecanica.html (Área 3: 3 cursos)
   - Revision_Temarios/automotriz.html (Área 4: 6 cursos)
4. Sincronización en MyBrain.
"""

import os
import shutil
import re
import json

base_dir = "/Users/arqovalle/Library/CloudStorage/OneDrive-Personal/Software/Antigravity/Diseño Instruccional"
tsu_dir = os.path.join(base_dir, "TSU")
rev_dir = os.path.join(base_dir, "Revision_Temarios")
rev_hist_dir = os.path.join(rev_dir, "historico")

mybrain_base = "/Users/arqovalle/Library/CloudStorage/OneDrive-Personal/MyBrain/MyBrain/01 - My Brain/Kinal"
mybrain_tsu = os.path.join(mybrain_base, "TSU")
mybrain_rev = os.path.join(mybrain_base, "Revision_Temarios")

os.makedirs(tsu_dir, exist_ok=True)
os.makedirs(rev_dir, exist_ok=True)
os.makedirs(rev_hist_dir, exist_ok=True)
os.makedirs(mybrain_tsu, exist_ok=True)
os.makedirs(mybrain_rev, exist_ok=True)

# -------------------------------------------------------------
# METADATA DE LOS 20 CURSOS TÉCNICOS POR ÁREA
# -------------------------------------------------------------

areas_data = [
    {
        "id": "construccion",
        "num": 1,
        "filename": "construccion.html",
        "name": "Área de Construcción, Topografía y Modelado BIM",
        "short_name": "Construcción & BIM",
        "icon": "hard-hat",
        "color": "amber",
        "total_hours": 720,
        "courses_count": 6,
        "desc": "Modernización curricular orientada a la ingeniería estructural sísmica (AGIES NSE-4), administración y supervisión de obras (Plan SSO 229-2014, Carta Gantt, APU), adopción del estándar BIM Forum Guatemala, interoperabilidad CAD-BIM, Navisworks clash detection y diseño vial con Autodesk Civil 3D y fotogrametría LiDAR de drones.",
        "normas": "AGIES NSE-4, Acuerdo Gubernativo 229-2014, BIM Forum GT, DGC Guatemala",
        "courses": [
            {
                "file": "Fundamentos_de_la_Construccion_Propuesta.html",
                "id": "fundamentos_construccion",
                "name": "Fundamentos de la Construcción",
                "hours": 180,
                "modules": 5,
                "badge": "180 Horas • 5 Módulos",
                "icon": "hard-hat",
                "desc": "Interpretación de planos, normas AGIES NSE-4, sistemas livianos (drywall), PPR termofusión e introducción a AutoCAD.",
                "ia_highlight": "IA: Visión artificial para EPP y fotogrametría móvil LiDAR."
            },
            {
                "file": "Administracion_de_Obras_Propuesta.html",
                "id": "administracion_obras",
                "name": "Administración de Obras",
                "hours": 180,
                "modules": 4,
                "badge": "180 Horas • 4 Módulos",
                "icon": "clipboard-check",
                "desc": "Plan de SSO (Acuerdo Gub. 229-2014), introducción a Revit BIM, Carta Gantt, APU y leyes laborales de Guatemala.",
                "ia_highlight": "IA: Predicción de retrasos en ruta crítica y bitácoras automáticas."
            },
            {
                "file": "AutoCAD_Propuesta.html",
                "id": "autocad",
                "name": "AutoCAD 2D & 3D",
                "hours": 90,
                "modules": 4,
                "badge": "90 Horas • 4 Módulos",
                "icon": "compass",
                "desc": "Capas bajo norma AIA, layouts/viewports anotativos, interoperabilidad CAD-BIM, AutoCAD Web/Mobile y planos As-Built.",
                "ia_highlight": "IA: Autodesk AI Markup Assist y generación de AutoLISP."
            },
            {
                "file": "Revit_Architecture_Propuesta.html",
                "id": "revit_architecture",
                "name": "Autodesk Revit Architecture",
                "hours": 90,
                "modules": 5,
                "badge": "90 Horas • 5 Módulos",
                "icon": "box",
                "desc": "Estándar BIM Forum GT, familias paramétricas, fases de demolición/nuevo y tablas dinámicas de cómputo métrico.",
                "ia_highlight": "IA: Renders instantáneos con Veras AI y Dynamo asistido por LLMs."
            },
            {
                "file": "Revit_Structure_MEP_Propuesta.html",
                "id": "revit_structure_mep",
                "name": "Revit Structure & MEP",
                "hours": 90,
                "modules": 6,
                "badge": "90 Horas • 6 Módulos",
                "icon": "layers",
                "desc": "Armado sísmico AGIES, despiece automático de varilla, ruteo hidrosanitario y Clash Detection con Navisworks.",
                "ia_highlight": "IA: Ruteo generativo de tuberías y matriz de colisiones."
            },
            {
                "file": "Civil_3D_Propuesta.html",
                "id": "civil_3d",
                "name": "Autodesk Civil 3D",
                "hours": 90,
                "modules": 4,
                "badge": "90 Horas • 4 Módulos",
                "icon": "map",
                "desc": "Diseño vial según manual de la DGC Guatemala, peraltes, nubes de puntos LiDAR de drones y redes de drenaje.",
                "ia_highlight": "IA: Filtrado de terreno LiDAR y rasante generativa de balance cero."
            }
        ]
    },
    {
        "id": "electricidad",
        "num": 2,
        "filename": "electricidad.html",
        "name": "Área de Electricidad Industrial, Electrónica y Automatización",
        "short_name": "Electricidad & Automatización",
        "icon": "zap",
        "color": "yellow",
        "total_hours": 900,
        "courses_count": 5,
        "desc": "Formación técnica avanzada alineada a los pliegos tarifarios y normas de distribución de EEGSA y Energuate, medición de resistividad con telurómetro, generación solar fotovoltaica On-Grid (CNEE-186-2008), control de motores con VFD y arrancadores suaves, reparación de fuentes conmutadas SMPS, control de procesos con PLC Siemens S7-1200 en TIA Portal, lazos PID continuos y supervisión SCADA con redes industriales Profinet y Modbus TCP.",
        "normas": "Normas de Distribución EEGSA/Energuate, CNEE-186-2008, NFPA 70E, Siemens TIA Portal",
        "courses": [
            {
                "file": "Instalaciones_Electricas_Generales_Propuesta.html",
                "id": "instalaciones_electricas",
                "name": "Instalaciones Eléctricas Generales",
                "hours": 180,
                "modules": 10,
                "badge": "180 Horas • 10 Módulos",
                "icon": "zap",
                "desc": "Normativa EEGSA/Energuate, malla de tierra con telurómetro, protecciones GFCI y sistemas solares On-Grid.",
                "ia_highlight": "IA: Termografía predictiva de tableros y balance de cargas inteligente."
            },
            {
                "file": "Controles_y_Maquinas_Electricas_Propuesta.html",
                "id": "controles_maquinas",
                "name": "Controles y Máquinas Eléctricas",
                "hours": 180,
                "modules": 10,
                "badge": "180 Horas • 10 Módulos",
                "icon": "cpu",
                "desc": "Variadores de frecuencia (VFD), arrancadores suaves, corrección de factor de potencia y megado de motores.",
                "ia_highlight": "IA: Análisis de firma de corriente (MCSA) para detectar barras rotas."
            },
            {
                "file": "Electronica_Analogica_Propuesta.html",
                "id": "electronica_analogica",
                "name": "Electrónica Analógica",
                "hours": 180,
                "modules": 10,
                "badge": "180 Horas • 10 Módulos",
                "icon": "activity",
                "desc": "Fuentes conmutadas (SMPS), amplificadores operacionales 4-20mA, reparación de tarjetas y optoacopladores.",
                "ia_highlight": "IA: Detección visual de componentes SMD quemados en PCB."
            },
            {
                "file": "Control_Industrial_Sistemas_Programables_Propuesta.html",
                "id": "control_programables",
                "name": "Control Industrial con Sistemas Programables",
                "hours": 180,
                "modules": 3,
                "badge": "180 Horas • 3 Módulos",
                "icon": "terminal",
                "desc": "PLC Siemens S7-1200 en TIA Portal, pantallas táctiles HMI, electroneumática y redes Modbus TCP.",
                "ia_highlight": "IA: Generación de código Structured Text (ST) con LLMs."
            },
            {
                "file": "Automatizacion_Industrial_Propuesta.html",
                "id": "automatizacion_industrial",
                "name": "Automatización Industrial",
                "hours": 180,
                "modules": 6,
                "badge": "180 Horas • 6 Módulos",
                "icon": "sliders",
                "desc": "Lazos PID de control continuo, transmisores HART (4-20mA), SCADA (Ignition / Node-RED) y redes Profinet.",
                "ia_highlight": "IA: Visión industrial para control de calidad y PID autónomo."
            }
        ]
    },
    {
        "id": "mecanica",
        "num": 3,
        "filename": "mecanica.html",
        "name": "Área de Mecánica Industrial, Soldadura y Calderas de Vapor",
        "short_name": "Mecánica & Calderas",
        "icon": "wrench",
        "color": "red",
        "total_hours": 540,
        "courses_count": 3,
        "desc": "Especialización para plantas de producción continua: mantenimiento mecánico preventivo y predictivo con alineación láser de ejes y análisis de vibraciones IoT, calificación de procedimientos y soldadores según códigos AWS D1.1 y ASME Sección IX (GMAW/FCAW y TIG en acero inoxidable alimenticio), operación segura de generadores de vapor, química de aguas y estricto cumplimiento del Reglamento de Calderas del Ministerio de Trabajo.",
        "normas": "AWS D1.1, ASME Sección IX, Reglamento de Calderas MinTrab, ISO 10816",
        "courses": [
            {
                "file": "Mantenimiento_Mecanico_Industrial_Propuesta.html",
                "id": "mantenimiento_mecanico",
                "name": "Mantenimiento Mecánico Industrial",
                "hours": 180,
                "modules": 10,
                "badge": "180 Horas • 10 Módulos",
                "icon": "tool",
                "desc": "Alineación láser de ejes, calentadores de inducción para rodamientos, tribología y detección de fugas por ultrasonido.",
                "ia_highlight": "IA: Análisis de vibraciones mecánicas IoT y diagnóstico prescriptivo."
            },
            {
                "file": "Soldadura_Industrial_Propuesta.html",
                "id": "soldadura_industrial",
                "name": "Soldadura Industrial",
                "hours": 180,
                "modules": 10,
                "badge": "180 Horas • 10 Módulos",
                "icon": "flame",
                "desc": "Calificación según AWS D1.1 y ASME IX, procesos GMAW/FCAW pesados, TIG sanitario en acero inoxidable y líquidos penetrantes.",
                "ia_highlight": "IA: Inspección de cordones por visión artificial y simuladores VR."
            },
            {
                "file": "Calderas_de_Vapor_Propuesta.html",
                "id": "calderas_vapor",
                "name": "Calderas de Vapor",
                "hours": 180,
                "modules": 5,
                "badge": "180 Horas • 5 Módulos",
                "icon": "gauge",
                "desc": "Tratamiento químico de agua, quemadores modulantes, retorno de condensados y cumplimiento del Reglamento de Calderas MinTrab.",
                "ia_highlight": "IA: Optimización de combustión y monitoreo de trampas de vapor."
            }
        ]
    },
    {
        "id": "automotriz",
        "num": 4,
        "filename": "automotriz.html",
        "name": "Área de Tecnología Automotriz y Motocicletas",
        "short_name": "Automotriz & Motos",
        "icon": "car",
        "color": "blue",
        "total_hours": 1080,
        "courses_count": 6,
        "desc": "Modernización de vanguardia en mecánica vehicular y de 2 ruedas: diagnóstico computarizado con escáner y osciloscopio automotriz de 4 canales, motores con distribución variable (VVT) y ciclo Atkinson/GDI, sistemas de seguridad activa ABS/ESP con ciclado electrónico, cajas automáticas CVT, redes multiplexadas CAN-Bus y LIN, protocolos de seguridad NFPA 70E para alta tensión en vehículos híbridos, transición ecológica al gas R-1234yf y sistemas de inyección electrónica (FI) en motocicletas.",
        "normas": "OBD-II, CAN-Bus ISO 11898, NFPA 70E (Alta Tensión Híbridos), SAE J2843 (R-1234yf)",
        "courses": [
            {
                "file": "Mecanica_Motores_Gasolina_Propuesta.html",
                "id": "motores_gasolina",
                "name": "Mecánica de Motores Gasolina",
                "hours": 180,
                "modules": 10,
                "badge": "180 Horas • 10 Módulos",
                "icon": "disc",
                "desc": "Distribución variable (VVT), probador de fugas de cilindro con manómetro, inyección directa GDI y motores ciclo Atkinson.",
                "ia_highlight": "IA: Diagnóstico acústico de golpeteo de biela e inspección con boroscopio."
            },
            {
                "file": "Mecanismos_del_Automovil_Propuesta.html",
                "id": "mecanismos_automovil",
                "name": "Mecanismos del Automóvil",
                "hours": 180,
                "modules": 10,
                "badge": "180 Horas • 10 Módulos",
                "icon": "settings",
                "desc": "Frenos ABS/ESP con ciclado electrónico, dirección eléctrica EPS, cajas automáticas/CVT y alineación 3D láser.",
                "ia_highlight": "IA: Reconocimiento por imagen de desgaste de neumáticos y calibración SAS."
            },
            {
                "file": "Electromecanica_Automotriz_Propuesta.html",
                "id": "electromecanica_automotriz",
                "name": "Electromecánica Automotriz",
                "hours": 180,
                "modules": 10,
                "badge": "180 Horas • 10 Módulos",
                "icon": "zap",
                "desc": "Redes multiplexadas CAN-Bus/LIN, alternadores pilotados, baterías AGM y protocolos de seguridad en alta tensión para híbridos.",
                "ia_highlight": "IA: Decodificación asistida de tramas CAN y diagramas interactivos."
            },
            {
                "file": "Inyeccion_Electronica_Automotriz_Propuesta.html",
                "id": "inyeccion_electronica",
                "name": "Inyección Electrónica Automotriz",
                "hours": 180,
                "modules": 10,
                "badge": "180 Horas • 10 Módulos",
                "icon": "radio",
                "desc": "Osciloscopio automotriz de 4 canales, sensores A/F de banda ancha, análisis de Fuel Trims y diésel Common Rail ligero.",
                "ia_highlight": "IA: Comparación automática de señales de osciloscopio y diagnóstico DTC."
            },
            {
                "file": "Aire_Acondicionado_Automotriz_Propuesta.html",
                "id": "aire_acondicionado",
                "name": "Aire Acondicionado Automotriz",
                "hours": 180,
                "modules": 2,
                "badge": "180 Horas • 2 Módulos",
                "icon": "wind",
                "desc": "Transición a gas R-1234yf, detección de fugas con Nitrógeno UV, compresores de cilindrada variable PWM y HVAC híbrido.",
                "ia_highlight": "IA: Termografía asistida de condensadores y dosificación por VIN."
            },
            {
                "file": "Mecanica_de_Motocicletas_Propuesta.html",
                "id": "mecanica_motocicletas",
                "name": "Mecánica de Motocicletas",
                "hours": 180,
                "modules": 6,
                "badge": "180 Horas • 6 Módulos",
                "icon": "navigation",
                "desc": "Sistemas de inyección electrónica en motos (FI), frenos ABS de rueda, escáner multimarca para 2 ruedas y CVT de scooters.",
                "ia_highlight": "IA: Diagnóstico por sonido de holgura de punterías y cruce de repuestos."
            }
        ]
    }
]

# Cargar el cuerpo HTML de cada uno de los 20 cursos desde historico
course_bodies = {}
for area in areas_data:
    for c in area["courses"]:
        fpath = os.path.join(rev_hist_dir, c["file"])
        if not os.path.exists(fpath):
            fpath = os.path.join(rev_dir, c["file"])
        with open(fpath, "r", encoding="utf-8", errors="ignore") as f:
            txt = f.read()
        m = re.search(r'<main[^>]*>(.*?)</main>', txt, re.DOTALL)
        body = m.group(1) if m else "<p>Contenido no disponible</p>"
        
        # Sanitizar IDs y onclicks
        body = re.sub(r'id=[\"\']propuesta[\"\']', f'id="propuesta_{c["id"]}"', body)
        body = re.sub(r'id=[\"\']btn-all[\"\']', f'id="btn-all-{c["id"]}"', body)
        body = re.sub(r'id=[\"\']btn-delete[\"\']', f'id="btn-delete-{c["id"]}"', body)
        body = re.sub(r'id=[\"\']btn-update[\"\']', f'id="btn-update-{c["id"]}"', body)
        body = re.sub(r'id=[\"\']btn-new[\"\']', f'id="btn-new-{c["id"]}"', body)
        body = re.sub(r'id=[\"\']btn-keep[\"\']', f'id="btn-keep-{c["id"]}"', body)
        body = re.sub(r'onclick=[\"\']filterItems\(([\'\"].*?[\'\"])\)[\"\']', f"onclick=\"filterEtsItems(\\1, '{c['id']}')\"", body)
        course_bodies[c["id"]] = body

print(f"Cargados con éxito {len(course_bodies)} cursos técnicos.")

# -------------------------------------------------------------
# 1. GENERAR PÁGINAS DEDICADAS POR ÁREA TÉCNICA
# -------------------------------------------------------------

def build_area_page(area):
    area_id = area["id"]
    area_title = area["name"]
    area_desc = area["desc"]
    area_courses = area["courses"]
    
    # Navegación entre áreas
    other_areas_links = ""
    for a in areas_data:
        if a["id"] == area_id:
            other_areas_links += f'<span class="px-2.5 py-1 rounded bg-blue-800 text-amber-300 font-bold">{a["short_name"]}</span>\n'
        else:
            other_areas_links += f'<a href="{a["filename"]}" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 transition">{a["short_name"]}</a>\n'
    
    # Selector rápido options
    quick_select_options = ""
    for c in area_courses:
        quick_select_options += f'<option value="{c["id"]}">{c["name"]} ({c["hours"]}h)</option>\n'
    
    # Tarjetas de cursos
    cards_html = ""
    for c in area_courses:
        cards_html += f"""
        <div class="area-course-card group bg-white p-5 rounded-2xl border border-slate-200 hover:border-blue-600 hover:shadow-lg transition cursor-pointer flex flex-col justify-between"
             onclick="showCourse('{c["id"]}')" id="card-{c["id"]}">
            <div class="space-y-3">
                <div class="flex justify-between items-start">
                    <span class="px-2.5 py-1 rounded-full bg-slate-100 text-slate-700 font-bold text-[11px] uppercase tracking-wider">
                        {c["badge"]}
                    </span>
                    <div class="w-8 h-8 rounded-lg bg-blue-50 text-blue-700 flex items-center justify-center group-hover:bg-blue-600 group-hover:text-white transition">
                        <i data-lucide="{c["icon"]}" class="w-4 h-4"></i>
                    </div>
                </div>
                <div>
                    <h4 class="text-base font-bold text-slate-900 group-hover:text-blue-700 transition">
                        {c["name"]}
                    </h4>
                    <p class="text-xs text-slate-600 mt-1 leading-relaxed">
                        {c["desc"]}
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
        
    # Paneles de detalle de cada curso del área
    details_html = ""
    for idx, c in enumerate(area_courses):
        body = course_bodies.get(c["id"], "<p>Contenido no disponible</p>")
        disp = "block" if idx == 0 else "none"
        details_html += f"""
        <div id="course-pane-{c["id"]}" class="course-detail-pane" style="display: {disp};">
            <div class="bg-slate-900 text-white p-4 rounded-t-2xl flex flex-wrap justify-between items-center gap-4">
                <div class="flex items-center gap-3">
                    <span class="px-2.5 py-1 rounded bg-blue-600 text-white text-xs font-bold uppercase">Curso {idx+1} de {len(area_courses)}</span>
                    <span class="text-slate-400">|</span>
                    <span class="text-slate-200 font-bold text-sm sm:text-base flex items-center gap-2">
                        <i data-lucide="{c["icon"]}" class="w-4 h-4 text-blue-400"></i>
                        {c["name"]} ({c["hours"]} Horas)
                    </span>
                </div>
                <div class="flex items-center gap-2">
                    <button onclick="scrollToSelector()" class="text-xs bg-slate-800 hover:bg-slate-700 text-slate-300 px-3 py-1.5 rounded-lg border border-slate-700 transition flex items-center gap-1.5">
                        <i data-lucide="grid" class="w-3.5 h-3.5"></i> Ver Lista de Cursos
                    </button>
                </div>
            </div>
            <div class="bg-white border-x border-b border-slate-200 rounded-b-2xl p-6 sm:p-8 space-y-8">
                {body}
            </div>
        </div>
        """
        
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{area_title} | Auditoría Curricular Kinal 2026</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@500;700;800&display=swap');
        body {{ font-family: 'Inter', sans-serif; background-color: #f8fafc; color: #0f172a; }}
        h1, h2, h3, h4, .font-heading {{ font-family: 'Space Grotesk', sans-serif; }}
        .item-delete {{ background-color: #fef2f2; border-left: 4px solid #ef4444; color: #991b1b; }}
        .item-update {{ background-color: #fefce8; border-left: 4px solid #eab308; color: #854d0e; }}
        .item-new {{ background-color: #eff6ff; border-left: 4px solid #3b82f6; color: #1e40af; }}
        .item-keep {{ background-color: #f0fdf4; border-left: 4px solid #22c55e; color: #166534; }}
        @media print {{ .no-print {{ display: none !important; }} }}
    </style>
</head>
<body class="antialiased min-h-screen flex flex-col">

    <!-- Header Corporativo -->
    <header class="bg-slate-900 text-white border-b border-slate-800 sticky top-0 z-50 shadow-md">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3 flex flex-wrap justify-between items-center gap-4">
            <div class="flex items-center gap-3">
                <a href="../index.html" class="bg-gradient-to-r from-amber-500 to-amber-600 text-slate-950 font-extrabold text-xs uppercase px-3 py-1.5 rounded-lg shadow-sm hover:opacity-90 transition flex items-center gap-1.5">
                    <i data-lucide="arrow-left" class="w-3.5 h-3.5"></i> Portal Maestro
                </a>
                <span class="text-slate-600 hidden sm:inline">|</span>
                <div class="text-white font-bold text-sm sm:text-base flex items-center gap-2">
                    <i data-lucide="{area["icon"]}" class="w-5 h-5 text-amber-400"></i>
                    {area_title}
                </div>
            </div>

            <!-- Navegación entre Áreas y TSU -->
            <div class="flex items-center gap-2 text-xs no-print">
                <a href="../TSU/index.html" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 transition">
                    TSU 3er Año
                </a>
                <a href="index.html" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-slate-200 transition">
                    Hub Áreas
                </a>
                <span class="text-slate-600">|</span>
                {other_areas_links}
            </div>
        </div>
    </header>

    <!-- Main Content -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8 flex-1">
        
        <!-- Hero de Área -->
        <div class="bg-white rounded-2xl border border-slate-200 p-6 sm:p-8 shadow-sm space-y-4">
            <div class="flex flex-wrap justify-between items-start gap-4">
                <div class="space-y-2 max-w-3xl">
                    <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-50 text-blue-700 text-xs font-bold border border-blue-200">
                        <i data-lucide="check-circle" class="w-3.5 h-3.5"></i> Auditoría Curricular 2026 • Escuela Técnica Superior Kinal
                    </div>
                    <h1 class="text-3xl sm:text-4xl font-extrabold text-slate-900 tracking-tight">
                        {area_title}
                    </h1>
                    <p class="text-slate-600 text-sm sm:text-base leading-relaxed">
                        {area_desc}
                    </p>
                </div>
                <div class="bg-slate-50 p-4 rounded-xl border border-slate-200 text-right space-y-1">
                    <div class="text-xs uppercase font-bold text-slate-500">Carga Formativa</div>
                    <div class="text-3xl font-black text-blue-900">{area["total_hours"]} Horas</div>
                    <div class="text-xs text-slate-600 font-medium">{len(area_courses)} Programas de Taller</div>
                </div>
            </div>

            <!-- Badges de Normas -->
            <div class="pt-3 border-t border-slate-100 flex flex-wrap items-center gap-2 text-xs">
                <span class="font-bold text-slate-700 flex items-center gap-1">
                    <i data-lucide="shield-check" class="w-3.5 h-3.5 text-emerald-600"></i> Normativa Industrial Aplicada:
                </span>
                <span class="px-2.5 py-0.5 rounded bg-emerald-50 text-emerald-800 border border-emerald-200 font-medium">
                    {area["normas"]}
                </span>
            </div>
        </div>

        <!-- Código de Color de Auditoría -->
        <div class="p-5 rounded-2xl bg-white border border-slate-200 shadow-sm space-y-3">
            <h3 class="text-xs font-bold text-slate-500 uppercase tracking-wider flex items-center gap-2">
                <i data-lucide="info" class="w-4 h-4 text-blue-600"></i> Metodología de Código de Color en esta Especialidad
            </h3>
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3 text-xs">
                <div class="p-3 rounded-xl bg-red-50 border border-red-200 text-red-900">
                    <strong class="text-red-700 block mb-1">🔴 ROJO (Eliminar)</strong>
                    Contenidos obsoletos retirados para optimizar el tiempo de taller.
                </div>
                <div class="p-3 rounded-xl bg-amber-50 border border-amber-200 text-amber-900">
                    <strong class="text-amber-700 block mb-1">🟡 AMARILLO (Actualizar)</strong>
                    Temas existentes modernizados según las normas vigentes.
                </div>
                <div class="p-3 rounded-xl bg-blue-50 border border-blue-200 text-blue-900">
                    <strong class="text-blue-700 block mb-1">🔵 AZUL (Propuesta Nueva)</strong>
                    Nuevas competencias prioritarias demandadas por la industria en Guatemala.
                </div>
                <div class="p-3 rounded-xl bg-purple-50 border border-purple-200 text-purple-900">
                    <strong class="text-purple-700 block mb-1">🟣 PÚRPURA (Innovación IA)</strong>
                    Módulos aplicados de Inteligencia Artificial en cada programa.
                </div>
            </div>
        </div>

        <!-- Selector de Cursos del Área -->
        <div id="course-selector-anchor" class="space-y-4">
            <div class="flex flex-wrap justify-between items-center gap-4">
                <div>
                    <h2 class="text-xl font-bold text-slate-900 flex items-center gap-2">
                        <i data-lucide="layers" class="w-5 h-5 text-blue-600"></i>
                        Cursos Auditados de esta Área
                    </h2>
                    <p class="text-xs text-slate-500">Haz clic en cualquier tarjeta para desplegar el informe completo de auditoría.</p>
                </div>
                <div class="flex items-center gap-2 text-xs">
                    <label for="area-quick-select" class="text-slate-600 font-semibold">Selector Rápido:</label>
                    <select id="area-quick-select" onchange="showCourse(this.value)" class="bg-white border border-slate-300 rounded-lg px-3 py-1.5 text-xs text-slate-800 font-medium focus:ring-2 focus:ring-blue-600">
                        {quick_select_options}
                    </select>
                </div>
            </div>

            <!-- Grid de Tarjetas de Cursos -->
            <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-4">
                {cards_html}
            </div>
        </div>

        <!-- Visor de Detalle del Curso Seleccionado -->
        <div id="detail-viewer-wrapper" class="space-y-4 pt-4">
            <div class="flex items-center justify-between text-xs font-bold text-slate-500 uppercase tracking-wider">
                <span class="flex items-center gap-1.5 text-blue-900">
                    <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse"></span>
                    Informe de Auditoría Completa del Curso
                </span>
            </div>

            <!-- Contenedores individuales de cursos -->
            {details_html}
        </div>

    </main>

    <!-- Footer -->
    <footer class="bg-slate-900 border-t border-slate-800 text-white py-6 text-center text-xs text-slate-400">
        <div class="max-w-7xl mx-auto px-4 space-y-1">
            <p class="font-semibold text-slate-200">Fundación Kinal • Escuela Técnica Superior (ETS) • Ciclo Académico 2026</p>
            <p>Auditoría Curricular y Ecosistema de Innovación con Inteligencia Artificial</p>
        </div>
    </footer>

    <script>
        lucide.createIcons();

        function showCourse(courseId) {{
            document.querySelectorAll('.course-detail-pane').forEach(el => el.style.display = 'none');
            const target = document.getElementById(`course-pane-${{courseId}}`);
            if (target) target.style.display = 'block';

            const sel = document.getElementById('area-quick-select');
            if (sel) sel.value = courseId;

            const viewer = document.getElementById('detail-viewer-wrapper');
            if (viewer) viewer.scrollIntoView({{ behavior: 'smooth', block: 'start' }});

            if (window.lucide) lucide.createIcons();
        }}

        function scrollToSelector() {{
            const el = document.getElementById('course-selector-anchor');
            if (el) el.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
        }}

        function filterEtsItems(status, courseId) {{
            const pane = document.getElementById(`course-pane-${{courseId}}`);
            if (!pane) return;
            const items = pane.querySelectorAll('.content-item');
            items.forEach(item => {{
                if (status === 'all') {{
                    item.style.display = 'block';
                }} else {{
                    if (item.getAttribute('data-status') === status) {{
                        item.style.display = 'block';
                    }} else {{
                        item.style.display = 'none';
                    }}
                }}
            }});

            const buttons = {{
                'all': document.getElementById(`btn-all-${{courseId}}`),
                'delete': document.getElementById(`btn-delete-${{courseId}}`),
                'update': document.getElementById(`btn-update-${{courseId}}`),
                'new': document.getElementById(`btn-new-${{courseId}}`),
                'keep': document.getElementById(`btn-keep-${{courseId}}`)
            }};

            Object.values(buttons).forEach(btn => {{
                if (btn) btn.classList.remove('ring-2', 'ring-offset-2', 'ring-slate-900', 'font-black');
            }});

            if (buttons[status]) {{
                buttons[status].classList.add('ring-2', 'ring-offset-2', 'ring-slate-900', 'font-black');
            }}
        }}
    </script>
</body>
</html>
"""
    return html

for area in areas_data:
    page_html = build_area_page(area)
    fpath = os.path.join(rev_dir, area["filename"])
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(page_html)
    print(f"✓ Generada página de área: {fpath} ({len(page_html)/1024:.1f} KB)")
    
    # Mirror en MyBrain
    mb_fpath = os.path.join(mybrain_rev, area["filename"])
    shutil.copy2(fpath, mb_fpath)

# -------------------------------------------------------------
# 2. GENERAR REVISION_TEMARIOS/INDEX.HTML (HUB DE ESPECIALIDADES ETS)
# -------------------------------------------------------------

hub_areas_cards = ""
for a in areas_data:
    hub_areas_cards += f"""
    <div class="bg-white rounded-2xl border border-slate-200 p-6 shadow-sm hover:shadow-md hover:border-blue-600 transition flex flex-col justify-between space-y-4">
        <div class="space-y-3">
            <div class="flex justify-between items-start">
                <span class="px-3 py-1 rounded-full bg-slate-100 text-slate-800 font-extrabold text-xs uppercase tracking-wider">
                    {a["courses_count"]} Cursos • {a["total_hours"]} Horas
                </span>
                <div class="w-10 h-10 rounded-xl bg-blue-50 text-blue-700 flex items-center justify-center">
                    <i data-lucide="{a["icon"]}" class="w-5 h-5"></i>
                </div>
            </div>
            <div>
                <h3 class="text-xl font-bold text-slate-900">{a["name"]}</h3>
                <p class="text-xs text-slate-600 mt-2 leading-relaxed">{a["desc"]}</p>
            </div>
        </div>
        <div class="pt-4 border-t border-slate-100 space-y-3">
            <div class="text-[11px] text-slate-500 font-medium">
                <strong>Normativa:</strong> {a["normas"]}
            </div>
            <a href="{a["filename"]}" class="block text-center w-full py-2.5 px-4 rounded-xl bg-blue-900 hover:bg-blue-800 text-white font-bold text-xs shadow transition flex items-center justify-center gap-1.5">
                Ver Auditoría Curricular del Área <i data-lucide="arrow-right" class="w-3.5 h-3.5"></i>
            </a>
        </div>
    </div>
    """

hub_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hub de Especialidades Técnicas | Auditoría Curricular ETS Kinal 2026</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@500;700;800&display=swap');
        body {{ font-family: 'Inter', sans-serif; background-color: #f8fafc; color: #0f172a; }}
        h1, h2, h3, h4, .font-heading {{ font-family: 'Space Grotesk', sans-serif; }}
    </style>
</head>
<body class="antialiased min-h-screen flex flex-col">

    <!-- Top Header -->
    <header class="bg-slate-900 text-white border-b border-slate-800 sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3.5 flex flex-wrap justify-between items-center gap-4">
            <div class="flex items-center gap-3">
                <a href="../index.html" class="bg-gradient-to-r from-amber-500 to-amber-600 text-slate-950 font-extrabold text-xs uppercase px-3 py-1.5 rounded-lg shadow-sm hover:opacity-90 transition flex items-center gap-1.5">
                    <i data-lucide="arrow-left" class="w-3.5 h-3.5"></i> Portal Maestro
                </a>
                <span class="text-slate-600">|</span>
                <span class="font-bold text-sm text-slate-200 flex items-center gap-2">
                    <i data-lucide="layers" class="w-4 h-4 text-blue-400"></i>
                    Escuela Técnica Superior (ETS) • Auditoría Curricular 2026
                </span>
            </div>
            <div class="flex items-center gap-2 text-xs">
                <a href="../TSU/index.html" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 transition font-medium">
                    Ir al TSU (3er Año)
                </a>
            </div>
        </div>
    </header>

    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 space-y-10 flex-1">
        
        <!-- Hero Section -->
        <div class="text-center space-y-3 max-w-4xl mx-auto">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-50 border border-blue-200 text-blue-800 text-xs font-semibold">
                <i data-lucide="sparkles" class="w-3.5 h-3.5 text-blue-600"></i> Ciclo Académico 2026 • Análisis de Demanda Industrial en Guatemala
            </div>
            <h1 class="text-3xl sm:text-5xl font-black text-slate-900 tracking-tight">
                Auditoría Curricular de Especialidades Técnicas & Ecosistema IA
            </h1>
            <p class="text-slate-600 text-base sm:text-lg leading-relaxed">
                Modernización integral de los programas técnicos de la Escuela Técnica Superior Kinal frente a las exigencias reales de los sectores productivos de Guatemala, complementado con <strong>módulos de Inteligencia Artificial aplicada</strong> en cada especialidad.
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

        <!-- Áreas Técnicas Grid -->
        <div class="space-y-4">
            <div>
                <h2 class="text-2xl font-bold text-slate-900">Selecciona un Área Técnica</h2>
                <p class="text-xs text-slate-500">Ingresa a cada área para ver el detalle curso por curso, investigación de mercado y dosificación temática con IA.</p>
            </div>
            <div class="grid md:grid-cols-2 gap-6">
                {hub_areas_cards}
            </div>
        </div>

    </main>

    <!-- Footer -->
    <footer class="bg-slate-900 text-white border-t border-slate-800 py-6 text-center text-xs text-slate-400">
        Fundación Kinal • Escuela Técnica Superior (ETS) • Auditoría Curricular 2026
    </footer>

    <script>
        lucide.createIcons();
    </script>
</body>
</html>
"""

rev_hub_path = os.path.join(rev_dir, "index.html")
with open(rev_hub_path, "w", encoding="utf-8") as f:
    f.write(hub_html)
print(f"✓ Generado Hub de Especialidades: {rev_hub_path}")
shutil.copy2(rev_hub_path, os.path.join(mybrain_rev, "index.html"))

# -------------------------------------------------------------
# 3. ACTUALIZAR TSU/INDEX.HTML (PÁGINA DEDICADA DEL TSU)
# -------------------------------------------------------------

import unify_tsu_portal
tsu_html = unify_tsu_portal.master_html

# Agregar enlace "← Portal Maestro" en la navegación del TSU
tsu_nav_search = '<nav class="nav-links">'
tsu_nav_replace = """<nav class="nav-links">
            <a href="../index.html" class="nav-item" style="color: #d97706; font-weight: 700; display: inline-flex; align-items: center; gap: 4px;">
                ← Portal Maestro
            </a>"""
tsu_html = tsu_html.replace(tsu_nav_search, tsu_nav_replace)

tsu_index_file = os.path.join(tsu_dir, "index.html")
with open(tsu_index_file, "w", encoding="utf-8") as f:
    f.write(tsu_html)
print(f"✓ Actualizado portal dedicado TSU: {tsu_index_file}")
shutil.copy2(tsu_index_file, os.path.join(mybrain_tsu, "index.html"))

# -------------------------------------------------------------
# 4. GENERAR PÁGINA PRINCIPAL RAÍZ (INDEX.HTML)
# -------------------------------------------------------------

root_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ecosistema Curricular & Didáctico Kinal 2026 | Portal Maestro</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@500;700;800;900&display=swap');
        body {{ font-family: 'Inter', sans-serif; background-color: #f8fafc; color: #0f172a; }}
        h1, h2, h3, h4, .font-heading {{ font-family: 'Space Grotesk', sans-serif; }}
        .hero-gradient {{
            background: linear-gradient(135deg, #09172e 0%, #0f2d59 50%, #1e3a8a 100%);
        }}
    </style>
</head>
<body class="antialiased min-h-screen flex flex-col">

    <!-- Header Corporativo -->
    <header class="bg-slate-950 text-white border-b border-slate-800 sticky top-0 z-50 shadow-md">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-3.5 flex flex-wrap justify-between items-center gap-4">
            <div class="flex items-center gap-3">
                <span class="bg-gradient-to-r from-amber-500 to-amber-600 text-slate-950 font-black text-xs tracking-wider uppercase px-2.5 py-1 rounded shadow-sm">
                    KINAL 2026
                </span>
                <span class="text-slate-600">|</span>
                <div class="text-slate-200 font-bold text-sm sm:text-base flex items-center gap-2">
                    <i data-lucide="graduation-cap" class="w-5 h-5 text-blue-400"></i>
                    Coordinación Académica & Diseño Curricular
                </div>
            </div>
            <nav class="flex items-center gap-3 text-xs">
                <a href="TSU/index.html" class="px-3 py-1.5 rounded-lg bg-blue-900/60 hover:bg-blue-800 text-amber-300 font-bold transition flex items-center gap-1">
                    <i data-lucide="book-open" class="w-3.5 h-3.5"></i> TSU (3er Año)
                </a>
                <a href="Revision_Temarios/index.html" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 transition font-medium flex items-center gap-1">
                    <i data-lucide="wrench" class="w-3.5 h-3.5"></i> Especialidades Técnicas
                </a>
            </nav>
        </div>
    </header>

    <!-- Hero de Alto Impacto -->
    <section class="hero-gradient text-white py-16 px-4 sm:px-6 lg:px-8">
        <div class="max-w-5xl mx-auto text-center space-y-5">
            <div class="inline-flex items-center gap-2 px-3 py-1 rounded-full bg-blue-500/20 border border-blue-400/30 text-blue-300 text-xs font-semibold">
                <i data-lucide="sparkles" class="w-3.5 h-3.5"></i> Ciclo Académico 2026 • Marco Alemán DQR 5/6 & Alianza UNIS-Kinal
            </div>
            <h1 class="text-4xl sm:text-6xl font-black tracking-tight leading-tight text-white">
                Sistema de Modernización Curricular e Instruccional
            </h1>
            <p class="text-slate-300 text-base sm:text-lg max-w-3xl mx-auto leading-relaxed">
                Portal central de acceso a los dos grandes pilares pedagógicos de Fundación Kinal: 
                el <strong>Año Académico del TSU (Técnico Superior Universitario)</strong> y la <strong>Auditoría Curricular de Especialidades Técnicas de Taller (ETS)</strong> con integración transversal de Inteligencia Artificial.
            </p>

            <!-- Métricas Clave Consolidadas -->
            <div class="grid grid-cols-2 md:grid-cols-4 gap-4 pt-6 max-w-4xl mx-auto text-left">
                <div class="bg-white/10 backdrop-blur rounded-2xl p-4 border border-white/10 space-y-1">
                    <div class="text-[11px] uppercase tracking-wider text-slate-300 font-bold">Total Asignaturas</div>
                    <div class="text-3xl font-black text-white">40 Cursos</div>
                    <div class="text-[11px] text-amber-300">20 TSU + 20 Especialidades</div>
                </div>
                <div class="bg-white/10 backdrop-blur rounded-2xl p-4 border border-white/10 space-y-1">
                    <div class="text-[11px] uppercase tracking-wider text-slate-300 font-bold">Carga Presencial</div>
                    <div class="text-3xl font-black text-white">3,510 hrs</div>
                    <div class="text-[11px] text-emerald-300">270h TSU + 3,240h Talleres</div>
                </div>
                <div class="bg-white/10 backdrop-blur rounded-2xl p-4 border border-white/10 space-y-1">
                    <div class="text-[11px] uppercase tracking-wider text-slate-300 font-bold">Ecosistema IA</div>
                    <div class="text-3xl font-black text-purple-300">80 Módulos</div>
                    <div class="text-[11px] text-purple-200">Visión, LLMs, IoT y Simulación</div>
                </div>
                <div class="bg-white/10 backdrop-blur rounded-2xl p-4 border border-white/10 space-y-1">
                    <div class="text-[11px] uppercase tracking-wider text-slate-300 font-bold">Aprobación Mínima</div>
                    <div class="text-3xl font-black text-amber-400">75 Pts</div>
                    <div class="text-[11px] text-slate-300">Regla Estricta + Inglés A2</div>
                </div>
            </div>
        </div>
    </section>

    <!-- Selector Principal de Pilares Formativos -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 space-y-16 flex-1">
        
        <div class="text-center space-y-2 max-w-2xl mx-auto">
            <h2 class="text-2xl sm:text-3xl font-extrabold text-slate-900 tracking-tight">
                Selecciona la Dimensión Curricular a Explorar
            </h2>
            <p class="text-slate-500 text-sm">
                Accede a la troncal universitaria de tercer año o ingresa directamente a las auditorías técnicas por especialidad.
            </p>
        </div>

        <div class="grid lg:grid-cols-2 gap-8">
            
            <!-- PILAR 1: TSU (AÑO ACADÉMICO) -->
            <div class="bg-white rounded-3xl border-2 border-slate-200 hover:border-blue-600 p-8 shadow-sm hover:shadow-xl transition flex flex-col justify-between space-y-6 group">
                <div class="space-y-5">
                    <div class="flex justify-between items-start">
                        <span class="px-3.5 py-1.5 rounded-full bg-blue-50 text-blue-900 font-extrabold text-xs uppercase tracking-wider border border-blue-200">
                            Año Académico 3er Año • UNIS / Kinal
                        </span>
                        <div class="w-12 h-12 rounded-2xl bg-blue-900 text-white flex items-center justify-center group-hover:scale-105 transition shadow-sm">
                            <i data-lucide="graduation-cap" class="w-6 h-6 text-amber-400"></i>
                        </div>
                    </div>
                    <div>
                        <h3 class="text-2xl font-black text-slate-900 group-hover:text-blue-900 transition">
                            Técnico Superior Universitario (TSU)
                        </h3>
                        <p class="text-slate-600 text-sm mt-2 leading-relaxed">
                            Troncal académica y transversal de gestión técnica e industrial para los graduados de Kinal que cursan el 3er año universitario avalado por la Universidad del Istmo (UNIS).
                        </p>
                    </div>

                    <!-- Componentes Clave TSU -->
                    <div class="space-y-2.5 pt-2 text-xs">
                        <div class="flex items-center gap-2 text-slate-700">
                            <i data-lucide="check-circle" class="w-4 h-4 text-emerald-600 shrink-0"></i>
                            <span><strong>Mapa Curricular & Red SVG:</strong> Matriz 4x4 y grafo de prerrequisitos interactivo en tiempo real.</span>
                        </div>
                        <div class="flex items-center gap-2 text-slate-700">
                            <i data-lucide="check-circle" class="w-4 h-4 text-emerald-600 shrink-0"></i>
                            <span><strong>4 Líneas Formativas:</strong> Administración Industrial, Ética Integral, Física y Matemática Aplicada (20 asignaturas).</span>
                        </div>
                        <div class="flex items-center gap-2 text-slate-700">
                            <i data-lucide="check-circle" class="w-4 h-4 text-emerald-600 shrink-0"></i>
                            <span><strong>Auditoría & Dictamen TSU:</strong> Contenidos anulados, modernizaciones y justificaciones laborales CIG.</span>
                        </div>
                        <div class="flex items-center gap-2 text-slate-700">
                            <i data-lucide="check-circle" class="w-4 h-4 text-emerald-600 shrink-0"></i>
                            <span><strong>Operación Bimestral:</strong> Dosificación en 4 bimestres con 5 períodos diarios de 50 minutos.</span>
                        </div>
                    </div>
                </div>

                <div class="pt-6 border-t border-slate-100">
                    <a href="TSU/index.html" class="w-full py-3.5 px-6 rounded-2xl bg-blue-900 hover:bg-blue-800 text-white font-extrabold text-sm shadow-md transition flex items-center justify-center gap-2">
                        Explorar Año Académico del TSU <i data-lucide="arrow-right" class="w-4 h-4 text-amber-400"></i>
                    </a>
                </div>
            </div>

            <!-- PILAR 2: ESPECIALIDADES TÉCNICAS (ETS) -->
            <div class="bg-white rounded-3xl border-2 border-slate-200 hover:border-amber-500 p-8 shadow-sm hover:shadow-xl transition flex flex-col justify-between space-y-6 group">
                <div class="space-y-5">
                    <div class="flex justify-between items-start">
                        <span class="px-3.5 py-1.5 rounded-full bg-amber-50 text-amber-900 font-extrabold text-xs uppercase tracking-wider border border-amber-200">
                            Escuela Técnica Superior (ETS) • 3,240 Horas
                        </span>
                        <div class="w-12 h-12 rounded-2xl bg-amber-600 text-white flex items-center justify-center group-hover:scale-105 transition shadow-sm">
                            <i data-lucide="wrench" class="w-6 h-6 text-white"></i>
                        </div>
                    </div>
                    <div>
                        <h3 class="text-2xl font-black text-slate-900 group-hover:text-amber-800 transition">
                            Auditoría de Especialidades Técnicas
                        </h3>
                        <p class="text-slate-600 text-sm mt-2 leading-relaxed">
                            Revisión curricular integral de los 20 programas técnicos de especialidad en taller, auditados individualmente con código de color (Eliminar, Actualizar, Nuevos, Mantener) e Inteligencia Artificial.
                        </p>
                    </div>

                    <!-- Componentes Clave ETS -->
                    <div class="space-y-2.5 pt-2 text-xs">
                        <div class="flex items-center gap-2 text-slate-700">
                            <i data-lucide="check-circle" class="w-4 h-4 text-amber-600 shrink-0"></i>
                            <span><strong>1,276 Temas Auditados:</strong> Desglose analítico tema por tema con filtros interactivos.</span>
                        </div>
                        <div class="flex items-center gap-2 text-slate-700">
                            <i data-lucide="check-circle" class="w-4 h-4 text-amber-600 shrink-0"></i>
                            <span><strong>Demanda Industrial Guatemala:</strong> Salarios reales (Q4,000 - Q8,000), normas AGIES, CNEE y MinTrab 229.</span>
                        </div>
                        <div class="flex items-center gap-2 text-slate-700">
                            <i data-lucide="check-circle" class="w-4 h-4 text-amber-600 shrink-0"></i>
                            <span><strong>Ecosistema con IA:</strong> 60 casos prácticos de visión artificial, IoT, LLMs y simuladores.</span>
                        </div>
                        <div class="flex items-center gap-2 text-slate-700">
                            <i data-lucide="check-circle" class="w-4 h-4 text-amber-600 shrink-0"></i>
                            <span><strong>Fichas Oficiales ("Reporte"):</strong> Horarios, costos, jornadas y perfiles de egreso oficiales.</span>
                        </div>
                    </div>
                </div>

                <div class="pt-6 border-t border-slate-100">
                    <a href="Revision_Temarios/index.html" class="w-full py-3.5 px-6 rounded-2xl bg-amber-600 hover:bg-amber-700 text-slate-950 font-extrabold text-sm shadow-md transition flex items-center justify-center gap-2">
                        Explorar Hub de Especialidades Técnicas <i data-lucide="arrow-right" class="w-4 h-4 text-slate-950"></i>
                    </a>
                </div>
            </div>

        </div>

        <!-- Acceso Directo a las 4 Áreas Técnicas -->
        <div class="space-y-6 pt-4">
            <div class="border-b border-slate-200 pb-3 flex flex-wrap justify-between items-end gap-2">
                <div>
                    <h3 class="text-xl sm:text-2xl font-bold text-slate-900">
                        Acceso Directo a las 4 Áreas Técnicas Industriales
                    </h3>
                    <p class="text-xs text-slate-500 mt-1">Consulta la auditoría curricular completa de cada especialidad técnica.</p>
                </div>
                <a href="Revision_Temarios/index.html" class="text-xs text-blue-700 font-bold hover:underline flex items-center gap-1">
                    Ver vista resumen de las 4 áreas <i data-lucide="chevron-right" class="w-3 h-3"></i>
                </a>
            </div>

            <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-5">
                
                <!-- Área 1 -->
                <div class="bg-white rounded-2xl border border-slate-200 p-5 shadow-sm hover:border-amber-500 hover:shadow-md transition flex flex-col justify-between space-y-4">
                    <div class="space-y-2">
                        <div class="flex justify-between items-center">
                            <span class="px-2.5 py-0.5 rounded-full bg-amber-50 text-amber-800 font-bold text-[10px] uppercase">6 Cursos • 720h</span>
                            <i data-lucide="hard-hat" class="w-5 h-5 text-amber-600"></i>
                        </div>
                        <h4 class="font-bold text-base text-slate-900">Construcción & BIM</h4>
                        <p class="text-xs text-slate-600 leading-relaxed">
                            Fundamentos, Adm. de Obras, AutoCAD 2D/3D, Revit Architecture, Revit Structure & MEP, Civil 3D.
                        </p>
                    </div>
                    <a href="Revision_Temarios/construccion.html" class="block w-full py-2 px-3 rounded-xl bg-slate-900 hover:bg-slate-800 text-white font-bold text-xs text-center transition">
                        Ver Área Construcción →
                    </a>
                </div>

                <!-- Área 2 -->
                <div class="bg-white rounded-2xl border border-slate-200 p-5 shadow-sm hover:border-yellow-500 hover:shadow-md transition flex flex-col justify-between space-y-4">
                    <div class="space-y-2">
                        <div class="flex justify-between items-center">
                            <span class="px-2.5 py-0.5 rounded-full bg-yellow-50 text-yellow-800 font-bold text-[10px] uppercase">5 Cursos • 900h</span>
                            <i data-lucide="zap" class="w-5 h-5 text-yellow-600"></i>
                        </div>
                        <h4 class="font-bold text-base text-slate-900">Electricidad & Automatización</h4>
                        <p class="text-xs text-slate-600 leading-relaxed">
                            Instalaciones Eléctricas, Controles y Máquinas, Electrónica Analógica, PLC Siemens S7-1200, Automatización SCADA.
                        </p>
                    </div>
                    <a href="Revision_Temarios/electricidad.html" class="block w-full py-2 px-3 rounded-xl bg-slate-900 hover:bg-slate-800 text-white font-bold text-xs text-center transition">
                        Ver Área Electricidad →
                    </a>
                </div>

                <!-- Área 3 -->
                <div class="bg-white rounded-2xl border border-slate-200 p-5 shadow-sm hover:border-red-500 hover:shadow-md transition flex flex-col justify-between space-y-4">
                    <div class="space-y-2">
                        <div class="flex justify-between items-center">
                            <span class="px-2.5 py-0.5 rounded-full bg-red-50 text-red-800 font-bold text-[10px] uppercase">3 Cursos • 540h</span>
                            <i data-lucide="wrench" class="w-5 h-5 text-red-600"></i>
                        </div>
                        <h4 class="font-bold text-base text-slate-900">Mecánica & Soldadura</h4>
                        <p class="text-xs text-slate-600 leading-relaxed">
                            Mantenimiento Mecánico Industrial, Soldadura Calificada (AWS/ASME), Calderas de Vapor (MinTrab).
                        </p>
                    </div>
                    <a href="Revision_Temarios/mecanica.html" class="block w-full py-2 px-3 rounded-xl bg-slate-900 hover:bg-slate-800 text-white font-bold text-xs text-center transition">
                        Ver Área Mecánica →
                    </a>
                </div>

                <!-- Área 4 -->
                <div class="bg-white rounded-2xl border border-slate-200 p-5 shadow-sm hover:border-blue-500 hover:shadow-md transition flex flex-col justify-between space-y-4">
                    <div class="space-y-2">
                        <div class="flex justify-between items-center">
                            <span class="px-2.5 py-0.5 rounded-full bg-blue-50 text-blue-800 font-bold text-[10px] uppercase">6 Cursos • 1,080h</span>
                            <i data-lucide="car" class="w-5 h-5 text-blue-600"></i>
                        </div>
                        <h4 class="font-bold text-base text-slate-900">Automotriz & Motocicletas</h4>
                        <p class="text-xs text-slate-600 leading-relaxed">
                            Motores Gasolina VVT, Mecanismos ABS/ESP, Electromecánica CAN-Bus, Inyección Electrónica, HVAC R-1234yf, Motos FI.
                        </p>
                    </div>
                    <a href="Revision_Temarios/automotriz.html" class="block w-full py-2 px-3 rounded-xl bg-slate-900 hover:bg-slate-800 text-white font-bold text-xs text-center transition">
                        Ver Área Automotriz →
                    </a>
                </div>

            </div>
        </div>

    </main>

    <!-- Footer Institucional -->
    <footer class="bg-slate-950 text-white border-t border-slate-800 py-10 text-xs text-slate-400">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-4 text-center sm:text-left sm:flex sm:justify-between sm:items-center">
            <div class="space-y-1">
                <p class="font-bold text-white text-sm">Fundación Kinal • Coordinación Académica & Curricular</p>
                <p>Sistema Integral de Diseño Curricular, Auditoría Técnica y Didáctica Dual • Ciclo 2026</p>
            </div>
            <div class="text-slate-500 text-[11px] space-y-0.5">
                <p>Alineado a los estándares DQR 5/6 y al marco legal del trabajo y educación técnica en Guatemala.</p>
                <p>Nota mínima de aprobación: 75/100 | Nivel de inglés: A2 (ELASH II).</p>
            </div>
        </div>
    </footer>

    <script>
        lucide.createIcons();
    </script>
</body>
</html>
"""

root_index_path = os.path.join(base_dir, "index.html")
with open(root_index_path, "w", encoding="utf-8") as f:
    f.write(root_html)
print(f"✓ Generada Página Principal Raíz: {root_index_path}")
shutil.copy2(root_index_path, os.path.join(mybrain_base, "index.html"))

print("\n¡Reorganización completa finalizada con éxito!")
