#
# Método de Montencarlo
# ---------------------------------------------------
# Consiste en un problema basado en una solución
# que construye en el tiempo con valores aleatorios
# Podemos dividir la solución para paralelizarla 
#

from random import uniform

# Total
n_samples = 10_000_000

# Los bloques o sub-problemas
m_chunks = 4 

hints_list = []

for j in range(m_chunks):
    hints = 0
    total = int(n_samples / m_chunks)
    for i in range(total):
        x = uniform(-1, 1)
        y = uniform(-1, 1)
        d = (x ** 2 + y ** 2) ** 0.5
        if d <= 1:
            hints += 1
    hints_list.append(hints)

print(hints_list)

hints_global = sum(hints_list)

print(hints_global)

