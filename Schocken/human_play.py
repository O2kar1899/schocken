from dice import Dice
from keep_or_not import *


class Play():
    def __init__(self, player=None):
        self.dice = Dice(6)
        self.result = [0, 0, 0]

    def first_round(self):
        for i in range(3):
            self.result[i] = self.dice.roll_dice()
        return self.result

    def further_rounds(self, result):
        kon = (keep_dice_or_not(result))
        for i in range(len(kon)):
            if kon[i] == False:
                result[i] = self.dice.roll_dice()
                self.round_number = 3
        return result
