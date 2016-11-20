#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

import Tkinter as tk
import tkMessageBox
from utils.methods import Methods
# Forms Import
from forms.viviendo import ViviendoForm
from forms.solicitud import SolicitudForm
from forms.search import SearchForm

class Toolbar(tk.Frame, Methods):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        # BOTTOM div
        self.body = tk.Frame(self.parent, relief=tk.RAISED)
        self.body.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH)
        # TOP Toolbar
        self.tool = self.toolbar()
        # Close window
        self.parent.protocol('WM_DELETE_WINDOW', self.exit)

    def viviendo(self):
        self.clean(self.body)
        self.formViviendo = ViviendoForm(self.body)

    def search(self):
        self.clean(self.body)
        self.formSearch = SearchForm(self.body)

    def exit(self):
        if tkMessageBox.askyesno(title='Advertencia',
            message='¿Seguro(a) que desea salir?'):
            self.quit()

    def toolbar(self):

        toolbar = tk.Frame(self.parent, bd=1, relief=tk.RAISED)

        iconAdd = self.getImage("views/images/add-viviendo.png")
        iconShow = self.getImage("views/images/show-viviendo.png")
        iconExit = self.getImage("views/images/exit.png")

        addButton = tk.Button(toolbar, image=iconAdd, relief=tk.FLAT,
            command=self.viviendo)
        showButton = tk.Button(toolbar, image=iconShow, relief=tk.FLAT,
            command=self.search)
        exitButton = tk.Button(toolbar, image=iconExit, relief=tk.FLAT,
            command=self.exit)

        addButton.image = iconAdd
        addButton.pack(side=tk.LEFT, padx=2, pady=2)

        showButton.image = iconShow
        showButton.pack(side=tk.LEFT, padx=2, pady=2)
        
        exitButton.image = iconExit
        exitButton.pack(side=tk.LEFT, padx=2, pady=2)

        toolbar.pack(side=tk.TOP, fill=tk.X)
        self.pack()
