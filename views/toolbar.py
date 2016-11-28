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
from forms.user.register import RegisterForm
from forms.user.login import LoginForm

class Toolbar(tk.Frame, Methods):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        # BOTTOM div
        self.body = tk.Frame(self.parent, relief=tk.RAISED)
        self.body.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH)
        # TOP Toolbar
        self.tool = self.toolbar()
        # Login
        self.login()
        # Close window
        self.parent.protocol('WM_DELETE_WINDOW', self.exit)

    def viviendo(self):
        self.clean(self.body)
        self.parent.title('Registar Viviendo')
        self.formViviendo = ViviendoForm(self.body)

    def search(self):
        self.clean(self.body)
        self.parent.title('Buscar Viviendo')
        self.formSearch = SearchForm(self.body)

    def register(self):
        self.clean(self.body)
        self.parent.title('Crear Cuenta')
        self.formRegister = RegisterForm(self.body)

    def login(self):
        self.clean(self.body)
        self.parent.title('Iniciar Sesión')
        self.formLogin = LoginForm(self.body)

    def exit(self):
        if tkMessageBox.askyesno(title='Advertencia',
            message='¿Seguro(a) que desea salir?'):
            self.quit()

    def toolbar(self):

        toolbar = tk.Frame(self.parent, bd=1, relief=tk.RAISED)

        iconHome = self.getImage("views/images/homeIcon.png")
        iconAdd = self.getImage("views/images/add-viviendo.png")
        iconAddUser = self.getImage("views/images/add-user.png")
        iconShow = self.getImage("views/images/show-viviendo.png")
        iconExit = self.getImage("views/images/exit.png")

        homeButton = tk.Button(toolbar, image=iconHome, relief=tk.FLAT,
            command=self.login)
        addButton = tk.Button(toolbar, image=iconAdd, relief=tk.FLAT,
            command=self.viviendo)
        showButton = tk.Button(toolbar, image=iconShow, relief=tk.FLAT,
            command=self.search)
        addUserButton = tk.Button(toolbar, image=iconAddUser, relief=tk.FLAT,
            command=self.register)
        exitButton = tk.Button(toolbar, image=iconExit, relief=tk.FLAT,
            command=self.exit)

        # Packs
        homeButton.image = iconHome
        homeButton.pack(side=tk.LEFT, padx=2, pady=2)

        addButton.image = iconAdd
        addButton.pack(side=tk.LEFT, padx=2, pady=2)

        showButton.image = iconShow
        showButton.pack(side=tk.LEFT, padx=2, pady=2)

        addUserButton.image = iconAddUser
        addUserButton.pack(side=tk.LEFT, padx=2, pady=2)
        
        exitButton.image = iconExit
        exitButton.pack(side=tk.LEFT, padx=2, pady=2)

        toolbar.pack(side=tk.TOP, fill=tk.X)
        self.pack()
