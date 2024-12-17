from pieces.pawn import Pawn
from pieces.bishop import Bishop
from pieces.rook import Rook
from pieces.queen import Queen
from pieces.king import King
from pieces.knight import Knight
from constants import Color, Move


class Board:
    def __init__(self):
        self.board = [[None for i in range(8)] for j in range(8)]
        self.white = []
        self.black = []
        self.white_king = King(0, 3, Color.WHITE, self)
        self.black_king = King(7, 3, Color.BLACK, self)
        self.reverse_add_pieces = [] # holds sequence of pieces to be placed on the board
        self.reverse_rem_pieces = [] # holds sequence of pieces to be removed from the board --> do I need to find equality


        # Pawns
        for i in range(8):
            for j in range(8):
                if i == 1:
                    pawn = Pawn(i, j, Color.WHITE, self)

                if i == 6:
                    pawn = Pawn(i, j, Color.BLACK, self)

        # Queens
        white_queen = Queen(0, 4, Color.WHITE, self)
        black_queen = Queen(7, 4, Color.BLACK, self)

        # Rooks
        white_rook_1 = Rook(0, 0, Color.WHITE, self)
        white_rook_2 = Rook(0, 7, Color.WHITE, self)
        black_rook_1 = Rook(7, 0, Color.BLACK, self)
        black_rook_2 = Rook(7, 7, Color.BLACK, self)

        # Bishops
        white_bish_1 = Bishop(0, 2, Color.WHITE, self)
        white_bish_2 = Bishop(0, 5, Color.WHITE, self)
        black_bish_1 = Bishop(7, 2, Color.BLACK, self)
        black_bish_2 = Bishop(7, 5, Color.BLACK, self)

        # Knights
        white_knight_1 = Knight(0, 1, Color.WHITE, self)
        white_knight_2 = Knight(0, 6, Color.WHITE, self)
        black_knight_1 = Knight(7, 1, Color.BLACK, self)
        black_knight_2 = Knight(7, 6, Color.BLACK, self)

    def printBoard(self):
        # debugging mode: the rows are 0-indexed right now
        print()
        for i in range(len(self.board)):
            line = str(i + 1) + "  "
            for j in range(len(self.board[0])):
                piece = self.board[i][j]
                if piece == None:
                    line += "x"
                    line += " "
                else:
                    line += str(piece)
                    line += " "
            print(line)
        print()
        print("   h g f e d c b a")
        print()

    def getPieceAtLocation(self, row, col):
        piece = self.board[row][col]
        return piece

    def setPieceAtLocation(self, row, col, piece):
        self.board[row][col] = piece

    def checkDetect(self):
        # instead of checking every single piece, maybe check the row, column, and diagonals 
        # that the king is on, plus knights of the opposite color. only check until you run
        # into a piece (only knight can jump).
        for piece in self.black:
            if piece.check_move(self, self.white_king.row, self.white_king.col, None):
                return Color.WHITE
            
        for piece in self.white:
            if piece.check_move(self, self.black_king.row, self.black_king.col, None):
                return Color.BLACK
        
        return None
    
    # if you are in check, you must get out of check
    # you cannot make a move that puts you or leaves you in check (same thing)
    # how to validate a move without making it??? -- my current approach: you do make it. you just reverse it
    # reverse move

    # checkmate detection(?)
    # checkmate is when no matter what move you make, your king will get gobbled up nom nom
    # checkmate also occurs when you cannot make any valid moves while being in check <-- stop counting as soon as there's 1 valid move
    # stalemate occurs when you cannot make any valid moves while NOT in check <-- stop counting as soon as there's 1 valid move
    # can count number of moves SMARTLY for each piece

    # each time a piece is moved, they need to call checkDetect AFTER THE MOVE for validity for themselves and also enemy king
    # if causing self check, invalidate the move... by reversing it?
    # if causing enemy king check, then set enemy king check status to true


