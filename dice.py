from random import randint


class Dice():
    def __init__(self, sides):
        self.sides = sides

    # def random_side(self):
    #     value = randint(1, self.sides)
    #     return value

    def random_side_grafic():
        pass

    def roll_dices(self, dices):
        self.dices = dices
        print("Würfel", self.dices)
        wurf = []
        for i in range(self.dices):
            value = randint(1, self.sides)
            wurf.append(value)
        return wurf
