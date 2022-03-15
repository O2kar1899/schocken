
from evaluation import evaluation
from human_play import *
from keep_or_not import keep_human_round_or_not, keep_pc_round_or_not
from result_comparision import *

pot = 13


# --------------- Mensch ------------------
human = Play('heiner')
result = human.first_round()
if keep_human_round_or_not(result) == True:
    rounds = 1
    human_result = result
else:
    rounds = 2
    result = human.further_rounds(result)
    human_result = None

if human_result == None:
    if keep_human_round_or_not(result) == True:
        human_result = result
    else:
        rounds = 3
        human_result = human.further_rounds(result)

erg_string, erg_list, _ = evaluation(human_result)
print(f'Dein Ergebnis: {erg_string}: {erg_list} im {rounds}. Versuch')

# +++++++++++++++++ Computer +++++++++++++++++++++++++++++++++
computer = Play('PC')
result = computer.first_round()
if keep_pc_round_or_not(result) == True:
    rounds = 1
    computer_result = result
else:
    rounds = 2
    result = computer.first_round()
    if keep_pc_round_or_not(result) == True:
        rounds = 2
        computer_result = result
    else:
        rounds = 3
        computer_result = computer.first_round()

erg_string, erg_list, _ = evaluation(computer_result)
print(f'Computer: {erg_string}: {erg_list} im {rounds}. Versuch')

# ++++++++++++++++++++++ Auswertung +++++++++++++++++++++++++++

winning_player = result_comparision(evaluation(
    human_result), evaluation(computer_result))
if winning_player == 1:
    print("Du hast die Runde gewonnen!")
elif winning_player == 2:
    print("Du hast die Runde leider verloren!")
else:
    print("Unentschieden! Keine Wertung")
