from constants import Move


def log_move(piece, startRow, startCol, status, special, move_list):
    move_log_entry = (piece, startRow, startCol, status, special)
    move_list.append(move_log_entry)


def reverse_move(board, moves):
    if len(moves) == 0:
        return False
    else:
        last_move = moves.pop()
        piece, startRow, startCol, status, special = last_move
        board.transport(piece, startRow, startCol)
        match status:

            case Move.CAPTURE | Move.PAWN_ENPASSANT:
                board.pieceRestore(special)

            case Move.PAWN_PROMOTE:
                potential_captured, old_pawn = special

                board.pieceRemoval(piece)
                board.pieceRestore(old_pawn)
                board.transport(old_pawn, startRow, startCol)
                if potential_captured != None:
                    board.pieceRestore(potential_captured)

            case Move.KINGSIDE_CASTLE | Move.QUEENSIDE_CASTLE:
                rook, oldRow, oldCol = special
                board.transport(rook, oldRow, oldCol)
                piece.hasMoved = False
                rook.hasMoved = False

        return True
