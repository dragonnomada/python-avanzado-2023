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

import multiprocessing

class PiProcess (multiprocessing.Process):

    # Esperamos una variable compartida, definida antes del proceso
    def __init__(self, k, hints_shared):
        super().__init__()
        self.k = k
        # Publicar la variable compartida hacia la clase (disponible en el `self`)
        self.hints_shared = hints_shared

    def run(self):
        # Actualizamos el valor de la variable compartida, aún después del proceso
        self.hints_shared.value = task_hints_partial(self.k)
        # self.hints_shared.value += task_hints_partial(self.k)

if __name__ == "__main__":
    #
    # Las variables compartidas, son variables especiales creadas por multiprocessing
    # para retener valores antes y después de que los procesos inician y finalizan
    # Lo más común es usarlas para retener los resultados de cada procesamiento
    #

    #
    # Los values esperan un CType
    # i -> %i (int)
    # f -> %f (float)
    # c -> %c (char)
    # s -> %s (str) 
    #

    hints_shared1 = multiprocessing.Value("i", 0) # Value(type, default, lock=True)
    hints_shared2 = multiprocessing.Value("i", 0)
    hints_shared3 = multiprocessing.Value("i", 0)
    hints_shared4 = multiprocessing.Value("i", 0)

    p1 = PiProcess(2_500_000, hints_shared1)
    p2 = PiProcess(2_500_000, hints_shared2)
    p3 = PiProcess(2_500_000, hints_shared3)
    p4 = PiProcess(2_500_000, hints_shared4)

    p1.start(), p2.start(), p3.start(), p4.start()

    p1.join(), p2.join(), p3.join(), p4.join()

    print("Hints 1:" , hints_shared1.value)
    print("Hints 2:" , hints_shared2.value)
    print("Hints 3:" , hints_shared3.value)
    print("Hints 4:" , hints_shared4.value)

    s =  hints_shared1.value +  hints_shared2.value +  hints_shared3.value +  hints_shared4.value

    print(s)
    print(s / 10_000_000)
    print(4 * s / 10_000_000)



