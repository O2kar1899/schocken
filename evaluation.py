from doctest import FAIL_FAST
import dice
import time


dice = dice.Dice(6)


def start():  # Die Funktion gibt "S" für Start oder "A" für Abbruch aus
    start = ""
    while start == "":
        start = input('"S" für Start oder "A" für Abbruch: ')
        if start == "S" or "s":
            print("Start", start)
            return True
        elif start == "A" or "a":
            print("Das Spiel wurde beendet!")
            return False
        else:
            start = ""


def roll_dices(dices):
    wurf = []
    for i in range(dices):
        value = dice.random_side()
        wurf.append(value)
    print(wurf)


roll_dices(5)
