from abc import ABCMeta, abstractmethod
from constants import Color, Move
from utils import handle_piece


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
        # self.abbreviation = None
        # self.startPosition = None

    @abstractmethod
    def check_move(self, board, row, col, lastMove):
        # returns enum that represents move status
        # returns Move.INVALID if unsuccessful
        # should also return information about capture or special moves (castle, enpassant, etc)
        pass

    def move(self, board, row, col, lastMove):
        board.reverse_add_pieces = []
        board.reverse_rem_pieces = []
        status = self.check_move(board, row, col, lastMove)

        if status == Move.REGULAR:
            handle_piece.transport(board, self, row, col)

        elif status == Move.CAPTURE:
            captured = board.getPieceAtLocation(row, col)
            handle_piece.pieceRemoval(board, captured)
            handle_piece.transport(board, self, row, col)

        else:
            raise Exception("Invalid move.")

    def __str__(self):
        if self.color == Color.WHITE:
            return self.name
        else:
            return self.name.lower()
