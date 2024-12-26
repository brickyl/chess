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

        # Pawns
        for i in range(8):
            for j in range(8):
                if i == 1:
                    Pawn(i, j, Color.WHITE, self)

                if i == 6:
                    Pawn(i, j, Color.BLACK, self)

        # Queens
        Queen(0, 4, Color.WHITE, self)
        Queen(7, 4, Color.BLACK, self)

        # Rooks
        Rook(0, 0, Color.WHITE, self)
        Rook(0, 7, Color.WHITE, self)
        Rook(7, 0, Color.BLACK, self)
        Rook(7, 7, Color.BLACK, self)

        # Bishops
        Bishop(0, 2, Color.WHITE, self)
        Bishop(0, 5, Color.WHITE, self)
        Bishop(7, 2, Color.BLACK, self)
        Bishop(7, 5, Color.BLACK, self)

        # Knights
        Knight(0, 1, Color.WHITE, self)
        Knight(0, 6, Color.WHITE, self)
        Knight(7, 1, Color.BLACK, self)
        Knight(7, 6, Color.BLACK, self)

    def printBoard(self):
        # debugging mode: the rows are 0-indexed right now
        print()
        print("[chess] --- Board ---")
        for i in range(len(self.board)):
            line = "  " + str(i + 1) + "  "
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
        print("     h g f e d c b a")
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
    
    def pieceRemoval(self, piece):
        # function to remove a piece from a board using row and col
        self.setPieceAtLocation(piece.row, piece.col, None)
        if piece.color == Color.WHITE:
            self.white.remove(piece)
        else:
            self.black.remove(piece)

    def pieceRestore(self, piece):
        if piece in self.white or piece in self.black:
            raise Exception("Tried to restore active piece.")
        
        self.setPieceAtLocation(piece.row, piece.col, piece)
        if piece.color == Color.WHITE:
            self.white.append(piece)
        else:
            self.black.append(piece)

    def transport(self, piece, newRow, newCol):
        self.setPieceAtLocation(piece.row, piece.col, None)
        self.setPieceAtLocation(newRow, newCol, piece)
        piece.row = newRow
        piece.col = newCol
            
    # check detection 
    # rule 1: if you are in check, you must get out of check
    # rule 2: you cannot make a move that puts you or leaves you in check (same thing)
    # how to validate a move without making it??? -- my current approach: you do make it. you just reverse it...
    # reverse move <-- two separate versions of this? reversing move(s) that actually happen vs. validating moves with one reversal if fail

    # checkmate detection(?)
    # checkmate is when no matter what move you make, your king will get gobbled up nom nom
    # checkmate also occurs when you cannot make any valid moves while being in check <-- stop counting as soon as there's 1 valid move
    # stalemate occurs when you cannot make any valid moves while NOT in check <-- stop counting as soon as there's 1 valid move
    # can count number of moves SMARTLY for each piece

    # each time a piece is moved, they need to call checkDetect AFTER THE MOVE for validity for themselves and also enemy king
    # if causing self check, invalidate the move... by reversing it?
    # if causing enemy king check, then set enemy king check status to true

    # IMMEDIATE TODOS
    # implement reverse_move 
    # get rid of last_move
    # then maybe finally i will be ready for check detection and validating moves so that they don't do check



