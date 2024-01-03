# Tic Tac Toe

## Overview
Welcome to the classic game of Tic Tac Toe! This Python implementation allows you to play against a computer opponent. The game features a simple text-based interface and an AI opponent that randomly selects its moves.

## How to Play
1. Run the Python script to start the game.
2. Choose your symbol: ❌ or ⭕.
3. The game board is numbered from 1 to 9, representing the positions you can place your symbol.
4. Enter the position where you want to place your symbol when prompted.
5. The computer will make its move automatically.
6. The game continues until a player wins or the board is full.

## Dependencies
This project utilizes the following Python modules:
- `art`: ASCII art library for a visually appealing game interface.

## Code Structure
The code is organized into functions for better readability and modularity. Here are some key functions:

- `clear()`: Resets the game state.
- `play_again()`: Prompts the user if they want to play again.
- `check_winner(player_moves, pc_moves)`: Checks if the player or computer has won.
- `choose_symbol()`: Lets the player choose 'X' or 'O'.
- Main Game Loop: Manages the game flow, player and computer turns, and checks for a winner.

## How to Run
1. Ensure you have Python installed on your machine.
2. Download the script and run it using a Python interpreter.

```bash
python main.py
```

## Enjoy the Game!
Have fun playing Tic Tac Toe against the computer! If you have any feedback or suggestions, feel free to contribute or open an issue. Happy gaming! ❌⭕❌⭕
