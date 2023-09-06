#
# Método de Montencarlo
# ---------------------------------------------------
# Consiste en un problema basado en una solución
# que construye en el tiempo con valores aleatorios
# Podemos dividir la solución para paralelizarla 
#

from random import uniform

n_samples = 10_000_000

# Puntos contados dentro del círculo
hints = 0
# Puntos totales
total = n_samples

for _ in range(n_samples):
    x = uniform(-1, 1) # Valor aleatorio entre (-1, +1)
    y = uniform(-1, 1) # Valor aleatorio entre (-1, +1)

    d = (x ** 2 + y ** 2) ** 0.5

    if d <= 1:
        hints += 1

print("Hints:", hints)
print("Total:", total)
print("Hints/total:", hints / total)
print("Hints/total:", 4 * hints / total)