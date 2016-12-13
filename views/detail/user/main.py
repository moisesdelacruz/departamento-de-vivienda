#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import ttk
import Tkinter as tk

from utils.methods import Methods
from views.detail.user.profile import ProfileView
from views.detail.user.users_list import UsersListDetail
from views.forms.user.register import RegisterForm
from views.detail.home import HomeView


class ConfigView(tk.Frame, Methods):
	def __init__(self, root, **kwargs):
		tk.Frame.__init__(self, root)
		self.root = root

		if kwargs.get('session'):
			self.session = kwargs.get('session')

		self._menu = tk.Frame(self.root, width=300, bd=1,
			background="white")
		self._menu.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
		self._menu.pack_propagate(0)

		self._body = ttk.Frame(self.root, width=2000, style='Kim.TFrame')
		self._body.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
		self._body.pack_propagate(0)

		self.menu()


	def menu(self):

		iconConfig = self.getImage("views/images/config.png", 20,20)
		t=ttk.Label(self._menu, text="Configuracion",
			image=iconConfig, style="Text.TLabel",
			padding=10, compound=tk.LEFT)
		t.image = iconConfig
		t.pack(anchor=tk.NW, padx=2, pady=1, fill=tk.BOTH)

		# options------
		btn1=tk.Button(self._menu, text="Mi Perfil",bd=0,
			font=("Microsoft New Tai Lue", "11", "normal"),
			justify=tk.LEFT, command=self.my_profile)
		btn1.pack(anchor=tk.NW, padx=2, pady=1, fill=tk.BOTH)
		btn1.pack_propagate(0)

		btn2=tk.Button(self._menu, text="Lista de Usuarios", bd=0,
			font=("Microsoft New Tai Lue", "11", "normal"),
			justify=tk.LEFT, command=self.user_list)
		btn2.pack(anchor=tk.NW, padx=2, pady=1, fill=tk.BOTH)
		btn2.pack_propagate(0)

		btn3=tk.Button(self._menu, text="Nuevo Usuario", bd=0,
			font=("Microsoft New Tai Lue", "11", "normal"),
			justify=tk.LEFT, command=self.new_user)
		btn3.pack(anchor=tk.NW, padx=2, pady=1, fill=tk.BOTH)
		btn3.pack_propagate(0)

		btn4=tk.Button(self._menu, text="Editar Mi Perfil", bd=0,
			font=("Microsoft New Tai Lue", "11", "normal"),
			justify=tk.LEFT, command=self.edit_user)
		btn4.pack(anchor=tk.NW, padx=2, pady=1, fill=tk.BOTH)
		btn4.pack_propagate(0)

		btn5=tk.Button(self._menu, text="Salir", height=1, bd=0,
			font=("Microsoft New Tai Lue", "11", "normal"),
			justify=tk.LEFT, command=self.exit)
		btn5.pack(anchor=tk.NW, padx=2, pady=1, fill=tk.BOTH)
		btn5.pack_propagate(0)

	def my_profile(self):
		self.clean(self._body)
		ProfileView(self._body, session=self.session)

	def user_list(self):
		self.clean(self._body)
		UsersListDetail(self._body, session=self.session)

	def new_user(self):
		self.clean(self._body)
		RegisterForm(self._body)

	def edit_user(self):
		self.clean(self._body)
		RegisterForm(self._body, session=self.session)

	def exit(self):
		self.clean(self.root)
		HomeView(self.root, session=self.session)