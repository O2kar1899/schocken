

from numpy import result_type

# rank 1 = Schock Aus
# rank 2 = Schock
# rank 3 = General
# rank 4 = Straße
# rank 5 = Zahl


def result_comparision(result_1=(None, None, None), result_2=(None, None, None)):
    r1_string, r1_val, r1_rank = result_1
    r2_string, r2_val, r2_rank = result_2

    print(f'R1 {r1_val} R2 {r2_val} ')

    if r1_rank < r2_rank:
        return 1
    elif r1_rank > r2_rank:
        return 2
    else:
        if r1_rank == 2 or r1_rank == 3:
            if r1_val > r2_val:
                return 1
            elif r1_val < r2_val:
                return 2
            else:
                return 0

        if r1_rank == 4:
            pass

        if r1_rank == 5:
            if r1_val[0] > r2_val[0]:
                return 1
            if r1_val[0] < r2_val[0]:
                return 2
            else:
                if r1_val[1] > r2_val[1]:
                    return 1
                if r1_val[1] < r2_val[1]:
                    return 2
                else:
                    if r1_val[2] > r2_val[2]:
                        return 1
                    if r1_val[2] < r2_val[2]:
                        return 2
                    else:
                        return 0


# R1 = ("Zahl", [5, 5, 6], 5)
# R2 = ("Zahl", [5, 5, 4], 5)
# print(result_comparision(R1, R2))
