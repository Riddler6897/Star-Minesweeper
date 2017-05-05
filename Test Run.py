from Tkinter import * #We could also use pygame#
from time import time #To set a timer#
from time import sleep #To make the RGBs turn on and off#
#import RPi.GPIO as GPIO 

class Minesweeper(Frame):

    def __init__(self, master):

        self.images = [PhotoImage(file = "images/plaintile.gif"),
                       PhotoImage(file = "images/clickedtile.gif"),
                       PhotoImage(file = "images/minetile.gif"),
                       PhotoImage(file = "images/flagtile.gif")]
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

        self.button = []

        self.constellation = []

        self.Canus = [42, 182]

        self.level = 0


    def buttonPressed(self, i):
        self.button[i].config(image = self.images[1])

    def minePressed(self, i):
        self.button[i].config(image=self.images[2])

    def constellation_plot(self):
        if self.level==0:
            for i in self.Canus:
                self.button[i].config(command = lambda i=i: self.minePressed(i))

       
    def grid(self): #This will make the grid#
        i = 0
        for r in range(15):
            for c in range(15):
                self.mGrid = Button(self.master, image=self.images[0], command = lambda i=i :self.buttonPressed((i)))
                self.button.append(self.mGrid)
                self.mGrid.image = self.images[0]
                self.mGrid.grid(row=r, column=c)
                i += 1

        self.constellation_plot()

       
    def play(): #Will actually run the game#
        pass
        
    def lose(): #Will use GPIO for RGBs and allow the player to start the same level over#
        pass
        
    def score(): #How many non-mine tiles are left to uncover. Could also use GUI to display score for completed levels#
        pass
        
    def plot(): #Plots desired constellations#
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
