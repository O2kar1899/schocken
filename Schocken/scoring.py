from evaluation import evaluation


def compare_score(human_result=(None, None, None), computer_result=(None, None, None)):
    human_result = evaluation(human_result)
    computer_result = evaluation(computer_result)
    r1_string, r1_val, r1_rank = human_result
    r2_string, r2_val, r2_rank = computer_result

    # print(
    #     f' r1-String: {r1_string} \n r1_val: {r1_val} \n r1_rank: {r1_rank} ')
    # print(
    #     f' r2-String: {r2_string} \n r2_val: {r2_val} \n r2_rank: {r2_rank} ')

    if r1_rank < r2_rank:
        winner = 1
    elif r1_rank > r2_rank:
        winner = 2
    else:
        if r1_rank == 2 or r1_rank == 3:
            if r1_val[2] > r2_val[2]:
                winner = 1
            elif r1_val[2] < r2_val[2]:
                winner = 2
            else:
                winner = 0

        if r1_rank == 4:
            pass

        if r1_rank == 5:
            if r1_val[0] > r2_val[0]:
                winner = 1
            elif r1_val[0] < r2_val[0]:
                winner = 2
            else:
                if r1_val[1] > r2_val[1]:
                    winner = 1
                elif r1_val[1] < r2_val[1]:
                    winner = 2
                else:
                    if r1_val[2] > r2_val[2]:
                        winner = 1
                    if r1_val[2] < r2_val[2]:
                        winner = 2
                    else:
                        winner = 0

    if winner == 1:
        print("Du hast die Runde gewonnen!")
        result = r1_val

    elif winner == 2:
        print("Du hast die Runde leider verloren!")
        result = r2_val

    else:
        print("Unentschieden! Keine Wertung")
        result = None

    if winner == 1:
        rank = r1_rank
    elif winner == 2:
        rank = r2_rank
    else:
        rank = None

    return (winner, result, rank)


def scoring_points(compared_result):
    """from fn compare_score"""
    _, result_dices, result_rank = compared_result
    if result_rank == 1:
        points = 13
    elif result_rank == 2:
        result_dices.sort(reverse=True)
        points = result_dices[-1]
    elif result_rank == 3:
        points = 3
    elif result_rank == 4:
        points = 2
    elif result_rank == 5:
        points = 1

    return points


def scoring_pott(pott, points, direction='ascending'):
    """points to pott = ascending / back = descending"""

    if direction is not 'ascending' and direction is not 'descending':
        print("'direction' can be only 'ascending or 'descendig'")
        return False

    if points > pott:
        points = pott
    if direction == 'descending':
        points = points*(-1)

    new_pott = pott + points

    return new_pott