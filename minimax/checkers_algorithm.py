from copy import deepcopy
import pygame

YELLOW = (255,0,0)
WHITE = (255, 255, 255)


"""
It uses the minimax algorithm to find the optimal move in the checkers game. 
The function takes four arguments:

1) position: the current state of the game, 
represented as an object with methods to access information about the game state.

2) depth: the depth of the search tree to explore. 
The higher the depth, the more accurate the result, 
but also the more computationally expensive the search becomes.

3) max_player: a boolean that indicates whether it is the turn of the player who 
wants to maximize the evaluation function.

4) game: an object that represents the game being played, with methods to get 
all possible moves for a given player.

The function recursively explores the search tree, evaluating each possible 
move and selecting the one that maximizes the score for the max player, and 
minimizes the score for the min player.

The evaluation function used in this implementation is defined in the "evaluate" 
method of the "position" object, which should return a score for the current game state. 
The higher the score, the better the position is for the max player, and the worse it is for the min player.

"""

def minimax_algorithm(position, depth, max_player, game):
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position
    
    if max_player:
        maxEval = float('-inf')
        best_move = None
        for move in get_all_moves_board(position, WHITE, game):
            evaluation = minimax_algorithm(move, depth-1, False, game)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                best_move = move
        
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        for move in get_all_moves_board(position, YELLOW, game):
            evaluation = minimax_algorithm(move, depth-1, True, game)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                best_move = move
        
        return minEval, best_move
    

"""
It simulates a move in a board game. The function takes five arguments:

1) piece: the game piece to be moved.
2) move: a tuple containing the coordinates of the destination square.
3) board: the current state of the game board, represented as an object 
with methods to access and modify the game state.
4) game: an object that represents the game being played, with methods 
to get all possible moves for a given player.
5) skip: a game piece that has been removed from the board as a result of 
a previous move, indicating that the current piece can jump over it.

The function updates the game board by moving the given piece to the 
destination square and removing the skipped piece if there is one. It then returns the updated board object.

"""


def simulate_move_checkers(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board


"""

This is a Python function that generates all possible moves for a given player in a board game. The function takes three arguments:

1) board: the current state of the game board, represented as an object 
with methods to access and modify the game state.
2) color: the color of the player for whom 
moves are being generated.
3) game: an object that represents the game being played, 
with methods to get all possible moves for a given player.
The function generates all possible moves for each piece of the specified color, 
using the "get_valid_moves" method of the "board" object to get a dictionary of 
valid moves and their corresponding skipped pieces. For each valid move, 
the function creates a copy of the board using the "deepcopy" function, 
simulates the move using the "simulate_move_checkers" function, and adds the 
resulting board state to a list of all possible moves.

"""


def get_all_moves_board(board, color, game):
    moves = []

    for piece in board.get_all_pieces(color):
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move_checkers(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)
    
    return moves


"""

This is a Python function that draws the valid moves of a given game 
piece on the game board. The function takes three arguments:

1) game: an object that represents the game being played, 
with methods to draw the game board and pieces.
2) board: the current state of the game board, represented 
as an object with methods to access and modify the game state.
3) piece: the game piece for which valid moves are being drawn.

The function first gets a dictionary of valid moves for the piece using the 
"get_valid_moves" method of the "board" object. It then calls the
 "draw" method of the "board" object to draw the current state of the 
 game board on the Pygame window. It then draws a green circle around the 
 current piece using the "pygame.draw.circle" function to indicate the selected piece.

The function then calls the "draw_valid_moves" method of the "game" object, 
which takes a list of valid move coordinates as an argument and 
draws a red circle around each valid move location on the game board.

Finally, the function calls "pygame.display.update()" to update the Pygame window with the changes made to the game board.

"""

def draw_moves_checkers(game, board, piece):
    valid_moves = board.get_valid_moves(piece)
    board.draw(game.win)
    pygame.draw.circle(game.win, (0,255,0), (piece.x, piece.y), 50, 5)
    game.draw_valid_moves(valid_moves.keys())
    pygame.display.update()
