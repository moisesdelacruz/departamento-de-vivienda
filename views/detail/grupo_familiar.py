#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import Tkinter as tk
import tkMessageBox
from utils.methods import Methods
from database.main import FamilyModel

class Grupo_familiarDetail(tk.Frame, Methods):
	def __init__(self, root, viviendo_id):
		tk.Frame.__init__(self, root)
		self.root = root
		self.viviendo_id = viviendo_id
		self.db = FamilyModel()
		self.models = self.db.list(viviendo_id=self.viviendo_id)

		# Title
		tk.Label(self.root, text="Grupo Familiar", fg="orange",
			font="Helvetica 16 bold").place(x=200,y=30)

		# content list
		self.div = tk.Frame(self.root, bd=0, relief=tk.RAISED)
		self.div.pack(side=tk.TOP, pady=70, expand=True, fill=tk.BOTH)

		self.list()

	def list(self):
		for model in self.models:
			self.item(model)

	def item(self, model):
		model_id = int(model[0])
		print model_id

		root = tk.Frame(self.div, bd=1, height=30, relief=tk.RAISED)
		root.pack(side=tk.TOP, padx=2, pady=1, fill=tk.X)

		tk.Label(root, text=model[2], font="Helvetica 10 normal",
			fg="#757575", bg="#EFEFEF").pack(side=tk.LEFT, padx=4)

		tk.Label(root, text=' '.join([model[3], model[4]]), font="Helvetica 13 normal",
			fg="#757575", bg="#EFEFEF").pack(side=tk.LEFT, padx=4)

		tk.Button(root, text="Eliminar", font="Helvetica 12 normal",
			command=lambda : self.delete(model_id), fg="#757575",
			bg="#EFEFEF", bd=0).pack(side=tk.RIGHT, padx=4)

	def delete(self, model):
		if tkMessageBox.askyesno(title='Advertencia',
            message='¿Seguro(a) que desea Eliminar?'):
			self.db.delete(model)
			self.div.destroy()
			self.__init__(self.root, self.viviendo_id)