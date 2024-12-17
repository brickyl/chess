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

        # Kings
        white_king = King(0, 3, Color.WHITE, self)
        black_king = King(7, 3, Color.BLACK, self)

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
        # PSEUDOCODE
        # For each of all the opposite color pieces, check if they can capture the king using check_move.

        # white

        pass

    # each time a piece is moved, they need to call isKingInCheck AFTER THE MOVE for validity for themselves and also enemy king
    # if causing self check, invalidate the move... by reversing it?
    # if causing enemy king check, then set enemy king check status to true

    # checkmate detection(?)