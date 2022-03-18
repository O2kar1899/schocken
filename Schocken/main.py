from evaluation import evaluation
from play import RollDices
from keep_or_not import keep_human_round, keep_pc_round
from scoring import compare_score, scoring_points, scoring_pott


pott = 13
human_points = 0
computer_points = 0

while pott > 0:
    human = RollDices()
    human_play = human.human_play(3)
    human_result, human_rounds = human_play

    computer = RollDices()
    computer_play = computer.computer_play(human_rounds)
    computer_result, computer_rounds = computer_play

    compared_score = (compare_score(human_result, computer_result))
    winner_nr, compared_score_result, _ = compared_score

    points = scoring_points(compared_score)
    print(f'Points {points} ')

    pott = scoring_pott(pott, points, 'ascending')

    if winner_nr == 1:
        human_points += points
    elif winner_nr == 2:
        computer_points += points
    else:
        pass

    print(
        f' Aktueller Pott: {pott} \n Punktestand Mensch {human_points} \n Punktestand Computer {computer_points} ')
