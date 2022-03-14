from operator import rshift
from tkinter.messagebox import NO
from dice import Dice
from keep_or_not import *

print("+++++++++++++ human_play.py +++++++++++++")


class Play():
    def __init__(self, player=None):
        self.player = player
        self.dice = Dice(6)
        self.result = []
        self.answers = [False, False, False]

    def first_round(self):
        for roll in range(3):
            x = self.dice.roll_dice()
            self.result.append(x)
        return self.result

        return self.result

    def further_rounds(self, result):
        kon = (keep_dice_or_not(result))
        for i in range(len(kon)):
            if kon[i] == False:
                result[i] = human.dice.roll_dice()
                print("Neu:", result[i])
        self.round_number = 3
        return result

    def ergebnis():
        pass


human = Play('heiner')
result = human.first_round()
if keep_round_or_not(result) == True:
    rounds = 1
    human_result = result
else:
    rounds = 2
    result = human.further_rounds(result)
    human_result = None
if human_result == None:
    if keep_round_or_not(result) == True:
        human_result = result
    else:
        rounds = 3
        human_result = human.further_rounds(result)

print(f'Dein Ergebnis: {human_result} im {rounds}. Versuch')
