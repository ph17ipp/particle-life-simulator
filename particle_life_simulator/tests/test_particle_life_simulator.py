import sys
import os
import numpy as np
import pytest

# Add particle_life_simulator directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'particle_life_simulator')))

import physics
import particles

class TestPhysics:
    """Tests for physics.py"""
    
    def test_dist(self):
        """Distance calculation"""
        p1 = np.array([0.0, 0.0])
        p2 = np.array([3.0, 4.0])
        distance = physics.dist(p1, p2)
        assert distance == 5.0, f"Expected 5.0, got {distance}"
    
    def test_calculate_force_attraction(self):
        """Force calculation (attraction)"""
        p1 = np.array([0.0, 0.0])
        p2 = np.array([10.0, 0.0])
        force = physics.calculate_force(p1, p2, attraction=1.0, max_distance=100)
        assert force[0] > 0, f"Force should be greater than 0, Current: {force[0]}"
    
    def test_calculate_force_repulsion(self):
        """Force calculation (repulsion)"""
        p1 = np.array([0.0, 0.0])
        p2 = np.array([10.0, 0.0])
        force = physics.calculate_force(p1, p2, attraction=-1.0, max_distance=100)
        assert force[0] < 0, f"Force should be less than 0, Current: {force[0]}"


class TestParticles:
    """Tests for particles.py"""
    
    def test_particles_object(self):
        """Particle object"""
        particle = particles.Particles(n_particles=50, n_type=4, width=600, height=600)
        assert particle.n_particles == 50
        assert len(particle.position) == 50
        assert len(particle.n_type) == 50
        assert len(particle.speed) == 50
    
    def test_update_position_wrap_around(self):
        """Particles wrap around at screen edges"""
        particle = particles.Particles(10, 2, 100, 100)
        particle.position[0] = np.array([101, 101])
        particle.update_position(dt=0.1)
        assert 0 <= particle.position[0, 0] < 100
        assert 0 <= particle.position[0, 1] < 100


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
