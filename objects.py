import parameters
import physics
import physics_constants
import coords_math

object_list = []

class Physical_Object:
    def __init__(self, name, mass, radius, position, color):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.color = color
        self.position = position
        self.velocity = [0, 0]
        self.acceleration = [0, 0]
        self.previous_positions = []
        object_list.append(self)

    def tick(self):
        self.previous_positions.append(self.position.copy())  # Copy to avoid reference issues (chatgpt

        for i in range(parameters.dimensions):
            for j in range(parameters.time_multiplier):
                self.position[i] = self.position[i] + self.velocity[i]/parameters.ticks_per_second
                self.velocity[i] = self.velocity[i] + self.acceleration[i]/parameters.ticks_per_second
                self.acceleration = physics.get_acceleration(self)
        if not parameters.debug:
            print("\nName:", self.name, "\nvel:", self.velocity, "\nacc:", self.acceleration)
            print("\nMass center:", physics.get_mass_center())
            
class Planet(Physical_Object):
    def __init__(self, name, mass, radius, position, color):
        super().__init__(name, mass, radius, position, color)

class Rocket(Physical_Object):
    def __init__(self, name, mass, radius, position, color):
        super().__init__(name, mass, radius, position, color)

#sun = Planet("sun", 1.989*10**30, 6.9634*10**9, [0, 0], "red")
#earth = Planet("earth", physics_constants.EARTH_MASS, physics_constants.EARTH_RADIUS, [0, 0], "blue")
#moon = Planet("moon", physics_constants.MOON_MASS, physics_constants.MOON_RADIUS, [physics_constants.DISTANCE_EARTH_MOON, 0], "white")
#moon.velocity = [0, (physics_constants.G*earth.mass/moon.position[0])**0.5]
#rocket = Rocket("rocket", 1000, 10**2, [earth.radius + 100, 0], "red")

test1 = Planet("test1", 10**25, 10**4, [-3*10**5, 0], "blue")
test2 = Planet("test2", 10**25, 10**4, [3*10**5, 0], "red")
test1.velocity = [0, 5000]
test2.velocity = [0, -5000]


center_object = None