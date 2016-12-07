#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *
from views.toolbar import Toolbar

class Main(object):

    def __init__(self, root):
        self.root = root
        self.root.title('Home')
        self.root.minsize(950,620)
        # self.root.maxsize(850,800)
        self.root.geometry("1000x720+300+300")
        tool = Toolbar(self.root)

if __name__ == "__main__":
    root = Tk()
    Main(root)
    root.mainloop()
