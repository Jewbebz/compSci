import random
def drawBoard(board):
    print("     |     |     ")
    print("  "+board[0]+"  |  "+board[1]+"  |  "+board[2]+"  ")
    print("     |     |     ")
    print("-----------------")
    print("     |     |     ")
    print("  "+board[3]+"  |  "+board[6]+"  |  "+board[5]+"  ")
    print("     |     |     ")
    print("-----------------")
    print("     |     |     ")
    print("  "+board[6]+"  |  "+board[7]+"  |  "+board[8]+"  ")
    print("     |     |     ")

def playerLetter():
    letter=""
    while not (letter=="X" or letter=="O"):
        print("Would you like to be X's or O's?(x/o)\nAnswer: ")
        letter=input().upper()
    if letter=="X":
        return["X", "O"]
    else:
        return["O", "X"]
def whoGoesFirst():
    firstN=random.randrange(1, 2)+1
    if firstN ==1:
        return "computer"
    else:
        return "player"

def playAgain():
    keepPlaying = input("Would you like to play again?(y/n)")
    keepPlaying = keepPlaying.lower()
    if keepPlaying == "y":
        print("Cool!")
        play = "y"
    elif keepPlaying == "n":
        print("Darn, well thanks for playing.")
        play = "n"
    else:
        print("You can only answer with an 'n' or an 'a'")

def move(board, pLetter, move):
    board[move]=pLetter

def won(board, pLetter):
    return ((board[1]==letter and board[2]==letter and board[3]==letter) or
            (board[4]==letter and board[5]==letter and board[6]==letter) or
            (board[7]==letter and board[8]==letter and board[9]==letter) or
            (board[1]==letter and board[4]==letter and board[7]==letter) or
            (board[2]==letter and board[5]==letter and board[8]==letter) or
            (board[3]==letter and board[6]==letter and board[9]==letter) or
            (board[1]==letter and board[5]==letter and board[9]==letter) or
            (board[7]==letter and board[5]==letter and board[3]==letter))

def copyBoard(board):
    boardCopy=[]
    for m in board:
        boardCopy.append(m)
    return boardCopy

def isSpaceFree(board, move):
    return board[move]==" "

def playerMove(board):
    move=""
    while move not in "1 2 3 4 5 6 7 8 9".split() or not isSpaceFree(board, int(move)):
        move = input("Which space would you like to place your ", pLetter, " in?(1-9)\n Answer:")
    return int(move)

def doRandomMove(board, moveList):
    possibleMoves=[]
    for m in moveList:
        if isSpaceFree(board, i):
            possibleMoves.append(m)
    if len(possibleMoves)!=0:
        return random.choice(possibleMoves)
    else:
        return None

def getCMove(board, cLetter):
    for n in range(1, 10):
        copy = boardCopy(board)
        if isSpaceFree(copy, m):
            makeMove(copy, cLetter, m)
            if won(copy, cLetter):
                return m
    for m in range(1, 10):
        copy = boardCopy(board)
        if isSpaceFree(copy, m):
            makeMove(copy, pLetter, m)
            if won(copy, pLetter):
                return m
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
    if ifSpaceFree(board, 5):
        return 5
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])

def fullBoard (board):
    for s in range(1, 10):
        if isSpaceFree(board, s):
            return False
    return True

print ("""\n
`7MMF'     A     `7MF'     `7MM                                           
  `MA     ,MA     ,V         MM                                           
   VM:   ,VVM:   ,V .gP"Ya   MM  ,p6"bo   ,pW"Wq.`7MMpMMMb.pMMMb.  .gP"Ya 
    MM.  M' MM.  M',M'   Yb  MM 6M'  OO  6W'   `Wb MM    MM    MM ,M'   Yb
    `MM A'  `MM A' 8M8M8M8M  MM 8M       8M     M8 MM    MM    MM 8M8M8M8M
     :MM;    :MM;  YM.    ,  MM YM.    , YA.   ,A9 MM    MM    MM YM.    ,
      VF      VF    `Mbmmd'.JMML.YMbmd'   `Ybmd9'.JMML  JMML  JMML.`Mbmmd' """)

while True:
    playBoard = [" "] * 10
    pLetter, cLetter = playerLetter()
    turn = whoGoesFirst()
    print("The ", turn, " will go first.")
    gameIsPlaying=True
    while gameIsPlaying == True:
        if turn == "player":
            drawBoard(playBoard)
            move = playerMove(playBoard)
            makeMove(playBoard, pLetter, move)
            if isWinner(playBoard, pLetter):
                drawBoard(playBoard)
                print("Congrats!!!")
                gameIsPlaying = False
            else:
                if fullBoard(playBoard):
                    drawBoard(playBoard)
                    print("The game is a tie.")
                    break
                else:
                    turn = "computer"
        else:
            move = getCMove(theBoard, cLetter)
            move(playBoard, cLetter, move)
            if won(playBoard, cLetter, move):
                drawBoard(playBoard)
                print("The computer won the game.")
                gameIsPlaying = False
            else:
                if fullBoard(playBoard):
                    drawBoard(playBoard)
                    print("It's a tie!")
                    break
                else:
                    turn = "player"

        if not playAgain():
            break
