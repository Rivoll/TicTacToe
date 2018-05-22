def count_coll(board, symbol, coll_number):
    count = 0
    for line in board:
        if line[coll_number] == symbol:
            count += 1
        elif line[coll_number] != ' ':
            return 0
    return count


def row(*val):
    nb_row = 0
    for nb in val:
        if nb == 2:
            nb_row += 1
    return nb_row


def nb_2row(board, symbol):
    count = row(count_diag1(board, symbol), count_diag2(board, symbol), count_coll(board, symbol, 0),
                count_coll(board, symbol, 1), count_coll(board, symbol, 2), count_line(board[0], symbol),
                count_line(board[1], symbol), count_line(board[2], symbol))
    return count


def count_diag1(board, symbol):
    i = 0
    j = 0
    count = 0
    while i < 3:
        if board[j][i] == symbol:
            count += 1
        elif board[j][i] != ' ':
            return 0
        i += 1
        j += 1
    return count

def count_diag1(board, symbol):
    count = 0
    for i in range(3):
        if board[i][i] == symbol:
            count += 1
        elif board[i][i] != " ":
            return 0
    return count

def count_diag2(board, symbol):
    i = 2
    j = 0
    count = 0
    while i > -1:
        if board[j][i] == symbol:
            count += 1
        elif board[j][i] != ' ':
            return 0
        i -= 1
        j += 1
    return count


def count_line(line, symbol):
    count = 0
    for case in line:
        if case == symbol:
            count += 1
        elif case != ' ':
            return 0
    return count


def check_lines(board, symbol):
    for line in board:
        if count_line(line, symbol) == 3:
            return 1
    return 0


def check_colls(board, symbol):
    nb_coll = 0
    while nb_coll < 3:
        if count_coll(board, symbol, nb_coll) == 3:
            return 1
        nb_coll += 1
    return 0


def check_diags(board, symbol):
    if count_diag1(board, symbol) == 3 or count_diag2(board, symbol) == 3:
        return 1
    return 0


def is_game_won(board):
    if (check_colls(board, "X") + check_colls(board, "O") + check_diags(board, "X") + check_diags(board, "O") +
        check_lines(board, "X") + check_lines(board, "O")) == 0:
        return 0
    else:
        return 1

