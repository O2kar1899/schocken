from dice import *
from schocken import HumanPlayer
import time

print("************  main.py ********************")

heiner = HumanPlayer("Heiner")


for i in range(3):
    wert = heiner.roll()
    print(f"Würfel {i+1}: Augen: {wert[i]} ")
    time.sleep(0.5)

a = heiner.evaluation(wert)
if "Schock Aus" in a:
    print("SCHOCK AUS!")
    print("")
    print("Du hast die Runde gewonnen und bekommst alle Punkte die noch im Pott sind")
else:
    print("Erbebnis des ersten Wurfs:", wert)
    print("+++++++++++++++++++++++++")
    print('Möchtest Du den gesamten Wur behalten? Der Gegner hat dann auch nur einen Versuch')
    further = input(
        'Drücke "J" für ganzen Wurf behalten oder "N", wenn Du noch mal würfeln willst.')
    if further == "J" or further == "j" or further == "Y" or further == "y":
        print("")
        print(f'Dein Ergebnis: {a} im Ersten')
        print("")
    else:
        pass
