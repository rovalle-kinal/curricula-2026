#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador Maestro del Repositorio 'electronica-cet'
Incluye:
1. index.html: Portal HOME para seleccionar entre Electrónica CET e Informática CET,
   con resumen ejecutivo 'for dummies' de temas a eliminar y actualizar y su justificación clara.
2. electronica.html: Auditoría y temario detallado de Electrónica CET (botón home -> index.html).
3. informatica.html: Auditoría y temario detallado de Informática CET (botón home -> index.html).
Sin contraseñas (acceso directo y abierto).
"""

import json
import os
import shutil
import html

REPO_DIR = r"D:\OneDrive\Software\Antigravity\Diseño Instruccional\rovalle-kinal.git\electronica-cet"
INFORMATICA_SRC_DIR = r"D:\OneDrive\Software\Antigravity\Diseño Instruccional\rovalle-kinal.git\informatica-cet"

ELECTRONICA_JSON = os.path.join(REPO_DIR, "pensum_data.json")
INFORMATICA_JSON = os.path.join(INFORMATICA_SRC_DIR, "pensum_data.json")

def generate_subportal_html(data, portal_type):
    """
    Genera el HTML detallado para electronica.html o informatica.html
    con el botón de Home apuntando a 'index.html'.
    """
    is_elec = portal_type == 'electronica'
    
    if is_elec:
        portal_title = "Auditoría Curricular y Catálogo de Pensum CET • Electrónica"
        page_title = "Auditoría Curricular y Pensum CET • Electrónica | Fundación Kinal"
        area_badge = "Centro Escolar Técnico (CET) • Área de Electrónica y Dispositivos Digitales"
        hero_desc = (
            "Auditoría técnica exhaustiva de los núcleos temáticos del ciclo diversificado frente a la demanda laboral "
            "del sector industrial guatemalteco, articulado con el Marco DQR, el Sistema Dual en Alternancia "
            "y la incorporación de la Inteligencia Artificial como coworker de taller."
        )
        careers_meta = [
            {"id": "quinto_electronica", "name": "5to Perito en Electrónica", "badge": "Ciclo Troncal • 4 Bimestres", "icon": "cpu"},
            {"id": "sexto_industrial", "name": "6to Perito en Electrónica Industrial", "badge": "Especialidad • 3 Bimestres", "icon": "factory"},
            {"id": "sexto_computacion", "name": "6to Perito en Electrónica en Computación", "badge": "Especialidad • 3 Bimestres", "icon": "network"}
        ]
        ets_spec_notes = (
            "• Diferenciación CET vs ETS: En CET diversificado se consolidan el cableado normado, lógica digital aplicada, "
            "microcontroladores modernos con C++, parametrización de variadores, lectura de planos IEC y redes IPv4/MikroTik. "
            "Las competencias de nivel terciario ETS (TSU / DQR 6) abarcan programación abstracta en SCL/IEC 61131-3, lazos PID "
            "complejos, DCS, ciberseguridad industrial OT y enrutamiento corporativo BGP/MPLS."
        )
    else:
        portal_title = "Auditoría Curricular y Catálogo de Pensum CET • Informática"
        page_title = "Auditoría Curricular y Pensum CET • Informática | Fundación Kinal"
        area_badge = "Centro Escolar Técnico (CET) • Área de Informática y Computación"
        hero_desc = (
            "Auditoría técnica rigurosa de los núcleos temáticos del ciclo diversificado frente a las exigencias de la industria "
            "del software y servicios digitales de Guatemala, alineado con el Marco DQR, el Sistema Dual de Formación "
            "y la integración transversal de la Inteligencia Artificial como copiloto de ingeniería."
        )
        careers_meta = [
            {"id": "cuarto_informatica", "name": "4to Perito en Informática", "badge": "Ciclo Troncal • 4 Bimestres", "icon": "binary"},
            {"id": "quinto_informatica", "name": "5to Perito en Informática", "badge": "Ingeniería de Software • 4 Bimestres", "icon": "code-2"},
            {"id": "sexto_informatica", "name": "6to Perito en Informática", "badge": "Full-Stack & Cloud • 3 Bimestres", "icon": "cloud"}
        ]
        ets_spec_notes = (
            "• Diferenciación CET vs ETS: En CET diversificado se desarrollan fundamentos sólidos de algoritmia, POO con Java, "
            "bases de datos relacionales normalizadas (PostgreSQL/MySQL), APIs RESTful, React, Docker básico y control de versiones con Git Flow. "
            "Las competencias de nivel terciario ETS (TSU / DQR 6) corresponden a arquitecturas de microservicios distribuidos a gran escala, "
            "clústeres Kubernetes en alta disponibilidad, ciberseguridad ofensiva, telemetría distribuida APM y modelos de machine learning."
        )

    # Compute stats
    total_topics = 0
    stats = {"adecuado": 0, "revisar": 0, "eliminar": 0, "propuesto": 0}
    summary_topics = []
    
    for c_meta in careers_meta:
        cid = c_meta["id"]
        if cid in data:
            career = data[cid]
            c_name = career.get("title", c_meta["name"])
            for b in career.get("bimestres", []):
                b_num = b.get("bimestre_num", 1)
                b_name = b.get("nombre", f"Bimestre {b_num}")
                for t in b.get("temas", []):
                    total_topics += 1
                    st = t.get("estado", "adecuado")
                    stats[st] = stats.get(st, 0) + 1
                    
                    if st in ["eliminar", "revisar", "propuesto"]:
                        summary_topics.append({
                            "career_id": cid,
                            "career_name": c_name,
                            "bimestre_num": b_num,
                            "bimestre_name": b_name,
                            "nombre": t.get("nombre", ""),
                            "descripcion": t.get("descripcion", ""),
                            "estado": st,
                            "justificacion": t.get("justificacion", ""),
                            "enfoque": t.get("enfoque", ""),
                            "tipo": t.get("tipo", "troncal")
                        })

    pct_adecuado = round((stats["adecuado"] / total_topics) * 100, 1) if total_topics else 0
    pct_revisar = round((stats["revisar"] / total_topics) * 100, 1) if total_topics else 0
    pct_eliminar = round((stats["eliminar"] / total_topics) * 100, 1) if total_topics else 0
    pct_propuesto = round((stats["propuesto"] / total_topics) * 100, 1) if total_topics else 0

    # Build Summary Table Rows HTML
    summary_rows_html = []
    for item in summary_topics:
        st = item["estado"]
        if st == "eliminar":
            badge_class = "bg-red-100 text-red-800 border-red-200"
            dictamen_label = "🔴 Eliminar"
            status_filter_val = "delete"
        elif st == "revisar":
            badge_class = "bg-amber-100 text-amber-800 border-amber-200"
            dictamen_label = "🟡 Actualizar"
            status_filter_val = "update"
        else:
            badge_class = "bg-purple-100 text-purple-800 border-purple-200"
            dictamen_label = "🟣 Propuesta IA / Innovación"
            status_filter_val = "proposal"

        row_html = f"""
        <tr class="summary-table-row border-b border-slate-100 hover:bg-slate-50/80 transition" data-career="{item['career_id']}" data-status="{status_filter_val}">
            <td class="p-4 align-top whitespace-nowrap">
                <span class="inline-block px-2.5 py-1 rounded text-[11px] font-bold bg-[#152244] text-white">
                    {html.escape(item['career_name'])}
                </span>
                <div class="text-[11px] text-slate-500 font-medium mt-1">Bimestre {item['bimestre_num']}</div>
            </td>
            <td class="p-4 align-top">
                <div class="font-bold text-slate-900 text-sm leading-snug">{html.escape(item['nombre'])}</div>
                <div class="text-xs text-slate-500 mt-1 leading-relaxed">{html.escape(item['descripcion'])}</div>
                {f'<div class="mt-2 text-xs text-slate-600 bg-slate-50 p-2 rounded border border-slate-200 flex items-start gap-1.5"><i data-lucide="wrench" class="w-3.5 h-3.5 text-[#EC9123] shrink-0 mt-0.5"></i><span><strong>Enfoque práctico:</strong> {html.escape(item["enfoque"])}</span></div>' if item["enfoque"] else ''}
            </td>
            <td class="p-4 align-top whitespace-nowrap">
                <span class="inline-flex items-center gap-1.5 px-3 py-1 rounded-full text-xs font-bold border {badge_class}">
                    {dictamen_label}
                </span>
            </td>
            <td class="p-4 align-top text-xs text-slate-700 leading-relaxed max-w-md">
                <div class="bg-white p-3 rounded-lg border border-slate-200 shadow-2xs">
                    <strong class="text-slate-900 block mb-1">Fundamento Curricular / Industria:</strong>
                    {html.escape(item['justificacion'])}
                </div>
            </td>
        </tr>
        """
        summary_rows_html.append(row_html)

    # Build Detailed Bimester Cards HTML
    career_tabs_content = []
    for c_meta in careers_meta:
        cid = c_meta["id"]
        career_data = data.get(cid, {})
        c_title = career_data.get("title", c_meta["name"])
        c_subtitle = career_data.get("subtitle", "")
        c_docente = career_data.get("docente", "")
        c_horas = career_data.get("horas", "")
        bimestres = career_data.get("bimestres", [])

        bimesters_cards_html = []
        for b in bimestres:
            b_num = b.get("bimestre_num", 1)
            b_name = b.get("nombre", f"Bimestre {b_num}")
            temas = b.get("temas", [])

            b_counts = {"adecuado": 0, "revisar": 0, "eliminar": 0, "propuesto": 0}
            for t in temas:
                st = t.get("estado", "adecuado")
                b_counts[st] = b_counts.get(st, 0) + 1

            temas_items_html = []
            for idx, t in enumerate(temas, 1):
                st = t.get("estado", "adecuado")
                t_nombre = t.get("nombre", "")
                t_desc = t.get("descripcion", "")
                t_just = t.get("justificacion", "")
                t_enf = t.get("enfoque", "")

                if st == "eliminar":
                    container_cls = "bg-red-50/70 border-l-4 border-red-500"
                    emoji_badge = '<span class="inline-flex items-center justify-center w-6 h-6 rounded-full bg-red-100 text-red-700 text-sm shadow-2xs shrink-0" title="Eliminar / Obsolescencia">🔴</span>'
                    status_data_val = "delete"
                elif st == "revisar":
                    container_cls = "bg-amber-50/70 border-l-4 border-amber-500"
                    emoji_badge = '<span class="inline-flex items-center justify-center w-6 h-6 rounded-full bg-amber-100 text-amber-800 text-sm shadow-2xs shrink-0" title="Actualizar / Modernizar">🟡</span>'
                    status_data_val = "update"
                elif st == "propuesto":
                    container_cls = "bg-purple-50/70 border-l-4 border-purple-500"
                    emoji_badge = '<span class="inline-flex items-center justify-center w-6 h-6 rounded-full bg-purple-100 text-purple-700 text-sm shadow-2xs shrink-0" title="Propuesta IA / Innovación">🟣</span>'
                    status_data_val = "proposal"
                else:
                    container_cls = "bg-emerald-50/70 border-l-4 border-emerald-500"
                    emoji_badge = '<span class="inline-flex items-center justify-center w-6 h-6 rounded-full bg-emerald-100 text-emerald-800 text-sm shadow-2xs shrink-0" title="Adecuado / Mantener">🟢</span>'
                    status_data_val = "keep"

                t_html = f"""
                <div class="bimester-topic-card {container_cls} rounded-xl p-3.5 border border-slate-200/80 transition-all duration-200 hover:shadow-sm" data-status="{status_data_val}" data-title="{html.escape(t_nombre.lower())}">
                    <div class="flex items-start justify-between gap-3">
                        <div class="flex-1">
                            <div class="flex items-baseline gap-2">
                                <span class="text-[11px] font-bold text-slate-400 select-none">{idx}.</span>
                                <h5 class="text-sm font-bold text-slate-900 leading-snug">{html.escape(t_nombre)}</h5>
                            </div>
                            <p class="text-xs text-slate-600 mt-1.5 leading-relaxed">{html.escape(t_desc)}</p>
                            
                            {f'''
                            <div class="mt-2 text-xs text-slate-700 bg-white/80 p-2 rounded-lg border border-slate-200">
                                <strong class="text-slate-800">Justificación:</strong> {html.escape(t_just)}
                            </div>
                            ''' if t_just and st in ['eliminar', 'revisar', 'propuesto'] else ''}

                            {f'''
                            <div class="mt-1.5 text-[11px] text-slate-500 flex items-start gap-1">
                                <i data-lucide="wrench" class="w-3 h-3 text-[#EC9123] shrink-0 mt-0.5"></i>
                                <span><strong>Enfoque práctico:</strong> {html.escape(t_enf)}</span>
                            </div>
                            ''' if t_enf else ''}
                        </div>
                        {emoji_badge}
                    </div>
                </div>
                """
                temas_items_html.append(t_html)

            bimester_card_html = f"""
            <div class="bimester-card bg-white rounded-2xl border border-slate-300 shadow-md overflow-hidden flex flex-col transition hover:border-[#22376D]/40">
                <div class="bg-[#152244] text-white p-5 border-b border-slate-700 flex flex-col justify-between gap-3">
                    <div class="flex flex-wrap items-center justify-between gap-2">
                        <span class="inline-flex items-center gap-1.5 px-2.5 py-0.5 rounded-full text-[11px] font-bold bg-[#EC9123] text-white uppercase tracking-wider">
                            <i data-lucide="calendar" class="w-3 h-3"></i> Bimestre {b_num}
                        </span>
                        <span class="text-xs text-slate-300 font-medium">
                            {len(temas)} Núcleos Temáticos
                        </span>
                    </div>
                    <div>
                        <h4 class="text-lg font-bold brand-serif text-white tracking-wide leading-tight">
                            {html.escape(b_name)}
                        </h4>
                    </div>
                    <div class="flex flex-wrap items-center gap-1.5 pt-1 text-[11px]">
                        <span class="px-2 py-0.5 rounded bg-emerald-950/80 text-emerald-300 border border-emerald-700/50 font-semibold" title="Adecuados">
                            🟢 {b_counts['adecuado']} Mantener
                        </span>
                        {f'<span class="px-2 py-0.5 rounded bg-amber-950/80 text-amber-300 border border-amber-700/50 font-semibold" title="Actualizar">🟡 {b_counts["revisar"]} Actualizar</span>' if b_counts['revisar'] > 0 else ''}
                        {f'<span class="px-2 py-0.5 rounded bg-red-950/80 text-red-300 border border-red-700/50 font-semibold" title="Eliminar">🔴 {b_counts["eliminar"]} Eliminar</span>' if b_counts['eliminar'] > 0 else ''}
                        {f'<span class="px-2 py-0.5 rounded bg-purple-950/80 text-purple-300 border border-purple-700/50 font-semibold" title="Propuestas">🟣 {b_counts["propuesto"]} Innovación</span>' if b_counts['propuesto'] > 0 else ''}
                    </div>
                </div>

                <div class="p-4 sm:p-5 flex-1 space-y-3 bg-slate-50/40">
                    {''.join(temas_items_html)}
                </div>
            </div>
            """
            bimesters_cards_html.append(bimester_card_html)

        career_section_html = f"""
        <div id="career-panel-{cid}" class="career-panel space-y-6" style="{'display: block;' if cid == careers_meta[0]['id'] else 'display: none;'}">
            <div class="bg-white rounded-2xl border border-slate-200 p-6 shadow-sm flex flex-col md:flex-row md:items-center justify-between gap-4">
                <div class="space-y-1">
                    <div class="inline-flex items-center gap-2 text-xs font-bold text-[#EC9123] uppercase tracking-wider">
                        <i data-lucide="award" class="w-4 h-4"></i> {html.escape(c_meta['badge'])}
                    </div>
                    <h3 class="text-2xl font-bold brand-serif text-[#22376D]">{html.escape(c_title)}</h3>
                    <p class="text-xs sm:text-sm text-slate-600 max-w-2xl">{html.escape(c_subtitle)}</p>
                </div>
                <div class="flex flex-col sm:flex-row md:flex-col gap-2 text-xs text-slate-700 bg-slate-50 p-4 rounded-xl border border-slate-200 shrink-0">
                    <div class="flex items-center gap-2">
                        <i data-lucide="clock" class="w-4 h-4 text-[#22376D]"></i>
                        <span><strong>Carga:</strong> {html.escape(c_horas)}</span>
                    </div>
                    {f'''
                    <div class="flex items-center gap-2">
                        <i data-lucide="users" class="w-4 h-4 text-[#22376D]"></i>
                        <span><strong>Cuerpo Docente:</strong> {html.escape(c_docente)}</span>
                    </div>
                    ''' if c_docente else ''}
                </div>
            </div>

            <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
                {''.join(bimesters_cards_html)}
            </div>
        </div>
        """
        career_tabs_content.append(career_section_html)

    html_template = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{page_title}</title>
    
    <link rel="icon" type="image/png" href="assets/escudo_kinal_cuadrado.png">
    
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://unpkg.com/lucide@latest"></script>
    
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Playfair+Display:ital,wght@0,600;0,700;0,800;0,900;1,600&display=swap" rel="stylesheet">

    <style>
        :root {{
            --kinal-blue: #22376D;
            --kinal-blue-dark: #152244;
            --kinal-blue-deep: #0D162C;
            --kinal-blue-light: #2E4A91;
            --kinal-flame: #EC9123;
            --kinal-gold: #F5A623;
            --kinal-gray-8c: #888B8D;
            --kinal-bg-light: #F8FAFC;
            --kinal-border: #DDE2E5;
        }}

        body {{
            font-family: Arial, Helvetica, "Nimbus Sans L", "Liberation Sans", sans-serif;
            background-color: var(--kinal-bg-light);
            color: #1E293B;
            -webkit-font-smoothing: antialiased;
        }}

        h1, h2, h3, h4, .font-kinal-title, .brand-serif {{
            font-family: "Times New Roman", Times, "Playfair Display", Georgia, serif;
            letter-spacing: -0.01em;
        }}

        .hero-kinal-gradient {{
            background: linear-gradient(135deg, #0D162C 0%, #152244 45%, #22376D 100%);
        }}

        @media (max-width: 767px) {{
            *, *::before, *::after {{ box-sizing: border-box !important; }}
            html, body {{ overflow-x: hidden !important; max-width: 100vw !important; }}
            .no-scrollbar::-webkit-scrollbar {{ display: none !important; }}
            .no-scrollbar {{ -ms-overflow-style: none !important; scrollbar-width: none !important; }}
        }}
    </style>
</head>
<body id="top" class="min-h-screen flex flex-col antialiased pt-[115px] sm:pt-[125px]">

    <!-- ENCABEZADO FIJO PERMANENTE -->
    <div class="fixed top-0 left-0 right-0 z-50 bg-white shadow-md border-b border-slate-200">
        
        <!-- BARRA INSTITUCIONAL SUPERIOR -->
        <div class="bg-[#152244] text-white text-xs border-b-2 border-[#EC9123]">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-1.5 flex flex-wrap justify-between items-center gap-2">
                <div class="flex items-center gap-3">
                    <span class="inline-flex items-center gap-1.5 font-bold tracking-wider uppercase text-[#EC9123]">
                        <i data-lucide="award" class="w-3.5 h-3.5"></i> Fundación Kinal
                    </span>
                    <span class="text-slate-500">|</span>
                    <span class="text-slate-300 font-medium hidden sm:inline">
                        Centro Escolar Técnico (CET) • Ideario: <em>«El trabajo bien hecho»</em>
                    </span>
                </div>
                <div class="flex items-center gap-4 text-slate-300 font-medium">
                    <span class="flex items-center gap-1.5">
                        <i data-lucide="calendar" class="w-3.5 h-3.5 text-[#EC9123]"></i> Ciclo Académico 2026
                    </span>
                    <span class="text-slate-600">|</span>
                    <span class="text-emerald-400 font-bold flex items-center gap-1">
                        <i data-lucide="shield-check" class="w-3.5 h-3.5"></i> Aval UNIS-Kinal
                    </span>
                </div>
            </div>
        </div>

        <!-- HEADER CORPORATIVO (LOGO ETS & BOTONES BLANCOS, INICIO AL FINAL A LA DERECHA) -->
        <header class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-2.5 sm:py-3 flex flex-wrap justify-between items-center gap-3">
            
            <div class="flex items-center">
                <a href="index.html" class="flex items-center group" title="Ir al Portal de Inicio">
                    <img src="assets/escuela_tecnica_superior.png" alt="Fundación Kinal - Escuela Técnica Superior" class="h-8 sm:h-10 w-auto object-contain transition group-hover:opacity-90">
                </a>
            </div>

            <nav class="flex items-center gap-2 sm:gap-3 text-xs overflow-x-auto no-scrollbar py-1 font-bold">
                <a href="#resumen" class="px-3.5 py-2 rounded-lg bg-white hover:bg-slate-50 text-[#22376D] transition flex items-center gap-1.5 shadow-sm whitespace-nowrap border border-slate-200">
                    <i data-lucide="file-check-2" class="w-4 h-4 text-[#EC9123]"></i> Resumen Ejecutivo
                </a>
                <a href="#temarios" class="px-3.5 py-2 rounded-lg bg-white hover:bg-slate-50 text-[#22376D] transition flex items-center gap-1.5 shadow-sm whitespace-nowrap border border-slate-200">
                    <i data-lucide="book-marked" class="w-4 h-4 text-[#EC9123]"></i> Temarios Bimestrales
                </a>
                <a href="#articulacion" class="px-3.5 py-2 rounded-lg bg-white hover:bg-slate-50 text-[#22376D] transition flex items-center gap-1.5 shadow-sm whitespace-nowrap border border-slate-200">
                    <i data-lucide="layers" class="w-4 h-4 text-[#EC9123]"></i> Articulación ETS
                </a>
                <!-- Botón de Inicio: al final, lo más a la derecha, solo icono de la casa, vuelve a index.html -->
                <a href="index.html" class="px-3.5 py-2 rounded-lg bg-white hover:bg-slate-50 text-[#22376D] transition flex items-center justify-center shadow-sm whitespace-nowrap border border-slate-200 ml-auto" title="Volver a Inicio (Selección de Pensums)">
                    <i data-lucide="home" class="w-4 h-4 text-[#EC9123]"></i>
                </a>
            </nav>
        </header>

    </div>

    <!-- HERO PRINCIPAL -->
    <section class="hero-kinal-gradient text-white py-12 sm:py-16 px-4 sm:px-6 lg:px-8 relative overflow-hidden">
        <div class="max-w-7xl mx-auto space-y-6 relative z-10">
            
            <div class="inline-flex items-center px-3.5 py-1.5 rounded-full bg-white/10 border border-white/20 text-[#EC9123] text-xs font-bold tracking-wide uppercase">
                <i data-lucide="shield" class="w-3.5 h-3.5 mr-1.5"></i>
                <span>{area_badge}</span>
            </div>

            <h1 class="text-3xl sm:text-4xl lg:text-5xl font-bold tracking-tight leading-tight brand-serif text-white">
                {portal_title}
            </h1>

            <p class="text-slate-200 text-sm sm:text-base lg:text-lg max-w-4xl leading-relaxed">
                {hero_desc}
            </p>

            <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-5 gap-3 sm:gap-4 pt-4 text-left">
                <div class="bg-white/10 backdrop-blur rounded-2xl p-4 border border-white/15 space-y-1">
                    <div class="text-[11px] uppercase tracking-wider text-slate-300 font-bold">Total Auditado</div>
                    <div class="text-2xl sm:text-3xl font-bold brand-serif text-white">{total_topics} Temas</div>
                    <div class="text-[11px] text-[#EC9123] font-medium">Ciclo Oficial 2026</div>
                </div>
                <div class="bg-white/10 backdrop-blur rounded-2xl p-4 border border-white/15 space-y-1">
                    <div class="text-[11px] uppercase tracking-wider text-slate-300 font-bold">🟢 Adecuados</div>
                    <div class="text-2xl sm:text-3xl font-bold brand-serif text-emerald-400">{stats['adecuado']} Temas</div>
                    <div class="text-[11px] text-slate-200 font-medium">{pct_adecuado}% de Cobertura</div>
                </div>
                <div class="bg-white/10 backdrop-blur rounded-2xl p-4 border border-white/15 space-y-1">
                    <div class="text-[11px] uppercase tracking-wider text-slate-300 font-bold">🟡 Actualizar</div>
                    <div class="text-2xl sm:text-3xl font-bold brand-serif text-amber-400">{stats['revisar']} Temas</div>
                    <div class="text-[11px] text-slate-200 font-medium">{pct_revisar}% Modernización</div>
                </div>
                <div class="bg-white/10 backdrop-blur rounded-2xl p-4 border border-white/15 space-y-1">
                    <div class="text-[11px] uppercase tracking-wider text-slate-300 font-bold">🔴 Eliminar</div>
                    <div class="text-2xl sm:text-3xl font-bold brand-serif text-red-400">{stats['eliminar']} Temas</div>
                    <div class="text-[11px] text-slate-200 font-medium">{pct_eliminar}% Obsolescencia</div>
                </div>
                <div class="bg-white/10 backdrop-blur rounded-2xl p-4 border border-white/15 space-y-1 col-span-2 sm:col-span-1">
                    <div class="text-[11px] uppercase tracking-wider text-slate-300 font-bold">🟣 Innovación / IA</div>
                    <div class="text-2xl sm:text-3xl font-bold brand-serif text-purple-300">{stats['propuesto']} Temas</div>
                    <div class="text-[11px] text-slate-200 font-medium">{pct_propuesto}% Demanda 2026</div>
                </div>
            </div>

        </div>
    </section>

    <!-- CONTENIDO PRINCIPAL -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 space-y-14 flex-1">

        <!-- SECCIÓN 1: RESUMEN EJECUTIVO (PREVIO AL CONTENIDO) -->
        <section id="resumen" class="space-y-6 scroll-mt-28">
            <div class="bg-white rounded-3xl border border-slate-300 p-6 sm:p-8 shadow-sm space-y-6">
                
                <div class="border-b border-slate-200 pb-5">
                    <div class="flex items-center gap-2 text-xs font-bold text-[#EC9123] uppercase tracking-widest">
                        <i data-lucide="clipboard-check" class="w-4 h-4"></i> Diagnóstico y Dictamen Curricular 2026
                    </div>
                    <h2 class="text-2xl sm:text-3xl font-bold brand-serif text-[#22376D] mt-1">
                        1. Resumen Ejecutivo: Dictamen de Temas a Eliminar y Actualizar
                    </h2>
                    <p class="text-slate-600 text-xs sm:text-sm mt-1 max-w-4xl leading-relaxed">
                        Diagnóstico consolidado de los núcleos temáticos que requieren desincorporación 
                        por obsolescencia técnica o actualización frente a las exigencias contemporáneas del sector productivo.
                    </p>
                </div>

                <div class="grid sm:grid-cols-3 gap-4">
                    <div class="p-4 rounded-2xl bg-red-50 border border-red-200 space-y-1">
                        <div class="flex items-center justify-between text-red-900 font-bold text-xs">
                            <span class="flex items-center gap-1.5"><span class="text-base">🔴</span> Temas a Eliminar</span>
                            <span class="px-2 py-0.5 rounded-full bg-red-200 text-red-900">{stats['eliminar']} Núcleos</span>
                        </div>
                        <p class="text-xs text-slate-700 leading-relaxed mt-2">
                            Tecnologías en desuso comercial que restan períodos de taller práctico. Su eliminación libera carga horaria para competencias productivas.
                        </p>
                    </div>

                    <div class="p-4 rounded-2xl bg-amber-50 border border-amber-200 space-y-1">
                        <div class="flex items-center justify-between text-amber-900 font-bold text-xs">
                            <span class="flex items-center gap-1.5"><span class="text-base">🟡</span> Temas a Actualizar</span>
                            <span class="px-2 py-0.5 rounded-full bg-amber-200 text-amber-900">{stats['revisar']} Núcleos</span>
                        </div>
                        <p class="text-xs text-slate-700 leading-relaxed mt-2">
                            Contenidos vigentes que deben acotarse al nivel perito o modernizarse con herramientas y metodologías contemporáneas.
                        </p>
                    </div>

                    <div class="p-4 rounded-2xl bg-purple-50 border border-purple-200 space-y-1">
                        <div class="flex items-center justify-between text-purple-900 font-bold text-xs">
                            <span class="flex items-center gap-1.5"><span class="text-base">🟣</span> Nuevas Propuestas / IA</span>
                            <span class="px-2 py-0.5 rounded-full bg-purple-200 text-purple-900">{stats['propuesto']} Núcleos</span>
                        </div>
                        <p class="text-xs text-slate-700 leading-relaxed mt-2">
                            Nuevas competencias altamente requeridas en Guatemala no contempladas originalmente, incluyendo IA como asistente de taller.
                        </p>
                    </div>
                </div>

                <!-- Filtros del Resumen -->
                <div class="flex flex-wrap items-center justify-between gap-3 pt-2 border-t border-slate-100">
                    <div class="flex flex-wrap items-center gap-2">
                        <span class="text-xs font-bold text-slate-600 mr-1">Filtrar Dictamen:</span>
                        <button onclick="filterSummaryTable('all')" id="sum-btn-all" class="sum-filter-btn px-3 py-1.5 rounded-lg bg-[#22376D] text-white text-xs font-bold shadow-xs transition">
                            Todos ({len(summary_topics)})
                        </button>
                        <button onclick="filterSummaryTable('delete')" id="sum-btn-delete" class="sum-filter-btn px-3 py-1.5 rounded-lg bg-red-100 text-red-800 text-xs font-bold hover:bg-red-200 transition">
                            🔴 Eliminar ({stats['eliminar']})
                        </button>
                        <button onclick="filterSummaryTable('update')" id="sum-btn-update" class="sum-filter-btn px-3 py-1.5 rounded-lg bg-amber-100 text-amber-800 text-xs font-bold hover:bg-amber-200 transition">
                            🟡 Actualizar ({stats['revisar']})
                        </button>
                        <button onclick="filterSummaryTable('proposal')" id="sum-btn-proposal" class="sum-filter-btn px-3 py-1.5 rounded-lg bg-purple-100 text-purple-800 text-xs font-bold hover:bg-purple-200 transition">
                            🟣 Propuestas IA ({stats['propuesto']})
                        </button>
                    </div>

                    <div class="flex items-center gap-2">
                        <label for="summaryCareerFilter" class="text-xs font-bold text-slate-600">Carrera / Grado:</label>
                        <select id="summaryCareerFilter" onchange="filterSummaryTableByCareer(this.value)" class="text-xs font-semibold bg-white border border-slate-300 rounded-lg px-2.5 py-1.5 text-slate-700 focus:outline-none focus:border-[#22376D]">
                            <option value="all">Todas las Carreras</option>
                            {''.join(f'<option value="{c["id"]}">{c["name"]}</option>' for c in careers_meta)}
                        </select>
                    </div>
                </div>

                <!-- Tabla Detallada -->
                <div class="overflow-x-auto rounded-2xl border border-slate-200 shadow-2xs">
                    <table class="w-full text-left border-collapse bg-white">
                        <thead class="bg-slate-100/80 text-slate-700 text-[11px] uppercase tracking-wider font-bold border-b border-slate-200">
                            <tr>
                                <th class="p-4 w-44">Especialidad / Bimestre</th>
                                <th class="p-4">Tema Oficial Auditado</th>
                                <th class="p-4 w-36">Dictamen</th>
                                <th class="p-4">Justificación Técnica e Industrial</th>
                            </tr>
                        </thead>
                        <tbody id="summaryTableBody" class="divide-y divide-slate-100 text-xs">
                            {''.join(summary_rows_html)}
                        </tbody>
                    </table>
                </div>

            </div>
        </section>

        <!-- SECCIÓN 2: TEMARIOS POR BIMESTRE (TARJETAS) -->
        <section id="temarios" class="space-y-6 scroll-mt-28">
            
            <div class="bg-white rounded-3xl border border-slate-300 p-6 sm:p-8 shadow-sm space-y-6">
                
                <div class="flex flex-col md:flex-row md:items-end justify-between gap-4 border-b border-slate-200 pb-5">
                    <div>
                        <div class="flex items-center gap-2 text-xs font-bold text-[#EC9123] uppercase tracking-widest">
                            <i data-lucide="sliders-horizontal" class="w-4 h-4"></i> Dosificación y Catálogo Oficial 2026
                        </div>
                        <h2 class="text-2xl sm:text-3xl font-bold brand-serif text-[#22376D] mt-1">
                            2. Temarios Detallados por Especialidad y Bimestre
                        </h2>
                        <p class="text-slate-600 text-xs sm:text-sm mt-1 max-w-3xl leading-relaxed">
                            Organización modular en tarjetas bimestrales independientes. Cada núcleo temático contiene su 
                            descripción técnica, justificación industrial y señalización cromática institucional.
                        </p>
                    </div>

                    <div class="relative w-full md:w-72">
                        <i data-lucide="search" class="w-4 h-4 absolute left-3 top-1/2 -translate-y-1/2 text-slate-400"></i>
                        <input type="text" id="topicSearchInput" oninput="liveSearchTopics(this.value)" placeholder="Buscar tema o tecnología..." class="w-full pl-9 pr-3 py-2 text-xs rounded-xl border border-slate-300 focus:outline-none focus:border-[#22376D] focus:ring-1 focus:ring-[#22376D] bg-slate-50/50">
                    </div>
                </div>

                <!-- Nomenclatura Oficial (Apartado 3) -->
                <div class="space-y-2">
                    <span class="text-xs font-bold uppercase tracking-wider text-slate-500">Nomenclatura y Código Cromático Institucional:</span>
                    <div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-3 text-xs">
                        <div class="p-3 rounded-xl bg-red-50 border border-red-200 text-red-900">
                            <div class="font-bold flex items-center gap-1.5 mb-1 text-sm">
                                <span>🔴</span> <span>Eliminar / Descontinuar</span>
                            </div>
                            <p class="text-slate-600 text-[11px] leading-relaxed">
                                Tecnologías obsoletas que restan semanas de taller práctico. Se anulan para dar paso a destrezas demandadas.
                            </p>
                        </div>

                        <div class="p-3 rounded-xl bg-amber-50 border border-amber-200 text-amber-900">
                            <div class="font-bold flex items-center gap-1.5 mb-1 text-sm">
                                <span>🟡</span> <span>Actualizar / Modernizar</span>
                            </div>
                            <p class="text-slate-600 text-[11px] leading-relaxed">
                                Contenidos vigentes que requieren acotación o modernización con instrumental contemporáneo.
                            </p>
                        </div>

                        <div class="p-3 rounded-xl bg-emerald-50 border border-emerald-200 text-emerald-900">
                            <div class="font-bold flex items-center gap-1.5 mb-1 text-sm">
                                <span>🟢</span> <span>Adecuado / Mantener</span>
                            </div>
                            <p class="text-slate-600 text-[11px] leading-relaxed">
                                Fundamentos técnicos de alta demanda laboral acordes al perfil de egreso del técnico de nivel medio.
                            </p>
                        </div>

                        <div class="p-3 rounded-xl bg-purple-50 border border-purple-200 text-purple-900">
                            <div class="font-bold flex items-center gap-1.5 mb-1 text-sm">
                                <span>🟣</span> <span>Propuesta / Innovación</span>
                            </div>
                            <p class="text-slate-600 text-[11px] leading-relaxed">
                                Nuevas competencias prioritarias en la industria guatemalteca e integración de IA aplicada como coworker.
                            </p>
                        </div>
                    </div>
                </div>

                <!-- Tabs de Carreras y Filtro de Estados -->
                <div class="flex flex-wrap items-center justify-between gap-4 pt-3 border-t border-slate-100">
                    <div class="flex flex-wrap items-center gap-2">
                        {''.join(f'''
                        <button onclick="switchCareerTab('{c["id"]}')" id="tab-btn-{c["id"]}" class="career-tab-btn px-4 py-2 rounded-xl text-xs font-bold transition flex items-center gap-2 {'bg-[#22376D] text-white shadow-sm' if idx == 0 else 'bg-slate-100 text-slate-700 hover:bg-slate-200'}">
                            <i data-lucide="{c['icon']}" class="w-4 h-4"></i> {c['name']}
                        </button>
                        ''' for idx, c in enumerate(careers_meta))}
                    </div>

                    <div class="flex flex-wrap items-center gap-1.5 text-xs font-bold">
                        <button onclick="filterBimesterTopics('all')" id="topic-btn-all" class="topic-filter-btn px-3 py-1.5 rounded-lg bg-slate-800 text-white shadow-xs transition">Todos</button>
                        <button onclick="filterBimesterTopics('keep')" id="topic-btn-keep" class="topic-filter-btn px-3 py-1.5 rounded-lg bg-emerald-100 text-emerald-800 hover:bg-emerald-200 transition">🟢 Mantener</button>
                        <button onclick="filterBimesterTopics('update')" id="topic-btn-update" class="topic-filter-btn px-3 py-1.5 rounded-lg bg-amber-100 text-amber-800 hover:bg-amber-200 transition">🟡 Actualizar</button>
                        <button onclick="filterBimesterTopics('delete')" id="topic-btn-delete" class="topic-filter-btn px-3 py-1.5 rounded-lg bg-red-100 text-red-800 hover:bg-red-200 transition">🔴 Eliminar</button>
                        <button onclick="filterBimesterTopics('proposal')" id="topic-btn-proposal" class="topic-filter-btn px-3 py-1.5 rounded-lg bg-purple-100 text-purple-800 hover:bg-purple-200 transition">🟣 Propuestas</button>
                    </div>
                </div>

            </div>

            <div id="careerPanelsContainer">
                {''.join(career_tabs_content)}
            </div>

        </section>

        <!-- SECCIÓN 3: ARTICULACIÓN ETS -->
        <section id="articulacion" class="space-y-6 scroll-mt-28">
            <div class="bg-white rounded-3xl border border-slate-300 p-6 sm:p-8 shadow-sm space-y-6">
                
                <div class="border-b border-slate-200 pb-4">
                    <div class="flex items-center gap-2 text-xs font-bold text-[#EC9123] uppercase tracking-widest">
                        <i data-lucide="network" class="w-4 h-4"></i> Marco Institucional y Articulación Educativa
                    </div>
                    <h2 class="text-2xl sm:text-3xl font-bold brand-serif text-[#22376D] mt-1">
                        3. Articulación Formativa: Nivel Diversificado (CET) y Nivel Superior (ETS)
                    </h2>
                </div>

                <div class="grid md:grid-cols-2 gap-6">
                    <div class="bg-slate-50 p-5 rounded-2xl border border-slate-200 space-y-3">
                        <div class="flex items-center gap-2 text-[#22376D] font-bold text-sm">
                            <i data-lucide="graduation-cap" class="w-5 h-5 text-[#EC9123]"></i>
                            <span>Nivel Medio Diversificado (CET • DQR 4)</span>
                        </div>
                        <p class="text-xs text-slate-700 leading-relaxed">
                            Formación técnica operativa terminal. Prepara al perito para la ejecución práctica directa, montaje, cableado normado, parametrización de equipos, mantenimiento preventivo y correctivo, y soporte técnico ágil en empresas de Guatemala.
                        </p>
                        <div class="text-xs text-slate-600 bg-white p-3 rounded-xl border border-slate-200 leading-relaxed">
                            {ets_spec_notes}
                        </div>
                    </div>

                    <div class="bg-slate-50 p-5 rounded-2xl border border-slate-200 space-y-3">
                        <div class="flex items-center gap-2 text-[#22376D] font-bold text-sm">
                            <i data-lucide="sparkles" class="w-5 h-5 text-purple-600"></i>
                            <span>Inteligencia Artificial como Coworker y Rigor Evaluativo</span>
                        </div>
                        <p class="text-xs text-slate-700 leading-relaxed">
                            La Inteligencia Artificial se adopta como un copiloto productivo de taller y laboratorio. Ningún estudiante puede entregar código o diseños sin validación técnica propia.
                        </p>
                        <div class="text-xs text-slate-600 bg-white p-3 rounded-xl border border-slate-200 space-y-2">
                            <p><strong>• Principio de Trazabilidad:</strong> Todo prompt o consulta a modelos generativos debe ser documentado.</p>
                            <p><strong>• Defensa Verbal Obligatoria:</strong> El estudiante debe justificar verbalmente cada bloque de código o circuito presentado ante el docente.</p>
                            <p><strong>• Umbral Aprobatorio:</strong> Nota mínima de <strong>75 puntos sobre 100</strong> para la superación de cada módulo y curso técnico.</p>
                        </div>
                    </div>
                </div>

            </div>
        </section>

    </main>

    <!-- FOOTER INSTITUCIONAL -->
    <footer class="bg-[#152244] text-white border-t-4 border-[#EC9123] mt-16 py-10">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-6 text-center sm:text-left">
            <div class="flex flex-col sm:flex-row justify-between items-center gap-4 border-b border-slate-700 pb-6">
                <div class="flex items-center gap-3">
                    <img src="assets/fundacion_kinal_blanco.png" alt="Fundación Kinal" class="h-10 w-auto object-contain">
                    <div>
                        <div class="font-bold text-base tracking-wide brand-serif">Fundación Kinal</div>
                        <div class="text-xs text-slate-300">Centro Escolar Técnico (CET) • Escuela Técnica Superior (ETS)</div>
                    </div>
                </div>
                <div class="text-xs text-slate-300 text-center sm:text-right">
                    <div>Ciclo Académico Oficial 2026</div>
                    <div class="text-[#EC9123] font-semibold">«Aprender en el proceso de trabajo»</div>
                </div>
            </div>

            <div class="flex flex-col sm:flex-row justify-between items-center gap-2 text-xs text-slate-400">
                <p>© 2026 Fundación Kinal. Todos los derechos reservados. Documento de auditoría curricular técnica.</p>
                <p class="font-medium text-slate-300">Plataforma Educativa Microsoft Teams • LMS Moodle (Kinal.academy)</p>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', () => {{
            lucide.createIcons();
        }});

        let activeCareerId = '{careers_meta[0]["id"]}';
        let activeTopicFilter = 'all';
        let activeSummaryStatusFilter = 'all';
        let activeSummaryCareerFilter = 'all';

        function switchCareerTab(careerId) {{
            activeCareerId = careerId;
            
            document.querySelectorAll('.career-tab-btn').forEach(btn => {{
                btn.classList.remove('bg-[#22376D]', 'text-white', 'shadow-sm');
                btn.classList.add('bg-slate-100', 'text-slate-700');
            }});
            const activeBtn = document.getElementById('tab-btn-' + careerId);
            if (activeBtn) {{
                activeBtn.classList.remove('bg-slate-100', 'text-slate-700');
                activeBtn.classList.add('bg-[#22376D]', 'text-white', 'shadow-sm');
            }}

            document.querySelectorAll('.career-panel').forEach(panel => {{
                panel.style.display = 'none';
            }});
            const activePanel = document.getElementById('career-panel-' + careerId);
            if (activePanel) {{
                activePanel.style.display = 'block';
            }}

            applyTopicFilters();
        }}

        function filterBimesterTopics(status) {{
            activeTopicFilter = status;

            document.querySelectorAll('.topic-filter-btn').forEach(btn => {{
                btn.classList.remove('ring-2', 'ring-offset-1', 'ring-slate-900');
            }});
            const btn = document.getElementById('topic-btn-' + status);
            if (btn) {{
                btn.classList.add('ring-2', 'ring-offset-1', 'ring-slate-900');
            }}

            applyTopicFilters();
        }}

        function liveSearchTopics(query) {{
            applyTopicFilters();
        }}

        function applyTopicFilters() {{
            const searchVal = (document.getElementById('topicSearchInput')?.value || '').toLowerCase().trim();
            const panel = document.getElementById('career-panel-' + activeCareerId);
            if (!panel) return;

            const cards = panel.querySelectorAll('.bimester-card');
            cards.forEach(bCard => {{
                let visibleCount = 0;
                const topics = bCard.querySelectorAll('.bimester-topic-card');
                
                topics.forEach(t => {{
                    const tStatus = t.getAttribute('data-status');
                    const tTitle = t.getAttribute('data-title') || '';
                    
                    const matchStatus = (activeTopicFilter === 'all') || (tStatus === activeTopicFilter);
                    const matchSearch = (!searchVal) || tTitle.includes(searchVal);

                    if (matchStatus && matchSearch) {{
                        t.style.display = 'block';
                        visibleCount++;
                    }} else {{
                        t.style.display = 'none';
                    }}
                }});

                if (visibleCount === 0 && (activeTopicFilter !== 'all' || searchVal !== '')) {{
                    bCard.style.display = 'none';
                }} else {{
                    bCard.style.display = 'flex';
                }}
            }});
        }}

        function filterSummaryTable(status) {{
            activeSummaryStatusFilter = status;

            document.querySelectorAll('.sum-filter-btn').forEach(btn => {{
                btn.classList.remove('ring-2', 'ring-offset-1', 'ring-[#22376D]');
            }});
            const btn = document.getElementById('sum-btn-' + status);
            if (btn) {{
                btn.classList.add('ring-2', 'ring-offset-1', 'ring-[#22376D]');
            }}

            applySummaryTableFilters();
        }}

        function filterSummaryTableByCareer(careerId) {{
            activeSummaryCareerFilter = careerId;
            applySummaryTableFilters();
        }}

        function applySummaryTableFilters() {{
            const rows = document.querySelectorAll('.summary-table-row');
            rows.forEach(row => {{
                const rCareer = row.getAttribute('data-career');
                const rStatus = row.getAttribute('data-status');

                const matchCareer = (activeSummaryCareerFilter === 'all') || (rCareer === activeSummaryCareerFilter);
                const matchStatus = (activeSummaryStatusFilter === 'all') || (rStatus === activeSummaryStatusFilter);

                if (matchCareer && matchStatus) {{
                    row.style.display = '';
                }} else {{
                    row.style.display = 'none';
                }}
            }});
        }}
    </script>
</body>
</html>
"""
    return html_template


