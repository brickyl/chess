from abc import ABCMeta, abstractmethod
from constants import Color, Move
# from utils import handle_piece # this needs to be reassigned to board


class Piece(object, metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, name, row, col, color, board):
        # self.color = None
        self.row = row  # ranks
        self.col = col  # files
        self.name = name
        self.color = color
        if color == Color.WHITE:
            board.white.append(self)
        else:
            board.black.append(self)
        board.board[row][col] = self

    @abstractmethod
    def check_move(self, board, row, col, moves):
        # returns enum that represents move status
        # returns Move.INVALID if unsuccessful
        # should also return information about capture or special moves (castle, enpassant, etc)
        pass

    def move(self, board, row, col, moves):
        # returns piece, oldrow, oldcol, newrow, newcol, status, special pieces to be reinstated
        status = self.check_move(board, row, col, moves)
        if status == Move.INVALID:
            return None

        oldRow, oldCol = self.row, self.col
        if status == Move.REGULAR:
            board.transport(self, row, col)
            return (self, oldRow, oldCol, status, None)

        elif status == Move.CAPTURE:
            captured = board.getPieceAtLocation(row, col)
            board.pieceRemoval(captured)
            board.transport(self, row, col)
            return (self, oldRow, oldCol, status, captured)
            

    def __str__(self):
        if self.color == Color.WHITE:
            return self.name
        else:
            return self.name.lower()
