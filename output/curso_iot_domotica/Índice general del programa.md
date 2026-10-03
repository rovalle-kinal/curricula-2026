---
title: Índice general del programa
created: 2026-09-19
creado: 2026-09-19
status: Propuesta
tags:
  - Kinal/IoT/Home-Automation
---
# Índice general del programa

## Taller de Automatización Residencial e Internet de las Cosas (IoT): De Sensores y Microcontroladores ESP32 a la Domótica Local con Home Assistant

> [!IMPORTANT]
> **Ficha Técnica Institucional:**
> * **Institución:** Fundación Kinal - Sede Central (Zona 7, Ciudad de Guatemala)
> * **Área Académica:** Cursos Libres de Tecnología y Formación Continua (TICs / Electrónica)
> * **Modalidad:** Presencial en Laboratorios de Electrónica y Redes
> * **Duración Total:** 16 horas pedagógicas intensivas (4 sesiones de 4 horas o 2 jornadas completas de 8 horas)
> * **Nivel de Referencia:** Equivalencia DQR Nivel 4 - 5 (Competencia Técnica en IoT, Redes Locales y Automatización Embebida)
> * **Nota Mínima Aprobatoria:** **75 puntos sobre 100** en proyectos prácticos, configuración de red y evaluación Capstone
> * **Ideario Institucional:** Principio del *"trabajo bien hecho"*, seguridad eléctrica residencial estricta (120 VAC), privacidad de datos personales y soberanía tecnológica

---

## Estructura del Ecosistema de Estudio (Navegación del Sistema)

El presente programa formativo se encuentra estructurado a través de cuatro notas interconectadas mediante wikilinks:

* 🧭 **[[Índice general del programa]]:** Ficha técnica institucional, navegación del ecosistema, perfiles formativos y dosificación curricular de 16 horas.
* ⚙️ **[[Planificación]]:** Fundamentación técnica de redes IoT, protocolos de mensajería (MQTT / Mosquitto), microcontroladores ESP32, firmware ESPHome, arquitectura de Home Assistant, seguridad eléctrica y criterios de cableado residencial Kinal.
* 🎯 **[[Secuencia didáctica]]:** Microdiseño de las 4 sesiones de taller (Apertura 20 min, Desarrollo 190 min, Cierre 30 min), especificación del proyecto Capstone *"Smart Room"*, rúbrica analítica terminal (&ge; 75 pts) y Bitácora de Taller (*Berichtsheft*).
* 💼 **[[Promesa de venta]]:** Diagnóstico de la domótica comercial dependiente de la nube, propuesta de valor de automatización privada y local, capacidades de egreso y temario curricular jerárquico tabulado con viñetas.

---

## Perfil de Ingreso

El curso está diseñado para:
* Técnicos electricistas, técnicos electrónicos, instaladores de redes o sistemas de seguridad que deseen expandir sus servicios hacia la domótica residencial moderna.
* Estudiantes de ingeniería en sistemas, electrónica, telecomunicaciones o mecatrónica que busquen dominar el enlace físico entre microcontroladores y plataformas de supervisión IoT.
* Entusiastas de la tecnología y usuarios avanzados (*makers*) con conocimientos básicos de electricidad o informática interesados en automatizar su hogar sin depender de servicios de suscripción en la nube.
* Compromiso con la seguridad eléctrica, puntualidad y trabajo ordenado en laboratorio.

---

## Perfil de Egreso

Al finalizar el taller, el participante será capaz de:
* Diseñar e implementar redes de domótica local basadas en la plataforma abierta **Home Assistant**, garantizando privacidad, nula dependencia de servidores externos y operación continua sin conexión a internet.
* Configurar e integrar un broker de mensajería **MQTT (Mosquitto)**, comprendiendo la arquitectura publicador/suscriptor, jerarquía de tópicos y cargas útiles JSON.
* Programar microcontroladores **ESP32** mediante **ESPHome** y C++ (Arduino IDE/PlatformIO) para la adquisición de datos de sensores ambientales (temperatura, humedad, presencia por radar mmWave/PIR y luminosidad).
* Conectar y gobernar actuadores de potencia a 120 VAC (relés mecánicos, relés de estado sólido y dispositivos comerciales Shelly / Sonoff) respetando la normativa de seguridad eléctrica y el principio del trabajo bien hecho.
* Desarrollar paneles de control táctiles personalizados (**Lovelace Dashboards**) accesibles desde teléfonos móviles, tabletas y computadoras.
* Programar automatizaciones avanzadas basadas en eventos condicionales, estados cruzados de sensores, programaciones horarias y notificaciones push directas.

