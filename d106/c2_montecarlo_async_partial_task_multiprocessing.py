#
# Método de Montencarlo
# ---------------------------------------------------
# Consiste en un problema basado en una solución
# que construye en el tiempo con valores aleatorios
# Podemos dividir la solución para paralelizarla 
#

from collections.abc import Callable, Iterable, Mapping
from random import uniform
from typing import Any

def task_hints_partial(k):
    return sum([ (uniform(-1, 1) ** 2 + uniform(-1, 1) ** 2) ** 0.5 <= 1 \
                for _ in range(k)])

# print(4 * task_hints_partial(100) / 100)
# print(4 * task_hints_partial(1_000) / 1_000)
# print(4 * task_hints_partial(10_000) / 10_000)
# print(4 * task_hints_partial(100_000) / 100_000)
# print(4 * task_hints_partial(1_000_000) / 1_000_000)

# print("=" * 80)

# suma = 0

# for _ in range(100):
#     suma += task_hints_partial(10_000)

# print(4 * suma / (1_000_000))

import multiprocessing

class PiProcess (multiprocessing.Process):

    # Variable local a la clase/programa (en procesos se pierde)
    hints = 0

    def __init__(self, k):
        super().__init__()
        self.k = k

    def run(self):
        self.hints = task_hints_partial(self.k)


if __name__ == "__main__":
    p1 = PiProcess(2_500_000)
    p2 = PiProcess(2_500_000)
    p3 = PiProcess(2_500_000)
    p4 = PiProcess(2_500_000)

    p1.start(), p2.start(), p3.start(), p4.start()

    p1.join(), p2.join(), p3.join(), p4.join()

    print("Hints 1:" , p1.hints)
    print("Hints 2:" , p2.hints)
    print("Hints 3:" , p3.hints)
    print("Hints 4:" , p4.hints)

    s = p1.hints + p2.hints + p3.hints + p4.hints

    print(s)
    print(s / 10_000_000)
    print(4 * s / 10_000_000)



