# Tic Tac Toe
import art
import random
from itertools import permutations

# Constants
NUM_CELLS = 9

# Global Variables
player_turns = []
pc_turns = []
exclude_values = []
winning_turns = [
    [1, 2, 3], [4, 5, 6], [7, 8, 9],  # Rows
    [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Columns
    [1, 5, 9], [3, 5, 7]  # Diagonals
]


def clear():
    """Clear the game state."""
    # Reset global variables
    player_turns.clear()
    pc_turns.clear()
    exclude_values.clear()
    return 1, art.field


def play_again():
    """Prompt the user if they want to play again."""
    return input("Do you want to play again? Y/N ").upper() == "Y"


def check_winner(player_moves, pc_moves):
    """Check if the player or computer has won."""
    for winning_combo in winning_turns:
        if all(cell in player_moves for cell in winning_combo):
            print("😎🏆You Win!!!🏆😎")
            return True
        elif all(cell in pc_moves for cell in winning_combo):
            print("😒🫂You Lose!!!🫂😒")
            return True
    return False


def choose_symbol():
    """Let the player choose 'X' or 'O'."""
    while True:
        player_choice = input("Choose your fighter: ❌ or ⭕? ").upper()
        if player_choice in ['X', 'O']:
            player = '❌ ' if player_choice == "X" else '⭕ '
            pc = '⭕ ' if player_choice == 'X' else '❌ '
            print(f"Fantastic! You choose: {player}")
            print(f"Computer plays with: {pc}")
            return player, pc
        else:
            print("Please choose a valid letter (X or O)")


# Main Game Loop
print(f"Welcome to the game! {art.logo}\n")
while True:
    turn, field = clear()
    player, pc = choose_symbol()

    while turn <= 4:
        player_turn = input(f"Where? Choose a place for your {player} \n{field}")

        if not player_turn.isdigit() or int(player_turn) > NUM_CELLS:
            print(f"👾Please choose a valid number (1-{NUM_CELLS})")
        elif int(player_turn) in pc_turns or int(player_turn) in player_turns:
            print("🚫Already taken! Please choose a different position!")
        else:
            player_turns.append(int(player_turn))
            new_field = field.replace(f" {str(player_turn)} ", player)
            print(new_field)
            print(f"Your moves: {player_turns}")

            exclude_values = player_turns + pc_turns
            if check_winner(player_turns, pc_turns):
                break

            pc_turn = random.choice([x for x in range(1, NUM_CELLS + 1) if x not in exclude_values])
            print(f"🤖 puts {pc} in {pc_turn}")
            pc_turns.append(pc_turn)
            print(f"🤖 moves: {pc_turns}")

            if check_winner(player_turns, pc_turns):
                break

            new_field = new_field.replace(f" {str(pc_turn)} ", pc)
            print(new_field)
            field = new_field
            turn += 1
    else:
        print("🤯☮️Nobody wins...☮️🤯")

    if not play_again():
        print("Goodbye! Thanks for playing.❌⭕❌⭕")
        break