---

## Arquitectura y Dosificación Curricular en Laboratorios Kinal

El curso de 16 horas se distribuye en cuatro bloques intensivos de 4 horas que combinan un 20% de fundamentos conceptuales y un 80% de implementación práctica sobre hardware real:

| Bloque y Eje Formativo | Horas Teoría | Horas Taller / Lab | Competencia Central a Desarrollar | Evidencia de Desempeño Principal |
| :--- | :--- | :--- | :--- | :--- |
| **Bloque: Fundamentos de IoT, Redes y Home Assistant Local**<br>Sesión 1 (4 horas) | 1.0 hr | 3.0 hrs | Desplegar la arquitectura local de Home Assistant, configurar el broker MQTT Mosquitto y asegurar la red doméstica contra accesos no autorizados. | Servidor Home Assistant operativo con broker MQTT y cliente de diagnóstico validado (&ge; 75 pts). |
| **Bloque: Microcontroladores ESP32 y Sensado Ambiental**<br>Sesión 2 (4 horas) | 1.0 hr | 3.0 hrs | Configurar el ESP32 con firmware ESPHome, calibrar sensores analógicos y digitales, y publicar telemetría en tiempo real hacia el broker. | Nodo sensor ESP32 reportando temperatura, humedad y presencia en el dashboard (&ge; 75 pts). |
| **Bloque: Actuación Segura a 120 VAC y Dispositivos Comerciales**<br>Sesión 3 (4 horas) | 1.0 hr | 3.0 hrs | Cablear relés de potencia bajo normas de seguridad eléctrica residencial Kinal e integrar módulos inteligentes comerciales (Shelly / Sonoff) sin nube. | Módulo de conmutación de cargas a 120 VAC accionado de forma manual y remota con cableado seguro (&ge; 75 pts). |
| **Bloque: Automatizaciones Avanzadas, Dashboard y Capstone**<br>Sesión 4 (4 horas) | 1.0 hr | 3.0 hrs | Construir tableros visuales ergonómicos, programar secuencias lógicas reactivas ante eventos y sustentar la estación domótica integrada. | Evaluación integrada (*Theorie und Praxis integrierende Prüfung*): defensa del proyecto Smart Room (&ge; 75 pts). |
| **TOTALES DEL PROGRAMA** | **4.0 hrs** | **12.0 hrs** | **16 horas pedagógicas intensivas presenciales en Kinal** | **Certificación Terminal de Aprobación (&ge; 75 pts)** |

---

## Recursos e Infraestructura Requeridos en Fundación Kinal

Para el desarrollo del taller presencial se requiere:
* **Infraestructura de Red:** Router Wi-Fi de alta densidad para laboratorio que permita segmentación de red local y comunicación multidifusión (mDNS) sin aislamiento de clientes.
* **Servidor Central del Laboratorio:** Instancia de Home Assistant OS corriendo sobre Mini PC, Raspberry Pi 4/5 o servidor virtual local en red, con Mosquitto Broker preconfigurado para pruebas rápidas.
* **Kits de Hardware por Estación de Trabajo:**
  * Placa de desarrollo ESP32 (NodeMCU-32S o similar con micro-USB/USB-C).
  * Sensor de temperatura y humedad relativa DHT22 / BME280.
  * Sensor de presencia humana PIR / radar mmWave (LD2410 o RCWL-0516).
  * Sensor de luminosidad fotorresistor (LDR) con divisor de tensión.
  * Módulo de relevadores de 2 o 4 canales con optoacoplador para 120 VAC / 10 A.
  * Dispositivo comercial inteligente (ej. Shelly 1 Plus o Sonoff Mini R4) para integración local sin nube.
* **Herramientas de Electricidad Residencial:**
  * Clemas o conectores de palanca WAGO 221 (2, 3 y 5 vías) para conexiones seguras sin cinta aislante improvisada.
  * Cajas de registro rectangulares y cuadradas de PVC / metal tipo chalupa.
  * Focos LED con base socket estándar E27 y cable de alimentación de 120 VAC con clavija polarizada.
  * Multímetros digitales de categoría CAT II/CAT III y alicates pelacables de precisión.
