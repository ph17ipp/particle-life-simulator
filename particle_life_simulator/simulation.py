"""simulation.py: Main simulation and user interface module.
This module initializes the particle system, sets up the simulation window,
creates the slider-based UI for configuring the interaction matrix 
and runs the main simulation loop.
"""

import pygame
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

from . import particles


def main():

    # Asks the user for the total number of particles and particle types (limited to the available colors).
    while True:
        user_input = input("Enter number of particles: ")
        try:
            num_particles = int(user_input)
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue
        break

    while True:
        user_input = input("Enter number of particle types (1-4): ")
        try:
            num_types = int(user_input)
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue
        if num_types not in range(1, 5):
            print("Between 1-4 particle types are only allowed.")
            continue
        break
    
    # Config: Simulation configuration values
    NUM_TYPE = num_types
    NUM_PARTICLES = num_particles
    SCREEN_WIDTH = 1280
    SCREEN_HEIGHT = 720

    particle_object = particles.Particles(NUM_PARTICLES, NUM_TYPE, SCREEN_WIDTH, SCREEN_HEIGHT)


# ==========================================================================
# Particle Life Simulator with Pygame
# ==========================================================================
    
    # Initialize Pygame and set up game window
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Particle Life Simulator")
    
    # Color definitions for particles
    colors = [
            (255, 0, 0),    # Red - Type 0
            (0, 255, 0),    # Green - Type 1
            (0, 0, 255),    # Blue - Type 2
            (255, 255, 0)   # Yellow - Type 3
    ]


# ==========================================================================
# Slider UI setup (interaction matrix control)
# ==========================================================================
# This section creates and manages all UI elements based on sliders
# to control the interaction matrix between particle types.
# Each slider shows one unique type pair (i, j) and allows real-time
# adjustments of attraction and repulsion strength.

    # Color distribution for Labels
    type_colors = ["Red", "Green", "Blue", "Yellow"]
    active_colors = type_colors[:NUM_TYPE]

    combinations = []

    for i in range(NUM_TYPE):
        for j in range(i, NUM_TYPE):
            combinations.append((i, j))

    num_sliders = len(combinations)


    # --- Slider Layout ---
    # Margins: distance between window edges and UI elements
    left_margin = 40
    top_margin = 40
    bottom_margin = 40

    # Slider uses the left 15% of the window width
    right_limit = int(SCREEN_WIDTH * 0.15)
    usable_width = int(right_limit - left_margin)
    usable_height = SCREEN_HEIGHT - top_margin - bottom_margin

    # Max height for Slider-Block
    max_block_height = 70 
    block_height = min(max_block_height, usable_height / num_sliders)


# --- UI elements ---
    sliders = []        # interactive Slider widgets
    labels = []         # TextBox labels
    value_boxes = []    # Textboxes showing slider values

    # Creating Slider and Labels 
    for index, (a, b) in enumerate(combinations):
        y = int(top_margin + index * block_height)

        # Split label area into three equally sized parts:
        # [type a label] [ "+" label] [type b label]
        w = int(usable_width / 3)

        # --- Labels for Slider (type a, "+", type b) ---
        # Label for type a
        label = TextBox(
            win = screen,
            x = int(left_margin),
            y = y,
            width = w,
            height = 20,
            fontSize = 14,
            borderColour=(0, 0, 0),
            borderThickness= 1,
            textColour=(0, 0, 0),
            colour=colors[a]
        )
        label.disable()
        label.setText(active_colors[a])
        labels.append(label)

        # Label for "+"
        label = TextBox(
            win = screen,
            x = int(left_margin + w),
            y = y,
            width = w,
            height = 20,
            fontSize = 14,
            borderColour=(0, 0, 0),
            borderThickness= 1,
            textColour=(255, 255, 255),
            colour=(0, 0, 0)
        )
        label.disable()
        label.setText("      + ")
        labels.append(label)


        # Label for type b
        label = TextBox(
            win = screen,
            x = int(left_margin + 2*w),
            y = y,
            width = w,
            height = 20,
            fontSize = 14,
            borderColour=(0, 0, 0),
            borderThickness= 1,
            textColour=(0, 0, 0),
            colour=colors[b]
        )
        label.disable()
        label.setText(active_colors[b])
        labels.append(label)


        # --- Slider ---
        # Each slider controls interaction strength between types.
        # Range: [-1.0, 1.0], step: 0.01
        slider = Slider(
            win = screen,
            x = int(left_margin),
            y = int(y + 22 + 6),
            width = int(usable_width),
            height = 18,
            min = -1.0,
            max = 1.0,
            step = 0.01,
            handleColour=(40, 40, 40)
        )
        sliders.append(slider)

        # --- Value-Box ---
        # Display for the current slider value
        value_box = TextBox(
            win = screen,
            x = int(left_margin + usable_width + 15),
            y = int(y + 24 + 6),
            width = 40,
            height = 20,
            fontSize = 14,
            borderColour = (255, 255, 255),
            borderThickness= 1,
            textColour = (255, 255, 255),
            colour = (0, 0, 0)
        )
        value_box.disable()
        value_box.setText(f"{slider.getValue():.2f}")
        value_boxes.append(value_box)


# ==========================================================================
# Main simulation loop
# ==========================================================================
# Handle events, update UI and particles and draw particles

    running = True
    clock = pygame.time.Clock()
    
    while running:
        clock.tick(60)  # 60 FPS
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        
       # UI update: update value boxes to match with the slider
        for slider, value_box in zip(sliders, value_boxes):
            value_box.setText(f"{slider.getValue():.2f}")
            
                
        # Update particles: apply slider values to interaction matrix
        for (i, j), slider in zip(combinations, sliders):
            value = slider.getValue()

            particle_object.inter_matrix[i, j] = value
            particle_object.inter_matrix[j, i] = value
        
        particle_object.update_position(dt = 2)
        
        
        # Draw particles
        positions = particle_object.position.astype(int)
        for i in range(NUM_PARTICLES):
            color = colors[particle_object.n_type[i]]
            pygame.draw.circle(screen, color, positions[i], 2)
        
        pygame_widgets.update(events)
        pygame.display.update()
        
    pygame.quit()


if __name__ == "__main__":
    main()