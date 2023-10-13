

import random 
import string 
import math
import sys # exit()
from functools import partial
from tkinter import Tk, Button

print("*" * 50)
print("Welcome to Lights Out!")
print("There are a few different versions you can play!")
print("*" * 50)

print("1 for basic lights out, 2 for AI mode, 3 for Lights Out 2000(three states), 4 for probability mode, 5 for OOP mode, 6 for visual GUI")

masterinput = input("Enter a number: ")

if masterinput == "1": # normal
    
    def enterBoardSize():
        # Lets player type in board size.
        # Returns a two-item list of ints: [width, height]
        print('What board size do you want to play? Enter size as width x height, or the number of columns followed by number of rows.')
        print('You can do any integer, but 3x3 to 6x6 is recommended.')
        while True:
            size = input()
            size = size.split('x')
            if len(size) == 2 and isValidSize(size[0]) and isValidSize(size[1]):
                return [int(size[0]), int(size[1])]
            print('Enter size as width x height. Your format is incorrect.')


    def isValidSize(n):
        # Returns True if n is a number and between 3 and 10. Otherwise returns False.
        return n.isdigit() and int(n) >= 1 and int(n) <= 10

    def enterDifficulty(): # difficulty, this function dictates how many random moves are done in setting up the board
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
        width, height = enterBoardSize() # form board, prompt user for entry
        diff = enterDifficulty() # difficulty is just equivalent to the no. of random moves the computer makes before player begins
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
elif masterinput == "2": # AI
    # Lights Out! I adapted this from http://inventwithpython.com/extra/lightsout.py, albeit with a few additional features as well as changing it to meet the requirements.
    # This enables one to play the Lights Out game on a 2D board. There will be other files fulfilling the bonus criteria.
    # AI mode

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
            print(input("Go to next move? Press Enter."))

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
elif masterinput == "3": # 3 states

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
        
    def showInstructions():
        print('''Instructions:
    In Lights Out the user is presented with a row of lights, some of which are on and some of which
    are off. The goal is to turn all lights off. Each light can be toggled, i.e., if it is off, it turns on, and if it
    is on, it turns off. The problem is that when a light is toggled, its neighbors are toggled, too. The basic game will ask the user how many
    lights to start with and randomly choose whether each of the lights is on or off. The game will then
    repeatedly show the user the lights, ask the user for a light to toggle, toggle the light (and its
    neighbor(s)), and repeat. When all the lights are off, YOU WIN!''')
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
elif masterinput == "4": # probability
    
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

    def getBoardSymbol(boardValue):
        # Returns 'O' if boardValue is True, otherwise '.'
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
            board.append([False] * height)
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
        for i in range(numMoves):
            makeMove(board, random.randint(0, width-1), random.randint(0, height-1)) # randomize board by making random moves

    def letterToIndex(letter):
        return string.ascii_uppercase.find(letter)

    def isOnBoard(board, x, y):
        width, height = getWidthHeight(board)
        return x >= 0 and x < width and y >= 0 and y < height

    def makeMove(board, x, y):
        if isOnBoard(board, x, y): # flip space
            if random.random() < p: # this generates a number between 0 and 1, if it is less than the p value, the light successfully switches on/off
                board[x][y] = not board[x][y]
        if isOnBoard(board, x, y-1): # flip space above
            if random.random() < p:
                board[x][y-1] = not board[x][y-1]
        if isOnBoard(board, x, y+1): # flip space below
            if random.random() < p:
                board[x][y+1] = not board[x][y+1]
        if isOnBoard(board, x-1, y): # flip space to the left
            if random.random() < p:
                board[x-1][y] = not board[x-1][y]
        if isOnBoard(board, x+1, y): # flip space to the right
            if random.random() < p:
                board[x+1][y] = not board[x+1][y]

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


    print('Welcome to Lights Out!')
    print('Do you want instructions? (yes/no)')
    if input().lower().startswith('y'):
        showInstructions()

    while True:
        width, height = enterBoardSize()
        diff = enterDifficulty()
        p = float(input("Please enter the probabilty r of an action being able to occur (between 0-1): ")) # insert probability value

        theBoard = getNewBoard(width, height)
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
                # Computer has won the game
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
elif masterinput == "5": # OOP/Class
        
    # define the class for a cell in the game grid
    class Cell: # each cell/light, where each is either on or off
        def __init__(self, x, y, on):
            self.x = x
            self.y = y
            self.on = on
            
        def switch(self): # switch by assigning self.on to not self.on
            self.on = not self.on
            
        def __str__(self): # this is to display the cell (O or *)
            return "O" if self.on else "*"
        
    # define the class for the game grid
    class Grid:
        def __init__(self, rows, cols): # if use Grid(), need rows and cols
            self.rows = rows
            self.cols = cols
            self.grid = [[Cell(i, j, False) for j in range(cols)] for i in range(rows)]
            
        def switch(self, x, y):
            self.grid[x][y].switch()
            if x > 0:
                self.grid[x-1][y].switch()
            if x < self.rows - 1: # if the value of x indicated by user is one less than the total no. of rows
                self.grid[x+1][y].switch()
            if y > 0:
                self.grid[x][y-1].switch()
            if y < self.cols - 1:
                self.grid[x][y+1].switch()
                
        def __str__(self): # this is to generate the grid, return s
            s = "" 
            for i in range(self.rows):
                for j in range(self.cols):
                    s += str(self.grid[i][j])
                s += "\n"
            return s

    # define the main game class
    class LightsOutGame:
        def __init__(self):
            # prompt the user for the number of rows and columns
            while True:
                try:
                    row_value = input("Enter the number of rows in the game grid: ")
                    break
                except ValueError:
                    pass
                return row_value
            while True:
                try:
                    col_value = input("Enter the number of columns in the game grid: ")
                    break
                except ValueError:
                    pass
                return row_value
            self.rows = int(row_value)
            self.cols = int(col_value)
            self.grid = Grid(self.rows, self.cols)

            # jumble up the game grid in a random manner
            for i in range(self.rows):
                for j in range(self.cols):
                    if random.random() < 0.5:
                        self.grid.switch(i, j)
            
        def play(self):
            while True:
                print(self.grid)
                input_value = input("Enter the row no. followed by the column no. to switch (e.g. 1 2). Please use the right format. Press 0 to exit: ")
                if input_value == "0":
                    print("Bye bye!")
                    quit
                x, y = map(int, input_value.split()) # map(fun, iter)
                self.grid.switch(x-1, y-1)
                
                # check if all lights are off
                if self.all_lights_off():
                    print("You won!")
                    print(self.grid)
                    break
                
        def all_lights_off(self):
            for i in range(self.rows):
                for j in range(self.cols):
                    if self.grid.grid[i][j].on:
                        return False
            return True
                
    # create a game instance and start playing
    game = LightsOutGame()
    game.play()
