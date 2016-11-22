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
		# query to data base
		self.query = self.db.retrive(self.viviendo_id)
		if self.query:
			self.show()

	def show(self):
		data = {
			"residence_constancia": self.query[0][5],
			"copy_ci": self.query[0][6],
			"medical_reports": self.query[0][7],
			"housing_in_risk": self.query[0][8],
			"firefighters_constancy": self.query[0][9],
			"health_case": self.query[0][10],
			"copy_register_mision_vivienda": self.query[0][11]
		}

		tk.Label(self.root, text="Estatus", font="Helvetica 16 bold",
			fg="violet").place(x=250,y=30)

		pointRed = self.getImage("views/images/false.png", 15, 15)
		pointGreen = self.getImage("views/images/true.png", 20, 15)

		# Constancia de residencia
		residence_constancia = tk.Label(self.root,
			image=pointGreen if data['residence_constancia'] else pointRed)
		residence_constancia.place(x=20,y=400)
		residence_constancia.image=pointGreen if data['residence_constancia'] else pointRed
		tk.Label(self.root, text="Constancia de residencia",
			font="Helvetica 10 normal", fg="#474747").place(x=40,y=399)

		# copía de cedula
		copy_ci = tk.Label(self.root,
			image=pointGreen if data['copy_ci'] else pointRed)
		copy_ci.place(x=20,y=440)
		copy_ci.image=pointGreen if data['copy_ci'] else pointRed
		tk.Label(self.root, text="copia de cedula",
			font="Helvetica 10 normal", fg="#474747").place(x=40,y=439)

		# informes medicos
		medical_reports = tk.Label(self.root,
			image=pointGreen if data['medical_reports'] else pointRed)
		medical_reports.place(x=20,y=480)
		medical_reports.image=pointGreen if data['medical_reports'] else pointRed
		tk.Label(self.root, text="Informes medicos",
			font="Helvetica 10 normal", fg="#474747").place(x=40,y=479)

		# riesgo en la vivienda
		housing_in_risk = tk.Label(self.root,
			image=pointGreen if data['housing_in_risk'] else pointRed)
		housing_in_risk.place(x=20,y=520)
		housing_in_risk.image=pointGreen if data['housing_in_risk'] else pointRed
		tk.Label(self.root, text="Riesgo en la vivienda",
			font="Helvetica 10 normal", fg="#474747").place(x=40,y=519)

		# constancia de los bomberos
		firefighters_constancy = tk.Label(self.root,
			image=pointGreen if data['firefighters_constancy'] else pointRed)
		firefighters_constancy.place(x=20,y=560)
		firefighters_constancy.image=pointGreen if data['firefighters_constancy'] else pointRed
		tk.Label(self.root, text="Constancia de los bomberos",
			font="Helvetica 10 normal", fg="#474747").place(x=40,y=559)

		# right
		# caso de salud
		health_case = tk.Label(self.root,
			image=pointGreen if data['health_case'] else pointRed)
		health_case.place(x=300,y=400)
		health_case.image=pointGreen if data['health_case'] else pointRed
		tk.Label(self.root, text="Caso de salud",
			font="Helvetica 10 normal", fg="#474747").place(x=320,y=399)

		# copia del registro de la gran mision vivienda
		copy_register_mision_vivienda = tk.Label(self.root,
			image=pointGreen if data['copy_register_mision_vivienda'] else pointRed)
		copy_register_mision_vivienda.place(x=300,y=440)
		copy_register_mision_vivienda.image=pointGreen if data['copy_register_mision_vivienda'] else pointRed
		tk.Label(self.root, text="Copia del registro Gran Misíon Vivienda",
			font="Helvetica 10 normal", fg="#474747").place(x=320,y=439)