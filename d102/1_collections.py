#
# Colecciones:
#  - Listas ~ [1, 2, 3]
#  - Tuplas ~ (-99.123, 104.56)
#  - Diccionarios ~ { "a": 123, "b": True, "c": 45.67 }
#

# Listas
nombres = ["Ana", "Beto", "Carla", "Daniel", "Estefany"]

# Agregar 1+ al final
nombres.append("Fabian")

# Agregar 1 en el índice
nombres.insert(1, "Bety") # -> Los otros se deplazan a la derecha

print(nombres)

# Quitar el último
nombres.pop()

# Quitar el del índice especificado
nombres.pop(0)

print(nombres)

urls = []

# Solicitar las URLs desde un usuario, archivo, api, etc

urls.append("http://fake.com/1.zip")
urls.append("http://fake.com/18.png")
urls.append("http://fake.com/94.pdf")

# for url in urls:
#     # TODO: Descarga el archivo de las URLs

while len(urls) > 0:
    # url = urls.pop() # LIFO (Last-Input -> First-Output)
    url = urls.pop(0) # FIFO (First-Input -> First-Output)

    print("Descargando: {}...".format(url))

# Tuplas

def min_max(x):
    assert len(x) > 0

    minix = x[0]
    maxix = x[0]

    for xi in x:
        if minix > xi:
            minix = xi
        if maxix < xi:
            maxix = xi

    return (minix, maxix) # (1, 9) | (-34, 78) ~> 2-tupla

# Una n-tupla acopla/empaqueta n-valores 
# que pueden ser desacoplados/desempaquetados en n-variables

a, b = min_max([4, 5, 3, 6, 7, 9, 8, 2, 1])

print(a, b)

c, d = min_max([-17, 34, -34, 78, 17, 25, -22])

print(c, d)

# e, f = min_max([]) # AssertionError

import random

def generar_puntos(n):
    puntos = []

    for i in range(n):
        xi = int(random.gauss(4, 3.2))
        yi = int(random.gauss(6, 4.2))
        
        puntos.append( (xi, yi) )

    return puntos

s = generar_puntos(3)

print(s)

# Camelcase -> POO

for p in generar_puntos(4): # `p` es una 2-tupla
    print(p)
    x, y = p
    print("x={}, y={}".format(x, y))

print("-" * 40)

for x, y in generar_puntos(4):
    print("x={}, y={}".format(x, y))

print("=" * 40)

# Diccionarios

persona = ("Ana", 23, False) # (?, ?, ???)

nombre, edad, casado = persona # :/

# { [key]: <value> }
persona = { 
    "nombre": "Ana",
    "edad": 23,
    "casado": False  
}

print(persona["nombre"])
print(persona["edad"])
print(persona["casado"])

texto = "hola mundo mundial este es un texto de prueba para contar el numero de caracteres en este texto"

caracteres = {} # { 'h': ?, 'o': ?, 'l': ?, 't': ? }

# Existe la clave en el diccionario: Incrementa el conteo
# Sino: Establece el conteo para esa clave en 1

for c in texto:
    # key in diccionario:
    if c in caracteres:
        caracteres[c] += 1
    else:
        caracteres[c] = 1

print(caracteres)

# Extraemos las clave -> como lista
print(list(caracteres.keys()))
print(list(caracteres.values()))

keys = list(caracteres.keys())
values = list(caracteres.values())

# zip -> Formar una lista de tuplas
#        donde cada tupla tiene los valores
#        recorridos de cada lista (elemento-por-elemento)
print(list(zip(keys, values)))

for caracter, conteo in zip(keys, values):
    print("Caracter '{}' -> {}".format(caracter, conteo))

print("-" * 40)

for caracter, conteo in caracteres.items():
    print("Caracter '{}' -> {}".format(caracter, conteo))