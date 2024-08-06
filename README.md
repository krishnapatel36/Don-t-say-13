# Don't Say 13 Interactive Book

## Overview

The "Don't Say 13" interactive book is a PDF guide designed to provide a comprehensive overview of the "Don't Say 13" game, a strategy game where players take turns saying a number between 1 and 2. The player who is forced to say the number 13 loses the game. This book generates and visualizes all possible game states and decisions, helping players understand the game's dynamics and strategies.

## Features

- **Interactive Game States**: Provides detailed pages for each game state, including current sum and possible moves.
- **Player and Computer Moves**: Displays both human and computer moves, showing the implications of each choice.
- **Game Instructions**: Includes a description of the game's rules and how to play.

## Requirements

- **Python 3.x**: Ensure you have Python installed on your system.
- **ReportLab Library**: The `reportlab` library is used to generate the PDF. Install it using pip:

  ```bash
  pip install reportlab
  ```

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/yourrepository.git
   ```

2. Navigate to the project directory:

   ```bash
   cd yourrepository
   ```

3. Install the required Python library:

   ```bash
   pip install reportlab
   ```

## Usage

1. **Run the Script**:

   ```bash
   python dont_say_13_book.py
   ```

   This will generate a PDF named `dont_say_13_book.pdf` in the same directory.

## Code Explanation

- **`generate_moves(current_sum, moves, human_turn)`**: Recursively generates all possible game states and moves from the current sum.
- **`computer_turn(current_sum)`**: Determines the optimal move for the computer based on the current sum.
- **`save_to_pdf(file_name, states)`**: Creates a PDF file with all game states and their corresponding transitions, including instructions and results.
- **`main()`**: Orchestrates the generation of game states and their conversion to PDF.

## Game Instructions

- **Objective**: Avoid being forced to say the number 13.
- **Gameplay**: Players take turns saying a number between 1 and 2. The total is accumulated with each move. The player who has to say 13 loses the game.
