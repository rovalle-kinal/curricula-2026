# Auditoría y Revisión Curricular: Automatización Industrial (180 Horas)

**Institución:** Fundación Kinal — Escuela Técnica Superior (ETS)  
**Programa Formativo:** Carrera Técnica en Automatización Industrial y Redes  
**Acreditación:** Diploma de Técnico en Automatización Industrial (Avalado por Universidad del Istmo - UNIS)  
**Duración Total:** 180 Horas Lectivas (6 Módulos de 30 Horas)  
**Modalidad:** Híbrida / Presencial en Talleres de Automatización y Laboratorios de Control Industrial  
**Umbral Mínimo Aprobatorio:** 75 puntos sobre 100  
**Nivel Marco de Cualificaciones:** DQR Nivel 5 – 6  

---

## 1. Justificación Pedagógica y Diagnóstico de Demanda 2027

La modernización del pensum de **Automatización Industrial** (Expediente Técnico `2026_AIM.xlsx`) responde a las necesidades reales de los sectores de manufactura, alimentos y bebidas, energía y agroindustria en Guatemala:

1. **Alineación con la Norma Internacional IEC 61131-3:**  
   Estandarización de lenguajes de programación industrial: LADDER (diagrama de contactos), FBD (bloques funcionales), SFC / S7-GRAPH (diagramas funcionales secuenciales) y SCL / ST (texto estructurado) para garantizar la portabilidad y diagnóstico rápido de código en piso de planta.
2. **Reubicación de Instrumentación y Lazo Cerrado PID:**  
   El Módulo 1 se enfoca rigurosamente en mando electromagnético, protecciones, simbología y diagnóstico de fallas cableadas. Los lazos de control PID y transmisores inteligentes HART se trasladan formalmente al Módulo 2 (Instrumentación Industrial), donde se cuenta con la base física y matemática necesaria.
3. **Descarte Técnico de Arduino para Adquisición de Datos (DAQ):**  
   Se tacha de manera explícita el uso de placas de desarrollo genéricas (Arduino) en adquisición de datos industriales debido a la falta de aislamiento galvánico, nula inmunidad al ruido electromagnético y ausencia de homologación industrial, reemplazándolo por módulos DAQ didácticos (LabVIEW) y tarjetas I/O analógicas de PLC.
4. **Incorporación de Industria 4.0, Redes de Campo e IIoT:**  
   Ampliación hacia protocolos estándar de interoperabilidad IT/OT: servidores OPC UA, telemetría ligera mediante brokers MQTT, supervisión SCADA con Ignition / WinCC y almacenamiento histórico en bases de datos relacionales SQL.

---

## 2. Matriz Ejecutiva de Modificaciones (Criterio 2027 y Ampliaciones Condicionadas)

| Módulo | Enfoque Núcleo 2027 | Ampliación Condicionada | Estado Curricular |
| :--- | :--- | :--- | :--- |
| **1. Lógica Cableada** | Mando, protección, simbología, simulación, diagramas y fallas. Lazo abierto/cerrado introductorio. | PID y HART especializados fuera de este módulo. | 🟢 12 Mantener<br>🟡 1 Actualizado (Gris)<br>🔴 1 Tachado (Reubicado)<br>🔵 1 Nuevo (Azul) |
| **2. Instrumentación** | Sensores, señales 0–10 V y 4–20 mA, escalamiento, LabVIEW y adquisición didáctica. | Transmisores HART, calibración y banco PID. | 🟢 11 Mantener<br>🟡 4 Actualizados (Gris)<br>🔴 1 Tachado (Arduino DAQ)<br>🔵 2 Nuevos (Azul) |
| **3. PLC Combinacional** | Ladder, direccionamiento, temporizadores, contadores, enclavamientos y diagnóstico. | Nuevas plataformas bajo esquema de licencias. | 🟢 11 Mantener<br>🟡 5 Actualizados (Gris)<br>🔵 1 Nuevo (Azul) |
| **4. PLC Secuencial** | GRAFCET/conceptos de estados, secuencias, transiciones, pruebas, diagnóstico y proyecto. | S7-GRAPH/SCL y redes avanzadas. | 🟢 8 Mantener<br>🟡 4 Actualizados (Gris)<br>🔵 2 Nuevos (Azul) |
| **5. Relés Industriales** | LOGO! como controlador, FBD/UDF, analógica, Ethernet y LWE; prácticas por estaciones. | Más unidades físicas e instrumentación. | 🟢 5 Mantener<br>🟡 5 Actualizados (Gris)<br>🔴 1 Tachado (Duplicado)<br>🔵 1 Nuevo (Azul) |
| **6. Redes e IIoT** | Direcciones IP, intercambio de variables y una supervisión final operativa en Node-RED. | MQTT, OPC UA, SCADA, SQL y redes avanzadas. | 🟡 5 Actualizados (Gris)<br>🔵 2 Nuevos (Azul) |

* **Total de Temas Auditados:** 77 Temas.
* **Resumen Cuatricolor:** 🔴 3 Tachados (sin borrar) • 🟡 22 En Gris (Actualizados 2027) • 🔵 8 En Azul (Nuevos / Ampliación condicionada) • 🟢 44 En Verde (Mantenidos).

