#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import Tkinter as tk
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
		print self.models

		# content list
		# Content Horizontal
		self.parent = tk.Frame(self.root, height=550, background="grey", relief=tk.RAISED)
		self.parent.pack(expand=True, fill=tk.X)
		self.parent.pack_propagate(0)

		# Content Vertical
		self.div = tk.Frame(self.parent, width=650, relief=tk.RAISED)
		self.div.pack(expand=True, fill=tk.Y)
		self.div.pack_propagate(0)

		# Title
		tk.Label(self.div, text="Lista de Usuarios", fg="orange",
			font="Helvetica 16 bold").pack(pady=20)

		self.list()

	def list(self):
		for model in self.models:
			if model[0] != self.session.content_session.get('user_id'):
				self.item(model)

	def item(self, model):
		model_id = int(model[0])

		root = tk.Frame(self.div, bd=1, height=30, relief=tk.RAISED)
		root.pack(side=tk.TOP, padx=2, pady=1, fill=tk.X)

		tk.Label(root, text=model[4], font="Helvetica 10 normal",
			fg="#757575", bg="#EFEFEF").pack(side=tk.LEFT, padx=4)

		tk.Label(root, text=model[1], font="Helvetica 13 normal",
			fg="#757575", bg="#EFEFEF").pack(side=tk.LEFT, padx=4)

		tk.Label(root, text=model[6], font="Helvetica 13 normal",
			fg="#757575", bg="#EFEFEF").pack(side=tk.LEFT, padx=4)

		tk.Label(root, text='superusuario' if model[5] else 'usuario',
			font="Helvetica 13 normal", fg="#757575",
			bg="#EFEFEF").pack(side=tk.LEFT, padx=4)

		tk.Button(root, text="Eliminar", font="Helvetica 12 normal",
			command=lambda : self.delete(model_id), fg="#757575",
			bg="#EFEFEF", bd=0).pack(side=tk.RIGHT, padx=4)

		tk.Button(root, text="Editar", font="Helvetica 12 normal",
			command=lambda : self.edit(model_id), fg="#757575",
			bg="#EFEFEF", bd=0).pack(side=tk.RIGHT, padx=4)

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
			RegisterForm(self.root, user_id=model)
