import objects
import coords_math
import parameters
import pygame
import os
import events

pygame.init()
screen = pygame.display.set_mode((parameters.screen_dimensions[0], parameters.screen_dimensions[1]))
pygame.display.set_caption("Rocket Simulator")
clock = pygame.time.Clock()

def draw():
    for object in objects.object_list:
        object.tick()
        pygame.draw.circle(
                        screen,
                        object.color,
                        coords_math.translate_coords(object.position),
                        object.radius/parameters.distance_factor
        )

while(parameters.running):

    events.runEventListener()

    os.system('clear')
    screen.fill("black")
    draw()
    
    pygame.display.flip()
    clock.tick(parameters.ticks_per_second)

pygame.quit()