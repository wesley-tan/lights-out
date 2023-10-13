# Lights Out! I adapted this from http://inventwithpython.com/extra/lightsout.py, albeit with a few additional features as well as changing it to meet the requirements.
# This enables one to play the Lights Out game on a 2D board. There will be other files fulfilling the bonus criteria.
# 3 states, *, o and 0

import random # for the randint() function
import string # for the ascii_uppercase string
import math # for the sqrt() function
import sys # for the exit() function

def enterBoardSize():
    # Lets player type in board size.
    # Returns a two-item list of ints: [width, height]
    print('What board size do you want to play? Enter size as WIDTHxHEIGHT.')
    print('For example, type 3x3 or 5x7. Min is 3x3, max is 10x10.')
    while True:
        size = input()
        size = size.split('x')
        if len(size) == 2 and isValidSize(size[0]) and isValidSize(size[1]):
            return [int(size[0]), int(size[1])]
        print('Enter size as WIDTHxHEIGHT. Min size is 3, max size is 10.')


def isValidSize(n):
    # Returns True if n is a number and between 1 and 10. Otherwise returns False.
    return n.isdigit() and int(n) >= 1 and int(n) <= 10

def enterDifficulty(): # difficulty, this function dictates how many random moves are done in setting up the board
    while True:
        print('Enter the difficulty: (1-9)')
        diff = input()
        if diff.isdigit() and int(diff) >= 1 and int(diff) <= 9:
            return int(diff)

def getWidthHeight(board):
    return [len(board), len(board[0])]

def drawBoard(board):
    width, height = getWidthHeight(board)
    print('  ' + ' '.join(string.ascii_uppercase[:width]))
    # print('+' + ('-+' * (width)))
    for y in range(height):
        print(string.ascii_uppercase[y] + ' ' + ' '.join(getRow(board, y)) + ' ')
        # print('+' + ('-+' * (width)))

def getBoardSymbol(boardValue): # let the three symbols be *,o,0
    if boardValue == "0":
        return '*'
    elif boardValue == "1":
        return 'o'
    elif boardValue == "2":
        return '0'

def getRow(board, row):
    # Returns a list of the board spaces for the row number given.
    width, height = getWidthHeight(board)
    boardRow = []
    row = int(row)
    for i in range(width):
        boardRow.append(getBoardSymbol(board[i][row]))
    return boardRow

def getNewBoard(width, height):
    # Creates a brand new, blank board data structure.
    board = []
    for i in range(width):
        board.append([])
        for j in range(height):
            board[i].append("0") # start off all off
    return board

def getBoardCopy(board):
    width, height = getWidthHeight(board)
    dupeBoard = getNewBoard(width, height)
    for x in range(width):
        for y in range(height):
            dupeBoard[x][y] = board[x][y]
    return dupeBoard

def randomMoves(board, numMoves): # the difficulty simply dictates how many RandomMoves are done on the pre-set board
    width, height = getWidthHeight(board)
    for i in range(random.randint(1,width*height-1)):
        makeMove(board, random.randint(0, width-1), random.randint(0, height-1)) # randomize board by making random moves

def letterToIndex(letter):
    return string.ascii_uppercase.find(letter)

def isOnBoard(board, x, y):
    width, height = getWidthHeight(board)
    return x >= 0 and x < width and y >= 0 and y < height

def makeMove(board, x, y):
    if isOnBoard(board, x, y): # flip space
        if board[x][y] == "0":
            board[x][y] = "1"
        elif board[x][y] == "1":
            board[x][y] = "2"
        elif board[x][y] == "2":
            board[x][y] = "0"
    if isOnBoard(board, x, y-1): # flip space above
        if board[x][y-1] == "0":
            board[x][y-1] = "1"
        elif board[x][y-1] == "1":
            board[x][y-1] = "2"
        elif board[x][y-1] == "2":
            board[x][y-1] = "0"
    if isOnBoard(board, x, y+1): # flip space below
        if board[x][y+1] == "0":
            board[x][y+1] = "1"
        elif board[x][y+1] == "1":
            board[x][y+1] = "2"
        elif board[x][y+1] == "2":
            board[x][y+1] = "0"
    if isOnBoard(board, x-1, y): # flip space to the left
        if board[x-1][y] == "0":
            board[x-1][y] = "1"
        elif board[x-1][y] == "1":
            board[x-1][y] = "2"
        elif board[x-1][y] == "2":
            board[x-1][y] = "0"
    if isOnBoard(board, x+1, y): # flip space to the right
        if board[x+1][y] == "0":
            board[x+1][y] = "1"
        elif board[x+1][y] == "1":
            board[x+1][y] = "2"
        elif board[x+1][y] == "2":
            board[x+1][y] = "0"

