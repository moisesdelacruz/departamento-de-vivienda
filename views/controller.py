#!/usr/bin/python
# -*- coding: utf-8 -*-
import os

import Tkinter as tk
import tkMessageBox
from utils.methods import Methods
# database imports
from database.main import UserModel
# Views Imports
from views.forms.viviendo import ViviendoForm
from views.forms.solicitud import SolicitudForm
from views.forms.search import SearchForm
from views.forms.user.register import RegisterForm
from views.forms.user.login import LoginForm
from views.detail.home import HomeView
from views.detail.user.users_list import UsersListDetail
from views.detail.user.profile import ProfileView
from views.detail.user.main import ConfigView
from views.generic.about import AboutView

class Toolbar(tk.Frame, Methods):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        # instance database
        self.db = UserModel()
        # Init styles
        self.style()
        # BOTTOM div
        self.body = tk.Frame(self.parent)
        self.body.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH)
        # session
        self.content_session = {}
        self.last_login = {}
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

    def formViviendo(self, *args):
        if self.permission():
            self.clean(self.body)
            self.formViviendo = ViviendoForm(self.body, self)

    def formSearch(self, *args):
        if self.session():
            self.clean(self.body)
            self.formSearch = SearchForm(self.body, self)


    def loginFrom(self):
        if not self.content_session:
            self.clean(self.body)
            self.login = LoginForm(self.body, self)


    def home(self):
        if self.content_session:
            self.clean(self.body)
            HomeView(self.body, self)
        self.loginFrom()


    def config(self, **kwargs):
        self.clean(self.body)
        if kwargs.get('view'):
            option = kwargs.get('view')
            self.parent.title(option)
            ConfigView(self.body, self, view=option)
        ConfigView(self.body, self)


    def about(self):
        self.clean(self.body)
        about = AboutView(self.body)


    def set_session(self, account):
        self.content_session = account
        self.last_login = account.get('last_login')
        # TOP Toolbar
        self.menu()
        # self.toolbar()
        self.home()

    def update_session(self):
        user_id = self.content_session.get('user_id')
        query = self.db.retrive(user_id, field='user_id')
        self.content_session = self._format_user(query[0])

    def get_session(self):
        return self.content_session

    def exit(self):
        if tkMessageBox.askyesno(title='Advertencia',
            message='¿Seguro(a) que desea salir?'):
            self.quit()

    def toolbar(self):

        self.tool = tk.Frame(self.parent, bd=1, relief=tk.RAISED)

        iconHome = self.getImage("views/images/homeIcon.png", 90, 30)
        iconAdd = self.getImage("views/images/add-viviendo.png", 90, 30)
        iconAddUser = self.getImage("views/images/add-user.png", 90, 30)
        iconShow = self.getImage("views/images/show-viviendo.png", 90, 30)
        iconListUser = self.getImage("views/images/user-list-icons.png", 90, 30)
        iconProfile = self.getImage("views/images/user-information-icon.png", 90, 30)
        iconExit = self.getImage("views/images/exit.png", 90, 30)

        homeButton = tk.Button(self.tool, image=iconHome,
            relief=tk.FLAT, command=self.home)
        addButton = tk.Button(self.tool, image=iconAdd,
            relief=tk.FLAT, command=self.formViviendo)
        showButton = tk.Button(self.tool, image=iconShow,
            relief=tk.FLAT, command=self.formSearch)
        showProfile = tk.Button(self.tool, image=iconProfile,
            relief=tk.FLAT, command=self.profile)
        addUserButton = tk.Button(self.tool, image=iconAddUser,
            relief=tk.FLAT, command=self.formRegister)
        listUsersButton = tk.Button(self.tool, image=iconListUser,
            relief=tk.FLAT, command=self.users_list)
        exitButton = tk.Button(self.tool, image=iconExit,
            relief=tk.FLAT, command=self.exit)

        # Packs
        homeButton.image = iconHome
        homeButton.pack(side=tk.LEFT, pady=2)

        if self.permission():
            addButton.image = iconAdd
            addButton.pack(side=tk.LEFT, pady=2)

        showButton.image = iconShow
        showButton.pack(side=tk.LEFT, pady=2)

        showProfile.image = iconProfile
        showProfile.pack(side=tk.LEFT, pady=2)

        if self.content_session.get('is_superuser'):
            listUsersButton.image = iconListUser
            listUsersButton.pack(side=tk.LEFT, pady=2)

            addUserButton.image = iconAddUser
            addUserButton.pack(side=tk.LEFT, pady=2)


        exitButton.image = iconExit
        exitButton.pack(side=tk.LEFT, pady=2)

        self.tool.pack(side=tk.TOP, fill=tk.X)
        self.pack()


    def menu(self):
        # ---- teclado ----
        # New Viviendo
        self.parent.bind_all("<Control-n>", self.formViviendo)
        # form search viviendo
        self.parent.bind_all("<Control-b>", self.formSearch)

        # ---- menu ----
        self.menubar = tk.Menu(self.parent)
        # File
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label='Inicio', command=self.home)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Nuevo Viviendo',
            command=self.formViviendo, accelerator="Ctrl+N")
        self.filemenu.add_command(label='Buscar Viviendo',
            command=self.formSearch, accelerator="Ctrl+B")
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Salir', command=self.exit)

        # Edit
        self.editmenu = tk.Menu(self.menubar, tearoff=0)
        self.editmenu.add_command(label='Mi Perfil', command=self.config)
        self.editmenu.add_separator()
        self.editmenu.add_command(label='Nuevo Usuario',
            command=lambda : self.config(view='new_user'))
        self.editmenu.add_command(label='Lista de Usuarios',
            command=lambda : self.config(view='user_list'))
        self.editmenu.add_separator()
        self.editmenu.add_command(label='Configuracion', command=self.config)

        # Help
        self.helpmenu = tk.Menu(self.menubar, tearoff=0)
        self.helpmenu.add_command(label='Acerca de', command=self.about)
        self.helpmenu.add_separator()
        self.helpmenu.add_command(label='Ayuda')

        self.menubar.add_cascade(label="Archivo", menu=self.filemenu)
        self.menubar.add_cascade(label="Editar", menu=self.editmenu)
        self.menubar.add_cascade(label="Ayuda", menu=self.helpmenu)

        self.parent.config(menu=self.menubar)
