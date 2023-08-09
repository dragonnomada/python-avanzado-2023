#
# Diseñar un simulador de partículas para moverlas en el tiempo
# Partícula puede definirse con una posición (x, y) y una velecidad angular
#

# Las clases pueden definir un método especial llamado 
# el constructor: `def __init__(self, ...)`
# cuyo objeto sea recibir parámetros de contrucción e inicializar el estado
# inicial (es decir, el contexto-self) desde que se crea la instancia

# En otros lenguajes existe la posibilidad de crear dos métodos del mismo
# nombre con diferentes parámetros a esto se le llama sobrecarga

class Particle:

    # x = ?
    # y = ?
    # ang_vel = ?

    # CONSTRUCTOR
    def __init__(self, x0, y0, a0):
        # Podemos inicializar el contexto `self` 
        # con los parámetros de construcción (x0, y0, a0)

        self.x = x0
        self.y = y0
        self.ang_vel = a0

    # REEMPLAZA LA REPRESENTACIÓN EN TEXTO DE NUESTRA CLASE
    def __str__(self):
        return "({:.2f}, {:.2f}) <{:.4f}>".format(self.x, self.y, self.ang_vel)
    
    def norm(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

# Podemos hacer comprobaciones con condicionales, 
# pero tendríamos que generar una excepción manualmente
#
# if not <condición>:
#    raise ...

# Las acersiones comprueban una condición y de no cumplirse
# generan una excepción automáticamente

class ParticleSimulator:

    # particles = []

    def __init__(self, particles):
        # if type(particles) != list:
        #     raise Exception("No es una lista")

        assert type(particles) == list

        for particle in particles:
            assert type(particle) == Particle

        self.particles = particles

    def evolve(self, dt):
        timestep = 0.00001 # El tiempo de simulación fina
        nsteps = int(dt / timestep) # número de pasos para la simulación fina

        for _ in range(nsteps):
            for particle in self.particles:
                v_x = -particle.y / particle.norm()
                v_y = particle.x / particle.norm()

                d_x = timestep * particle.ang_vel * v_x
                d_y = timestep * particle.ang_vel * v_y

                particle.x += d_x
                particle.y += d_y

    def __str__(self):
        text = "--- PARTICLE SIMULATOR ---\n"
        for particle in self.particles:
            text += str(particle) + "\n"
        text += "--------------------------"
        return text


if __name__ == '__main__':
    p1 = Particle(1, 1, 0.3)

    print(p1)

    sim1 = ParticleSimulator([
        Particle(1, 1, 3), 
        Particle(2, 2, 1), 
        Particle(1, 2, -1)
    ])

    print(sim1)

    sim1.evolve(0.1)

    print(sim1)