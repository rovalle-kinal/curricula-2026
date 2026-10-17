# Auditoría y Revisión Curricular: CAD para Topografía (Autodesk Civil 3D)

**Institución:** Fundación Kinal — Escuela Técnica Superior (ETS)  
**Programa Formativo:** CAD para Topografía y Diseño de Infraestructura  
**Software Oficial:** Autodesk Civil 3D 2026 • Autodesk ReCap Pro • Dynamo for Civil 3D  
**Duración Total:** 90 Horas Lectivas (20 Sesiones Prácticas de 4.5 Horas)  
**Modalidad:** Presencial en Laboratorio Especializado con Instrumental de Campo (Estación Total, GPS y Drones)  
**Umbral Mínimo Aprobatorio:** 75 puntos sobre 100  
**Nivel Marco de Cualificaciones:** DQR Nivel 4 - 5  

---

## 1. Justificación Pedagógica y Diagnóstico de Demanda en Guatemala (2025–2026)

La auditoría del temario anterior de Autodesk Civil 3D (basado en la ficha original `2026_Civil 3D.xlsx`) evidenció tres brechas críticas frente a las exigencias de la industria guatemalteca:

1. **Adopción Obligatoria del Sistema de Coordenadas GTM:**  
   Históricamente, los ejercicios utilizaban sistemas locales o arbitrarios (1000, 1000). Actualmente, el **Registro de Información Catastral (RIC)**, las municipalidades del departamento de Guatemala y el **Instituto Geográfico Nacional (IGN)** exigen obligatoriamente planos georreferenciados en **Guatemala Transversa de Mercator (GTM)** y **WGS84 UTM (Zonas 15N y 16N)** para escrituración, licencias y desmembraciones.
2. **Alineación con la Normativa de Carreteras de la Dirección General de Caminos (DGC / SIECA):**  
   El sector vial en Guatemala exige técnicos con destreza en el cálculo y transición de peraltes en curvas horizontales, asignación de sobreanchos para camiones pesados (**C2 y articulados WB-15**) y curvas verticales simétricas parabólicas con parámetro $K$.
3. **Incorporación de Fotogrametría con Drones y Nubes de Puntos LiDAR:**  
   Los proyectos de gran extensión y topografía accidentada requieren importar y clasificar nubes de puntos densas (`.RCP`/`.RCS` vía **Autodesk ReCap**) para generar modelos digitales de terreno en minutos, superando la limitación del levantamiento tradicional a pie.

---

## 2. Resumen Cuatricolor de la Auditoría Curricular

* 🟢 **Temas a Mantener (19 Temas):** Núcleo sólido de agrimensura, importación de puntos COGO (`PNEZD`), triangulación de superficies TIN, curvas de nivel, líneas de rotura (*Breaklines*), trazo de alineamientos, perfiles rápidos, subensamblajes y redes por gravedad.
* 🟡 **Temas a Actualizar (15 Temas):** Georreferenciación formal en GTM, cálculo de sobreanchos y peraltes DGC, rasantes con parámetro $K$, diagramas de masas con factor de abundamiento/esponjamiento de suelos locales, formatos oficiales Planta-Perfil para licitaciones públicas y pozos/tuberías bajo especificaciones EMPAGUA e INFOM.
* 🔵 **Nuevas Competencias Propuestas (4 Temas):**
  1. *Nubes de puntos LiDAR y Drones (Autodesk ReCap a Civil 3D).*
  2. *Cálculo y transición automática de peraltes según normativas DGC / SIECA.*
  3. *Interoperabilidad BIM-GIS y exportación LandXML e IFC para coordinación interdisciplinaria con Revit y Navisworks.*
  4. *Delimitación de cuencas hidrológicas de captación pluvial (Catchments) con el Método Racional.*
* 🔴 **Temas a Eliminar (2 Temas Obsoletos):**
  1. *Tipos de software del mercado (teoría comercial redundante).*
  2. *Recorridos virtuales Drive en Civil 3D (herramienta obsoleta con alto consumo de recursos; se traslada a Infraworks).*

---

## 3. Estructura Modular del Pensum (90 Horas)

