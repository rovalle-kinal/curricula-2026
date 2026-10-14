import json
import subprocess
import time

PRES_ID = "16Nf4DykVZb0lSkzm5N9OPaKhDWXMfRdZel5RFwf3O58"

# 1. Obtener diapositivas actuales
res = subprocess.run(["gslides", "readonly", "list-slides", PRES_ID, "--json"], capture_output=True, text=True, check=True)
slides = json.loads(res.stdout)
print(f"Total slides actuales: {len(slides)}")

# Eliminar elementos de la primera lámina 'p'
p_slide = slides[0]
del_p_ops = [{"op": "delete-element", "element": el["objectId"]} for el in p_slide.get("pageElements", [])]
if del_p_ops:
    with open("del_p_ops.json", "w") as f:
        json.dump(del_p_ops, f, indent=2)
    subprocess.run(["gslides", "mutate", "batch", PRES_ID, "-f", "del_p_ops.json"], check=True)
    print("Elementos de slide p eliminados.")

# Eliminar las demás diapositivas (slides 1 en adelante)
for s in slides[1:]:
    s_id = s["objectId"]
    print(f"Eliminando slide {s_id}...")
    subprocess.run(["gslides", "mutate", "delete-slide", PRES_ID, s_id], check=True)

print("Diapositivas antiguas eliminadas.")

