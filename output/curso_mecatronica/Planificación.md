---
title: Planificación
created: 2026-09-19
creado: 2026-09-19
status: Propuesta
tags:
  - Kinal/Mechatronics/Industrial
---
# Planificación

> [!NOTE]
> Este documento contiene la fundamentación técnica, la arquitectura de hardware/software, los protocolos de seguridad industrial y el marco metodológico del *Curso Presencial de Mecatrónica Industrial*.  
> Para consultar la visión panorámica del programa y la ficha técnica institucional, dirígete a [[Índice general del programa]].  
> Para la dosificación por momentos didácticos de taller y la rúbrica terminal analítica, consulta [[Secuencia didáctica]].  
> Para la propuesta de valor comercial y el temario curricular jerárquico, revisa [[Promesa de venta]].

---

## Fundamentación Técnica y Sinergia Mecatrónica

La mecatrónica no es una simple yuxtaposición de componentes mecánicos y electrónicos, sino la **integración sinérgica en tiempo real** de cuatro subsistemas interdependientes:

```text
       ┌───────────────────────────────┐
       │   SUBSISTEMA MECÁNICO-FLUIDO  │
       │ (Cilindros, Actuadores, Guías)│
       └──────────────┬────────────────┘
                      │ Fuerza / Movimiento
                      ▼
┌──────────────────────────────────────────────┐
│       SUBSISTEMA DE SENSADO Y SEÑALES        │
│ (Inductivos, Ópticos, Reed Switches, PNP/NPN)│
└─────────────────────┬────────────────────────┘
                      │ Señal eléctrica (24 VDC)
                      ▼
┌──────────────────────────────────────────────┐
│       SUBSISTEMA DE CONTROL INTELIGENTE      │
│  (Siemens S7-1200, TIA Portal, Lógica KOP)   │
└─────────────────────┬────────────────────────┘
                      │ Salida de conmutación
                      ▼
┌──────────────────────────────────────────────┐
│     SUBSISTEMA DE ACCIONAMIENTO Y POTENCIA   │
│ (Electroválvulas 5/2, Variador VFD, Motores) │
└──────────────────────────────────────────────┘
```

El proceso didáctico capacita al estudiante para diagnosticar y articular cada eslabón de esta cadena sin crear cuellos de botella entre disciplinas.

---

## El Principio del "Trabajo Bien Hecho" en el Taller de Mecatrónica

Fiel al ideario formativo de Fundación Kinal, la destreza técnica debe manifestarse en hábitos rigurosos de orden, exactitud y pulcritud artesanal-industrial:

### Normas de Cableado y Montaje de Tableros Eléctricos
* **Cero hilos sueltos:** Queda terminantemente prohibido insertar hilos de cobre trenzado desnudos en las borneras de conexión. Es obligatorio el uso de casquillos de compresión (*ferrules*) aislados conforme a la sección del conductor (código de colores DIN 46228-4).
* **Canalización y peinado:** Todos los conductores deben transitar ordenadamente por canaletas plásticas ranuradas con tapa. La ocupación máxima de la canaleta no superará el 70% para permitir disipación térmica y futuras ampliaciones.
* **Separación de potenciales:** Los conductores de potencia en corriente alterna (120/240 VAC para motores o alimentación de fuentes) deben tenderse con separación física estricta respecto a los cables de señales analógicas y señales digitales de 24 VDC para evitar ruidos por inducción electromagnética.
* **Rotulado e identificación alfanumérica:** Todo cable debe llevar un marbete o anillo termocontráctil legible en ambos extremos con su código identificador, coincidiendo exactamente con el plano esquemático elaborado bajo norma **IEC 60617 / IEC 81346** (ej. `-1B1` para sensor magnético, `-1Y1` para solenoide, `+24V` y `0V` para barras de potencial).

### Criterios de Instalación Neumática Impecable
* **Corte a escuadra (90°):** Los tubos flexibles de poliuretano (PU de 4 mm y 6 mm) deben seccionarse utilizando exclusivamente herramientas especiales de corte tipo guillotina. El uso de tijeras o cuchillas inclinadas daña el labio de estanqueidad y genera microfugas de aire comprimido.
* **Inserción al tope en racores rápidos:** Cada tramo de manguera debe introducirse con firmeza hasta sentir el tope interno del racor *push-in*, seguido de una ligera tracción manual de verificación.
* **Tendido sin tensiones mecánicas:** Las mangueras neumáticas deben instalarse respetando los radios mínimos de curvatura para evitar estrangulamientos y fatiga del material durante el movimiento dinámico de actuadores.

