import os
import time
from enum import Enum
from colorama import Fore, Style


lettersEqs = {
    "A" : 0,
    "B" : 1,
    "C" : 2,
    "D" : 3,
    "E" : 4,
    "F" : 5,
    "G" : 6,
    "H" : 7
}

class pieceState(Enum): #state
    ALIVE = 1
    DEAD = 2

class PieceType(Enum): #types of piece
    PEON = 0
    TORRE = 1
    ALFIL = 2
    CABALLO = 3
    REINA = 4
    REY = 5

class Piece():
    state = pieceState.ALIVE # Alive or dead?
    typeP = PieceType.PEON # type of piece
    position = [0,0]

    def __init__(self, type, pos) -> None:
        self.typeP = type
        self.position = pos

    def changePiece(self, typeToChange):
        if self.typeP == PieceType.PEON:
            self.typeP = typeToChange
        else:
            print("NO ES UN PEON!")

    def Kill(self):
        self.state = pieceState.DEAD




P1 = [Piece(PieceType.PEON, [6,0]),Piece(PieceType.PEON, [6,1]),Piece(PieceType.PEON, [6,2]),Piece(PieceType.PEON, [6,3]),Piece(PieceType.PEON, [6,4]),Piece(PieceType.PEON, [6,5]),Piece(PieceType.PEON, [6,6]),Piece(PieceType.PEON, [6,7]),
      Piece(PieceType.TORRE, [7,0]),Piece(PieceType.CABALLO, [7,1]),Piece(PieceType.ALFIL, [7,2]),Piece(PieceType.REY, [7,3]),Piece(PieceType.REINA, [7,4]),Piece(PieceType.ALFIL, [7,5]),Piece(PieceType.CABALLO, [7,6]),Piece(PieceType.TORRE, [7,7])]

P2 = [Piece(PieceType.PEON, [1,0]),Piece(PieceType.PEON, [1,1]),Piece(PieceType.PEON, [1,2]),Piece(PieceType.PEON, [1,3]),Piece(PieceType.PEON, [1,4]),Piece(PieceType.PEON, [1,5]),Piece(PieceType.PEON, [1,6]),Piece(PieceType.PEON, [1,7]),
      Piece(PieceType.TORRE, [0,0]),Piece(PieceType.CABALLO, [0,1]),Piece(PieceType.ALFIL, [0,2]),Piece(PieceType.REY, [0,3]),Piece(PieceType.REINA, [0,4]),Piece(PieceType.ALFIL, [0,5]),Piece(PieceType.CABALLO, [0,6]),Piece(PieceType.TORRE, [0,7])]

EatenPiecesP1 = []
EatenPiecesP2 = []

PosibleMovements = list()

Player1Turn = True

endTx = ""
i = int(1)

selectedPiece = P1[0]

ColorPlayer1 = Fore.CYAN
ColorPlayer2 = Fore.CYAN
Player1Name = "PLAYER 1"
Player2Name = "PLAYER 2"

def clear():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For macOS and Linux
    else:
        os.system('clear')



def getPiece(typep):
    if typep == PieceType.PEON:
        return "P"
    elif typep == PieceType.TORRE:
        return "T"
    elif typep == PieceType.CABALLO:
        return "C"
    elif typep == PieceType.ALFIL:
        return "A"
    elif typep == PieceType.REY:
        return "R"
    elif typep == PieceType.REINA:
        return "I"

def printPiece(typep, color):
    if color == True:
        fa = ColorPlayer1
    else:
        fa = ColorPlayer2

    print(f"{fa}{getPiece(typep)} {Style.RESET_ALL}", end=endTx)


endNow = True

#select name and stuff
clear()
print("This is a multiplayer chess game, youll play with a friend...")
time.sleep(1)
Player1Name = input("Select who will be player one... and give me their name -->")
if Player1Name == "" or Player1Name.isspace():
    Player1Name = "Player 1"
print(f"Very well {Player1Name}")
time.sleep(1)
Player2Name = input("Now tell me player 2 name -->")
if Player2Name == "" or Player2Name.isspace():
    Player2Name = "Player 2"
print(f"Excellent {Player2Name}")
time.sleep(1)


#select colors
clear()
print(f"Colors available --> {Fore.RED} RED {Fore.CYAN} CYAN {Fore.GREEN} GREEN {Fore.YELLOW} YELLOW {Style.RESET_ALL}")
color = input(Player1Name + "... select your color --> ")
try:
    ColorPlayer1 = Fore.__getattribute__(color)
except:
    print("ERROR! ASSIGNING DEF COLOR")
    ColorPlayer1 = Fore.CYAN

color = input(Player2Name + "... select your color --> ")
try:
    ColorPlayer2 = Fore.__getattribute__(color)
except:
    print("ERROR! ASSIGNING OTHER COLOR")
    if ColorPlayer1 == Fore.GREEN:
        ColorPlayer2 = Fore.CYAN
    else:
        ColorPlayer2 = Fore.GREEN

print("Finishing last touches...")
time.sleep(1)
clear()

#print the interface
while endNow:
    print(f"{ColorPlayer1} {Player1Name}   ", end="")

    for a in EatenPiecesP1:
        print(f"{getPiece(a.typeP)}  ", end="")

    print(f"{ColorPlayer2} {Player2Name}   ", end="")

    for a in EatenPiecesP2:
        print(f"{getPiece(a.typeP)}  ", end="")
    print(f"{Style.RESET_ALL}\n", end="\n")

    for x in range(8):
        for y in range(8):
            if i == 8:
                endTx="\n"
                i = 0
            else:
                endTx=""
            
            i += 1
            got = False
            for piece in P1:
                if x ==piece.position[0] and y ==piece.position[1]:
                    got = True
                    printPiece(piece.typeP, True)
            for piece2 in P2:
                if x ==piece2.position[0] and y ==piece2.position[1]:
                    got = True
                    printPiece(piece2.typeP, False)
            if got == False:
                print("# ", end=endTx)
        
    print(" ", end="\n")
    selectedPiece = Piece(100,100)
    if Player1Turn == True:
        selection = input(f"Select the piece to move {ColorPlayer1}{Player1Name} (ex: A4) {Style.RESET_ALL} -->")
        for a in P1:
            try:
                if a.position == [int(lettersEqs.get(selection[0])), int(selection[1]) - 1]:
                    selectedPiece = a
                    print(selectedPiece.typeP.name)
                    endNow = False
                    break
            except:
                selectedPiece.typeP = 100
        if selectedPiece.typeP == 100:
            print("Repeat your command")
            time.sleep(1)
    else:
        selection = input(f"Select the piece to move {ColorPlayer2}{Player2Name} (ex: A4) {Style.RESET_ALL} -->")
        for a in P2:
            try:
                if a.position == [int(lettersEqs.get(selection[0])), int(selection[1])]:
                    selectedPiece = a
                    print(selectedPiece.typeP.name)
                    endNow = False
                    break
            except:
                selectedPiece.typeP = 100
        if selectedPiece.typeP == 100:
            print("Repeat your command")
            time.sleep(1)