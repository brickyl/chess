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

        # Pawns
        for i in range(8):
            for j in range(8):
                if i == 1:
                    pawn = Pawn(i, j, Color.WHITE)
                    self.board[i][j] = pawn

                if i == 6:
                    pawn = Pawn(i, j, Color.BLACK)
                    self.board[i][j] = pawn
        
        # Queens
        self.board[0][4] = Queen(0, 4, Color.WHITE)
        self.board[7][4] = Queen(7, 4, Color.BLACK)

        # Kings
        self.board[0][3] = King(0, 3, Color.WHITE)
        self.board[7][3] = King(7, 3, Color.BLACK)

        # Rooks
        self.board[0][0] = Rook(0, 0, Color.WHITE)
        self.board[0][7] = Rook(0, 7, Color.WHITE)
        self.board[7][0] = Rook(7, 0, Color.BLACK)
        self.board[7][7] = Rook(7, 7, Color.BLACK)

        # Bishops
        self.board[0][2] = Bishop(0, 2, Color.WHITE)
        self.board[0][5] = Bishop(0, 5, Color.WHITE)
        self.board[7][2] = Bishop(7, 2, Color.BLACK)
        self.board[7][5] = Bishop(7, 5, Color.BLACK)

        # Knights 
        self.board[0][1] = Knight(0, 1, Color.WHITE)
        self.board[0][6] = Knight(0, 6, Color.WHITE)
        self.board[7][1] = Knight(7, 1, Color.BLACK)
        self.board[7][6] = Knight(7, 6, Color.BLACK)

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

    def isKingInCheck(self):
        # PSEUDOCODE
        # For each of all the opposite color pieces, check if they can capture the king using check_move.

        # black
        # white
        pass

    # each time a piece is moved, they need to call isKingInCheck AFTER THE MOVE for validity for themselves and also enemy king
    # if causing self check, invalidate the move... by reversing it?
    # if causing enemy king check, then set enemy king check status to true

    # checkmate detection(?)