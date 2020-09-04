class Animal:

    name = "default name"

    def eat(self, food):
        print(f"Eating {food}")

class Food:

    def __init__(self, food_type):
        self.food_type = food_type

    def get_food_type(self):
        return self.food_type

    def __str__(self):
        return f"a food of type {self.food_type}"

class Carnivore(Animal):

    def eat(self, food):
        if food.get_food_type() == "meat":
            Animal.eat(self, food)
        else:
            print("I will not eat this")

class Herbivore(Animal):

    def eat(self, food):
        if food.get_food_type() == "herbal":
            Animal.eat(self, food)
        else:
            print("I will not eat this")

class Omnivore(Carnivore, Herbivore):

    def eat(self, food):
        print("I will eat anything")
        Animal.eat(self, food)

meat = Food("meat")
herbal = Food("herbal")

carni = Carnivore()
carni.eat(meat)
carni.eat(herbal)

print("")

herbi = Herbivore()
herbi.eat(meat)
herbi.eat(herbal)

print("")

omni = Omnivore()
omni.eat(meat)
omni.eat(herbal)
