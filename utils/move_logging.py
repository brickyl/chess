def log_move(piece, startRow, startCol, status, special, move_list):
    move_log_entry = (piece, startRow, startCol, status, special)
    move_list.append(move_log_entry)
