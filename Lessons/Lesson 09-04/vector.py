class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"

v1, v2 = Vector(3,4), Vector(6,7)
print(v1+v2)

print(5+7)