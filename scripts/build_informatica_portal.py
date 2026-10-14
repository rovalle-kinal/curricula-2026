#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador Maestro del Catálogo de Pensum CET y Diagnóstico Curricular • Informática
Fundación Kinal • Centro Escolar Técnico (CET)
Genera pensum_data.json, index.html y README.md en rovalle-kinal.git/informatica-cet/
"""

import json
import os
import html

OUTPUT_DIR = "rovalle-kinal.git/informatica-cet"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# -------------------------------------------------------------
# 1. Dataset Completo y Curado de Informática CET (4to, 5to, 6to)
# -------------------------------------------------------------

pensum_data = {
    "cuarto_informatica": {
        "id": "cuarto_informatica",
        "title": "4to Perito en Informática",
        "subtitle": "Ciclo de Fundamentación Algorítmica, Bases de Datos y Programación Orientada a Objetos",
        "docente": "Área Técnica de Informática (Denys Orozco, Magno Solís, Kenneth Velázquez, Alvaro Calderón, Elmer Santos)",
        "horas": "30 períodos semanales (15 Tecnología + 15 Taller)",
        "bimestres": [
            {
                "bimestre_num": 1,
                "nombre": "Bimestre 1: Lógica Computacional, Algoritmia y Fundamentos de Programación",
                "temas": [
                    {
                        "nombre": "Pensamiento Computacional y Descomposición de Problemas",
                        "descripcion": "Análisis estructurado de situaciones problemáticas, descomposición modular en entradas, procesos y salidas, identificación de patrones lógicos.",
                        "estado": "adecuado",
                        "justificacion": "Competencia basal crítica requerida por la industria para la resolución metódica de requerimientos de software.",
                        "enfoque": "Modelado de problemas reales y pruebas de escritorio exhaustivas.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Diagramas de Flujo y Simbología ANSI/ISO",
                        "descripcion": "Representación gráfica de algoritmos mediante diagramas de flujo normalizados, decisiones lógicas y flujos de control.",
                        "estado": "adecuado",
                        "justificacion": "Facilita la comunicación visual de la lógica del sistema y el alineamiento con requerimientos técnicos.",
                        "enfoque": "Construcción de diagramas de flujo y verificación de caminos lógicos.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Pseudocódigo Formal y Estructuras de Control Secuenciales",
                        "descripcion": "Diseño algorítmico independiente del lenguaje mediante convenciones formales de pseudocódigo y asignación de variables.",
                        "estado": "adecuado",
                        "justificacion": "Desarrolla el razonamiento sintáctico y la abstracción previa a la codificación en compiladores reales.",
                        "enfoque": "Escritura de algoritmos legibles con validación rigurosa de secuencia.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Estructuras de Control Condicionales (if, if-else, switch-case)",
                        "descripcion": "Bifurcaciones de flujo, evaluación de expresiones booleanas, operadores lógicos (AND, OR, NOT) y condiciones anidadas.",
                        "estado": "adecuado",
                        "justificacion": "Permite implementar reglas de negocio y validación de estados requeridos en cualquier sistema empresarial.",
                        "enfoque": "Construcción y ejecución de algoritmos con múltiples caminos y casos límite.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Estructuras de Control Repetitivas (while, do-while, for)",
                        "descripcion": "Bucles iterativos, condiciones de parada, acumuladores, contadores, control de índices y prevención de bucles infinitos.",
                        "estado": "adecuado",
                        "justificacion": "Esencial para el procesamiento repetitivo de datos, registros y validaciones.",
                        "enfoque": "Resolución de problemas de iteración y cálculo numérico.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Traducción de Algoritmos a Lenguaje Java Moderno",
                        "descripcion": "Correspondencia directa entre diagrama/pseudocódigo y sintaxis Java; función main, tipos de datos primitivos y operadores nativos.",
                        "estado": "adecuado",
                        "justificacion": "Java es un lenguaje tipado estándar en el sector financiero y bancario guatemalteco que forma disciplina de tipado fuerte.",
                        "enfoque": "Compilación y ejecución en IDE moderno (IntelliJ IDEA / VS Code).",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Pruebas de Escritorio y Depuración con Breakpoints",
                        "descripcion": "Seguimiento de trazas de memoria, ejecución paso a paso (step over, step into), inspección de variables y localización de fallos.",
                        "estado": "adecuado",
                        "justificacion": "Habilidad fundamental para reducir tiempos de resolución de bugs en proyectos reales.",
                        "enfoque": "Depuración guiada con debugger del IDE en casos normales y extremos.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Buenas Prácticas de Indentación, Nomenclatura y Clean Code",
                        "descripcion": "Convenciones camelCase, nombres autoexplicativos de variables y funciones, indentación consistente y comentarios de propósito.",
                        "estado": "adecuado",
                        "justificacion": "Estándar mandatorio en equipos de desarrollo ágil para garantizar mantenibilidad.",
                        "enfoque": "Refactorización de código y revisión entre pares.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Uso Prolongado de PseInt más allá de las Primeras Semanas",
                        "descripcion": "Permanencia excesiva en entornos didácticos de pseudocódigo en español sin pasar tempranamente al lenguaje de programación real.",
                        "estado": "eliminar",
                        "justificacion": "PseInt debe limitarse a las primeras 2 semanas como andamiaje. Extenderlo retrasa la familiarización con errores de compilación, sintaxis real y el ecosistema profesional.",
                        "enfoque": "Transición temprana a Java y VS Code/IntelliJ desde la semana 3.",
                        "tipo": "obsoleto"
                    },
                    {
                        "nombre": "Control de Versiones Básico desde Bimestre 1 (git init, commit)",
                        "descripcion": "Inicialización de repositorios locales, registro de cambios mediante commits atómicos y comprensión del historial de código desde el primer programa.",
                        "estado": "propuesto",
                        "justificacion": "La industria exige que todo desarrollador junior use Git como parte de su flujo natural de trabajo diario desde el día uno.",
                        "enfoque": "Práctica de versionado de cada ejercicio y tarea en la terminal.",
                        "tipo": "propuesta"
                    }
                ]
            },
            {
                "bimestre_num": 2,
                "nombre": "Bimestre 2: Modularidad, Estructuras de Datos y Persistencia Relacional / NoSQL",
                "temas": [
                    {
                        "nombre": "Eje Transversal IA CoWork y Prompting Técnico",
                        "descripcion": "Uso de asistentes de código (Copilot, Gemini) bajo el protocolo institucional de validación humana obligatoria, trazabilidad de prompts y defensa técnica de código.",
                        "estado": "adecuado",
                        "justificacion": "Alinea a los estudiantes con las herramientas modernas de productividad requeridas por empresas globales sin perder criterio técnico.",
                        "enfoque": "Prácticas de generación y auditoría crítica de fragmentos de código.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Programación Modular: Funciones, Métodos y Ámbito de Variables",
                        "descripcion": "Descomposición funcional, paso de parámetros por valor y referencia, valores de retorno, sobrecarga de métodos y ámbito local/global.",
                        "estado": "adecuado",
                        "justificacion": "Principio esencial de reutilización y principio de responsabilidad única en funciones.",
                        "enfoque": "Creación de librerías de funciones reutilizables y pruebas unitarias básicas.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Estructuras de Datos Lineales: Arreglos y Matrices",
                        "descripcion": "Declaración, instanciación y recorrido de arreglos unidimensionales y bidimensionales; algoritmos de búsqueda lineal y ordenamiento básico.",
                        "estado": "adecuado",
                        "justificacion": "Comprensión del manejo de memoria contigua e indexación fundamental en algoritmos.",
                        "enfoque": "Manipulación de colecciones estáticas y procesamiento de tablas en memoria.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Colecciones Dinámicas en Java (ArrayList, Listas)",
                        "descripcion": "Manejo de colecciones dinámicas de objetos, adición, eliminación, filtrado e iteración mediante estructuras de Java Collections Framework.",
                        "estado": "adecuado",
                        "justificacion": "La gran mayoría de aplicaciones empresariales operan sobre colecciones dinámicas en lugar de arreglos de tamaño fijo.",
                        "enfoque": "Implementación de catálogos y listas dinámicas en memoria.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Modelado Conceptual de Datos: Diagrama Entidad-Relación (ER)",
                        "descripcion": "Identificación de entidades, atributos simples/compuestos, claves primarias, claves foráneas, relaciones y cardinalidades (1:1, 1:N, N:M).",
                        "estado": "adecuado",
                        "justificacion": "Competencia crítica para estructurar la persistencia de cualquier sistema de información corporativo.",
                        "enfoque": "Construcción de diagramas ER a partir de casos de uso y requerimientos de clientes.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Normalización de Bases de Datos Relacionales (1FN, 2FN, 3FN)",
                        "descripcion": "Reglas de normalización para eliminar redundancia de datos, evitar anomalías de inserción/actualización/borrado y garantizar integridad.",
                        "estado": "adecuado",
                        "justificacion": "Estándar de calidad indiscutible en la arquitectura de datos relacionales en la industria.",
                        "enfoque": "Transformación de hojas de cálculo desorganizadas a esquemas relacionales normalizados.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "SQL DDL y DML Fundamental (CREATE, INSERT, UPDATE, DELETE, SELECT)",
                        "descripcion": "Definición de esquemas, tipos de datos, restricciones de clave (PK, FK, UNIQUE, NOT NULL, CHECK) y manipulación transaccional básica.",
                        "estado": "adecuado",
                        "justificacion": "Habilidad universal requerida en cualquier puesto junior de soporte, calidad o desarrollo.",
                        "enfoque": "Ejecución de scripts DDL y operaciones CRUD directas en MySQL / PostgreSQL.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Consultas Relacionales con Filtros, Agregaciones y GROUP BY",
                        "descripcion": "Cláusulas WHERE, operadores lógicos y relacionales, ORDER BY, funciones de agregación (COUNT, SUM, AVG, MIN, MAX) y agrupamiento con HAVING.",
                        "estado": "adecuado",
                        "justificacion": "Esencial para la generación de reportes y consultas analíticas requeridas por la administración del negocio.",
                        "enfoque": "Resolución de requerimientos analíticos sobre bases de datos de prueba.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Fundamentos de Bases de Datos Documentales NoSQL (JSON/BSON y MongoDB)",
                        "descripcion": "Estructuras semiestructuradas, colecciones, documentos JSON/BSON, documentos embebidos vs referencias y operaciones CRUD con MongoDB Shell.",
                        "estado": "adecuado",
                        "justificacion": "Alta adopción en stacks modernos (MERN, microservicios) para datos flexibles no estrictamente tabulares.",
                        "enfoque": "Diseño de colecciones documentales y comparación de casos de uso con SQL.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Almacenamiento de Datos en Tablas Desnormalizadas sin Integridad Referencial",
                        "descripcion": "Prácticas de diseño de tablas huérfanas sin definición de foreign keys, dependencias funcionales rotas o campos multievaluados no normalizados.",
                        "estado": "eliminar",
                        "justificacion": "Genera vicios graves de diseño que provocan corrupción e inconsistencia de datos en sistemas reales.",
                        "enfoque": "Exigir llaves foráneas y constraints de integridad en todo esquema evaluado.",
                        "tipo": "obsoleto"
                    },
                    {
                        "nombre": "Persistencia Transaccional en Archivos Planos (.txt/.dat) para Sistemas Multiusuario",
                        "descripcion": "Uso de streams secuenciales de archivos de texto o binarios locales para almacenar catálogos y transacciones de negocio simuladas.",
                        "estado": "eliminar",
                        "justificacion": "Práctica desfasada que no escala a la concurrencia ni provee propiedades ACID; debe sustituirse de inmediato por motores de bases de datos relacionales o NoSQL.",
                        "enfoque": "Migrar directamente a MySQL, SQLite o PostgreSQL sin perder semanas en archivos planos.",
                        "tipo": "obsoleto"
                    },
                    {
                        "nombre": "Prevención Temprana de Inyección SQL mediante Consultas Parametrizadas",
                        "descripcion": "Demostración de vulnerabilidad por concatenación de cadenas SQL y aplicación rigurosa de PreparedStatement desde el primer enlace con BD.",
                        "estado": "propuesto",
                        "justificacion": "OWASP A03 (Injection) sigue siendo un riesgo crítico; los alumnos deben salir con el hábito inviolable del uso de consultas parametrizadas.",
                        "enfoque": "Laboratorios de seguridad defensiva y refactorización de consultas vulnerables.",
                        "tipo": "propuesta"
                    }
                ]
            },
            {
                "bimestre_num": 3,
                "nombre": "Bimestre 3: Programación Orientada a Objetos, Arquitectura en Capas y SQL Avanzado",
                "temas": [
                    {
                        "nombre": "Paradigmas de Programación: Transición de Estructurado a POO",
                        "descripcion": "Diferenciación conceptual entre enfoque procedimental y orientado a objetos; ventajas de modelar el dominio mediante entidades de software.",
                        "estado": "adecuado",
                        "justificacion": "Fundamento indispensable para la programación empresarial en Java, C#, TypeScript y Python.",
                        "enfoque": "Modelado conceptual de objetos del mundo real en clases de software.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Clases, Objetos, Estado, Comportamiento y Métodos Constructores",
                        "descripcion": "Definición de clases, instanciación en memoria, ciclo de vida del objeto, constructores por defecto y parametrizados, destructores y garbage collection.",
                        "estado": "adecuado",
                        "justificacion": "Base operativa de la POO requerida en el 100% de proyectos de software medianos y grandes.",
                        "enfoque": "Creación e interconexión de múltiples objetos en el dominio del negocio.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Pilares de POO: Encapsulamiento, Abstracción, Herencia y Polimorfismo",
                        "descripcion": "Modificadores de acceso (private, protected, public), getters/setters, jerarquías de clases (`extends`), clases abstractas, sobrescritura de métodos (`@Override`) y ligadura dinámica.",
                        "estado": "adecuado",
                        "justificacion": "Permite escribir código reutilizable, protegido y extensible según estándares de la industria.",
                        "enfoque": "Diseño de modelos polimórficos de dominio empresarial (ej. cuentas bancarias, facturación).",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Interfaces y Contratos de Software",
                        "descripcion": "Definición e implementación de interfaces (`implements`), separación entre firma y ejecución, y polimorfismo por interfaz.",
                        "estado": "adecuado",
                        "justificacion": "Base del desacoplamiento en arquitecturas modulares modernas e inyección de dependencias.",
                        "enfoque": "Implementación de interfaces para servicios y repositorios de datos.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Principios SOLID Introductorios (Principio de Responsabilidad Única - SRP)",
                        "descripcion": "Conceptos de alta cohesión y bajo acoplamiento; identificación de responsabilidades excesivas en una clase y refactorización.",
                        "estado": "adecuado",
                        "justificacion": "Criterio de ingeniería indispensable para evitar código espagueti en sistemas comerciales.",
                        "enfoque": "Auditoría de clases de más de 300 líneas y división en módulos cohesivos.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Arquitectura por Capas (Presentación, Lógica de Negocio y Datos / DAO)",
                        "descripcion": "Separación de responsabilidades: interfaz de usuario, capa de servicio con reglas de negocio y capa de acceso a datos (Data Access Object / Repository).",
                        "estado": "adecuado",
                        "justificacion": "Arquitectura estándar en proyectos Java/Spring y .NET en el mercado laboral guatemalteco.",
                        "enfoque": "Refactorización de una aplicación monolítica dividiéndola en 3 capas bien delimitadas.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Patrón de Arquitectura Modelo-Vista-Controlador (MVC)",
                        "descripcion": "Flujo de control: el controlador recibe la petición, consulta la capa de servicio/modelo y actualiza la vista correspondiente.",
                        "estado": "adecuado",
                        "justificacion": "Patrón architectural de facto en desarrollo web y de escritorio que estructura el trabajo en equipo.",
                        "enfoque": "Construcción de un CRUD completo aplicando el patrón MVC.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "SQL Avanzado: INNER JOIN, LEFT/RIGHT JOIN y Subconsultas",
                        "descripcion": "Combinación de múltiples tablas relacionales, análisis de coincidencias, producto cartesiano evitado, subconsultas en WHERE y FROM, y vistas.",
                        "estado": "adecuado",
                        "justificacion": "Pregunta mandatoria en cualquier entrevista técnica para desarrolladores junior en Guatemala.",
                        "enfoque": "Construcción de consultas complejas multi-tabla para reportes de negocio.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Transacciones ACID, Procedimientos Almacenados y Triggers",
                        "descripcion": "Propiedades ACID (Atomicidad, Consistencia, Aislamiento, Durabilidad), COMMIT, ROLLBACK, lógica en el motor de base de datos e índices.",
                        "estado": "adecuado",
                        "justificacion": "Esencial para operaciones financieras y sistemas de inventario donde las fallas parciales son inaceptables.",
                        "enfoque": "Simulación de transferencias bancarias protegidas por transacciones en SQL.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Patrones Creacionales Complejos (Abstract Factory y Builder en 4to Grado)",
                        "descripcion": "Enseñanza teórica de familias de fábricas de objetos y constructores fluidos complejos a nivel de 4to diversificado.",
                        "estado": "revisar",
                        "justificacion": "Sobrecarga cognitiva para alumnos que apenas están asimilando POO básica; se recomienda acotar el enfoque a Factory Method simple y Singleton práctico.",
                        "enfoque": "Acotar a Factory Method y Singleton antes de introducir patrones más avanzados.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Patrones de Diseño Esenciales: Factory Method y Singleton",
                        "descripcion": "Implementación práctica de instancias únicas (Singleton para conexiones a BD) y creación delegada de objetos (Factory Method).",
                        "estado": "adecuado",
                        "justificacion": "Patrones de alta frecuencia de uso en frameworks profesionales.",
                        "enfoque": "Creación de un gestor de conexiones a base de datos como Singleton.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Mapeo Objeto-Relacional (ORM Básico) con JPA / Hibernate o Prisma",
                        "descripcion": "Concepto de entidades mapeadas a tablas mediante anotaciones, repositorios tipados y reducción de código SQL repetitivo manual.",
                        "estado": "propuesto",
                        "justificacion": "La industria moderna casi no utiliza JDBC directo en código productivo; el uso de ORMs acelera drásticamente la productividad.",
                        "enfoque": "Configuración de una entidad mapeada con repositorio CRUD tipado.",
                        "tipo": "propuesta"
                    }
                ]
            },
            {
                "bimestre_num": 4,
                "nombre": "Bimestre 4: Interfaces de Usuario, Metodologías Ágiles y Control de Versiones con Git",
                "temas": [
                    {
                        "nombre": "Fundamentos de Experiencia e Interfaz de Usuario (UX/UI)",
                        "descripcion": "Principios de usabilidad, accesibilidad, jerarquía visual, diseño centrado en el usuario, wireframes y flujos de navegación.",
                        "estado": "adecuado",
                        "justificacion": "Garantiza que el software construido sea intuitivo y cumpla con expectativas profesionales de clientes reales.",
                        "enfoque": "Elaboración de wireframes antes de comenzar la codificación de interfaces.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Desarrollo de GUI: Formularios, Componentes y Diálogos",
                        "descripcion": "Construcción de vistas interactivas con cajas de texto, botones, tablas dinámicas, menús desplegables y validación de campos obligatorios.",
                        "estado": "adecuado",
                        "justificacion": "Permite al estudiante crear productos de software completos e interactivos.",
                        "enfoque": "Implementación de pantallas de captura de datos y listados tabulares.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Manejo de Eventos, Listeners y Enlace con Lógica de Negocio",
                        "descripcion": "Programación reactiva a eventos de usuario (clicks, teclado, cambios de foco), separación de eventos y desacoplamiento con controladores.",
                        "estado": "adecuado",
                        "justificacion": "Mecanismo universal de interacción presente tanto en desktop como en frontend web móvil.",
                        "enfoque": "Conexión de componentes visuales a la capa de servicios y persistencia.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Metodologías Ágiles: Manifiesto Ágil y Marco de Trabajo Scrum",
                        "descripcion": "Valores y principios ágiles, roles (Product Owner, Scrum Master, Developers), eventos (Sprint Planning, Daily, Review, Retrospective) y artefactos.",
                        "estado": "adecuado",
                        "justificacion": "Metodología estándar en prácticamente todas las empresas de software de Guatemala y el mundo.",
                        "enfoque": "Simulación de un sprint de 2 semanas con roles asignados dentro del aula.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Historias de Usuario, Criterios de Aceptación y Estimación Ágil",
                        "descripcion": "Formato 'Como [rol], quiero [acción], para [beneficio]', criterios de aceptación verificables, estimación con Planning Poker y Definition of Done (DoD).",
                        "estado": "adecuado",
                        "justificacion": "Garantiza que el programador comprenda el valor de negocio de lo que está programando antes de escribir código.",
                        "enfoque": "Redacción y desglose de un backlog de producto en historias de usuario estimadas.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Gestión Visual con Tableros Kanban",
                        "descripcion": "Flujo de trabajo visual: To Do, In Progress, Code Review, Done; límites de trabajo en progreso (WIP) e identificación de cuellos de botella.",
                        "estado": "adecuado",
                        "justificacion": "Herramienta indispensable de transparencia operativa utilizada en Jira, Trello y GitHub Projects.",
                        "enfoque": "Uso diario del tablero para seguimiento del avance del proyecto integrador.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Control de Versiones Colaborativo con Git y GitHub",
                        "descripcion": "Conceptos de repositorio local y remoto, comandos esenciales: git clone, status, add, commit, push, pull, log y diff.",
                        "estado": "adecuado",
                        "justificacion": "Habilidad no negociable en el 100% de empresas de tecnología modernas.",
                        "enfoque": "Creación y sincronización de repositorios remotos en GitHub con README detallado.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Estrategias de Ramas (Branches), Merge y Resolución de Conflictos",
                        "descripcion": "Aislamiento de funcionalidades mediante ramas (feature branches), integración (merge) y resolución controlada de conflictos de código.",
                        "estado": "adecuado",
                        "justificacion": "Permite el trabajo en paralelo de múltiples desarrolladores sin sobrescribir el trabajo ajeno.",
                        "enfoque": "Ejercicio guiado de trabajo en equipo provocando y resolviendo conflictos de merge.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Pull Requests, Code Review y Defensa de Código",
                        "descripcion": "Proceso de solicitud de extracción (PR), revisión de pares, comentarios de mejora, criterios de aprobación y sustentación oral frente al docente.",
                        "estado": "adecuado",
                        "justificacion": "Fomenta la cultura de calidad, trabajo colaborativo y previene la copia ciega de código generado por IA.",
                        "enfoque": "Aprobación de al menos un PR por estudiante con revisión obligatoria de pares.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Diseño de Interfaces Complejas con Java Swing Antiguo (GridBagLayout manual)",
                        "descripcion": "Enseñanza exhaustiva de componentes arcaicos de Swing de escritorio con posicionamiento manual rígido en píxeles.",
                        "estado": "eliminar",
                        "justificacion": "Tecnología en desuso comercial absoluto. Las empresas no desarrollan interfaces nuevas en Swing; consume tiempo valioso que debe dedicarse a frontend web moderno.",
                        "enfoque": "Sustituir por interfaces web o mantener solo layouts visuales sencillos para pruebas.",
                        "tipo": "obsoleto"
                    },
                    {
                        "nombre": "JavaFX como Entorno Exclusivo de Interfaces de Usuario",
                        "descripcion": "Dedicación de todo el módulo de interfaces a tecnología desktop en lugar de introducir conceptos web.",
                        "estado": "revisar",
                        "justificacion": "JavaFX tiene un nicho reducido en la industria local; conviene conectar los conceptos de GUI con fundamentos web (HTML5/CSS3) para mayor empleabilidad.",
                        "enfoque": "Modularizar el tiempo de GUI para incorporar nociones web frontend.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Conventional Commits y Automatización de Changelog",
                        "descripcion": "Estandarización de mensajes de commit (`feat:`, `fix:`, `docs:`, `refactor:`) y generación automática de versiones.",
                        "estado": "propuesto",
                        "justificacion": "Buenas prácticas de ingeniería altamente valoradas por líderes técnicos en empresas de software guatemaltecas.",
                        "enfoque": "Validación de commits con linter de Git en proyectos de fin de ciclo.",
                        "tipo": "propuesta"
                    }
                ]
            }
        ]
    },
    "quinto_informatica": {
        "id": "quinto_informatica",
        "title": "5to Perito en Informática",
        "subtitle": "Ciclo de Ingeniería de Software, APIs RESTful, Testing Automatizado y Despliegue",
        "docente": "Área Técnica de Informática (Magno Solís, Elmer Santos, Kenneth Velázquez, Diego Barrascout)",
        "horas": "30 períodos semanales (15 Tecnología + 15 Taller)",
        "bimestres": [
            {
                "bimestre_num": 1,
                "nombre": "Bimestre 1: Elicitación de Requerimientos, Análisis de Problemas e Ingeniería de Requisitos",
                "temas": [
                    {
                        "nombre": "Ciclo de Vida de Desarrollo de Software (SDLC) Moderno",
                        "descripcion": "Fases del SDLC: concepción, análisis, diseño, construcción, pruebas, despliegue, operación y retiro; modelos iterativos e incrementales.",
                        "estado": "adecuado",
                        "justificacion": "Brinda la visión global de la profesión y sitúa al estudiante en el rol de ingeniero de software junior.",
                        "enfoque": "Mapeo de las etapas del ciclo de vida en proyectos de software comerciales.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Caracterización de Problemas del Mundo Real y Mapeo de Stakeholders",
                        "descripcion": "Técnicas de diagnóstico empresarial, identificación de actores, intereses, dolores del cliente y objetivos del negocio.",
                        "estado": "adecuado",
                        "justificacion": "Previene el error más costoso en el desarrollo de software: construir la solución equivocada para el problema equivocado.",
                        "enfoque": "Estudios de caso con empresas y pymes guatemaltecas reales.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Elicitación de Requerimientos: Entrevistas Técnicas y Cuestionarios",
                        "descripcion": "Técnicas estructuradas para obtener requerimientos de clientes, usuarios finales y operadores del sistema sin ambigüedades.",
                        "estado": "adecuado",
                        "justificacion": "Habilidad blanda y técnica requerida para analistas y programadores en contacto con clientes.",
                        "enfoque": "Role-playing simulando sesiones de levantamiento de requisitos con clientes.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Especificación de Requerimientos Funcionales y No Funcionales (NFR)",
                        "descripcion": "Definición rigurosa de lo que el sistema debe hacer (funcionales) vs cómo debe operar (rendimiento, seguridad, disponibilidad, escalabilidad).",
                        "estado": "adecuado",
                        "justificacion": "Los NFR determinan el éxito arquitectónico de la aplicación en producción y son evaluados por clientes corporativos.",
                        "enfoque": "Matriz de trazabilidad de requerimientos funcionales y criterios no funcionales.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Modelado de Casos de Uso y Diagramas de Secuencia UML",
                        "descripcion": "Actores, casos de uso, relaciones `include` y `extend`, diagramas de secuencia para representar el intercambio de mensajes temporal.",
                        "estado": "adecuado",
                        "justificacion": "Lenguaje gráfico universal de modelado para entender flujos entre capas y sistemas externos.",
                        "enfoque": "Modelado de flujos principales y alternativos en herramientas CASE modernas.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Historias de Usuario Detalladas y Criterios de Aceptación (Given-When-Then)",
                        "descripcion": "Redacción con estructura de usuario, validación con criterios INVEST y especificación en formato BDD (Dado que / Cuando / Entonces).",
                        "estado": "adecuado",
                        "justificacion": "Formato estándar que conecta el negocio con los tests automatizados de desarrollo.",
                        "enfoque": "Redacción de historias listas para desarrollo en el backlog del equipo.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Priorización Ágil del Backlog (MoSCoW, Valor vs Esfuerzo)",
                        "descripcion": "Clasificación de funcionalidades en Must have, Should have, Could have y Won't have; análisis de retorno de valor y dependencias críticas.",
                        "estado": "adecuado",
                        "justificacion": "Permite entregar versiones funcionales a tiempo sin retrasar lanzamientos por detalles secundarios.",
                        "enfoque": "Sesión de priorización de backlog para el MVP (Producto Mínimo Viable) del bimestre.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Estimación Ágil de Esfuerzo y Definition of Done (DoD)",
                        "descripcion": "Asignación de Story Points con secuencia Fibonacci, velocidad de equipo y establecimiento de la lista de verificación obligatoria para dar por terminada una tarea.",
                        "estado": "adecuado",
                        "justificacion": "Fomenta la previsibilidad del equipo y la cultura de calidad antes de cerrar entregables.",
                        "enfoque": "Definición del checklist institucional de DoD para el código del estudiante.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Documentación Extensa Tradicional estilo RUP / Cascada Estricta",
                        "descripcion": "Elaboración de extensos documentos de especificación de cientos de páginas previo a cualquier codificación.",
                        "estado": "eliminar",
                        "justificacion": "Metodología obsoleta y desfasada. Las empresas de desarrollo ágil exigen especificaciones concisas, iterativas y documentación viva de código.",
                        "enfoque": "Reemplazar por backlog ágil bien documentado y contratos de API claros.",
                        "tipo": "obsoleto"
                    },
                    {
                        "nombre": "Diseño de Prototipos de Alta Fidelidad en Figma para Validación con Cliente",
                        "descripcion": "Construcción de wireframes interactivos navegables en Figma para validar la experiencia de usuario antes de codificar.",
                        "estado": "propuesto",
                        "justificacion": "Ahorra hasta un 40% del tiempo de desarrollo al evitar cambios de diseño tardíos en código.",
                        "enfoque": "Diseño y presentación del prototipo navegable al inicio del proyecto.",
                        "tipo": "propuesta"
                    }
                ]
            },
            {
                "bimestre_num": 2,
                "nombre": "Bimestre 2: Arquitectura de Software, Backend y Desarrollo de APIs RESTful",
                "temas": [
                    {
                        "nombre": "Principios de Arquitectura de Software: Cohesión y Acoplamiento Débil",
                        "descripcion": "Diseño modular de sistemas, principios de inversión de control, límites arquitectónicos claros y flujo ordenado de datos entre capas.",
                        "estado": "adecuado",
                        "justificacion": "Garantiza que el sistema sea escalable, testeable y fácil de mantener a lo largo de su vida útil.",
                        "enfoque": "Diseño de diagramas de arquitectura de componentes de software.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Diseño y Principios de APIs RESTful",
                        "descripcion": "Recursos, URI descriptivas, verbos HTTP (GET, POST, PUT, PATCH, DELETE), códigos de respuesta estándar (200, 201, 400, 401, 403, 404, 500) y statelessness.",
                        "estado": "adecuado",
                        "justificacion": "Estándar absoluto de interoperabilidad en la industria para comunicar frontend, móviles y sistemas de backend.",
                        "enfoque": "Diseño de la especificación de endpoints JSON antes de la programación.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Desarrollo de Servicios Backend con Node.js / Express o Spring Boot",
                        "descripcion": "Configuración del servidor, enrutamiento, controladores, capas de servicio, inyección de dependencias y middlewares de procesamiento.",
                        "estado": "adecuado",
                        "justificacion": "Las dos tecnologías backend más demandadas en el mercado laboral centroamericano y corporativo.",
                        "enfoque": "Construcción de una API completa con endpoints CRUD para gestión comercial.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Validación de Payloads y Manejo Centralizado de Errores",
                        "descripcion": "Sanitización y validación de esquemas de datos entrantes (Joi, Zod o Jakarta Bean Validation) y captura global de excepciones.",
                        "estado": "adecuado",
                        "justificacion": "Previene inconsistencias, caídas de servidor y filtración involuntaria de trazas de error internas.",
                        "enfoque": "Implementación de middleware global de errores que retorna respuestas JSON coherentes.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Persistencia de Datos Integrada en Backend (Conexión Relacional)",
                        "descripcion": "Conexión eficiente con bases de datos relacionales (PostgreSQL / MySQL), pools de conexiones y persistencia transaccional.",
                        "estado": "adecuado",
                        "justificacion": "Habilidad indispensable para asegurar que las operaciones del usuario queden almacenadas de forma duradera.",
                        "enfoque": "Integración del backend con la base de datos relacional del proyecto.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Persistencia de Datos en Bases NoSQL Documentales",
                        "descripcion": "Conexión a MongoDB con Mongoose u ODM oficial, esquemas flexibles, operaciones atómicas y consultas agregadas.",
                        "estado": "adecuado",
                        "justificacion": "Permite resolver casos de uso donde los esquemas son altamente variables o basados en logs y catálogos.",
                        "enfoque": "Implementación de colecciones NoSQL integradas con la API REST.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Autenticación Segura con JSON Web Tokens (JWT) y Hash de Contraseñas",
                        "descripcion": "Cifrado irreversible de passwords con bcrypt/argon2, generación y firma de tokens JWT, claims, expiración y middleware de verificación.",
                        "estado": "adecuado",
                        "justificacion": "Estándar de la industria para autenticación sin estado en aplicaciones web y móviles.",
                        "enfoque": "Implementación de endpoints `/auth/register` y `/auth/login` con rutas protegidas.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Sobrecarga Simultánea de Múltiples Stacks Backend en un Mismo Bimestre",
                        "descripcion": "Intentar enseñar Java Spring Boot, C# .NET y Node.js en las mismas 7 semanas lectivas.",
                        "estado": "revisar",
                        "justificacion": "Genera dispersión y confusión de sintaxis en el estudiante; se debe seleccionar un stack principal (ej. TypeScript/Node.js o Java/Spring Boot) y consolidarlo a fondo.",
                        "enfoque": "Consolidar un stack vehicular unificado durante el ciclo lectivo.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Documentación Interactiva de APIs con OpenAPI y Swagger",
                        "descripcion": "Generación de documentación viva de endpoints con Swagger UI, prueba interactiva de parámetros y contratos formales.",
                        "estado": "propuesto",
                        "justificacion": "Herramienta obligatoria en software houses para la integración entre equipos de frontend y backend.",
                        "enfoque": "Anotación de la API y publicación de la documentación en `/api-docs`.",
                        "tipo": "propuesta"
                    },
                    {
                        "nombre": "Pruebas de APIs con Postman y Automatización con Newman",
                        "descripcion": "Creación de colecciones de pruebas en Postman, variables de entorno, aserciones en JavaScript de status code y respuesta JSON.",
                        "estado": "propuesto",
                        "justificacion": "La habilidad más demandada a un QA Tester junior o desarrollador junior para validar el comportamiento de endpoints.",
                        "enfoque": "Creación de colección Postman con tests automatizados para el 100% de los endpoints.",
                        "tipo": "propuesta"
                    }
                ]
            },
            {
                "bimestre_num": 3,
                "nombre": "Bimestre 3: Construcción Incremental, Testing Automatizado y Despliegue",
                "temas": [
                    {
                        "nombre": "Desarrollo Incremental Basado en Sprints",
                        "descripcion": "Entrega de software potencialmente desplegable al final de cada iteración, control de cambios y trazabilidad hacia el backlog.",
                        "estado": "adecuado",
                        "justificacion": "Forma la disciplina de entrega continua de valor demandada en los equipos ágiles profesionales.",
                        "enfoque": "Ejecución de dos sprints consecutivos con entregas funcionales comprobables.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Pirámide de Pruebas y Estrategia de Calidad de Software",
                        "descripcion": "Estructura de pruebas: base amplia de tests unitarios, capa intermedia de integración y capa superior de pruebas funcionales/E2E.",
                        "estado": "adecuado",
                        "justificacion": "Enseña al alumno a invertir el esfuerzo de testing de forma eficiente y económica.",
                        "enfoque": "Diseño de la matriz de pruebas del proyecto según la pirámide de testing.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Pruebas Unitarias Automatizadas (Jest / JUnit)",
                        "descripcion": "Diseño de tests unitarios aislados, mocks, stubs, spies, aserciones y cálculo de cobertura de código (code coverage).",
                        "estado": "adecuado",
                        "justificacion": "Competencia clave para escribir código robusto que previene regresiones ante modificaciones futuras.",
                        "enfoque": "Implementación de tests unitarios para las reglas de negocio críticas del sistema.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Pruebas de Integración de Endpoints y Persistencia",
                        "descripcion": "Pruebas automáticas de rutas HTTP con Supertest / MockMvc, verificación de transacciones reales en base de datos de prueba.",
                        "estado": "adecuado",
                        "justificacion": "Verifica que los módulos de la aplicación trabajen en conjunto de manera armónica.",
                        "enfoque": "Batería de pruebas de integración que simula llamadas cliente-servidor.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Gestión Profesional de Defectos y Reporte de Bugs",
                        "descripcion": "Ciclo de vida del defecto: reporte con pasos para reproducir, severidad, prioridad, asignación, corrección y re-testeo.",
                        "estado": "adecuado",
                        "justificacion": "Cultura de aseguramiento de calidad indispensable para el rol de QA tester o developer junior.",
                        "enfoque": "Registro y resolución de issues en GitHub Projects con etiquetas de severidad.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Versionado Semántico (SemVer) y Preparación de Releases",
                        "descripcion": "Convenio MAJOR.MINOR.PATCH, etiquetado de versiones (`git tag`), notas de lanzamiento (Changelog) y release candidates.",
                        "estado": "adecuado",
                        "justificacion": "Estándar internacional para comunicar el impacto de los cambios a usuarios y consumidores de software.",
                        "enfoque": "Publicación formal de la versión v1.0.0 del proyecto con release notes en GitHub.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Configuración de Ambientes de Staging y Procedimientos de Despliegue",
                        "descripcion": "Diferenciación estricta entre entornos de desarrollo local, pre-producción (staging) y producción; variables de configuración independientes.",
                        "estado": "adecuado",
                        "justificacion": "Evita errores catastróficos en producción por diferencias de configuración.",
                        "enfoque": "Despliegue de la solución en un entorno de staging en la nube.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Planes de Contingencia y Rollback ante Fallos en Despliegue",
                        "descripcion": "Estrategias de reversión a la versión estable anterior, respaldo previo a despliegue y comprobación posterior (smoke testing).",
                        "estado": "adecuado",
                        "justificacion": "Capacidad operativa indispensable para mantener la continuidad del negocio ante imprevistos.",
                        "enfoque": "Simulación controlada de un fallo en despliegue y ejecución exitosa de rollback.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Enfoque Exclusivo en Pruebas Manuales sin Automatización",
                        "descripcion": "Validación de software dependiendo enteramente de comprobaciones manuales en pantalla sin escribir código de prueba.",
                        "estado": "revisar",
                        "justificacion": "El mercado laboral junior demanda automatización; depender de pruebas manuales no escala y hace ineficiente al graduando.",
                        "enfoque": "Asegurar que cada funcionalidad cuente con al menos un test automatizado.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Integración Continua Básica con GitHub Actions",
                        "descripcion": "Creación de un workflow en YAML que ejecute linters y tests automatizados con cada Pull Request a la rama main.",
                        "estado": "propuesto",
                        "justificacion": "Habilidad moderna de DevOps que asegura que solo código verificado llegue a las ramas principales.",
                        "enfoque": "Configuración de un archivo `.github/workflows/ci.yml` funcional en el repositorio.",
                        "tipo": "propuesta"
                    }
                ]
            },
            {
                "bimestre_num": 4,
                "nombre": "Bimestre 4: Operación en Producción, Telemetría, Mantenimiento y Retroalimentación",
                "temas": [
                    {
                        "nombre": "Operación de Software en Entornos Reales y Disponibilidad",
                        "descripcion": "Concepto de servicio continuo, métricas de uptime/downtime, comportamiento en condiciones reales de carga y acuerdos de servicio (SLA).",
                        "estado": "adecuado",
                        "justificacion": "Brinda al alumno la perspectiva del valor que el software entrega cuando ya está en manos del usuario final.",
                        "enfoque": "Auditoría de disponibilidad y tiempos de respuesta del sistema desplegado.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Logging Estructurado y Niveles de Registro (INFO, WARN, ERROR, DEBUG)",
                        "descripcion": "Registro consistente de eventos en formato JSON, marcas de tiempo, trazas de excepción limpias y herramientas de rotación de logs.",
                        "estado": "adecuado",
                        "justificacion": "Herramienta primaria para el soporte técnico y la investigación de incidencias en sistemas empresariales.",
                        "enfoque": "Implementación de una librería de logging profesional (Winston, Logback) en el backend.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Gestión de Incidentes y Análisis de Causa Raíz (RCA)",
                        "descripcion": "Protocolo de atención de incidentes: detección, contención, aislamiento, hipótesis de causa raíz, corrección definitiva y lecciones aprendidas.",
                        "estado": "adecuado",
                        "justificacion": "Forma la madurez operativa requerida en puestos de soporte técnico y operaciones (ITSM / DevOps).",
                        "enfoque": "Elaboración de un informe de post-mortem para un incidente simulado en el aula.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Tipos de Mantenimiento de Software: Correctivo, Preventivo y Evolutivo",
                        "descripcion": "Diferenciación entre solucionar errores urgentes (correctivo), optimizar código antes de que falle (preventivo) y agregar nuevas capacidades (evolutivo).",
                        "estado": "adecuado",
                        "justificacion": "El 70% del ciclo de vida de un software en la industria se dedica a tareas de mantenimiento.",
                        "enfoque": "Planificación y ejecución de tareas de mantenimiento sobre un sistema existente.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Retroalimentación de Usuarios y Priorización de Mejoras para Nueva Iteración",
                        "descripcion": "Canales de recolección de feedback, análisis de encuestas y tickets de soporte, y transformación de quejas en nuevas historias de usuario.",
                        "estado": "adecuado",
                        "justificacion": "Cierra el ciclo virtuoso de la mejora continua y el desarrollo ágil centrado en el cliente.",
                        "enfoque": "Incorporación de feedback de usuarios reales en el backlog del siguiente release.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Refactorización Segura Respaldada por Tests de Regresión",
                        "descripcion": "Mejora de la estructura interna del código (eliminación de duplicidad, simplificación de métodos) garantizando que los tests sigan pasando en verde.",
                        "estado": "adecuado",
                        "justificacion": "Práctica indispensable para combatir la deuda técnica acumulada en los proyectos.",
                        "enfoque": "Sesión de refactorización de código legado comprobando que ningún test unitario falle.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Telemetría y APM Avanzado a Nivel de Microservicios Distribuidos",
                        "descripcion": "Instrumentación masiva con agentes distribuidos de telemetría (OpenTelemetry, Datadog, Jaeger) a nivel perito.",
                        "estado": "revisar",
                        "justificacion": "Demasiada complejidad de infraestructura para nivel diversificado; corresponde a la formación superior en ETS. En perito debe centrarse en logging y monitoreo de servidor.",
                        "enfoque": "Acotar a métricas de servidor y logging estructurado en disco o servicio cloud simple.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Gestión Segura de Variables de Entorno (.env) y Prevención de Fugas",
                        "descripcion": "Uso de archivos `.env`, exclusión mandatoria en `.gitignore`, plantillas `.env.example` y herramientas para escanear secretos en repositorios.",
                        "estado": "propuesto",
                        "justificacion": "Cientos de credenciales bancarias y API keys se filtran diariamente en GitHub por descuidos de juniors; este tema es de seguridad crítica.",
                        "enfoque": "Auditoría de repositorios de estudiantes con escáneres de secretos para garantizar cero credenciales expuestas.",
                        "tipo": "propuesta"
                    }
                ]
            }
        ]
    },
    "sexto_informatica": {
        "id": "sexto_informatica",
        "title": "6to Perito en Informática",
        "subtitle": "Ciclo de Cierre: Desarrollo Full-Stack, Containerización, Cloud y DevOps (Bimestres 1 al 3)",
        "docente": "Área Técnica de Informática (Diego Barrascout, Kenneth Velázquez, Elmer Santos, Denys Orozco)",
        "horas": "30 períodos semanales (15 Tecnología + 15 Taller) • Bimestre 4 reservado para Práctica Supervisada",
        "bimestres": [
            {
                "bimestre_num": 1,
                "nombre": "Bimestre 1: Del Problema al Desarrollo de Servicios Empresariales",
                "temas": [
                    {
                        "nombre": "Arquitectura de Software Empresarial y Principios de Servicios Web",
                        "descripcion": "Diseño de soluciones basadas en servicios desacoplados, contratos de comunicación, capas de dominio y patrones arquitectónicos modernos.",
                        "estado": "adecuado",
                        "justificacion": "Prepara al futuro perito para integrarse a arquitecturas corporativas reales sin sentirse abrumado.",
                        "enfoque": "Diseño de la arquitectura integral del proyecto de graduación.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Contratos Formales de APIs y Estándar JSON Schema",
                        "descripcion": "Definición estricta de interfaces de comunicación entre componentes, validación de contratos y consistencia de datos.",
                        "estado": "adecuado",
                        "justificacion": "Permite el desarrollo en paralelo y desacoplado entre programadores de frontend y backend.",
                        "enfoque": "Establecimiento de contratos de API aprobados por todo el equipo antes de programar.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Seguridad en APIs: Autenticación OAuth2 / JWT y Roles (RBAC)",
                        "descripcion": "Control de acceso basado en roles (Admin, Cajero, Cliente), expiración de sesiones, refresh tokens y protección de recursos sensibles.",
                        "estado": "adecuado",
                        "justificacion": "Requisito mandatorio de seguridad en aplicaciones financieras, comerciales y de telecomunicaciones.",
                        "enfoque": "Implementación de control de acceso por roles en endpoints críticos de la solución.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Servicios Backend Robustos y Manejo de Concurrencia",
                        "descripcion": "Construcción de endpoints asíncronos de alto desempeño, manejo eficiente de I/O, control de límites de peticiones (rate limiting) y sanitización.",
                        "estado": "adecuado",
                        "justificacion": "Evita vulnerabilidades de denegación de servicio y asegura la estabilidad del backend ante picos de uso.",
                        "enfoque": "Pruebas de estrés básico y protección de endpoints contra solicitudes masivas.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Persistencia Avanzada: Transacciones Complejas y Pools de Conexión",
                        "descripcion": "Optimización de accesos a base de datos, configuración de pools (HikariCP, pg-pool), aislamiento transaccional y prevención de bloqueos.",
                        "estado": "adecuado",
                        "justificacion": "Habilidad clave para evitar cuellos de botella severos en bases de datos empresariales.",
                        "enfoque": "Configuración y medición del rendimiento de conexiones a base de datos.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Validación Rigurosa y Sanitización de Entradas contra XSS e Inyecciones",
                        "descripcion": "Uso de validadores automáticos, filtrado de caracteres maliciosos, escape de HTML y prevención de inyecciones NoSQL y SQL.",
                        "estado": "adecuado",
                        "justificacion": "Protege los sistemas contra los vectores de ataque más comunes en la web según OWASP.",
                        "enfoque": "Implementación de capas de validación y sanitización en todos los endpoints de entrada.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Adopción de IA CoWork para Aceleración y Validación de Código",
                        "descripcion": "Generación asistida de pruebas, documentación de código y scaffolding con copilotos, acompañada de sustentación oral individual del código generado.",
                        "estado": "adecuado",
                        "justificacion": "Los equipos de desarrollo de punta en Guatemala utilizan IA para aumentar su productividad; Kinal enseña su uso responsable y ético.",
                        "enfoque": "Bitácora obligatoria de prompts y justificación técnica en la defensa del proyecto.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Ciberseguridad Práctica: OWASP Top 10 para Desarrolladores Web Junior",
                        "descripcion": "Estudio práctico de las 10 principales vulnerabilidades web (Broken Access Control, Cryptographic Failures, Injection, Insecure Design) y cómo mitigarlas.",
                        "estado": "propuesto",
                        "justificacion": "La banca y el sector corporativo guatemalteco priorizan egresados que ya tienen conciencia de seguridad en su código desde el día uno.",
                        "enfoque": "Laboratorio de auditoría de seguridad sobre la propia API desarrollada.",
                        "tipo": "propuesta"
                    },
                    {
                        "nombre": "Migraciones Automatizadas de Bases de Datos (Flyway / Liquibase / Prisma Migrate)",
                        "descripcion": "Control de versiones de los cambios de esquema de base de datos a lo largo del tiempo, scripts reproducibles y rollback de migraciones.",
                        "estado": "propuesto",
                        "justificacion": "Ningún equipo profesional altera tablas manualmente con herramientas visuales en entornos reales; las migraciones son el estándar indiscutible.",
                        "enfoque": "Gestión de todas las modificaciones de tablas mediante scripts de migración versionados en Git.",
                        "tipo": "propuesta"
                    }
                ]
            },
            {
                "bimestre_num": 2,
                "nombre": "Bimestre 2: Del Desarrollo al Software Desplegado en la Nube",
                "temas": [
                    {
                        "nombre": "Desarrollo Frontend Moderno Basado en Componentes (React / SPA)",
                        "descripcion": "Arquitectura de componentes funcionales, props, estados (useState, useEffect), hooks personalizados y ciclo de vida de la interfaz.",
                        "estado": "adecuado",
                        "justificacion": "React es la librería frontend más demandada en Guatemala y el mercado nearshore internacional.",
                        "enfoque": "Construcción de una interfaz moderna y responsiva tipo Single Page Application.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Consumo Asíncrono de APIs con Axios / Fetch y Manejo de Estados de Carga",
                        "descripcion": "Peticiones HTTP asíncronas, manejo de promises/async-await, interceptores de autenticación (adjuntar token Bearer), feedback visual (spinners, alertas).",
                        "estado": "adecuado",
                        "justificacion": "Esencial para que la interfaz se comunique con el backend de forma fluida y sin recargas de página completas.",
                        "enfoque": "Integración completa entre la interfaz React y la API backend desarrollada en B1.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Pruebas de Extremo a Extremo (E2E) y Validación de Flujos de Usuario",
                        "descripcion": "Automatización de pruebas en el navegador (Cypress / Playwright), simulación de interacciones reales de usuario y verificación de flujos completos.",
                        "estado": "adecuado",
                        "justificacion": "Garantiza que la experiencia del usuario y las integraciones entre sistemas funcionen a la perfección.",
                        "enfoque": "Creación de una suite de pruebas E2E que valide el flujo de autenticación y compra.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Containerización de Aplicaciones con Docker: Dockerfile e Imágenes",
                        "descripcion": "Conceptos de contenedores vs máquinas virtuales, creación de Dockerfiles eficientes multi-stage, capas de imagen, tags y Docker Hub.",
                        "estado": "adecuado",
                        "justificacion": "Estándar global de empaquetado y distribución de software moderno que elimina el problema de 'en mi máquina sí funciona'.",
                        "enfoque": "Creación de imágenes optimizadas de frontend y backend.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Orquestación Multi-Contenedor con Docker Compose",
                        "descripcion": "Composición de ambientes completos mediante archivos `docker-compose.yml`: levantar backend, frontend, base de datos relacional y Redis en un comando.",
                        "estado": "adecuado",
                        "justificacion": "Permite que cualquier miembro del equipo o evaluador levante el ecosistema completo en segundos.",
                        "enfoque": "Configuración del entorno completo del proyecto integrador con Docker Compose.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Preparación de Ambientes Aislados y Variables de Configuración",
                        "descripcion": "Gestión de configuraciones por ambiente sin tocar código fuente (Twelve-Factor App methodology).",
                        "estado": "adecuado",
                        "justificacion": "Principio clave de ingeniería para que la misma imagen de contenedor funcione en cualquier nube.",
                        "enfoque": "Separación de variables en producción vs desarrollo.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Despliegue Continuo a la Nube (PaaS / Cloud Hosting)",
                        "descripcion": "Publicación de contenedores y servicios en plataformas cloud (Render, Railway, Fly.io, AWS EC2/App Runner) con dominio y certificado SSL.",
                        "estado": "adecuado",
                        "justificacion": "Permite entregar productos reales accesibles en internet a clientes y reclutadores de talento.",
                        "enfoque": "Despliegue en vivo del proyecto de fin de año accesible vía URL pública HTTPS.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Dispersión de Múltiples Frameworks Frontend Incompatibles en Pocas Semanas",
                        "descripcion": "Intentar cubrir React, Angular y Vue de forma consecutiva y superficial en un mismo bimestre.",
                        "estado": "revisar",
                        "justificacion": "Genera sobrecarga y conocimiento fragmentado en el estudiante; la industria recomienda dominar profundamente un ecosistema (React + TypeScript) y transferir conceptos después.",
                        "enfoque": "Especializarse en React con TypeScript para máxima solidez formativa.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Publicación del Portafolio Profesional en Vivo en la Nube",
                        "descripcion": "Cada estudiante despliega su portafolio web personal con enlaces a sus proyectos de GitHub, demos en vivo, CV técnico y credenciales.",
                        "estado": "propuesto",
                        "justificacion": "Herramienta determinante de empleabilidad directa; los reclutadores contratan al ver código real y productos funcionando.",
                        "enfoque": "Revisión obligatoria del portafolio en vivo como requisito previo a la Práctica Supervisada.",
                        "tipo": "propuesta"
                    }
                ]
            },
            {
                "bimestre_num": 3,
                "nombre": "Bimestre 3: Del Software en Producción a la Nueva Iteración Ágil",
                "temas": [
                    {
                        "nombre": "Monitoreo en Producción: Health Checks y Métricas de Rendimiento",
                        "descripcion": "Endpoints `/health` y `/metrics`, monitoreo de consumo de CPU, memoria, tasa de errores HTTP y disponibilidad del sistema en tiempo real.",
                        "estado": "adecuado",
                        "justificacion": "Permite detectar fallos antes de que los usuarios se quejen y tomar acciones preventivas.",
                        "enfoque": "Configuración de health checks en el backend y pruebas de disponibilidad.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Detección de Cuellos de Botella y Optimización de Consultas",
                        "descripcion": "Análisis de queries lentas (Slow Query Log), uso de EXPLAIN en bases de datos relacionales, creación de índices estratégicos y cacheo.",
                        "estado": "adecuado",
                        "justificacion": "Habilidad que distingue a un buen programador de uno novato, evitando costos excesivos en servidores cloud.",
                        "enfoque": "Optimización guiada de consultas complejas mejorando el plan de ejecución.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Clasificación de Incidentes Críticos y Acuerdos de Nivel de Servicio (SLA)",
                        "descripcion": "Clasificación de fallos por severidad (P1 crítico, P2 alto, P3 medio), tiempos máximos de respuesta y protocolos de comunicación.",
                        "estado": "adecuado",
                        "justificacion": "Estándar de operación en empresas de telecomunicaciones, finanzas y consultoría de TI en Guatemala.",
                        "enfoque": "Simulación de una caída de servicio P1 y cálculo del tiempo de restauración (MTTR).",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Mantenimiento Evolutivo: Conversión de Incidentes en Historias del Backlog",
                        "descripcion": "Transformación de los problemas detectados en producción en nuevos requerimientos de mejora planificados para la siguiente iteración.",
                        "estado": "adecuado",
                        "justificacion": "Cierra el ciclo del desarrollo ágil asegurando que el software evolucione con base en datos reales.",
                        "enfoque": "Planificación del sprint de mejora continua post-despliegue.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Análisis de Impacto de Cambios en Sistemas en Producción",
                        "descripcion": "Evaluación de dependencias, riesgos colaterales, compatibilidad hacia atrás en APIs y estrategias de migración sin pérdida de datos.",
                        "estado": "adecuado",
                        "justificacion": "Evita que un cambio menor rompa funcionalidades existentes en clientes reales.",
                        "enfoque": "Matriz de impacto de cambios y planes de prueba de regresión antes de aplicar parches.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Consolidación de Métricas del Proyecto y Auditoría Final de Calidad",
                        "descripcion": "Revisión final de métricas de cobertura de código, cumplimiento de DoD, análisis estático con SonarQube/ESLint y lecciones aprendidas.",
                        "estado": "adecuado",
                        "justificacion": "Consolida la autocrítica profesional y garantiza que el proyecto final de perito sea de nivel profesional.",
                        "enfoque": "Auditoría formal de calidad de código previa al cierre del ciclo lectivo.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Cierre del Ciclo Formativo y Preparación para la Práctica Supervisada",
                        "descripcion": "Entrega final del proyecto integrador, defensa oral ante jurado técnico, retroalimentación institucional y transición hacia la empresa.",
                        "estado": "adecuado",
                        "justificacion": "Hito culminante de la formación de nivel diversificado en el Centro Escolar Técnico de Fundación Kinal.",
                        "enfoque": "Sustentación pública y entrega de documentación final.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Orquestación Avanzada de Clústeres Kubernetes a Nivel Diversificado",
                        "descripcion": "Intento de enseñar despliegue, ingress controllers y autoescalado con clústeres complejos de Kubernetes en 6to perito.",
                        "estado": "revisar",
                        "justificacion": "Kubernetes a gran escala pertenece a la formación terciaria en ETS (TSU); en nivel diversificado es más formativo y empleable dominar Docker y Docker Compose a la perfección.",
                        "enfoque": "Focalizar en Docker Compose y despliegue PaaS antes de intentar orquestación avanzada.",
                        "tipo": "troncal"
                    },
                    {
                        "nombre": "Estrategias de Branching Profesional (Trunk-Based Development / GitFlow Simplificado)",
                        "descripcion": "Adopción de flujos de trabajo de ramas profesionales para equipos ágiles, releases protegidos y hotfixes en producción.",
                        "estado": "propuesto",
                        "justificacion": "Práctica universal exigida a los nuevos ingresos en empresas de desarrollo para no entorpecer el flujo continuo de entregas.",
                        "enfoque": "Aplicación rigurosa del flujo de ramas en el proyecto integrador final.",
                        "tipo": "propuesta"
                    }
                ]
            }
        ]
    }
}

# -------------------------------------------------------------
# 2. Guardar pensum_data.json
# -------------------------------------------------------------
json_path = os.path.join(OUTPUT_DIR, "pensum_data.json")
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(pensum_data, f, indent=2, ensure_ascii=False)

# Estadísticas matemáticas
stats = {}
global_stats = {"total": 0, "adecuado": 0, "revisar": 0, "eliminar": 0, "propuesto": 0}

for cid, cdata in pensum_data.items():
    c_stats = {"total": 0, "adecuado": 0, "revisar": 0, "eliminar": 0, "propuesto": 0}
    for b in cdata["bimestres"]:
        for t in b["temas"]:
            st = t["estado"]
            c_stats[st] += 1
            c_stats["total"] += 1
            global_stats[st] += 1
            global_stats["total"] += 1
    stats[cid] = c_stats

print(f"Dataset generado con {global_stats['total']} temas en total:")
print(f"  - Adecuado:  {global_stats['adecuado']}")
print(f"  - Revisar:   {global_stats['revisar']}")
print(f"  - Eliminar:  {global_stats['eliminar']}")
print(f"  - Propuesta: {global_stats['propuesto']}")

# -------------------------------------------------------------
# 3. Generar index.html Autocontenido y de Alto Impacto
# -------------------------------------------------------------

def generate_html():
    # Helper badges
    status_label_map = {
        "adecuado": "Adecuado",
        "revisar": "Revisar",
        "eliminar": "Eliminar",
        "propuesto": "Propuesta"
    }

    # Generate topic rows HTML for each career
    career_tabs_html = ""
    for cid, cdata in pensum_data.items():
        cs = stats[cid]
        tab_content = f"""
        <div id="tab-{cid}" class="tab-pane">
            <div class="career-header">
                <div class="career-info">
                    <h2>{html.escape(cdata['title'])}</h2>
                    <p class="career-desc">{html.escape(cdata['subtitle'])}</p>
                    <div class="career-meta">
                        <span class="career-meta-item">
                            <svg width="14" height="14" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path></svg>
                            {html.escape(cdata['horas'])}
                        </span>
                        <span class="career-meta-item">
                            <svg width="14" height="14" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path></svg>
                            {html.escape(cdata['docente'])}
                        </span>
                    </div>
                </div>
                <div class="mini-stats">
                    <span class="mini-badge" style="background: rgba(148, 163, 184, 0.15); color: #cbd5e1;">Total: {cs['total']}</span>
                    <span class="mini-badge badge-adecuado">Adecuado: {cs['adecuado']}</span>
                    <span class="mini-badge badge-revisar">Revisar: {cs['revisar']}</span>
                    <span class="mini-badge badge-eliminar">Eliminar: {cs['eliminar']}</span>
                    <span class="mini-badge badge-propuesto">Propuesta: {cs['propuesto']}</span>
                </div>
            </div>
        """

        for b in cdata["bimestres"]:
            tab_content += f"""
            <div class="bimester-block">
                <div class="bimester-header">
                    <div class="bimester-title">
                        <span class="bimester-badge">Bimestre {b['bimestre_num']}</span>
                        <span>{html.escape(b['nombre'])}</span>
                    </div>
                    <span class="text-muted text-xs" style="font-size: 0.775rem;">{len(b['temas'])} núcleos temáticos</span>
                </div>
                <div class="topics-list">
            """

            for t in b["temas"]:
                st = t["estado"]
                badge_text = status_label_map[st]
                badge_class = f"badge-{st}"
                row_class = f"status-{st}"

                just_title_color = "var(--color-green)"
                if st == "revisar": just_title_color = "var(--color-yellow)"
                elif st == "eliminar": just_title_color = "var(--color-red)"
                elif st == "propuesto": just_title_color = "var(--color-proposal-text)"

                tab_content += f"""
                    <div class="topic-row {row_class}" data-status="{st}" data-title="{html.escape(t['nombre'].lower())} {html.escape(t['descripcion'].lower())} {html.escape(t['justificacion'].lower())}">
                        <div class="topic-main">
                            <div class="topic-name">
                                <span>{html.escape(t['nombre'])}</span>
                            </div>
                            <div class="topic-desc">{html.escape(t['descripcion'])}</div>
                            <div>
                                <span class="topic-enfoque">{html.escape(t['enfoque'])}</span>
                            </div>
                        </div>

                        <div class="topic-justification">
                            <span class="justification-title" style="color: {just_title_color};">Diagnóstico e Impacto Industrial:</span>
                            <span class="justification-text">{html.escape(t['justificacion'])}</span>
                        </div>

                        <div class="topic-badge-col">
                            <span class="status-badge {badge_class}">{badge_text}</span>
                        </div>
                    </div>
                """

            tab_content += """
                </div>
            </div>
            """

        tab_content += "</div>"
        career_tabs_html += tab_content

    # Now assemble the complete HTML document
    full_html = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Catálogo y Diagnóstico de Pensum CET | Informática y Computación</title>
    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-body: #0b0f19;
            --bg-surface: #111827;
            --bg-card: #1a2234;
            --bg-card-hover: #222d42;
            --text-primary: #f9fafb;
            --text-secondary: #94a3b8;
            --text-muted: #64748b;
            --border: #2e384d;
            --border-light: #3e4b66;

            /* Status Colors */
            --color-green: #10b981;
            --color-green-bg: rgba(16, 185, 129, 0.12);
            --color-green-border: rgba(16, 185, 129, 0.35);

            --color-yellow: #f59e0b;
            --color-yellow-bg: rgba(245, 158, 11, 0.14);
            --color-yellow-border: rgba(245, 158, 11, 0.4);

            --color-red: #ef4444;
            --color-red-bg: rgba(239, 68, 68, 0.14);
            --color-red-border: rgba(239, 68, 68, 0.4);

            /* Morado / Purple for Proposals */
            --color-proposal: #a855f7;
            --color-proposal-bg: rgba(168, 85, 247, 0.14);
            --color-proposal-border: rgba(168, 85, 247, 0.4);
            --color-proposal-text: #c084fc;

            --radius-sm: 6px;
            --radius-md: 10px;
            --radius-lg: 14px;
            --shadow-sm: 0 2px 8px rgba(0, 0, 0, 0.35);
            --shadow-md: 0 8px 24px rgba(0, 0, 0, 0.45);
        }}

        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            background-color: var(--bg-body);
            color: var(--text-primary);
            font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
            font-size: 14.5px;
            line-height: 1.55;
            -webkit-font-smoothing: antialiased;
        }}

        header {{
            background: linear-gradient(180deg, #162033 0%, var(--bg-surface) 100%);
            border-bottom: 1px solid var(--border);
            padding: 1.25rem 1.5rem 1rem 1.5rem;
            position: sticky;
            top: 0;
            z-index: 100;
            backdrop-filter: blur(12px);
        }}

        .header-container {{
            max-width: 1320px;
            margin: 0 auto;
            display: flex;
            flex-direction: column;
            gap: 0.9rem;
        }}

        .header-top {{
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            flex-wrap: wrap;
            gap: 0.85rem;
        }}

        .brand-badge {{
            display: inline-block;
            background: rgba(56, 189, 248, 0.12);
            color: #38bdf8;
            border: 1px solid rgba(56, 189, 248, 0.3);
            padding: 0.2rem 0.65rem;
            border-radius: 9999px;
            font-size: 0.725rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 0.3rem;
        }}

        .header-title h1 {{
            font-size: 1.65rem;
            font-weight: 800;
            letter-spacing: -0.03em;
            color: #ffffff;
            display: flex;
            align-items: center;
            gap: 0.65rem;
        }}

        .header-title p {{
            color: var(--text-secondary);
            font-size: 0.88rem;
            margin-top: 0.2rem;
            max-width: 900px;
        }}

        .header-actions {{
            display: flex;
            align-items: center;
            gap: 0.65rem;
        }}

        .btn {{
            display: inline-flex;
            align-items: center;
            gap: 0.45rem;
            padding: 0.4rem 0.85rem;
            border-radius: var(--radius-md);
            font-size: 0.8rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s ease;
            text-decoration: none;
            border: 1px solid transparent;
        }}

        .btn-outline {{
            background: transparent;
            color: var(--text-primary);
            border-color: var(--border-light);
        }}

        .btn-outline:hover {{
            background: var(--bg-card);
            border-color: #38bdf8;
        }}

        /* Controls bar */
        .controls-bar {{
            display: flex;
            flex-wrap: wrap;
            gap: 0.65rem;
            align-items: center;
            justify-content: space-between;
            background: rgba(17, 24, 39, 0.75);
            border: 1px solid var(--border);
            padding: 0.5rem 0.85rem;
            border-radius: var(--radius-md);
        }}

        .search-box {{
            flex: 1;
            min-width: 260px;
            position: relative;
        }}

        .search-box input {{
            width: 100%;
            padding: 0.42rem 0.75rem 0.42rem 2.2rem;
            background: #101625;
            border: 1px solid var(--border);
            border-radius: var(--radius-md);
            color: var(--text-primary);
            font-size: 0.825rem;
            outline: none;
            transition: border-color 0.2s;
        }}

        .search-box input:focus {{
            border-color: #38bdf8;
            box-shadow: 0 0 0 2px rgba(56, 189, 248, 0.2);
        }}

        .search-icon {{
            position: absolute;
            left: 0.75rem;
            top: 50%;
            transform: translateY(-50%);
            color: var(--text-muted);
            font-size: 0.8rem;
            pointer-events: none;
        }}

        .filter-pills {{
            display: flex;
            flex-wrap: wrap;
            gap: 0.35rem;
        }}

        .pill-btn {{
            background: var(--bg-card);
            border: 1px solid var(--border);
            color: var(--text-secondary);
            padding: 0.26rem 0.65rem;
            border-radius: 9999px;
            font-size: 0.775rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.15s ease;
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
        }}

        .pill-btn:hover {{
            color: var(--text-primary);
            background: var(--bg-card-hover);
        }}

        .pill-btn.active {{
            background: #0284c7;
            color: #ffffff;
            border-color: #38bdf8;
        }}

        .pill-btn.pill-green.active {{
            background: var(--color-green);
            border-color: var(--color-green);
            color: #022c22;
        }}

        .pill-btn.pill-yellow.active {{
            background: var(--color-yellow);
            border-color: var(--color-yellow);
            color: #451a03;
        }}

        .pill-btn.pill-red.active {{
            background: var(--color-red);
            border-color: var(--color-red);
            color: #ffffff;
        }}

        .pill-btn.pill-proposal.active {{
            background: var(--color-proposal);
            border-color: #c084fc;
            color: #ffffff;
        }}

        /* Navigation tabs */
        .nav-tabs {{
            display: flex;
            overflow-x: auto;
            border-bottom: 1px solid var(--border);
            background: #0d1322;
        }}

        .nav-tabs-container {{
            max-width: 1320px;
            margin: 0 auto;
            width: 100%;
            display: flex;
            gap: 0.25rem;
            padding: 0 1.5rem;
        }}

        .tab-btn {{
            padding: 0.75rem 1.15rem;
            background: transparent;
            border: none;
            border-bottom: 2px solid transparent;
            color: var(--text-secondary);
            font-size: 0.85rem;
            font-weight: 600;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 0.45rem;
            white-space: nowrap;
            transition: all 0.2s;
        }}

        .tab-btn:hover {{
            color: var(--text-primary);
            background: rgba(255, 255, 255, 0.02);
        }}

        .tab-btn.active {{
            color: #38bdf8;
            border-bottom-color: #38bdf8;
            background: rgba(14, 165, 233, 0.06);
        }}

        /* Main */
        main {{
            max-width: 1320px;
            margin: 1.6rem auto;
            padding: 0 1.5rem;
        }}

        /* Stats grid */
        .stats-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
            gap: 1.1rem;
            margin-bottom: 1.85rem;
        }}

        .stat-card {{
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            padding: 1.15rem 1.25rem;
            display: flex;
            flex-direction: column;
            gap: 0.35rem;
            box-shadow: var(--shadow-sm);
            position: relative;
            cursor: pointer;
            transition: transform 0.2s, border-color 0.2s;
        }}

        .stat-card:hover {{
            transform: translateY(-2px);
            border-color: var(--border-light);
        }}

        .stat-card::before {{
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 3px;
        }}

        .stat-card.card-total::before {{ background: #94a3b8; }}
        .stat-card.card-green::before {{ background: var(--color-green); }}
        .stat-card.card-yellow::before {{ background: var(--color-yellow); }}
        .stat-card.card-red::before {{ background: var(--color-red); }}
        .stat-card.card-proposal::before {{ background: var(--color-proposal); }}

        .stat-label {{
            font-size: 0.775rem;
            color: var(--text-secondary);
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.04em;
        }}

        .stat-value {{
            font-size: 1.85rem;
            font-weight: 800;
            color: #ffffff;
            line-height: 1.1;
        }}

        .stat-desc {{
            font-size: 0.775rem;
            color: var(--text-muted);
        }}

        /* Career header */
        .career-header {{
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            padding: 1.35rem 1.5rem;
            margin-bottom: 1.6rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 1.2rem;
        }}

        .career-info h2 {{
            font-size: 1.35rem;
            font-weight: 700;
            color: #ffffff;
            letter-spacing: -0.02em;
        }}

        .career-desc {{
            color: #38bdf8;
            font-size: 0.875rem;
            margin-top: 0.2rem;
            font-weight: 500;
        }}

        .career-meta {{
            display: flex;
            flex-wrap: wrap;
            gap: 1rem;
            margin-top: 0.65rem;
            font-size: 0.8rem;
            color: var(--text-secondary);
        }}

        .career-meta-item {{
            display: inline-flex;
            align-items: center;
            gap: 0.35rem;
        }}

        .mini-stats {{
            display: flex;
            flex-wrap: wrap;
            gap: 0.45rem;
            margin-top: 0.15rem;
        }}

        .mini-badge {{
            padding: 0.2rem 0.55rem;
            border-radius: var(--radius-sm);
            font-size: 0.725rem;
            font-weight: 600;
            display: inline-flex;
            align-items: center;
            gap: 0.3rem;
        }}

        /* Bimester block */
        .bimester-block {{
            background: var(--bg-surface);
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            margin-bottom: 1.85rem;
            overflow: hidden;
            box-shadow: var(--shadow-sm);
        }}

        .bimester-header {{
            background: #162033;
            padding: 0.85rem 1.35rem;
            border-bottom: 1px solid var(--border);
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 0.65rem;
        }}

        .bimester-title {{
            font-size: 1.025rem;
            font-weight: 700;
            color: #ffffff;
            display: flex;
            align-items: center;
            gap: 0.55rem;
        }}

        .bimester-badge {{
            background: rgba(255, 255, 255, 0.08);
            padding: 0.18rem 0.55rem;
            border-radius: 9999px;
            font-size: 0.725rem;
            font-weight: 600;
            color: var(--text-secondary);
        }}

        /* Topic Rows */
        .topics-list {{
            display: flex;
            flex-direction: column;
        }}

        .topic-row {{
            padding: 1.15rem 1.35rem;
            display: grid;
            grid-template-columns: 1fr 1.35fr 110px;
            gap: 1.25rem;
            align-items: flex-start;
            border-bottom: 1px solid rgba(55, 65, 81, 0.45);
            transition: background 0.15s ease;
        }}

        .topic-row:last-child {{
            border-bottom: none;
        }}

        .topic-row:hover {{
            background: rgba(26, 34, 52, 0.5);
        }}

        .topic-row.status-adecuado {{
            border-left: 4px solid var(--color-green);
        }}

        .topic-row.status-revisar {{
            border-left: 4px solid var(--color-yellow);
            background: rgba(245, 158, 11, 0.025);
        }}

        .topic-row.status-eliminar {{
            border-left: 4px solid var(--color-red);
            background: rgba(239, 68, 68, 0.035);
        }}

        .topic-row.status-propuesto {{
            border-left: 4px solid var(--color-proposal);
            background: rgba(168, 85, 247, 0.035);
        }}

        .topic-main {{
            display: flex;
            flex-direction: column;
            gap: 0.35rem;
        }}

        .topic-name {{
            font-size: 0.95rem;
            font-weight: 700;
            color: #ffffff;
            line-height: 1.35;
        }}

        .topic-desc {{
            font-size: 0.825rem;
            color: var(--text-secondary);
            line-height: 1.48;
        }}

        .topic-enfoque {{
            font-size: 0.75rem;
            color: #38bdf8;
            margin-top: 0.15rem;
            font-family: 'JetBrains Mono', monospace;
            background: rgba(56, 189, 248, 0.08);
            padding: 0.18rem 0.45rem;
            border-radius: var(--radius-sm);
            display: inline-block;
        }}

        .topic-row.status-propuesto .topic-enfoque {{
            color: var(--color-proposal-text);
            background: var(--color-proposal-bg);
        }}

        .topic-justification {{
            background: rgba(10, 15, 25, 0.5);
            border: 1px solid var(--border);
            border-radius: var(--radius-sm);
            padding: 0.65rem 0.85rem;
            font-size: 0.8rem;
            display: flex;
            flex-direction: column;
            gap: 0.25rem;
        }}

        .justification-title {{
            font-size: 0.7rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.04em;
        }}

        .justification-text {{
            color: #cbd5e1;
            line-height: 1.42;
        }}

        .topic-badge-col {{
            display: flex;
            flex-direction: column;
            align-items: flex-end;
            gap: 0.35rem;
        }}

        /* Status Badge - Single word */
        .status-badge {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            padding: 0.22rem 0.55rem;
            border-radius: 9999px;
            font-size: 0.7rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.03em;
            white-space: nowrap;
        }}

        .badge-adecuado {{
            background: var(--color-green-bg);
            color: var(--color-green);
            border: 1px solid var(--color-green-border);
        }}

        .badge-revisar {{
            background: var(--color-yellow-bg);
            color: var(--color-yellow);
            border: 1px solid var(--color-yellow-border);
        }}

        .badge-eliminar {{
            background: var(--color-red-bg);
            color: var(--color-red);
            border: 1px solid var(--color-red-border);
        }}

        .badge-propuesto {{
            background: var(--color-proposal-bg);
            color: var(--color-proposal-text);
            border: 1px solid var(--color-proposal-border);
        }}

        /* Two columns */
        .grid-two-col {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(460px, 1fr));
            gap: 1.4rem;
            margin-bottom: 2.2rem;
        }}

        .info-panel {{
            background: var(--bg-card);
            border: 1px solid var(--border);
            border-radius: var(--radius-lg);
            padding: 1.4rem;
            display: flex;
            flex-direction: column;
            gap: 0.95rem;
        }}

        .info-panel h3 {{
            font-size: 1.15rem;
            color: #ffffff;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}

        .criteria-list {{
            list-style: none;
            display: flex;
            flex-direction: column;
            gap: 0.85rem;
        }}

        .criteria-item {{
            display: flex;
            gap: 0.7rem;
            font-size: 0.85rem;
            line-height: 1.48;
            color: var(--text-secondary);
        }}

        .criteria-icon {{
            font-size: 1.05rem;
            flex-shrink: 0;
            margin-top: 0.1rem;
        }}

        .criteria-content strong {{
            color: #ffffff;
            display: block;
            margin-bottom: 0.12rem;
        }}

        /* Tab panes */
        .tab-pane {{
            display: none;
        }}

        .tab-pane.active {{
            display: block;
        }}

        /* Footer */
        footer {{
            border-top: 1px solid var(--border);
            background: #0d1322;
            padding: 2.2rem 1.5rem;
            color: var(--text-muted);
            font-size: 0.825rem;
            text-align: center;
            margin-top: 3.5rem;
        }}

        .footer-container {{
            max-width: 1200px;
            margin: 0 auto;
            display: flex;
            flex-direction: column;
            gap: 0.45rem;
            align-items: center;
        }}

        /* Responsive */
        @media (max-width: 960px) {{
            .topic-row {{
                grid-template-columns: 1fr;
                gap: 0.8rem;
            }}
            .topic-badge-col {{
                align-items: flex-start;
                order: -1;
            }}
            .grid-two-col {{
                grid-template-columns: 1fr;
            }}
        }}

        @media print {{
            header, .controls-bar, .nav-tabs, footer, .btn {{
                display: none !important;
            }}
            body {{
                background: #ffffff !important;
                color: #000000 !important;
            }}
            .bimester-block, .stat-card, .topic-row, .info-panel {{
                border: 1px solid #cccccc !important;
                background: #ffffff !important;
                color: #000000 !important;
            }}
            .topic-name, .bimester-title, h1, h2, h3 {{
                color: #000000 !important;
            }}
            .topic-desc, .justification-text {{
                color: #333333 !important;
            }}
        }}
    </style>
</head>
<body>

    <!-- Header -->
    <header>
        <div class="header-container">
            <div class="header-top">
                <div class="header-title">
                    <span class="brand-badge">Fundación Kinal • Centro Escolar Técnico (CET)</span>
                    <h1>Auditoría Curricular y Catálogo de Pensum</h1>
                    <p>Diagnóstico técnico de temas curriculares de Informática frente a las demandas de la industria del software en Guatemala, estándares del CNB (MINEDUC) y articulación con la Escuela Técnica Superior (ETS).</p>
                </div>
                <div class="header-actions">
                    <button class="btn btn-outline" onclick="window.print()">
                        <svg width="14" height="14" fill="currentColor" viewBox="0 0 16 16"><path d="M2.5 8a.5.5 0 1 0 0-1 .5.5 0 0 0 0 1z"/><path d="M5 1a2 2 0 0 0-2 2v2H2a2 2 0 0 0-2 2v3a2 2 0 0 0 2 2h1v1a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2v-1h1a2 2 0 0 0 2-2V7a2 2 0 0 0-2-2h-1V3a2 2 0 0 0-2-2H5zM4 3a1 1 0 0 1 1-1h6a1 1 0 0 1 1 1v2H4V3zm1 5a2 2 0 0 0-2 2v1H2a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h12a1 1 0 0 1 1 1v3a1 1 0 0 1-1 1h-1v-1a2 2 0 0 0-2-2H5zm7 2v3a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1v-3a1 1 0 0 1 1-1h6a1 1 0 0 1 1 1z"/></svg>
                        Imprimir / PDF
                    </button>
                </div>
            </div>

            <!-- Controls bar -->
            <div class="controls-bar">
                <div class="search-box">
                    <span class="search-icon">🔍</span>
                    <input type="text" id="searchInput" placeholder="Filtrar por tecnología, concepto o palabra clave (ej. React, Docker, SQL, JWT)..." oninput="filterTopics()">
                </div>
                <div class="filter-pills">
                    <button class="pill-btn active" onclick="setStatusFilter('all', this)">Todos ({global_stats['total']})</button>
                    <button class="pill-btn pill-green" onclick="setStatusFilter('adecuado', this)">Adecuado ({global_stats['adecuado']})</button>
                    <button class="pill-btn pill-yellow" onclick="setStatusFilter('revisar', this)">Revisar ({global_stats['revisar']})</button>
                    <button class="pill-btn pill-red" onclick="setStatusFilter('eliminar', this)">Eliminar ({global_stats['eliminar']})</button>
                    <button class="pill-btn pill-proposal" onclick="setStatusFilter('propuesto', this)">Propuesta ({global_stats['propuesto']})</button>
                </div>
            </div>
        </div>
    </header>

    <!-- Navigation Tabs -->
    <div class="nav-tabs">
        <div class="nav-tabs-container">
            <button class="tab-btn active" onclick="switchTab('resumen', this)">📊 Resumen Ejecutivo y Diagnóstico</button>
            <button class="tab-btn" onclick="switchTab('cuarto_informatica', this)">💻 4to Perito en Informática</button>
            <button class="tab-btn" onclick="switchTab('quinto_informatica', this)">⚙️ 5to Perito en Informática</button>
            <button class="tab-btn" onclick="switchTab('sexto_informatica', this)">🚀 6to Perito en Informática</button>
        </div>
    </div>

    <!-- Main Content -->
    <main>

        <!-- Tab 0: Resumen Ejecutivo -->
        <div id="tab-resumen" class="tab-pane active">
            <!-- Stats Grid -->
            <div class="stats-grid">
                <div class="stat-card card-total" onclick="switchTabAndFilter('all')">
                    <span class="stat-label">Temas Evaluados</span>
                    <span class="stat-value">{global_stats['total']}</span>
                    <span class="stat-desc">4to, 5to y 6to Perito CET 2026</span>
                </div>
                <div class="stat-card card-green" onclick="switchTabAndFilter('adecuado')">
                    <span class="stat-label">Adecuado (Industria)</span>
                    <span class="stat-value" style="color: var(--color-green);">{global_stats['adecuado']}</span>
                    <span class="stat-desc">{global_stats['adecuado']/global_stats['total']*100:.1f}% alineado con el mercado</span>
                </div>
                <div class="stat-card card-yellow" onclick="switchTabAndFilter('revisar')">
                    <span class="stat-label">Revisar / Acotar</span>
                    <span class="stat-value" style="color: var(--color-yellow);">{global_stats['revisar']}</span>
                    <span class="stat-desc">Requieren enfoque o simplificación</span>
                </div>
                <div class="stat-card card-red" onclick="switchTabAndFilter('eliminar')">
                    <span class="stat-label">Eliminar (Obsoleto)</span>
                    <span class="stat-value" style="color: var(--color-red);">{global_stats['eliminar']}</span>
                    <span class="stat-desc">Prácticas desfasadas en desuso</span>
                </div>
                <div class="stat-card card-proposal" onclick="switchTabAndFilter('propuesto')">
                    <span class="stat-label">Propuesta Industria</span>
                    <span class="stat-value" style="color: var(--color-proposal-text);">{global_stats['propuesto']}</span>
                    <span class="stat-desc">Habilidades de alta demanda añadidas</span>
                </div>
            </div>

            <!-- Two Column Diagnostic Matrix -->
            <div class="grid-two-col">
                <div class="info-panel">
                    <h3>📌 Criterios de Evaluación y Diagnóstico</h3>
                    <ul class="criteria-list">
                        <li class="criteria-item">
                            <span class="criteria-icon">🟢</span>
                            <div class="criteria-content">
                                <strong>Adecuado ({global_stats['adecuado']} temas - {global_stats['adecuado']/global_stats['total']*100:.1f}%)</strong>
                                Contenidos modernos que responden directamente a lo que demanda el mercado laboral guatemalteco y regional para desarrolladores junior: programación orientada a objetos en Java, diseño relacional SQL y NoSQL, APIs RESTful con Node.js/Spring Boot, frontend en React, Git colaborativo y testing básico.
                            </div>
                        </li>
                        <li class="criteria-item">
                            <span class="criteria-icon">🟡</span>
                            <div class="criteria-content">
                                <strong>Revisar ({global_stats['revisar']} temas - {global_stats['revisar']/global_stats['total']*100:.1f}%)</strong>
                                Contenidos con sobrecarga conceptual o descontextualización: Abstract Factory/Builder en 4to perito (sobreingeniería prematura); interfaces de escritorio JavaFX exclusivas; dispersión simultánea de 3 stacks backend/frontend en 7 semanas; o instrumentación compleja de Kubernetes/telemetría distribuida que sobrepasa el nivel perito.
                            </div>
                        </li>
                        <li class="criteria-item">
                            <span class="criteria-icon">🔴</span>
                            <div class="criteria-content">
                                <strong>Eliminar ({global_stats['eliminar']} temas - {global_stats['eliminar']/global_stats['total']*100:.1f}%)</strong>
                                Enfoques descontinuados y vicios técnicos: uso prolongado de PseInt en 4to grado; esquemas relacionales huérfanos sin integridad referencial; persistencia arcaica en archivos planos (.txt/.dat); maquetación de interfaces con Java Swing antiguo; y documentación masiva en cascada tipo RUP.
                            </div>
                        </li>
                        <li class="criteria-item">
                            <span class="criteria-icon">🟣</span>
                            <div class="criteria-content">
                                <strong>Propuesta ({global_stats['propuesto']} temas - {global_stats['propuesto']/global_stats['total']*100:.1f}%)</strong>
                                Habilidades críticas altamente cotizadas por reclutadores en Guatemala: Higiene de ciberseguridad OWASP Top 10 para juniors; colecciones de pruebas de API con Postman; tipado estricto con TypeScript; Git Flow profesional y Conventional Commits; gestión segura de secretos (.env); y publicación en vivo de un portafolio cloud.
                            </div>
                        </li>
                    </ul>
                </div>

                <div class="info-panel">
                    <h3>🎯 Alineación Normativa: CNB, Industria y ETS</h3>
                    <ul class="criteria-list">
                        <li class="criteria-item">
                            <span class="criteria-icon">🏛️</span>
                            <div class="criteria-content">
                                <strong>Alineación con el CNB (MINEDUC Guatemala)</strong>
                                Cumple y supera las competencias del Currículo Nacional Base para <em>Perito en Informática / Computación</em>: pensamiento lógico algorítmico (Comp. 1), desarrollo POO modular (Comp. 2), bases de datos íntegras (Comp. 3), aplicaciones web cliente-servidor (Comp. 4) y gestión ética de proyectos ágiles (Comp. 6).
                            </div>
                        </li>
                        <li class="criteria-item">
                            <span class="criteria-icon">🏢</span>
                            <div class="criteria-content">
                                <strong>Demanda Laboral de la Industria en Guatemala</strong>
                                El sector bancario (BI, Banrural, G&T), empresas de telecomunicaciones (Claro, Tigo), firmas de outsourcing y startups locales buscan programadores que dominen Git, APIs RESTful con JSON/JWT, bases de datos SQL bien estructuradas, frontend responsivo y testing automatizado para integrarse de inmediato a squads ágiles.
                            </div>
                        </li>
                        <li class="criteria-item">
                            <span class="criteria-icon">🎓</span>
                            <div class="criteria-content">
                                <strong>Articulación con ETS (Escuela Técnica Superior - TSU / DQR 6)</strong>
                                Delimitación clara de niveles formativos: el nivel Perito (CET) forma competencias terminales operativas de construcción, testing y despliegue de software comercial. En ETS (nivel terciario universitario) se desarrollan arquitecturas de microservicios distribuidos a gran escala, orquestación con Kubernetes, ciberseguridad ofensiva/defensiva y modelos de Inteligencia Artificial avanzados.
                            </div>
                        </li>
                        <li class="criteria-item">
                            <span class="criteria-icon">🤖</span>
                            <div class="criteria-content">
                                <strong>Eje Transversal IA CoWork en Fundación Kinal</strong>
                                La Inteligencia Artificial generativa se integra como copiloto de productividad diaria, condicionada estrictamente a la <strong>validación humana obligatoria</strong>, trazabilidad del prompt y capacidad del estudiante de defender y refactorizar verbalmente cada línea de código entregada.
                            </div>
                        </li>
                    </ul>
                </div>
            </div>

            <!-- Resumen por Grados -->
            <div class="bimester-block">
                <div class="bimester-header">
                    <div class="bimester-title">
                        <span>Resumen Comparativo por Nivel Formativo (CET Informática)</span>
                    </div>
                </div>
                <div style="padding: 1.25rem 1.4rem; overflow-x: auto;">
                    <table style="width: 100%; border-collapse: collapse; font-size: 0.85rem;">
                        <thead>
                            <tr style="border-bottom: 1px solid var(--border); text-align: left; color: var(--text-secondary);">
                                <th style="padding: 0.65rem 0.85rem;">Grado / Carrera</th>
                                <th style="padding: 0.65rem 0.85rem;">Bimestres</th>
                                <th style="padding: 0.65rem 0.85rem;">Enfoque Formativo</th>
                                <th style="padding: 0.65rem 0.85rem;">Total Temas</th>
                                <th style="padding: 0.65rem 0.85rem; color: var(--color-green);">Adecuado</th>
                                <th style="padding: 0.65rem 0.85rem; color: var(--color-yellow);">Revisar</th>
                                <th style="padding: 0.65rem 0.85rem; color: var(--color-red);">Eliminar</th>
                                <th style="padding: 0.65rem 0.85rem; color: var(--color-proposal-text);">Propuesta</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr style="border-bottom: 1px solid rgba(55, 65, 81, 0.4); cursor: pointer;" onclick="switchTab('cuarto_informatica', document.querySelectorAll('.tab-btn')[1])">
                                <td style="padding: 0.85rem; font-weight: 700; color: #ffffff;">4to Perito en Informática</td>
                                <td style="padding: 0.85rem;">B1 a B4 (4 Bimestres)</td>
                                <td style="padding: 0.85rem; color: var(--text-secondary);">Algoritmia, POO en Java, SQL/NoSQL, Git y Metodologías Ágiles</td>
                                <td style="padding: 0.85rem; font-weight: 700;">{stats['cuarto_informatica']['total']}</td>
                                <td style="padding: 0.85rem; color: var(--color-green); font-weight: 700;">{stats['cuarto_informatica']['adecuado']}</td>
                                <td style="padding: 0.85rem; color: var(--color-yellow); font-weight: 700;">{stats['cuarto_informatica']['revisar']}</td>
                                <td style="padding: 0.85rem; color: var(--color-red); font-weight: 700;">{stats['cuarto_informatica']['eliminar']}</td>
                                <td style="padding: 0.85rem; color: var(--color-proposal-text); font-weight: 700;">{stats['cuarto_informatica']['propuesto']}</td>
                            </tr>
                            <tr style="border-bottom: 1px solid rgba(55, 65, 81, 0.4); cursor: pointer;" onclick="switchTab('quinto_informatica', document.querySelectorAll('.tab-btn')[2])">
                                <td style="padding: 0.85rem; font-weight: 700; color: #ffffff;">5to Perito en Informática</td>
                                <td style="padding: 0.85rem;">B1 a B4 (4 Bimestres)</td>
                                <td style="padding: 0.85rem; color: var(--text-secondary);">Ingeniería de Requerimientos, APIs RESTful, Testing Automatizado y Despliegue</td>
                                <td style="padding: 0.85rem; font-weight: 700;">{stats['quinto_informatica']['total']}</td>
                                <td style="padding: 0.85rem; color: var(--color-green); font-weight: 700;">{stats['quinto_informatica']['adecuado']}</td>
                                <td style="padding: 0.85rem; color: var(--color-yellow); font-weight: 700;">{stats['quinto_informatica']['revisar']}</td>
                                <td style="padding: 0.85rem; color: var(--color-red); font-weight: 700;">{stats['quinto_informatica']['eliminar']}</td>
                                <td style="padding: 0.85rem; color: var(--color-proposal-text); font-weight: 700;">{stats['quinto_informatica']['propuesto']}</td>
                            </tr>
                            <tr style="cursor: pointer;" onclick="switchTab('sexto_informatica', document.querySelectorAll('.tab-btn')[3])">
                                <td style="padding: 0.85rem; font-weight: 700; color: #ffffff;">6to Perito en Informática</td>
                                <td style="padding: 0.85rem;">B1 a B3 (3 Bimestres Lectivos)</td>
                                <td style="padding: 0.85rem; color: var(--text-secondary);">Full-Stack React + Node.js/Spring Boot, Docker, Cloud y DevOps</td>
                                <td style="padding: 0.85rem; font-weight: 700;">{stats['sexto_informatica']['total']}</td>
                                <td style="padding: 0.85rem; color: var(--color-green); font-weight: 700;">{stats['sexto_informatica']['adecuado']}</td>
                                <td style="padding: 0.85rem; color: var(--color-yellow); font-weight: 700;">{stats['sexto_informatica']['revisar']}</td>
                                <td style="padding: 0.85rem; color: var(--color-red); font-weight: 700;">{stats['sexto_informatica']['eliminar']}</td>
                                <td style="padding: 0.85rem; color: var(--color-proposal-text); font-weight: 700;">{stats['sexto_informatica']['propuesto']}</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>

        <!-- Career Tabs -->
        {career_tabs_html}

    </main>

    <!-- Footer -->
    <footer>
        <div class="footer-container">
            <p><strong>Fundación Kinal • Centro Escolar Técnico (CET)</strong></p>
            <p>Auditoría y Diagnóstico de Pensum de Informática 2026 | Sistema de Formación Dual en Alternancia & Marco DQR</p>
            <p class="text-xs" style="color: var(--text-muted); font-size: 0.75rem;">Documento técnico generado a partir de las Propuestas Curriculares Actualizadas v2 y Programas Oficiales del SGC.</p>
        </div>
    </footer>

    <!-- Interactive Logic Script -->
    <script>
        let currentTab = 'resumen';
        let currentStatusFilter = 'all';

        function switchTab(tabId, btn) {{
            currentTab = tabId;
            document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
            if (btn) btn.classList.add('active');

            document.querySelectorAll('.tab-pane').forEach(p => p.classList.remove('active'));
            const targetPane = document.getElementById('tab-' + tabId);
            if (targetPane) targetPane.classList.add('active');

            filterTopics();
            window.scrollTo({{ top: 0, behavior: 'smooth' }});
        }}

        function setStatusFilter(status, btn) {{
            currentStatusFilter = status;
            document.querySelectorAll('.pill-btn').forEach(b => b.classList.remove('active'));
            if (btn) btn.classList.add('active');

            if (currentTab === 'resumen') {{
                switchTab('cuarto_informatica', document.querySelectorAll('.tab-btn')[1]);
            }}

            filterTopics();
        }}

        function switchTabAndFilter(status) {{
            currentStatusFilter = status;
            document.querySelectorAll('.pill-btn').forEach(b => {{
                b.classList.remove('active');
                if (status === 'all' && b.innerText.includes('Todos')) b.classList.add('active');
                if (status === 'adecuado' && b.innerText.includes('Adecuado')) b.classList.add('active');
                if (status === 'revisar' && b.innerText.includes('Revisar')) b.classList.add('active');
                if (status === 'eliminar' && b.innerText.includes('Eliminar')) b.classList.add('active');
                if (status === 'propuesto' && b.innerText.includes('Propuesta')) b.classList.add('active');
            }});
            switchTab('cuarto_informatica', document.querySelectorAll('.tab-btn')[1]);
            filterTopics();
        }}

        function filterTopics() {{
            const query = (document.getElementById('searchInput').value || '').toLowerCase().trim();
            const activePane = document.getElementById('tab-' + currentTab);
            if (!activePane) return;

            const rows = document.querySelectorAll('.topic-row');

            rows.forEach(row => {{
                const rowStatus = row.getAttribute('data-status');
                const rowTitle = row.getAttribute('data-title');

                const matchesStatus = (currentStatusFilter === 'all') || (rowStatus === currentStatusFilter);
                const matchesQuery = !query || rowTitle.includes(query);

                if (matchesStatus && matchesQuery) {{
                    row.style.display = 'grid';
                }} else {{
                    row.style.display = 'none';
                }}
            }});

            // Handle bimester block visibility
            document.querySelectorAll('.bimester-block').forEach(block => {{
                let count = 0;
                block.querySelectorAll('.topic-row').forEach(r => {{
                    if (r.style.display !== 'none') count++;
                }});

                if (count === 0 && (currentStatusFilter !== 'all' || query !== '')) {{
                    block.style.display = 'none';
                }} else {{
                    block.style.display = 'block';
                }}
            }});
        }}
    </script>
</body>
</html>
"""
    html_path = os.path.join(OUTPUT_DIR, "index.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(full_html)
    print(f"Portal HTML generado exitosamente en: {html_path}")

generate_html()

# -------------------------------------------------------------
# 4. Generar README.md del Repositorio de Informática
# -------------------------------------------------------------
readme_content = f"""# Catálogo de Pensum CET y Diagnóstico Curricular • Informática

Este repositorio contiene la plataforma web estática para el análisis y auditoría técnica de los pensums de estudio de las tres carreras de nivel diversificado del **Centro Escolar Técnico (CET) de Fundación Kinal**:

1. **Cuarto Perito en Informática** (Ciclo Troncal - Bimestres 1 al 4)
2. **Quinto Perito en Informática** (Ciclo de Ingeniería de Software - Bimestres 1 al 4)
3. **Sexto Perito en Informática** (Ciclo Full-Stack, Cloud y DevOps - Bimestres 1 al 3)

> **Nota de Alcance:** En 6to Perito en Informática la formación lectiva en aula abarca los **Bimestres 1, 2 y 3**. El **Bimestre 4** está reservado institucionalmente para la **Práctica Supervisada / Formación en Centros de Trabajo**.

---

## 🎯 Enfoque y Criterios del Diagnóstico

El catálogo evalúa **{global_stats['total']} núcleos temáticos** extraídos de las propuestas curriculares oficiales 2026 (que incorporan inteligencia artificial como coworker y proyectos integradores), presentándolos de forma sintética (sin cronogramas semanales ni dosificaciones de clase):

* 🟢 **Adecuado ({global_stats['adecuado']} temas - {global_stats['adecuado']/global_stats['total']*100:.1f}%):** Temas acordes con la demanda laboral de la industria guatemalteca para técnicos de nivel medio/diversificado (Java, SQL, POO, MVC, Git, Scrum, REST APIs, React, Docker).
* 🟡 **Revisar ({global_stats['revisar']} temas - {global_stats['revisar']/global_stats['total']*100:.1f}%):** Temas que requieren acotación, modernización o simplificación para no sobrecargar el nivel perito (ej. Abstract Factory/Builder en 4to grado; dispersión de múltiples stacks backend/frontend en semanas consecutivas; Kubernetes y telemetría distribuida compleja que corresponden a ETS).
* 🔴 **Eliminar ({global_stats['eliminar']} temas - {global_stats['eliminar']/global_stats['total']*100:.1f}%):** Tecnologías y prácticas obsoletas en desuso comercial (uso prolongado de PseInt más allá de 2 semanas; almacenamiento desnormalizado sin foreign keys; persistencia en archivos planos .txt/.dat para sistemas multiusuario; desarrollo con Java Swing GridBagLayout manual; documentación exhaustiva en cascada RUP).
* 🟣 **Propuesta ({global_stats['propuesto']} temas - {global_stats['propuesto']/global_stats['total']*100:.1f}%):** Competencias altamente demandadas en Guatemala no cubiertas (Higiene de ciberseguridad OWASP Top 10 para juniors; colecciones de pruebas automatizadas con Postman/Newman; tipado estricto con TypeScript; Git Flow profesional y Conventional Commits; gestión segura de secretos .env; despliegue cloud de portafolio web personal).

---

## 🏛️ Marco Normativo y Articulación

* **CNB (Curriculum Nacional Base de MINEDUC):** Alineación con las 6 competencias de área para *Perito en Computación / Informática*.
* **Articulación con ETS (Escuela Técnica Superior - TSU / DQR 6):** Delimitación clara entre las competencias terminales operativas de diversificado (desarrollo, testing, dockerización básica y despliegue de aplicaciones comerciales) y las competencias de nivel terciario en ETS (microservicios distribuidos a gran escala, clústeres Kubernetes, ciberseguridad ofensiva y machine learning avanzado).
* **Eje Transversal IA CoWork:** Adopción de IA generativa bajo el principio de **validación humana obligatoria**, trazabilidad de prompts y defensa técnica verbal de todo código desarrollado.

---

## 📂 Archivos del Portal Local

* `index.html`: Dashboard web interactivo 100% autocontenido y responsivo (dark theme, filtros dinámicos, búsqueda en tiempo real, resumen ejecutivo y vista para impresión/PDF).
* `pensum_data.json`: Especificación estructurada de los 110 núcleos temáticos con descripciones, enfoques y justificaciones técnicas de la industria.
* `README.md`: Este documento descriptivo.
"""

readme_path = os.path.join(OUTPUT_DIR, "README.md")
with open(readme_path, "w", encoding="utf-8") as f:
    f.write(readme_content)

print(f"README generado exitosamente en: {readme_path}")
