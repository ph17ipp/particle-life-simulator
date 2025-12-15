import numpy as np

class Particles:
    def __init__(self, n_particles: int, n_type: int):
        self.n_particles = n_particles
        self.n_type = np.random.randint(0, n_type, n_particles)
        self.position = np.random.rand(n_particles, 2) * [600, 600] 
        self.speed = np.zeros((n_particles, 2))
    
    def update_position(self):
        self.position = np.random.normal(self.position, 5)
        self.position = self.position % 600
        return self.position