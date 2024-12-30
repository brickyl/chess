from pieces.piece import Piece
from pieces.queen import Queen
from pieces.knight import Knight
from pieces.bishop import Bishop
from pieces.rook import Rook
from constants import Color, Move


class Pawn(Piece):
    def __init__(self, row, col, color, board):
        super().__init__("P", row, col, color, board)

    def check_move(self, board, row, col, moves):
        pieceAtDestination = board.getPieceAtLocation(row, col)

        if pieceAtDestination != None:
            if pieceAtDestination.color != self.color:
                # checking for capture
                if row - self.row == self.color.value and abs(col - self.col) == 1:
                    if (
                        self.color == Color.WHITE
                        and row == 7
                        or self.color == Color.BLACK
                        and row == 0
                    ):
                        return Move.PAWN_PROMOTE
                    return Move.CAPTURE

        else:
            # checking regular moves
            if row - self.row == self.color.value and col == self.col:
                if (
                    self.color == Color.WHITE
                    and row == 7
                    or self.color == Color.BLACK
                    and row == 0
                ):
                    return Move.PAWN_PROMOTE
                return Move.REGULAR

            elif row - self.row == self.color.value * 2 and col == self.col:
                if (
                    self.color == Color.WHITE
                    and self.row == 1
                    or self.color == Color.BLACK
                    and self.row == 6
                ):
                    return Move.REGULAR

            # checking capture-en passant
            elif row - self.row == self.color.value and abs(col - self.col) == 1 and len(moves) > 0:
                (
                    lastMovePiece,
                    lastMoveStartRow,
                    lastMoveStartCol,
                    _
                ) = moves[-1]
                lastMoveDestRow, lastMoveDestCol = lastMovePiece.row, lastMovePiece.col
                if (
                    type(lastMovePiece) == Pawn
                    and lastMoveDestRow - lastMoveStartRow
                    == 2 * lastMovePiece.color.value
                    and lastMoveStartCol == lastMoveDestCol
                    and lastMoveStartCol == col
                ):
                    return Move.PAWN_ENPASSANT

        return Move.INVALID
    
    def try_move(self, status, board, row, col, moves):
        if status == Move.REGULAR or status == Move.CAPTURE:
            return super().try_move(status, board, row, col, moves)

        elif status == Move.PAWN_PROMOTE:
            oldRow, oldCol = self.row, self.col

            promotionMsg = "[chess] What would you like to promote your pawn into? The options are: Q, N, B, R."
            print(promotionMsg)
            promoPiece = input().upper()

            potential_captured = board.getPieceAtLocation(row, col)
            if potential_captured != None:
                board.pieceRemoval(potential_captured)

            board.transport(self, row, col)
            board.pieceRemoval(self)

            match promoPiece:
                case "Q":
                    promoPiece = Queen(row, col, self.color, board)
                case "N":
                    promoPiece = Knight(row, col, self.color, board)
                case "B":
                    promoPiece = Bishop(row, col, self.color, board)
                case "R":
                    promoPiece = Rook(row, col, self.color, board)
                case _:
                    print("[chess] Bad promotion.")
                    return None
            # this function needs to handle the old pawn and new piece properly
            return (promoPiece, oldRow, oldCol, status, (potential_captured, self))

        elif status == Move.PAWN_ENPASSANT:
            oldRow, oldCol = self.row, self.col
            captured = board.getPieceAtLocation(row - self.color.value, col)
            board.pieceRemoval(captured)
            board.transport(self, row, col)
            return (self, oldRow, oldCol, status, captured)

        else:
            return None
    


        # check if there's a piece there
        # [CAPTURE]
        # if so, what color is it?
        # if enemy piece, check if capture is possible
        # capture is possible if
        # the piece can capture that way
        # there are no other pieces in between (unless knight)
        # check is not revealed
        # en passant is unique
        # if friendly piece, can't move. return false
        # [MOVE]
        # if not, check if move is possible
        # move is possible if
        # piece can get there on a blank board
        # there are no other pieces in between (unless knight)
        # check is not revealed
