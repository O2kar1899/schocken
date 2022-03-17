from dice import Dice
from keep_or_not import *
from evaluation import evaluation


class RollDices():
    def __init__(self):
        self.dice = Dice(6)
        self.result = [0, 0, 0]

    def human_first_roll(self):
        for i in range(3):
            self.result[i] = self.dice.roll_dice()
        return self.result

    def human_further_roll(self, result):
        kon = (keep_dice(result))
        for i in range(len(kon)):
            if kon[i] == False:
                result[i] = self.dice.roll_dice()
                self.round_number = 3
        return result

    def computer_first_round(self):
        for i in range(3):
            self.result[i] = self.dice.roll_dice()
        return self.result

    def computer_further_roll(self, roll_result):
        _, _, rank = evaluation(roll_result)

        if rank < 4 or roll_result[0] == 6:
            computer_result = self.result

        return computer_result
