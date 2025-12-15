from particles import Particles
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

    NUM_TYPE = num_types
    NUM_PARTICLES = num_particles

    particles = Particles(NUM_PARTICLES, NUM_TYPE)

    # Initialize Pygame
    pygame.init()

    # Set up the game window
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption("Particle Life Simulator")

    # Game loop
    running = True
    clock = pygame.time.Clock()
    
    while running:
        clock.tick(10)  # 60 FPS
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Clear screen
        screen.fill((0, 0, 0))
        
        # Update particles
        particles.update_position()
        
        # Draw particles
        for i in range(NUM_PARTICLES):
            color = pygame.Color(0)
            if particles.n_type[i] == 0:
                color = pygame.Color(255, 0, 0)  # Red
            elif particles.n_type[i] == 1:
                color = pygame.Color(0, 255, 0)  # Green
            elif particles.n_type[i] == 2:
                color = pygame.Color(0, 0, 255)  # Blue
            elif particles.n_type[i] == 3:
                color = pygame.Color(255, 255, 0)  # Yellow
            pygame.draw.circle(screen, color, particles.position[i].astype(int), 3)
        
        # Update display
        pygame.display.flip()
        
    # Quit Pygame
    pygame.quit()


if __name__ == "__main__":
    main()