# 2. Generar las 9 Diapositivas ULTRA-VISUALES con MÍNIMO TEXTO
visual_ops = [
    # =========================================================================
    # SLIDE 1: PORTADA
    # =========================================================================
    {"op": "set-background", "slide": "p", "color": "#0D162C"},
    {"op": "add-shape", "slide": "p", "shape_type": "RECTANGLE", "x": 0, "y": 0, "width": 720, "height": 8, "background_color": "#EC9123"},
    {"op": "add-textbox", "slide": "p", "text": "ESCUELA TÉCNICA SUPERIOR · KINAL", "x": 45, "y": 25, "width": 380, "height": 20, "font_size": 11, "bold": True, "color": "#EC9123", "font_family": "Arial"},
    {"op": "add-textbox", "slide": "p", "text": "El Copiloto\ndel Negocio", "x": 45, "y": 60, "width": 320, "height": 90, "font_size": 36, "bold": True, "color": "#FFFFFF", "font_family": "Arial"},
    {"op": "add-textbox", "slide": "p", "text": "Inteligencia Artificial para Pequeños Negocios y Toma de Decisiones", "x": 45, "y": 160, "width": 320, "height": 45, "font_size": 13, "italic": True, "color": "#CBD5E1", "font_family": "Arial"},
    {"op": "add-textbox", "slide": "p", "text": "⏱️ De 3 Horas a 7 Minutos\n📱 100% Desde tu Celular o Laptop\n🎯 Cero Códigos · Decisiones Reales", "x": 45, "y": 220, "width": 320, "height": 110, "font_size": 12, "bold": True, "color": "#FFFFFF", "font_family": "Arial", "background_color": "#152244", "line_spacing": 160},
    {"op": "add-textbox", "slide": "p", "text": "Fundación Kinal · Innovación y Productividad con Enfoque Humano | Lámina 1 de 9", "x": 45, "y": 365, "width": 630, "height": 20, "font_size": 9, "color": "#94A3B8", "font_family": "Arial"},
    {"op": "set-notes", "slide": "p", "text": "OBJETIVO DE LA LÁMINA: Conectar de inmediato, romper el hielo y prometer valor real sin discursos comerciales.\n\nGUION DE APERTURA (0:00 - 3:00):\n«Buenas noches a todos y bienvenidos a la Escuela Técnica Superior de Fundación Kinal. Quiero empezar haciéndoles una promesa muy clara: en esta sesión de 60 minutos NO venimos a venderles nada con discursos aburridos ni a llenarlos de teoría matemática. Hoy venimos a que ustedes mismos experimenten lo que significa resolver un problema que normalmente les quita tres horas en solo siete minutos».\n\n«La Inteligencia Artificial no vino a quitarle el trabajo a nadie; vino a quitarle a usted el dolor de cabeza de las tareas mecánicas para devolverle el tiempo de ser el director de su propio negocio».\n\nPREGUNTA AL CHAT: «Escríbanme en el chat: ¿cuál es esa tarea de su trabajo o negocio que más pereza les da hacer cada semana?»"},

    # =========================================================================
    # SLIDE 2: EL DIAGNÓSTICO (80% vs 20%)
    # =========================================================================
    {"op": "add-slide", "layout": "BLANK", "id": "SLIDE_2"},
    {"op": "set-background", "slide": "SLIDE_2", "color": "#0D162C"},
    {"op": "add-shape", "slide": "SLIDE_2", "shape_type": "RECTANGLE", "x": 0, "y": 0, "width": 720, "height": 8, "background_color": "#EC9123"},
    {"op": "add-textbox", "slide": "SLIDE_2", "text": "DIAGNÓSTICO DEL NEGOCIO", "x": 45, "y": 25, "width": 450, "height": 20, "font_size": 11, "bold": True, "color": "#EC9123", "font_family": "Arial"},
    {"op": "add-textbox", "slide": "SLIDE_2", "text": "¿En qué se va tu día a día?", "x": 45, "y": 48, "width": 630, "height": 40, "font_size": 28, "bold": True, "color": "#FFFFFF", "font_family": "Arial"},
    # Tarjeta 80%
    {"op": "add-textbox", "slide": "SLIDE_2", "text": "80%", "x": 45, "y": 95, "width": 305, "height": 70, "font_size": 52, "bold": True, "color": "#F87171", "font_family": "Arial", "background_color": "#2A121A", "alignment": "center"},
    {"op": "add-textbox", "slide": "SLIDE_2", "text": "APAGANDO FUEGOS\n\n🔥 Cotizaciones manuales a contrarreloj\n🔥 Reclamos de clientes en WhatsApp\n🔥 Mercadería estancada en estantería\n🔥 Cobros incómodos en libreta de fiado", "x": 45, "y": 165, "width": 305, "height": 165, "font_size": 11.5, "color": "#FECDD3", "font_family": "Arial", "background_color": "#2A121A", "line_spacing": 150},
    # Tarjeta 20%
    {"op": "add-textbox", "slide": "SLIDE_2", "text": "20%", "x": 370, "y": 95, "width": 305, "height": 70, "font_size": 52, "bold": True, "color": "#34D399", "font_family": "Arial", "background_color": "#0D281E", "alignment": "center"},
    {"op": "add-textbox", "slide": "SLIDE_2", "text": "CRECER Y LIDERAR\n\n🎯 Nuevas ofertas para vender más\n🎯 Proteger el margen de ganancia\n🎯 Innovar y dar servicio de calidad\n🎯 Paz mental y tiempo en familia", "x": 370, "y": 165, "width": 305, "height": 165, "font_size": 11.5, "color": "#A7F3D0", "font_family": "Arial", "background_color": "#0D281E", "line_spacing": 150},
    {"op": "add-textbox", "slide": "SLIDE_2", "text": "💡 La IA no viene a sustituirte; viene a devolverte ese 80% de tu tiempo.", "x": 45, "y": 340, "width": 630, "height": 22, "font_size": 10.5, "bold": True, "color": "#FFD166", "alignment": "center"},
    {"op": "add-textbox", "slide": "SLIDE_2", "text": "Fundación Kinal · Escuela Técnica Superior | Lámina 2 de 9", "x": 45, "y": 365, "width": 630, "height": 20, "font_size": 9, "color": "#94A3B8", "font_family": "Arial"},
    {"op": "set-notes", "slide": "SLIDE_2", "text": "OBJETIVO: Empatizar con el agotamiento del emprendedor. Mostrar que el problema no es falta de esfuerzo, sino exceso de tareas manuales repetitivas.\n\nGUION SUGERIDO:\n«¿A cuántos de ustedes les pasa que abren el negocio a las 7:00 AM pensando en cómo van a vender más, y cuando dan las 6:00 PM sienten que no avanzaron nada porque se pasaron el día apagando fuegos? Respondiendo reclamos, cuadrando notas a mano o peleando con números».\n\n«El problema no es que les falte esfuerzo. El problema es que están usando su mente brillante para hacer tareas de máquina. Hoy vamos a delegarle a la máquina lo repetitivo para que ustedes vuelvan a ser los estrategas».\n\nPAUSA: Dejar 3 segundos de silencio para que la pregunta resuene en la audiencia."},

    # =========================================================================
    # SLIDE 3: LOS DOS MITOS
    # =========================================================================
    {"op": "add-slide", "layout": "BLANK", "id": "SLIDE_3"},
    {"op": "set-background", "slide": "SLIDE_3", "color": "#0D162C"},
    {"op": "add-shape", "slide": "SLIDE_3", "shape_type": "RECTANGLE", "x": 0, "y": 0, "width": 720, "height": 8, "background_color": "#EC9123"},
    {"op": "add-textbox", "slide": "SLIDE_3", "text": "DESMITIFICACIÓN", "x": 45, "y": 25, "width": 450, "height": 20, "font_size": 11, "bold": True, "color": "#EC9123", "font_family": "Arial"},
    {"op": "add-textbox", "slide": "SLIDE_3", "text": "Dos Grandes Mitos de la IA", "x": 45, "y": 48, "width": 630, "height": 40, "font_size": 28, "bold": True, "color": "#FFFFFF", "font_family": "Arial"},
    # Mito 1
    {"op": "add-textbox", "slide": "SLIDE_3", "text": "❌ ¿Saber de Sistemas?\n\n✔ Tu idioma es la interfaz", "x": 45, "y": 105, "width": 305, "height": 80, "font_size": 16, "bold": True, "color": "#FFFFFF", "font_family": "Arial", "background_color": "#1A2238"},
    {"op": "add-textbox", "slide": "SLIDE_3", "text": "No necesitas programar ni una sola línea de código. La herramienta funciona 100% en el español que hablas todos los días.", "x": 45, "y": 185, "width": 305, "height": 130, "font_size": 12, "color": "#CBD5E1", "font_family": "Arial", "background_color": "#152244", "line_spacing": 140},
    # Mito 2
    {"op": "add-textbox", "slide": "SLIDE_3", "text": "❌ ¿Respuestas Tontas?\n\n✔ La orden define el resultado", "x": 370, "y": 105, "width": 305, "height": 80, "font_size": 16, "bold": True, "color": "#FFFFFF", "font_family": "Arial", "background_color": "#1A2238"},
    {"op": "add-textbox", "slide": "SLIDE_3", "text": "La IA no lee mentes. Una orden vaga da basura genérica; una instrucción estructurada da una consultoría de oro en segundos.", "x": 370, "y": 185, "width": 305, "height": 130, "font_size": 12, "color": "#CBD5E1", "font_family": "Arial", "background_color": "#152244", "line_spacing": 140},
    {"op": "add-textbox", "slide": "SLIDE_3", "text": "💡 La IA es el motor; el volante lo manejas tú con el Método Kinal.", "x": 45, "y": 330, "width": 630, "height": 26, "font_size": 11, "bold": True, "color": "#0D162C", "font_family": "Arial", "background_color": "#EC9123", "alignment": "center"},
    {"op": "add-textbox", "slide": "SLIDE_3", "text": "Fundación Kinal · Escuela Técnica Superior | Lámina 3 de 9", "x": 45, "y": 365, "width": 630, "height": 20, "font_size": 9, "color": "#94A3B8", "font_family": "Arial"},
    {"op": "set-notes", "slide": "SLIDE_3", "text": "OBJETIVO: Derribar el temor tecnológico y explicar por qué antes obtuvieron respuestas insípidas de ChatGPT.\n\nGUION SUGERIDO:\n«Muchos me dicen: 'Mire, yo ya entré a ChatGPT y le pedí que me hiciera una carta de venta, pero me escribió algo que parecía un robot de hace diez años'. Y tienen toda la razón. Si ustedes le dicen 'hazme una carta', la IA promedia lo que encuentra en internet y da una respuesta insípida».\n\n«La IA es como un practicante nuevo que llegó hoy a su negocio: si usted le dice 'ayúdame en la tienda', se va a quedar parado sin saber qué hacer. Pero si le da un rol, un contexto y reglas claras, le resuelve en segundos».\n\nINTERACCIÓN: «Pongan un 1 en el chat los que ya han probado la IA y sintieron que el resultado fue demasiado genérico»."},

    # =========================================================================
    # SLIDE 4: MÉTODO RC-TRF
    # =========================================================================
    {"op": "add-slide", "layout": "BLANK", "id": "SLIDE_4"},
    {"op": "set-background", "slide": "SLIDE_4", "color": "#0D162C"},
    {"op": "add-shape", "slide": "SLIDE_4", "shape_type": "RECTANGLE", "x": 0, "y": 0, "width": 720, "height": 8, "background_color": "#EC9123"},
    {"op": "add-textbox", "slide": "SLIDE_4", "text": "MÉTODO KINAL", "x": 45, "y": 25, "width": 450, "height": 20, "font_size": 11, "bold": True, "color": "#EC9123", "font_family": "Arial"},
    {"op": "add-textbox", "slide": "SLIDE_4", "text": "La Fórmula Maestra: RC-TRF", "x": 45, "y": 48, "width": 630, "height": 40, "font_size": 28, "bold": True, "color": "#FFFFFF", "font_family": "Arial"},
    # 5 Bloques
    {"op": "add-textbox", "slide": "SLIDE_4", "text": "R\nROL\n\n¿Quién es la IA?", "x": 45, "y": 105, "width": 115, "height": 135, "font_size": 11, "bold": True, "color": "#FFFFFF", "font_family": "Arial", "background_color": "#1E40AF", "alignment": "center"},
    {"op": "add-textbox", "slide": "SLIDE_4", "text": "C\nCONTEXTO\n\nTu situación real", "x": 170, "y": 105, "width": 115, "height": 135, "font_size": 11, "bold": True, "color": "#FFFFFF", "font_family": "Arial", "background_color": "#0284C7", "alignment": "center"},
    {"op": "add-textbox", "slide": "SLIDE_4", "text": "T\nTAREA\n\nLa acción exacta", "x": 295, "y": 105, "width": 115, "height": 135, "font_size": 11, "bold": True, "color": "#FFFFFF", "font_family": "Arial", "background_color": "#059669", "alignment": "center"},
    {"op": "add-textbox", "slide": "SLIDE_4", "text": "R\nRESTRICCIÓN\n\nLo que NO se hace", "x": 420, "y": 105, "width": 115, "height": 135, "font_size": 11, "bold": True, "color": "#FFFFFF", "font_family": "Arial", "background_color": "#D97706", "alignment": "center"},
    {"op": "add-textbox", "slide": "SLIDE_4", "text": "F\nFORMATO\n\nSalida estructurada", "x": 545, "y": 105, "width": 130, "height": 135, "font_size": 11, "bold": True, "color": "#FFFFFF", "font_family": "Arial", "background_color": "#7C3AED", "alignment": "center"},
    # Contraste visual
    {"op": "add-textbox", "slide": "SLIDE_4", "text": "🔴 Petición Novata: 'Redáctame un correo cobrando' ➔ Inútil y robótico\n🟢 Con Método RC-TRF: Matriz estratégica + 3 opciones + WhatsApp diplomático listo", "x": 45, "y": 255, "width": 630, "height": 65, "font_size": 11.5, "bold": True, "color": "#FFD166", "font_family": "Arial", "background_color": "#152244", "line_spacing": 150},
    {"op": "add-textbox", "slide": "SLIDE_4", "text": "Fundación Kinal · Escuela Técnica Superior | Lámina 4 de 9", "x": 45, "y": 365, "width": 630, "height": 20, "font_size": 9, "color": "#94A3B8", "font_family": "Arial"},
    {"op": "set-notes", "slide": "SLIDE_4", "text": "OBJETIVO: Presentar la base metodológica de Fundación Kinal de manera simple y memorable.\n\nGUION SUGERIDO:\n«En Fundación Kinal no enseñamos a 'chatear' con la máquina. Enseñamos una metodología profesional: el método RC-TRF: Rol, Contexto, Tarea, Restricción y Formato. Grábense estas 5 letras. Si ustedes le dan a la IA estas cinco piezas, el resultado deja de ser un texto genérico y se convierte en un trabajo de consultoría de alto nivel».\n\n«Y para demostrárselo, no me crean a mí: vamos a poner el cronómetro en 7 minutos y lo van a hacer ustedes mismos ahora mismo».\n\nCONSEJO: Pedir que anoten las siglas RC-TRF en su libreta o celular. Es la llave dorada del webinar."},

    # =========================================================================
    # SLIDE 5: RETO EN VIVO 1 (PYMES)
    # =========================================================================
    {"op": "add-slide", "layout": "BLANK", "id": "SLIDE_5"},
    {"op": "set-background", "slide": "SLIDE_5", "color": "#0D162C"},
    {"op": "add-shape", "slide": "SLIDE_5", "shape_type": "RECTANGLE", "x": 0, "y": 0, "width": 720, "height": 8, "background_color": "#EC9123"},
    {"op": "add-textbox", "slide": "SLIDE_5", "text": "ACTIVIDAD EN VIVO 1 (7 MINUTOS)", "x": 45, "y": 25, "width": 450, "height": 20, "font_size": 11, "bold": True, "color": "#EC9123", "font_family": "Arial"},
    {"op": "add-textbox", "slide": "SLIDE_5", "text": "El Dilema del Descuento", "x": 45, "y": 48, "width": 630, "height": 40, "font_size": 28, "bold": True, "color": "#FFFFFF", "font_family": "Arial"},
    {"op": "add-textbox", "slide": "SLIDE_5", "text": "⏱️ CRONÓMETRO: 07:00 MIN\n\nEL DILEMA:\nCliente clave exige 20% descuento o se va. Tus costos subieron 12%. No puedes perder dinero, pero tampoco al cliente.", "x": 370, "y": 95, "width": 305, "height": 115, "font_size": 11, "bold": True, "color": "#FFFFFF", "font_family": "Arial", "background_color": "#1A2238", "line_spacing": 140},
    {"op": "add-textbox", "slide": "SLIDE_5", "text": "TU RETO EN LA SALA:\n1. Abre Gemini o ChatGPT en tu celular\n2. Pega el prompt maestro del chat de Teams\n3. Dale ENTER y mira la solución", "x": 370, "y": 220, "width": 305, "height": 95, "font_size": 11, "color": "#A7F3D0", "font_family": "Arial", "background_color": "#0D281E", "line_spacing": 140},
    {"op": "add-textbox", "slide": "SLIDE_5", "text": "💡 Regla de Oro: Nunca regales dinero en efectivo; ofrece valor estratégico.", "x": 45, "y": 335, "width": 630, "height": 24, "font_size": 10.5, "bold": True, "color": "#FFD166", "alignment": "center"},
    {"op": "add-textbox", "slide": "SLIDE_5", "text": "Fundación Kinal · Escuela Técnica Superior | Lámina 5 de 9", "x": 45, "y": 365, "width": 630, "height": 20, "font_size": 9, "color": "#94A3B8", "font_family": "Arial"},
    {"op": "set-notes", "slide": "SLIDE_5", "text": "OBJETIVO: Que el 100% de la sala copie el prompt y vea la matriz y el WhatsApp en su propia pantalla.\n\nGUION DE FACILITACIÓN:\n«El enlace y el texto acaban de ser pegados en el chat de Microsoft Teams. Les doy 3 minutos para que abran ChatGPT o Google Gemini en su teléfono o computadora, peguen el texto y le den ENTER. No tienen que cambiar nada por ahora; solo ejecútenlo y vean lo que ocurre».\n\n«Fíjense en la magia: en vez de un correo sumiso pidiendo disculpas o regalando dinero, la IA les desglosa tres escenarios inteligentes: compensar con garantía extendida, ofrecer una bonificación en servicio futuro de bajo costo y una respuesta comercial que protege su dinero y mantiene la dignidad de su negocio».\n\nINTERACCIÓN: «Escriban LISTO en el chat los que ya vieron la tabla y el mensaje en su pantalla». Leer nombres en voz alta."},

    # =========================================================================
    # SLIDE 6: EL CASO DEL TENDERO
    # =========================================================================
    {"op": "add-slide", "layout": "BLANK", "id": "SLIDE_6"},
    {"op": "set-background", "slide": "SLIDE_6", "color": "#0D162C"},
    {"op": "add-shape", "slide": "SLIDE_6", "shape_type": "RECTANGLE", "x": 0, "y": 0, "width": 720, "height": 8, "background_color": "#EC9123"},
    {"op": "add-textbox", "slide": "SLIDE_6", "text": "ACTIVIDAD EN VIVO 2 (ECONOMÍA POPULAR)", "x": 45, "y": 25, "width": 450, "height": 20, "font_size": 11, "bold": True, "color": "#EC9123", "font_family": "Arial"},
    {"op": "add-textbox", "slide": "SLIDE_6", "text": "El Caso del Tendero: Mercadería a Caja", "x": 45, "y": 48, "width": 630, "height": 40, "font_size": 28, "bold": True, "color": "#FFFFFF", "font_family": "Arial"},
    {"op": "add-textbox", "slide": "SLIDE_6", "text": "🛒 EL RETO DE DON CARLOS:\n• 15 jugos y 20 galletas a 4 días de vencer\n• Mañana llega el camión proveedor\n• Libreta de fiado con cobros pendientes", "x": 370, "y": 95, "width": 305, "height": 105, "font_size": 11, "bold": True, "color": "#FFFFFF", "font_family": "Arial", "background_color": "#1A2238", "line_spacing": 140},
    {"op": "add-textbox", "slide": "SLIDE_6", "text": "LA SOLUCIÓN EN 3 MINUTOS:\n🏷️ Combo Refacción Vecinal (Q6.50)\n📝 Cartel de vitrina con marcador\n💬 Mensaje cálido de WhatsApp de barrio\n\n✔ Q0 Pérdidas · Efectivo en caja hoy", "x": 370, "y": 210, "width": 305, "height": 115, "font_size": 11, "color": "#D1FAE5", "font_family": "Arial", "background_color": "#064E3B", "line_spacing": 140},
    {"op": "add-textbox", "slide": "SLIDE_6", "text": "💡 La IA sirve para el negocio familiar de mostrador, no solo para grandes empresas.", "x": 45, "y": 335, "width": 630, "height": 24, "font_size": 10.5, "bold": True, "color": "#FFD166", "alignment": "center"},
    {"op": "add-textbox", "slide": "SLIDE_6", "text": "Fundación Kinal · Escuela Técnica Superior | Lámina 6 de 9", "x": 45, "y": 365, "width": 630, "height": 20, "font_size": 9, "color": "#94A3B8", "font_family": "Arial"},
    {"op": "set-notes", "slide": "SLIDE_6", "text": "OBJETIVO: Conectar con el comercio local y los pequeños emprendimientos cotidianos.\n\nGUION SUGERIDO:\n«Muchos piensan: 'Ah, eso sirve para empresas con gerentes en corbata'. ¡No! Piensen en Don Carlos, el tendero del barrio. Tiene 15 jugos y 20 galletas a punto de vencer en 4 días. Si los deja ahí, se van a la basura y pierde su dinero. O tiene a Doña Carmen que le debe en la libreta de fiado desde hace un mes y le da pena cobrarle».\n\n«En 7 minutos con su teléfono, la IA le calculó el combo de recuperación, le armó el texto para el cartel y le redactó un mensajito para el grupo de WhatsApp de la colonia tan amable que la gente llega agradecida a comprarle. Eso es usar la tecnología al servicio de la persona y de la economía familiar».\n\nPREGUNTA AL CHAT: «¿Quién de aquí conoce a alguien con una tienda, una panadería o un negocio familiar al que esto le salvaría el día?»"},

    # =========================================================================
    # SLIDE 7: EL ABISMO ÉTICO (EL ICEBERG)
    # =========================================================================
    {"op": "add-slide", "layout": "BLANK", "id": "SLIDE_7"},
    {"op": "set-background", "slide": "SLIDE_7", "color": "#0D162C"},
    {"op": "add-shape", "slide": "SLIDE_7", "shape_type": "RECTANGLE", "x": 0, "y": 0, "width": 720, "height": 8, "background_color": "#EC9123"},
    {"op": "add-textbox", "slide": "SLIDE_7", "text": "CRITERIO ÉTICO & RIGOR INSTITUCIONAL", "x": 45, "y": 25, "width": 450, "height": 20, "font_size": 11, "bold": True, "color": "#EC9123", "font_family": "Arial"},
    {"op": "add-textbox", "slide": "SLIDE_7", "text": "El Abismo: ¿Por qué no bastan videos de YouTube?", "x": 45, "y": 48, "width": 630, "height": 40, "font_size": 26, "bold": True, "color": "#FFFFFF", "font_family": "Arial"},
    {"op": "add-textbox", "slide": "SLIDE_7", "text": "⚠️ EL RIESGO DE USAR IA SIN MÉTODO:\n\n• Alucinaciones: Datos falsos que parecen reales\n• Fuga de Privacidad: Subir DPIs o datos de clientes\n• Textos Robóticos: Destruyen la confianza del cliente", "x": 370, "y": 95, "width": 305, "height": 110, "font_size": 11, "color": "#FECDD3", "font_family": "Arial", "background_color": "#450A0A", "line_spacing": 140},
    {"op": "add-textbox", "slide": "SLIDE_7", "text": "🛡️ EL SELLO DE FUNDACIÓN KINAL:\n\n• El 'Trabajo Bien Hecho': Excelencia y verdad\n• Director Crítico: Auditar antes de enviar\n• La persona siempre por encima de la máquina", "x": 370, "y": 215, "width": 305, "height": 110, "font_size": 11, "color": "#DBEAFE", "font_family": "Arial", "background_color": "#1E3A8A", "line_spacing": 140},
    {"op": "add-textbox", "slide": "SLIDE_7", "text": "💡 La tecnología es una herramienta; el criterio y la reputación son tuyos.", "x": 45, "y": 335, "width": 630, "height": 24, "font_size": 10.5, "bold": True, "color": "#FFD166", "alignment": "center"},
    {"op": "add-textbox", "slide": "SLIDE_7", "text": "Fundación Kinal · Escuela Técnica Superior | Lámina 7 de 9", "x": 45, "y": 365, "width": 630, "height": 20, "font_size": 9, "color": "#94A3B8", "font_family": "Arial"},
    {"op": "set-notes", "slide": "SLIDE_7", "text": "OBJETIVO: Sembrar la necesidad de una formación académica formal y estructurada sin sonar comercial.\n\nGUION CLAVE:\n«Lo que vieron hoy es emocionante, pero como formador de Fundación Kinal tengo el deber de ser muy honesto con ustedes: una herramienta tan potente en manos de alguien sin método es peligrosa. La IA a veces 'alucina': inventa datos, leyes o precios con total seguridad. En Kinal nos mueve el principio del 'Trabajo Bien Hecho': la excelencia no es sacar 50 páginas de texto en un minuto; es tener el ojo crítico para auditarlo, asegurar la verdad y proteger la privacidad de sus clientes. En Kinal ustedes aprenden a ser los directores de la herramienta, nunca sus esclavos»."},

    # =========================================================================
    # SLIDE 8: EL PROGRAMA OFICIAL
    # =========================================================================
    {"op": "add-slide", "layout": "BLANK", "id": "SLIDE_8"},
    {"op": "set-background", "slide": "SLIDE_8", "color": "#0D162C"},
    {"op": "add-shape", "slide": "SLIDE_8", "shape_type": "RECTANGLE", "x": 0, "y": 0, "width": 720, "height": 8, "background_color": "#EC9123"},
    {"op": "add-textbox", "slide": "SLIDE_8", "text": "PROGRAMA OFICIAL KINAL ETS", "x": 45, "y": 25, "width": 450, "height": 20, "font_size": 11, "bold": True, "color": "#EC9123", "font_family": "Arial"},
    {"op": "add-textbox", "slide": "SLIDE_8", "text": "Inteligencia Artificial Aplicada y Productividad Ética", "x": 45, "y": 48, "width": 630, "height": 40, "font_size": 24, "bold": True, "color": "#FFFFFF", "font_family": "Arial"},
    # 4 Módulos
    {"op": "add-textbox", "slide": "SLIDE_8", "text": "MÓDULO 1\nMultimodelo\n\nGemini, ChatGPT y Copilot en paralelo sin costo", "x": 45, "y": 105, "width": 145, "height": 130, "font_size": 10, "color": "#FFFFFF", "font_family": "Arial", "background_color": "#1E3A8A", "alignment": "center"},
    {"op": "add-textbox", "slide": "SLIDE_8", "text": "MÓDULO 2\nIngeniería Prompts\n\nMétodo RC-TRF y Catálogo Personal", "x": 200, "y": 105, "width": 145, "height": 130, "font_size": 10, "color": "#FFFFFF", "font_family": "Arial", "background_color": "#0E7490", "alignment": "center"},
    {"op": "add-textbox", "slide": "SLIDE_8", "text": "MÓDULO 3\nCasos Reales\n\nPDFs a Excel, minutas y correspondencia", "x": 355, "y": 105, "width": 145, "height": 130, "font_size": 10, "color": "#FFFFFF", "font_family": "Arial", "background_color": "#047857", "alignment": "center"},
    {"op": "add-textbox", "slide": "SLIDE_8", "text": "MÓDULO 4\nTu Asistente\n\nProyecto Integrador evaluado con rúbrica", "x": 510, "y": 105, "width": 165, "height": 130, "font_size": 10, "color": "#FFFFFF", "font_family": "Arial", "background_color": "#6D28D9", "alignment": "center"},
    # 3 Sellos
    {"op": "add-textbox", "slide": "SLIDE_8", "text": "🌙 8 Sesiones Nocturnas (16h)\nMar y Jue de 19:00 a 21:00", "x": 45, "y": 250, "width": 200, "height": 70, "font_size": 11, "bold": True, "color": "#FFFFFF", "font_family": "Arial", "background_color": "#152244", "alignment": "center"},
    {"op": "add-textbox", "slide": "SLIDE_8", "text": "💻 Microsoft Teams\n+ Kinal.academy (Moodle)", "x": 260, "y": 250, "width": 200, "height": 70, "font_size": 11, "bold": True, "color": "#FFFFFF", "font_family": "Arial", "background_color": "#152244", "alignment": "center"},
    {"op": "add-textbox", "slide": "SLIDE_8", "text": "🎓 Nota Mínima: 75/100\nCertificación Oficial Kinal", "x": 475, "y": 250, "width": 200, "height": 70, "font_size": 11, "bold": True, "color": "#A7F3D0", "font_family": "Arial", "background_color": "#0D281E", "alignment": "center"},
    {"op": "add-textbox", "slide": "SLIDE_8", "text": "Fundación Kinal · Escuela Técnica Superior | Lámina 8 de 9", "x": 45, "y": 365, "width": 630, "height": 20, "font_size": 9, "color": "#94A3B8", "font_family": "Arial"},
    {"op": "set-notes", "slide": "SLIDE_8", "text": "OBJETIVO: Presentar el programa formal como una solución integral, estructurada, accesible y de prestigio institucional.\n\nGUION SUGERIDO:\n«Por eso en la Escuela Técnica Superior de Kinal abrimos este programa de 16 horas formativas en 4 semanas. Son dos noches por semana, de 7:00 a 9:00 de la noche por Microsoft Teams, diseñado para gente trabajadora que no tiene tiempo que perder».\n\n«No es un curso para sacar un diploma de asistencia: la nota mínima para aprobar es de 75 puntos sobre 100 y ustedes se gradúan defendiendo en vivo un Asistente de Inteligencia Artificial construido a la medida de su propio trabajo o negocio».\n\nDETALLE: Destacar que las clases quedan grabadas en Kinal.academy pero la magia está en la práctica en vivo con el profesor."},

    # =========================================================================
    # SLIDE 9: CIERRE Y ACCIÓN
    # =========================================================================
    {"op": "add-slide", "layout": "BLANK", "id": "SLIDE_9"},
    {"op": "set-background", "slide": "SLIDE_9", "color": "#0D162C"},
    {"op": "add-shape", "slide": "SLIDE_9", "shape_type": "RECTANGLE", "x": 0, "y": 0, "width": 720, "height": 8, "background_color": "#EC9123"},
    {"op": "add-textbox", "slide": "SLIDE_9", "text": "TU DECISIÓN DE HOY", "x": 45, "y": 25, "width": 450, "height": 20, "font_size": 11, "bold": True, "color": "#EC9123", "font_family": "Arial"},
    {"op": "add-textbox", "slide": "SLIDE_9", "text": "Tu Siguiente Decisión Estratégica", "x": 45, "y": 48, "width": 630, "height": 40, "font_size": 28, "bold": True, "color": "#FFFFFF", "font_family": "Arial"},
    # Izquierda
    {"op": "add-textbox", "slide": "SLIDE_9", "text": "Invierte 16 Horas\nAhorra 10h Semanales\n\n• Acompañamiento docente en vivo\n• Proyecto aplicado a tu negocio real\n• Respaldo de Fundación Kinal", "x": 45, "y": 105, "width": 320, "height": 210, "font_size": 12, "color": "#FFFFFF", "font_family": "Arial", "background_color": "#1A2238", "line_spacing": 150},
    # Derecha
    {"op": "add-textbox", "slide": "SLIDE_9", "text": "📲 RESERVA TU LUGAR\n\n1. Entra a:\nkinal.academy\n\n2. Haz clic en el enlace del chat\n\n🎁 Incluye: Plantilla con 50 Prompts Maestros de Negocio", "x": 380, "y": 105, "width": 295, "height": 210, "font_size": 12, "bold": True, "color": "#0D162C", "font_family": "Arial", "background_color": "#EC9123", "alignment": "center", "line_spacing": 140},
    {"op": "add-textbox", "slide": "SLIDE_9", "text": "Fundación Kinal · Escuela Técnica Superior | Lámina 9 de 9", "x": 45, "y": 365, "width": 630, "height": 20, "font_size": 9, "color": "#94A3B8", "font_family": "Arial"},
    {"op": "set-notes", "slide": "SLIDE_9", "text": "OBJETIVO: Cierre orgánico, de servicio y sin presión agresiva. Invitar a tomar la decisión de superación personal y profesional con el respaldo de Kinal.\n\nGUION FINAL (CIERRE):\n«Para terminar, les dejo esta reflexión: en este momento tienen dos opciones. La primera es cerrar el webinar, guardar el prompt y seguir haciendo las cosas igual el lunes por la mañana. La segunda es invertir 16 horas de su vida durante las próximas cuatro semanas para adquirir una habilidad que multiplicará su productividad por los próximos diez años».\n\n«El cupo es reducido porque no es una conferencia pasiva: es un taller de acompañamiento donde ningún estudiante se queda atrás. En el chat y en pantalla tienen el enlace directo para asegurar su lugar. Será un verdadero honor tenerlos como alumnos en las aulas virtuales de Fundación Kinal. ¡Muchas gracias y abrimos micrófono para preguntas!»\n\nCONSEJO FINAL: Quedarse en la sala respondiendo dudas específicas de negocio de 3 a 5 participantes. Quienes se quedan al final son las inscripciones más seguras."}
]

