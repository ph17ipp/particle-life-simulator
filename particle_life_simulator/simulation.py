from particles import *

def main():

    number = int(input("How many particles?: "))
    particles = Particles(n_particles = number, n_type = 2)
    particles.get_positions()

    while True:
        question = input("What do you want? move, show_speed or exit? ")

        if question == "move":
            question = int(input("How many steps? "))
            for step in range(question):
                print(f"Step: {step + 1}")
                particles.move()
                print("----------------------------")

        if question == "show_speed":
            particles.get_speed()

        if question == "exit":
            print("Thanks for using our particle simulator.")
            exit()

if __name__ == "__main__":
    main()