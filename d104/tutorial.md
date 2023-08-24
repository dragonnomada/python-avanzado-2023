## PASO 1 - Crear el módulo `*.pyx`

El módulo de tipo `.pyx` es un módulo especial entre Python y C, el cuál define funciones que estarán disponibles en módulo compilado (`*.so`) y podrá ser usado dentro de archivos de `C/C++` y archivos de `Python`.

```py
# `foo.pyx`
def foo():
    print("Hola foo()")
```

## PASO 2 - Crear el archivo de `setup.py`

El archivo `setup.py` tiene el objetivo de `cythonizar` el módulo `.pyx` en un archivo `.c` (la traducción literal) y el archivo `.so` (la librería dinámica de **C/C++** y **Python**).

```py
# setup_foo.py
from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize("foo.pyx") 
    # foo.c | foo.cpython-<version>-<platform>.so
)
```

## PASO 3 - Instalar/Ejecutar el `setup.py`

**Nota**: Instalar `cython` mediante `python3 -m pip install cython`

> `python3 setup.py build_ext --inplace`

Generará los archivos `foo.c` y `foo.cpython-<version>-<platform>.so`.

## PASO 4 - Crear un archivo prueba que utilice nuestra función

```py
from util import foo

foo() # Ejecutamos la función del *.so con eficiencia de C
```

## Resultados de Eficiencia:

| CÓDIGO    | TIEMPO  | CPU    |
| ------    | ------  | ------ |
| C         | ~0.010s | ~80%   |
| Python    | ~0.131s | ~98%   |
| Cython    | ~0.060s | ~95%   |
