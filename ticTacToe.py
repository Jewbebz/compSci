import random

def gameBoard(place):
    print("     |     |     ")#row 1
    print("  "+place[1]+"  |  "+place[2]+"  |  "+place[3]+"  ")#row 2
    print("     |     |     ")#row 3
    print("-----------------")#row 4
    print("     |     |     ")#row 5
    print("  "+place[4]+"  |  "+place[5]+"  |  "+place[6]+"  ")#row 6
    print("     |     |     ")#row 7
    print("-----------------")#row 8
    print("     |     |     ")#row 9
    print("  "+place[7]+"  |  "+place[8]+"  |  "+place[9]+"  ")#row 10
    print("     |     |     ")#row 11

def playerLetter():
    pLetter=""
    while pLetter!="X" or pLetter!="O":
        pLetter=input("Would you like to be X's or O's?")
        pLetter=pLetter.upper()
    if pLetter=="X":
        print("\nOK! You are X's and the computer is O's.")
    else:
        print("\nOK! You are O's and the computer is X's.")

def firstMove():
    start=random.randrange(2)+1
    if start==1:
        print("You go first!")
    else:
        print("The computer gets to go first.")

def copyBoard(place):
    replicateBoard=[]
    for i in board:
        replicateBoard.append(i)
    return replicateBoard

def freeSpace(place, turn):
    return place[turn]==""

def playerTurn(place):
    turn=""
    while turn not in "1 2 3 4 5 6 7 8 9".split() or not freeSpace(place, int(turn)):
        turn=input("Where would you like to go?(1-9)")
    return int(turn)
