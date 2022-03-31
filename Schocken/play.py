from dice import Dice
from keep_or_not import keep_dice, keep_human_round, keep_pc_round
from evaluation import evaluation


class RollDices():
    def __init__(self):
        # festlegen wie viele Seiten der Würfel hat
        self.dice = Dice(6)
        # die Liste result hat soviele werte, wie Würfel geworfen werden.
        self.result = [0, 0, 0]
        # der Computer bekommt nur soviele Versuche, wie der Mensch genutzt hat
        self.computer_attemps = None
        self.human_attemps = None

    # für den ersten Wurf werden alle drei Würfel genutzt
    def human_first_roll(self):
        for i in range(3):
            self.result[i] = self.dice.roll_dice()
        return self.result

    # in der funktion keep.dice wird ermittelt welche Würfel der Mensch behalten möchte
    def human_further_roll(self, result):
        kd = (keep_dice(result))
        for i in range(len(kd)):
            if kd[i] == False:
                result[i] = self.dice.roll_dice()
        return result

    # der Computer nutzt immer alle Würfel - schön blöd!
    def computer_first_round(self):
        for i in range(3):
            self.result[i] = self.dice.roll_dice()
        return self.result

    # def computer_further_roll(self, roll_result):
    #     _, _, rank = evaluation(roll_result)

    #     if rank < 4 or roll_result[0] == 6:
    #         computer_result = self.result

    #     return computer_result

    def computer_play(self, human_result, computer_attemps=1):
        self.computer_attemps = computer_attemps
        result = self.computer_first_round()
        computer_rounds = 1
        if keep_pc_round(result, human_result) == True:
            computer_rounds = 1
            computer_result = result
        elif (keep_pc_round(result, human_result) == False) and (self.computer_attemps > computer_rounds):

            computer_rounds = 2
            computer_result = self.computer_first_round()

            if keep_pc_round(result, human_result) == True:

                computer_rounds = 2
                computer_result = result

            elif keep_pc_round(result, human_result) == False and self.computer_attemps > computer_rounds:
                computer_rounds = 3
                computer_result = self.computer_first_round()
        else:
            computer_result = result

        erg_string, erg_list, _ = evaluation(computer_result)

        return computer_result, computer_rounds

    def human_play(self, human_attemps=3):
        self.human_attemps = human_attemps
        result = self.human_first_roll()
        human_result = None
        if keep_human_round(result) == True:
            human_rounds = 1
            human_result = result
        else:
            result = self.human_further_roll(result)
            human_rounds = 1

        if human_result == None:
            if keep_human_round(result) == True:
                human_result = result
                human_rounds = 2
            else:
                result = self.human_further_roll(result)
                #human_result = result
                human_rounds = 2

        if human_result == None:
            if keep_human_round(result) == True:
                human_result = result
                human_rounds = 3
            else:
                result = self.human_further_roll(result)
                human_result = result
                human_rounds = 3

        return human_result, human_rounds
