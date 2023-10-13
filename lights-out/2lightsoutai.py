# Lights Out! I adapted this from http://inventwithpython.com/extra/lightsout.py, albeit with a few additional features as well as changing it to meet the requirements.
# This enables one to play the Lights Out game on a 2D board. There will be other files fulfilling the bonus criteria.
# AI mode

import random # for the randint() function
import string # for the ascii_uppercase string
import math # for the sqrt() function
import sys # for the exit() function

def enterBoardSize():
    # Lets player type in board size.
    # Returns a two-item list of ints: [width, height]
    print('What board size do you want to play? Enter size as WIDTHxHEIGHT.')
    print('For example, min is 1x1 and max is 10x10.')
    while True:
        size = input()
        size = size.split('x')
        if len(size) == 2 and isValidSize(size[0]) and isValidSize(size[1]):
            return [int(size[0]), int(size[1])]
        print('Enter size as WIDTHxHEIGHT. Min size is 3, max size is 10.')

def isValidSize(n):
    # Returns True if n is a number and between 3 and 10. Otherwise returns False.
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
    for y in range(height):
        print(string.ascii_uppercase[y] + ' ' + ' '.join(getRow(board, y)) + ' ')

def getBoardSymbol(boardValue):
    if boardValue:
        return 'O'
    else:
        return '*'

def getRow(board, row):
    # Returns a list of the board spaces for the row number given.
    width, height = getWidthHeight(board) # height isn't used in this function
    boardRow = []
    row = int(row)
    for i in range(width):
        boardRow.append(getBoardSymbol(board[i][row])) # * 3 because each space is 3x3 characters
    return boardRow

def getNewBoard(width, height):
    # Creates a brand new, blank board data structure.
    board = []
    for i in range(width):
        board.append([False] * height) # appends some, should be 0, 1, 2 for some object
    return board

def getBoardCopy(board):
    width, height = getWidthHeight(board)
    dupeBoard = getNewBoard(width, height)
    for x in range(width):
        for y in range(height):
            dupeBoard[x][y] = board[x][y]
    return dupeBoard

answers = list()

def randomMoves(board, numMoves): # the difficulty simply dictates how many RandomMoves are done on the pre-set board
    width, height = getWidthHeight(board)
    for i in range(numMoves):
        randomwidth = random.randint(0, width-1)
        randomheight = random.randint(0, height-1)
        makeMove(board, randomwidth, randomheight) # randomize board by making random moves
        answers.append(str(chr(randomwidth+65))+str(chr(randomheight+65))) # store answers in a list

def letterToIndex(letter):
    return string.ascii_uppercase.find(letter)

def isOnBoard(board, x, y):
    width, height = getWidthHeight(board)
    return x >= 0 and x < width and y >= 0 and y < height

def makeMove(board, x, y):
    if isOnBoard(board, x, y): # flip space
        board[x][y] = not board[x][y]
    if isOnBoard(board, x, y-1): # flip space above
        board[x][y-1] = not board[x][y-1]
    if isOnBoard(board, x, y+1): # flip space below
        board[x][y+1] = not board[x][y+1]
    if isOnBoard(board, x-1, y): # flip space to the left
        board[x-1][y] = not board[x-1][y]
    if isOnBoard(board, x+1, y): # flip space to the right
        board[x+1][y] = not board[x+1][y]

def enterMove(board): # use answers here
    for i in range(len(answers)):
        width, height = getWidthHeight(board)
        while True:
            move = answers[i]
            answers.pop(0)
            print("Computer moves " + str(move))
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
            if board[x][y]:
                return False
    return True

def showInstructions():
    print('''Instructions:
In Lights Out the user is presented with a row of lights, some of which are on and some of which
are off. The goal is to turn all lights off. Each light can be toggled, i.e., if it is off, it turns on, and if it
is on, it turns off. The problem is that when a light is toggled, its neighbors are toggled, too. The basic game will ask the user how many
lights to start with and randomly choose whether each of the lights is on or off. The game will then
repeatedly show the user the lights, ask the user for a light to toggle, toggle the light (and its
neighbor(s)), and repeat. When all the lights are off, YOU WIN! This mode is for the AI mode which solves the board for you!''')
    print()


print('Welcome to Lights Out AI!')
print('Do you want instructions? (yes/no)')
if input().lower().startswith('y'):
    showInstructions()

while True:
    width, height = enterBoardSize()
    diff = enterDifficulty()

    theBoard = getNewBoard(width, height)
    print("The current board is:")
    # Make several random moves on the board depending on board size and difficulty.
    # round() returns a float, so call int() to cut off the trailing .0
    fewestMoves = diff * int(round(math.sqrt(width * height)))
    randomMoves(theBoard, fewestMoves) # so theBoard is simply a few lists together

    originalBoard = getBoardCopy(theBoard) # for when the player wants to reset the board
    movesTaken = 0
    drawBoard(theBoard)
    input("AI is ready! Press enter to proceed.")
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
            print('Computer solved the puzzle in %s moves.' % (movesTaken))
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
        print(input("Go to next move?"))

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