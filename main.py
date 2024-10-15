import objects
import coords_math
import parameters
import pygame
import os
import events
import messages
import paint
import physics

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((parameters.screen_dimensions[0], parameters.screen_dimensions[1]))
pygame.display.set_caption("Rocket Simulator")
clock = pygame.time.Clock()
background = pygame.image.load("image.jpg")
display_surface = pygame.display.set_mode((1280, 720))

time = 0
rocket = objects.rocket

text_title = pygame.font.SysFont("", messages.info_size, False, True).render("", True, "white")

def draw_shining_circle(surface, position, max_radius):
    for i in range(max_radius*2, 0, -2):  # Draw decreasing radius for glow effect
        inner_radius = max_radius/2
        if i < inner_radius:
            color = pygame.Color(255, 255, 255, a=0)
        elif i < max_radius:
            b = int(255 * (i-max_radius)/(inner_radius-max_radius))
            color = pygame.Color(b, 255, b, a=0)  # Adjust transparency based on radius
        else:
            b = int(255 * (i-max_radius*2)/(-max_radius*2))
            color = pygame.Color(0, b, 0, a=0)  # Adjust transparency based on radius
        pygame.draw.circle(surface, color, position, i)


def tick(time):
    screen.blit(background, (0, 0))  # Position the image at the top-left corner (0, 0)

    for object in objects.object_list:
        object.tick()
        translated_position = coords_math.translate_coords(object.position)
        
        if parameters.trajectories:
            for previous_position in object.previous_positions:
                pygame.draw.circle(
                        screen,
                        object.color,
                        coords_math.translate_coords(previous_position),
                        1
        )

        pygame.draw.circle(
                        screen,
                        object.color,
                        translated_position,
                        object.radius/parameters.zoom
        )
        
        object_name = pygame.font.SysFont("", 15, False, True).render(object.name, True, "white")
        display_surface.blit(object_name, object_name.get_rect(topleft=(translated_position[0], translated_position[1])))

    #messages.update()
    text_title = pygame.font.SysFont("", messages.info_size, False, True).render(messages.get_info_message(), True, "white")
    display_surface.blit(text_title, text_title.get_rect())

prev_energy = physics.get_energy(rocket)
while(parameters.running):
    events.runEventListener()
    
    if not parameters.debug:
        os.system('clear')

    tick(time)
    pygame.display.flip()

    clock.tick(parameters.ticks_per_second)
    time +=1

    energy = physics.get_energy(rocket)
    print("potential", physics.get_potential_energy(rocket))
    print("kinetic", physics.get_kinetic_energy(rocket))
    print("e diff", prev_energy - energy, "\n")
    prev_energy = energy


pygame.quit()