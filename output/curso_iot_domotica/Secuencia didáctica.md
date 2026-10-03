---
title: Secuencia didáctica
created: 2026-09-19
creado: 2026-09-19
status: Propuesta
tags:
  - Kinal/IoT/Home-Automation
---
# Secuencia didáctica

> [!NOTE]
> Este documento especifica el microdiseño pedagógico de las cuatro sesiones intensivas de taller, los momentos didácticos, el proyecto Capstone presencial, la rúbrica terminal analítica y el sistema de bitácora del *Taller de Automatización Residencial e Internet de las Cosas (IoT)*.  
> Para consultar la visión panorámica del programa y la ficha técnica institucional, dirígete a [[Índice general del programa]].  
> Para la fundamentación técnica de redes, protocolos y seguridad eléctrica, revisa [[Planificación]].  
> Para la propuesta de valor comercial y el temario curricular jerárquico, consulta [[Promesa de venta]].

---

## Estructura de los Momentos Pedagógicos por Sesión de Taller

Cada una de las cuatro sesiones presenciales de 4 horas (240 minutos) se organiza en tres momentos didácticos diseñados para maximizar la ejecución práctica en laboratorio:

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│                       SESIÓN DE TALLER (240 MINUTOS)                        │
├──────────────────────────┬─────────────────────────────────┬────────────────┤
│    APERTURA (20 MIN)     │      DESARROLLO (190 MIN)       │ CIERRE (30 MIN)│
│                          │                                 │                │
│ • Activación y contexto  │ • Modelado docente en vivo      │ • Pruebas live │
│ • Prevención de riesgos  │ • Configuración de Home Assist. │ • Calidad Kinal│
│ • Inspección de multímet.│ • Cableado con WAGO y relés     │ • 5S en banco  │
│ • Planteamiento del reto │ • Flasheo OTA de ESP32          │ • Berichtsheft │
└──────────────────────────┴─────────────────────────────────┴────────────────┘
```

---

## Matriz de Secuencias Didácticas en Laboratorio y Taller

| Sesión y Eje Formativo | Momento Didáctico | Actividad del Instructor (Enfoque AEVO / Kinal) | Actividad del Participante en Estación de Trabajo | Recursos y Equipamiento | Criterio e Instrumento de Evaluación |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Sesión: Infraestructura, Redes y Home Assistant Local**<br>Bloque Servidor y MQTT | **Apertura**<br>(20 min) | Presenta el taller; expone la vulnerabilidad de las nubes comerciales y el valor de la domótica 100% local. Establece normas de ciberseguridad en redes Wi-Fi. | Debate sobre casos reales de cámaras hackeadas o fallas de internet en casas inteligentes; revisa la topología de red del laboratorio. | Presentación técnica; router Wi-Fi de alta densidad de laboratorio. | **Criterio:** Comprensión de riesgos de privacidad.<br>**Instrumento:** Evaluación formativa oral. |
| **Sesión: Infraestructura, Redes y Home Assistant Local**<br>Bloque Servidor y MQTT | **Desarrollo**<br>(190 min) | Guía la inicialización de Home Assistant OS; modela la instalación del complemento Mosquitto Broker y la creación de credenciales de usuario locales. | Configura su entorno en Home Assistant; instala un cliente MQTT (MQTT Explorer) en su PC; publica mensajes de prueba y verifica la recepción en tiempo real. | Mini PC / Raspberry Pi con Home Assistant; computadoras de laboratorio; MQTT Explorer. | **Criterio:** Broker MQTT configurado y autenticado.<br>**Instrumento:** Lista de verificación de conectividad de red. |
| **Sesión: Infraestructura, Redes y Home Assistant Local**<br>Bloque Servidor y MQTT | **Cierre**<br>(30 min) | Supervisa la comprobación de tráfico MQTT y la asignación de direcciones IP estáticas por DHCP para evitar pérdidas de enlace. | Realiza una copia de seguridad (*Backup*) inicial del sistema; documenta las credenciales de red y anota los pasos en su bitácora. | Consola de administración de Home Assistant; formato de bitácora (*Berichtsheft*). | **Criterio:** Respaldo y orden documental.<br>**Instrumento:** Registro visado en bitácora. |
| **Sesión: Microcontroladores ESP32 y Sensado Ambiental**<br>Bloque Nodos Sensores | **Apertura**<br>(20 min) | Explica el mapa de pines (GPIO) del ESP32, los límites de corriente por pin (máx. 12 mA) y el peligro de dañar el chip por sobretensión a 5V en entradas analógicas. | Identifica los pines seguros para sensores en la placa NodeMCU-32S; analiza el diagrama esquemático del divisor de tensión para el fotorresistor LDR. | Hojas de datos de ESP32; componentes pasivos; protoboard. | **Criterio:** Reconocimiento de pines seguros del SoC.<br>**Instrumento:** Prueba rápida de pines GPIO. |
| **Sesión: Microcontroladores ESP32 y Sensado Ambiental**<br>Bloque Nodos Sensores | **Desarrollo**<br>(190 min) | Modela la integración de ESPHome en Home Assistant; escribe en vivo un archivo YAML para leer temperatura/humedad (DHT22) y presencia (PIR/radar mmWave). | Conecta los sensores en protoboard; compila y sube el firmware al ESP32 vía USB inicial y luego por Wi-Fi (OTA); verifica la aparición automática de entidades en Home Assistant. | Placas ESP32; sensores DHT22; sensores de presencia LD2410/PIR; LDRs; cables puente. | **Criterio:** Autodescubrimiento de entidades sin errores.<br>**Instrumento:** Rúbrica de hardware embebido y sensado. |
| **Sesión: Microcontroladores ESP32 y Sensado Ambiental**<br>Bloque Nodos Sensores | **Cierre**<br>(30 min) | Evalúa la estabilidad de las lecturas y la ausencia de falsos positivos en la detección de presencia humana. | Calibra los umbrales de sensibilidad del radar mmWave; documenta los nombres de entidades generadas en la bitácora técnica. | Interfaz de telemetría en tiempo real de Home Assistant. | **Criterio:** Precisión y estabilidad de datos (&ge; 75 pts).<br>**Instrumento:** Hoja de calibración de sensores. |
| **Sesión: Actuación Segura a 120 VAC y Dispositivos Comerciales**<br>Bloque Cargas de Potencia | **Apertura**<br>(20 min) | Imparte la inducción de seguridad eléctrica a 120 VAC: uso de multímetro para identificación de fase viva vs. neutro; advertencia de arco eléctrico y riesgos de incendio. | Verifica la ausencia de tensión con multímetro antes de manipular líneas de fuerza; inspecciona los conectores WAGO 221 de palanca. | Multímetros digitales CAT III; clavijas de prueba polarizadas; guías de seguridad eléctrica Kinal. | **Criterio:** Identificación rigurosa de fase y neutro.<br>**Instrumento:** Lista de cotejo de seguridad eléctrica. |
| **Sesión: Actuación Segura a 120 VAC y Dispositivos Comerciales**<br>Bloque Cargas de Potencia | **Desarrollo**<br>(190 min) | Demuestra el conexionado de un módulo de relé optoacoplado al ESP32 y la integración de un interruptor inteligente Shelly/Sonoff flasheado para control local puro. | Cablea una bombilla incandescente/LED a 120 VAC pasando la fase por el relé; utiliza conectores WAGO dentro de una caja de registro chalupa; prueba el mando manual y remoto. | Cajas de registro chalupa; focos LED E27; conectores WAGO 221; relés optoacoplados; módulos Shelly. | **Criterio:** Montaje seguro, limpio y libre de empalmes sueltos.<br>**Instrumento:** Rúbrica de calidad de instalación residencial Kinal. |
| **Sesión: Actuación Segura a 120 VAC y Dispositivos Comerciales**<br>Bloque Cargas de Potencia | **Cierre**<br>(30 min) | Inspecciona cada banco de trabajo: penaliza terminaciones con cobre expuesto o conmutación indebida del neutro. | Prueba el accionamiento del foco desde el pulsador de pared físico y desde la interfaz web; desconecta y guarda el cableado de potencia con seguridad. | Tableros de prueba residencial. | **Criterio:** Cumplimiento del *"trabajo bien hecho"* (&ge; 75 pts).<br>**Instrumento:** Lista de verificación de aislamiento eléctrico. |
| **Sesión: Automatizaciones Avanzadas, Dashboard y Capstone**<br>Bloque Integración Terminal | **Apertura**<br>(20 min) | Plantea las condiciones del proyecto Capstone *"Smart Room"*: integración completa de sensado, iluminación adaptativa, corte automático y panel de control ergonómico. | Revisa las especificaciones de entrega; define la paleta de colores y distribución de tarjetas en la pantalla táctil de su dashboard Lovelace. | Guías de ergonomía de interfaz de usuario para domótica. | **Criterio:** Diseño centrado en el habitante del hogar.<br>**Instrumento:** Evaluación formativa de boceto de interfaz. |
| **Sesión: Automatizaciones Avanzadas, Dashboard y Capstone**<br>Bloque Integración Terminal | **Desarrollo**<br>(190 min) | Asesora la programación de automatizaciones complejas (condiciones de iluminación, retardo de apagado por inactividad y notificaciones al celular ante eventos críticos). | Programa el motor de automatizaciones ECA en YAML o interfaz gráfica; vincula el sensor de presencia, el sensor de lux y la lámpara a 120 VAC; diseña su dashboard Lovelace móvil. | Servidor Home Assistant; estación domótica completa; smartphones de los aprendices. | **Criterio:** Lógica reactiva impecable sin bucles infinitos.<br>**Instrumento:** Rúbrica de automatización y diseño UI. |
| **Sesión: Automatizaciones Avanzadas, Dashboard y Capstone**<br>Bloque Integración Terminal | **Cierre**<br>(30 min) | Evalúa individualmente la defensa del proyecto Capstone conforme a la rúbrica terminal; entrega certificados de aprobación y clausura el taller. | Sustenta su estación domótica en vivo: demuestra la automatización de la habitación, simula una intrusión y muestra el control móvil; entrega su bitácora visada. | Estación Capstone operativa; certificados de acreditación Kinal. | **Criterio:** Dominio técnico integral y defensa oral (**Nota mínima: 75 pts**).<br>**Instrumento:** Rúbrica analítica terminal y consolidación de actas. |

---

## Especificación del Proyecto Capstone Terminal Presencial

### Título del Proyecto
*Smart Room: Habitación Residencial Autónoma y Segura con Gestión de Clima, Iluminación Circadiana y Supervisión Local.*

### Descripción Funcional de la Estación Domótica
1. **Monitoreo Ambiental Completo:** El nodo ESP32 adquiere y publica continuamente los valores de temperatura (°C), humedad relativa (%) y luminosidad ambiental (lux) hacia el broker MQTT local.
2. **Detección de Presencia Inmediata:** Un sensor de radar mmWave / PIR detecta el ingreso de personas a la habitación con respuesta en menos de 100 ms.
3. **Iluminación Automática Condicional:**
   * Si hay presencia humana **Y** la luminosidad ambiental es inferior a 60 lux, el sistema conmuta la lámpara principal de 120 VAC a través del relé o módulo Shelly.
   * Al abandonar la habitación, tras 2 minutos continuos de inactividad confirmada por el sensor, el sistema apaga automáticamente la luminaria para ahorro de energía.
4. **Alerta Preventiva de Clima o Ventilación:** Si la temperatura supera los 28°C o la humedad supera el 70%, el sistema activa una salida para ventilación forzada y envía una notificación instantánea al teléfono móvil del usuario.
5. **Dashboard Táctil Lovelace:** Pantalla principal con tarjetas interactivas que reflejan el estado en tiempo real de la habitación, gráfica histórica de clima de las últimas 24 horas y selector manual de modo (*Automático / Forzado / Vacaciones*).

---

## Rúbrica Analítica Terminal de Evaluación

La acreditación del taller exige el cumplimiento estricto del estándar institucional de Fundación Kinal:
* **Nota Mínima Aprobatoria:** **75 puntos sobre 100** en el promedio ponderado y en cada dimensión técnica evaluada.

| Dimensión Evaluada y Ponderación | Excelente (90 - 100 pts) | Satisfactorio (75 - 89 pts)<br>*[Umbral Aprobatorio]* | En Desarrollo (60 - 74 pts) | No Aprobado (< 60 pts) |
| :--- | :--- | :--- | :--- | :--- |
| **Infraestructura de Red y Broker MQTT**<br>(25%) | Despliegue impecable de Home Assistant; broker Mosquitto securizado con usuarios y contraseñas específicas; tópicos organizados con sintaxis REST/MQTT limpia; cero pérdidas de paquetes. | Home Assistant y Mosquitto operativos en red local; tópicos funcionales y comunicación estable con clientes (**&ge; 75 pts**). | Broker funcionando sin autenticación de seguridad; desconexiones ocasionales por conflictos de IP en la red Wi-Fi. | Incapacidad para inicializar Home Assistant o Mosquitto; desconocimiento absoluto del modelo publicador/suscriptor. |
| **Hardware Embebido y Sensado con ESP32**<br>(25%) | Nodo sensor ESP32 compilado con ESPHome; lecturas estables y filtradas; actualización por aire (OTA) operativa; cero falsos positivos en el radar de presencia; cableado limpio en protoboard. | ESP32 conectado y reportando temperatura, humedad y presencia en Home Assistant sin caídas (**&ge; 75 pts**). | Lecturas de sensores con ruido o congelamientos esporádicos; dificultades para flashear el microcontrolador vía Wi-Fi. | Microcontrolador bloqueado por conexiones erróneas; sensores quemados por sobretensión en pines GPIO. |
| **Actuación Segura a 120 VAC y Calidad de Montaje**<br>(25%) | Montaje eléctrico de estándar profesional Kinal: uso de conectores WAGO 221, fase conmutada con aislamiento galvánico verificado, cables peinados dentro de chalupa, cero riesgo de contacto directo. | Conexiones firmes y seguras a 120 VAC con conectores adecuados; fase conmutada en el relé; aislamiento comprobado con multímetro (**&ge; 75 pts**). | Conexiones inseguras con cinta aislante; dudas al identificar fase vs. neutro; conductores con exceso de cobre pelado expuesto. | Cortocircuitos por inversión de fase y neutro; manipulación de líneas vivas sin desenergizar; violación grave de normas de seguridad. |
| **Automatización, Dashboard Lovelace y Trabajo Bien Hecho**<br>(25%) | Dashboard visualmente ergonómico y responsivo; automatizaciones lógicas complejas con múltiples condiciones; puntualidad perfecta, orden en banco y bitácora completa. | Dashboard funcional con controles de luces y clima; automatización de presencia operativa; banco limpio y bitácora entregada (**&ge; 75 pts**). | Dashboard saturado o poco intuitivo; automatizaciones con bucles de encendido/apagado erráticos; bitácora incompleta. | Ausencia de automatizaciones funcionales; panel de control roto; desorden crónico y herramientas abandonadas en el laboratorio. |

---

## Sistema de Bitácora de Aprendizaje en Taller (Berichtsheft)

Cada participante lleva una bitácora técnica de seguimiento:
* **Estructura del Registro:**
  * Fecha, bloque de taller y objetivo del montaje.
  * Esquema de conexionado de pines entre el ESP32, sensores y módulos de relé.
  * Fragmento clave de código YAML (ESPHome / Automatizaciones) y diagrama de flujo lógico.
  * Incidencias encontradas y soluciones implementadas (ej. corrección de rebotes en sensores o asignación de IP estática).
  * Firma del participante y visado del instructor de laboratorio.
* **Requisito de Aprobación:** La bitácora visada con nota satisfactoria (&ge; 75 pts) es requisito indispensable para optar a la certificación del curso.
