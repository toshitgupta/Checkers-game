# Checkers Game

A simple Checkers game implemented using Python and Pygame. The game includes a graphical interface, basic game mechanics, and an AI opponent using the Minimax algorithm for optimal moves.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [How It Works](#how-it-works)
   - [Game Initialization](#game-initialization)
   - [Minimax Algorithm](#minimax-algorithm)
   - [Game Loop](#game-loop)
6. [Contributing](#contributing)

## Project Overview

This Checkers game allows two players to play checkers with a graphical interface using Pygame. One of the players can be controlled by an AI that uses the Minimax algorithm to make optimal moves.

## Features

1. Graphical user interface using Pygame.
2. Two-player mode with AI opponent.
3. AI implementation using Minimax algorithm.
4. Valid moves visualization for user.
5. Piece promotion and removal mechanics.

## Installation

To set up and run the Checkers game on your local machine, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/checkers-game.git
   cd checkers-game

2. **Install dependencies:**
   
   Ensure you have Python 3 installed. Then, install the required Python packages:

   ```bash
   pip install pygame

3. **Add assets:**
   
   Ensure the assets/crown.jpg image is available in the assets directory for the crown image on king pieces.

## Usage

To run the Checkers game, execute the following command:

```bash
python main.py
```

The game window will open, allowing you to play checkers. You can interact with the game using your mouse to select and move pieces.

## How It Works

### Game Initialization

* 'Game' Class: Manages game state, player turns, and interactions.
* 'Board' Class: Handles board setup, piece movements, and game rules.
* 'Piece' Class: Represents individual checkers pieces with attributes and methods.

### Minimax Algorithm

The Minimax algorithm is used to determine the optimal move for the AI opponent. It evaluates the game state recursively to maximize the AI's chances of winning while minimizing the player's chances.

### Game Loop

The main game loop handles:

* Event handling (mouse clicks for piece selection and movement).
* AI move calculation when it's the AI's turn.
* Game state updates and rendering using Pygame.

## Contributing

Contributions are welcome! If you have suggestions or improvements, please open an issue or submit a pull request. Ensure your code adheres to the project's coding standards and includes appropriate tests.
