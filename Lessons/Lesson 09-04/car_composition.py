class Engine:

    def __init__(self, power, volume):
        self.power = power
        self.volume = volume

class Car:

    def __init__(self, power, volume, make, model):
        self.make = make
        self.model = model
        self.engine = Engine(power, volume)

car = Car(210, 2.8, "audi", "A8")