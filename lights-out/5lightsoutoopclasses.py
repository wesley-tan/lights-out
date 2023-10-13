# OOP version

import random

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