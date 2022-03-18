
def evaluation(result):
    if result[0] == 1 and result[1] == 1 and result[2] == 1:
        return ("Schock Aus", result, 1)

    elif (result[0] == 1 and (result[1] == 1 or result[2] == 1)) or (result[1] == 1 and result[2] == 1):  # Schock
        for i in range(3):
            if result[i] != 1:
                schock = result
        return ("Schock", schock, 2)

    elif result[0] == result[1] and result[0] == result[2] and result[0] != 1:  # General
        general = result
        return ("General", general, 3)

    # +++++++++++++++++++++++++++++++++++++++++++++++++ Straße fehlt noch

    else:
        result.sort(reverse=True)       # Zahl
        return ("Zahl", result, 5)
