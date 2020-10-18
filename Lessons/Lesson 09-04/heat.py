class HeatingElement:

    max_degree = 100

    def __init__(self, max_degree):
        self.max_degree = max_degree

    def get_max_degree(self):
        return self.max_degree

    def heat(self, obj):
        print(f"heating {object} to {self.max_degree} degree")

class HeatingPanel(HeatingElement):

    make = "Indesit"

    def __init__(self, max_degree, make):
        HeatingElement.__init__(self, max_degree)
        self.make = make

    def get_make(self):
        return self.make

    def heat(self, obj):
        HeatingElement.heat(self, object)
        print(f"by heating panel {self.make}")

def Heat(element, obj):
    element.heat(obj)

hp = HeatingPanel(170, "Bosch")
#print(hp.get_make())
#print(hp.get_max_degree())

he = HeatingElement(180)
#he.heat([1,2,3,4,5])

#hp.heat("str test")

x = [he, hp, ""]
for i in x:
    Heat(i, 13)
    print("")