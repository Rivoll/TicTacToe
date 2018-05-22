from Annexe import *
from Board import *
import random as rand
import time


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
    time.sleep(.2)
    return board


def first_turn(board, symbol):
    res = ("a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3")
    choice = res[rand.randrange(0, 9)]
    board[int(choice[1]) - 1][ord(choice[0]) - 97] = symbol
    return board


def invicibleplay(board, symbol, e_symbol, nb_turn):
    res = ("a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3")
    act = 0
    meilleur = -100
    best_choices = []
    if nb_turn == 1:
        time.sleep(.2)
        return first_turn(board, symbol)
    while act < 9:
        choice = res[act]
        if isplaceable(choice, board):
            j = ord(choice[0]) - 97
            i = int(choice[1]) - 1
            board[i][j] = symbol
            ret = -(alphabeta(board, e_symbol, nb_turn + 1, -100, 100))
            if ret > meilleur:
                meilleur = ret
                best_choices[:] = []
                best_choices.append(res[act])
            elif ret == meilleur:
                best_choices.append(res[act])
            board[i][j] = " "
        act += 1
    choice = rand.randrange(0, len(best_choices))
    j = ord(best_choices[choice][0]) - 97
    i = int(best_choices[choice][1]) - 1
    board[i][j] = symbol
    time.sleep(0.2)
    return board


def eval(board, symbol, e_symbol, nb_turn):
    if (check_colls(board, e_symbol) + check_diags(board, e_symbol) + check_lines(board, e_symbol)) > 0:
        return -1000 + nb_turn
    elif (check_colls(board, symbol) + check_diags(board, symbol) + check_lines(board, symbol)) > 0:
        return 1000 - nb_turn
    else:
        return 0


def alphabeta(board, symbol, nb_turn, alpha, beta):
    res = ("a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3")
    meilleur = -1000
    if symbol == "X":
        e_symbol = "O"
    else:
        e_symbol = "X"
    if nb_turn == 10 or is_game_won(board) == 1:
        return eval(board, symbol, e_symbol, nb_turn)
    for index in range(9):
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