### Módulo 1: Fundamentos de Civil 3D, Georreferenciación y Modelado de Terreno (~22.5 Horas)
* **Logro de Aprendizaje:** Configurar el entorno de trabajo georreferenciado en GTM, importar puntos COGO de campo y modelar superficies TIN precisas con explanaciones y nubes de puntos de drones.
* **Contenidos Clave:**
  * Configuración de plantillas institucionales `.DWT` en sistema métrico.
  * Asignación de proyección **GTM** y visualización de mapas satelitales en vivo (Bing Maps).
  * Puntos COGO (`PNEZD`), grupos de puntos y estilos anotativos.
  * Superficies TIN, líneas de rotura (*Breaklines*) y delimitación de bordes (*Boundaries*).
  * Subdivisión de parcelas en urbanizaciones y cuadros de datos técnicos para el RIC.
  * Explanaciones (*Gradings*) con taludes 1:1 en corte y 1.5:1 en terraplén.
  * Procesamiento de nubes de puntos LiDAR/drones en **Autodesk ReCap Pro**.

### Módulo 2: Alineamientos Horizontales y Perfiles Longitudinales (Norma DGC/SIECA) (~22.5 Horas)
* **Logro de Aprendizaje:** Diseñar alineamientos viales bajo normativa DGC/SIECA, curvas de transición, perfiles de terreno y rasantes de diseño vial con guitarras informativas.
* **Contenidos Clave:**
  * Trazo de ejes con tangentes, puntos de inflexión (PI) y curvas circulares simples.
  * Parámetros de velocidad de diseño (40, 60, 80 km/h) y radio mínimo.
  * Curvas de transición espirales (clotoides) y sobreanchos para vehículos C2/WB-15.
  * Muestreo del perfil de terreno natural.
  * Diseño de rasantes con pendientes máximas admisibles (10%–12%) y curvas verticales parabólicas.
  * Guitarras inferiores normalizadas (cota terreno, cota rasante, corte/relleno y abscisado cada 20 m).
  * Cálculo y asistente de transición de peraltes ($e = 8\%$ y $e = 6\%$).

### Módulo 3: Corredores Viales, Secciones Transversales y Movimiento de Tierras (~22.5 Horas)
* **Logro de Aprendizaje:** Ensamblar secciones típicas de carretera, modelar corredores 3D paramétricos, cubicar tierras mediante el Diagrama de Masas y producir planos para licitaciones públicas.
* **Contenidos Clave:**
  * Ensamblajes seccionales con carpetas asfálticas, bases trituradas y cunetas tipo DGC.
  * Modelado del sólido tridimensional de carretera (*Corridor*) con objetivos de superficie (*Targets*).
  * Superficies de coronación (*Top*) y subrasante (*Datum*).
  * Líneas de muestreo (*Sample Lines*) y secciones transversales múltiples.
  * Cubicación de movimiento de tierras por el método de áreas medias y Diagrama de Bruckner (curva de masas).
  * Automatización de planos Planta-Perfil (*Plan Production*).
  * Interoperabilidad BIM-GIS: Exportación **LandXML** e **IFC** hacia Revit y Navisworks.

### Módulo 4: Redes de Tuberías por Gravedad, Drenajes y Cuencas (EMPAGUA/INFOM) (~22.5 Horas)
* **Logro de Aprendizaje:** Diseñar redes de alcantarillado pluvial y sanitario por gravedad, trazar perfiles hidráulicos de tuberías y verificar pendientes mínimas de escorrentía.
* **Contenidos Clave:**
  * Creación de catálogo de piezas normalizadas en Guatemala (pozos de 1.20 m y tubería PVC Novafort).
  * Trazo en planta de redes de alcantarillado pluvial y sanitario con sentido de flujo.
  * Perfiles longitudinales de tuberías con colchón mínimo de protección (FHA) y pendientes de autolimpieza ($0.5\%$ a $2\%$).
  * Tablas automáticas de pozos: Cota de tapadera, cota de inversión y diámetros.
  * Detección de interferencias físicas entre tuberías y cruces de servicios.
  * Delimitación de cuencas hidrológicas de captación (*Catchments*) y cálculo de gasto por el Método Racional.

---

## 4. Dosificación Didáctica y Esquema de Evaluación (20 Sesiones)

