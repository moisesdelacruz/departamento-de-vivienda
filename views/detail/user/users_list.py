#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import Tkinter as tk
import ttk
import tkMessageBox
from utils.methods import Methods
from database.main import UserModel
from views.forms.user.register import RegisterForm
from views.detail.user.profile import ProfileView

class UsersListDetail(tk.Frame, Methods):
	def __init__(self, root, controller, **kwargs):
		tk.Frame.__init__(self, root)
		self.root = root
		self.controller = controller

		self.db = UserModel()
		self.models = self.db.list()

		# content list
		# Content Horizontal
		self.parent = ttk.Frame(self.root, height=550, style="Kim.TFrame")
		self.parent.pack(expand=True, fill=tk.X)
		self.parent.pack_propagate(0)

		# Content Vertical
		self.div = ttk.Frame(self.parent, width=650, style="Kim.TFrame")
		self.div.pack(expand=True, fill=tk.Y)
		self.div.pack_propagate(0)

		# set title of window
		self.controller.parent.title('Lista de Usuarios')
		# Title
		ttk.Label(self.div, text="Lista de Usuarios",
			style="Title.TLabel").pack(pady=15, anchor=tk.NW)

		self.list()

	def list(self):
		for model in self.models:
			model = self._format_user(model)
			if model.get('user_id') != self.controller.get_session().get('user_id'):
				self.item(model)

	def item(self, model):
		model_id = int(model.get('user_id'))

		root = ttk.Frame(self.div, height=50, style='Item.TFrame')
		root.pack(side=tk.TOP, padx=2, pady=1, fill=tk.X)
		root.pack_propagate(0)

		ttk.Label(root, text=model.get('cedula'), style='Item.TLabel'
			).pack(side=tk.LEFT, padx=4)

		username=ttk.Label(root, text=model.get('username'), style='Item.TLabel')
		username.pack(side=tk.LEFT, padx=4)
		username.bind("<Button-1>",lambda e,model=model:self.see(model))

		ttk.Label(root, text=model.get('permission'), style='Item.TLabel'
			).pack(side=tk.LEFT, padx=4)

		ttk.Label(root,
			text='superusuario' if model.get('is_superuser') else 'usuario',
			style='Item.TLabel').pack(side=tk.LEFT, padx=4)

		btn_delete=tk.Button(root, text="Eliminar", font="Helvetica 12 normal",
			command=lambda : self.delete(model_id), fg="#FFF",
			bg="#00162D", bd=0, activebackground="#00162D",
			activeforeground="#BBB")

		btn_edit=tk.Button(root, text="Editar", font="Helvetica 12 normal",
			command=lambda : self.edit(model), fg="#FFF",
			bg="#00162D", bd=0, activebackground="#00162D",
			activeforeground="#BBB")
		# if is superuser show buttons
		if self.controller.is_superuser():
			btn_delete.pack(side=tk.RIGHT, padx=4)
			btn_edit.pack(side=tk.RIGHT, padx=4)

	def delete(self, model_id):
		if self.controller.is_superuser():
			if tkMessageBox.askyesno(title='Advertencia',
				message='¿Seguro(a) que desea Eliminar?'):
				self.db.delete(model_id)
				self.parent.destroy()
				self.__init__(self.root, self.controller)
		else: self.controller.denegate()


	def edit(self, model):
		if self.controller.is_superuser():
			self.clean(self.root)
			RegisterForm(self.root, self.controller, action='edit_user', data=model)


	def see(self, model):
		self.clean(self.root)
		ProfileView(self.root, self.controller, user=model)