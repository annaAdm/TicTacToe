# Tic Tac Toe
import art
import random
from itertools import permutations


def clear():
    go_again=True
    turn = 1
    pc_turns.clear()
    player_turns.clear()
    exclude_values.clear()
    return field,turn,go_again


def play_again():
    again = input("Do You Want to play again? Y/N").upper()
    if again == "Y":
        clear()
    else:
        go_again = False
        return go_again


def check_winner(player_moves, pc_moves):
    player_permutations = list(permutations(player_moves, 3))
    pc_permutations = list(permutations(pc_moves,3))
    for perm in player_permutations :
        if list(perm) in winning_turns:
            print("😎🏆You Win!!!🏆😎")
            play_again()

    for perm in pc_permutations:
        if list(perm) in winning_turns:
            print("😒🫂You Lose!!!🫂😒")
            play_again()


def choose_symbol():
    player = input(f"Choose your fighter: 'X' or 'O'? ").upper()
    if player == "X" or player == "O":
        print(f"Fantastic! you choose: {player.upper()}")
        if player == "X":
            pc = "O"
            print(f"Computer plays with: {pc}")
        elif player == "O":
            pc = "X"
            print(f"Computer plays with: {pc}")
    else:
        print(f"please choose a valid letter (0_0)")

    return player,pc

#-------------------------------------------------------------------------------------
go_again = True
pc = ""
field = art.field
player_turns = []
pc_turns = []
exclude_values = []
turn = 1
winning_turns = [
    # Rows
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    # Columns
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    # Diagonals
    [1, 5, 9],
    [3, 5, 7]
]
#------------------------------------------- Start -------------------------------------------
print(f"Welcome to the {art.logo}  game!")


while go_again:
    turn= 1
    go_again = True
    field = art.field
    player, pc = choose_symbol()
    while turn < 5 and go_again:
        player_turn = input(f"Where? Choose a place for your {player}\n{field}")

        if not player_turn.isnumeric() or int(player_turn) > 9:
            print(f"please choose a valid number (1-9)")
        elif int(player_turn) in pc_turns:
            print("Already taken! Please choose a different position!")
        else:
            player_turns.append(int(player_turn))
            new_field = field.replace(str(player_turn), player)
            print(new_field)
            print(f"your moves: {player_turns}")

            check_winner(player_turns, pc_turns)

            exclude_values = player_turns + pc_turns
            pc_turn = random.choice([x for x in range(1, 10) if x not in exclude_values])
            print(f"Computer put its {pc} in {pc_turn}")
            pc_turns.append(pc_turn)
            print(f"Pc moves: {pc_turns}")
            check_winner(player_turns, pc_turns)

            new_field = new_field.replace(str(pc_turn), pc)
            print(new_field)
            turn += 1
    else:
        print("Nobody wins..")
        play_again()

else:
    print("Goodbye! Thanks for playing.")



# TODO reset field
# todo svuotare le liste dopo play again



