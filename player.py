import re
# from unicodedata import name


class Player():

    def __init__(self, name="unknown"):
        self.name = name

        if name == "unknwon":
            self.name = input("Bitte gebe Deinen Namen ein: ")

    def player_info(self):
        print("Der Spieler hat den Namen", self.name)