def generate_home_portal_html():
    """
    Genera el archivo index.html principal del repositorio electronica-cet.
    Provee la selección entre Electrónica CET e Informática CET y el resumen 'for dummies'
    de temas a eliminar, actualizar y novedades.
    """
    html_home = """<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Auditoría Curricular y Catálogo de Pensums CET 2026 | Fundación Kinal</title>
    
    <!-- Favicon Oficial Cuadrado de Fundación Kinal -->
    <link rel="icon" type="image/png" href="assets/escudo_kinal_cuadrado.png">
    
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Lucide Icons -->
    <script src="https://unpkg.com/lucide@latest"></script>
    
    <!-- Fuentes Web Oficiales (Times New Roman y Arial con fallbacks) -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800;900&family=Playfair+Display:ital,wght@0,600;0,700;0,800;0,900;1,600&display=swap" rel="stylesheet">

    <style>
        :root {
            --kinal-blue: #22376D;
            --kinal-blue-dark: #152244;
            --kinal-blue-deep: #0D162C;
            --kinal-blue-light: #2E4A91;
            --kinal-flame: #EC9123;
            --kinal-gold: #F5A623;
            --kinal-gray-8c: #888B8D;
            --kinal-bg-light: #F8FAFC;
            --kinal-border: #DDE2E5;
        }

        body {
            font-family: Arial, Helvetica, "Nimbus Sans L", "Liberation Sans", sans-serif;
            background-color: var(--kinal-bg-light);
            color: #1E293B;
            -webkit-font-smoothing: antialiased;
        }

        h1, h2, h3, h4, .font-kinal-title, .brand-serif {
            font-family: "Times New Roman", Times, "Playfair Display", Georgia, serif;
            letter-spacing: -0.01em;
        }

        .hero-kinal-gradient {
            background: linear-gradient(135deg, #0D162C 0%, #152244 45%, #22376D 100%);
        }

        @media (max-width: 767px) {
            *, *::before, *::after { box-sizing: border-box !important; }
            html, body { overflow-x: hidden !important; max-width: 100vw !important; }
            .no-scrollbar::-webkit-scrollbar { display: none !important; }
            .no-scrollbar { -ms-overflow-style: none !important; scrollbar-width: none !important; }
        }
    </style>
</head>
<body id="top" class="min-h-screen flex flex-col antialiased pt-[115px] sm:pt-[125px]">

    <!-- ========================================================= -->
    <!-- ENCABEZADO FIJO PERMANENTE                                -->
    <!-- ========================================================= -->
    <div class="fixed top-0 left-0 right-0 z-50 bg-white shadow-md border-b border-slate-200">
        
        <!-- BARRA INSTITUCIONAL SUPERIOR -->
        <div class="bg-[#152244] text-white text-xs border-b-2 border-[#EC9123]">
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-1.5 flex flex-wrap justify-between items-center gap-2">
                <div class="flex items-center gap-3">
                    <span class="inline-flex items-center gap-1.5 font-bold tracking-wider uppercase text-[#EC9123]">
                        <i data-lucide="award" class="w-3.5 h-3.5"></i> Fundación Kinal
                    </span>
                    <span class="text-slate-500">|</span>
                    <span class="text-slate-300 font-medium hidden sm:inline">
                        Centro Escolar Técnico (CET) • Ideario: <em>«El trabajo bien hecho»</em>
                    </span>
                </div>
                <div class="flex items-center gap-4 text-slate-300 font-medium">
                    <span class="flex items-center gap-1.5">
                        <i data-lucide="calendar" class="w-3.5 h-3.5 text-[#EC9123]"></i> Ciclo Académico 2026
                    </span>
                    <span class="text-slate-600">|</span>
                    <span class="text-emerald-400 font-bold flex items-center gap-1">
                        <i data-lucide="shield-check" class="w-3.5 h-3.5"></i> Aval UNIS-Kinal
                    </span>
                </div>
            </div>
        </div>

        <!-- HEADER CORPORATIVO (LOGO ETS & BOTONES TODOS BLANCOS) -->
        <header class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-2.5 sm:py-3 flex flex-wrap justify-between items-center gap-3">
            
            <div class="flex items-center">
                <a href="#top" class="flex items-center group">
                    <img src="assets/escuela_tecnica_superior.png" alt="Fundación Kinal - Escuela Técnica Superior" class="h-8 sm:h-10 w-auto object-contain transition group-hover:opacity-90">
                </a>
            </div>

            <!-- Navegación: Botones blancos, Inicio con solo icono al final a la derecha -->
            <nav class="flex items-center gap-2 sm:gap-3 text-xs overflow-x-auto no-scrollbar py-1 font-bold">
                <a href="#seleccion" class="px-3.5 py-2 rounded-lg bg-white hover:bg-slate-50 text-[#22376D] transition flex items-center gap-1.5 shadow-sm whitespace-nowrap border border-slate-200">
                    <i data-lucide="layers" class="w-4 h-4 text-[#EC9123]"></i> Carreras CET
                </a>
                <a href="#dummies" class="px-3.5 py-2 rounded-lg bg-white hover:bg-slate-50 text-[#22376D] transition flex items-center gap-1.5 shadow-sm whitespace-nowrap border border-slate-200">
                    <i data-lucide="help-circle" class="w-4 h-4 text-[#EC9123]"></i> Resumen Rápido
                </a>
                <a href="electronica.html" class="px-3.5 py-2 rounded-lg bg-white hover:bg-slate-50 text-[#22376D] transition flex items-center gap-1.5 shadow-sm whitespace-nowrap border border-slate-200">
                    <i data-lucide="cpu" class="w-4 h-4 text-[#22376D]"></i> Electrónica
                </a>
                <a href="informatica.html" class="px-3.5 py-2 rounded-lg bg-white hover:bg-slate-50 text-[#22376D] transition flex items-center gap-1.5 shadow-sm whitespace-nowrap border border-slate-200">
                    <i data-lucide="code-2" class="w-4 h-4 text-[#22376D]"></i> Informática
                </a>
                <a href="#top" class="px-3.5 py-2 rounded-lg bg-white hover:bg-slate-50 text-[#22376D] transition flex items-center justify-center shadow-sm whitespace-nowrap border border-slate-200 ml-auto" title="Inicio">
                    <i data-lucide="home" class="w-4 h-4 text-[#EC9123]"></i>
                </a>
            </nav>
        </header>

    </div>

    <!-- ========================================================= -->
    <!-- HERO PRINCIPAL                                            -->
    <!-- ========================================================= -->
    <section class="hero-kinal-gradient text-white py-14 sm:py-20 px-4 sm:px-6 lg:px-8 relative overflow-hidden">
        <div class="max-w-5xl mx-auto space-y-6 relative z-10 text-center sm:text-left">
            
            <div class="inline-flex items-center px-3.5 py-1.5 rounded-full bg-white/10 border border-white/20 text-[#EC9123] text-xs font-bold tracking-wide uppercase">
                <i data-lucide="shield" class="w-3.5 h-3.5 mr-1.5"></i>
                <span>Centro Escolar Técnico (CET) • Fundación Kinal • Ciclo 2026</span>
            </div>

            <h1 class="text-3xl sm:text-5xl lg:text-6xl font-bold tracking-tight leading-tight brand-serif text-white">
                Auditoría Curricular y Modernización de Pensums CET
            </h1>

            <p class="text-slate-200 text-sm sm:text-base lg:text-lg max-w-3xl leading-relaxed">
                Portal institucional de diagnóstico y modernización de los planes de estudio de nivel diversificado.
                Compara qué contenidos obsoletos se <strong>eliminan</strong>, qué temas se <strong>actualizan</strong> 
                y qué competencias de <strong>Inteligencia Artificial y demanda industrial</strong> se incorporan para 2026.
            </p>

            <!-- Métricas Clave Consolidadas -->
            <div class="grid grid-cols-2 md:grid-cols-4 gap-3 sm:gap-4 pt-4 text-left">
                <div class="bg-white/10 backdrop-blur rounded-2xl p-4 border border-white/15 space-y-1">
                    <div class="text-[11px] uppercase tracking-wider text-slate-300 font-bold">Carreras Auditadas</div>
                    <div class="text-3xl font-bold brand-serif text-white">2 Programas</div>
                    <div class="text-[11px] text-[#EC9123] font-medium">Electrónica e Informática</div>
                </div>
                <div class="bg-white/10 backdrop-blur rounded-2xl p-4 border border-white/15 space-y-1">
                    <div class="text-[11px] uppercase tracking-wider text-slate-300 font-bold">Núcleos Analizados</div>
                    <div class="text-3xl font-bold brand-serif text-white">204 Temas</div>
                    <div class="text-[11px] text-emerald-400 font-medium">151 Mantenidos (74%)</div>
                </div>
                <div class="bg-white/10 backdrop-blur rounded-2xl p-4 border border-white/15 space-y-1">
                    <div class="text-[11px] uppercase tracking-wider text-slate-300 font-bold">Temas Depurados</div>
                    <div class="text-3xl font-bold brand-serif text-red-300">10 Eliminados</div>
                    <div class="text-[11px] text-amber-300 font-medium">16 Actualizados</div>
                </div>
                <div class="bg-white/10 backdrop-blur rounded-2xl p-4 border border-white/15 space-y-1">
                    <div class="text-[11px] uppercase tracking-wider text-slate-300 font-bold">Innovación e IA</div>
                    <div class="text-3xl font-bold brand-serif text-purple-300">27 Propuestas</div>
                    <div class="text-[11px] text-purple-200 font-medium">Demanda Real Guatemala</div>
                </div>
            </div>

        </div>
    </section>

    <!-- ========================================================= -->
    <!-- CONTENIDO PRINCIPAL                                       -->
    <!-- ========================================================= -->
    <main class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 space-y-16 flex-1">

        <!-- ===================================================== -->
        <!-- SECCIÓN: SELECCIÓN DE PENSUMS (TARJETAS GRANDES)     -->
        <!-- ===================================================== -->
        <section id="seleccion" class="space-y-8 scroll-mt-28">
            
            <div class="text-center max-w-3xl mx-auto space-y-2">
                <span class="text-xs font-bold text-[#EC9123] tracking-widest uppercase">Elige la Especialidad Técnica</span>
                <h2 class="text-3xl sm:text-4xl font-bold brand-serif text-[#22376D]">
                    Plataformas de Auditoría Detallada
                </h2>
                <p class="text-slate-600 text-xs sm:text-sm">
                    Selecciona una carrera para consultar su desglose bimestral completo, dictamen temático por tema y justificaciones técnicas.
                </p>
            </div>

            <div class="grid md:grid-cols-2 gap-8">
                
                <!-- TARJETA 1: ELECTRÓNICA CET -->
                <div class="bg-white rounded-3xl border-2 border-slate-200 hover:border-[#22376D] transition-all duration-300 shadow-md hover:shadow-xl overflow-hidden flex flex-col justify-between group">
                    <div>
                        <!-- Cabecera de la tarjeta -->
                        <div class="bg-gradient-to-r from-[#152244] to-[#22376D] p-6 text-white space-y-2">
                            <div class="flex justify-between items-start">
                                <span class="px-3 py-1 rounded-full text-xs font-bold bg-[#EC9123] text-white uppercase tracking-wider">
                                    Nivel Diversificado
                                </span>
                                <div class="w-10 h-10 rounded-xl bg-white/10 flex items-center justify-center text-white">
                                    <i data-lucide="cpu" class="w-6 h-6"></i>
                                </div>
                            </div>
                            <h3 class="text-2xl font-bold brand-serif text-white">
                                Electrónica y Dispositivos Digitales
                            </h3>
                            <p class="text-xs text-slate-200">
                                5to Perito Troncal • 6to Electrónica Industrial • 6to Electrónica en Computación
                            </p>
                        </div>

                        <!-- Métricas y Síntesis -->
                        <div class="p-6 space-y-5">
                            
                            <!-- Badges de Conteo -->
                            <div class="grid grid-cols-4 gap-2 text-center text-xs">
                                <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200">
                                    <div class="font-bold text-slate-800 text-base">93</div>
                                    <div class="text-[10px] text-slate-500 uppercase font-semibold">Temas</div>
                                </div>
                                <div class="p-2.5 rounded-xl bg-emerald-50 border border-emerald-200 text-emerald-800">
                                    <div class="font-bold text-base">65</div>
                                    <div class="text-[10px] uppercase font-semibold">🟢 Adecuados</div>
                                </div>
                                <div class="p-2.5 rounded-xl bg-amber-50 border border-amber-200 text-amber-800">
                                    <div class="font-bold text-base">9</div>
                                    <div class="text-[10px] uppercase font-semibold">🟡 Actualizar</div>
                                </div>
                                <div class="p-2.5 rounded-xl bg-red-50 border border-red-200 text-red-800">
                                    <div class="font-bold text-base">5</div>
                                    <div class="text-[10px] uppercase font-semibold">🔴 Eliminar</div>
                                </div>
                            </div>

                            <!-- Resumen breve for dummies en la tarjeta -->
                            <div class="space-y-3 text-xs bg-slate-50 p-4 rounded-2xl border border-slate-200">
                                <strong class="text-slate-900 block text-xs uppercase tracking-wide text-[#EC9123]">
                                    Diagnóstico Rápido:
                                </strong>
                                <ul class="space-y-2 text-slate-700">
                                    <li class="flex items-start gap-2">
                                        <span class="text-red-600 font-bold text-sm shrink-0">🔴</span>
                                        <span><strong>Se elimina:</strong> Alambrado masivo en protoboard, chips PIC antiguos en Assembly, arrancadores por reóstatos y protocolos RIP/DTP viejos.</span>
                                    </li>
                                    <li class="flex items-start gap-2">
                                        <span class="text-amber-600 font-bold text-sm shrink-0">🟡</span>
                                        <span><strong>Se actualiza:</strong> Menos álgebra teórica abstracta y más práctica con osciloscopio, redes IPv4 con NAT y firewalls modernos.</span>
                                    </li>
                                    <li class="flex items-start gap-2">
                                        <span class="text-purple-600 font-bold text-sm shrink-0">🟣</span>
                                        <span><strong>Se incorpora:</strong> Soldadura profesional SMD, diseño PCB en KiCad, cámaras CCTV IP, MikroTik y seguridad LOTO.</span>
                                    </li>
                                </ul>
                            </div>

                        </div>
                    </div>

                    <!-- Botón de Acción -->
                    <div class="p-6 pt-0">
                        <a href="electronica.html" class="w-full py-3.5 px-6 rounded-xl bg-[#22376D] hover:bg-[#152244] text-white font-bold text-sm transition flex items-center justify-center gap-2 shadow-sm group-hover:shadow-md">
                            <span>Ver Pensum y Auditoría de Electrónica</span>
                            <i data-lucide="arrow-right" class="w-4 h-4 transition-transform group-hover:translate-x-1"></i>
                        </a>
                    </div>
                </div>

                <!-- TARJETA 2: INFORMÁTICA CET -->
                <div class="bg-white rounded-3xl border-2 border-slate-200 hover:border-[#22376D] transition-all duration-300 shadow-md hover:shadow-xl overflow-hidden flex flex-col justify-between group">
                    <div>
                        <!-- Cabecera de la tarjeta -->
                        <div class="bg-gradient-to-r from-[#152244] to-[#22376D] p-6 text-white space-y-2">
                            <div class="flex justify-between items-start">
                                <span class="px-3 py-1 rounded-full text-xs font-bold bg-[#EC9123] text-white uppercase tracking-wider">
                                    Nivel Diversificado
                                </span>
                                <div class="w-10 h-10 rounded-xl bg-white/10 flex items-center justify-center text-white">
                                    <i data-lucide="code-2" class="w-6 h-6"></i>
                                </div>
                            </div>
                            <h3 class="text-2xl font-bold brand-serif text-white">
                                Informática y Desarrollo de Software
                            </h3>
                            <p class="text-xs text-slate-200">
                                4to Perito Troncal • 5to Ingeniería de Software • 6to Full-Stack, Cloud & DevOps
                            </p>
                        </div>

                        <!-- Métricas y Síntesis -->
                        <div class="p-6 space-y-5">
                            
                            <!-- Badges de Conteo -->
                            <div class="grid grid-cols-4 gap-2 text-center text-xs">
                                <div class="p-2.5 rounded-xl bg-slate-50 border border-slate-200">
                                    <div class="font-bold text-slate-800 text-base">111</div>
                                    <div class="text-[10px] text-slate-500 uppercase font-semibold">Temas</div>
                                </div>
                                <div class="p-2.5 rounded-xl bg-emerald-50 border border-emerald-200 text-emerald-800">
                                    <div class="font-bold text-base">86</div>
                                    <div class="text-[10px] uppercase font-semibold">🟢 Adecuados</div>
                                </div>
                                <div class="p-2.5 rounded-xl bg-amber-50 border border-amber-200 text-amber-800">
                                    <div class="font-bold text-base">7</div>
                                    <div class="text-[10px] uppercase font-semibold">🟡 Actualizar</div>
                                </div>
                                <div class="p-2.5 rounded-xl bg-red-50 border border-red-200 text-red-800">
                                    <div class="font-bold text-base">5</div>
                                    <div class="text-[10px] uppercase font-semibold">🔴 Eliminar</div>
                                </div>
                            </div>

                            <!-- Resumen breve for dummies en la tarjeta -->
                            <div class="space-y-3 text-xs bg-slate-50 p-4 rounded-2xl border border-slate-200">
                                <strong class="text-slate-900 block text-xs uppercase tracking-wide text-[#EC9123]">
                                    Diagnóstico Rápido:
                                </strong>
                                <ul class="space-y-2 text-slate-700">
                                    <li class="flex items-start gap-2">
                                        <span class="text-red-600 font-bold text-sm shrink-0">🔴</span>
                                        <span><strong>Se elimina:</strong> Meses en PseInt de principiantes, guardar en archivos de texto .txt, interfaces Swing viejas y carpetas RUP en cascada.</span>
                                    </li>
                                    <li class="flex items-start gap-2">
                                        <span class="text-amber-600 font-bold text-sm shrink-0">🟡</span>
                                        <span><strong>Se actualiza:</strong> No saltar entre 5 tecnologías sin dominar ninguna, automatizar pruebas con Postman y dejar Kubernetes avanzado para la universidad.</span>
                                    </li>
                                    <li class="flex items-start gap-2">
                                        <span class="text-purple-600 font-bold text-sm shrink-0">🟣</span>
                                        <span><strong>Se incorpora:</strong> TypeScript, Git Flow con Pull Requests en equipo, higiene de ciberseguridad OWASP y copiloto de IA con defensa verbal.</span>
                                    </li>
                                </ul>
                            </div>

                        </div>
                    </div>

                    <!-- Botón de Acción -->
                    <div class="p-6 pt-0">
                        <a href="informatica.html" class="w-full py-3.5 px-6 rounded-xl bg-[#22376D] hover:bg-[#152244] text-white font-bold text-sm transition flex items-center justify-center gap-2 shadow-sm group-hover:shadow-md">
                            <span>Ver Pensum y Auditoría de Informática</span>
                            <i data-lucide="arrow-right" class="w-4 h-4 transition-transform group-hover:translate-x-1"></i>
                        </a>
                    </div>
                </div>

            </div>

        </section>

        <!-- ===================================================== -->
        <!-- SECCIÓN: RESUMEN COMPARATIVO 'FOR DUMMIES'           -->
        <!-- ===================================================== -->
        <section id="dummies" class="space-y-8 scroll-mt-28">
            
            <div class="bg-white rounded-3xl border border-slate-300 p-6 sm:p-10 shadow-sm space-y-8">
                
                <div class="border-b border-slate-200 pb-5">
                    <div class="flex items-center gap-2 text-xs font-bold text-[#EC9123] uppercase tracking-widest">
                        <i data-lucide="zap" class="w-4 h-4"></i> Guía Rápida y Directa
                    </div>
                    <h2 class="text-2xl sm:text-4xl font-bold brand-serif text-[#22376D] mt-1">
                        ¿Qué Cambia en Cada Pensum y Por Qué? (Explicado en Sencillo)
                    </h2>
                    <p class="text-slate-600 text-xs sm:text-sm mt-1 max-w-3xl leading-relaxed">
                        Una explicación concisa, directa y sin tecnicismos complejos para entender de inmediato 
                        el porqué de cada decisión tomada en la actualización de los programas formativos.
                    </p>
                </div>

                <div class="grid lg:grid-cols-2 gap-8">

                    <!-- COLUMNA ELECTRÓNICA -->
                    <div class="space-y-6 bg-slate-50/70 p-6 rounded-2xl border border-slate-200">
                        <div class="flex items-center gap-3 border-b border-slate-200 pb-3">
                            <div class="p-2 rounded-lg bg-blue-100 text-[#22376D]">
                                <i data-lucide="cpu" class="w-5 h-5"></i>
                            </div>
                            <div>
                                <h3 class="font-bold text-lg text-slate-900 brand-serif">Electrónica CET</h3>
                                <span class="text-xs text-slate-500">¿Qué quitamos, qué arreglamos y qué sumamos?</span>
                            </div>
                        </div>

                        <!-- 🔴 ELIMINAR -->
                        <div class="space-y-2">
                            <div class="flex items-center gap-2 text-xs font-bold text-red-700 uppercase">
                                <span class="text-base">🔴</span> <span>¿Qué eliminamos y por qué?</span>
                            </div>
                            <div class="space-y-2 text-xs text-slate-700">
                                <div class="bg-white p-3 rounded-xl border border-red-200/80 shadow-2xs space-y-1">
                                    <div class="font-bold text-slate-900">1. Cablear cientos de chips en protoboard:</div>
                                    <p class="text-slate-600">Se pasaban semanas buscando cables flojos en vez de aprender lógica. Hoy en la industria nadie arregla placas armando cables telefónicos en protoboard; se usan simuladores y tarjetas modulares.</p>
                                </div>
                                <div class="bg-white p-3 rounded-xl border border-red-200/80 shadow-2xs space-y-1">
                                    <div class="font-bold text-slate-900">2. Chips PIC antiguos programados en Ensamblador:</div>
                                    <p class="text-slate-600">Tecnología de hace 25 años que nadie contrata. Se enseña programación en lenguaje C/C++ en microcontroladores modernos que sí se usan en las empresas.</p>
                                </div>
                                <div class="bg-white p-3 rounded-xl border border-red-200/80 shadow-2xs space-y-1">
                                    <div class="font-bold text-slate-900">3. Arrancar motores con resistencias de alambre viejas:</div>
                                    <p class="text-slate-600">Piezas de museo que ya no existen en plantas industriales. En su lugar se aprende a calibrar variadores de frecuencia y arrancadores electrónicos.</p>
                                </div>
                                <div class="bg-white p-3 rounded-xl border border-red-200/80 shadow-2xs space-y-1">
                                    <div class="font-bold text-slate-900">4. Protocolos viejos de red (RIP y DTP):</div>
                                    <p class="text-slate-600">Lentos e inseguros. Se eliminan para que aprendan los protocolos actuales que pide Cisco y la industria.</p>
                                </div>
                            </div>
                        </div>

                        <!-- 🟡 ACTUALIZAR -->
                        <div class="space-y-2">
                            <div class="flex items-center gap-2 text-xs font-bold text-amber-800 uppercase">
                                <span class="text-base">🟡</span> <span>¿Qué actualizamos y por qué?</span>
                            </div>
                            <div class="space-y-2 text-xs text-slate-700">
                                <div class="bg-white p-3 rounded-xl border border-amber-200/80 shadow-2xs space-y-1">
                                    <div class="font-bold text-slate-900">1. Menos álgebra matemática y más práctica de taller:</div>
                                    <p class="text-slate-600">No llenar cuadernos enteros demostrando fórmulas lógicas a mano. En el trabajo el técnico usa software y equipo de medición (osciloscopio, multímetro).</p>
                                </div>
                                <div class="bg-white p-3 rounded-xl border border-amber-200/80 shadow-2xs space-y-1">
                                    <div class="font-bold text-slate-900">2. Redes IPv4 reales antes que enredarse con IPv6:</div>
                                    <p class="text-slate-600">El 95% de las empresas en Guatemala operan con IPv4. Se prioriza que sepan armar redes locales que funcionen bien.</p>
                                </div>
                                <div class="bg-white p-3 rounded-xl border border-amber-200/80 shadow-2xs space-y-1">
                                    <div class="font-bold text-slate-900">3. Firewalls modernos:</div>
                                    <p class="text-slate-600">Dejar los comandos de consolas viejas (Cisco ASA) e incluir interfaces web actuales como FortiGate o pfSense.</p>
                                </div>
                            </div>
                        </div>

                        <!-- 🟣 NOVEDADES -->
                        <div class="space-y-2">
                            <div class="flex items-center gap-2 text-xs font-bold text-purple-800 uppercase">
                                <span class="text-base">🟣</span> <span>¿Qué agregamos de nuevo?</span>
                            </div>
                            <div class="bg-white p-3.5 rounded-xl border border-purple-200/80 shadow-2xs text-xs text-slate-700 space-y-1">
                                <p>• <strong>Soldadura SMD profesional:</strong> Soldar componentes microscópicos en placas reales.</p>
                                <p>• <strong>Diseño de Circuitos en KiCad:</strong> Diseñar sus propias tarjetas de circuito impreso.</p>
                                <p>• <strong>CCTV IP y Cámaras de Seguridad:</strong> El empleo con mayor salida laboral inmediata en Guatemala.</p>
                                <p>• <strong>Routers MikroTik:</strong> Los equipos que usan casi todas las PyMEs y colegios del país.</p>
                            </div>
                        </div>

                    </div>

                    <!-- COLUMNA INFORMÁTICA -->
                    <div class="space-y-6 bg-slate-50/70 p-6 rounded-2xl border border-slate-200">
                        <div class="flex items-center gap-3 border-b border-slate-200 pb-3">
                            <div class="p-2 rounded-lg bg-blue-100 text-[#22376D]">
                                <i data-lucide="code-2" class="w-5 h-5"></i>
                            </div>
                            <div>
                                <h3 class="font-bold text-lg text-slate-900 brand-serif">Informática CET</h3>
                                <span class="text-xs text-slate-500">¿Qué quitamos, qué arreglamos y qué sumamos?</span>
                            </div>
                        </div>

                        <!-- 🔴 ELIMINAR -->
                        <div class="space-y-2">
                            <div class="flex items-center gap-2 text-xs font-bold text-red-700 uppercase">
                                <span class="text-base">🔴</span> <span>¿Qué eliminamos y por qué?</span>
                            </div>
                            <div class="space-y-2 text-xs text-slate-700">
                                <div class="bg-white p-3 rounded-xl border border-red-200/80 shadow-2xs space-y-1">
                                    <div class="font-bold text-slate-900">1. Pasar meses en PseInt de principiantes:</div>
                                    <p class="text-slate-600">PseInt es solo una ruedita de entrenamiento para aprender a pensar. Usarlo más de 2 semanas atrasa el aprendizaje del lenguaje real (Java).</p>
                                </div>
                                <div class="bg-white p-3 rounded-xl border border-red-200/80 shadow-2xs space-y-1">
                                    <div class="font-bold text-slate-900">2. Guardar datos en archivos planos (.txt):</div>
                                    <p class="text-slate-600">Si dos usuarios entran a la vez, se borra o corrompe la información. Desde el primer año se enseña a guardar en bases de datos relacionales bien hechas (SQL).</p>
                                </div>
                                <div class="bg-white p-3 rounded-xl border border-red-200/80 shadow-2xs space-y-1">
                                    <div class="font-bold text-slate-900">3. Ventanas grises viejas con Java Swing manual:</div>
                                    <p class="text-slate-600">Nadie en una empresa crea hoy programas con interfaces Swing de hace 20 años. Ese tiempo se usa para aprender desarrollo web (React) y APIs.</p>
                                </div>
                                <div class="bg-white p-3 rounded-xl border border-red-200/80 shadow-2xs space-y-1">
                                    <div class="font-bold text-slate-900">4. Manuales gigantescos de 80 páginas estilo RUP:</div>
                                    <p class="text-slate-600">En las empresas de tecnología nadie lee manuales gigantescos que quedan desactualizados el primer mes; se trabaja con metodologías ágiles (Scrum y GitHub).</p>
                                </div>
                            </div>
                        </div>

                        <!-- 🟡 ACTUALIZAR -->
                        <div class="space-y-2">
                            <div class="flex items-center gap-2 text-xs font-bold text-amber-800 uppercase">
                                <span class="text-base">🟡</span> <span>¿Qué actualizamos y por qué?</span>
                            </div>
                            <div class="space-y-2 text-xs text-slate-700">
                                <div class="bg-white p-3 rounded-xl border border-amber-200/80 shadow-2xs space-y-1">
                                    <div class="font-bold text-slate-900">1. No ver 5 lenguajes a la vez sin dominar ninguno:</div>
                                    <p class="text-slate-600">Menos dispersión. Es mucho mejor dominar con maestría un stack fuerte y demandado (Java + Spring Boot + React + PostgreSQL) que saber poquito de diez cosas.</p>
                                </div>
                                <div class="bg-white p-3 rounded-xl border border-amber-200/80 shadow-2xs space-y-1">
                                    <div class="font-bold text-slate-900">2. Automatizar pruebas en vez de probar a mano:</div>
                                    <p class="text-slate-600">Enseñar a crear pruebas automáticas con Postman para comprobar que el sistema no falla antes de entregarlo al cliente.</p>
                                </div>
                                <div class="bg-white p-3 rounded-xl border border-amber-200/80 shadow-2xs space-y-1">
                                    <div class="font-bold text-slate-900">3. Dejar los servidores gigantes para la universidad:</div>
                                    <p class="text-slate-600">La administración de clústeres gigantes con Kubernetes pertenece al Técnico Superior (ETS); en perito se aprende Docker práctico para que sus sistemas corran en cualquier máquina.</p>
                                </div>
                            </div>
                        </div>

                        <!-- 🟣 NOVEDADES -->
                        <div class="space-y-2">
                            <div class="flex items-center gap-2 text-xs font-bold text-purple-800 uppercase">
                                <span class="text-base">🟣</span> <span>¿Qué agregamos de nuevo?</span>
                            </div>
                            <div class="bg-white p-3.5 rounded-xl border border-purple-200/80 shadow-2xs text-xs text-slate-700 space-y-1">
                                <p>• <strong>TypeScript:</strong> El estándar mundial para escribir código JavaScript sin errores tontos.</p>
                                <p>• <strong>Git Flow y Pull Requests:</strong> Aprender a trabajar en equipo como en las empresas reales de software.</p>
                                <p>• <strong>Higiene de Ciberseguridad:</strong> Nunca dejar contraseñas quemadas en el código y evitar ataques comunes (OWASP).</p>
                                <p>• <strong>IA como Copiloto:</strong> Usar asistentes de código pero sabiendo defender y explicar verbalmente cada línea de código creada.</p>
                            </div>
                        </div>

                    </div>

                </div>

            </div>

        </section>

        <!-- ===================================================== -->
        <!-- SECCIÓN: DIRECTRICES INSTITUCIONALES                  -->
        <!-- ===================================================== -->
        <section class="space-y-6">
            <div class="bg-white rounded-3xl border border-slate-300 p-6 sm:p-8 shadow-sm space-y-6">
                
                <div class="border-b border-slate-200 pb-4">
                    <div class="flex items-center gap-2 text-xs font-bold text-[#EC9123] uppercase tracking-widest">
                        <i data-lucide="check-circle-2" class="w-4 h-4"></i> Calidad Formativa Kinal
                    </div>
                    <h2 class="text-2xl sm:text-3xl font-bold brand-serif text-[#22376D] mt-1">
                        Criterios Clave de la Formación Técnica en Kinal
                    </h2>
                </div>

                <div class="grid sm:grid-cols-3 gap-6 text-xs text-slate-700">
                    <div class="p-5 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
                        <div class="flex items-center gap-2 text-[#22376D] font-bold text-sm">
                            <i data-lucide="award" class="w-4 h-4 text-[#EC9123]"></i>
                            <span>Nota Mínima ≥ 75 Puntos</span>
                        </div>
                        <p class="leading-relaxed">
                            En Fundación Kinal la exigencia académica no se negocia. La aprobación de cualquier módulo o examen de suficiencia exige un mínimo de <strong>75 puntos sobre 100</strong>.
                        </p>
                    </div>

                    <div class="p-5 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
                        <div class="flex items-center gap-2 text-[#22376D] font-bold text-sm">
                            <i data-lucide="briefcase" class="w-4 h-4 text-[#EC9123]"></i>
                            <span>Sistema Dual en Alternancia</span>
                        </div>
                        <p class="leading-relaxed">
                            Aprender en el proceso de trabajo. Los conocimientos de taller se conectan directamente con los problemas reales que enfrentan las empresas de Guatemala.
                        </p>
                    </div>

                    <div class="p-5 rounded-2xl bg-slate-50 border border-slate-200 space-y-2">
                        <div class="flex items-center gap-2 text-[#22376D] font-bold text-sm">
                            <i data-lucide="sparkles" class="w-4 h-4 text-purple-600"></i>
                            <span>IA con Defensa Verbal</span>
                        </div>
                        <p class="leading-relaxed">
                            La Inteligencia Artificial es una herramienta de productividad, pero cada estudiante debe ser capaz de explicar y defender verbalmente cualquier solución entregada.
                        </p>
                    </div>
                </div>

            </div>
        </section>

    </main>

    <!-- FOOTER INSTITUCIONAL -->
    <footer class="bg-[#152244] text-white border-t-4 border-[#EC9123] mt-16 py-10">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-6 text-center sm:text-left">
            <div class="flex flex-col sm:flex-row justify-between items-center gap-4 border-b border-slate-700 pb-6">
                <div class="flex items-center gap-3">
                    <img src="assets/fundacion_kinal_blanco.png" alt="Fundación Kinal" class="h-10 w-auto object-contain">
                    <div>
                        <div class="font-bold text-base tracking-wide brand-serif">Fundación Kinal</div>
                        <div class="text-xs text-slate-300">Centro Escolar Técnico (CET) • Escuela Técnica Superior (ETS)</div>
                    </div>
                </div>
                <div class="text-xs text-slate-300 text-center sm:text-right">
                    <div>Ciclo Académico Oficial 2026</div>
                    <div class="text-[#EC9123] font-semibold">«Aprender en el proceso de trabajo»</div>
                </div>
            </div>

            <div class="flex flex-col sm:flex-row justify-between items-center gap-2 text-xs text-slate-400">
                <p>© 2026 Fundación Kinal. Todos los derechos reservados. Repositorio: <code>electronica-cet</code>.</p>
                <p class="font-medium text-slate-300">Plataforma Educativa Microsoft Teams • LMS Moodle (Kinal.academy)</p>
            </div>
        </div>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', () => {
            lucide.createIcons();
        });
    </script>
</body>
</html>
"""
    return html_home


