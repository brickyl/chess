from constants import mapping


def decodeChessNotation(notation):
    # Feature TBD: Catch bad inputs to let the user try again.
    # try:
    #     col = mapping[notation[0].lower()]
    # except KeyError:
    #     print("Invalid column.")
    # try:
    #     row = int(notation[1])
    # except:
    #     print("Invalid row.")
    col = mapping[notation[0].lower()]
    row = int(notation[1])
    if row < 0 or row > 7 or col < 0 or col > 7:
        raise Exception("Out of bounds")
    # return str(8-row) + " " + str(col)
    return (row, col)


def encodeRowColNotation(row, col):
    notation = list(mapping.keys())[list(mapping.values()).index(col)]  # column
    notation += str(8 - row)  # row
    return notation