---

## 3. Temario Oficial en 2 Columnas

### BLOQUE A: LÓGICA CABLEADA E INSTRUMENTACIÓN (SEMANAS 1 A 14)

| MÓDULO 1: LÓGICA CABLEADA (~30 Horas) | MÓDULO 2: INSTRUMENTACIÓN INDUSTRIAL (~30 Horas) |
| :--- | :--- |
| **Logro:** Diseñar, simular, ensamblar y diagnosticar tableros de control con mando electromagnético y protecciones normalizadas. | **Logro:** Calibrar sensores y acondicionadores analógicos (0–10V, 4–20mA), virtualizar con LabVIEW e integrar instrumentación inteligente. |
| 🟢 Introducción a la automatización industrial | 🟡 *[En Gris]* Introducción a la instrumentación industrial y metrología |
| 🟡 *[En Gris]* Sistemas de control (lazo abierto y lazo cerrado introductorio) | 🟢 Variables de proceso industrial (presión, nivel, flujo, temperatura) |
| 🔴 *~~PID y calibración de campo HART especializados~~* *(Excluido de este módulo; trasladado a Módulo 2)* | 🟡 *[En Gris]* Sensores análogos y digitales (señales estándar 0–10 V y 4–20 mA) |
| 🟢 Aparatos de maniobra (contactores, relés, pulsadores, selectores) | 🟢 Acondicionadores de señal y transmisores de 2 y 4 hilos |
| 🟢 Medidas de protección (disyuntores, guardamotores, relés térmicos) | 🟢 Interpretación de hojas técnicas de sensores y diagramas P&ID (ISA 5.1) |
| 🟢 Comités de normalización y seguridad eléctrica (IEC 60947, NFPA 70E) | 🟡 *[En Gris]* Escalamiento matemático y calibración de sensores ($y = mx + b$) |
| 🟢 Simbología normalizada IEC y NEMA | 🟢 Configuración física y conexionado de sensores en campo (shielding) |
| 🟢 Automatismos de lógica cableada básica y enclavamientos | 🟡 *[En Gris]* Virtualización de instrumentos con LabVIEW y adquisición didáctica (DAQ) |
| 🟢 Automatismos de lógica programable (introductorio) | 🟢 Programación G para instrumentación y panel frontal |
| 🟢 Interpretación y representación de diagramas unifilares y multifilares | 🟢 Arreglos, clusters y manejo de tipos de datos en adquisición |
| 🟢 Herramientas de simulación y diseño de paneles (CADe_SIMU / PC_SIMU) | 🟢 Estructuras y elementos de programación (While, For, Case) |
| 🟢 Simulación de automatismos de lógica cableada | 🟢 Funciones básicas y avanzadas de filtrado de señal |
| 🟢 Dibujo CAD básico - integración de paneles eléctricos en riel DIN | 🔴 *~~Integración de instrumentos a ARDUINO como DAQ~~* *(Tachado: Desaconsejado industrialmente; sustituido por DAQ didáctico y PLC)* |
| 🔵 **[NUEVO 2027] Diagnóstico sistemático y localización de fallas en diagramas y tableros** | 🟢 Visualización de variables de proceso industrial y conectividad |
| — | 🟢 Data Dashboard para monitoreo gráfico de instrumentación |
| — | 🔵 **[AMPLIACIÓN 2027] Transmisores inteligentes con protocolo HART y calibración de campo** |
| — | 🔵 **[AMPLIACIÓN 2027] Control de procesos en lazo cerrado PID y banco didáctico de calibración de presión y nivel** |

---

### BLOQUE B: CONTROLADORES LÓGICOS PROGRAMABLES (SEMANAS 15 A 28)

