import particles
import pygame
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox

def main():
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
        if not num_types in range(1, 5):
            print("Between 1-4 particle types are only allowed.")
            continue
        break
    
    # Config
    NUM_TYPE = num_types
    NUM_PARTICLES = num_particles
    WIDTH = 1280
    HEIGHT = 720

    particle_object = particles.Particles(NUM_PARTICLES, NUM_TYPE, WIDTH, HEIGHT)

    # Initialize Pygame
    pygame.init()

    # Set up the game window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Particle Life Simulator")
    
    # Colours
    colors = [
            (255, 0, 0),    # Red - Type 0
            (0, 255, 0),    # Green - Type 1
            (0, 0, 255),    # Blue - Type 2
            (255, 255, 0)   # Yellow - Type 3
    ]

    # colourdistribution for Labels
    type_colors = ["Red", "Green", "Blue", "Yellow"]
    active_colors = type_colors[:NUM_TYPE]

    combinations = []

    for i in range(NUM_TYPE):
        for j in range(i, NUM_TYPE):
            combinations.append((i, j))

    num_sliders = len(combinations)

    # Slider Layout
    left_margin = 40
    right_limit = int(WIDTH * 0.35)
    usable_width = int(right_limit - left_margin)

    top_margin = 40
    bottom_margin = 40
    usable_height = HEIGHT - top_margin - bottom_margin

    # Max height for Slider-Block
    max_block_height = 70 
    block_height = min(max_block_height, usable_height / num_sliders)

    sliders = []
    labels = []
    value_boxes = []

    # Creating Slider and Labels 
    for index, (a, b) in enumerate(combinations):
        y = int(top_margin + index * block_height)

        # Label for Slider
        label = TextBox(
            win = screen,
            x = int(left_margin),
            y = y,
            width = int(usable_width),
            height = 30,
            fontSize = 18,
            borderColour=(255, 0, 0),
            textColour=(255, 0, 0),
            colour=(0, 0, 0)
        )
        label.disable()
        label.setText(f"{active_colors[a]} + {active_colors[b]}")
        labels.append(label)

        # Slider
        slider = Slider(
            win = screen,
            x = int(left_margin),
            y = int(y + 30 + 5),
            width = int(usable_width),
            height = 30,
            min = -1.0,
            max = 1.0,
            step = 0.01
        )
        sliders.append(slider)

        # Value-Box
        value_box = TextBox(
            win = screen,
            x = int(left_margin + usable_width + 10),
            y = int(y + 30 + 5),
            width = 60,
            height = 30,
            fontSize = 18,
            borderColour = (255, 0, 0),
            textColour = (255, 0, 0),
            colour = (0, 0, 0)
        )
        value_box.disable()
        value_box.setText(f"{slider.getValue():.2f}")
        value_boxes.append(value_box)

    # Game loop
    running = True
    clock = pygame.time.Clock()
    
    while running:
        clock.tick(60)  # 60 FPS
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        # Clear screen
        screen.fill((0, 0, 0))
        
       # Update Slider-values
        for slider, value_box in zip(sliders, value_boxes):
            value_box.setText(f"{slider.getValue():.2f}")
                
        # Update particles
        particle_object.update_position(dt = 5)
        
        # Draw particles
        positions = particle_object.position.astype(int)

        for i in range(NUM_PARTICLES):
            color = colors[particle_object.n_type[i]]
            pygame.draw.circle(screen, color, positions[i], 2)
        
        # Update display
        pygame_widgets.update(events)
        pygame.display.update()
        
    # Quit Pygame
    pygame.quit()


if __name__ == "__main__":
    main()