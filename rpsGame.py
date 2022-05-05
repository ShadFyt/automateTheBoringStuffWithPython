import random
from typing import Dict

score_tracker = {"Wins": 0, "Losses": 0, "Ties": 0}
selections: Dict = {"r": "ROCK", "p": "PAPER", "s": "SCISSORS"}
key_list = list(score_tracker)
up_to = 5
while score_tracker["Wins"] < up_to:
    random_num = random.randint(0, 2)

    print("ROCK, PAPER, SCISSORS")
    print(
        f"{score_tracker.get('Wins')} {key_list[0]}, {score_tracker.get('Losses')} {key_list[1]}, {score_tracker.get('Ties')} {key_list[2]}"
    )
    print("Enter your move: (r)ock (p)aper (s)cissors or (q)uit")
    player_input = input()
    if player_input == "q":
        break
    player_move = selections[player_input]
    selection_keys = list(selections.keys())
    ai_move = selections[selection_keys[random_num]]
    print(f"{player_move} versus...")
    print(selections[selection_keys[random_num]])
    if player_move == ai_move:
        print("It is a tie!")
        score_tracker["Ties"] += 1
    elif (
        (player_move == "ROCK" and ai_move == "PAPER")
        or (player_move == "PAPER" and ai_move == "SCISSORS")
        or player_move == "SCISSORS"
        and ai_move == "ROCK"
    ):
        print("You lose!")
        score_tracker["Losses"] += 1
    else:
        print("You win!")
        score_tracker["Wins"] += 1
