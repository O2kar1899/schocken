from unittest import result
from dice import Dice
import time


class HumanPlayer():
    def __init__(self, name="unknown", wurf=[], number_of_points=0):
        self.name = name
        self.number_of_point = number_of_points
        self.wurf = wurf

    def roll(self):
        dice = Dice(6)  # Würfel mit 6 Seiten
        result = dice.roll_dice()
        self.wurf.append(result)
        return self.wurf

    def evaluation(self, result=[0, 0, 0]):
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

    def keep_or_dicard(self, results=[], counter=1):
        self.results = results
        self.counter = counter
        keep = []
        for value in self.results:
            answer = input(f"Möchtest Du Würfel {self.counter} ehalten? Y/N")
            if answer == "Y":
                keep.append(value)
            else:
                keep.append("X")

            self.counter += 1
            print(keep)
            return keep

        #     if i < 2:
        #         print(f"{self.name} möchtest Du das Ergebnis stehen lassen?")
        #         print(f"Der Gegner hat dann auch {(i+1)} Versuche.")
        #         question_0 = input(
        #             "Gebe 'y' für stehen lassen oder 'N' für weiter würfeln ein ")

        #         if question_0 != "Y" and question_0 != "y" and question_0 != "J" and question_0 != "j":

        #             if result_round_one[0] == "X":
        #                 question_1 = input(
        #                     f"{self.name} möchtest Du Würfel 1 ({result_1[0]} Augen) behalten? Y/N ")
        #                 if question_1 == "Y" or question_1 == "y" or question_1 == "J" or question_1 == "j":
        #                     result_round_one[0] = result_1[0]

        #             if result_round_one[1] == "X":
        #                 question_2 = input(
        #                     f"2 Möchtest Du Würfel 2 ({result_2[0]} Augen) behalten? Y/N ")
        #                 if question_2 == "Y" or question_2 == "y" or question_2 == "J" or question_2 == "j":
        #                     result_round_one[1] = result_1[1]

        #             question_3 = input(
        #                 f"3 Möchtest Du Würfel 3 ({result_3[0]} Augen) behalten? Y/N ")
        #             if question_3 == "Y" or question_3 == "y" or question_3 == "J" or question_3 == "j":
        #                 result_round_one[2] = result_1[2]
        #                 print(result_round_one)

        #         else:  # question_0 wird mit Y,y,J oder j beantwortet

        #             result_round_one[0] = result_1[0]
        #             result_round_one[1] = result_1[1]
        #             result_round_one[2] = result_1[2]
        #             print(result_round_one)
