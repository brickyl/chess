from abc import ABCMeta, abstractmethod
from constants import Color, Move
from utils.move_logging import log_move, reverse_move


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

# cursor.sh
    @abstractmethod
    def check_move(self, board, row, col, moves):
        # returns enum that represents move status
        # returns Move.INVALID if unsuccessful
        # should also return information about capture or special moves (castle, enpassant, etc)
        pass

    def try_move(self, status, board, row, col, moves):
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

    def move(self, board, row, col, moves):
        status = self.check_move(board, row, col, moves)

        move_result = self.try_move(status, board, row, col, moves)
        if move_result == None:
            return False

        log_move(*move_result, moves)
        if board.checkDetect() == self.color:
            reverse_move(board, moves)
            print("[chess] Cannot stay in check.")
            return False
        else:
            return True

    def __str__(self):
        if self.color == Color.WHITE:
            return self.name
        else:
            return self.name.lower()
