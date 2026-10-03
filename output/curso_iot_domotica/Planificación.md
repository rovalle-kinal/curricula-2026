---
title: Planificación
created: 2026-09-19
creado: 2026-09-19
status: Propuesta
tags:
  - Kinal/IoT/Home-Automation
---
# Planificación

> [!NOTE]
> Este documento contiene la fundamentación técnica, la arquitectura de comunicaciones, los protocolos de seguridad eléctrica residencial y el marco metodológico del *Taller de Automatización Residencial e Internet de las Cosas (IoT)*.  
> Para consultar la visión general del programa y la ficha técnica institucional, dirígete a [[Índice general del programa]].  
> Para el microdiseño de las 4 sesiones presenciales y la rúbrica terminal analítica, consulta [[Secuencia didáctica]].  
> Para la propuesta de valor comercial y el temario curricular jerárquico, revisa [[Promesa de venta]].

---

## Fundamentación Técnica: Nube Comercial vs. Domótica Local Soberana

La automatización residencial convencional se sustenta en ecosistemas comerciales propietarios basados en la nube (Tuya, SmartLife, eWeLink, Sonoff Cloud, Tuya Cloud). Aunque su configuración inicial parece sencilla, presentan debilidades críticas para el usuario profesional:

| Dimensión Operativa | Solución en Nube Comercial Propietaria | Solución Domótica Local con Home Assistant |
| :--- | :--- | :--- |
| **Privacidad de Datos** | La telemetría, horarios de estancia y hábitos de vida se transmiten a servidores extranjeros de terceros. | **100% Local:** Todos los datos, estados de sensores y contraseñas residen dentro de la red privada del hogar. |
| **Disponibilidad y Conectividad** | Si se corta el proveedor de internet (ISP) o el servidor del fabricante cae, las luces y rutinas no responden. | **Inmunidad Total:** El sistema sigue operando con total normalidad a nivel de red de área local (LAN). |
| **Latencia de Conmutación** | Alta latencia (500 ms a 3 segundos), ya que la orden viaja a la nube y retorna a la casa. | **Respuesta Instantánea (< 50 ms):** Comunicación directa por socket local sin saltos a servidores externos. |
| **Interoperabilidad Multimarca** | Ecosistemas cerrados (*vendor lock-in*) que obligan a usar múltiples aplicaciones móviles desconectadas. | **Plataforma Universal Abierta:** Integra en un único panel dispositivos ESP32, Shelly, Sonoff, Zigbee y Wi-Fi. |
| **Obsolescencia Programada** | Si la empresa fabricante discontinúa el servicio o cambia su política de cobro por suscripción, el hardware queda inútil. | **Soberanía Tecnológica Permanente:** Código abierto auditado con actualización continua y control total del usuario. |

---

## Arquitectura de Red y Protocolo de Comunicaciones MQTT

El núcleo de transporte ligero para el Internet de las Cosas residencial es el protocolo **MQTT (Message Queuing Telemetry Transport)**:

```text
┌───────────────────────────┐                 ┌───────────────────────────┐
│   NODO SENSOR (ESP32)     │                 │   ACTUADOR (SHELLY / RELÉ)│
│  (Mide temperatura / PIR) │                 │   (Enciende lámpara 120V) │
└─────────────┬─────────────┘                 └─────────────▲─────────────┘
              │ Publica (PUBLISH)                           │ Se suscribe (SUBSCRIBE)
              ▼                                             │
┌───────────────────────────────────────────────────────────┴─────────────┐
│                      BROKER MQTT LOCAL (MOSQUITTO)                      │
│                  Tópico: "hogar/habitacion/luz/estado"                  │
└───────────────────────────────────────────────────────────▲─────────────┘
                                                            │ Control / Estado
                                                            ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                    SERVIDOR LOCAL HOME ASSISTANT                        │
│                (Automatizaciones, Dashboard y Lógica)                   │
└─────────────────────────────────────────────────────────────────────────┘
```

### Principios Operativos del Protocolo MQTT
* **Modelo Publicador / Suscriptor (*Pub/Sub*):** Los clientes (sensores y actuadores) no se comunican directamente entre sí, sino que publican mensajes en un intermediario central denominado **Broker (Eclipse Mosquitto)**.
* **Jerarquía de Tópicos (*Topics*):** Estructura semántica organizada por barras inclinadas que facilita el enrutamiento:
  * Telemetría de sensores: `hogar/sala/sensor_clima/temperatura`
  * Comandos de control: `hogar/sala/luz_techo/set` (con carga `ON` o `OFF`)
  * Estado real del actuador: `hogar/sala/luz_techo/state`
* **Calidad de Servicio (QoS):**
  * `QoS 0` (Como máximo una vez): Envío rápido sin acuse de recibo (ideal para lecturas periódicas de temperatura cada 30 segundos).
  * `QoS 1` (Al menos una vez): Envío con acuse de recibo obligatorio (adecuado para alarmas de intrusión o accionamiento de cerraduras).
* **Cargas Útiles Formateadas en JSON:** Empaquetado de múltiples variables en una sola trama para optimizar el ancho de banda del microcontrolador:
  `{"temperatura": 22.4, "humedad": 58.2, "presencia": true, "voltaje": 121.8}`

---

## Hardware Embebido: Microcontroladores ESP32 y Firmware ESPHome

El microcontrolador **ESP32** (SoC de Espressif Systems) constituye la unidad modular de cómputo físico predilecta para proyectos domóticos por su costo accesible, conectividad integrada y amplia versatilidad:

