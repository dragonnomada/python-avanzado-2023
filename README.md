# Curso de Python Avanzado

> **THINCRS**
>
> TAE - FORMACIÓN DE TALENTO ALTAMENTE ESPECIALIZADO 2023

Profesor: [Alan Badillo Salas](alan@nomadacode.com)

## Introducción

En este curso aprenderás:

* Realizar pruebas de rendimiento y perfilado de memoria para aislar el código de bajo rendimiento
* Usar optimizadores puros de Python y estructuras de datos para mejorar los tiempos de ejecución
* Dominar las operaciones rápidas en arreglos de Numpy, Pandas y Xarray
* Usar CPython para generar código eficiente de C y lograr el rendimiento a nivel de C
* Implementar concurrencia con AsyncIO y RxPy
* Usar procesamiento paralelo en GPU con Theano y Tensorflow
* Generar solicitudes web simultáneas y en sincronía
* Entender y evitar los bloqueos internos en la concurrencia y el dilema de los filósofos cenando
* Entender el problema de la inanición por ejecución priorizada y el dilema de lectores-escritores
* Usar los patrones de diseño en Python como (fábrica, constructor, creacionales, adaptador, decorador, de puente y fachada)

Prerrequisitos:

* Fuerte dominio del lenguaje Python y su sintaxis (uso de variables, condicionales, iteradores, funciones)
* Nociones matemáticas de álgebra y cálculo (es altamente recomendado haber cursado álgebra discreta, álgebra lineal, cálculo diferencial y optimización)
* Tener nociones de programación en cualquier lenguaje (es altamente recomendado haber cursado estructuras de datos y programación orientada a objetos)
* Tener una formación técnica, de licenciatura o ingeniería computacional, matemáticas o afín
* Es recomendable haber cursado Ciencia de Datos, Machine Learning, Minería de Datos o Bases de Datos
* Tener capacidad de Programación y Resolución de Algoritmos en tiempo real

## Contenido

> Módulo 1: Benchmarking y elaboración de perfiles

    - Diseñando tu aplicación
    - Escribir pruebas y puntos de referencia
    - Escribir mejores pruebas y puntos de referencia con pytest-benchmark
    - Encontrar cuellos de botella con cProfile
    - Optimizando nuestro código
    - Usando el módulo dis
    - Generación de perfiles de uso de memoria con memory_profiler

> Módulo 2: Optimizaciones de Python puro

    - Usar los algoritmos y las estructuras de datos correctos
    - Eficiencia mejorada con almacenamiento en caché y memorización
    - Iteración eficiente con comprensiones y generadores

> Módulo 3: Operaciones de matrices rápidas con NumPy, Pandas y Xarray

    - Comenzando con NumPy
    - Reescribiendo el simulador de partículas en NumPy
    - Alcanzar un rendimiento óptimo con numexpr
    - Trabajar con datos de estilo de base de datos con pandas
    - Datos etiquetados de alto rendimiento con xarray

> Módulo 4: Rendimiento de C con Cython

    - Compilando extensiones de Cython
    - Agregar tipos estáticos
    - Compartir declaraciones
    - Trabajando con arreglos
    - Usando un simulador de partículas en Cython
    - Perfilado Cython
    - Usando Cython con Jupyter

> Módulo 5: Implementación de concurrencia

    - Programación asíncrona
    - El framework asyncio
    - Programación reactiva

> Módulo 6: Procesamiento en paralelo

    - Introducción a la programación paralela
    - Usando múltiples procesos
    - Cython paralelo con OpenMP
    - Paralelismo automático

> Módulo 7: Solicitudes web simultáneas

    - Los fundamentos de las solicitudes web
    - El módulo de solicitudes
    - Solicitudes web simultáneas
    - El problema de los tiempos de espera
    - Buenas prácticas en la realización de solicitudes web

> Módulo 8: Deadlocks

    - El concepto de deadlocks
    - Enfoques de situaciones de deadlocks
    - El concepto de livelocks

> Módulo 9: Starvation

    - Entendiendo starvation
    - Aproximación al problema de los readers-writers
    - Soluciones a starvation

> Módulo 10: Patrones de diseño en Python

    - El patrón Factory
    - El patrón Constructor
    - Otros patrones creacionales
    - El patrón Adapter
    - El patrón Decorator
    - El patrón Bridge
    - El patrón Facade
