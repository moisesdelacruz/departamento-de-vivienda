#!/usr/bin/python
# -*- coding: utf-8 -*-

import Tkinter as tk
from database.main import SolicitudModel
from utils.methods import Methods

class StatusDetail(tk.Frame, Methods):
	def __init__(self, root, viviendo_id):
		tk.Frame.__init__(self, root)
		self.root = root
		self.db = SolicitudModel()
		self.viviendo_id = viviendo_id

		# Content Horizontal
		parent = tk.Frame(self.root, height=700, background="grey", relief=tk.RAISED)
		parent.pack(expand=True, fill=tk.X)
		parent.pack_propagate(0)

		# Content Vertical
		div = tk.Frame(parent, width=650, relief=tk.RAISED)
		div.pack(expand=True, fill=tk.Y)
		div.pack_propagate(0)

		# TOP content
		self.top = tk.Frame(div, background="yellow", relief=tk.RAISED)
		self.top.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
		self.top.pack_propagate(0)

		# BOTTOM content
		self.bottom = tk.Frame(div, relief=tk.RAISED)
		self.bottom.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH)
		self.bottom.pack_propagate(0)

		# query to data base
		self.query = self.db.retrive(self.viviendo_id)
		if self.query:
			self.data = {
				"residence_constancia": self.query[0][5],
				"copy_ci": self.query[0][6],
				"medical_reports": self.query[0][7],
				"housing_in_risk": self.query[0][8],
				"firefighters_constancy": self.query[0][9],
				"health_case": self.query[0][10],
				"copy_register_mision_vivienda": self.query[0][11]
			}
			self.status()

	def status(self):
		item = self.bottom		

		# ------------
		# Title
		tk.Label(item, text="Estatus", font="Helvetica 16 bold",
			fg="violet").pack(pady=20)

		pointRed = self.getImage("views/images/false.png", 15, 15)
		pointGreen = self.getImage("views/images/true.png", 20, 15)

		# Constancia de residencia
		residence_constancia = tk.Label(item,
			image=pointGreen if self.data['residence_constancia'] else pointRed)
		residence_constancia.place(x=20,y=100)
		residence_constancia.image=pointGreen if self.data['residence_constancia'] else pointRed
		tk.Label(item, text="Constancia de residencia",
			font="Helvetica 10 normal", fg="#474747").place(x=40, y=100)

		# copía de cedula
		copy_ci = tk.Label(item,
			image=pointGreen if self.data['copy_ci'] else pointRed)
		copy_ci.place(x=20,y=140)
		copy_ci.image=pointGreen if self.data['copy_ci'] else pointRed
		tk.Label(item, text="copia de cedula",
			font="Helvetica 10 normal", fg="#474747").place(x=40,y=140)

		# informes medicos
		medical_reports = tk.Label(item,
			image=pointGreen if self.data['medical_reports'] else pointRed)
		medical_reports.place(x=20,y=180)
		medical_reports.image=pointGreen if self.data['medical_reports'] else pointRed
		tk.Label(item, text="Informes medicos",
			font="Helvetica 10 normal", fg="#474747").place(x=40,y=180)

		# riesgo en la vivienda
		housing_in_risk = tk.Label(item,
			image=pointGreen if self.data['housing_in_risk'] else pointRed)
		housing_in_risk.place(x=20,y=220)
		housing_in_risk.image=pointGreen if self.data['housing_in_risk'] else pointRed
		tk.Label(item, text="Riesgo en la vivienda",
			font="Helvetica 10 normal", fg="#474747").place(x=40,y=220)

		# constancia de los bomberos
		firefighters_constancy = tk.Label(item,
			image=pointGreen if self.data['firefighters_constancy'] else pointRed)
		firefighters_constancy.place(x=20,y=260)
		firefighters_constancy.image=pointGreen if self.data['firefighters_constancy'] else pointRed
		tk.Label(item, text="Constancia de los bomberos",
			font="Helvetica 10 normal", fg="#474747").place(x=40,y=260)

		# right
		# caso de salud
		health_case = tk.Label(item,
			image=pointGreen if self.data['health_case'] else pointRed)
		health_case.place(x=300,y=100)
		health_case.image=pointGreen if self.data['health_case'] else pointRed
		tk.Label(item, text="Caso de salud",
			font="Helvetica 10 normal", fg="#474747").place(x=320,y=100)

		# copia del registro de la gran mision vivienda
		copy_register_mision_vivienda = tk.Label(item,
			image=pointGreen if self.data['copy_register_mision_vivienda'] else pointRed)
		copy_register_mision_vivienda.place(x=300,y=140)
		copy_register_mision_vivienda.image=pointGreen if self.data['copy_register_mision_vivienda'] else pointRed
		tk.Label(item, text="Copia del registro Gran Misíon Vivienda",
			font="Helvetica 10 normal", fg="#474747").place(x=320,y=140)