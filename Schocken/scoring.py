
from evaluation import evaluation


def compare_score(human_result, computer_result):
    human_result = evaluation(human_result)
    computer_result = evaluation(computer_result)
    r1_string, r1_val, r1_rank = human_result
    r2_string, r2_val, r2_rank = computer_result

    r1_val.sort(reverse=True)
    r2_val.sort(reverse=True)

    if r1_rank < r2_rank:
        winner = 1
    elif r1_rank > r2_rank:
        winner = 2
    else:
        if r1_rank == 2 or r1_rank == 3:
            if r1_val[0] > r2_val[0]:
                winner = 1
            elif r1_val[2] < r2_val[2]:
                winner = 2
            else:
                winner = 0

        if r1_rank == 4:
            if r1_val[0] > r2_val[0]:
                winner = 1
            elif r1_val[0] < r2_val[0]:
                winner = 2
            else:
                winner = 0

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
        result = r1_val
        rank = r1_rank

    elif winner == 2:
        result = r2_val
        rank = r2_rank

    else:
        result = None
        rank = 0

    # if rank == 1:
    #     rank_string = 'Schock Aus'
    # elif rank == 2:
    #     rank_string = 'Schock'
    # elif rank == 3:
    #     rank_string = 'General'
    # elif rank == 4:
    #     rank_string = 'Straße'
    # elif rank == 5:
    #     rank_string = 'Zahl'

    return (winner, result, rank)


def scoring_points(compared_result):
    """from fn compare_score"""
    _, result_dices, result_rank = compared_result
    if result_rank == 1:
        points = 13
    elif result_rank == 2:
       # result_dices.sort()
        points = result_dices[0]
    elif result_rank == 3:
        points = 3
    elif result_rank == 4:
        points = 2
    elif result_rank == 5:
        points = 1
    else:
        points = 0

    return points


def scoring_pott(pott, points, direction='ascending'):
    """points to pott = ascending / back = descending"""

    if direction != 'ascending' and direction != 'descending':
        """direction' can be only 'ascending or 'descendig"""
        return False

    if direction == 'ascending':
        if points > pott:
            points = pott

    if direction == 'descending':
        points *= -1

    new_pott = pott - points

    return new_pott
