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
