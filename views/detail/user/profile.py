#!/usr/bin/python
# -*- coding: utf-8 -*-

import Tkinter as tk
import ttk
from utils.methods import Methods
from views.forms.user.register import RegisterForm

class ProfileView(tk.Frame, Methods):
	def __init__(self, root, **kwargs):
		tk.Frame.__init__(self, root)
		self.root = root
		if kwargs.get('session'):
			self.session = kwargs.get('session')
			self.account = self.session.content_session
		self.view()

	def edit(self):
		self.clean(self.root)
		RegisterForm(self.root, session=self.session)
		

	def view(self):
		div = tk.Frame(self.root, height=550, background="grey", relief=tk.RAISED)
		div.pack(expand=True, fill=tk.X)
		div.pack_propagate(0)

		view = tk.Frame(div, width=650, relief=tk.RAISED)
		view.pack(expand=True, fill=tk.Y)
		view.pack_propagate(0)

		tk.Label(view, text=' '.join(['Bienvenido',
			self.account.get('full_name')]),
			font="Helvetica 22 normal").pack(pady=20)
		# ---- button edit ----
		ttk.Button(view, text="Editar", command=self.edit).pack(pady=10)

		# ---- info ----
		left = tk.Frame(view)
		left.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

		info = ["Nombre de Usuario:", "Cedula de Identidad:",
			"Nombre:", "Apellido:", "Permisos:", "Superusuario:"]

		for item in info:
			tk.Label(left, text=item, font="Helvetica 13",
				fg="#474747").pack(anchor=tk.E, padx=2, pady=8)

		# ---- data account ----
		right = tk.Frame(view)
		right.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

		data = [self.account.get('username'), self.account.get('cedula'),
			self.account.get('first_name'), self.account.get('last_name'),
			self.account.get('permission'), self.account.get('is_superuser')]

		for item in data:
			tk.Label(right, text=item, font="Helvetica 13",
				fg="#474747").pack(anchor=tk.W, padx=2, pady=8)