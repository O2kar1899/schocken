import pygame


def keep_human_round(result):
    if result == [1, 1, 1]:
        return [True]  # der Wurf wird behalten
    else:
        answer = input(f'Möchtest Du den Wurf: {result} behalten? (J/N): ')
        if answer == "J" or answer == "j" or answer == "Y" or answer == "y":
            return True
        elif answer == 'q' or answer == 'Q':
            quit()
        else:
            return False


def keep_pc_round(result):
    if (result[0] == 1 and (result[1] == 1 or result[2] == 1) or (result[1] == 1 and result[2] == 1)) \
            or result[0] == 6 or (result[0] == result[1] and result[0] == result[2]):
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
            quit()
        else:
            output.append(False)

    return output
