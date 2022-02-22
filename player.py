class Player():
    def input_name(self):
        self.name = input("Spieler 1 gib Deinen Namen ein: ")
        print("Schön, dass Du dabei bist", self.name + "!")

    def __str__(self):
        pass


player_1 = Player()
player_1.input_name()
