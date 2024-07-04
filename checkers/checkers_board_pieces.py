from .checkers_constant import YELLOW, WHITE, SQUARE_SIZE, GREY, CROWN_IMAGE
import pygame

class Piece:
    PADDING = 15
    OUTLINE = 2

    """
    
    The __init__ method initializes the attributes of the piece, 
    including its row and column positions, its color, and whether 
    or not it is a king piece. It also sets the initial x and y 
    positions of the piece on the board by calling the calc_pos method.
    
    """

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

        
        """
        
        The calc_pos method calculates the x and y pixel positions 
        of the piece on the board based on its row and column 
        positions and the size of each square on the board.

        """
    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

        """
        
        The make_king method sets the king attribute of the 
        piece to True, indicating that the piece has been promoted to a king piece.

        """

    def make_king(self):
        self.king = True

    
    """
    
    The draw method takes a Pygame window object as an argument and draws the piece on 
    the board. It first draws a grey circle as the background of the piece, then draws a 
    colored circle on top of it representing the piece. If the piece is a king, it also 
    draws a crown image on top of the piece.

    """
    
    def draw(self, win):
        radius = SQUARE_SIZE//2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            win.blit(CROWN_IMAGE, (self.x - CROWN_IMAGE.get_width()//2, self.y - CROWN_IMAGE.get_height()//2))

    """
    
    The move method updates the row and column positions of the piece and recalculates 
    its x and y positions on the board by calling the calc_pos method.
    
    """

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    """
    
    The __repr__ method returns a string representation of the piece's color.

    """

    def __repr__(self):
        return str(self.color)