
def evaluation(result):
    result.sort(reverse=True)

    if result == [1, 1, 1]:
        result_str = 'Schock Aus'
        rank = 1

    elif result[-1] == 1 and result[-2] == 1:  # Schock
        result_str = 'Schock'
        rank = 2

    elif result[0] == result[1] and result[0] == result[2] and result[0] != 1:  # General
        result_str = 'General'
        rank = 3

    elif result[1] == result[0]-1 and result[2] == result[1]-1:
        result_str = "Straße"
        rank = 4

    else:
        result_str = 'Zahl'
        rank = 5

    return (result_str, result, rank)
