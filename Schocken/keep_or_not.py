
result = [4, 5, 2]


def keep_round_or_not(result):
    if result == [1, 1, 1]:
        return [True]  # der Wurf wird behalten
    else:
        answer = input(f'Möchtest Du den Wurf: {result} behalten? (J/N): ')
        if answer == "J" or answer == "j" or answer == "Y" or answer == "y":
            return True
        else:
            return False


def keep_dice_or_not(result):
    output = []
    for element in range(len(result)):
        print(
            f'Möchtest Du Würfel {element+1} mit {result[element]} Augen behalten?')
        answer = input("J/N: ")
        if answer == "J" or answer == "j" or answer == "Y" or answer == "y":
            output.append(True)
        else:
            output.append(False)

    return output
