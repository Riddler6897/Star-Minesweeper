from Tkinter import *

class countTime(Canvas):
    def __init__(self):
        self.window = Tk()
        Canvas.__init__(self, self.window, bg = "white")
        self.pack(fill = BOTH, expand = 1)
        self.window.title("Timer")
        self.window.state('zoomed')
        self.sec = 0
        self.time = Label(self.window, fg = 'red')
        self.time.pack()
        self.button = Button(self.window, fg = 'blue', text = 'Start', command = self.toc)
        self.button.pack()
        self.window.mainloop()

    def toc(self):
        self.sec
        self.sec += 1
        self.time['text'] = self.sec
        self.time.after(1000, self.toc)


countTime()
