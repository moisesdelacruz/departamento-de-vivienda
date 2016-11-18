#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

from PIL import Image, ImageTk
import Tkinter as tk
import tkMessageBox
# Forms Import
from forms.viviendo import ViviendoForm
from forms.solicitud import SolicitudForm
from forms.grupo_familiar import Grupo_familiarForm
from forms.search import SearchForm

class Toolbar(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.tool = self.toolbar()

    def viviendo(self):
        self.cleanWindow()
        formViviendo = ViviendoForm(self.parent)

    def search(self):
        self.cleanWindow()
        formSearch = SearchForm(self.parent)

    def solicitud(self):
        self.cleanWindow()
        formSolicitud = SolicitudForm(self.parent)

    def grupo_familiar(self):
        self.cleanWindow()
        formGrupo_familiar = Grupo_familiarForm(self.parent)

    def cleanWindow(self):
        for child in self.parent.winfo_children():
            child.destroy()
        self.__init__(self.parent)

    def exit(self):
        if tkMessageBox.askyesno(title='Advertencia', message='¿Seguro(a) que desea salir?'):
            self.quit()
        else:
            print 'no salir'

    def getImage(self, image, sizeY=30, sizeX=30):
        self.img = Image.open(image)
        self.img = self.img.resize((sizeY, sizeX), Image.ANTIALIAS)
        return ImageTk.PhotoImage(self.img)


    def toolbar(self):

        toolbar = tk.Frame(self.parent, bd=1, relief=tk.RAISED)

        iconAdd = self.getImage("views/images/add-viviendo.png")
        iconShow = self.getImage("views/images/show-viviendo.png")
        iconAddHome = self.getImage("views/images/home_add.png")
        iconAddGroup = self.getImage("views/images/add-group.png")
        iconExit = self.getImage("views/images/exit.png")

        addButton = tk.Button(toolbar, image=iconAdd, relief=tk.FLAT,
            command=self.viviendo)
        showButton = tk.Button(toolbar, image=iconShow, relief=tk.FLAT,
            command=self.search)
        addGroupButton = tk.Button(toolbar, image=iconAddGroup, relief=tk.FLAT,
                command=self.grupo_familiar)
        addHomeButton = tk.Button(toolbar, image=iconAddHome, relief=tk.FLAT,
                command=self.solicitud)
        exitButton = tk.Button(toolbar, image=iconExit, relief=tk.FLAT,
            command=self.exit)

        addButton.image = iconAdd
        addButton.pack(side=tk.LEFT, padx=2, pady=2)

        showButton.image = iconShow
        showButton.pack(side=tk.LEFT, padx=2, pady=2)

        addGroupButton.image = iconAddGroup
        addGroupButton.pack(side=tk.LEFT, padx=2, pady=2)

        addHomeButton.image = iconAddHome
        addHomeButton.pack(side=tk.LEFT, padx=2, pady=2)

        exitButton.image = iconExit
        exitButton.pack(side=tk.LEFT, padx=2, pady=2)

        toolbar.pack(side=tk.TOP, fill=tk.X)
        self.pack()
