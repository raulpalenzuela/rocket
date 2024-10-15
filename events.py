import parameters
import pygame
import objects
import coords_math
import event_booleans
import settings
import messages

def runEventListener():
    for event in pygame.event.get():
        #print(pygame.event.event_name(event.type))
        match event.type:
            case pygame.QUIT:
                parameters.running = False

            case pygame.MOUSEWHEEL:
                exp = 0
                
                if event.y > 0:
                    exp = -0.01
                elif event.y < 0:
                    exp = 0.01

                parameters.zoom = parameters.zoom * 10**exp

            #case pygame.MOUSEBUTTONUP:
             #   for object in objects.object_list:
              #      if coords_math.distance(coords_math.translate_coords(object.position), event.pos) <= object.radius/parameters.zoom: #object.position doesnt have translated coords
               #         objects.center_object = object
                #        return

            case pygame.KEYDOWN:
                #print(event.key)
                if event.key == 1073742048: #control key
                    event_booleans.CTRL_status = True

                if event.key == 99 and event_booleans.CTRL_status:
                    pygame.quit()

                if event.key == 105:
                    settings.show_info = not settings.show_info
                    print(f"Switched show info: {settings.show_info}")

                if event.key == 122:
                    settings.manual_zoom = not settings.manual_zoom
                    print(f"Switched manual Zoom: {settings.manual_zoom}")
                
                if event.key == 116:
                    parameters.trajectories = not parameters.trajectories
                    print(f"Switched trajectories: {parameters.trajectories}")
                    messages.update()

            case pygame.KEYUP:  
                if event.key == 1073742048:
                    event_booleans.CTRL_status = False