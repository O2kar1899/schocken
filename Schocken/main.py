from play import RollDices
from scoring import compare_score, scoring_points, scoring_pott
import time
from rules import rules


pott = 13
human_points = 0
computer_points = 0
print(" ")
print(" Willkommen beim Würfelspiel Schocken!")
time.sleep(2)
print("\n Als Mensch bekommst Du immer den ersten Versuch!")
time.sleep(2)
print("\n Du kannst bis zu dreimal Würfel. Nach jedem Wurf (ausser nach dem 3. ;-)")
print(" kannst Du entscheiden, ob Du nochmal würfeln möchtest.")
time.sleep(2)
print("\n Ich kann höchstens so oft würfeln wie Du!")
time.sleep(1)
print("\n Mit 'Q' kannst Du das Spiel abbrechen. \n ")

print(" ")

# Hin-Runde Hölzchen vom Pott zum verlierer
print("     ****************")
print("     **  Hinrunde  **")
print("     *****************")
print("\n In der Hinrunde bekommt der Verlierer die Hölzchen \n")
while pott > 0:
    human = RollDices()
    human_play = human.human_play(3)
    human_result, human_rounds = human_play

    computer = RollDices()
    computer_play = computer.computer_play(human_result, human_rounds)
    computer_result, computer_rounds = computer_play

    compared_score = (compare_score(human_result, computer_result))
    winner_nr, compared_score_result, compared_rank = compared_score

    points = scoring_points(compared_score)
    #print(f'Points {points} ')

    pott = scoring_pott(pott, points, 'ascending')

    if winner_nr == 1:
        computer_points += points
        print("\n Du hast die Runde gewonnen! \n")

    elif winner_nr == 2:
        human_points += points
        print("\n Du hast die Runde leider verloren!\n")
    else:
        print("\n Unentschieden! Keine Wertung\n")

    print(f'Mensch: {human_result} im {human_rounds}. Versuch ')
    print(f'Computer: {computer_result} im {computer_rounds}. Versuch ')
    print(
        f' \n Aktueller Pott: {pott} \n Punktestand Mensch {human_points} \n Punktestand Computer {computer_points} \n ')

    read_rules = input("Wenn Du die Regeln lesen mötest Drücke 'R': ")
    if read_rules == "R" or "r":
        rules()

    time.sleep(2)

# Rück-Runde Hölzchen vom Gewinner zum Pott
print("     ****************")
print("     **  Rückrunde  **")
print("     *****************")
print("\n In der Rückrunde gibt der Gewinner Hölzchen ab\n")
while human_points > 0 and computer_points > 0:
    human = RollDices()
    human_play = human.human_play(3)
    human_result, human_rounds = human_play

    #print("human play:", human_play, "human_rounds: ", human_rounds)

    computer = RollDices()
    computer_play = computer.computer_play(human_result, human_rounds)
    computer_result, computer_rounds = computer_play

    compared_score = (compare_score(human_result, computer_result))
    winner_nr, compared_score_result, _ = compared_score

    #print(f'winner_nr: {winner_nr} compared_score_result: {compared_score_result} ')

    points = scoring_points(compared_score)
    print(f'Points {points} ')

    pott = scoring_pott(pott, points, 'descending')

    if winner_nr == 1:
        human_points -= points
        print("\n Du hast die Runde gewonnen! \n")
        if human_points < 0:
            human_points = 0

    elif winner_nr == 2:
        computer_points -= points
        print("\n Du hast die Runde leider verloren!\n")
        if computer_points < 0:
            computer_points = 0
    else:
        print("\n Unentschieden! Keine Wertung\n")

    print(f'Mensch: {human_result} im {human_rounds}. Versuch ')
    print(f'Computer: {computer_result} im {computer_rounds}. Versuch ')
    print(
        f' \n Aktueller Pott: {pott} \n Punktestand Mensch {human_points} \n Punktestand Computer {computer_points} \n ')

    time.sleep(3)

if computer_points == 0:
    winner_string = "der logisch denkende Computer"
else:
    winner_string = "der frei denkende Mensch"
print('##################################################')
print('')
print(f'Der Gewinner ist {winner_string}')
print('')
print('##################################################')