| MÓDULO 3: PROGRAMACIÓN COMBINACIONAL DE PLC (~30 Horas) | MÓDULO 4: PROGRAMACIÓN SECUENCIAL DE PLC (~30 Horas) |
| :--- | :--- |
| **Logro:** Programar e interconectar PLCs bajo lenguaje Ladder IEC 61131-3, configurando hardware, temporizadores, contadores y enclavamientos. | **Logro:** Estructurar procesos industriales complejos mediante GRAFCET (IEC 60848), validar con gemelos digitales y programar secuencias en S7-GRAPH y SCL. |
| 🟢 Tecnología digital de control y arquitectura de PLC | 🟢 Pensamiento lógico secuencial aplicado a la manufactura |
| 🟡 *[En Gris]* Herramientas de programación y simulación (TIA Portal / Studio 5000) | 🟢 Introducción al control industrial secuencial y máquinas de estado |
| 🟡 *[En Gris]* Conceptos básicos de programación en lenguaje Ladder (LADDER / KOP) | 🟡 *[En Gris]* GRAFCET y Diagramas Funcionales de Secuencia (IEC 60848) |
| 🟢 Modos de operación del autómata (RUN, STOP, FAULT) y ciclo de scan | 🟢 Bloques de organización modular (OB, FB, FC y Data Blocks DB) |
| 🟡 *[En Gris]* Depuración, forzado de variables y diagnóstico de programas en línea | 🟡 *[En Gris]* Diagramación secuencial, secuencias únicas y bifurcaciones (O / Y) |
| 🟡 *[En Gris]* Tipos de datos y direccionamiento estructurado de E/S (IEC 61131-3) | 🟢 Pasos, acciones asociadas (continuas, memorizadas) y receptividades |
| 🟡 *[En Gris]* Procedimiento de apertura y configuración de hardware en PLC | 🟢 Señales de transferencia y sincronización entre subprocesos |
| 🟢 Operaciones lógicas con bits (contactos NO, NC, bobinas, flancos P/N) | 🟢 Seccionamiento del programa (control de secuencias, modos manual y auto) |
| 🟢 Enclavamientos lógicos por software y eléctricos para seguridad | 🟢 Secciones independientes: tratamiento de alarmas y paros de emergencia |
| 🟢 Paro de proceso vs paro de emergencia (ISO 13850) | 🟢 Lectura y escalamiento de variables análogas en el ciclo secuencial |
| 🟢 Optimización de segmentos y buenas prácticas de diagramación | 🟡 *[En Gris]* Pruebas, simulación dinámica y diagnóstico con gemelos digitales (Factory I/O) |
| 🟢 Instrucciones de memorización Set (S) y Reset (R) | 🟢 Proyecto integrador de automatización secuencial de celda |
| 🟢 Tipos de temporizadores normalizados (TON, TOF, TP) | 🔵 **[AMPLIACIÓN 2027] Programación avanzada en S7-GRAPH (SFC) y Texto Estructurado (SCL según IEC 61131-3)** |
| 🟢 Diagramas de tiempo aplicados al control de motores | 🔵 **[AMPLIACIÓN 2027] Redes industriales avanzadas (PROFINET MRP) e integración de sensores inteligentes IO-Link** |
| 🟢 Operaciones con temporizadores combinados y cascada de tiempos | — |
| 🟢 Operación con contadores progresivos/regresivos (CTU, CTD) y comparadores | — |
| 🔵 **[AMPLIACIÓN 2027] Nuevas plataformas de PLC bajo esquema de licencias corporativas y compatibilidad multiplataforma (Siemens / Rockwell / Codesys)** | — |

---

### BLOQUE C: RELÉS INDUSTRIALES, REDES DE COMUNICACIÓN E IIOT (SEMANAS 29 A 40)

| MÓDULO 5: PROGRAMACIÓN DE RELÉS INDUSTRIALES (~30 Horas) | MÓDULO 6: REDES INDUSTRIALES E IIOT (~30 Horas) |
| :--- | :--- |
| **Logro:** Implementar aplicaciones de control con relés inteligentes LOGO!, pantallas web embebidas LWE y ampliación de unidades físicas. | **Logro:** Configurar direccionamiento IP industrial, intercambiar variables entre autómatas, desplegar supervisión en Node-RED y conectar con SCADA y bases de datos SQL. |
| 🟢 Networking local industrial y asignación de nodos | 🟡 *[En Gris]* Configuración de direcciones IP industriales y segmentación de subredes |
| 🟢 Configuración de red LAN industrial cableada para relés programables | 🟡 *[En Gris]* Intercambio de variables punto a punto y cliente-servidor (S7 / Modbus TCP) |
| 🟢 Configuración de red WLAN y routers industriales en tablero | 🟡 *[En Gris]* Supervisión final operativa mediante dashboards de monitoreo en Node-RED |
| 🟡 *[En Gris]* LOGO! como controlador de procesos y software SoftComfort v8 | 🟡 *[En Gris]* Instalación y configuración del entorno Node-RED en gateways y PCs |
| 🟡 *[En Gris]* Programación en Diagrama de Bloques (FBD) y macro-bloques (UDF) | 🟡 *[En Gris]* Comunicación bidireccional entre Node-RED y controladores industriales |
| 🟡 *[En Gris]* Manejo de señales análogas (0–10 V / 4–20 mA) en LOGO! y Ethernet | 🔵 **[AMPLIACIÓN 2027] Conectividad IIoT con brokers MQTT y servidores industriales OPC UA** |
| 🟢 Comunicación inter-controladores LOGO! (Master/Slave y Peer-to-Peer) | 🔵 **[AMPLIACIÓN 2027] Supervisión SCADA de planta (Ignition / WinCC) con registro histórico en bases de datos relacionales SQL y redes avanzadas** |
| 🟢 Introducción a LOGO! Web Editor (LWE) y servidor web embebido | — |
| 🟡 *[En Gris]* Integración con LWE como HMI Web responsiva para monitoreo remoto | — |
| 🟡 *[En Gris]* Aplicaciones prácticas de integración multiplataforma por estaciones | — |
| 🔴 *~~Networking local industrial (tema duplicado)~~* *(Tachado: Mantenido para trazabilidad)* | — |
| 🔵 **[AMPLIACIÓN 2027] Prácticas por estaciones con más unidades físicas de E/S e instrumentación industrial acoplada a LOGO!** | — |
