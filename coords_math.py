import parameters
import objects

def translate_coords(object_coords): #translates the coords from earth being the origin to the rocket being the origin to render the rocket at the center of the screen at all times
    vector = []
    for i in range(parameters.dimensions):
        vector.append(parameters.screen_dimensions[i]/2 + (object_coords[i]-objects.center_object.position[i])/(parameters.distance_factor))
    return vector

def distance(object1_coords, object2_coords):
    vector = pointing_vector(object1_coords, object2_coords)
    sum = 0
    for i in range(parameters.dimensions):
        sum += vector[i]**2
    return sum**0.5

def pointing_vector(initial_vector, final_vector):
    vector = []
    for i in range(parameters.dimensions):
        vector.append(final_vector[i] - initial_vector[i])
    return vector

def get_relative_velocity(new_origin_object, velocity):
    velocity = []
    for i in range(parameters.dimensions):
        velocity.append(new_origin_object.velocity[i] + velocity[i])
    return velocity