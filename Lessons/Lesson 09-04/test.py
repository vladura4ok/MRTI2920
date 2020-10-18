class Hero:

    hp = 100
    damage = 10

    __test = "don't touch me"

    def get_test(self):
        return self.__test

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"hero {self.name}"

    def __repr__(self):
        return f"hero object {self.name} {self.damage} {self.hp}"

    def get_name(self):
        return self.name

    def set_damage(self, damage):
        self.damage = damage

    def damaged(self, damage):
        self.damage =- damage

hero = Hero("Jane")
print(hero._Hero__test)

