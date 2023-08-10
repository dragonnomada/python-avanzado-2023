from matplotlib import pyplot as plt
from matplotlib import animation

# Importamos las clases diseñadas desde el archivo/módulo c2_simulador.py
from c2_simulador import Particle, ParticleSimulator 

# https://matplotlib.org

# plt.plot([1, 2, 3], [4, 5, 6], "r^--")
# plt.plot([1, 2, 3], [6, 4, 2], "b+-")
# plt.show()

# Creamos una gráfica (figura)
fig = plt.figure() 

# Generamos 1-gráfica (111)
ax = plt.subplot(111, aspect="equal") 

plt.xlim(-3, 3)
plt.ylim(-3, 3)

# Tuplas:
# 2-tupla (x, y) = (4, 5) | x, y = 4, 5
# 1-tupla (x,) = (1,) | x, = 1

# Dibujamos una línea (creamos el objeto línea)
# line, = ax.plot([1, 2, 3], [4, 5, 6]) # 1-tupla
line, = ax.plot([], [], "ro") # 1-tupla

sim = ParticleSimulator([
    Particle(1, 1, 1),
    Particle(-1, 1, -1),
    Particle(2, 2, 3),
    Particle(1.5, 2.3, -8),
])

# Definimos la función que inicialice la gráfica al inicializar la animación
def init():
    # line.set_data([1, 2, 3], [4, 5, 6])
    line.set_data([], [])
    return line, # 1-tupla

# Definimos la función que actualizará la gráfica en cada frame (iteración)
def animate(i):
    # line.set_data([1, 2, 3], [4 + i / 1_000, 5, 6])
    sim.evolve(0.01) # ¿Cuánto tiempo tarda en evolucionar la simulación?
    x = [ particle.x for particle in sim.particles ]
    y = [ particle.y for particle in sim.particles ]
    line.set_data(x, y)
    return line, # 1-tupla
    
# Creamos una animación cada 10ms
anim = animation.FuncAnimation(fig, animate, init_func=init, blit=True, interval=10)

plt.show()