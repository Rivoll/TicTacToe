import random
import pickle

DRAW = 2
WIN = 1
CONTINUE = 0

class Player:
    def __init__(self, nom= "", type="" ):
        self.nom = nom
        self.score ={"draw" : 0, "win" : 0, "lose" : 0}
        self.type = type
    def describe(self):
        print("{} is a {}\nHe has {} draw(s), {} win(s) and {} lose(s)\n".format(self.nom, self.type, self.score["draw"],
                                                                               self.score["win"], self.score["lose"]))
    def reset(self):
        self.score["draw"] = 0
        self.score["win"] = 0
        self.score["lose"] = 0
        print("Score has been succesfully reset")

    def addDraw(self):
        self.score["draw"] += 1
    def addWin(self):
        self.score["win"] += 1
    def addLose(self):
        self.score["lose"] += 1


def CreatBoard():
    Board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    return Board


def PrintBoard(Board):
    j = 0
    print("   A B C")
    while j < 3:
        print(j + 1, " ", end="")
        i = 0
        while i < 3:
            print(Board[j][i], end="")
            i += 1
            if i != 3:
                print("|", end="")
            else:
                print("")
        j += 1
        if j != 3:
            print("  -------")
    print("")


def GetName():
    name = None
    while type(name) != str:
        name = input("Quel est votre nom ? (Entre 2 et 16 caracteres)\n")
        if type(name) == str:
            if len(name) < 2:
                name = None
                print("Un vrai nom svp")
    return name.capitalize()


def get_list_players():
    try:
        with open("TicTacToe_Data", "rb") as fichier:
            depickler = pickle.Unpickler(fichier)
            try:
                fiche = depickler.load()
            except EOFError:
                fiche = {}
                return fiche
            return fiche
    except FileNotFoundError:
        fiche = {}
        return fiche


def get_ia(fiche):
    answer = None
    res = ("1", "2")
    while answer not in res:
        answer = input("Qu'elle niveau d'IA (1 ou 2) ?")
    if answer == "1":
        return fiche["Low, A256W193SD96"]
    else:
        return fiche["Invicible, A2048Z4872"]


def restart():
  answer = None
  res = ('oui', 'non', "change")
  while answer not in res:
      answer = str(input("Voulez vous rejouer ?\n-\"Oui\" pour rejouer directement\n-\"Non\" pour quitter le jeu\n"
                         "-\"Change\" pour changer de joueur\n").lower())
  return answer


def ChooseFirstPLayer(Player1, Player2):
    print("On va jouer a pile ou face si c'est pile le premier joueur sera {} si c'est face le premier joueur sera {}".format(Player1.nom, Player2.nom))
    check = random.randrange(0, 2)
    if check == 0:
        print("C'est pile le premier joueur est donc %s" % Player1.nom)
        return Player1
    else:
        print("C'est face le premier joueur est donc %s" % Player2.nom)
        return Player2


def isplaceable(choice, board):
    j = ord(choice[0]) - 97
    i = int(choice[1]) - 1
    if board[i][j] == ' ':
        return 1
    return 0


def save(fiche):
    with open("TicTacToe_Data", "wb") as fichier:
        pickler = pickle.Pickler(fichier)
        pickler.dump(fiche)


def choose_mode_game():
    res = ("1", "2", "3")
    answer = None
    while answer not in res:
        answer = input("Choisissez votre mode de jeu:\n-1 Pour humain vs L'IA\n-2 pour Humain vs humain\n"
                       "-3 Pour IA vs IA\n")
    return answer


def add_player(fiche, player_name):
    print("Nouveau n'est ce pas ? :)\nJe vous enregistre Immediatement")
    fiche[player_name] = Player(player_name, "human")
    return fiche