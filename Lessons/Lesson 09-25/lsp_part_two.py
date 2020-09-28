class Engine:

    def __init__(self, max_speed):
        self.max_speed = max_speed

    def move_vehicle(self):
        print(f"moving at {self.max_speed} speed")

class Vehicle:

    def __init__(self, name, engine):
        self.name = name
        self.engine = engine

    def move(self):
        self.engine.move_vehicle()

class Car(Vehicle):

    def __init__(self, name, engine):
        Vehicle.__init__(self, name, engine)

    def enable_radio(self):
        print("radio is on")

class Bicycle(Vehicle):

    def __init__(self, name):
        Vehicle.__init__(self, name, "") #error anyway on the move() method

    def Jump(self):
        pass

engine = Engine(100)
car = Car("fast_car", engine)
car.move()

