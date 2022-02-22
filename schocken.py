import dice


class Schocken():
    def number_of_players(self):
        self.number_of_players = input(
            "Bitte die Zahl der Spieler zwischen 1 und 3 eingeben: ")
        if self.number_of_players > 0 and self.number_of_players <= 3:
            start()

    def start():
        start = ""
        while start == "":
            start = input('"S" für Start oder "A" für Abbruch: ')
            if start == "S" or "s":
                print("Start", start)
                return True
            elif start == "A" or "a":
                print("Das Spiel wurde abgebrochen!")
                return False
            else:
                start = ""

    def round_one(self):
        open_points = 13

        while open_points > 0:


w = dice.Dice(6)


print("1. Würfel: ", wurf[0])
print("2. Würfel: ", wurf[1])
print("3. Würfel: ", wurf[2])
