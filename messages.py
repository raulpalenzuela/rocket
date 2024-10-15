import parameters
import objects
import physics

rocket = objects.rocket

info_size = 25

settings_info = f"Trajectories: {parameters.trajectories}\n"

controls_info = ""

    
def get_rocket_info():
    position = rocket.position
    velocity = rocket.velocity
    acceleration = rocket.acceleration
    energy = physics.get_energy(rocket)

    return_message = f"Position: {position[0]:.2f}, {position[1]:.2f}\n" + f"Velocity: {velocity[0]:.2f}, {velocity[1]:.2f}\n" +f"Acceleration: {acceleration[0]:.2f}, {acceleration[1]:.2f}\n" + f"Energy: {energy}"

    return return_message

def get_info_message():
    return get_rocket_info()