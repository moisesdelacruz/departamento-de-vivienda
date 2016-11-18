#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import Tkinter as tk
from PIL import Image, ImageTk

class ViviendoDetail(tk.Frame):
	def __init__(self, root, viviendo):
		tk.Frame.__init__(self, root)
		self.root = root
		self.viviendo = ' '.join([viviendo[0][2], viviendo[0][3]])
		self.view()


	def getImage(self, image, sizeY=30, sizeX=30):
		self.img = Image.open(image)
		self.img = self.img.resize((sizeY, sizeX), Image.ANTIALIAS)
		return ImageTk.PhotoImage(self.img)


	def view(self):
		tk.Label(self.root, text=self.viviendo,
			font="Helvetica 16 bold", bg="blue",
			fg="grey").pack(side=tk.TOP, fill=tk.X)

		self.btnViviendo()
		self.btnFamily()
		self.btnSolicitud()


	def btnViviendo(self):
		viviendoFrame = tk.Frame(self.root, bd=1, width=270, relief=tk.RAISED)
		viviendoFrame.pack(anchor=tk.NW, expand=True, fill=tk.Y)
		viviendoFrame.pack_propagate(0)
		# images
		iconViviendo_male = self.getImage("views/images/viviendo-male.png", 100, 100)
		iconViviendo_female = self.getImage("views/images/viviendo-female.png", 100, 100)

		# icon
		icon=tk.Label(viviendoFrame, image=iconViviendo_male)
		icon.pack(side=tk.LEFT)
		icon.image = iconViviendo_male

		# Action
		btn=tk.Button(viviendoFrame, text="Actualizar",
			font="Helvetica 14 normal", fg="grey", bd=0)
		btn.pack(anchor=tk.NE)

		# CI
		ci=tk.Label(viviendoFrame, text="CI: 26300434",
			font="Helvetica 10 normal", fg="grey")
		ci.pack(anchor=tk.SE)


	def btnFamily(self):
		familyFrame = tk.Frame(self.root, bd=1, width=270, relief=tk.RAISED)
		familyFrame.pack(anchor=tk.NW, expand=True, fill=tk.Y)
		familyFrame.pack_propagate(0)
		# images
		iconViviendo = self.getImage("views/images/show-group.png", 100, 100)

		# icon
		icon=tk.Label(familyFrame, image=iconViviendo)
		icon.pack(side=tk.LEFT)
		icon.image = iconViviendo

		# Action
		btn=tk.Button(familyFrame, text="Agregar",
			font="Helvetica 14 normal", fg="grey", bd=0)
		btn.pack(anchor=tk.NE)

		# CI
		ci=tk.Label(familyFrame, text="6 en el grupo",
			font="Helvetica 10 normal", fg="grey")
		ci.pack(anchor=tk.SE)


	def btnSolicitud(self):
		solicitudFrame = tk.Frame(self.root, bd=1, width=270, relief=tk.RAISED)
		solicitudFrame.pack(anchor=tk.NW, expand=True, fill=tk.Y)
		solicitudFrame.pack_propagate(0)
		# images
		iconViviendo = self.getImage("views/images/home.ico", 100, 100)

		# icon
		icon=tk.Label(solicitudFrame, image=iconViviendo)
		icon.pack(side=tk.LEFT)
		icon.image = iconViviendo

		# Action
		btn=tk.Button(solicitudFrame, text="Actualizar",
			font="Helvetica 14 normal", fg="grey", bd=0)
		btn.pack(anchor=tk.NE)

		# CI
		ci=tk.Label(solicitudFrame, text="estatus: espera",
			font="Helvetica 10 normal", fg="red")
		ci.pack(anchor=tk.SE)


# anchor support: must be n, ne, e, se, s, sw, w, nw, or center
