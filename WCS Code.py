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

        #self.label1 = Label(master, text = "Constellation Minesweeper") #Not sure we need this#
        #self.label1.grid(row = 0, column = 0, columnspan = 15) #Or this#

        self.flags = 0
        self.correctFlags = 0
        self.clicked = 0

        self.button = []

        self.score = 1 #When the score increases, then the mines will change places#

        #All the buttons#
        b0 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(0))
        b0.grid(row=0, column=0)
        self.button.append(b0)

        b1 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(1))
        b1.grid(row=0, column=1)
        self.button.append(b1)

        b2 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(2))
        b2.grid(row=0, column=2)
        self.button.append(b2)

        b3 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(3))
        b3.grid(row=0, column=3)
        self.button.append(b3)

        b4 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(4))
        b4.grid(row=0, column=4)
        self.button.append(b4)

        b5 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(5))
        b5.grid(row=0, column=5)
        self.button.append(b5)

        b6 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(6))
        b6.grid(row=0, column=6)
        self.button.append(b6)

        b7 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(7))
        b7.grid(row=0, column=7)
        self.button.append(b7)

        b8 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(8))
        b8.grid(row=0, column=8)
        self.button.append(b8)

        b9 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(9))
        b9.grid(row=0, column=9)
        self.button.append(b9)

        b10 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(10))
        b10.grid(row=0, column=10)
        self.button.append(b10)

        b11 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(11))
        b11.grid(row=0, column=11)
        self.button.append(b11)

        b12 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(12))
        b12.grid(row=0, column=12)
        self.button.append(b12)

        b13 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(13))
        b13.grid(row=0, column=13)
        self.button.append(b13)

        b14 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(14))
        b14.grid(row=0, column=14)
        self.button.append(b14)

        b15 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(15))
        b15.grid(row=1, column=0)
        self.button.append(b15)

        b16 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(16))
        b16.grid(row=1, column=1)
        self.button.append(b16)
        
        b17 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(17))
        b17.grid(row=1, column=2)
        self.button.append(b17)

        b18 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(18))
        b18.grid(row=1, column=3)
        self.button.append(b18)

        b19 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(19))
        b19.grid(row=1, column=4)
        self.button.append(b19)

        b20 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(20))
        b20.grid(row=1, column=5)
        self.button.append(b20)

        b21 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(21))
        b21.grid(row=1, column=6)
        self.button.append(b21)

        b22 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(22))
        b22.grid(row=1, column=7)
        self.button.append(b22)

        b23 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(23))
        b23.grid(row=1, column=8)
        self.button.append(b23)

        b24 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(24))
        b24.grid(row=1, column=9)
        self.button.append(b24)

        b25 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(25))
        b25.grid(row=1, column=10)
        self.button.append(b25)

        b26 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(26))
        b26.grid(row=1, column=11)
        self.button.append(b26)

        b27 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(27))
        b27.grid(row=1, column=12)
        self.button.append(b27)

        b28 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(28))
        b28.grid(row=1, column=13)
        self.button.append(b28)

        b29 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(29))
        b29.grid(row=1, column=14)
        self.button.append(b29)

        b30 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(30))
        b30.grid(row=2, column=0)
        self.button.append(b30)

        b31 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(31))
        b31.grid(row=2, column=1)
        self.button.append(b31)

        b32 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(32))
        b32.grid(row=2, column=2)
        self.button.append(b32)

        b33 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(33))
        b33.grid(row=2, column=3)
        self.button.append(b33)

        b34 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(34))
        b34.grid(row=2, column=4)
        self.button.append(b34)

        b35 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(35))
        b35.grid(row=2, column=5)
        self.button.append(b35)

        b36 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(36))
        b36.grid(row=2, column=6)
        self.button.append(b36)

        b37 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(37))
        b37.grid(row=2, column=7)
        self.button.append(b37)

        b38 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(38))
        b38.grid(row=2, column=8)
        self.button.append(b38)

        b39 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(39))
        b39.grid(row=2, column=9)
        self.button.append(b39)

        b40 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(40))
        b40.grid(row=2, column=10)
        self.button.append(b40)

        b41 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(41))
        b41.grid(row=2, column=11)
        self.button.append(b41)

        b42 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(42))
        b42.grid(row=2, column=12)
        self.button.append(b42)

        b43 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(43))
        b43.grid(row=2, column=13)
        self.button.append(b43)

        b44 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(44))
        b44.grid(row=2, column=14)
        self.button.append(b44)

        b45 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(45))
        b45.grid(row=3, column=0)
        self.button.append(b45)

        b46 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(46))
        b46.grid(row=3, column=1)
        self.button.append(b46)

        b47 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(47))
        b47.grid(row=3, column=2)
        self.button.append(b47)

        b48 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(48))
        b48.grid(row=3, column=3)
        self.button.append(b48)

        b49 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(49))
        b49.grid(row=3, column=4)
        self.button.append(b49)

        b50 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(50))
        b50.grid(row=3, column=5)
        self.button.append(b50)

        b51 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(51))
        b51.grid(row=3, column=6)
        self.button.append(b51)

        b52 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(52))
        b52.grid(row=3, column=7)
        self.button.append(b52)

        b53 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(53))
        b53.grid(row=3, column=8)
        self.button.append(b53)

        b54 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(54))
        b54.grid(row=3, column=9)
        self.button.append(b54)

        b55 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(55))
        b55.grid(row=3, column=10)
        self.button.append(b55)

        b56 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(56))
        b56.grid(row=3, column=11)
        self.button.append(b56)

        b57 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(57))
        b57.grid(row=3, column=12)
        self.button.append(b57)

        b58 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(58))
        b58.grid(row=3, column=13)
        self.button.append(b58)

        b59 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(59))
        b59.grid(row=3, column=14)
        self.button.append(b59)

        b60 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(60))
        b60.grid(row=4, column=0)
        self.button.append(b60)

        b61 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(61))
        b61.grid(row=4, column=1)
        self.button.append(b61)

        b62 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(62))
        b62.grid(row=4, column=2)
        self.button.append(b62)

        b63 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(63))
        b63.grid(row=4, column=3)
        self.button.append(b63)

        b64 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(64))
        b64.grid(row=4, column=4)
        self.button.append(b64)

        b65 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(65))
        b65.grid(row=4, column=5)
        self.button.append(b65)

        b66 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(66))
        b66.grid(row=4, column=6)
        self.button.append(b66)

        b67 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(67))
        b67.grid(row=4, column=7)
        self.button.append(b67)

        b68 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(68))
        b68.grid(row=4, column=8)
        self.button.append(b68)

        b69 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(69))
        b69.grid(row=4, column=9)
        self.button.append(b69)

        b70 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(70))
        b70.grid(row=4, column=10)
        self.button.append(b70)

        b71 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(71))
        b71.grid(row=4, column=11)
        self.button.append(b71)

        b72 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(72))
        b72.grid(row=4, column=12)
        self.button.append(b72)

        b73 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(73))
        b73.grid(row=4, column=13)
        self.button.append(b73)

        b74 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(74))
        b74.grid(row=4, column=14)
        self.button.append(b74)

        b75 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(75))
        b75.grid(row=5, column=0)
        self.button.append(b75)

        b76 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(76))
        b76.grid(row=5, column=1)
        self.button.append(b76)

        b77 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(77))
        b77.grid(row=5, column=2)
        self.button.append(b77)

        b78 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(78))
        b78.grid(row=5, column=3)
        self.button.append(b78)

        b79 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(79))
        b79.grid(row=5, column=4)
        self.button.append(b79)

        b80 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(80))
        b80.grid(row=5, column=5)
        self.button.append(b80)

        b81 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(81))
        b81.grid(row=5, column=6)
        self.button.append(b81)

        b82 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(82))
        b82.grid(row=5, column=7)
        self.button.append(b82)

        b83 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(83))
        b83.grid(row=5, column=8)
        self.button.append(b83)

        b84 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(84))
        b84.grid(row=5, column=9)
        self.button.append(b84)

        b85 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(85))
        b85.grid(row=5, column=10)
        self.button.append(b85)

        b86 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(86))
        b86.grid(row=5, column=11)
        self.button.append(b86)

        b87 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(87))
        b87.grid(row=5, column=12)
        self.button.append(b87)

        b88 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(88))
        b88.grid(row=5, column=13)
        self.button.append(b88)

        b89 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(89))
        b89.grid(row=5, column=14)
        self.button.append(b89)

        b90 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(90))
        b90.grid(row=6, column=0)
        self.button.append(b90)

        b91 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(91))
        b91.grid(row=6, column=1)
        self.button.append(b91)

        b92 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(92))
        b92.grid(row=6, column=2)
        self.button.append(b92)

        b93 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(93))
        b93.grid(row=6, column=3)
        self.button.append(b93)

        b94 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(94))
        b94.grid(row=6, column=4)
        self.button.append(b94)

        b95 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(95))
        b95.grid(row=6, column=5)
        self.button.append(b95)

        b96 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(96))
        b96.grid(row=6, column=6)
        self.button.append(b96)

        b97 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(97))
        b97.grid(row=6, column=7)
        self.button.append(b97)

        b98 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(98))
        b98.grid(row=6, column=8)
        self.button.append(b98)

        b99 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(99))
        b99.grid(row=6, column=9)
        self.button.append(b99)

        b100 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(100))
        b100.grid(row=6, column=10)
        self.button.append(b100)

        b101 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(101))
        b101.grid(row=6, column=11)
        self.button.append(b101)

        b102 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(102))
        b102.grid(row=6, column=12)
        self.button.append(b102)

        b103 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(103))
        b103.grid(row=6, column=13)
        self.button.append(b103)

        b104 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(104))
        b104.grid(row=6, column=14)
        self.button.append(b104)

        b105 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(105))
        b105.grid(row=7, column=0)
        self.button.append(b105)

        b106 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(106))
        b106.grid(row=7, column=1)
        self.button.append(b106)

        b107 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(107))
        b107.grid(row=7, column=2)
        self.button.append(b107)

        b108 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(108))
        b108.grid(row=7, column=3)
        self.button.append(b108)

        b109 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(109))
        b109.grid(row=7, column=4)
        self.button.append(b109)

        b110 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(110))
        b110.grid(row=7, column=5)
        self.button.append(b110)

        b111 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(111))
        b111.grid(row=7, column=6)
        self.button.append(b111)

        b112 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(112))
        b112.grid(row=7, column=7)
        self.button.append(b112)

        b113 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(113))
        b113.grid(row=7, column=8)
        self.button.append(b113)

        b114 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(114))
        b114.grid(row=7, column=9)
        self.button.append(b114)

        b115 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(115))
        b115.grid(row=7, column=10)
        self.button.append(b115)

        b116 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(116))
        b116.grid(row=7, column=11)
        self.button.append(b116)

        b117 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(117))
        b117.grid(row=7, column=12)
        self.button.append(b117)

        b118 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(118))
        b118.grid(row=7, column=13)
        self.button.append(b118)

        b119 = Button(self.master, image=self.images[0], command= lambda: self.buttonPressed(119))
        b119.grid(row=7, column=14)
        self.button.append(b119)
        #End of buttons#

        self.Constellation() #Runs the constellation function, which puts the mines in certain locations#
        
    def buttonPressed(self, i): #Each button has this as a command. Will change to a clicked tile#
        self.button[i].config(image = self.images[1])
            
    def minePressed(self, i): #Will change the picture to the mine when a certain button is pressed#
        self.button[i].config(image = self.images[2])

    def Constellation(self): #Will change the command of certain buttons to the minePressed function depending on score#
        if self.score==0:
            self.button[42].config(command= lambda: self.minePressed(42))
            self.button[107].config(command= lambda: self.minePressed(107))
        if self.score==1:
            self.button[1].config(command= lambda: self.minePressed(1))
        
        
    def play(): #Will actually run the game#
        pass
        
    def lose(self): #Will use GPIO for RGBs and allow the player to start the same level over#
        print "You Lose"
        self.master.destroy()
    
    def time_out(): #timer. When the time goes out, the whole program will stop running while still showing score.#
        pass
        
    def sound(): #To play a sound if they win or lose. Can be put under the lose function#
        pass

class Timer(Canvas): #Need to work on making it work with our code#
    def __init__(self):
        self.window= Tk()       
        Canvas.__init__(self, self.window, bg = "white")
        self.pack(fill = BOTH, expand = 1)
        self.window.title("Minesweeper")
        self.time = 1200
        self.after(1, self.tick)
        self.window.mainloop()

        
    def tick(self):
        # It has to rewrie itself everytime so we need to delete
        # the previous number using delete(ALL)
        self.delete(ALL)
        self.time -= 1
        # You can place the time wherever in the canvas
        # (I chose 10,10 for the example)
        self.create_text(200, 10, text=self.time)
        if self.time == 0:
            pass
            # write funciton here to stop game
        else:
            self.after(1000, self.tick)
                      
window = Tk()
minesweeper = Minesweeper(window)
Timer() #Makes it a separate window when it doesn't need to be. Need to fix#
window.title("Minesweeper")
minesweeper.grid()
window.mainloop()
