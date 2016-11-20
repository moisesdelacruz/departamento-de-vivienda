#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import Tkinter as tk
from utils.methods import Methods
from views.forms.grupo_familiar import Grupo_familiarForm
from views.forms.solicitud import SolicitudForm
from views.detail.status import StatusDetail

class ViviendoDetail(tk.Frame, Methods):
	def __init__(self, root, viviendo):
		tk.Frame.__init__(self, root)
		self.root = root
		self.viviendo = {
			"id": viviendo[0][0],
			"ci": viviendo[0][1],
			"full_name": ' '.join([viviendo[0][2], viviendo[0][3]])
		}
		# Left div
		self.left = tk.Frame(self.root, bd=1, width=270, relief=tk.RAISED)
		self.left.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
		self.left.pack_propagate(0)
		# Right div
		self.right = tk.Frame(self.root, width=700, relief=tk.RAISED)
		self.right.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
		self.right.pack_propagate(0)

		# render
		self.view()
		self.status()

	def view(self):
		tk.Label(self.root, text=self.viviendo['full_name'],
			font="Helvetica 16 bold", bg="blue",
			fg="grey").pack(side=tk.TOP, fill=tk.X)

		self.viviendoFrame()
		self.familyFrame()
		self.solicitudFrame()


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
		btn=tk.Button(viviendo, text="Actualizar",
			font="Helvetica 14 normal", fg="grey", bd=0)
		btn.pack(anchor=tk.NE)

		# CI
		ci=tk.Label(viviendo, text=self.viviendo['ci'],
			font="Helvetica 10 normal", fg="grey")
		ci.pack(anchor=tk.SE, side=tk.BOTTOM)


	def familyFrame(self):
		family = tk.Frame(self.left, bd=1, width=270, height=150, relief=tk.RAISED)
		family.pack(anchor=tk.NW, expand=True, fill=tk.Y)
		family.pack_propagate(0)
		# images
		iconViviendo = self.getImage("views/images/show-group.png", 100, 100)

		# icon
		icon=tk.Label(family, image=iconViviendo)
		icon.pack(side=tk.LEFT)
		icon.image = iconViviendo

		# Action
		btn=tk.Button(family, text="Agregar", command=self.family,
			font="Helvetica 14 normal", fg="grey", bd=0)
		btn.pack(anchor=tk.NE)

		# CI
		ci=tk.Label(family, text="6 en el grupo",
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

		# Action
		btn=tk.Button(solicitud, text="Actualizar", command=self.solicitud,
			font="Helvetica 14 normal", fg="grey", bd=0)
		btn.pack(anchor=tk.NE)

		# CI
		ci=tk.Label(solicitud, text="estatus: espera",
			font="Helvetica 10 normal", fg="red")
		ci.pack(anchor=tk.SE, side=tk.BOTTOM)


	def family(self):
		self.clean(self.right)
		group_family = Grupo_familiarForm(self.right, self.viviendo['id'])
		group_family.pack()

	def solicitud(self):
		self.clean(self.right)
		solicitud = SolicitudForm(self.right, self.viviendo['id'])
		solicitud.pack()

	def status(self):
		self.clean(self.right)
		status = StatusDetail(self.right, self.viviendo['id'])
		status.pack()



# anchor support: must be n, ne, e, se, s, sw, w, nw, or center
