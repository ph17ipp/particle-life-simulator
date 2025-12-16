import numpy as np
from particle_life_simulator.interactions import InteractionMatrix


def test_zero_force_outside_radius():
   
    positions = np.array([
        [0.0, 0.0],
        [1.0, 1.0],
    ])
    types = np.array([0, 0])

    matrix = np.array([[1.0]])
    interactions = InteractionMatrix(matrix, interaction_radius=0.1)

    forces = interactions.compute_forces(positions, types)

    assert np.allclose(forces, np.zeros((2, 2)))


def test_symmetric_repulsion():
    
    positions = np.array([
        [0.4, 0.5],
        [0.6, 0.5],
    ])
    types = np.array([0, 0])

    matrix = np.array([[1.0]])
    interactions = InteractionMatrix(matrix, interaction_radius=0.5)

    forces = interactions.compute_forces(positions, types)

    assert np.allclose(forces[0], -forces[1])
    assert np.linalg.norm(forces[0]) > 0


def test_type_dependent_interaction():
    """Unterschiedliche Typen müssen unterschiedliche Kräfte erzeugen."""
    positions = np.array([
        [0.45, 0.5],
        [0.55, 0.5],
    ])
    types = np.array([0, 1])

    matrix = np.array([
        [0.0, 1.0],
        [-1.0, 0.0],
    ])

    interactions = InteractionMatrix(matrix, interaction_radius=0.5)
    forces = interactions.compute_forces(positions, types)

    assert not np.allclose(forces[0], forces[1])
    assert forces.shape == (2, 2)