#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import ttk
import Tkinter as tk

from utils.methods import Methods

class ConfigView(tk.Frame, Methods):
	def __init__(self, root, **kwargs):
		tk.Frame.__init__(self, root)
		self.root = root

		if kwargs.get('session'):
			self.session = kwargs.get('session')

		self._menu = tk.Frame(self.root, width=270, bd=1, background="white", relief=tk.RAISED)
		self._menu.pack(side=tk.LEFT, expand=True, fill=tk.Y)
		self._menu.pack_propagate(0)

		self._body = tk.Frame(self.root, width=2000, background="white")
		self._body.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

		self.menu()


	def menu(self):
		# Title--------------
		title=ttk.Frame(self._menu)
		title.pack(anchor=tk.N, expand=True, fill=tk.X)

		iconConfig = self.getImage("views/images/config.png")
		t=ttk.Label(title, text="Configuracion", image=iconConfig,
			style="Black.TLabel", padding=10, compound=tk.LEFT)
		t.image = iconConfig
		t.pack(side=tk.LEFT)

		# options------
		options=ttk.Frame(self._menu)
		options.pack(anchor=tk.N, expand=True, fill=tk.X)

		btn1=tk.Button(options, text="Mi Perfil",
			height=1, width=20, bd=0,
			font=("Microsoft New Tai Lue", "14", "normal"),
			justify=tk.LEFT)
		btn1.pack(anchor=tk.N,
			padx=2, pady=1, fill=tk.X)
		btn1.pack_propagate(0)

		btn2=tk.Button(options, text="Lista de Usuarios",
			height=1, width=20, bd=0,
			font=("Microsoft New Tai Lue", "14", "normal"),
			justify=tk.LEFT)
		btn2.pack(anchor=tk.N,
			padx=2, pady=1, fill=tk.X)
		btn2.pack_propagate(0)

		btn3=tk.Button(options, text="Nuevo Usuario",
			height=1, width=20, bd=0,
			font=("Microsoft New Tai Lue", "14", "normal"),
			justify=tk.LEFT)
		btn3.pack(anchor=tk.N,
			padx=2, pady=1, fill=tk.X)
		btn3.pack_propagate(0)

		btn4=tk.Button(options, text="Editar Mi Perfil",
			height=1, width=20, bd=0,
			font=("Microsoft New Tai Lue", "14", "normal"),
			justify=tk.LEFT)
		btn4.pack(anchor=tk.N,
			padx=2, pady=1, fill=tk.X)
		btn4.pack_propagate(0)

		btn5=tk.Button(options, text="Salir", height=1,
			width=20, bd=0,
			font=("Microsoft New Tai Lue", "14", "normal"),
			justify=tk.LEFT)
		btn5.pack(anchor=tk.N,
			padx=2, pady=1, fill=tk.X)
		btn5.pack_propagate(0)