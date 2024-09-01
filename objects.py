import parameters
import physics

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
        object_list.append(self)

    def tick(self):
        for i in range(parameters.dimensions):
            self.position[i] = self.position[i] + self.velocity[i]*parameters.time_multiplier/parameters.ticks_per_second
            self.velocity[i] = self.velocity[i] + self.acceleration[i]*parameters.time_multiplier/parameters.ticks_per_second
            self.acceleration = physics.get_acceleration(self)
        
        print("\nName:", self.name, "\nvel:", self.velocity, "\nacc:", self.acceleration)
            

class Planet(Physical_Object):
    def __init__(self, name, mass, radius, position, color):
        super().__init__(name, mass, radius, position, color)

class Rocket(Physical_Object):
    def __init__(self, name, mass, radius, position, color):
        super().__init__(name, mass, radius, position, color)

sun = Planet("sun", 1.989*10**30, 6.9634*10**9, [0, 0], "red")
earth = Planet("earth", 5.98*10**24, 6.37*10**9, [1.47098074000*10**11, 0], "blue")
moon = Planet("moon", 7.35*10**22, 1.74*10**6, [earth.position[0] + 3630104000, 0], "white")
moon.velocity = [0, 1023.056]
#rocket = Rocket("rocket", 1000, 10**2, [earth.radius + 100, 0], "red")

center_object = sun