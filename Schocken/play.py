from dice import Dice
from keep_or_not import keep_dice, keep_human_round, keep_pc_round
from evaluation import evaluation


class RollDices():
    def __init__(self):
        self.dice = Dice(6)
        self.result = [0, 0, 0]
        self.computer_attemps = None
        self.human_attemps = None

    def human_first_roll(self):
        for i in range(3):
            self.result[i] = self.dice.roll_dice()
        return self.result

    def human_further_roll(self, result):
        kon = (keep_dice(result))
        for i in range(len(kon)):
            if kon[i] == False:
                result[i] = self.dice.roll_dice()
        self.round_number = 3

        return result

    def computer_first_round(self):
        for i in range(3):
            self.result[i] = self.dice.roll_dice()
        return self.result

    def computer_further_roll(self, roll_result):
        _, _, rank = evaluation(roll_result)

        if rank < 4 or roll_result[0] == 6:
            computer_result = self.result

        return computer_result

    def computer_play(self, computer_attemps=1):
        self.computer_attemps = computer_attemps
        result = self.computer_first_round()
        computer_rounds = 1
        if keep_pc_round(result) == True:
            computer_rounds = 1
            computer_result = result
        elif (keep_pc_round(result) == False) and (self.computer_attemps > computer_rounds):

            computer_rounds = 2
            computer_result = self.computer_first_round()

            if keep_pc_round(result) == True:
                print(
                    f'B self.computer_attemps: {self.computer_attemps} > {computer_rounds} (computer_rounds) ')
                computer_rounds = 2
                computer_result = result

            elif keep_pc_round(result) == False and self.computer_attemps > computer_rounds:
                computer_rounds = 3
                computer_result = self.computer_first_round()
        else:
            computer_result = result

        computer_result.sort
        erg_string, erg_list, _ = evaluation(computer_result)

        print(
            f'Computer: {erg_string}: {erg_list} im {computer_rounds}. Versuch')

        return computer_result, computer_rounds

    def human_play(self, human_attemps=3):
        self.human_attemps = human_attemps
        result = self.human_first_roll()
        if keep_human_round(result) == True:
            human_rounds = 1
            human_result = result
        else:
            human_rounds = 2
            result = self.human_further_roll(result)
            human_result = None

        if human_result == None:
            if keep_human_round(result) == True:
                human_result = result
            else:
                human_rounds = 3
                human_result = self.human_further_roll(result)

        # print(f'HUMAN_RESULT {human_result}')
        # print(evaluation(human_result))

        print(
            f'++++++++++++++++++++++++++++++++++++++Dein Ergebnis: {human_result} im {human_rounds}. Versuch')

        return human_result, human_rounds
