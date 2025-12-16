import numpy as np
import physics
import simulation

class Particles:
    def __init__(self, n_particles: int, n_type: int, height, width):
        self.n_particles = n_particles
        self.n_type = np.random.randint(0, n_type, n_particles)
        self.height = height
        self.width = width
        self.position = np.random.rand(n_particles, 2) * [height, width] 
        self.speed = np.zeros((n_particles, 2))
    '''  
    def update_position(self):
        self.position = np.random.normal(self.position, 5)
        self.position[:, 0] = self.position[:, 0] % self.height
        self.position[:, 1] = self.position[:, 1] % self.width
        return self.position
    '''

    def update_position(self, dt=2):

        forces = np.zeros((self.n_particles, 2))

        for p1 in range(self.n_particles):
            for p2 in range(self.n_particles):
                if p1 == p2:
                    continue

                pos1 = self.position[p1]
                pos2 = self.position[p2]


                #if same colour -> repell 
                if self.n_type[p1] == self.n_type[p2]:
                    attraction = -0.5
                else:
                    attraction = 2
                
                force = physics.calculate_force(pos1, pos2, attraction)
                forces[p1] += force
        
        # Geschwindigkeit und Position aktualisieren
        self.speed += forces * dt
        self.speed *= 0.95  # Dämpfung
        self.position += self.speed * dt
                    

        self.position[:, 0] = self.position[:, 0] % self.height
        self.position[:, 1] = self.position[:, 1] % self.width

        print(f"forces:{forces}")
        print(f"dt:{dt}")