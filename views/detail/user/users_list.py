#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import Tkinter as tk
import ttk
import tkMessageBox
from utils.methods import Methods
from database.main import UserModel
from views.forms.user.register import RegisterForm

class UsersListDetail(tk.Frame, Methods):
	def __init__(self, root, **kwargs):
		tk.Frame.__init__(self, root)
		self.root = root
		# get session
		if kwargs.get('session'):
			self.session = kwargs.get('session')

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

		# Title
		ttk.Label(self.div, text="Lista de Usuarios",
			style="Title.TLabel").pack(pady=15, anchor=tk.NW)

		self.list()

	def list(self):
		for model in self.models:
			if model[0] != self.session.content_session.get('user_id'):
				self.item(model)

	def item(self, model):
		model_id = int(model[0])

		root = ttk.Frame(self.div, height=50, style='Item.TFrame')
		root.pack(side=tk.TOP, padx=2, pady=1, fill=tk.X)
		root.pack_propagate(0)

		ttk.Label(root, text=model[4], style='Item.TLabel'
			).pack(side=tk.LEFT, padx=4)

		ttk.Label(root, text=model[1], style='Item.TLabel'
			).pack(side=tk.LEFT, padx=4)

		ttk.Label(root, text=model[6], style='Item.TLabel'
			).pack(side=tk.LEFT, padx=4)

		ttk.Label(root, text='superusuario' if model[5] else 'usuario',
			style='Item.TLabel').pack(side=tk.LEFT, padx=4)

		tk.Button(root, text="Eliminar", font="Helvetica 12 normal",
			command=lambda : self.delete(model_id), fg="#FFF",
			bg="#00162D", bd=0, activebackground="#00162D",
			activeforeground="#BBB").pack(side=tk.RIGHT, padx=4)

		tk.Button(root, text="Editar", font="Helvetica 12 normal",
			command=lambda : self.edit(model), fg="#FFF",
			bg="#00162D", bd=0, activebackground="#00162D",
			activeforeground="#BBB").pack(side=tk.RIGHT, padx=4)

	def delete(self, model):
		if self.session.permission():
			if tkMessageBox.askyesno(title='Advertencia',
				message='¿Seguro(a) que desea Eliminar?'):
				self.db.delete(model)
				self.parent.destroy()
				self.__init__(self.root, session=self.session)
		else: self.session.denegate()


	def edit(self, model):
		if self.session.permission():
			self.clean(self.root)
			RegisterForm(self.root, user=model)
