"""physics.py: This module is responsible for the physical behavior of particles.
"""

import numpy as np
from numba import jit, prange


@jit(nopython=True, fastmath=True, cache=True, parallel=True)
def calculate_all_forces(position, n_type, n_particles, inter_matrix, max_distance = 150):
    """Calculates and returns interaction forces for all particles.
    
    It calculates interaction forces defined by an interaction matrix,
    with force strength scaled by the distance between particles.
    """
    forces = np.zeros((n_particles, 2))

    # Loop over all unique particle pairs
    for p1 in prange(n_particles):
        for p2 in range(p1 + 1, n_particles):
            dx = position[p2, 0] - position[p1, 0]
            dy = position[p2, 1] - position[p1, 1]
            
            if abs(dx) > max_distance or abs(dy) > max_distance:
                continue
            
            distance_sq = dx * dx + dy * dy
            
            # Skip particles that are too close or too far away (outside of interaction range)
            if distance_sq < 4 or distance_sq > max_distance * max_distance:
                continue
            
            distance = np.sqrt(distance_sq)
            
            # Interaction effect of particle p2 on particle p1
            attraction1 = inter_matrix[n_type[p1], n_type[p2]]
            force_magnitude1 = attraction1 / distance_sq
            
            # Apply force to particle p1
            forces[p1, 0] += dx / distance * force_magnitude1
            forces[p1, 1] += dy / distance * force_magnitude1
            
            # Interaction effect of particle p1 on particle p2
            attraction2 = inter_matrix[n_type[p2], n_type[p1]]
            force_magnitude2 = attraction2 / distance_sq
            
            # Apply force to particle p2 in the opposite direction
            forces[p2, 0] -= dx / distance * force_magnitude2
            forces[p2, 1] -= dy / distance * force_magnitude2
    
    return forces