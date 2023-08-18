# 
# Problema: Sumar los elementos de dos listas/arreglos 
#           en una nueva lista
#

# Código de ajuste (declarar `x1` y `x2`)
setups = [
"""
# numpy
import numpy as np

x1 = np.random.uniform(-1, 1, {n})
x2 = np.random.uniform(-1, 1, {n})
""",
"""
# listas generadas
import random

x1 = [ random.uniform(-1, 1) for _ in range({n}) ]
x2 = [ random.uniform(-1, 1) for _ in range({n}) ]
""",
"""
# natural
import random

x1 = []
x2 = []

for _ in range({n}):
    x1.append(random.uniform(-1, 1))
    x2.append(random.uniform(-1, 1))
"""
]

# Código de desempeño (`x3 = x1 + x2`)
codes = [
"""
# numpy
x3 = x1 + x2 # Suma elemento-a-elemento
""",
"""
# listas generadas (+zip)
x3 = [ x1i + x2i for x1i, x2i in zip(x1, x2) ]
""",
"""
# natural
x3 = []
for i in range(len(x1)):
    x3.append(x1[i] + x2[i])
"""
]

import timeit
import numpy as np

mat = []

for n in [1_000, 5_000, 10_000, 15_000]:
    row = []
    for index, (setup, code) in enumerate(zip(setups, codes)):
        time = np.mean(timeit.repeat(
            stmt=code.format(n=n), 
            setup=setup.format(n=n), 
            number=1, repeat=100)) / 1e-6
        print(index, time)
        row.append((n, time))
    mat.append(row)

print(mat)

X = np.array(mat)

print(X)

# X ~ dim(3) [4 x 3 x 2]

markers = ['ro--', 'bo-', 'k^--']
labels = ['numpy', 'listas generadas', 'natural']

for index in range(len(codes)):
    # times ~ dim(2) [4 x 2]
    times = X[:,index,:]

    x = times[:, 0] # Recuperamos de la matriz la columna 0 (n)
    y = times[:, 1] # Recuperamos de la matriz la columna 1 (time)

    print("*" * 60)

    print(x)
    print(y)

    from matplotlib import pyplot as plt

    plt.plot(x, y, markers[index], label=labels[index])

plt.legend()
plt.show()
