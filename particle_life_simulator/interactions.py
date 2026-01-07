import numpy as np


class InteractionMatrix:
    

    def __init__(self, matrix: np.ndarray, interaction_radius: float):
        assert matrix.ndim == 2
        assert matrix.shape[0] == matrix.shape[1]

        self.matrix = matrix
        self.num_types = matrix.shape[0]
        self.radius = interaction_radius

    def compute_forces(self, positions: np.ndarray, types: np.ndarray) -> np.ndarray:
      
        N = positions.shape[0]
        forces = np.zeros((N, 2))

        for i in range(N):
            for j in range(N):
                if i == j:
                    continue

                delta = positions[j] - positions[i]
                distance = np.linalg.norm(delta)

                if 0.0 < distance < self.radius:
                    strength = self.matrix[types[i], types[j]]

                    # Normierte Richtung
                    direction = delta / distance

                    # Lineare Distanz-Abschwächung
                    force_magnitude = strength * (1.0 - distance / self.radius)

                    forces[i] += force_magnitude * direction

        return forces
