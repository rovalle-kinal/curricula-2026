---
title: Promesa de venta
created: 2026-09-19
creado: 2026-09-19
status: Propuesta
tags:
  - Kinal/IoT/Home-Automation
---
# Promesa de venta

## Taller de Automatización Residencial e Internet de las Cosas (IoT): De Sensores y Microcontroladores ESP32 a la Domótica Local con Home Assistant

> [!NOTE]
> Este documento contiene el diagnóstico del mercado residencial, la propuesta de valor comercial transformadora, el perfil de egreso y el temario curricular jerárquico del taller presencial a impartirse en Fundación Kinal.  
> Para consultar la visión panorámica y ficha técnica institucional, revisa [[Índice general del programa]].  
> Para los fundamentos técnicos de redes, protocolos y seguridad eléctrica, consulta [[Planificación]].  
> Para el microdiseño de sesiones, rúbrica analítica y proyecto Capstone, revisa [[Secuencia didáctica]].

---

## Diagnóstico del Dolor: La Frustración de la Domótica Comercial en la Nube

El mercado residencial en Guatemala está inundado de dispositivos inteligentes económicos (bombillos Wi-Fi, enchufes inteligentes, interruptores táctiles de marcas comerciales como Tuya, SmartLife o eWeLink). Sin embargo, quienes intentan automatizar su hogar enfrentan rápidamente problemas frustrantes:

* **Dependencia Total de Internet:** Si el proveedor de telecomunicaciones tiene una caída de servicio o si el router pierde la conexión exterior, las luces no encienden, los sensores dejan de responder y las rutinas se detienen por completo.
* **Fragmentación de Aplicaciones (*App Fatigue*):** El usuario termina con 4 o 5 aplicaciones móviles distintas en su teléfono (una para las luces, otra para los enchufes, otra para las cámaras y otra para el aire acondicionado) que no se comunican entre sí.
* **Vulnerabilidad y Pérdida de Privacidad:** La telemetría de los sensores, los horarios de presencia en el hogar y el tráfico de video se transmiten a servidores remotos en el extranjero fuera del control del usuario.
* **Instalaciones Eléctricas Inseguras:** La mayoría de dispositivos son instalados con empalmes improvisados con cinta aislante dentro de cajas de registro estrechas, generando falsos contactos, sobrecalentamiento y peligro inminente de cortocircuito o incendio.

---

## La Propuesta de Valor Transformadora

El **Taller de Automatización Residencial e Internet de las Cosas en Fundación Kinal** te enseña a construir un sistema domótico profesional, robusto y soberano.

Aprenderás a desplegar **Home Assistant**, la plataforma de automatización de código abierto líder a nivel mundial, integrando un broker de mensajería **MQTT local** y microcontroladores de alto rendimiento **ESP32**.

El resultado es un ecosistema inteligente que opera **100% de forma local en tu propia red**:
* Funciona con o sin internet.
* Respuesta instantánea en milisegundos sin latencia de servidores externos.
* Privacidad absoluta: tus datos nunca salen de tu hogar.
* Integración multimarca total en un solo panel de control personalizado y elegante.
* Seguridad eléctrica residencial de grado profesional bajo el principio Kinal del *"trabajo bien hecho"*.

---

## Beneficios Concretos para el Participante y el Profesional

### Para Electricistas, Instaladores y Emprendedores Técnicos
* **Nueva Línea de Servicios de Alto Valor:** Pasa de ser un instalador eléctrico convencional a convertirte en un Integrador Domótico Profesional, cobrando por proyectos integrales de automatización de residencias, oficinas y comercios.
* **Cero Reclamos por Fallas de Conexión:** Al implementar sistemas locales con Home Assistant y MQTT, eliminas los reclamos de clientes cuyas luces dejan de funcionar cuando se cae el internet de la casa.
* **Montajes de Estándar Profesional:** Aprende a utilizar conectores de palanca WAGO 221, cajas normalizadas y relés optoacoplados con protección contra cargas inductivas, erradicando los empalmes defectuosos.

