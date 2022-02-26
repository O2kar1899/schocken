from curses import erasechar
from dice import Dice
import time


class Schocken():
    def __init__(self, number_of_points=13):
        self.number_of_point = number_of_points

        # def number_of_players(self):
        #     self.number_of_players = input(
        #         "Bitte die Zahl der Spieler zwischen 1 und 3 eingeben: ")
        #     if self.number_of_players > 0 and self.number_of_players <= 3:
        #         start()

        # def start(self):
        #     start = ""
        #     while start == "":
        #         start = input('"S" für Start oder "A" für Abbruch: ')
        #         if start == "S" or "s":
        #             print("Start", start)
        #             return True
        #         elif start == "A" or "a":
        #             print("Das Spiel wurde abgebrochen!")
        #             return False
        #         else:
        #             start = ""

    def round_one():
        w = Dice(6)
        result = w.roll_dices(3)
        print("1, Würfel: ", result[0])
        time.sleep(1)
        print("2, Würfel: ", result[1])
        time.sleep(2)
        print("3, Würfel: ", result[2])
        time.sleep(3)


me = Schocken
me.round_one()
