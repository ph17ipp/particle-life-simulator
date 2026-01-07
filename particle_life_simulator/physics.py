import numpy as np
from numba import jit

@jit(nopython=True)
def dist(p1, p2):
    distance = np.sqrt(np.sum((p1 - p2)**2))
    # np.linalg.norm()
    return distance

@jit(nopython=True)
def calculate_force(p1, p2, attraction = 0.0, max_distance = 300):
    dt = p2 - p1
    distance = dist(p1, p2)

    if distance < 2:
        distance = 2
    
    if distance > max_distance:
        #if attraction == 0.0:
            #return (np.random.random(2) - 0.5) * 0.005
        #else:
            return np.array([0.0, 0.0])

    force_magnitude = attraction / (distance**2)
    force = (dt / distance) * force_magnitude

    return force

@jit(nopython=True)
def calculate_all_forces(position, n_type, n_particles, inter_matrix):
    forces = np.zeros((n_particles, 2))

    for p1 in range(n_particles):
        for p2 in range(n_particles):
            if p1 == p2:
                continue

            pos1 = position[p1]
            pos2 = position[p2]
                   
            attraction = inter_matrix[n_type[p1],n_type[p2]]

            force = calculate_force(pos1, pos2, attraction)
            forces[p1] += force
    
    return forces