### Especificaciones Técnicas del ESP32
* Procesador dual-core Xtensa LX6 de 32 bits a 240 MHz.
* Conectividad inalámbrica Wi-Fi 802.11 b/g/n (2.4 GHz) y Bluetooth v4.2 BR/EDR y BLE.
* Pines de propósito general (GPIO) con soporte para interrupciones externas, canales PWM (modulación por ancho de pulsos para atenuación de luces LED) y convertidores analógico-digitales (ADC) de 12 bits.
* Modo de bajo consumo (*Deep Sleep*) con temporizador interno para sensores a batería.

### Ecosistema de Programación: ESPHome vs. C++ Tradicional
* **ESPHome (Enfoque Declarativo):** Sistema que compila firmware nativo para ESP32 a partir de un archivo de configuración en formato YAML.
  * Ventajas: Autodescubrimiento automático en Home Assistant mediante protocolo cifrado nativo, actualización de firmware por aire (**OTA - Over-The-Air**), nula necesidad de escribir líneas repetitivas de código en C++ para gestionar reconexiones de Wi-Fi o búferes MQTT.
* **C++ Nativo (Arduino IDE / PlatformIO):** Utilizado para aplicaciones personalizadas donde se requiere control directo de periféricos, algoritmos de filtrado digital de señales o protocolos propietarios.

---

## Seguridad Eléctrica y el Criterio Kinal del "Trabajo Bien Hecho"

La domótica implica necesariamente la interfaz entre circuitos de bajo voltaje (3.3 VDC / 5 VDC) y circuitos de potencia residencial en corriente alterna (**120 VAC / 60 Hz** en Guatemala). La seguridad personal y patrimonial es un valor ético inmutable en Fundación Kinal:

### Normas de Conexión y Montaje Residencial Seguro
* **Aislamiento Galvánico:** Uso estricto de módulos de relevadores optoacoplados. La pista de cobre de 120 VAC debe mantener una distancia de fuga (*creepage distance*) mínima de 3 mm respecto al plano de tierra de 3.3 VDC del microcontrolador.
* **Prohibición de Empalmes Improvisados:** Queda terminantemente prohibido entorchar cables de cobre con alicates y cubrirlos con cinta aislante tradicional en cajas de registro empotradas. Se exige el uso de **conectores de resorte y palanca WAGO 221**, garantizando presión constante, resistencia ante variaciones térmicas y cero riesgo de arco eléctrico.
* **Identificación Polarizada:**
  * Conductor de Fase (Línea Viva): Aislante de color negro o rojo. Debe pasar siempre por el interruptor y por el contacto común del relé. **Jamás se conmuta el neutro**.
  * Conductor Neutro: Aislante de color blanco. Conecta directo a la carga (socket de la bombilla).
  * Conductor de Puesta a Tierra: Aislante de color verde o cable de cobre desnudo, fijado a la estructura metálica de cajas y chasises.
* **Protección contra Cargas Inductivas:** Al conectar ventiladores o extractores (motores monofásicos de inducción), el rebote inductivo al desconectar la bobina genera arcos eléctricos que dañan los platinos del relé. Es mandatorio el uso de redes amortiguadoras snubber RC (resistor de 100 Ω en serie con capacitor de 0.1 µF / 400 V) o varistores de óxido metálico (MOV) en paralelo con los contactos.

---

## Arquitectura de Home Assistant y Motor de Automatizaciones

### Jerarquía de Abstracción en Home Assistant
* **Dispositivo (*Device*):** La placa física completa (ej. "Nodo Sensor ESP32 Dormitorio").
* **Entidad (*Entity*):** Cada punto individual de datos o control ofrecido por el dispositivo:
  * `sensor.temperatura_dormitorio` (valor numérico flotante en °C).
  * `binary_sensor.presencia_dormitorio` (estado booleano: `on` / `off`).
  * `switch.rele_lampara` (actuador conmutador: `turn_on` / `turn_off`).
  * `light.tira_led_sala` (luminaria con brillo y color regulable).

### Estructura del Motor Lógico de Automatización (ECA)
Las automatizaciones operan bajo el estándar universal **Disparador - Condición - Acción (Trigger - Condition - Action)**:

```text
┌────────────────────────────────────────────────────────┐
│ DISPARADOR (TRIGGER)                                   │
│ ¿Cuándo se evalúa la regla?                            │
│ Ej: "El sensor de presencia detecta movimiento"        │
└───────────────────────────┬────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────┐
│ CONDICIÓN (CONDITION)                                  │
│ ¿Bajo qué circunstancias se permite continuar?         │
│ Ej: "Solo si la luminosidad ambiental < 50 lux"       │
│     "Y la hora actual está entre 18:00 y 06:00"        │
└───────────────────────────┬────────────────────────────┘
                            │  Sí se cumplen todas
                            ▼
┌────────────────────────────────────────────────────────┐
│ ACCIÓN (ACTION)                                        │
│ ¿Qué debe ejecutar el sistema?                         │
│ Ej: "Encender la luz de cortesía al 30% de brillo"     │
│     "Esperar 3 minutos sin movimiento y apagar"        │
└────────────────────────────────────────────────────────┘
```

### Diseño de Cuadros de Mando Visuales (Lovelace UI)
* Interfaz táctil reactiva adaptativa a smartphones, tablets empotradas en pared y pantallas de ordenador.
* Tarjetas de estado (*State Cards*), tarjetas de control de termostato, tarjetas de botones con confirmación táctil y tarjetas condicionales que solo se muestran cuando ocurre una anomalía (ej. alerta de puerta abierta o fuga de agua).
