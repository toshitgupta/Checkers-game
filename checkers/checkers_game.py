import pygame
from .checkers_constant import YELLOW, WHITE, BLUE, SQUARE_SIZE
from checkers.checkers_board import Board



"""

update(self): This method updates the game display by 
calling the draw method of the game board and drawing 
valid moves on the window, then updates the game window using Pygame.

_init(self): This method initializes the game
 variables such as self.selected, self.board, self.turn, and self.valid_moves.

winner(self): This method returns the winner of the game, 
which is determined by the winner method of the game board.

reset(self): This method resets the game by calling the _init method.

select(self, row, col): This method selects a piece on the
 game board by getting the piece at the specified location 
 and checking if it is of the correct color. If it is, it 
 sets the piece as the self.selected piece and retrieves its valid moves, which are stored in self.valid_moves.

_move(self, row, col): This method moves a piece on the game 
board if the move is valid. It checks if the specified location 
is a valid move for the selected piece, and if it is, it moves 
the piece to that location, removes any pieces that were jumped over, and changes the turn.

draw_valid_moves(self, moves): This method draws valid moves 
on the game window by drawing blue circles on each valid move.

change_turn(self): This method changes the turn 
from the current player to the next player.

get_board(self): This method returns the current game board.

ai_move(self, board): This method performs a move for 
the AI player by changing the current game board to the specified board and changing the turn.



"""


class Game:
    def __init__(self, win):
        self._init()
        self.win = win
    
    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = YELLOW
        self.valid_moves = {}

    def winner(self):
        return self.board.winner()

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)
        
        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True
            
        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False

        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == YELLOW:
            self.turn = WHITE
        else:
            self.turn = YELLOW
    
    def get_board(self) :
        return self.board
    
    def ai_move(self, board):
        self.board = board
        self.change_turn()