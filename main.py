import objects
import coords_math
import parameters
import pygame
import os
import events

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((parameters.screen_dimensions[0], parameters.screen_dimensions[1]))
pygame.display.set_caption("Rocket Simulator")
clock = pygame.time.Clock()
background = pygame.image.load("image.jpg")

display_surface = pygame.display.set_mode((1280, 720))
text_title = pygame.font.SysFont("", 30, False, True).render('Rocket Simulator', True, "white")

def draw():
    for object in objects.object_list:
        object.tick()
        translated_position = coords_math.translate_coords(object.position)
        pygame.draw.circle(
                        screen,
                        object.color,
                        translated_position,
                        object.radius/parameters.zoom
        )

        if parameters.trajectories:
            for previous_position in object.previous_positions:
                pygame.draw.circle(
                        screen,
                        object.color,
                        coords_math.translate_coords(previous_position),
                        1
        )

        object_name = pygame.font.SysFont("", 15, False, True).render(object.name, True, "white")
        display_surface.blit(object_name, object_name.get_rect(topleft=(translated_position[0], translated_position[1])))


 
# set the center of the rectangular object.
while(parameters.running):

    events.runEventListener()
    
    if not parameters.debug:
        os.system('clear')
    #screen.fill("black")
    screen.blit(background, (0, 0))  # Position the image at the top-left corner (0, 0)
    display_surface.blit(text_title, text_title.get_rect())
    draw()
    
    pygame.display.flip()
    clock.tick(parameters.ticks_per_second)

pygame.quit()