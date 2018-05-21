from Annexe import *
from Board import *
import random as rand

def lowplay(board, symbol):
    res = ("a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3")
    ret = random.randrange(0, 9)
    choice = res[ret]
    while not isplaceable(choice, board):
        ret = random.randrange(0, 9)
        choice = res[ret]
    j = ord(choice[0]) - 97
    i = int(choice[1]) - 1
    board[i][j] = symbol
    return board

def first_turn(board, symbol, nb_turn):
    if nb_turn == 1:
        board[1][1] = symbol
        return board
    elif nb_turn == 2:
        if board[1][1] == " ":
            board[1][1] = symbol
        else:
            res = ("a1", "c1", "a3", "c3")
            choice = res[rand.randrange(0, 4)]
            j = ord(choice[0]) - 97
            i = int(choice[1]) - 1
            board[i][j] = symbol
    return board


def invicibleplay(board, symbol, e_symbol, nb_turn):
    res = ("a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3")
    act = 0
    meilleur = -1000000000
    if nb_turn == 1 or nb_turn == 2:
        return first_turn(board, symbol, nb_turn)
    while act < 9:
        choice = res[act]
        if isplaceable(choice, board):
            j = ord(choice[0]) - 97
            i = int(choice[1]) - 1
            board[i][j] = symbol
            ret = -(alphabeta(board, e_symbol, nb_turn + 1, -1000000000, 1000000000))
            if ret >= meilleur:
                meilleur = ret
                best_choice = res[act]
            board[i][j] = " "
        act += 1
    j = ord(best_choice[0]) - 97
    i = int(best_choice[1]) - 1
    board[i][j] = symbol
    return board


def eval(board, symbol, e_symbol, nb_turn):
    if (check_colls(board, e_symbol) + check_diags(board, e_symbol) + check_lines(board, e_symbol)) > 0:
        return -10000000000 + nb_turn
    elif (check_colls(board, symbol) + check_diags(board, symbol) + check_lines(board, symbol)) > 0:
        return 10000000000 - nb_turn
    else:
        return 0


def alphabeta(board, symbol, nb_turn, alpha, beta):
    res = ("a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3")
    index = 0
    meilleur = -10000000000
    if symbol == "X":
        e_symbol = "O"
    else:
        e_symbol = "X"
    if nb_turn == 10 or is_game_won(board) == 1:
        return eval(board, symbol, e_symbol, nb_turn)
    while index < 9:
        choice = res[index]
        if isplaceable(choice, board):
            j = ord(choice[0]) - 97
            i = int(choice[1]) - 1
            board[i][j] = symbol
            ret = -alphabeta(board, e_symbol, nb_turn + 1, -beta, -alpha)
            board[i][j] = " "
            if ret > meilleur:
                meilleur = ret
                if meilleur > alpha:
                    alpha = meilleur
                    if alpha >= beta:
                        return meilleur
        index += 1
    return meilleur
