#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *
from views.controller import Toolbar
import platform

class Main(object):

    def __init__(self, root):
        self.root = root
        self.root.title('Home')
        self.root.minsize(950,620)
        if platform.system() == "Windows":
            self.root.iconbitmap("views/images/home.ico")
        # self.root.maxsize(850,800)
        self.root.geometry("1000x720+300+300")
        tool = Toolbar(self.root)


root = Tk()
Main(root)
root.mainloop()
