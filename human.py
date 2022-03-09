from dice import Dice
from schocken import Player, evaluation, keep_or_discard
import time

Dice = Dice(6)  # klassicher Würfel mit 6 Seiten


def human_play():
    human = Player("Heiner")
    human_value = []

    for i in range(3):
        x = Dice.roll_dice()
        human_value.append(x)

    erster_wurf = evaluation(human_value)
    weiter = keep_or_discard(human_value, 1, erster_wurf)

    if weiter == True:
        zweiter_wurf = evaluation(human_value)
        keep_or_discard(human_value, 2, zweiter_wurf)

    if weiter == True:
        dritter_wurf = evaluation(human_value)

    human_result = evaluation(human_value)
    print("Ergebnis :", human_result)
