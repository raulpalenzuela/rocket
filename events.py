import parameters
import pygame
import objects
import coords_math

def runEventListener():
    for event in pygame.event.get():
        #print(pygame.event.event_name(event.type))
        match event.type:
            case pygame.QUIT:
                parameters.running = False
            case pygame.MOUSEBUTTONDOWN:
                for object in objects.object_list:
                    if coords_math.distance(coords_math.translate_coords(object.position), event.pos) <= object.radius/parameters.distance_factor: #object.position doesnt have translated coords
                        objects.center_object = object
                        return