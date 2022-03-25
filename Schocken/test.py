def scoring_points(compared_result):
    """from fn compare_score"""
    _, result_dices, result_rank = compared_result
    if result_rank == 1:
        points = 13
    elif result_rank == 2:
        result_dices.sort()
        points = result_dices[-1]
    elif result_rank == 3:
        points = 3
    elif result_rank == 4:
        points = 2
    elif result_rank == 5:
        points = 1
    else:
        points = 0

    return points


tup = (1, [5, 5, 5], 3)
print(scoring_points(tup))
