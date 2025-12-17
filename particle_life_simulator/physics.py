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
def calculate_all_forces(position, n_type, n_particles):
    forces = np.zeros((n_particles, 2))

    for p1 in range(n_particles):
        for p2 in range(n_particles):
            if p1 == p2:
                continue

            pos1 = position[p1]
            pos2 = position[p2]

            attraction = 0.0

            # Red/Red
            if n_type[p1] == 0 and n_type[p2] == 0:
                attraction = -0.5
           
            # Red/Green
            elif n_type[p1] == 0 and n_type[p2] == 1:
                attraction = 2.0
            
            # Red/Blue
            elif n_type[p1] == 0 and n_type[p2] == 2:
                attraction = -1.5
        
            # Red/Yellow
            elif n_type[p1] == 0 and n_type[p2] == 3:
                attraction = 0.5

            # Green/Red
            if n_type[p1] == 1 and n_type[p2] == 0:
                attraction = 1.0

            # Green/Green
            elif n_type[p1] == 1 and n_type[p2] == 1:
                attraction = 2.5

            # Green/Blue
            elif n_type[p1] == 1 and n_type[p2] == 2:
                attraction = 2.5

            # Green/Yellow
            elif n_type[p1] == 1 and n_type[p2] == 3:
                attraction = -1.0
            
            # Blue/Red
            if n_type[p1] == 2 and n_type[p2] == 0:
                attraction = -0.3

            # Blue/Green
            elif n_type[p1] == 2 and n_type[p2] == 1:
                attraction = -0.3

            # Blue/Blue
            elif n_type[p1] == 2 and n_type[p2] == 2:
                attraction = -0.3

            # Blue/Yellow
            elif n_type[p1] == 2 and n_type[p2] == 3:
                attraction = 1.5
            
            # Yellow/Red
            if n_type[p1] == 3 and n_type[p2] == 0:
                attraction = -1.0
            
            # Yellow/Green
            elif n_type[p1] == 3 and n_type[p2] == 1:
                attraction = -1.0

            # Yellow/Blue
            elif n_type[p1] == 3 and n_type[p2] == 2:
                attraction = -1.0

            # Yellow/Yellow
            elif n_type[p1] == 3 and n_type[p2] == 3:
                attraction = -1.0
       

            force = calculate_force(pos1, pos2, attraction)
            forces[p1] += force
    
    return forces