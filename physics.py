import objects
import coords_math
import physics_constants
import parameters

def get_acceleration(main_object):
    gravity_acceleration = [0, 0]
    for object in objects.object_list:
        if object == main_object:
            continue

        vec_object_to_mainObject = coords_math.pointing_vector(object.position, main_object.position)
        distance = coords_math.distance(main_object.position, object.position)

        for dimension in range(parameters.dimensions):
            u_vec = vec_object_to_mainObject[dimension]/distance #unitary vector
            gravity_acceleration[dimension] += -physics_constants.G * object.mass / distance**2 * u_vec
    return gravity_acceleration

def get_mass_center():
    mass_center_position = []
    for dimension in range(parameters.dimensions):
        sum_of_positions = 0
        sum_of_mass = 0
        for object in objects.object_list:
            sum_of_positions += object.position[dimension]
            sum_of_mass += object.mass
        mass_center_position.append(sum_of_positions/sum_of_mass)
    return mass_center_position