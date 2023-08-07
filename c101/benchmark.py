from particle import Particle
from particle_simulator import ParticleSimulator

from random import uniform 

def benchmark(): 
    particles = [
        Particle(uniform(-1.0, 1.0), uniform(-1.0, 1.0), 
        uniform(-1.0, 1.0)) 
        for i in range(1000)] 
    simulator = ParticleSimulator(particles) 
    simulator.evolve(0.1) 

if __name__ == '__main__': 
    benchmark()