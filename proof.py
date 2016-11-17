import Tkinter as tk
import os

from PIL import Image, ImageTk
master = tk.Tk()
master.minsize(300,100)
master.geometry("320x100")
 
def callback():
    print "click!"
 
 
photo=ImageTk.PhotoImage(file="views/images/exit.png")
b = tk.Button(master,image=photo, command=callback, height=50, width=150)
b.place(x = 20, y = 20)
 
master.mainloop()