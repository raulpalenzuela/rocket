import objects
import coords_math
import parameters
import pygame
import os
import events
import messages
import paint

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((parameters.screen_dimensions[0], parameters.screen_dimensions[1]))
pygame.display.set_caption("Rocket Simulator")
clock = pygame.time.Clock()
background = pygame.image.load("image.jpg")
display_surface = pygame.display.set_mode((1280, 720))
time = 0
temp_bool = False


#def update_with_events():
#    text_title = pygame.font.SysFont("", messages.info_size, False, True).render(messages.settings_info, True, "white")

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

text_title = pygame.font.SysFont("", messages.info_size, False, True).render(messages.settings_info, True, "white")
def tick(time):
    screen.blit(background, (0, 0))  # Position the image at the top-left corner (0, 0)
    display_surface.blit(text_title, text_title.get_rect())

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

        if time % (parameters.ticks_per_second) == 0:
            pygame.draw.circle(
                            screen,
                            object.color,
                            translated_position,
                            object.radius/parameters.zoom
            )
        #draw_shining_circle(screen, translated_position, int(object.radius/parameters.zoom))

        object_name = pygame.font.SysFont("", 15, False, True).render(object.name, True, "white")
        display_surface.blit(object_name, object_name.get_rect(topleft=(translated_position[0], translated_position[1])))


prev_distance = 0
# set the center of the rectangular object.
while(parameters.running):
    events.runEventListener()
    
    if not parameters.debug:
        os.system('clear')
    
    #distance = coords_math.distance(objects.earth.position, objects.moon.position)
    #print("dist diff", prev_distance - distance)
    #prev_distance = distance
    #print("distance", distance)

    tick(time)
    pygame.display.flip()

    clock.tick(parameters.ticks_per_second)

    print(time/parameters.ticks_per_second)
    time +=1

pygame.quit()