### Para Ingenieros, Estudiantes de Tecnología y Makers
* **Fusión Real entre Software y Hardware:** Conecta el mundo digital de la programación con actuadores y sensores del mundo físico a 120 VAC.
* **Dominio de Microcontroladores ESP32 y ESPHome:** Aprende a crear tus propios dispositivos inteligentes personalizados a una fracción del costo de los equipos comerciales.
* **Soberanía y Seguridad de Datos:** Diseña arquitecturas de red domótica inmunes a la obsolescencia programada y a las suscripciones mensuales de las grandes tecnológicas.

---

## Perfil de Egreso y Capacidades Demostrables

Al culminar satisfactoriamente el taller con una nota superior al umbral de suficiencia de Kinal (**$\ge 75$ puntos**), el participante demuestra en vivo:
* Configuración completa de un servidor Home Assistant local con broker MQTT Mosquitto asegurado con credenciales.
* Programación de nodos sensores basados en microcontroladores ESP32 mediante firmware declarativo ESPHome y C++.
* Integración de sensores ambientales de temperatura, humedad, luminosidad y radar de presencia humana mmWave con autodescubrimiento de entidades.
* Cableado e instalación de módulos de conmutación de cargas residenciales a 120 VAC (relés optoacoplados y módulos Shelly/Sonoff) con conectores WAGO 221 y fase conmutada.
* Diseño de un panel táctil Lovelace intuitivo y ergonómico para smartphones y tablets.
* Programación de rutinas y automatizaciones reactivas ante eventos (iluminación automática por presencia/lux, control de clima y notificaciones móviles).

---

## Temario Curricular General Jerárquico

Estructura temática detallada sin numeraciones, organizada mediante niveles de tabulación y viñetas limpias:

* **Módulo: Arquitectura de Domótica Local, Redes y Home Assistant**
	* Introducción al Internet de las Cosas (IoT) y la Automatización Residencial
		* Evolución de la domótica: de los sistemas centralizados cableados a las redes inalámbricas distribuidas
		* Nube comercial vs. domótica local independiente: análisis de latencia, privacidad, disponibilidad y costo
		* Soberanía tecnológica y ventajas del ecosistema de código abierto Home Assistant
	* Despliegue de la Infraestructura de Servidor
		* Opciones de instalación: Home Assistant OS (HAOS) en Mini PC, Raspberry Pi o máquina virtual
		* Configuración inicial del entorno, gestión de usuarios locales y asignación de direcciones IP estáticas
		* El almacén de complementos (*Add-ons*): File Editor, Terminal SSH y herramientas de diagnóstico
	* El Protocolo de Mensajería MQTT (Message Queuing Telemetry Transport)
		* Fundamentos del modelo Publicador/Suscriptor (*Pub/Sub*)
		* Despliegue y configuración del broker Eclipse Mosquitto en Home Assistant
		* Definición de usuarios de servicio, control de acceso y seguridad en la red local
		* Jerarquía y nomenclatura de tópicos (*Topics*) y niveles de Calidad de Servicio (QoS)
		* Diagnóstico y monitoreo de tráfico en tiempo real mediante clientes MQTT (MQTT Explorer)

* **Módulo: Microcontroladores ESP32, Firmware ESPHome y Sensado Ambiental**
	* Plataforma de Cómputo Físico: El Microcontrolador ESP32
		* Arquitectura del SoC ESP32: procesador dual-core, radio Wi-Fi 2.4 GHz y Bluetooth BLE
		* Mapeo de terminales de entrada/salida de propósito general (GPIO): pines de arranque seguro (*strapping pins*) y precauciones eléctricas
		* Canales de modulación por ancho de pulsos (PWM) y convertidores analógico-digitales (ADC)
	* Desarrollo Ágil de Nodos IoT con ESPHome
		* El ecosistema ESPHome: generación de firmware embebido a partir de configuraciones declarativas YAML
		* Flasheo inicial por puerto USB y configuración de credenciales Wi-Fi protegidas con secretos
		* Actualizaciones inalámbricas por aire (**OTA - Over-The-Air**)
		* Integración nativa por API cifrada y autodescubrimiento automático en Home Assistant
	* Red de Sensores Ambientales y Presencia Humana
		* Medición climática de precisión: sensores de temperatura y humedad relativa (DHT22 / BME280)
		* Medición de luminosidad ambiental mediante fotorresistores (LDR) y conversión analógica a lux
		* Detección de presencia humana avanzada: comparativa entre sensores infrarrojos pasivos (PIR) y radares de ondas milimétricas (mmWave LD2410) para detección de micro-movimientos
		* Calibración de umbrales, filtros de ruido y eliminación de falsos positivos en el registro de estancia

