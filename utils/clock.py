import Tkinter as tk
import ttk
import time

class Clock:
    def __init__(self, root):
        self.time1 = ''
        self.time2 = time.strftime('%I:%M:%S %p')
        self.mFrame = tk.Frame(root)
        self.mFrame.pack()

        self.watch = ttk.Label(self.mFrame, text=self.time2.lower(), style='Hour.TLabel')
        self.watch.pack()
        self.watch.configure(text=self.time2)

        self.changeLabel() #first call it manually

    def changeLabel(self): 
        self.time2 = time.strftime('%I:%M:%S %p')
        self.watch.configure(text=self.time2.lower())
        self.mFrame.after(200, self.changeLabel) #it'll call itself continuously