def enterMove(board):
    width, height = getWidthHeight(board)
    while True:
        print('Enter (A-%s)(A-%s). The first letter is the COLUMN, the second being the ROW (so AB would be column 1 row 2). Alternatively, key in quit, reset, or new:' % (string.ascii_uppercase[width-1], string.ascii_uppercase[height-1]))
        move = input().upper() # regardless of whether player types in capital or lowercase
        if move == 'QUIT' or move == 'RESET' or move == 'NEW':
            return move
        elif len(move) == 2 and move.isalpha() and isOnBoard(board, letterToIndex(move[0]), letterToIndex(move[1])):
            return [letterToIndex(move[0]), letterToIndex(move[1])]

def playAgain():
    print('Do you want to reset this board, play a new game, or quit? (new/reset/quit)')
    while True:
        action = input().lower()
        if action.startswith('r'):
            return 'reset'
        elif action.startswith('n'):
            return 'new'
        elif action.startswith('q'):
            return 'quit'

        print('Please type in new, reset, or quit.')
                
def isBoardOff(board):
    width, height = getWidthHeight(board)
    for x in range(width):
        for y in range(height):
            if board[x][y] != "0":
                return False
    return True

# def aiSolver(width,height):
#     while True:
#         drawBoard(theBoard)
#         if isBoardOff(theBoard):
#             # Player has won the game
#             print()
#             print('*' * 50)
#             print('Good job! You solved the puzzle in %s moves.' % (movesTaken))
#             print('This puzzle can be solved in at least %s moves.' % (fewestMoves))
#             print('*' * 50)
#             print()
#             action = playAgain()
#             if action == 'reset':
#                 movesTaken = 0
#                 theBoard = getBoardCopy(originalBoard)
#                 continue
#             elif action == 'new':
#                 break
#             else: # default of quit
#                 print('Thanks for playing!')
#                 sys.exit()
#         print('Turns taken: %s (Goal: %s)' % (movesTaken, fewestMoves))
#         move = random.choice(string.ascii_uppercase[width-1]) + random.choice(string.ascii_uppercase[height-1])
#         movesTaken += 1
#         if move == 'RESET':
#             movesTaken = 0
#             theBoard = getBoardCopy(originalBoard)
#         elif move == 'QUIT':
#             print('Thanks for playing!')
#             sys.exit()
#         elif move == 'NEW':
#             break
#         else:
#             makeMove(theBoard, move[0], move[1])
    
def showInstructions():
    print('''Instructions:
The Lights Out board is a made up of on (O) and off (.) lights.
Pushing down a light will reverse its state, and also the states of
the lights above, below, and to the left and right of it. (On lights
will turn off, off lights will turn on.)
The goal of the game is to turn off all the lights on the board in
as few moves as possible.

To enter a move, type the letter of the column followed by the letter
of the row you wish to push.
You can also type quit to exit the game, or type reset to start the
current puzzle over.
You can also type new to start a new game.''')
    print()


print('Welcome to Lights Out!')
print('Do you want instructions? (yes/no)')
if input().lower().startswith('y'):
    showInstructions()

while True:
    width, height = enterBoardSize()
    diff = enterDifficulty()

    theBoard = getNewBoard(width, height)
    print(theBoard)
    # Make several random moves on the board depending on board size and difficulty.
    # round() returns a float, so call int() to cut off the trailing .0
    fewestMoves = diff * int(round(math.sqrt(width * height)))
    randomMoves(theBoard, fewestMoves)
    print('You should be able to solve this in at least %s moves.' % (fewestMoves))

    originalBoard = getBoardCopy(theBoard) # for when the player wants to reset the board
    movesTaken = 0

    # print("Do you want an AI companion to play for you?")
    # if input().lower().startswith('y'):
    #     aiSolver(width,height)
    # else:
    while True:
        drawBoard(theBoard)
        if isBoardOff(theBoard):
            # Player has won the game
            print()
            print('*' * 50)
            print('Good job! You solved the puzzle in %s moves.' % (movesTaken))
            print('This puzzle can be solved in at least %s moves.' % (fewestMoves))
            print('*' * 50)
            print()
            action = playAgain()
            if action == 'reset':
                movesTaken = 0
                theBoard = getBoardCopy(originalBoard)
                continue
            elif action == 'new':
                break
            else: # default of quit
                print('Thanks for playing!')
                sys.exit()

        print('Turns taken: %s' % (movesTaken))

        move = enterMove(theBoard)
        movesTaken += 1
        if move == 'RESET':
            movesTaken = 0
            theBoard = getBoardCopy(originalBoard)
        elif move == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif move == 'NEW':
            break
        else:
            makeMove(theBoard, move[0], move[1])