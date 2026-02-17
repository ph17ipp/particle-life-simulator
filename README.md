## 🔬⚛️ Particle Life Simulator

A Python-based simulation of interacting particles inspired by biological systems and emergent behavior.

Multiple particle types follow attraction and repulsion rules. You can tune the interaction matrix live via sliders and observe emergent structures in real time.

## 🔧 Features

- Interactive Pygame visualization
- 1-4 particle types with a symmetric interaction matrix
- Live sliders for attraction/repulsion strength
- Random motion fallback when no forces apply

## 📦 Installation

Clone and install the package, then install runtime dependencies:

```console
git clone https://github.com/ph17ipp/particle-life-simulator.git
cd particle-life-simulator
python -m pip install .
python -m pip install numpy numba pygame pygame-widgets
# or on mac: python3 -m pip install .
#            python3 -m pip install numpy numba pygame pygame-widgets
```

## ▶️ Usage

Start the interactive simulation:

```console
python -m particle_life_simulator.simulation
```

You will be prompted for the number of particles and particle types (1-4). Use the sliders to set attraction/repulsion values for each type pair.

## 👥 Team

| Name | GitHub |
|------|------|
| Philipp Tran | @ph17ipp |
| Marc Le | @Furobashi |
| Alena Cicek | @Hebivi |
| Axin Yildiz | @Todozuka |


## 🛠 Developer Documentation
### 🔧 Code Architecture
```console
particle_life_simulator/
 ├── particles.py   # Particle state and integration step
 ├── physics.py     # Force calculation (Numba-accelerated)
 └── simulation.py  # Pygame UI and slider controls
```

### 🧪 Testing
Tests are located in:
```console
tests/
 └── test_particle_life_simulator.py
```

Run tests with:
```console
pytest
```

### 🧹 Code Quality
This project uses:
- `ruff` for formatting and linting
- `pytest` for testing
- GitHub Actions for CI with linting + unit tests
