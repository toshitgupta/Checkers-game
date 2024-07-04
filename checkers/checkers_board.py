import pygame
from .checkers_constant import BLACK, ROWS, YELLOW, SQUARE_SIZE, COLS, WHITE
from .checkers_board_pieces import Piece

class Board:
    def __init__(self):
        self.board = []
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0
        self.create_board()

    """
    
    draw_squares(self, win): Method that draws the yellow and black squares on the board using Pygame.

    
    """
    
    def draw_squares(self, win):
        win.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, YELLOW, (row*SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    """
    
    evaluate(self): Method that calculates and returns the 
    current score of the board based on the number of pieces and kings for each color.

    
    """
    
    def evaluate(self) :
        return self.white_left - self.red_left + (self.white_kings * 0.5 - self.red_kings * 0.5)
    

    """
    
    get_all_pieces(self, color): Method that returns a list of all the pieces on the board for a given color.
    
    """
    
    def get_all_pieces(self, color):
        pieces = []
        for row in self.board:
            for piece in row :
                if piece != 0 and piece.color == color :
                    pieces.append(piece)
        return pieces
    
    """
    
    move(self, piece, row, col): Method that updates the board 
    and the piece position when a piece is moved to a new location. 
    If the piece reaches the last row of the opponent's side, the piece is promoted to a king.

    
    """

    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row, col)

        if row == ROWS - 1 or row == 0:
            piece.make_king()
            if piece.color == WHITE:
                self.white_kings += 1
            else:
                self.red_kings += 1 
        
    """
    
    get_piece(self, row, col): Method that returns the piece object at a given row and column of the board.


    """

    def get_piece(self, row, col):
        return self.board[row][col]
    
    """
    
    create_board(self): Method that creates the initial configuration of 
    the board with the appropriate pieces in their starting positions
    
    """

    def create_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row +  1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, WHITE))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, YELLOW))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)
    
    """
    
    draw(self, win): Method that draws the board and all the pieces on the board using Pygame.
    
    """
        
    def draw(self, win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)
    
    """
    
    remove(self, pieces): Method that removes 
    the given pieces from the board and updates the number of remaining pieces for each color.

    
    """

    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color == YELLOW:
                    self.red_left -= 1
                else:
                    self.white_left -= 1
    
    """
    
    winner(self): Method that checks if a 
    color has won the game based on whether the other color has any remaining pieces.

    
    """
    
    def winner(self):
        if self.red_left <= 0:
            return WHITE
        elif self.white_left <= 0:
            return YELLOW
        
        return None 
    
    """
    
    get_valid_moves(self, piece): Method that returns a 
    dictionary of all valid moves for a given piece object.


    """
    
    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == YELLOW or piece.king:
            moves.update(self._traverse_left(row -1, max(row-3, -1), -1, piece.color, left))
            moves.update(self._traverse_right(row -1, max(row-3, -1), -1, piece.color, right))
        if piece.color == WHITE or piece.king:
            moves.update(self._traverse_left(row +1, min(row+3, ROWS), 1, piece.color, left))
            moves.update(self._traverse_right(row +1, min(row+3, ROWS), 1, piece.color, right))
    
        return moves
    

    """
    
    _traverse_left(self, start, stop, step, color, left, skipped=[]), 
    _traverse_right(self, start, stop, step, color, right, skipped=[]): 
    Private helper methods used by the get_valid_moves method to traverse 
    the board in search of valid moves for a given piece object. 
    These methods return a dictionary of all valid moves for a given piece object in the given direction.



    
    """

    def _traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break
            
            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last
                
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)
                    moves.update(self._traverse_left(r+step, row, step, color, left-1,skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, left+1,skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            left -= 1
        
        return moves

    def _traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break
            
            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r,right)] = last + skipped
                else:
                    moves[(r, right)] = last
                
                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)
                    moves.update(self._traverse_left(r+step, row, step, color, right-1,skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, right+1,skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1
        
        return moves