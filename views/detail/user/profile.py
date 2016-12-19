#!/usr/bin/python
# -*- coding: utf-8 -*-

import Tkinter as tk
import ttk
from utils.methods import Methods
from views.forms.user.register import RegisterForm

class ProfileView(tk.Frame, Methods):
	def __init__(self, root, controller, **kwargs):
		tk.Frame.__init__(self, root)
		self.root = root
		self.controller = controller

		if kwargs.get('user'):
			self.action_edit = 'edit_user'
			self.account = kwargs.get('user')
		else:
			self.action_edit = 'edit_me'
			# account
			self.account = self.controller.get_session()
			# set title of window
			self.controller.parent.title('Mi Perfil')

		# render view
		self.view()

	def edit(self):
		self.clean(self.root)
		RegisterForm(self.root, self.controller,
			action=self.action_edit, data=self.account)


	def view(self):
		div = ttk.Frame(self.root, height=550, style='Kim.TFrame')
		div.pack(expand=True, fill=tk.X)
		div.pack_propagate(0)

		view = ttk.Frame(div, width=650, style='Kim.TFrame')
		view.pack(expand=True, fill=tk.Y)
		view.pack_propagate(0)

		ttk.Label(view, text=' '.join(['Bienvenido',
			self.account.get('full_name')]),
			style="Title.TLabel").pack(pady=20)
		# ---- button edit ----

		# Image
		content_image = ttk.Frame(view, style='Kim.TFrame')
		content_image.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

		img = self.getImage("views/images/user.png", 200, 200)
		image = tk.Label(content_image, image=img, fg="blue", background="#012D5A")
		image.image = img
		image.pack(pady=10)

		if self.controller.is_superuser() or self.action_edit == 'edit_me':
			ttk.Button(content_image, text="Editar",
				command=self.edit).pack(pady=10)

		# ---- info ----
		left = ttk.Frame(view, style='Kim.TFrame')
		left.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)


		info = ["Nombre de Usuario:", "Cedula de Identidad:",
			"Nombre:", "Apellido:", "Permisos:", "Superusuario:"]

		for item in info:
			ttk.Label(left, text=item, style='Text_bold.TLabel'
				).pack(anchor=tk.E, padx=2, pady=8)

		# ---- data account ----
		right = ttk.Frame(view, style='Kim.TFrame')
		right.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

		data = [self.account.get('username'), self.account.get('cedula'),
			self.account.get('first_name'), self.account.get('last_name'),
			self.account.get('permission'), bool(self.account.get('is_superuser'))]

		for item in data:
			ttk.Label(right, text=item, style='Text.TLabel'
				).pack(anchor=tk.W, padx=2, pady=8)
