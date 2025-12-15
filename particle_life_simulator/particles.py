import random
import numpy as np
from simulation import *

class Particles:
    def __init__(self, n_particles: int, n_type: int):
        self.n_particles = n_particles
        self.n_type = np.random.randint(0, n_type, n_particles)
        self.position = np.random.rand(n_particles, 2) * [600, 600] 
        self.speed = np.zeros((n_particles, 2))
    
    def get_positions(self):
        return print(self.position)

    def get_speed(self):
        return print(f"Current speed: {self.speed}")
    
    def move(self):
        self.position = np.random.normal(self.position, 5)
        return self.position