* **Módulo: Actuación de Potencia a 120 VAC, Seguridad Eléctrica y Dispositivos Comerciales**
	* Seguridad Eléctrica Residencial y Normativa Kinal
		* Prevención de riesgos en circuitos de corriente alterna a 120 VAC / 60 Hz
		* Identificación instrumental de fase viva, neutro y tierra física mediante multímetro digital
		* La regla del *"trabajo bien hecho"*: erradicación de empalmes con cinta aislante y adopción de conectores de palanca WAGO 221
		* Disposición ordenada del cableado dentro de cajas de registro rectangulares (chalupas)
	* Módulos de Relevadores y Aislamiento Galvánico
		* Principio de funcionamiento del relevador electromagnético y relé de estado sólido (SSR)
		* Aislamiento galvánico por optoacoplador y separación física de planos de voltaje (3.3 VDC vs. 120 VAC)
		* Conmutación de fase viva a través de contactos normalmente abiertos (NO) y común (COM)
		* Protección contra sobretensiones y arcos inductivos en motores y ventiladores mediante redes snubber RC y varistores MOV
	* Integración Híbrida con Dispositivos Comerciales sin Nube
		* Módulos inteligentes comerciales compactos (Shelly 1 Plus, Sonoff Mini R4)
		* Desbloqueo y configuración de firmware para control local puro sin dependencia de la nube del fabricante
		* Conexión con interruptores de pared tradicionales manteniendo el accionamiento manual en paralelo con la automatización inteligente

* **Módulo: Interfaces Lovelace, Automatizaciones Avanzadas y Proyecto Capstone**
	* Diseño Ergonómico de Cuadros de Mando (Lovelace Dashboards)
		* Principios de diseño visual centrado en el usuario para interfaces de automatización residencial
		* Estructuración de vistas por habitaciones, áreas y funciones del hogar
		* Configuración de tarjetas interactivas: tarjetas de estado, medidores circulares (gauges), controles deslizantes de brillo y botones con confirmación táctil
		* Visualización de gráficas históricas de temperatura y consumo energético
		* Adaptación responsiva para smartphones, tablets empotradas en pared y ordenadores
	* Motor de Automatizaciones Lógicas (ECA)
		* Estructura universal: Disparadores (*Triggers*), Condiciones (*Conditions*) y Acciones (*Actions*)
		* Automatizaciones reactivas a la presencia humana y al nivel de luz ambiental para ahorro de energía
		* Automatizaciones basadas en horarios, eventos astronómicos (amanecer / atardecer) y temporizadores de seguridad
		* Gestión de modos de operación del hogar (*En Casa / Fuera de Casa / Modo Noche*)
		* Configuración de notificaciones push directas al teléfono móvil ante eventos anómalos
	* Proyecto Capstone Integrador: "Smart Room" y Evaluación Terminal
		* Integración en banco de trabajo: servidor Home Assistant, broker MQTT, nodo sensor ESP32, módulo de relé y carga a 120 VAC
		* Ejecución coordinada del ciclo de iluminación automática condicional y alerta ambiental
		* Demostración en vivo ante el instructor y prueba de control dual (físico y móvil)
		* Evaluación individual de sustentación conforme a la rúbrica terminal analítica (&ge; 75 pts)
		* Visado oficial de la Bitácora de Taller (*Berichtsheft*) y clausura del programa
