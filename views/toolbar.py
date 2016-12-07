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
from views.detail.home import HomeView
from views.detail.users_list import UsersListDetail

class Toolbar(tk.Frame, Methods):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        # BOTTOM div
        self.body = tk.Frame(self.parent, relief=tk.RAISED)
        self.body.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH)
        # session
        self.content_session = {}
        # Login
        self.home()
        # Close window
        self.parent.protocol('WM_DELETE_WINDOW', self.exit)

    def session(self):
        if self.content_session:
            return True

    def permission(self):
        if self.session():
            session = self.content_session
            per = session.get('permission')
            if per == 'Lectura y Escritura':
                return True

    def no_session(self):
        tkMessageBox.showwarning(title='Permiso Denegado',
            message='Debes Iniciar Sesión para realizar esta acción')

    def denegate(self):
        tkMessageBox.showwarning(title='Permiso Denegado',
            message='No tienes permisos para realizar esta acción')

    def formViviendo(self):
        self.clean(self.body)
        self.parent.title('Registar Viviendo')
        self.formViviendo = ViviendoForm(self.body, session=self)

    def formSearch(self):
        if self.session():
            self.clean(self.body)
            self.parent.title('Buscar Viviendo')
            self.formSearch = SearchForm(self.body, session=self)

    def formRegister(self):
        if self.content_session.get('is_superuser'):
            self.clean(self.body)
            self.parent.title('Crear Cuenta')
            self.formRegister = RegisterForm(self.body)


    def loginFrom(self):
        if not self.content_session:
            self.clean(self.body)
            self.parent.title('Iniciar Sesión')
            self.login = LoginForm(self.body, self)
            

    def home(self):
        if self.content_session:
            self.clean(self.body)
            HomeView(self.body, self.content_session)
        else:
            self.loginFrom()

    def users_list(self):
        if self.content_session.get('is_superuser'):
            self.clean(self.body)
            self.parent.title('Lista de Usuarios')
            self.users = UsersListDetail(self.body, session=self)

    def set(self, account):
        self.content_session = account
        # TOP Toolbar
        self.toolbar()
        self.home()

    def exit(self):
        if tkMessageBox.askyesno(title='Advertencia',
            message='¿Seguro(a) que desea salir?'):
            self.quit()

    def toolbar(self):

        self.tool = tk.Frame(self.parent, bd=1, relief=tk.RAISED)

        iconHome = self.getImage("views/images/homeIcon.png")
        iconAdd = self.getImage("views/images/add-viviendo.png")
        iconAddUser = self.getImage("views/images/add-user.png")
        iconListUser = self.getImage("views/images/user-list-icons.png")
        iconProfile = self.getImage("views/images/user-information-icon.png")
        iconShow = self.getImage("views/images/show-viviendo.png")
        iconExit = self.getImage("views/images/exit.png")

        homeButton = tk.Button(self.tool, image=iconHome, relief=tk.FLAT,
            command=self.home)
        addButton = tk.Button(self.tool, image=iconAdd, relief=tk.FLAT,
            command=self.formViviendo)
        showButton = tk.Button(self.tool, image=iconShow, relief=tk.FLAT,
            command=self.formSearch)
        showProfile = tk.Button(self.tool, image=iconProfile, relief=tk.FLAT,
            command=self.formSearch)
        addUserButton = tk.Button(self.tool, image=iconAddUser, relief=tk.FLAT,
            command=self.formRegister)
        listUsersButton = tk.Button(self.tool, image=iconListUser, relief=tk.FLAT,
            command=self.users_list)
        exitButton = tk.Button(self.tool, image=iconExit, relief=tk.FLAT,
            command=self.exit)

        # Packs
        homeButton.image = iconHome
        homeButton.pack(side=tk.LEFT, padx=2, pady=2)

        if self.permission():
            addButton.image = iconAdd
            addButton.pack(side=tk.LEFT, padx=2, pady=2)

        showButton.image = iconShow
        showButton.pack(side=tk.LEFT, padx=2, pady=2)

        showProfile.image = iconProfile
        showProfile.pack(side=tk.LEFT, padx=2, pady=2)

        if self.content_session.get('is_superuser'):
            listUsersButton.image = iconListUser
            listUsersButton.pack(side=tk.LEFT, padx=2, pady=2)

            addUserButton.image = iconAddUser
            addUserButton.pack(side=tk.LEFT, padx=2, pady=2)

        
        exitButton.image = iconExit
        exitButton.pack(side=tk.LEFT, padx=2, pady=2)

        self.tool.pack(side=tk.TOP, fill=tk.X)
        self.pack()
