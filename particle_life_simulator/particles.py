import numpy as np
import physics
from interactionmatrix import inter_matrix

class Particles:
    def __init__(self, n_particles: int, n_type: int, width, height):
        self.n_particles = n_particles
        self.n_type = np.random.randint(0, n_type, n_particles)
        self.width = width
        self.height = height
        self.position = np.random.rand(n_particles, 2) * [width, height] 
        self.speed = np.zeros((n_particles, 2))
        self.inter_matrix = inter_matrix()
    '''  
    def update_position(self):
        self.position = np.random.normal(self.position, 5)
        self.position[:, 0] = self.position[:, 0] % self.height
        self.position[:, 1] = self.position[:, 1] % self.width
        return self.position
    '''

    def update_position(self, dt= 0.1):
        forces = physics.calculate_all_forces(self.position, self.n_type, self.n_particles, self.inter_matrix)
        
        # Geschwindigkeit und Position aktualisieren
        self.speed += forces * dt
        self.speed *= 0.95  # Dämpfung
        self.position += self.speed * dt

        self.position[:, 0] = self.position[:, 0] % self.width
        self.position[:, 1] = self.position[:, 1] % self.height