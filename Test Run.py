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
#populates NoTile with images corresponding to the number of mines adjacent to each tile
        for x in range (1,9):
            self.NoTile.append(PhotoImage(file = "images/tile_"+str(x)+".gif"))

        self.button = []
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
        self.levels = [self.CanesVenatici, self.Chameleon, self.Libra, self.Crater, self.Vulpecula, self.Phoenix, self.CanisMajor, self.Taurus, self.Draco, self.Orion]
#an array containing all the constellations in order of "difficulty"
        self.level = 0
        self.score = 0
        self.pressed = 0
        self.tiles = 225-len(self.levels[self.level])
#labels showing the current level and the number of mines in the level        
        self.label1 = Label(master, text = "Mines: "+str(len(self.levels[self.level])))
        self.label1.grid(row = 16, column = 0, columnspan = 5)
        self.label2 = Label(master, text = "Level: "+ str(self.score))
        self.label2.grid(row = 16, column = 5, columnspan = 5)
        self.label3 = Label(master, text = "Tiles Left: "+str(self.pressed))
        self.label3.grid(row = 16, column = 10, columnspan = 5)

    def buttonPressed(self, i):
        self.pressed +=1
        self.tiles -= 1
        self.label3 = Label(self.master, text = "Tiles Left: "+str(self.tiles))
        self.label3.grid(row = 16, column = 10, columnspan = 5)
        self.button[i].config(image = self.images[1], state=DISABLED)
        if self.tiles == 0:
            self.win()

    def minePressed(self, i):
        self.button[i].config(image=self.images[2])

    def constellation_plot(self):
        for i in self.levels[self.level]:
            self.button[i].config(command = lambda i=i: self.minePressed(i))

     def win(self):
        Minesweeper(window).grid()
        self.level += 1
        self.label1 = Label(self.master, text = "Mines: "+str(len(self.levels[self.level])))
        self.label1.grid(row = 16, column = 0, columnspan = 5)
        self.score += 1
        self.label2 = Label(self.master, text = "Level: "+ str(self.score))
        self.label2.grid(row = 16, column = 5, columnspan = 5)
        self.pressed = 0
        self.tiles = 225-len(self.levels[self.level])  
        
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
