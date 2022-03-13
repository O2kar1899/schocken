from dice import Dice
from keep_or_not import *

print("+++++++++++++ human_play.py +++++++++++++")


class Play():
    def __init__(self, player=None):
        self.player = player
        self.dice = Dice(6)
        self.result = []
        self.answers = [False, False, False]

    def play(self):
        for roll in range(3):
            x = self.dice.roll_dice()
            self.result.append(x)

        return self.result

    def gg(self, result):
        erg = keep_round_or_not(result)


human = Play('heiner')


result = human.play()
if keep_round_or_not(result) == True:
    print('Wurf behalten')
else:
    keep_dice_or_not(result)
