# 
# Existe un plugin para pytest llamdo `pytest-benchmark`
# que podemos instalar mediante `python3 -m pip install pytest-benchmark`
#
# Podemos usar dicha librería para ejecutar pruebas:
# `python3 -m pytest c4_pytest_simulador.py::test1`
#

#
# La función benchmark puede ser inyectada a nuestras pruebas
# para medir el tiempo de ejecución dentro de las pruebas para
# una función objetivo.
#

from c2_simulador import Particle
from c2_simulador import ParticleSimulator

from random import uniform

# from time import time

# def benchmark():
#     sim = ParticleSimulator([Particle(uniform(-1, 1), uniform(-1, 1), uniform(0.5, 1.5)) for _ in range(1_000) ])

#     start = time()

#     sim.evolve(0.1)

#     end = time()

#     elapsed = end - start

#     print("Total: {:.1f}s".format(elapsed))

# if __name__ == "__main__":
#     benchmark()

#
# Vamos a diseñar una función de pruebas (`test_sim`)
# e inyectarle la función benchmark del plugin `pytest-benchmark`
#

def test_sim(benchmark):
    sim = ParticleSimulator([Particle(uniform(-1, 1), uniform(-1, 1), uniform(0.5, 1.5)) for _ in range(1_000) ])

    # benchmark(func, ...parms)
    benchmark(sim.evolve, 0.1)
    # benchmark.pedantic(sim.evolve, setup=init, args=(0.1), kwargs={'foo': 'bar'}, iterations=3, rounds=2)



