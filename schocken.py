from unittest import result
from dice import Dice
import time


class Player:
    def __init__(self, name="unknown"):
        self.name = name


# def roll(wurf=[]):
#     dice = Dice(6)  # Würfel mit 6 Seiten
#     result = dice.roll_dice()
#     wurf.append(result)
#     output = wurf
#     return wurf


def evaluation(result=[0, 0, 0]):
    if result[0] == result[1] and result[0] == result[2] and result[0] != 1:
        general = result[0]
        return f"General {result[0]}"
    elif result[0] == 1 and result[1] == 1 and result[2] == 1:
        return "Schock Aus"
    elif (result[0] == 1 and (result[1] == 1 or result[2] == 1)) or (result[1] == 1 and result[2] == 1):
        for i in range(3):
            if result[i] != 1:
                schock = result[i]
        return f"Schock {schock}"
    else:
        result.sort(reverse=True)
        return f"Zahl: {result} "


def keep_or_discard(value, evaluation=""):
    further = False
    w = Dice(6)

    if "Schock Aus" in evaluation:
        print("SCHOCK AUS!")
        print("")
        print("Du hast die Runde gewonnen und bekommst alle Punkte die noch im Pott sind")

    else:
        print("Erbebnis des Wurfs:", value)
        print("+++++++++++++++++++++++++")
        print('Möchtest Du den gesamten Wurf behalten? Der Gegner bekommt genauso viele Versuche wie Du')
        further = input(
            'Drücke "J" für ganzen Wurf behalten oder "N", wenn Du noch mal würfeln willst. ')
        if further == "J" or further == "j" or further == "Y" or further == "y":
            print("")
            print(f'Dein Ergebnis: {evaluation} im Ersten')
            print("")
            further = False
        else:
            further = True

    if further == True:
        dice_1 = input(
            f"Möchtest Du den ersten Würfel mit {value[0]} Augen behalten? J/N: ")
        print(f"Deine Antwort {dice_1} ")

        dice_2 = input(
            f"Möchtest Du den zweiten Würfel mit {value[1]} Augen behalten? J/N: ")
        dice_3 = input(
            f"Möchtest Du den dritten Würfel mit {value[2]} Augen behalten? J/N: ")
        x = 0

        if dice_1 != "J" and dice_1 != "j" and dice_1 != "Y" and dice_1 != "y":
            value[0] = w.roll_dice()
            print(f"Würfel 1 wurde neu gewürfelt: {value[0]} ")

        else:
            print(f"Der erste Würfel bleibt {value[0]} ")

        if dice_2 != "J" and dice_2 != "j" and dice_2 != "Y" and dice_2 != "y":
            value[1] = w.roll_dice()
            print(f"Würfel 2 wurde neu gewürfelt: {value[1]} ")
        if dice_3 != "J" and dice_3 != "j" and dice_3 != "Y" and dice_3 != "y":
            value[2] = w.roll_dice()
            print(f"Würfel 3 wurde neu gewürfelt: {value[2]} ")
