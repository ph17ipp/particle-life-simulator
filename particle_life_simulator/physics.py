import numpy as np

def dist(p1, p2):
    distance = np.sqrt(np.sum((p1 - p2)**2))
    # np.linalg.norm()
    return distance

def calculate_force(p1, p2, attraction = 1.0, max_distance = 100):

    dt = p1 - p2
    distance = dist(p1, p2)

    if distance < 1:
        distance = 1
    
    if distance > max_distance:
        return np.array([0.0, 0.0])

    force_magnitude = attraction / (distance**2)
    force = (dt / distance) * force_magnitude

    return force