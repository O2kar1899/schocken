from evaluation import evaluation
from play import RollDices
from keep_or_not import keep_human_round, keep_pc_round
from compare_score import compare_score, scoring

pot = 13


# --------------- Mensch ------------------

human = RollDices()
result = human.human_first_roll()
if keep_human_round(result) == True:
    rounds = 1
    human_result = result
else:
    rounds = 2
    result = human.human_further_roll(result)
    human_result = None

if human_result == None:
    if keep_human_round(result) == True:
        human_result = result
    else:
        rounds = 3
        human_result = human.human_further_roll(result)

erg_string, erg_list, _ = evaluation(human_result)
print(f'Dein Ergebnis: {erg_string}: {erg_list} im {rounds}. Versuch')

# +++++++++++++++++ Computer +++++++++++++++++++++++++++++++++
computer = RollDices()
result = computer.computer_first_round()
if keep_pc_round(result) == True:
    rounds = 1
    computer_result = result
else:
    rounds = 2
    result = computer.computer_first_round()
    if keep_pc_round(result) == True:
        rounds = 2
        computer_result = result
    else:
        rounds = 3
        computer_result = computer.computer_first_round()

erg_string, erg_list, _ = evaluation(computer_result)
print(f'Computer: {erg_string}: {erg_list} im {rounds}. Versuch')

# ++++++++++++++++++++++ Auswertung +++++++++++++++++++++++++++

compared_score = (compare_score(human_result, computer_result))
print(f" Compared Score {compared_score}")
winner_nr, compared_score_result, rank = compared_score
print(f"Winner {winner_nr} Result: {compared_score_result} Rank: {rank} ")
print("SCORE:", scoring(compared_score_result))
