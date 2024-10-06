import parameters
import pygame

def draw_circle(screen, center_position, object_radius, color):
    radius = object_radius/parameters.zoom
    for x in range(int(center_position[0] - radius), int(center_position[0] + radius)):
        for y in range(int(center_position[1] - radius), int(center_position[1] + radius)):
            screen.set_at((x, y), color)

def draw_circle_2(screen, center_position, object_radius, color):
    radius = object_radius/parameters.zoom
    print(color)
    for r in range(object_radius):
        pygame.draw.circle(
                        screen,
                        color,
                        center_position,
                        r/parameters.zoom
        )