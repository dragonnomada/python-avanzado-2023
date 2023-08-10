#
# Podemos usar `python3 -m cProfile c5_benchmarks_simulador.py`
#
# Podemos volcar la salida a un archivo con:
# `python3 -m cProfile -o report_simulador.prof.out c5_benchmarks_simulador.py`
#
# Para visualizar gráficamente el archivo usaremos snakeviz:
# `python3 -m pip install snakeviz`
# `python3 -m snakeviz report_simulador.prof.out`
#

from c2_simulador import Particle
from c2_simulador import ParticleSimulator

from random import uniform

sim = ParticleSimulator([Particle(uniform(-1, 1), uniform(-1, 1), uniform(0.5, 1.5)) for _ in range(1_000) ])

sim.evolve(0.1)