with open("visual_ops.json", "w") as f:
    json.dump(visual_ops, f, indent=2)

print("Ejecutando creación de diapositivas visuales...")
res_batch = subprocess.run(["gslides", "mutate", "batch", PRES_ID, "-f", "visual_ops.json", "--json"], capture_output=True, text=True, check=True)
data_batch = json.loads(res_batch.stdout)
resolved = data_batch["resolved_ids"]
print("Resolved IDs:", resolved)

# 3. Insertar las Imágenes
print("Insertando imágenes generadas y logotipos...")

# Slide 1: Logo ETS y Reloj
subprocess.run(["gslides", "mutate", "insert-image-from-file", PRES_ID, "--slide", "p", "--file", "assets/escuela_tecnica_superior.png", "--x", "45", "--y", "18", "--width", "130", "--height", "45"], check=True)
subprocess.run(["gslides", "mutate", "insert-image-from-file", PRES_ID, "--slide", "p", "--file", "assets/tiempo_productividad.jpg", "--x", "380", "--y", "85", "--width", "295", "--height", "255"], check=True)

# Slide 5: Imagen Negociación
subprocess.run(["gslides", "mutate", "insert-image-from-file", PRES_ID, "--slide", resolved["SLIDE_5"], "--file", "assets/negociacion_estrategica.jpg", "--x", "45", "--y", "95", "--width", "305", "--height", "225"], check=True)

# Slide 6: Imagen Tendero
subprocess.run(["gslides", "mutate", "insert-image-from-file", PRES_ID, "--slide", resolved["SLIDE_6"], "--file", "assets/tendero_tienda_barrio.jpg", "--x", "45", "--y", "95", "--width", "305", "--height", "225"], check=True)

# Slide 7: Imagen Iceberg
subprocess.run(["gslides", "mutate", "insert-image-from-file", PRES_ID, "--slide", resolved["SLIDE_7"], "--file", "assets/iceberg_etica_ia.jpg", "--x", "45", "--y", "95", "--width", "305", "--height", "225"], check=True)

print("¡Todas las imágenes insertadas con éxito!")