def main():
    print("=== Reconstruyendo Repositorio 'electronica-cet' ===")

    # 1. Asegurar copia de datos JSON de informática dentro de electronica-cet
    inf_dst_json = os.path.join(REPO_DIR, "pensum_data_informatica.json")
    if os.path.exists(INFORMATICA_JSON):
        shutil.copy2(INFORMATICA_JSON, inf_dst_json)
        print(f"[OK] Copiado pensum_data_informatica.json en {REPO_DIR}")

    # 2. Generar electronica.html
    if os.path.exists(ELECTRONICA_JSON):
        with open(ELECTRONICA_JSON, 'r', encoding='utf-8') as f:
            data_elec = json.load(f)
        elec_html = generate_subportal_html(data_elec, 'electronica')
        elec_out = os.path.join(REPO_DIR, "electronica.html")
        with open(elec_out, 'w', encoding='utf-8') as f:
            f.write(elec_html)
        print(f"[OK] Generado: {elec_out} ({len(elec_html)} bytes)")

    # 3. Generar informatica.html
    if os.path.exists(INFORMATICA_JSON):
        with open(INFORMATICA_JSON, 'r', encoding='utf-8') as f:
            data_inf = json.load(f)
        inf_html = generate_subportal_html(data_inf, 'informatica')
        inf_out = os.path.join(REPO_DIR, "informatica.html")
        with open(inf_out, 'w', encoding='utf-8') as f:
            f.write(inf_html)
        print(f"[OK] Generado: {inf_out} ({len(inf_html)} bytes)")

    # 4. Generar index.html (HOME Principal)
    home_html = generate_home_portal_html()
    home_out = os.path.join(REPO_DIR, "index.html")
    with open(home_out, 'w', encoding='utf-8') as f:
        f.write(home_html)
    print(f"[OK] Generado HOME: {home_out} ({len(home_html)} bytes)")

    print("=== Proceso completado exitosamente ===")


if __name__ == '__main__':
    main()
