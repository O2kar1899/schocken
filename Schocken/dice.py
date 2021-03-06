from random import randint


class Dice():
    """Arg: Number of sides of the Dice """

    def __init__(self, sides):
        self.sides = sides

    def roll_dice(self):
        roll_dice_result = randint(1, self.sides)

        return roll_dice_result