---

## Seguridad Industrial y Gestión de Energías Peligrosas

El taller de mecatrónica combina energía eléctrica (tensión peligrosa), energía neumática (presión acumulada) y componentes en movimiento mecánico (riesgo de atrapamiento). La seguridad es un valor no negociable:

### Equipo de Protección Personal (EPP) Obligatorio en Kinal
* **Gafas de seguridad anti-impacto (ANSI Z87.1):** Uso permanente desde el ingreso al taller. Protegen ante el eventual desprendimiento de virutas, expulsión repentina de mangueras a presión o chispas por cortocircuito.
* **Calzado de seguridad dieléctrico con puntera de protección:** Obligatorio para proteger los pies de caídas accidentales de motores o herramientas pesadas, brindando además aislamiento contra descargas eléctricas accidentales.
* **Restricción de accesorios:** Prohibición absoluta de anillos, relojes, pulseras, cadenas, corbatas o mangas sueltas durante el montaje en bancos de trabajo con ejes rotativos, poleas o cilindros en operación.

### Protocolo LOTO (Lockout / Tagout) de Consignación
Antes de cualquier modificación física en el cableado o conexionado neumático de un circuito, se ejecuta el procedimiento de consignación:
1. **Notificación:** Avisar al instructor y al compañero de banco sobre el inicio de la intervención.
2. **Apagado formal:** Detener el ciclo automático desde el pulsador de parada de la máquina.
3. **Seccionamiento:** Desconectar el interruptor termomagnético principal y cerrar la válvula manual de cierre de la unidad FRL.
4. **Disipación de energía residual:** Accionar la válvula de purga para descargar el aire comprimido remanente en las líneas y verificar en el manómetro que la presión marque exactamente **0 bar**. Medir con multímetro la ausencia de tensión en los bornes principales.
5. **Bloqueo y etiquetado:** Colocar candado de seguridad y tarjeta de señalización con los datos del aprendiz responsable.

---

## Arquitectura Instrumental y Tecnológica del Laboratorio

### Subsistema de Actuación Neumática y Electroneumática
* **Unidad de Mantenimiento (FRL):** Filtro de 5 micras con purga automática, regulador de presión con manómetro calibrado a **6 bar** de presión de trabajo y lubricador de micro-niebla (o bypass para líneas de mando sin lubricación).
* **Cilindros neumáticos:** Actuadores lineales de doble efecto equipados con amortiguación neumática regulable en ambos extremos y émbolos magnéticos para detección de posición por sensores exteriores.
* **Válvulas direccionales:**
  * Válvula 5/2 monoestable con solenoide de 24 VDC y retorno por resorte mecánico (posición de reposo definida).
  * Válvula 5/2 biestable con doble solenoide de 24 VDC (memoria neumática de posición).
  * Válvula 5/3 con centro cerrado para paradas intermedias de seguridad.

### Subsistema de Sensado Industrial e Instrumentación
* **Sensores de posición de vástago:** Interruptores de lengüeta magnética (*reed switches*) y sensores de estado sólido magnetorresistivos fijados en las ranuras en T del cilindro.
* **Sensores de proximidad:**
  * *Inductivos:* Detección exclusiva de piezas metálicas ferrosas y no ferrosas (cobre, aluminio) mediante la variación del campo electromagnético de alta frecuencia.
  * *Capacitivos:* Detección de materiales dieléctricos y no metálicos (plásticos, líquidos, madera, vidrio).
  * *Ópticos:* Sensores tipo réflex con espejo catadióptrico, de barrera emisor-receptor para largas distancias, y sensores difusos con ajuste de sensibilidad para discriminación de color.
* **Topologías de salida eléctrica:**
  * *Salida PNP (Carga a común 0 VDC):* El sensor conmuta el terminal positivo (+24 VDC) hacia la entrada del PLC (*Sourcing Output*). Estándar europeo preferido en la industria guatemalteca.
  * *Salida NPN (Carga a común +24 VDC):* El sensor conmuta la masa o tierra (0 VDC) hacia la entrada del PLC (*Sinking Output*).

### Subsistema de Control: PLC Siemens SIMATIC S7-1200
* **Unidad Central de Proceso (CPU 1214C DC/DC/DC):**
  * Alimentación: 24 VDC nominal.
  * Entradas digitales: 14 entradas integradas a 24 VDC tipo Sink/Source (`%I0.0` a `%I1.5`).
  * Salidas digitales: 10 salidas integradas a transistor de 24 VDC / 0.5 A (`%Q0.0` a `%Q1.1`).
  * Entradas analógicas: 2 canales de 0 a 10 VDC (`%IW64`, `%IW66`).
  * Puerto de comunicación: Interfaz integrada PROFINET (Ethernet industrial, RJ45) con switch de 2 puertos.
