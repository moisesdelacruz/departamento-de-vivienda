#!/usr/bin/python
# -*- coding: utf-8 -*-

import Tkinter as tk
import ttk
from utils.verticalScrolled import VerticalScrolledFrame
from utils.methods import Methods
from views import forms

class FamilyDetailView(tk.Frame, Methods):
	def __init__(self, root, controller, viviendo_id, **kwargs):
		tk.Frame.__init__(self, root)
		self.root = root
		self.controller = controller
		# viviendo
		self.viviendo_id = viviendo_id

		# data
		if not kwargs.get('family'):
			raise ValueError("This view require a 'family' **argument")
		self.family = kwargs.get('family')
			
		# render
		self.view()

	def edit(self):
		self.clean(self.root)
		forms.grupo_familiar.Grupo_familiarForm(
			self.root, self.controller, viviendo_id=self.viviendo_id,
			action='edit', data=self.family)
		

	def view(self):
		# view
		div = ttk.Frame(self.root, height=550, style='Kim.TFrame')
		div.pack(expand=True, fill=tk.X)
		div.pack_propagate(0)

		# scroll
		root = VerticalScrolledFrame(div, width=650, height=650)
		root.pack_propagate(0)
		root.pack()

		view = ttk.Frame(root.interior, width=650,
			height=650, style='White.TFrame')
		view.pack(expand=True, fill=tk.Y)
		view.pack_propagate(0)

		ttk.Label(view, text=self.family.get('full_name'),
			style="Black22.TLabel").pack(pady=20)
		# ---- button edit ----

		# Image
		content_image = ttk.Frame(view, style='White.TFrame')
		content_image.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)


		img = self.getImage("views/images/show-group.png", 200, 200)
		image_label = tk.Label(content_image,
			image=img, background="#FFF")
		image_label.image = img
		image_label.pack(pady=10)

		ttk.Button(content_image, text="Editar",
			command=self.edit).pack(pady=10)

		# ---- info ----
		left = ttk.Frame(view, style='White.TFrame')
		left.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)


		info = ["Cedula de Identidad:", "Nombre:", "Apellido:",
		"Fecha de Nacimiento:", "Estado de Nacimiento:",
		"Tercera Edad:", "Trabaja:", "Dinero:",
		"Discapacidad:", "Descripcion:"]

		for item in info:
			ttk.Label(left, text=item, style='Black12_bold.TLabel'
				).pack(anchor=tk.E, padx=2, pady=8)

		# ---- data family ----
		right = ttk.Frame(view, style='White.TFrame')
		right.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

		data = [self.family.get('ci'), self.family.get('first_name'),
			self.family.get('last_name'), self.family.get('birthday'),
			self.family.get('birth_state'), self.family.get('old_age'),
			bool(int(self.family.get('work'))), self.family.get('entry'),
			self.family.get('discapacity'),
			self.family.get('discapacity_desc')]

		for item in data:
			ttk.Label(right, text=item, style='Black12.TLabel'
				).pack(anchor=tk.W, padx=2, pady=8)