#!/usr/bin/python
# -*- coding: utf-8 -*-

import Tkinter as tk
import ttk
from utils.verticalScrolled import VerticalScrolledFrame
from utils.methods import Methods
from views import forms

class ViviendoDetailView(tk.Frame, Methods):
	def __init__(self, root, controller, viviendo, **kwargs):
		tk.Frame.__init__(self, root)
		self.root = root
		self.controller = controller
		# viviendo
		self.viviendo = viviendo

		# Detect Sex for styles change of the view
		if self.viviendo.get('sex') == "Hombre":
			self.suffixSex = 'male'
		elif self.viviendo.get('sex') == "Mujer":
			self.suffixSex = 'female'
		else:
			self.suffixSex = 'male'

		# render
		self.view()

	def edit(self):
		self.clean(self.root)
		forms.viviendo.ViviendoForm(self.root,
			self.controller, viviendo=self.viviendo)


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

		ttk.Label(view, text=self.viviendo.get('full_name'),
			style="Black22.TLabel").pack(pady=20)
		# ---- button edit ----

		# Image
		content_image = ttk.Frame(view, style='White.TFrame')
		content_image.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)


		img = self.getImage("views/images/viviendo-"+str(self.suffixSex)+
			".png", 200, 200)
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
		"Fecha de Nacimiento:", "Sexo:", "Estado Civil:", "Postulacion:",
		"Trabaja:", "Dinero:", "Discapacidad:", "Descripcion:", "Dirección:"]

		for item in info:
			ttk.Label(left, text=item, style='Black12_bold.TLabel'
				).pack(anchor=tk.E, padx=2, pady=8)

		# ---- data viviendo ----
		right = ttk.Frame(view, style='White.TFrame')
		right.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

		data = [self.viviendo.get('ci'), self.viviendo.get('first_name'),
			self.viviendo.get('last_name'), self.viviendo.get('birthday'),
			self.viviendo.get('sex'), self.viviendo.get('estado_civil'),
			self.viviendo.get('postulation'), bool(int(self.viviendo.get('work'))),
			self.viviendo.get('entry'), self.viviendo.get('discapacity'),
			self.viviendo.get('discapacity_desc') ,self.viviendo.get('direction')]

		for item in data:
			ttk.Label(right, text=item, style='Black12.TLabel'
				).pack(anchor=tk.W, padx=2, pady=8)
