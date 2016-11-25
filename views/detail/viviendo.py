#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import Tkinter as tk
from database.main import FamilyModel
from utils.methods import Methods
from views.forms.grupo_familiar import Grupo_familiarForm
from views.forms.solicitud import SolicitudForm
from views.forms.viviendo import ViviendoForm
from views.detail.status import StatusDetail
from views.detail.grupo_familiar import Grupo_familiarDetail

class ViviendoDetail(tk.Frame, Methods):
	def __init__(self, root, viviendo):
		tk.Frame.__init__(self, root)
		self.root = root
		self.viviendo = {
			"id": viviendo[0][0],
			"ci": viviendo[0][1],
			"full_name": ' '.join([viviendo[0][2], viviendo[0][3]]),
			"first_name": viviendo[0][2],
			"last_name": viviendo[0][3],
			"direction": viviendo[0][4],
			"birthday": viviendo[0][5],
			"estado_civil": viviendo[0][6],
			"work": viviendo[0][7],
			"entry": viviendo[0][8],
			"postulation": viviendo[0][9],
			"discapacity": viviendo[0][10],
			"discapacity_desc": viviendo[0][11]
		}

		# Title of window
		parent = self.root._nametowidget(self.root.winfo_parent())
		parent.title(self.viviendo['full_name'])

		# Data Base
		self.db = FamilyModel()
		# query to database
		self.group_family = self.db.list(viviendo_id=self.viviendo['id'])

		# Top div
		self.top = tk.Frame(self.root, bd=1, relief=tk.RAISED)
		self.top.pack(side=tk.TOP, fill=tk.X)
		# self.top.pack_propagate(0)
		# Left div
		self.left = tk.Frame(self.root, bd=1, width=270, relief=tk.RAISED)
		self.left.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
		self.left.pack_propagate(0)
		# Right div
		self.right = tk.Frame(self.root, width=2000, relief=tk.RAISED)
		self.right.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
		self.right.pack_propagate(0)
		
		# render
		self.render()

	def render(self):
		tk.Label(self.top, text=self.viviendo['full_name'],
			font="Helvetica 16 bold", bg="blue",
			fg="grey").pack(side=tk.TOP, fill=tk.X)

		self.viviendoFrame()
		self.familyFrame()
		self.solicitudFrame()
		self.status()


	def viviendoFrame(self):
		viviendo = tk.Frame(self.left, bd=1, width=270, height=150, relief=tk.RAISED)
		viviendo.pack(anchor=tk.NW, expand=True, fill=tk.Y)
		viviendo.pack_propagate(0)
		# images
		iconViviendo_male = self.getImage("views/images/viviendo-male.png", 100, 100)
		iconViviendo_female = self.getImage("views/images/viviendo-female.png", 100, 100)

		# icon
		icon=tk.Label(viviendo, image=iconViviendo_male)
		icon.pack(side=tk.LEFT)
		icon.image = iconViviendo_male

		# Action
		btn=tk.Button(viviendo, text="Actualizar", command=self.viviendoForm,
			font="Helvetica 14 normal", fg="grey", bd=0)
		btn.pack(anchor=tk.NE)

		# CI
		ci=tk.Label(viviendo, text=self.viviendo['ci'],
			font="Helvetica 10 normal", fg="grey")
		ci.pack(anchor=tk.SE, side=tk.BOTTOM)


	def familyFrame(self):
		self.length = ' '.join([str(len(self.group_family)), 'en el grupo'])

		family = tk.Frame(self.left, bd=1, width=270, height=150, relief=tk.RAISED)
		family.pack(anchor=tk.NW, expand=True, fill=tk.Y)
		family.pack_propagate(0)
		# images
		iconViviendo = self.getImage("views/images/show-group.png", 100, 100)

		# icon
		icon=tk.Label(family, image=iconViviendo)
		icon.pack(side=tk.LEFT, padx=5)
		icon.image = iconViviendo

		# Actions
		btn=tk.Button(family, text="Agregar", command=self.family,
			font="Helvetica 14 normal", fg="grey", bd=0)
		btn.pack(anchor=tk.NE)
		btn2=tk.Button(family, text="Lista", command=self.grupo_familiar,
			font="Helvetica 14 normal", fg="grey", bd=0)
		btn2.pack(anchor=tk.E)

		# CI
		ci=tk.Label(family, text=self.length,
			font="Helvetica 10 normal", fg="grey")
		ci.pack(anchor=tk.SE, side=tk.BOTTOM)


	def solicitudFrame(self):
		solicitud = tk.Frame(self.left, bd=1, width=270, height=150, relief=tk.RAISED)
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
			font="Helvetica 14 normal", fg="grey", bd=0)
		btn.pack(anchor=tk.NE)
		btn2=tk.Button(solicitud, text="Estatus", command=self.status,
			font="Helvetica 14 normal", fg="grey", bd=0)
		btn2.pack(anchor=tk.E)

		# CI
		ci=tk.Label(solicitud, text="estatus: espera",
			font="Helvetica 10 normal", fg="red")
		ci.pack(anchor=tk.SE, side=tk.BOTTOM)


	def family(self):
		self.clean(self.right)
		view = Grupo_familiarForm(self.right, self.viviendo['id'])
		view.pack()

	def grupo_familiar(self):
		self.clean(self.right)
		view = Grupo_familiarDetail(self.right, self.viviendo['id'])
		view.pack()

	def solicitudForm(self):
		self.clean(self.right)
		view = SolicitudForm(self.right, self.viviendo['id'])
		view.pack()

	def status(self):
		self.clean(self.right)
		view = StatusDetail(self.right, self.viviendo['id'])
		view.pack()

	def viviendoForm(self):
		self.clean(self.right)
		view = ViviendoForm(self.right, viviendo=self.viviendo)
		view.pack()


# anchor support: must be n, ne, e, se, s, sw, w, nw, or center
