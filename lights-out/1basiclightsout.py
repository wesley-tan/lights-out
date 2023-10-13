# Lights Out! I adapted this from http://inventwithpython.com/extra/lightsout.py, albeit with a few additional features as well as changing it to meet the requirements.
# This enables one to play the Lights Out game on a 2D board. There will be other files fulfilling the bonus criteria.
# This is the basic Lights Out game

import random 
import string 
import math
import sys # exit()

def BoardSize(): #enter board size
    print('What board size do you want to play? Enter size as width x height, or the number of columns followed by number of rows.')
    print('You can do any integer, but 3x3 to 6x6 is recommended.')
    while True:
        size = input()
        size = size.split('x')
        if len(size) == 2 and ValidSize(size[0]) and ValidSize(size[1]):
            return [int(size[0]), int(size[1])]
        print('Enter size as width x height. Your format is incorrect.')


def ValidSize(n):
    # Returns True if n is a number and between 3 and 10. Otherwise returns False.
    return n.isdigit() and int(n) >= 1 and int(n) <= 10

def DifficultyEntry(): # difficulty, this function dictates how many random moves are done in setting up the board
    while True:
        print('Enter difficulty: (1-9). This determines how jumbled your board is.')
        diff = input()
        if diff.isdigit() and int(diff) >= 1 and int(diff) <= 9:
            return int(diff)

def getWidthHeight(board):
    return [len(board), len(board[0])]

def drawBoard(board):
    width, height = getWidthHeight(board)
    print('  ' + ' '.join(string.ascii_uppercase[:width]))
    for h in range(height):
        print(string.ascii_uppercase[h] + ' ' + ' '.join(getRow(board, h)) + ' ')

def getBoardSymbol(boardValue):
    # Returns 'O' if boardValue is True, otherwise '*'
    if boardValue:
        return 'O'
    else:
        return '*'

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
        board.append([False] * height) # start with all lights/cells being false
    return board

def getBoardCopy(board): # we want to get a copy of the board
    width, height = getWidthHeight(board)
    dupeBoard = getNewBoard(width, height)
    for x in range(width):
        for y in range(height):
            dupeBoard[x][y] = board[x][y]
    return dupeBoard

def randomMoves(board, numMoves): # the difficulty simply dictates how many RandomMoves are done on the pre-set board
    width, height = getWidthHeight(board)
    for i in range(numMoves):
        makeMove(board, random.randint(0, width-1), random.randint(0, height-1)) # randomize board by making random moves

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

def enterMove(board):
    width, height = getWidthHeight(board)
    while True:
        print('Enter (A-%s)(A-%s). The first letter is the column no., the second is the row no. (so AB would be column 1 row 2). Alternatively, key in quit, reset, or new:' % (string.ascii_uppercase[width-1], string.ascii_uppercase[height-1]))
        move = input().upper() # regardless of whether player types in capital or lowercase
        if move == 'QUIT' or move == 'RESET' or move == 'NEW':
            return move
        elif len(move) == 2 and move.isalpha() and isOnBoard(board, letterToIndex(move[0]), letterToIndex(move[1])):
            return [letterToIndex(move[0]), letterToIndex(move[1])]

def playAgain():
    print('Play new game, reset game or quit? (new/reset/quit)')
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
neighbor(s)), and repeat. When all the lights are off, YOU WIN!''')
    print()

print("%" * 50)
print("LIGHTS OUT!")
print("%" * 50)
print('Do you want instructions? (yes/no)')
if input().lower().startswith('y'):
    showInstructions()

while True:
    width, height = BoardSize() # form board, prompt user for entry
    diff = DifficultyEntry() # difficulty is just equivalent to the no. of random moves the computer makes before player begins
    theBoard = getNewBoard(width, height)
    fewestMoves = diff * int(round(math.sqrt(width * height)))
    randomMoves(theBoard, fewestMoves)
    print('You should be able to solve this in at least %s moves.' % (fewestMoves))

    originalBoard = getBoardCopy(theBoard) # for when the player wants to reset the board
    movesTaken = 0 # start from zero moves, and count up

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
                print('Bye bye!')
                sys.exit()

        print('Turns taken: %s (Goal: %s)' % (movesTaken, fewestMoves))

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