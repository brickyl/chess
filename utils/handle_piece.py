from constants import Color


def pieceRemoval(board, piece):
    # function to remove a piece from a board using row and col
    # need to remove duplicate code from Pawn, Piece, and King(?)
    board.setPieceAtLocation(piece.row, piece.col, None)
    if piece.color == Color.WHITE:
        board.white.remove(piece)
    else:
        board.black.remove(piece)


def transport(board, piece, newRow, newCol):
    board.setPieceAtLocation(piece.row, piece.col, None)
    board.setPieceAtLocation(newRow, newCol, piece)
    piece.row = newRow
    piece.col = newCol

def reverse_move(board, piece, newRow, newCol):
    pass