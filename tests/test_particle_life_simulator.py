import numpy as np

from particle_life_simulator.particles import Particles
from particle_life_simulator.physics import calculate_all_forces


class TestPhysics:
    """Tests for physics.py"""

    def test_two_particles_attraction(self):
        """Two particles should attract each other"""
        position = np.array([[0.0, 0.0], [10.0, 0.0]])
        n_type = np.array([0, 0])
        inter_matrix = np.array([[1.0]])
        
        forces = calculate_all_forces(position, n_type, 2, inter_matrix)
        
        assert forces[0, 0] > 0.0
        assert forces[1, 0] < 0.0
    
    def test_two_particles_repulsion(self):
        """Two particles should repel each other"""
        position = np.array([[0.0, 0.0], [10.0, 0.0]])
        n_type = np.array([0, 0])
        inter_matrix = np.array([[-1.0]])
        
        forces = calculate_all_forces(position, n_type, 2, inter_matrix)
        
        assert forces[0, 0] < 0.0
        assert forces[1, 0] > 0.0

    def test_particles_too_far(self):
        """Test particles beyond max_distance - should have no forces"""
        position = np.array([[0.0, 0.0], [200.0, 0.0]])
        n_type = np.array([0, 0])
        inter_matrix = np.array([[1.0]])
        
        forces = calculate_all_forces(position, n_type, 2, inter_matrix, max_distance=150)
        
        assert forces[0, 0] == 0.0
        assert forces[1, 0] == 0.0


class TestParticles:
    """Tests for particles.py"""
    
    def test_particles_object(self):
        """Particle object"""
        particle = Particles(n_particles=50, n_type=4, width=600, height=600)

        assert particle.n_particles == 50
        assert len(particle.position) == 50
        assert len(particle.n_type) == 50
        assert len(particle.speed) == 50
    
    def test_update_position_wrap_around(self):
        """Particles wrap around at screen edges"""
        particle = Particles(10, 2, 100, 100)
        particle.position[0] = np.array([101, 101])
        particle.update_position(dt=0.1)

        assert 0 <= particle.position[0, 0] < 100
        assert 0 <= particle.position[0, 1] < 100