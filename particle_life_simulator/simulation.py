import particles
import pygame

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
        user_input = input("Enter number of particle types: ")
        try:
            num_types = int(user_input)
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue
        break
    
    # Config
    NUM_TYPE = num_types
    NUM_PARTICLES = num_particles
    HEIGHT = 600
    WIDTH = 600

    particle_object = particles.Particles(NUM_PARTICLES, NUM_TYPE, HEIGHT, WIDTH)

    # Initialize Pygame
    pygame.init()

    # Set up the game window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Particle Life Simulator")

    # Game loop
    running = True
    clock = pygame.time.Clock()
    
    while running:
        clock.tick(120)  # 60 FPS
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear screen
        screen.fill((0, 0, 0))
        
        # Update particles
        particle_object.update_position(dt = 5)
        
        # Draw particles
        for i in range(NUM_PARTICLES):
            color = pygame.Color(0)
            if particle_object.n_type[i] == 0:
                color = pygame.Color(255, 0, 0)  # Red
            elif particle_object.n_type[i] == 1:
                color = pygame.Color(0, 255, 0)  # Green
            elif particle_object.n_type[i] == 2:
                color = pygame.Color(0, 0, 255)  # Blue
            elif particle_object.n_type[i] == 3:
                color = pygame.Color(255, 255, 0)  # Yellow
            pygame.draw.circle(screen, color, particle_object.position[i].astype(int), 3)
        
        # Update display
        pygame.display.flip()
        
    # Quit Pygame
    pygame.quit()


if __name__ == "__main__":
    main()