import random
def drawBoard(board):
    print("     |     |     ")
    print("  "+board[1]+"  |  "+board[2]+"  |  "+board[3]+"  ")
    print("     |     |     ")
    print("-----------------")
    print("     |     |     ")
    print("  "+board[4]+"  |  "+board[5]+"  |  "+board[6]+"  ")
    print("     |     |     ")
    print("-----------------")
    print("     |     |     ")
    print("  "+board[7]+"  |  "+board[8]+"  |  "+board[9]+"  ")
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
    die = random.randrange(2)+1
    if die == 1:
        return "player"
    else:
        return "computer"
def playAgain():
    keepPlaying = input("Would you like to play again?(y/n)")
    keepPlaying = keepPlaying.lower()
    if keepPlaying == "y":
        print("Cool!")
        return "y"
    elif keepPlaying == "n":
        print("Darn, well thanks for playing.")
        return "n"
    else:
        print("You can only answer with an 'y' or an 'n'")
def doMove(board, pLetter, move):
    board[move]=pLetter
def won(board, pLetter):
    return ((board[1]==pLetter and board[2]==pLetter and board[3]==pLetter) or
            (board[4]==pLetter and board[5]==pLetter and board[6]==pLetter) or
            (board[7]==pLetter and board[8]==pLetter and board[9]==pLetter) or
            (board[1]==pLetter and board[4]==pLetter and board[7]==pLetter) or
            (board[2]==pLetter and board[5]==pLetter and board[8]==pLetter) or
            (board[3]==pLetter and board[6]==pLetter and board[9]==pLetter) or
            (board[1]==pLetter and board[5]==pLetter and board[9]==pLetter) or
            (board[7]==pLetter and board[5]==pLetter and board[3]==pLetter))
def copyBoard(board):
    boardCopy=[]
    for i in board:
        boardCopy.append(i)
    return boardCopy
def isSpaceFree(board, move):
    return board[move]==" "
def playerMove(board):
    move=""
    while move not in "1 2 3 4 5 6 7 8 9".split() or not isSpaceFree(board, int(move)):
        print("\nWhich space would you like to place your ", pLetter, " in?(1-9)\nAnswer:")
        move = input()
    return int(move)
def doRandomMove(board, moveList):
    possibleMoves=[]
    for m in moveList:
        if isSpaceFree(board, m):
            possibleMoves.append(m)
    if len(possibleMoves)!=0:
        return random.choice(possibleMoves)
    else:
        return None
def getCMove(board, cLetter):
    for n in range(1, 10):
        move = n
        copy = copyBoard(board)
        if isSpaceFree(copy, move):
            doMove(copy, cLetter, move)
            if won(copy, cLetter):
                return move
    for m in range(1, 10):
        move = m
        copy = copyBoard(board)
        if isSpaceFree(copy, move):
            doMove(copy, pLetter, move)
            if won(copy, pLetter):
                return move
    move = doRandomMove(board, [1, 3, 5, 7, 9])
    if move != None:
        return move
    return doRandomMove(board, [2, 4, 6, 8])
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
print("\nHere's an example board to give you an idea of how to place your peices.")
print("     |     |     ")
print("  1  |  2  |  3  ")
print("     |     |     ")
print("-----------------")
print("     |     |     ")
print("  4  |  5  |  6  ")
print("     |     |     ")
print("-----------------")
print("     |     |     ")
print("  7  |  8  |  9  ")
print("     |     |     ")
play = True
while play == True:
    playBoard = [" "] * 10
    pLetter, cLetter = playerLetter()
    turn = whoGoesFirst()
    print("\nThe ", turn, " will go first.")
    gameIsPlaying=True
    while gameIsPlaying == True:
        if turn == "player":
            drawBoard(playBoard)
            move = playerMove(playBoard)
            doMove(playBoard, pLetter, move)
            if won(playBoard, pLetter):
                drawBoard(playBoard)
                print("Congrats!!!")
                gameIsPlaying = False
            else:
                if fullBoard(playBoard):
                    drawBoard(playBoard)
                    print("The game is a tie.")
                    gameIsPlaying = False
                    break
                else:
                    turn = "computer"
        elif turn == "computer":
            move = getCMove(playBoard, cLetter)
            doMove(playBoard, cLetter, move)
            if won(playBoard, cLetter):
                drawBoard(playBoard)
                print("The computer won the game.")
                gameIsPlaying = False
            else:
                if fullBoard(playBoard):
                    drawBoard(playBoard)
                    print("It's a tie!")
                    gameIsPlaying = False
                    break
                else:
                    turn = "player"

    if playAgain() == "n":
        play = False
    else:
        play = True

