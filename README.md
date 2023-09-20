# Curso de Python Avanzado

> **THINCRS**
>
> TAE - FORMACIÓN DE TALENTO ALTAMENTE ESPECIALIZADO 2023

Profesor: [Alan Badillo Salas](alan@nomadacode.com)

## Instrucciones Cierre de Curso

> .1 Realizar el examen final disponible en [https://forms.office.com/r/Rs4NZrqe9D](https://forms.office.com/r/Rs4NZrqe9D)

O en la URL completa:

[https://forms.office.com/Pages/ResponsePage.aspx?id=DQSIkWdsW0yxEjajBLZtrQAAAAAAAAAAAAYAACM43dNUQ0xHV001VzdDOFU2NTc2R1dXU0NDMzQ1Si4u](https://forms.office.com/Pages/ResponsePage.aspx?id=DQSIkWdsW0yxEjajBLZtrQAAAAAAAAAAAAYAACM43dNUQ0xHV001VzdDOFU2NTc2R1dXU0NDMzQ1Si4u)

**IMPORTANTE:** Tienes hasta día Míercoles, 20 de Septiembre de 2023. El día Jueves, 21 de Septiembre durante el transcurso de la mañana será inhabilitada la URL y ya no podrás entregarlo quedando sin calificación, tendrás que justificar algún caso especial por correo, pero no es recomendable y correrás el riesgo de quedar sin calificación.

> .2 Entregar los ejercicios realizados durante el curso por correo a [dragonnomada123@gmail.com](mailto:dragonnomada123@gmail.com)

Deberás entregar **al menos 5 ejercicios** para obtener una calificación. A partir del 6to ejercicio serás considerado para la tabla de ponderación y destacamiento sobre los alumnos de alto desempeño. Estará mejor posicionado aquél que haya entregado más ejercicios y estén mejor documentados.

Considera que los ejercicios que no contengan comentarios o parezcan generados por CHATGPT o similar, podrían ser descartados. De buscar soluciones, deberás comprenderlas y comentar que hace dicho código, para demostrar dominio del ejercicio.

**ÉXITO EN SU EXAMEN y muchas gracias por su participación 🥳**

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
