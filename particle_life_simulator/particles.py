"""particles.py: Defines the Particles class, which has the state of particles (position, speed and type) 
and updates particle movement based on interaction forces. Adds random movement when
there are no forces acting on a particle.
"""

import numpy as np

from . import physics


class Particles:
    def __init__(self, n_particles: int, n_type: int, width, height):
        """Initializes the particle system.
        
        Sets the number of particles, assigns random types,
        initializes positions within the window size
        and sets up speed and interaction values.
        """
        self.n_particles = n_particles
        self.n_type = np.random.randint(0, n_type, n_particles)
        self.width = width
        self.height = height
        self.position = np.random.rand(n_particles, 2) * [width, height] 
        self.speed = np.zeros((n_particles, 2))
        self.inter_matrix = np.zeros((n_type, n_type), dtype=float)

    def update_position(self, dt = 0.1, random_motion = 0.1):
        """Update particle positions using interaction forces,
        random motion, friction (damping) and screen wraping.
        """
        forces = physics.calculate_all_forces(self.position, self.n_type, self.n_particles, self.inter_matrix)
        
        # Apply random motion only if there are no interaction forces on the particles
        for i in range(self.n_particles):
            force_magnitude_sq = forces[i, 0] * forces[i, 0] + forces[i, 1] * forces[i, 1]
            
            if force_magnitude_sq == 0: 
                random_force = (np.random.random(2) - 0.5) * random_motion
                forces[i] += random_force
        
        # Update speed and position
        self.speed += forces * dt
        self.speed *= 0.95  # Friction: slows particles down over time
        self.position += self.speed * dt

        # Wrap particles around the window borders
        self.position[:, 0] = self.position[:, 0] % self.width
        self.position[:, 1] = self.position[:, 1] % self.height