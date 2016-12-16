#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import Tkinter as tk
import ttk
from database.main import FamilyModel
from database.main import ViviendoModel
from utils.methods import Methods
from views.forms.grupo_familiar import Grupo_familiarForm
from views.forms.solicitud import SolicitudForm
from views import forms
from views.detail.status import StatusDetail
from views.detail.grupo_familiar import Grupo_familiarDetail

class ViviendoDetail(tk.Frame, Methods):
	def __init__(self, root, controller, **kwargs):
		tk.Frame.__init__(self, root)
		self.root = root
		self.controller = controller

		# instance of database
		class DB(object): pass
		self.db = DB()
		self.db.viviendo = ViviendoModel()
		self.db.family = FamilyModel()

		# Format data
		self.format(kwargs)


	def format(self, kwargs):
		# get data
		if kwargs.get('viviendo'):
			viviendo = kwargs.get('viviendo')
		elif kwargs.get('viviendo_id'):
			viviendo = self.db.viviendo.retrive(
				kwargs.get('viviendo_id'), field='viviendo_id')
		elif kwargs.get('ci'):
			viviendo = self.db.viviendo.retrive(
				kwargs.get('ci'), field='ci')
		else:
			raise ValueError('You must specify a'+
				'"viviendo_id" or "ci" attribute or viviendo object.')

		# format data
		self.viviendo = self.format_data(viviendo)

		# Detect Sex for styles change of the view
		if self.viviendo.get('sex') == "Hombre":
			self.suffixSex = 'male'
		elif self.viviendo.get('sex') == "Mujer":
			self.suffixSex = 'female'
		else:
			self.suffixSex = 'male'

		# Title of window
		self.controller.parent.title(self.viviendo.get('full_name'))

		# query to database
		self.group_family = self.db.family.list(
			viviendo_id=self.viviendo.get('id'))
		
		# render
		self.render()


	def format_data(self, viviendo):
		return ({
			"id": viviendo[0][0],
			"ci": viviendo[0][1],
			"full_name": ' '.join([viviendo[0][2], viviendo[0][3]]),
			"first_name": viviendo[0][2],
			"last_name": viviendo[0][3],
			"direction": viviendo[0][4],
			"birthday": viviendo[0][5],
			"sex": viviendo[0][6],
			"estado_civil": viviendo[0][7],
			"work": viviendo[0][8],
			"entry": viviendo[0][9],
			"postulation": viviendo[0][10],
			"discapacity": viviendo[0][11],
			"discapacity_desc": viviendo[0][12],
			"created_at": viviendo[0][13]
		})


	# ---- view instance ----
	def family(self):
		if self.controller.permission():
			self.clean(self.right)
			view = Grupo_familiarForm(self.right,
				self.controller, self.viviendo['id'])
			view.pack()

	def grupo_familiar(self):
		self.clean(self.right)
		view = Grupo_familiarDetail(self.right,
			self.controller, self.viviendo['id'])
		view.pack()

	def solicitudForm(self):
		if self.controller.permission():
			self.clean(self.right)
			view = SolicitudForm(self.right,
				self.controller, self.viviendo)
			view.pack()

	def status(self):
		self.clean(self.right)
		view = StatusDetail(self.right,
			self.controller, self.viviendo)
		view.pack()

	def viviendoForm(self):
		if self.controller.permission():
			self.clean(self.right)
			view = forms.viviendo.ViviendoForm(self.right,
				self.controller, viviendo=self.viviendo,
				viviendo_detail=self)
			view.pack()

	# ---- view ----
	def render(self):
		# Full name of the Viviendo
		ttk.Label(self.root, text=self.viviendo.get('full_name'),
			style='Title.TLabel').pack(side=tk.TOP, fill=tk.X)
		# self.top.pack_propagate(0)
		# Left div
		self.left = ttk.Frame(self.root, width=270, style='Kim.TFrame')
		self.left.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
		self.left.pack_propagate(0)
		# Right div
		self.right = ttk.Frame(self.root, width=2000, style='White.TFrame')
		self.right.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
		self.right.pack_propagate(0)

		# diff for sex
		color_male = "blue"
		color_female = "pink"
		color = eval('color_'+self.suffixSex)

		# render menu
		self.viviendoFrame()
		self.familyFrame()
		self.solicitudFrame()
		self.status()


	def viviendoFrame(self):
		viviendo = tk.Frame(self.left, width=270, height=150)
		viviendo.pack(anchor=tk.NW, expand=True, fill=tk.Y)
		viviendo.pack_propagate(0)
		# images
		iconViviendo_male = self.getImage(
			"views/images/viviendo-male.png", 100, 100)
		iconViviendo_female = self.getImage(
			"views/images/viviendo-female.png", 100, 100)
		image = eval('iconViviendo_'+self.suffixSex)
		# icon
		icon=tk.Label(viviendo, image=image)
		icon.pack(side=tk.LEFT)
		icon.image = image

		# Action
		btn=tk.Button(viviendo, text="Actualizar", command=self.viviendoForm,
			font="Helvetica 14 normal", fg="#2E2E2E", bd=0)

		if self.controller.permission():
			btn.pack(anchor=tk.NE)

		# CI
		tk.Label(viviendo, text=self.viviendo['ci'],
			font="Helvetica 10 normal",
			fg="#2E2E2E").pack(anchor=tk.SE, side=tk.BOTTOM)


	def familyFrame(self):
		self.length = ' '.join([str(len(self.group_family)), 'en el grupo'])

		family = tk.Frame(self.left, width=270, height=150)
		family.pack(anchor=tk.NW, expand=True, fill=tk.Y, pady=1)
		family.pack_propagate(0)
		# images
		iconViviendo = self.getImage("views/images/show-group.png", 100, 100)

		# icon
		icon=tk.Label(family, image=iconViviendo)
		icon.pack(side=tk.LEFT, padx=5)
		icon.image = iconViviendo

		# Actions
		btn=tk.Button(family, text="Agregar", command=self.family,
			font="Helvetica 14 normal", fg="#2E2E2E", bd=0)
		btn2=tk.Button(family, text="Lista", command=self.grupo_familiar,
			font="Helvetica 14 normal", fg="#2E2E2E", bd=0)

		if self.controller.permission():
			btn.pack(anchor=tk.NE)
		btn2.pack(anchor=tk.E)

		# length
		tk.Label(family, text=self.length,
			font="Helvetica 10 normal",
			fg="#2E2E2E").pack(anchor=tk.SE, side=tk.BOTTOM)


	def solicitudFrame(self):
		solicitud = tk.Frame(self.left, width=270, height=150)
		solicitud.pack(anchor=tk.NW, expand=True, fill=tk.Y)
		solicitud.pack_propagate(0)
		# images
		iconViviendo = self.getImage("views/images/home.ico", 100, 100)

		# icon
		icon=tk.Label(solicitud, image=iconViviendo)
		icon.pack(side=tk.LEFT)
		icon.image = iconViviendo

		# Actions
		btn=tk.Button(solicitud, text="Actualizar", command=self.solicitudForm,
			font="Helvetica 14 normal", fg="#2E2E2E", bd=0)
		btn2=tk.Button(solicitud, text="Estatus", command=self.status,
			font="Helvetica 14 normal", fg="#2E2E2E", bd=0)

		if self.controller.permission():
			btn.pack(anchor=tk.NE)
		btn2.pack(anchor=tk.E)