#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import Tkinter as tk
import ttk
import tkMessageBox
from utils.methods import Methods
from database.main import FamilyModel
from views import forms
from views.detail.detail_family import FamilyDetailView

class Grupo_familiarDetail(tk.Frame, Methods):
	def __init__(self, root, controller, viviendo_id, **kwargs):
		tk.Frame.__init__(self, root)
		self.root = root
		self.controller = controller

		self.viviendo_id = viviendo_id
		self.db = FamilyModel()
		self.models = self.db.list(viviendo_id=self.viviendo_id)

		self.render()


	def render(self):
		# content list
		# boxs------
		div = ttk.Frame(self.root, height=550, style='Kim.TFrame')
		div.pack(expand=True, fill=tk.X)
		div.pack_propagate(0)

		self._form = ttk.Frame(div, width=650, padding=20, style='White.TFrame')
		self._form.pack(expand=True, fill=tk.Y)
		self._form.pack_propagate(0)

		# Title
		ttk.Label(self._form, text="Lista de Usuarios",
			style="Black22.TLabel").pack(pady=15, anchor=tk.NW)

		self.list()


	def list(self):
		for model in self.models:
			model = self._format_family(model)
			self.item(model)


	def item(self, model):
		model_id = int(model.get('id'))

		root = ttk.Frame(self._form, height=50, style='Grey.TFrame')
		root.pack(side=tk.TOP, padx=2, pady=1, fill=tk.X)
		root.pack_propagate(0)

		ttk.Label(root, text=model.get('ci'), style='Grey12.TLabel'
			).pack(side=tk.LEFT, padx=4)

		name=ttk.Label(root, text=model.get('full_name'),
			style='Grey12.TLabel')
		name.pack(side=tk.LEFT, padx=4)
		name.bind("<Button-1>",lambda e,model=model:self.see(model))

		ttk.Button(root, text="Eliminar", style='Grey12.TLabel',
			command=lambda : self.delete(model_id)).pack(side=tk.RIGHT, padx=4)

		ttk.Button(root, text="Editar", style='Grey12.TLabel',
			command=lambda : self.edit(model)).pack(side=tk.RIGHT, padx=4)


	def delete(self, model_id):
		if self.controller.permission():
			if tkMessageBox.askyesno(title='Advertencia',
				message='¿Seguro(a) que desea Eliminar?'):
				self.db.delete(model_id)
				self.parent.destroy()
				self.__init__(self, self.root, self.controller, self.viviendo_id)
		else: self.controller.denegate()


	def edit(self, model):
		if self.controller.permission():
			self.clean(self.root)
			forms.grupo_familiar.Grupo_familiarForm(
				self.root, self.controller, viviendo_id=self.viviendo_id,
				action='edit', data=model)


	def see(self, model):
		self.clean(self.root)
		FamilyDetailView(
			self.root, self.controller, self.viviendo_id, family=model)