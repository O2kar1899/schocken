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
        versuch = 1
        print("Versuch 0", versuch)

    erster_wurf = evaluation(human_value)
    weiter = keep_or_discard(human_value, 1, erster_wurf)
    print("Weiter:", weiter)

    versuch = 1

    if weiter == True and versuch == 1:
        versuch = 2
        print("Versuch 2", versuch)
        zweiter_wurf = evaluation(human_value)
        keep_or_discard(human_value, 2, zweiter_wurf)
        return [zweiter_wurf, versuch]

    if weiter == True and versuch == 2:
        print("Versuch 3", versuch)
        dritter_wurf = evaluation(human_value)
        return [dritter_wurf, versuch]

    human_result = evaluation(human_value)
    #print("Ergebnis :", human_result)

    ergebnis = [human_result, versuch]
    return ergebnis
