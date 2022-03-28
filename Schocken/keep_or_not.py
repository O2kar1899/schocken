import sys
from scoring import compare_score


def keep_human_round(result):
    if result == [1, 1, 1]:
        return [True]  # der Wurf wird behalten
    else:
        answer = input(f'Möchtest Du den Wurf: {result} behalten? (J/N): ')
        if answer == "J" or answer == "j" or answer == "Y" or answer == "y":
            return True
        elif answer == 'q' or answer == 'Q':
            exit()
        else:
            return False


def keep_pc_round(computer_result, human_result):

    if compare_score(human_result, computer_result)[0] == 2:
        return True
    else:
        return False


def keep_dice(result):
    output = []
    for element in range(len(result)):
        print(
            f'Möchtest Du Würfel {element+1} mit {result[element]} Augen behalten?')
        answer = input("J/N: ")
        if answer == "J" or answer == "j" or answer == "Y" or answer == "y":
            output.append(True)
        elif answer == 'q' or answer == 'Q':
            exit()
        else:
            output.append(False)

    return output
