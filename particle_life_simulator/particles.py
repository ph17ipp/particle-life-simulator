import random
import numpy as np

class Particles:
    def __init__(self, n_particles: int, n_type: int):
        self.n_particles = n_particles
        self.n_type = n_type
        #self.position = [(random.uniform(0, 1), random.uniform(0, 1)) for i in range(n_particles)]
        self.position = np.random.uniform(0, 1, (n_particles, 2))
        self.speed = 0
    
    def get_positions(self):
        return print(self.position)

    def get_speed(self):
        return print(f"Current speed: {self.speed}")
    
    def move(self):
        self.position += np.random.uniform(0, 0.001)
        return print(self.position)