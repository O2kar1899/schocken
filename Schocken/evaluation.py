
def evaluation(result):
    print(f'RESULT STARTWERT {result} ')
    if result == [1, 1, 1]:
        result_str = 'Schock Aus'
        rank = 1

    elif (result[0] == 1 and (result[1] == 1 or result[2] == 1)) or (result[1] == 1 and result[2] == 1):  # Schock
        result_str = 'Schock'
        rank = 2

    elif result[0] == result[1] and result[0] == result[2] and result[0] != 1:  # General
        result_str = 'General'
        rank = 3

    # +++++++++++++++++++++++++++++++++++++++++++++++++ Straße fehlt noch

    else:
        result_str = 'Zahl'
        result.sort(reverse=True)
        rank = 5

    return (result_str, result, rank)
