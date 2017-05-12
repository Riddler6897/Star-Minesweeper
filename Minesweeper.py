##########################################################################################################################################
##########################################################################################################################################
# Names: Bradford Doughty, Steven Pirvu, Matthew LaCroix, Kimberly Atienza
# Date: 5/12/17
# Description: Final project for Compututer Science 132 at Louisiana Tech University Spring 2017. A variation of the classic game 
#               Minesweeper with a constellation theme. 
##########################################################################################################################################
##########################################################################################################################################

from Tkinter import * #To import all the Tkinter libraries
from time import time #To set a timer
from time import sleep #To make certain function wait
import RPi.GPIO as GPIO #To make the LEDs light up and turn off
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
import tkMessageBox #To display message boxes

class Minesweeper(Frame):

    def __init__(self, master):

        # This imports the images from the images file for the game 
        self.images = [PhotoImage(file = "images/plaintile.gif"),
                       PhotoImage(file = "images/clickedtile.gif"),
                       PhotoImage(file = "images/minetile.gif")]


        Frame.__init__(self, master)
        self.master = master

        #array that stores all the buttons
        self.button = []

        #array that stores all the pins
        self.gpio = []

        #arrays containing the position of each mine that will make the shape of the constellations
        self.Libra = [23, 63, 102, 124, 154, 161, 197, 209]
        self.Orion = [0, 2, 16, 30, 62, 66, 73, 89, 93, 103, 113, 118, 125, 132, 139, 146, 153, 211, 217]
        self.Phoenix = [22, 44, 45, 78, 85, 121, 148, 169, 203]
        self.Taurus = [3, 30, 35, 64, 67, 83, 95, 99, 113, 129, 146, 163, 178, 204, 223]
        self.CanisMajor = [21, 49, 69, 73, 81, 101, 140, 144, 186, 197, 203, 212]
        self.Draco = [32, 51, 63, 67, 96, 127, 157, 161, 167, 173, 193, 195, 198, 212, 224]
        self.CanesVenatici = [42, 182]
        self.Chameleon = [66, 104, 106, 133, 140]
        self.Crater = [4, 22, 98, 120, 142, 153, 164, 220]
        self.Vulpecula = [2, 51, 61, 83, 114, 145, 178, 209]
        
        #an array containing all the constellations in order of "difficulty"
        self.levels = [self.CanesVenatici, self.Chameleon, self.Libra, self.Crater, self.Vulpecula,
                       self.Phoenix, self.CanisMajor, self.Taurus, self.Draco, self.Orion]

        # variables for the scoring system
        self.level = 0
        self.score = 1
        self.pressed = 223
        self.tiles = 225-len(self.levels[self.level])

        #labels showing the current level and the number of mines in the level        
        self.label1 = Label(master, text = "Mines: "+str(len(self.levels[self.level])))
        self.label1.grid(row = 16, column = 0, columnspan = 5)
        self.label2 = Label(master, text = "Level: "+ str(self.score))
        self.label2.grid(row = 16, column = 5, columnspan = 5)
        self.label3 = Label(master, text = "Tiles Left: "+str(self.pressed))
        self.label3.grid(row = 16, column = 10, columnspan = 5)
        
    #set the GPIO pins     
    def setGPIO(self):
        
        gpio = [4, 17, 27, 22, 5, 6, 13, 19, 26, 21, 20, 16]
        for i in gpio:
            GPIO.setup(i, GPIO.OUT, initial = 1)
        for i in gpio:
            self.gpio.append(i)
        return self.gpio
    
    # Changes the image when you press the tile in the game
    def buttonPressed(self, i):
        self.pressed += 1
        self.tiles -= 1
        self.label3 = Label(self.master, text = "Tiles Left: "+str(self.tiles))
        self.label3.grid(row = 16, column = 10, columnspan = 5)
        self.button[i].config(image = self.images[1], state=DISABLED)
        if self.tiles == 0:
            self.win() #If there are zero tiles left then player goes to the next level

    # Makes you lose if you press a mine 
    def minePressed(self, i):
        self.button[i].config(image=self.images[2])
        self.lose() #Shows a message box and then restarts the level

    # Tells the user whether the block clicked is a mine or not by calling the mine Pressedfunction
    def constellation_plot(self):
        for i in self.levels[self.level]:
            self.button[i].config(command = lambda i=i: self.minePressed(i))

    # Deletes the previous level when one level is finished
    # Credit to user: martineau from Stackoverflow.com
    def grid_forget(self):
        while self.button:
            button = self.button.pop()
            button.destroy()

    # A function to move user to next level once all tiles are found without clicking on a mine
    def win(self):
        if self.level == 9:
            tkMessageBox.showinfo("Winner!", "You won the game!")
        self.grid_forget() #Deletes the previous level
        self.score += 1
        self.level += 1
        GPIO.output(20, 1)
        GPIO.output(self.gpio[self.level-1], 0)
        GPIO.output(16, 0)
        
        
        if self.level > 10:
            window.destroy()
            GPIO.cleanup()

        self.pressed = 0
        self.tiles = 225-len(self.levels[self.level])
        self.label1 = Label(self.master, text = "Mines: "+str(len(self.levels[self.level])))
        self.label1.grid(row = 16, column = 0, columnspan = 5)
        self.label2 = Label(self.master, text = "Level: "+ str(self.score))
        self.label2.grid(row = 16, column = 5, columnspan = 5)
        self.label3 = Label(self.master, text = "Tiles Left: "+str(self.pressed))
        self.label3.grid(row = 16, column = 10, columnspan = 5)
        self.grid() #Remakes the grid
        
        
    # Creates the grid and places the plain tile on each button
    def grid(self): 
        i = 0
        for r in range(15):
            for c in range(15):
                self.mGrid = Button(self.master, image=self.images[0], command = lambda i=i :self.buttonPressed((i)))
                self.button.append(self.mGrid)
                self.mGrid.image = self.images[0]
                self.mGrid.grid(row=r, column=c)
                i += 1
        
        self.constellation_plot() #plots the mines onto the grid based on level
        
       
        
    def lose(self): #Will use GPIO for RGB LEDs and allow the player to start the same level over#
        GPIO.output(20, 0)
        GPIO.output(16, 1)
        tkMessageBox.showinfo("Loser!", "You hit a mine! Press 'OK' to restart the level!" )
        
        sleep(.5)
        
        self.grid_forget() #Deletes the previous grid
        self.score = self.score
        self.level = self.level
        self.pressed = 0
        self.tiles = 225-len(self.levels[self.level])
        self.label1 = Label(self.master, text = "Mines: "+str(len(self.levels[self.level])))
        self.label1.grid(row = 16, column = 0, columnspan = 5)
        self.label2 = Label(self.master, text = "Level: "+ str(self.score))
        self.label2.grid(row = 16, column = 5, columnspan = 5)
        self.label3 = Label(self.master, text = "Tiles Left: "+str(self.pressed))
        self.label3.grid(row = 16, column = 10, columnspan = 5)
        self.grid() #Recreates the grid

#Makes a timer in a separate window
class Timer(Canvas):
    def __init__(self):
        self.window = Tk()       
        Canvas.__init__(self, self.window, bg = "white")
        self.pack(fill = BOTH, expand = 1)
        self.window.title("Timer")
        self.time = 1200
        self.after(1, self.tick)
        self.window.mainloop()

        
    def tick(self):
        # It has to rewrie itself everytime so we need to delete
        # the previous number using delete(ALL)
        self.delete(ALL)
        self.time -= 1
        self.create_text(200, 10, text=self.time)
        #If the time has run out, the game is over and the windows are destroyed
        if self.time == 0:
            tkMessageBox.showinfo("Time's Up!", "You ran out of time!")
            window.destroy()
            self.window.destroy()
            GPIO.cleanup()
            
        else:
            self.after(1000, self.tick)
    

#Actually creates the windows for player to see
window = Tk()
minesweeper = Minesweeper(window)
window.title("Minesweeper")
minesweeper.grid()
minesweeper.setGPIO()
Timer()
window.mainloop()
