# Python pgm for tic toe tack game
# One player is user and other is comp
import random
# the board to play the game. We have 9 boxes
board = {}
currentPlayer = 'x'  # start game with user move
gameOn = False  # decide end or stop of game; intially stopped
count = 0  # keep track of no. of moves


def intializeGame():    # Intialize the game

    global gameOn  # gameOn is now global var
    global board
    board = {boxNo: ' ' for boxNo in range(9)}
    print("\n\n********Let's play the Tic Tack Toe *******\n User move is shown by x and comp. is 0")
    k = 0
    print('The board and move numbers : \n')

    # To show move with numbers
    for i in range(3):  # each row of the board
        for j in range(3):   # each col of the board
            print('|', k, end=' ')
            k += 1  # each box in board
        print('|\n+---+---+---+')  # end inner loop
        # end outer loop

    gameOn = True  # start the game
# end of func


def showBoard():        # Function to print the game board
    k = 0
    for i in range(3):  # each row of the board
        for j in range(3):   # each col of the board
            print('|', board[k], end=' ')
            k += 1  # each box in board
        print('|\n+---+---+---+')  # end inner loop
        # end outer loop
# end function


def comp():  # system making its move
    global count  # state that count is global not local
    digonal = [0, 2, 6, 8]  # just to make comp moves quite smarter
    if not gameOn:
        return

    print('\n\tComputer making its move....')
    if board[4] != ' ' and count < 6:
        currentMove = random.choice(digonal)
        while board[currentMove] != ' ':
            currentMove = random.choice(digonal)
    else:
        currentMove = random.randrange(0, 9)
        # till get unoccupied box i.e correct move
        while board[currentMove] != ' ':
            currentMove = random.randrange(0, 9)

    board[currentMove] = currentPlayer
    count += 1
    showBoard()  # display board with new move

# func ends


def user():

    global count  # state that count is global not local
    currentMove = int(
        input("User(x) it's your turn now\nChoose a move from 1-9:- "))
    while currentMove not in range(1, 10):
        currentMove = int(
            input("Move must be between 1-9:- "))

    currentMove -= 1  # board starts from 0
    if board[currentMove] == ' ':
        board[currentMove] = currentPlayer  # User have made a move succesfully
        count += 1
        showBoard()  # display board with new move

        return True
    else:
        currentMove = print("-----WRONG MOVE-----")
        return False

# func ends


def changePlayer():  # change current player
    global currentPlayer
    if currentPlayer == 'x':
        currentPlayer = '0'
    else:
        currentPlayer = 'x'
# fun ends


def checkWinner():

    for i in [0, 3, 6]:  # row wise winner
        row = board[i] == board[i+1] == board[i+2] != ' '
        if row:
            print(currentPlayer, "wont the game.")
            return True
    for i in range(3):  # col wise winner
        col = board[i] == board[i+3] == board[i+6] != ' '
        if col:
            print(currentPlayer, "wont the game.")
            return True

    diagonal1 = board[0] == board[4] == board[8] != ' '
    diagonal2 = board[2] == board[4] == board[6] != ' '

    if (diagonal1 or diagonal2):
        print(currentPlayer, "won the game.")
        return True

    return False
# fun ends


def isGameEnd():  # check if game ends by win or tie
    global gameOn       # state that gameOn is global not local
    if count >= 5:
        if checkWinner():
            gameOn = False
            return True
    elif count == 9:
        print("*****  Ohh!! You lost ******")
        gameOn = False
        return True
    else:
        return False
# fun ends


def restart():
    global count, currentPlayer, gameOn
    count = 0
    currentPlayer = 'x'
    intializeGame()
    play()
# func ends


def play():  # function to operate game
    intializeGame()  # intialize aspects of game
    print("\n\tLet's start the game ")
    showBoard()  # intiale status of the board
    while gameOn:
        while not user():  # till user makes right move
            pass
        if isGameEnd():  # check if game has not ended
            print('******* Thank you for playing the game *********')
            break
        else:
            changePlayer()  # allow other player to make move
            comp()  # let computer make it's move
            changePlayer()
# fun ends


# main code
play()
newGame = input('Do you want play it again ?(Y/N)')
while (newGame == "y" or newGame == "Y"):
    restart()
    newGame = input('Do you want play it again ?(Y/N)')
# end loop
