import random
def drawBoard(board):
    print("     |     |     ")
    print("   "+board[1]+"  |   "+board[2]+"  |  "+board[3]+"  ")
    print("     |     |     ")
    print("-----------------")
    print("     |     |     ")
    print("   "+board[4]+"  |  "+board[5]+"   |  "+board[6]+"  ")
    print("     |     |     ")
    print("-----------------")
    print("     |     |     ")
    print("   "+board[7]+"  |   "+board[8]+"  |  "+board[9]+"  ")
    print("     |     |     ")
def inputPlayerLetter():
    letter=""
    while not (letter=="X" or letter=="O"):
        print("Would you like to be X's or O's?(x/o)\nAnswer: ")
        letter=input().upper()
    if letter=="X":
        return["X", "O"]
    else:
        return["O", "X"]
def whoGoesFirst():
    if random.randint(0, 1)==0:
        return "computer"
    else:
        return "player"
def playAgain():
    print("Would you like to play again?(yes/no)")
    return input().lower().startswith("y")
def makeMove(board, letter, move):
    board[move]=letter
def isWinner(board, letter):
    return ((board[1]==letter and board[2]==letter and board[3]==letter) or
            (board[4]==letter and board[5]==letter and board[6]==letter) or
            (board[7]==letter and board[8]==letter and board[9]==letter) or
            (board[1]==letter and board[4]==letter and board[7]==letter) or
            (board[2]==letter and board[5]==letter and board[8]==letter) or
            (board[3]==letter and board[6]==letter and board[9]==letter) or
            (board[1]==letter and board[5]==letter and board[9]==letter) or
            (board[7]==letter and board[5]==letter and board[3]==letter))
def getBoardCopy(board):
    dupeBoard=[]
    for i in board:
        dupeBoard.append(i)
    return dupeBoard
def isSpaceFree(board, move):
    return board[move]==""
def playerMove(board):
    move=""
    while move not in "1 2 3 4 5 6 7 8 9".split() or not isSpaceFree(board, int(move)):
        move=input("Where would you like to go?(1-9)\nAnswer: ")
    return int(move)
def chooseRandomMoveFromList(board, movesList):
    possibleMoves=[]
    for i in movesList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)
    if len(possibleMoves)!=0:
        return random.choice(possibleMoves)
    else:
        return None
def getComputerMove(board, computerLetter):
    if computerLetter=="X":
        playerLetter=="O"
    else:
        playerLetter=="X"
    for i in range(1, 10):
        copy=getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, computerLetter, i)
            if isWinner(copy, computerLetter):
                return i
    for i in range(1, 10):
        copy=getBoardCopy(board)
        if isSpaceFree(copy, i):
            makeMove(copy, playerLetter, i)
            if isWinner(copy, playerLetter):
                return i
    move=chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move!=None:
        return move
    if ifSpaceFree(board, 5):
        return 5
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])
def isBoardFull(board):
    for i in range(1, 10):
        if isSpaceFree(board, i):
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
    theBoard=[""]*10
    playerLetter, computerLetter=inputPlayerLetter()
    turn=whoGoesFirst()
    print("The", turn, "Will go first.")
    gameIsPlaying=True
    while gameIsPlaying==True:
        if turn=="player":
            drawBoard(theBoard)
            move=playerMove(theBoard)
            makeMove(theBoard, playerLetter, move)
            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print("Congrats! You won the game!")
                gameIsPlaying=False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("The game is a tie.")
                    break
                else:
                    turn="computer"
        else:
            move=getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)
            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print("The computer won the game.")
                gameIsPlaying=False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("It's a tie. Bummer")
                    break
                else:
                    turn="player"

        if not playAgain():
            break