* **Plataforma de Programación: TIA Portal (Totally Integrated Automation):**
  * Configuración de hardware mediante árbol de dispositivos y asignación de direcciones IP fijas.
  * Tabla de variables estándar con nemónicos claros (ej. `Sensor_Inicio_1B1`, `Motor_Banda_Q0`, `Pulsador_Marcha_S1`).
  * Estructuración modular del programa: Bloque de Organización principal (`OB1`), Funciones lógicas (`FC`) para rutinas de mando y Bloques de Función (`FB`) con Bloques de Datos de instancia (`DB`) para parámetros y recetas.
  * Lógica Ladder / Esquema de Contactos (KOP) y Diagrama de Bloques (FUP) respetando la norma internacional **IEC 61131-3**.

### Subsistema de Variación de Frecuencia y Motores
* **Variador de Frecuencia (VFD):** Convertidor de frecuencia industrial monofásico a trifásico (ej. Siemens Sinamics V20 de 0.37 kW).
* **Parámetros fundamentales:**
  * Frecuencia base (60 Hz) y tensión nominal del motor.
  * Rampas de aceleración (arranque progresivo sin choque mecánico) y deceleración (frenado controlado).
  * Modos de control: Control escalar V/f lineal para bandas transportadoras.
  * Cableado de control: Borne digital de marcha adelante (DI1), marcha reversa (DI2), selección de velocidades fijas (DI3) y consigna continua de velocidad mediante potenciómetro externo de 10 kΩ conectado a la entrada analógica AI1.

### Subsistema de Interfaz Hombre-Máquina (HMI)
* **Panel de Operador:** Pantalla táctil Siemens HMI KTP400 Basic (o estación de simulación en PC vía TIA Portal WinCC Runtime).
* **Funcionalidades maquetadas:**
  * Pantalla de sinóptico de proceso: Representación gráfica de la celda de manufactura con lámparas dinámicas de animación de estado (verde = activo, gris = reposo, rojo = falla).
  * Panel de mando manual: Botones virtuales de jog (avance por pasos) para cada actuador neumático y motor.
  * Registro de alarmas: Visualización de eventos de disparo térmico, caída de presión o parada de emergencia activa.
  * Contador numérico de piezas clasificadas y selector de velocidad de línea.

---

## Metodología de Diagnóstico Sistemático (Troubleshooting Mecatrónico)

Uno de los mayores valores añadidos del técnico formado en Kinal es su capacidad de resolver problemas de forma analítica, erradicando el empirismo ciego:

```text
[AVERÍA EN CELDA MECATRÓNICA]
               │
               ▼
[FASE 1: VERIFICACIÓN DE SUMINISTROS BÁSICOS]
¿Hay 24 VDC en la fuente conmutada? ¿El manómetro marca 6 bar?
               │  Sí
               ▼
[FASE 2: AISLAMIENTO POR NIVELES TECNOLÓGICOS]
¿El vástago mecánico se mueve libremente a mano sin atascarse?
               │  Sí
               ▼
[FASE 3: INSPECCIÓN DE SEÑALES DE ENTRADA (SENSADO)]
¿El LED del sensor enciende al detectar la pieza?
¿El LED de la entrada correspondiente en el PLC (%I0.x) conmuta físicamente?
               │  Sí
               ▼
[FASE 4: AUDITORÍA DE LÓGICA DE PROGRAMA (PLC EN LÍNEA)]
Monitorear con TIA Portal: ¿Se cumple la condición lógica en el peldaño Ladder?
¿La bobina de salida del PLC (%Q0.x) está energizada en el software y en el hardware?
               │  Sí
               ▼
[FASE 5: INSPECCIÓN DE CADENA DE ACTUACIÓN FINAL]
¿Llegan 24 VDC a los bornes del conector de la electroválvula?
¿El LED del conector brilla? ¿El piloto manual de la válvula acciona el cilindro?
               │
               ▼
[LOCALIZACIÓN Y REEMPLAZO DEL COMPONENTE DEFECTUOSO]
```

Esta metodología de 5 niveles garantiza que el estudiante identifique la raíz de una falla industrial en minutos, protegiendo los equipos y optimizando la productividad de la planta.
