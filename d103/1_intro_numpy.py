#
# Numpy es una librería para el manejo de arreglos n-dimensionales
#

# Arreglo -> Un conjunto ordenado de datos más eficiente que las lista
#            - Todos elementos comparten el mismo tipo de dato
#            - Se utilizan tipos compatibles con C
#            - Partes del uso pueden ser optimizados para el GPU

# Importaciones:
# - Importación canónica: import modulo | modulo.foo()
# - Importación por seudónido: import modulo as md | md.foo()
# - Importación por partes: from modulo import foo | foo()

# python3 -m pip install numpy

import numpy as np # np -> numpy

x = np.arange(1, 11) # 1-D dim(10,)

print(x)

# X = np.arange(1, 17) # 1-D dim(16,)
# La dimensión es una n-tupla con la profundidad de cada dimensión
# La multiplicación de las profundidades de las dimensiones 
# deben ser igual a la longitud lineal del arreglo
# X = np.arange(1, 17).reshape((4, 4)) # 2-D dim(4, 4)
# Las profundidades van de la dimensión más externa a la más interna
X = np.arange(1, 17).reshape((2, 8)) # 2-D dim(2, 8)

print(X)

# Diseñar una matriz de 3 dimensiones (alto, ancho, canal)
# Ejemplo: Matrix 5x6x3
# Nota: Podemos transformar una lista a un arreglo n-dimensional
im = np.array([
    [ [255, 0, 0], [4, 5, 6], [7, 8, 9], [1, 2, 3], [3, 2, 1], [0, 0, 0], ],
    [ [1, 0, 0], [0, 1, 2], [1, 1, 2], [3, 2, 3], [4, 4, 5], [2, 3, 4], ],
    [ [2, 0, 0], [0, 1, 2], [1, 1, 2], [3, 2, 3], [4, 4, 5], [2, 3, 4], ],
    [ [3, 0, 0], [0, 1, 2], [1, 1, 2], [3, 2, 3], [4, 4, 5], [2, 3, 4], ],
    [ [4, 0, 0], [0, 1, 2], [1, 1, 2], [3, 2, 3], [4, 4, 5], [2, 3, 4], ],
])

print(im)

A = np.ones((4, 5))

print(A)

B = np.zeros((5, 2))

print(B)

# Resolver un sistema de ecuaciones

# 2p + 3c = 19
# 1p + 2c = 11

# | 2 3 | |p|   |19|
# | 1 2 | |c| = |11|

A = np.array([ [2, 3], [1, 2] ]) # 2-D (2, 2)
b = np.array([ 19, 11 ]) # 1-D (2,)

print("A", A.ndim, A.shape)
print("b", b.ndim, b.shape)

sol = np.linalg.solve(A, b)

print(sol)

print(np.linalg.det(A))
print(np.linalg.inv(A))
print(np.linalg.inv(A) / np.linalg.det(A))
print(np.dot(np.linalg.inv(A) / np.linalg.det(A), b)) # solve

# Ejemplo de valores sobre la distribución normal (mu, ds)

s1 = np.random.normal(4, 2, 100) # 66% (4 - 2, 4 + 2) [2, 6] | 95% (4 - 2 * 2, 4 + 2 * 2) [0, 8]

print(s1)
# Los arreglos de numpy tienen métodos auxiliares útiles
print(s1.size) # TOTAL: 100
print(s1.min()) # MÍNIMO: ~0
print(s1.max()) # MÁXIMO: ~8
print(s1.mean()) # PROMEDIO: ~4
print(s1.std()) # D. ESTÁNDAR: ~2
print(np.quantile(s1, 0.17), np.quantile(s1, 0.83)) # I.C. 66%: ~[2, 6]
print(np.quantile(s1, 0.025), np.quantile(s1, 0.975)) # I.C. 95%: ~[0, 8]

from matplotlib import pyplot as plt

plt.hist(s1)

plt.show()

s2 = np.random.uniform(-2, 2, 1000)

print(s2)

plt.hist(s2)

plt.show()