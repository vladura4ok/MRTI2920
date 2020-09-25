class Engine:

    def __init__(self, max_speed):
        self.max_speed = max_speed

    def move_vehicle(self):
        print(f"moving at {self.max_speed} speed")

class Vehicle:

    def __init__(self, name):
        self.name = name

    def move(self):
        print("moving")

class VehicleWithEngine(Vehicle):

    def __init__(self, name, engine):
        Vehicle.__init__(self, name)
        self.engine = engine

    def move(self):
        self.engine.move()

class MuscleVehicle(Vehicle):

    def move(self):
        print("moving by muscle power")

class Car(VehicleWithEngine): pass

class Bicycle(MuscleVehicle): pass

