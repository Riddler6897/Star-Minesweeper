from Tkinter import * #We could also use pygame#
from time import time #To set a timer#
from time import sleep #To make the RGBs turn on and off#
#import RPi.GPIO as GPIO 

class Minesweeper(Frame):

    def __init__(self, master):

        self.PlainTile = PhotoImage(file = "images/plaintile.gif")
        self.ClickedTile = PhotoImage(file = "images/clickedtile.gif")
        self.MineTile = PhotoImage(file = "images/minetile.gif")
        self.FlagTile = PhotoImage(file = "images/flagtile.gif")
        self.NoTile = []
        Frame.__init__(self, master)
        self.master = master
        
        for x in range (1,9):
            self.NoTile.append(PhotoImage(file = "images/tile_"+str(x)+".gif"))

        self.label1 = Label(master, text = "Constellation Minesweeper") #Not sure we need this#
        self.label1.grid(row = 0, column = 0, columnspan = 15) #Or this#

        self.flags = 0
        self.correctFlags = 0
        self.clicked = 0
        
    def buttonPressed(self):
        self.mGrid.config(self, image=self.ClickedTile)
        self.mGrid.image = self.ClickedTile
        
    def grid(self): #This will make the grid#
        for r in range(15):
            for c in range(15):
                x = 5
                #Grid = Button(self.master, image=self.PlainTile, command=self.buttonPressed)
                self.mGrid = Button(self.master, image=self.PlainTile, command=self.buttonPressed)
                self.mGrid.image = self.PlainTile
                self.mGrid.grid(row=r, column=c)
        
    def play(): #Will actually run the game#
        pass
        
    def lose(): #Will use GPIO for RGBs and allow the player to start the same level over#
        pass
        
    def score(): #How many non-mine tiles are left to uncover. Could also use GUI to display score for completed levels#
        pass
        
    def plot(): #Plots desired constellations#
        pass
        
    def constellation(): #Which constellation is running#
        pass
        #def play():
        #def plot():
        #def score():
        #def lose():
        
    def image(): #actually shows the images. Could show image of constellation. Could show flag image#
        pass
    
    def time_out(): #timer. When the time goes out, the whole program will stop running while still showing score.#
        pass
        
    def sound(): #To play a sound if they win or lose. Can be put under the lose function#
        pass

window = Tk()
minesweeper = Minesweeper(window)
window.title("Minesweeper")
minesweeper.grid()
window.mainloop()
