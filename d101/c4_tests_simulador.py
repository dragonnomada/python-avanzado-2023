#
# Pruebas de fiabilidad/aseguramiento
#

from c2_simulador import Particle
from c2_simulador import ParticleSimulator

particles = [
    Particle(1, 1, 1),
    Particle(-1, -1, -1),
]

sim = ParticleSimulator(particles)

print(particles[0])
print(particles[1])

sim.evolve(0.1)

print(particles[0])
print(particles[1])

eps = 1e-2 # 0.01

def near(a, b):
    return abs(a - b) < eps

assert near(particles[0].x, 0.93)
assert near(particles[0].y, 1.07)

assert near(particles[1].x, -1.07)
assert near(particles[1].y, -0.93)

# assert abs(particles[0].x - 0.93) < eps
# assert abs(particles[0].y - 1.07) < eps

# assert abs(particles[1].x - (-1.07)) < eps
# assert abs(particles[1].y - (-0.93)) < eps