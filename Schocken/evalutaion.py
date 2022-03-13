
def evaluation(result=[0, 0, 0]):
    if result[0] == result[1] and result[0] == result[2] and result[0] != 1:  # General
        general = result[0]
        return f"General {result[0]}"
    elif result[0] == 1 and result[1] == 1 and result[2] == 1:  # Schock Aus
        return "Schock Aus"
    elif (result[0] == 1 and (result[1] == 1 or result[2] == 1)) or (result[1] == 1 and result[2] == 1):  # Schock
        for i in range(3):
            if result[i] != 1:
                schock = result[i]
        return f"Schock {schock}"
    else:
        result.sort(reverse=True)       # Zahl
        return f"Zahl: {result} "
