from curses import erasechar
from dice import Dice
import time


class HumanPlayer():
    def __init__(self, name, number_of_points=13):
        self.name = name
        self.number_of_point = number_of_points

    def round_one(self):
        roll_2 = 3
        roll_3 = 3

        w = Dice(6)

        result_round_one = ["X", "X", "X"]

        for i in range(3):
            result_1 = w.roll_dices(3)

            if result_round_one[0] == "X":
                print("1, Würfel: ", result_1[0])
                time.sleep(1)

            if result_round_one[1] == "X":
                print("2, Würfel: ", result_1[1])
                time.sleep(1)

            if result_round_one[2] == "X":
                print("3, Würfel: ", result_1[2])

            if i < 2:
                print(f"{self.name} möchtest Du das Ergebnis stehen lassen?")
                print(f"Der Gegner hat dann auch {(i+1)} Versuche.")
                question_0 = input(
                    "Gebe 'y' für stehen lassen oder 'N' für weiter würfeln ein ")

                if question_0 != "Y" and question_0 != "y" and question_0 != "J" and question_0 != "j":

                    if result_round_one[0] == "X":
                        question_1 = input(
                            f"{self.name} möchtest Du Würfel 1 ({result_1[0]} Augen) behalten? Y/N ")
                        if question_1 == "Y" or question_1 == "y" or question_1 == "J" or question_1 == "j":
                            result_round_one[0] = result_1[0]

                    if result_round_one[1] == "X":
                        question_2 = input(
                            f"2 Möchtest Du Würfel 2 ({result_1[1]} Augen) behalten? Y/N ")
                        if question_2 == "Y" or question_2 == "y" or question_2 == "J" or question_2 == "j":
                            result_round_one[1] = result_1[1]

                    question_3 = input(
                        f"3 Möchtest Du Würfel 3 ({result_1[2]} Augen) behalten? Y/N ")
                    if question_3 == "Y" or question_3 == "y" or question_3 == "J" or question_3 == "j":
                        result_round_one[2] = result_1[2]
                        print(result_round_one)

                else:  # question_0 wird mit Y,y,J oder j beantwortet

                    result_round_one[0] = result_1[0]
                    result_round_one[1] = result_1[1]
                    result_round_one[2] = result_1[2]
                    print(result_round_one)
                    break


me = HumanPlayer("Heiner", 13)
me.round_one()
