import numpy as np
import physics
from simulation import main

class Particles:
    def __init__(self, n_particles: int, n_type: int, height, width):
        self.n_particles = n_particles
        self.n_type = np.random.randint(0, n_type, n_particles)
        self.height = height
        self.width = width
        self.position = np.random.rand(n_particles, 2) * [height, width] 
        self.speed = np.zeros((n_particles, 2))
    
    def update_position(self):
        self.position = np.random.normal(self.position, 5)
        self.position[:, 0] = self.position[:, 0] % self.height
        self.position[:, 1] = self.position[:, 1] % self.width
        return self.position


    def update_position2(self):
        for p1 in range(self.n_particles):
            for p2 in range(self.n_particles):
                physics.dist(p1, p2)

                #if same colour -> repell 
                if self.n_type[p1] == self.n_type[p2]:
                    


