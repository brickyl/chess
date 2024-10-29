from constants import mapping

def decodeChessNotation(notation):
    col = mapping[notation[0].lower()]
    row = int(notation[1])
    # return str(8-row) + " " + str(col)
    return (row, col)

def encodeRowColNotation(row, col):
    notation = list(mapping.keys())[list(mapping.values()).index(col)] # column
    notation += str(8-row) # row
    return notation


