
from multiprocessing import Value
from dice import Dice
from schocken import Player, evaluation, keep_or_discard
import time

print("************  main.py ********************")

pott = 13


# +++++++++++++++++   Mensch   +++++++++++++++++++++++++++++++
human = Player("Heiner")
value = []
w = Dice(6)

for i in range(3):
    x = w.roll_dice()
    value.append(x)

erster_wurf = evaluation(value)
keep_or_discard(value, erster_wurf)

zweiter_wurf = evaluation(value)
keep_or_discard(value, zweiter_wurf)

dritter_wurf = evaluation(value)

print("Erster Wurf:", erster_wurf)
print("Zweiter Wurf:", zweiter_wurf)
print("Dritter Wurf:", dritter_wurf)
