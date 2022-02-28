from random import randint


class Dice():
    def __init__(self, sides):
        self.sides = sides

    # def random_side(self):
    #     value = randint(1, self.sides)
    #     return value

    def random_side_grafic(self):
        pass

    def roll_dice(self):
        roll_dice_result = randint(1, self.sides)

        return roll_dice_result
