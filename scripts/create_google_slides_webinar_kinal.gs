/**
 * GOOGLE APPS SCRIPT: Generador Automático de Presentación Google Slides
 * Institución: Fundación Kinal - Escuela Técnica Superior (ETS)
 * Título: El Copiloto del Negocio: Inteligencia Artificial Aplicada
 * 
 * INSTRUCCIONES:
 * 1. Ve a https://script.google.com o en Google Drive crea un "Google Apps Script".
 * 2. Pega este código completo en el editor y haz clic en "Ejecutar" (Run).
 * 3. Acepta los permisos de Google Drive / Google Slides.
 * 4. El script creará la presentación automáticamente en tu Google Drive y te imprimirá el enlace en los registros (Logs).
 */

function crearPresentacionWebinarKinal() {
  const nombrePresentacion = "Webinar Kinal ETS - El Copiloto del Negocio con IA";
  const deck = SlidesApp.create(nombrePresentacion);
  
  // Colores Oficiales Fundación Kinal y Escuela Técnica Superior
  const COLOR_NAVY = "#0D162C";
  const COLOR_KINAL_BLUE = "#22376D";
  const COLOR_ETS_ORANGE = "#EC9123";
  const COLOR_GOLD = "#FFD166";
  const COLOR_WHITE = "#FFFFFF";
  const COLOR_SLATE_LIGHT = "#E2E8F0";
  const COLOR_SLATE_MUTED = "#94A3B8";

  // Eliminar diapositiva en blanco por defecto
  const defaultSlides = deck.getSlides();
  
  // Definición de Diapositivas con Anotaciones del Orador
  const slidesData = [
    {
      num: 1,
      categoria: "APERTURA Y PROMESA",
      titulo: "El Copiloto del Negocio",
      subtitulo: "Cómo resolver tareas de 3 horas en 7 minutos y tomar mejores decisiones con Inteligencia Artificial",
      grafica: "[GRÁFICO CENTRAL]\n• Logotipos Oficiales ETS y Kinal sobre fondo azul profundo (#0D162C).\n• Cronómetro / Reloj digital: 3 Horas ➔ 7 Minutos.\n• Icono de Copiloto Inteligente.",
      notas: "OBJETIVO: Conectar de inmediato con la audiencia, generar expectativa sin vender nada aún y establecer la promesa de valor: hoy resolverán un problema real en vivo.\n\n" +
             "QUÉ DECIR (GUION):\n" +
             "«Buenas noches a todos y bienvenidos a la Escuela Técnica Superior de Fundación Kinal. Quiero empezar haciéndoles una promesa muy clara: en esta sesión de 60 minutos NO venimos a venderles nada con discursos aburridos ni a llenarlos de teoría matemática. Hoy venimos a que ustedes mismos experimenten lo que significa resolver un problema que normalmente les quita tres horas en solo siete minutos».\n\n" +
             "«La Inteligencia Artificial no vino a quitarle el trabajo a nadie; vino a quitarle a usted el dolor de cabeza de las tareas mecánicas para devolverle el tiempo de ser el director de su propio negocio».\n\n" +
             "INTERACCIÓN: Preguntar al chat de Teams: ¿Cuál es esa tarea que más tiempo y pereza les da hacer en su negocio o trabajo cada semana?"
    },
    {
      num: 2,
      categoria: "DIAGNÓSTICO DEL DOLOR",
      titulo: "¿En qué se va tu día a día en el negocio?",
      subtitulo: "El 80% del tiempo apagando fuegos vs. el 20% pensando estratégicamente",
      grafica: "[INFOGRAFÍA COMPARATIVA]\n• Lado Izquierdo (Rojo/Alerta): 80% Operativo (Cotizaciones manuales, quejas en WhatsApp, números desordenados, inventario estancado).\n• Lado Derecho (Verde/Estratégico): 20% Crecimiento (Nuevas ofertas, clientes nuevos, paz mental y tiempo en familia).",
      notas: "OBJETIVO: Empatizar profundamente con el dolor real de los dueños de negocios y trabajadores independientes, validando que el cansancio no es falta de ganas, sino exceso de tareas manuales.\n\n" +
             "QUÉ DECIR (GUION):\n" +
             "«¿A cuántos de ustedes les pasa que abren el negocio a las 7:00 AM pensando en cómo van a vender más, y cuando dan las 6:00 PM sienten que no avanzaron nada porque se pasaron el día apagando fuegos? Respondiendo mensajes repetitivos, lidiando con un cliente que reclama, cuadrando notas a mano o peleando con un proveedor».\n\n" +
             "«El problema no es que les falte esfuerzo. El problema es que están usando su mente brillante para hacer tareas de máquina. Hoy vamos a delegarle a la máquina lo repetitivo para que ustedes vuelvan a ser los estrategas».\n\n" +
             "CONSEJO: Hacer una pausa de 3 segundos después de preguntar quién se siente apagando fuegos todo el día."
    },
    {
      num: 3,
      categoria: "DESMITIFICACIÓN",
      titulo: "Derribando los Dos Grandes Mitos de la IA",
      subtitulo: "Ni necesitas programar código, ni la IA es un juguete inútil",
      grafica: "[TARJETAS DE CONTRASTE]\n• Tarjeta 1 (Tachada con X roja): 'Tengo que saber de informática' ➔ Realidad: La interfaz es el español cotidiano.\n• Tarjeta 2 (Tachada con X roja): 'Solo da respuestas genéricas y tontas' ➔ Realidad: El secreto está en cómo formulas la orden (Prompt).",
      notas: "OBJETIVO: Eliminar el miedo tecnológico y explicar que las malas experiencias previas con ChatGPT se deben a falta de técnica, no a inutilidad de la herramienta.\n\n" +
             "QUÉ DECIR (GUION):\n" +
             "«Muchos me dicen: 'Mire, yo ya entré a ChatGPT y le pedí que me hiciera una carta de venta, pero me escribió algo que parecía un robot de hace diez años'. Y tienen toda la razón. Si ustedes le dicen: 'hazme una carta', la IA promedia lo que encuentra en internet y da una respuesta insípida».\n\n" +
             "«La IA es como un practicante nuevo que llegó hoy a su negocio: si usted le dice 'ayúdame en la tienda', se va a quedar parado sin saber qué hacer. Pero si le da un rol, un contexto y reglas claras, le resuelve en segundos».\n\n" +
             "INTERACCIÓN: Pedir que pongan un '1' en el chat quienes ya han probado ChatGPT y sintieron que el resultado fue demasiado genérico."
    },
    {
      num: 4,
      categoria: "MÉTODO PEDAGÓGICO KINAL",
      titulo: "La Fórmula Maestra de Kinal: Método RC-TRF",
      subtitulo: "5 bloques que transforman una petición vaga en oro en polvo",
      grafica: "[DIAGRAMA DE 5 BLOQUES DE COLOR]\n[R] ROL (Azul) ➔ Quién es la IA (Consultor, mediador, analista).\n[C] CONTEXTO (Celeste) ➔ Tu situación real (precios, clientes, margen).\n[T] TAREA (Verde) ➔ La acción concreta y exacta.\n[R] RESTRICCIÓN (Naranja) ➔ Lo que NO debe hacer y el tono.\n[F] FORMATO (Morado) ➔ Estructura de salida (Tabla + WhatsApp listo).",
      notas: "OBJETIVO: Presentar de forma memorable el método pedagógico central del curso (RC-TRF). Mostrar que la claridad de la mente humana es la que condiciona la calidad de la IA.\n\n" +
             "QUÉ DECIR (GUION):\n" +
             "«En Fundación Kinal no enseñamos a 'chatear' con la máquina. Enseñamos una metodología profesional: el método RC-TRF: Rol, Contexto, Tarea, Restricción y Formato. Grábense estas 5 letras. Si ustedes le dan a la IA estas cinco piezas, el resultado deja de ser un texto genérico y se convierte en un trabajo de consultoría de alto nivel».\n\n" +
             "«Y para demostrárselo, no me crean a mí: vamos a poner el cronómetro en 7 minutos y lo van a hacer ustedes mismos ahora mismo».\n\n" +
             "CONSEJO: Pedir que anoten las siglas RC-TRF en un papel o notas de su celular. Es la llave dorada del webinar."
    },
    {
      num: 5,
      categoria: "ACTIVIDAD EN VIVO 1 (PYMES / SERVICIOS)",
      titulo: "RETO EN VIVO: El Dilema del Descuento en 7 Minutos",
      subtitulo: "Salvar al cliente enojado sin regalar el dinero del negocio",
      grafica: "[CRONÓMETRO Y CASO REAL]\n• Cronómetro gigante marcando 07:00.\n• Caso: Cliente exige 20% descuento por retraso de 48h. Costos subieron 12%.\n• Prompt Maestro proyectado listo para copiar con método RC-TRF.\n• Resultado esperado: Tabla comparativa + Correo/WhatsApp diplomático sin bajar precio.",
      notas: "OBJETIVO: Facilitar el primer 'Aha moment'. Lograr que el 100% de la sala pegue el prompt en Gemini/ChatGPT y vea la matriz estratégica y el mensaje diplomático en su propia pantalla.\n\n" +
             "QUÉ DECIR (GUION DE FACILITACIÓN):\n" +
             "«El enlace y el texto acaban de ser pegados en el chat de Microsoft Teams. Les doy 3 minutos para que abran ChatGPT o Google Gemini en su teléfono o computadora, peguen el texto y le den ENTER. No tienen que cambiar nada por ahora; solo ejecútenlo y vean lo que ocurre».\n\n" +
             "«Fíjense en la magia: en vez de un correo sumiso pidiendo disculpas o regalando dinero, la IA les desglosa tres escenarios inteligentes: compensar con garantía extendida, ofrecer una bonificación en servicio futuro de bajo costo y una respuesta comercial que protege su dinero y mantiene la dignidad de su negocio».\n\n" +
             "INTERACCIÓN: Pedir en el chat: 'Escriban LISTO los que ya vieron la tabla y el mensaje en su pantalla'. Leer nombres en voz alta para elevar la energía."
    },
    {
      num: 6,
      categoria: "ACTIVIDAD EN VIVO 2 (TIENDA DE BARRIO)",
      titulo: "CASO DEL TENDERO: De Mercadería Estancada a Dinero en Caja",
      subtitulo: "Rescate de producto próximo a vencer y cobro amable de la libreta de fiado",
      grafica: "[INFOGRAFÍA DE COMERCIO POPULAR]\n• Problema del tendero: 15 jugos y 20 galletas a vencer en 4 días + libreta de fiado atrasada.\n• Solución en 3 minutos: 1. Combo Refacción Vecinal (recupera costo y da ganancia), 2. Cartel de mostrador de 3 líneas, 3. Mensaje empático para WhatsApp vecinal.\n• Cero producto botado, efectivo en caja para el proveedor.",
      notas: "OBJETIVO: Demostrar que la IA sirve para cualquier escala de negocio, desde una gran empresa hasta la tienda de la esquina, democratizando la tecnología y conectando con la identidad popular y el valor del trabajo bien hecho de Kinal.\n\n" +
             "QUÉ DECIR (GUION):\n" +
             "«Muchos piensan: 'Ah, eso sirve para empresas con gerentes en corbata'. ¡No! Piensen en Don Carlos, el tendero del barrio. Tiene 15 jugos y 20 galletas a punto de vencer en 4 días. Si los deja ahí, se van a la basura y pierde su dinero. O tiene a Doña Carmen que le debe en la libreta de fiado desde hace un mes y le da pena cobrarle porque es vecina».\n\n" +
             "«En 7 minutos con su teléfono, la IA le calculó el combo de recuperación, le armó el texto para el cartel y le redactó un mensajito para el grupo de WhatsApp de la colonia tan amable que la gente llega agradecida a comprarle. Eso es usar la tecnología al servicio de la persona y de la economía familiar».\n\n" +
             "INTERACCIÓN: Preguntar al público: ¿Quién conoce a alguien con una tiendita, un taller o un negocio familiar que podría beneficiarse de esto hoy mismo?"
    },
    {
      num: 7,
      categoria: "CRITERIO ÉTICO Y RIGOR INSTITUCIONAL",
      titulo: "El Abismo: ¿Por qué no basta con videos de YouTube?",
      subtitulo: "El 90% del éxito no es generar texto, es auditarlo con el «Trabajo Bien Hecho»",
      grafica: "[GRÁFICO DEL ICEBERG / ALERTA DE RIESGO]\n• 10% Visible: Generar texto o hacer preguntas sueltas.\n• 90% Sumergido (El Riesgo): Alucinaciones (datos falsos con apariencia de verdad), Fuga de privacidad (subir DPIs o datos de clientes a la nube), Falta de criterio humano.\n• El Principio Kinal: La persona y la verdad siempre están por encima de la técnica.",
      notas: "OBJETIVO: Sembrar la necesidad de una formación académica formal y estructurada. Justificar por qué se requiere el curso completo de Kinal para no cometer errores costosos.\n\n" +
             "QUÉ DECIR (GUION CLAVE):\n" +
             "«Lo que vieron hoy es emocionante, pero tengo que ser muy honesto con ustedes como formador de Fundación Kinal: una herramienta tan potente en manos de alguien sin criterio es peligrosa. Si ustedes le creen todo ciegamente a la IA, cometerán errores graves. La IA a veces 'alucina': inventa datos con una seguridad absoluta».\n\n" +
             "«En Kinal creemos en el principio del 'Trabajo Bien Hecho'. La excelencia no es generar 50 páginas de texto en un minuto; es tener el ojo crítico para auditarlo, asegurar la verdad y proteger la privacidad de su negocio y de su familia. En Kinal ustedes aprenden a ser los directores críticos de la herramienta, nunca sus esclavos»."
    },
    {
      num: 8,
      categoria: "PROPUESTA FORMATIVA OFICIAL",
      titulo: "Programa Oficial Kinal ETS: 16 Horas de Formación Práctica",
      subtitulo: "Inteligencia Artificial Aplicada, Ingeniería de Prompts y Productividad Ética",
      grafica: "[MATRIZ MODULAR 4 SEMANAS]\n• Mód 1: Fundamentos y Entorno Multimodelo (Gemini, ChatGPT, Copilot).\n• Mód 2: Ingeniería de Prompts RC-TRF y Catálogo Personal.\n• Mód 3: Casos Reales (Extracción de PDFs a Excel, Minutas y Correspondencia).\n• Mód 4: Ética, Privacidad y Proyecto Integrador (Asistente Propio).\n• Ficha Técnica: 8 Sesiones nocturnas (Mar y Jue 19:00 - 21:00), Teams + Kinal.academy, Aprobación 75/100.",
      notas: "OBJETIVO: Presentar el programa formal como una solución integral, estructurada, accesible y de prestigio institucional.\n\n" +
             "QUÉ DECIR (GUION):\n" +
             "«Por eso en la Escuela Técnica Superior de Kinal abrimos este programa de 16 horas formativas en 4 semanas. Son dos noches por semana, de 7:00 a 9:00 de la noche por Microsoft Teams, diseñado para gente trabajadora que no tiene tiempo que perder».\n\n" +
             "«No es un curso para sacar un diploma de asistencia: la nota mínima para aprobar es de 75 puntos sobre 100 y ustedes se gradúan defendiendo en vivo un Asistente de Inteligencia Artificial construido a la medida de su propio trabajo o negocio».\n\n" +
             "DETALLE: Destacar que las clases quedan grabadas en Kinal.academy pero la magia está en la práctica en vivo con el profesor."
    },
    {
      num: 9,
      categoria: "LLAMADO A LA ACCIÓN (SERVICIO)",
      titulo: "Tu Siguiente Decisión Estratégica",
      subtitulo: "Invierte 16 horas hoy para ahorrarte 10 horas semanales por el resto de tu vida",
      grafica: "[TARJETA DE ACCESO Y CÓDIGO QR]\n• Cupos estrictamente limitados para asegurar acompañamiento y revisión individual.\n• Beneficio asistentes: Plantilla con 50 Prompts Maestros de Negocio de Kinal.\n• Código QR gigante hacia matrícula en Kinal.academy y enlace de Teams.\n• Logotipo Escuela Técnica Superior Kinal.",
      notas: "OBJETIVO: Cierre orgánico, de servicio y sin presión agresiva. Invitar a tomar la decisión de superación personal y profesional con el respaldo de Kinal.\n\n" +
             "QUÉ DECIR (CIERRE):\n" +
             "«Para terminar, les dejo esta reflexión: en este momento tienen dos opciones. La primera es cerrar el webinar, guardar el prompt y seguir haciendo las cosas igual el lunes por la mañana. La segunda es invertir 16 horas de su vida durante las próximas cuatro semanas para adquirir una habilidad que multiplicará su competitividad por los próximos diez años».\n\n" +
             "«El cupo es reducido porque no es una conferencia pasiva: es un taller de acompañamiento donde ningún estudiante se queda atrás. En el chat y en pantalla tienen el enlace directo para asegurar su lugar. Será un verdadero honor tenerlos como alumnos en las aulas virtuales de Fundación Kinal. ¡Muchas gracias y abrimos micrófono para preguntas!»\n\n" +
             "CONSEJO FINAL: Quedarse en la sala respondiendo dudas específicas de negocio de 3 a 5 participantes. Quienes se quedan al final son las inscripciones más seguras."
    }
  ];

  // Crear Diapositivas
  slidesData.forEach(function(item) {
    var slide = deck.appendSlide(SlidesApp.PredefinedLayout.BLANK);
    
    // Fondo temático Kinal Navy
    slide.getBackground().setSolidFill(COLOR_NAVY);
    
    // Franja Superior de Acento Naranja ETS
    var topBar = slide.insertShape(SlidesApp.ShapeType.RECTANGLE, 0, 0, 720, 8);
    topBar.getFill().setSolidFill(COLOR_ETS_ORANGE);
    topBar.getBorder().setTransparent();
    
    // Categoría / Badge
    var catBox = slide.insertTextBox(item.categoria, 40, 20, 400, 20);
    var catText = catBox.getText();
    catText.getTextStyle().setFontFamily("Arial").setFontSize(10).setBold(true).setForegroundColor(COLOR_ETS_ORANGE);
    
    // Título Principal
    var titleBox = slide.insertTextBox(item.titulo, 40, 42, 640, 45);
    var titleText = titleBox.getText();
    titleText.getTextStyle().setFontFamily("Arial").setFontSize(22).setBold(true).setForegroundColor(COLOR_WHITE);
    
    // Subtítulo
    var subBox = slide.insertTextBox(item.subtitulo, 40, 88, 640, 30);
    var subText = subBox.getText();
    subText.getTextStyle().setFontFamily("Arial").setFontSize(12).setItalic(true).setForegroundColor(COLOR_SLATE_MUTED);
    
    // Contenedor Gráfico Central (Tarjeta visual)
    var card = slide.insertShape(SlidesApp.ShapeType.ROUNDED_RECTANGLE, 40, 130, 640, 220);
    card.getFill().setSolidFill(COLOR_KINAL_BLUE);
    card.getBorder().setWeight(1).getBorderFill().setSolidFill(COLOR_ETS_ORANGE);
    
    var cardText = card.getText();
    cardText.setText(item.grafica);
    cardText.getTextStyle().setFontFamily("Arial").setFontSize(12).setForegroundColor(COLOR_SLATE_LIGHT);
    
    // Pie de diapositiva
    var footerBox = slide.insertTextBox("Fundación Kinal · Escuela Técnica Superior (ETS)  |  Lámina " + item.num + " de " + slidesData.length, 40, 365, 640, 20);
    var footerText = footerBox.getText();
    footerText.getTextStyle().setFontFamily("Arial").setFontSize(9).setForegroundColor(COLOR_SLATE_MUTED);

    // INSERCIÓN DE NOTAS DEL ORADOR (SPEAKER NOTES)
    var notesPage = slide.getNotesPage();
    var speakerNotesShape = notesPage.getSpeakerNotesShape();
    speakerNotesShape.getText().setText(item.notas);
  });

  // Eliminar diapositiva vacía inicial si existe
  if (defaultSlides.length > 0) {
    defaultSlides[0].remove();
  }

  Logger.log("¡Presentación creada con éxito!");
  Logger.log("Enlace de Google Slides: " + deck.getUrl());
  return deck.getUrl();
}
