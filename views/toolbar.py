import os
from PIL import Image, ImageTk
from Tkinter import Tk, Frame, Menu, Label, StringVar, Entry
from Tkinter import Button, LEFT, TOP, X, FLAT, RAISED
from forms.viviendo import FormViviendo

class Toolbar(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.toolbar()

    def viviendo(self):
        form = FormViviendo(self.parent)

    def getImage(self, image, sizeY=30, sizeX=30):
        self.img = Image.open(image)
        self.img = self.img.resize((sizeY, sizeX), Image.ANTIALIAS)
        return ImageTk.PhotoImage(self.img)


    def toolbar(self):

        toolbar = Frame(self.parent, bd=1, relief=RAISED)

        iconAdd = self.getImage("views/images/add-viviendo.png")
        iconShow = self.getImage("views/images/show-viviendo.png")
        iconAddGroup = self.getImage("views/images/add-group.png")
        iconShowGroup = self.getImage("views/images/show-group.png")
        iconExit = self.getImage("views/images/exit.png")

        addButton = Button(toolbar, image=iconAdd, relief=FLAT,
            command=self.viviendo)
        showButton = Button(toolbar, image=iconShow, relief=FLAT,
            command=self.quit)
        addGroupButton = Button(toolbar, image=iconAddGroup, relief=FLAT,
                command=self.quit)
        showGroupButton = Button(toolbar, image=iconShowGroup, relief=FLAT,
                command=self.quit)
        exitButton = Button(toolbar, image=iconExit, relief=FLAT,
            command=self.quit)

        addButton.image = iconAdd
        addButton.pack(side=LEFT, padx=2, pady=2)

        showButton.image = iconShow
        showButton.pack(side=LEFT, padx=2, pady=2)

        addGroupButton.image = iconAddGroup
        addGroupButton.pack(side=LEFT, padx=2, pady=2)

        showGroupButton.image = iconShowGroup
        showGroupButton.pack(side=LEFT, padx=2, pady=2)

        exitButton.image = iconExit
        exitButton.pack(side=LEFT, padx=2, pady=2)

        toolbar.pack(side=TOP, fill=X)
        self.pack()
