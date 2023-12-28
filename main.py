# Tic Tac Toe
import art
import random

def play_again():
    again = input("Do You Want to play again? Y/N").upper()
    if again == "Y":
        is_on = True
        turn = 1
        field = art.field
        pc_turns = []
        player_turns = []
        exclude_values = []
        return is_on,turn,field,pc_turns,player_turns,exclude_values
    else:
        is_on = False
        return is_on

print(f"Welcome to the {art.logo}  game!")

is_on = False
pc = ""
field = art.field
player_turns = []
pc_turns = []
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

while not is_on:
    player = input(f"Choose your fighter: 'X' or 'O'? ").upper()
    if player == "X" or player == "O":
        print(f"Fantastic! you choose: {player.upper()}")
        if player == "X":
            pc = "O"
            print(f"Computer plays with: {pc}")
        elif player == "O":
            pc = "X"
            print(f"Computer plays with: {pc}")
        while turn != 5:
            player_turn = input(f"Where ? Choose a place for your {player}\n{field}")

            if int(player_turn) in pc_turns:
                print("Already taken! Please choose a different position!")
                player_turn = input(f"Where ? Choose a place for your {player}\n{field}")
            else:
                player_turns.append(int(player_turn))
                field = field.replace(str(player_turn), player)
                print(field)
                print(f"your moves: {player_turns}")
                exclude_values = player_turns + pc_turns
                pc_turn = random.choice([x for x in range(1, 10) if x not in exclude_values])

                print(f"Computer put its {pc} in {pc_turn}")
                pc_turns.append(pc_turn)
                print(f"Pc moves: {pc_turns}")

                new_field = field.replace(str(pc_turn), pc)
                field = new_field
                turn += 1

            if player_turns in winning_turns:
                print("😎🏆You Win!!!🏆😎")
                play_again()

            elif pc_turns in winning_turns:
                print("😒🫂You lose!!!")
                play_again()

        # print(pc)
        is_on = True

    else:
        print(f"please choose a valid letter (0_0)")



# TODO fare che non crasha se mette altro quando deve scegliere la posizione
# todo svuotare le liste dopo play again