| Sesión | Módulo | Tema Principal | Actividad Práctica de Cómputo | Ponderación |
| :---: | :---: | :--- | :--- | :---: |
| **S-01** | M1 | Entorno Civil 3D y Proyección GTM / WGS84 | Asignación de GTM y comprobación con mapas Bing en vivo | 3 pts |
| **S-02** | M1 | Puntos COGO (`PNEZD`) e Importación Masiva | Importación de levantamiento real de 400 puntos de campo | 3 pts |
| **S-03** | M1 | Superficies TIN y Líneas de Rotura (*Breaklines*) | Modelado de terreno con quiebres de talud y fondo de quebrada | 4 pts |
| **S-04** | M1 | Subdivisión de Parcelas (*Sites*) y Tablas RIC | Lotificación automática de 12 predios con cuadro de rumbos | 4 pts |
| **S-05** | M1 | Explanaciones (*Gradings*) y Nubes LiDAR/ReCap | Plataforma nivelada e importación de nube de puntos de dron | **10 pts (Proj 1)** |
| **S-06** | M2 | Alineamiento Horizontal bajo Norma DGC/SIECA | Eje vial de 1.5 km con radio mínimo para velocidad de 60 km/h | 3 pts |
| **S-07** | M2 | Curvas Clotoides y Sobreanchos para Camiones | Inserción de espirales y sobreanchos para vehículo C2 | 4 pts |
| **S-08** | M2 | Perfil Altimétrico y Rasante Vertical (Parámetro $K$) | Trazo de rasante respetando pendientes máximas admisibles | 4 pts |
| **S-09** | M2 | Guitarras Inferiores de Perfil (Norma DGC) | Configuración de bandas informativas completas | 4 pts |
| **S-10** | M2 | Cálculo y Transición Automática de Peraltes | Asistente de peraltes DGC con tabla $e = 8\%$ | **10 pts (Proj 2)** |
| **S-11** | M3 | Ensamblajes Seccionales Típicos y Cunetas DGC | Sección de pavimento con carpeta asfáltica y cunetas tipo "V" | 3 pts |
| **S-12** | M3 | Modelado 3D de Corredores Viales (*Corridors*) | Sólido vial paramétrico vinculado a la superficie de terreno | 4 pts |
| **S-13** | M3 | Superficies Top/Datum y Líneas de Muestreo | Muestreo transversal cada 20 m en tangentes y 10 m en curvas | 4 pts |
| **S-14** | M3 | Secciones Transversales y Cubicación de Tierras | Reporte de áreas medias con esponjamiento de suelo local | 4 pts |
| **S-15** | M3 | Diagrama de Bruckner y Láminas Planta-Perfil | Balance económico de tierras y juego de planos de licitación | **10 pts (Proj 3)** |
| **S-16** | M4 | Catálogo de Piezas EMPAGUA/INFOM (Pozos y PVC) | Configuración de lista de piezas con pozos de 1.20 m | 3 pts |
| **S-17** | M4 | Trazado en Planta de Redes Pluviales y Sanitarias | Conexión de pozos y tragantes en cruces de calles | 4 pts |
| **S-18** | M4 | Perfiles de Tuberías y Cotas de Inversión | Ajuste de rasantes de fondo con colchón FHA | 4 pts |
| **S-19** | M4 | Delimitación de Cuencas (*Catchments*) y Cruces | Detección de interferencias y gasto pluvial | 4 pts |
| **S-20** | M4 | **Proyecto Integrador Final y Defensa Técnica** | Entrega y defensa de proyecto vial + topografía + drenaje | **15 pts (Final)** |

* **Total de Puntos:** 100 Puntos.
* **Nota Mínima de Aprobación:** **75 Puntos**.

---

## 5. Innovación con Inteligencia Artificial

1. **Clasificación Automática de Nubes de Puntos con IA:**  
   Uso de redes neuronales convolucionales en **Autodesk ReCap AI** y **CloudCompare** para aislar automáticamente vegetación, cableado y edificaciones, dejando la superficie de suelo desnudo (*Bare Earth*) lista para modelar en Civil 3D.
2. **Optimización Generativa de Explanaciones (*Autodesk Grading Optimization*):**  
   Algoritmo genético que evalúa millones de pendientes para determinar la plataforma que logra balance cero de corte y relleno, reduciendo acarreos y costos.
3. **Automatización con Dynamo for Civil 3D:**  
   Scripts visuales para estacado automático, colocación de postes de iluminación y reportes instantáneos de cotas en hojas Excel.

---

## 6. Enlaces de Acceso y Navegación en el Ecosistema

* **Página de Auditoría Dedicada:** [`cad_topografia_auditoria.html`](file:///Users/arqovalle/Library/CloudStorage/OneDrive-Personal/Software/Antigravity/Diseño%20Instruccional/cad_topografia_auditoria.html)
* **Portal del Área de Construcción:** [`construccion.html`](file:///Users/arqovalle/Library/CloudStorage/OneDrive-Personal/Software/Antigravity/Diseño%20Instruccional/construccion.html)
* **Portal Maestro Kinal 2026:** [`index.html`](file:///Users/arqovalle/Library/CloudStorage/OneDrive-Personal/Software/Antigravity/Diseño%20Instruccional/index.html)
