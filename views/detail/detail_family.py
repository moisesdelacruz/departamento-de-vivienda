#!/usr/bin/python
# -*- coding: utf-8 -*-

import Tkinter as tk
import ttk
from utils.verticalScrolled import VerticalScrolledFrame
from utils.methods import Methods
from views import forms
from views.reports.report import ReportsModule

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
		if self.controller.permission():
			self.clean(self.root)
			forms.grupo_familiar.Grupo_familiarForm(
				self.root, self.controller, viviendo_id=self.viviendo_id,
				action='edit', data=self.family)

	def report(self):
		report=ReportsModule(viviendo_id=self.viviendo_id)
		report._family(self.family)


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
			height=900, style='White.TFrame')
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
		# ----- Buttons -----
		btn_edit=ttk.Button(content_image, text="Editar",
			command=self.edit)

		btn_report=ttk.Button(content_image, text="Reporte",
			command=self.report)

		if self.controller.permission():
			btn_edit.pack(pady=10)
		btn_report.pack(pady=10)

		# ---- Labels ----
		left = ttk.Frame(view, style='White.TFrame')
		left.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
		# ---- data ----
		right = ttk.Frame(view, style='White.TFrame')
		right.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)

		labels = ['Cedula de Identidad:','Nombre:','Apellido:',
			'Fecha de Nacimiento:','Sexo:','Estado Civil:','Niv. Instruccional:',
			'Trabaja:','Occupacion:','Institucion:','Ingresos:',
			'Estado de Nacimiento:','Discapacidad:',
			'Desc. Descapacidad:','Tercera Edad:']


		data = [self.family.get('ci'),
			self.family.get('first_name'),
			self.family.get('last_name'),
			self.family.get('birthday'),
			self.family.get('sex'),
			self.family.get('estado_civil'),
			self.family.get('instructional_level'),
			str(self.family.get('work')),
			self.family.get('occupation'),
			self.family.get('institution'),
			self.family.get('entry'),
			self.family.get('birth_state'),
			str(self.family.get('discapacity')),
			self.family.get('discapacity_desc'),
			str(self.family.get('old_age'))]


		for (x, item) in enumerate(data):
			# labels
			ttk.Label(left, text=labels[x], style='Black12_bold.TLabel'
				).pack(anchor=tk.E, padx=2, pady=8)
			# data
			ttk.Label(right, text=item, style='Black12.TLabel'
				).pack(anchor=tk.W, padx=2, pady=8)
