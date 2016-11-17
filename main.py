#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *
from views.toolbar import Toolbar

class Main(object):

    def __init__(self, root):
        self.root = root
        self.root.title('Home')
        self.root.minsize(820,500)
        self.root.maxsize(850,800)
        self.root.geometry("830x700+300+300")
        tool = Toolbar(self.root)

if __name__ == "__main__":
    root = Tk()
    Main(root)
    root.mainloop()