elif masterinput == "6": # GUI version
        # GUI implementation

    import random
    from functools import partial
    from tkinter import Tk, Button

    class LightsOutGame:
        def __init__(self):
            # Create the main window and set the title
            self.window = Tk()
            self.window.title("Lights Out")
            
            # Create a grid of buttons
            self.buttons = []
            rows = int(input("Enter the number of rows you want:"))
            columns = int(input("Enter the number of columns you want:"))
            print("Turn all the buttons to O")
            for row in range(rows):
                button_row = []
                for col in range(columns):
                    # Create a new button and add it to the grid
                    # Use the button_clicked method as the command, and pass the row and col arguments to it when it is called
                    button = Button(self.window, width=2, height=2, command=lambda row=row, col=col: self.button_clicked(row, col))
                    button.grid(row=row, column=col)
                    button_row.append(button)
                self.buttons.append(button_row)

            quit_button = Button(self.window, text="Quit", command=self.window.quit) # add a quit button
            quit_button.grid(row=rows, column=0, columnspan=columns)
            
            # Randomize the initial state of the buttons
            self.randomize_buttons()

        def randomize_buttons(self):
            for row in self.buttons:
                for button in row:
                    # Set the button's text to "O" if a random number is less than 0.5, otherwise "X"
                    button.config(text="O" if random.random() < 0.5 else "X")
        
        def invert_button_state(self, row, col):
            # Get the button at the specified row and column
            button = self.buttons[row][col]
            # Invert the button's state (from "X" to "O" or vice versa)
            button.config(text="O" if button.cget("text") == "X" else "X")

        def button_clicked(self, row, column):
            # Invert the state of the clicked button
            self.invert_button_state(row, column)

            # Invert the state of the buttons above, below, left, and right of the clicked button (if they exist)
            if row > 0: # these conditions take into consideration that the button pressed may be the first row, column etc
                self.invert_button_state(row - 1, column)
            if row < len(self.buttons) - 1:
                self.invert_button_state(row + 1, column)
            if column > 0:
                self.invert_button_state(row, column - 1)
            if column < len(self.buttons[row]) - 1:
                self.invert_button_state(row, column + 1)
            
            # Check if the game is won (i.e. all buttons are "O")
            if self.check_win():
                print("Congratulations, you won!")

        def check_win(self): # this is to check if ther user has won
            for row in self.buttons:
                for button in row:
                    if button.cget("text") == "X": # if any "X", False, as the player hasn't won
                        return False
            return True # all "O"s

    game = LightsOutGame()
    game.window.mainloop()
