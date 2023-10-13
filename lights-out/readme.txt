In Lights Out, the user is presented with a row of lights, some of which are on and some of which 
are off. The goal is to turn all lights off. Each light can be toggled, i.e., if it is off, it turns on, and if it
is on, it turns off. The problem is that when a light is toggled, its neighbors are toggled, too (lights
at the edge have only one neighbor that is toggled). The basic game will ask the user how many
lights to start with and randomly choose whether each of the lights is on or off. The game will then
repeatedly show the user the lights, ask the user for a light to toggle, toggle the light (and its
neighbor(s)), and repeat. The game should detect automatically when all the lights are off and
declare the player a winner.

In the lights_out.py file, this serves as a master file for all the versions.

There are 6 versions I have implemented, as follows:
    1. The "normal" 2D version, which enables you to enter in desired number of row and columns, followed by the basic functionality of the Lights Out game
    2. The AI version, whereby the computer solves the puzzle from a randomly generated board for you.
    3. The "three states" version, whereby the lights have three states, */o/0, which can be toggled in a similar way as the typical version
    4. The "probability" version, whereby the user can stipulate how reliable the lights/cells are.
    5. The OOP/class version, which has a very similar to the basic version, but coded in an OOP-style
    6. The GUI version using tkinter. Indicate the no. of rows and columns in the terminal for the game to start, turn everything to "O"
    
Note: for 1-4, the way the computer randomizes the cells is by making moves prior to allowing the user to make moves
What this means is that every board is valid. This also enables the computer to record down the correct answer to the game; this will be helpful in the AI version in (2)
For 5-6, the buttons are completely random (in the way that Python is pseudo-random), so there may be invalid board, especially if you do a board like 1x2

I'd first like to put down a list of resources I used/referred to in crafting this:
https://www.cs.cmu.edu/~tcortina/15-105sp09/lab9.html
http://inventwithpython.com/extra/lightsout.py
https://forums.raspberrypi.com/viewtopic.php?t=249806

Since this is the last assignment, I'd like to thank Professor Zimmeck, and the CAs Conrad, Deborah, Pete, Gavin and Elana for all your help in COMP114 as a whole.
I've thoroughly enjoyed this class.