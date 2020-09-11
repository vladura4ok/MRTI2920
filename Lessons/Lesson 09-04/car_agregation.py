class Engine:

    def __init__(self, power, volume):
        self.power = power
        self.volume = volume

class Car:

    def __init__(self, engine, make, model):
        self.make = make
        self.model = model
        self.engine = engine

engine = Engine(210, 2.8)
car = Car(engine, "audi", "A8")