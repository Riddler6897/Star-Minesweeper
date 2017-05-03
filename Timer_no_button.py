from Tkinter import *


class Timer(Canvas):
    def __init__(self):
        self.window= Tk()       
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
        # You can place the time wherever in the canvas
        # (I chose 10,10 for the example)
        self.create_text(200, 10, text=self.time)
        if self.time == 0:
            pass
            # write funciton here to stop game
        else:
            self.after(1000, self.tick)
    

Timer()
