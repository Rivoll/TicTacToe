from IA_tic_tac_toe import *

DRAW = 2
WIN = 1
CONTINUE = 0

def place(board, symbol):
    choice = None
    res = ("a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3")
    while choice not in res or not isplaceable(choice, board):
        print("ton symbole est: %s" % symbol)
        choice = input("Choisissez la case sur laquelle vous voulez jouer \nDe A a C et de 1 a 3\n").lower()
    j = ord(choice[0]) - 97
    i = int(choice[1]) - 1
    board[i][j] = symbol
    return board


def Turn(Actual_player, Board, symbol, nb_turn):
    print("A ton tour de jouer %s:" % Actual_player.nom)
    if (Actual_player.type == "bot"):
        if Actual_player.nom == "Low, A256W193SD96":
            Board = lowplay(Board, symbol)
        elif Actual_player.nom == "Invicible, B2048Z4872":
            if symbol == "X":
                e_symbol = "O"
            else:
                e_symbol = "X"
            Board = invicibleplay(Board, symbol, e_symbol, nb_turn)
    else:
        Board = place(Board, symbol)
    if nb_turn < 5:
        return 0
    won = is_game_won(Board)
    if won == 0:
        if nb_turn == 9:
            return 2
        else:
            return 0
    if won == 1:
        return 1

def Game(Player1, Player2, Board):
    state = 0
    actual_player = ChooseFirstPLayer(Player1, Player2)
    rand = random.randrange(0, 2)
    nb_turn = 1
    if rand == 0:
        symbol = "X"
    else:
        symbol = "O"
    PrintBoard(Board)
    while True:
        state = Turn(actual_player, Board, symbol, nb_turn)
        if state == DRAW:
            PrintBoard(Board)
            Player1.addDraw()
            Player2.addDraw()
            print("Egalite !\n-------------------------")
            break
        elif state == WIN:
            PrintBoard(Board)
            if actual_player == Player1:
                Player1.addWin()
                Player2.addLose()
                print("Le gagnant est le joueur %s !\n-------------------------" % Player1.nom)
            else:
                Player1.addLose()
                Player2.addWin()
                print("Le gagnant est le joueur %s !\n-------------------------" % Player2.nom)
            break
        if actual_player == Player1:
            actual_player = Player2
        else:
            actual_player = Player1
        if symbol == "X":
            symbol = "O"
        else:
            symbol = "X"
        nb_turn += 1
        PrintBoard(Board)

def get_players(fiche, game_mode):
    if game_mode == "3":
        print("Vous avez choisis un combat entre IA\nVeuillez choisir le niveau de la premiere IA")
        Player1 = get_ia(fiche)
        print("Veuillez Choisir le niveau de la deuxieme IA")
        Player2 = get_ia(fiche)
    elif game_mode == "1":
        player_name = GetName()
        if fiche.get(player_name) is None:
            fiche = add_player(fiche, player_name)
            Player2 = fiche[player_name]
            save(fiche)
        else:
            print("Un plaisir de vous revoir %s" % player_name)
            Player2 = fiche[player_name]
        print("Veuillez choisir le niveau de IA")
        Player1 = get_ia(fiche)
    else:
        print("Vous avez choisis un combat joueur contre joueur\nLe joueur 1")
        player_name = GetName()
        if fiche.get(player_name) is None:
            fiche = add_player(fiche, player_name)
            Player2 = fiche[player_name]
            Player2.describe()
            save(fiche)
        else:
            print("Un plaisir de vous revoir %s" % player_name)
            Player2 = fiche[player_name]
        print("Le joueur 2")
        player_name = GetName()
        if fiche.get(player_name) is None:
            fiche = add_player(fiche, player_name)
            Player1 = fiche[player_name]
            save(fiche)
        else:
            print("Un plaisir de vous revoir %s" % player_name)
            Player1 = fiche[player_name]
    return fiche, Player1, Player2


def main():
    play = 'changer'
    fiche = get_list_players()
    if fiche.get("Low, A256W193SD96") is None:
        fiche["Low, A256W193SD96"] = Player("Low, A256W193SD96", "bot")
    if fiche.get("Invicible, A2048Z4872") is None:
        fiche["Invicible, A2048Z4872"] = Player("Invicible, B2048Z4872", "bot")
    while play == "oui" or play == "changer":
        if play == "changer":
            infos = get_players(fiche, choose_mode_game())
            fiche = infos[0]
            Player1 = infos[1]
            Player2 = infos[2]
        board = CreatBoard()
        Game(Player1, Player2, board)
        print("A l'issu de cette partie voici le stats des joueurs : ")
        Player1.describe()
        Player2.describe()
        print("-------------------------")
        play = restart()
        save(fiche)
    save(fiche)
    print("Game over")


if __name__ == "__main__":
    main()