#!/usr/bin/python
# -*- coding: utf-8 -*-

import Tkinter as tk
from database.main import SolicitudModel
from utils.methods import Methods
from utils.verticalScrolled import VerticalScrolledFrame
from utils.table import SimpleTable

class StatusDetail(tk.Frame, Methods):
	def __init__(self, root, viviendo_id):
		tk.Frame.__init__(self, root)
		self.root = root
		self.db = SolicitudModel()
		self.viviendo_id = viviendo_id

		# Content Horizontal
		parent = tk.Frame(self.root, height=700, relief=tk.RAISED)
		parent.pack(expand=True, fill=tk.X)
		parent.pack_propagate(0)

		# Content Vertical
		div = tk.Frame(parent, width=650, relief=tk.RAISED)
		div.pack(expand=True, fill=tk.Y)
		div.pack_propagate(0)

		# TOP content
		self.top = tk.Frame(div, background="#DDD", bd=1, relief=tk.RAISED)
		self.top.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
		self.top.pack_propagate(0)

		# BOTTOM content
		self.bottom = tk.Frame(div, background="#DDD", bd=1, relief=tk.RAISED)
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
			self.tracing()
			self.status()

	def status(self):
		# ------------
		# Title
		tk.Label(self.bottom, text="Estatus", font="Helvetica 16 bold",
			fg="violet").pack(pady=20)

		# scroll
		root = VerticalScrolledFrame(self.bottom)
		root.pack()

		# BOTTOM content
		item = tk.Frame(root.interior, width=600,
			height=250, relief=tk.RAISED)
		item.pack(expand=True, fill=tk.BOTH)
		item.pack_propagate(0)

		# images
		pointRed = self.getImage("views/images/false.png", 15, 15)
		pointGreen = self.getImage("views/images/true.png", 20, 15)

		# Constancia de residencia
		residence_constancia = tk.Label(item,
			image=pointGreen if self.data['residence_constancia'] else pointRed)
		residence_constancia.place(x=20,y=20)
		residence_constancia.image=pointGreen if self.data['residence_constancia'] else pointRed
		tk.Label(item, text="Constancia de residencia",
			font="Helvetica 10 normal", fg="#474747").place(x=40, y=20)

		# copía de cedula
		copy_ci = tk.Label(item,
			image=pointGreen if self.data['copy_ci'] else pointRed)
		copy_ci.place(x=20,y=60)
		copy_ci.image=pointGreen if self.data['copy_ci'] else pointRed
		tk.Label(item, text="copia de cedula",
			font="Helvetica 10 normal", fg="#474747").place(x=40,y=60)

		# informes medicos
		medical_reports = tk.Label(item,
			image=pointGreen if self.data['medical_reports'] else pointRed)
		medical_reports.place(x=20,y=100)
		medical_reports.image=pointGreen if self.data['medical_reports'] else pointRed
		tk.Label(item, text="Informes medicos",
			font="Helvetica 10 normal", fg="#474747").place(x=40,y=100)

		# riesgo en la vivienda
		housing_in_risk = tk.Label(item,
			image=pointGreen if self.data['housing_in_risk'] else pointRed)
		housing_in_risk.place(x=20,y=140)
		housing_in_risk.image=pointGreen if self.data['housing_in_risk'] else pointRed
		tk.Label(item, text="Riesgo en la vivienda",
			font="Helvetica 10 normal", fg="#474747").place(x=40,y=140)

		# constancia de los bomberos
		firefighters_constancy = tk.Label(item,
			image=pointGreen if self.data['firefighters_constancy'] else pointRed)
		firefighters_constancy.place(x=20,y=180)
		firefighters_constancy.image=pointGreen if self.data['firefighters_constancy'] else pointRed
		tk.Label(item, text="Constancia de los bomberos",
			font="Helvetica 10 normal", fg="#474747").place(x=40,y=180)

		# right
		# caso de salud
		health_case = tk.Label(item,
			image=pointGreen if self.data['health_case'] else pointRed)
		health_case.place(x=300,y=20)
		health_case.image=pointGreen if self.data['health_case'] else pointRed
		tk.Label(item, text="Caso de salud",
			font="Helvetica 10 normal", fg="#474747").place(x=320,y=20)

		# copia del registro de la gran mision vivienda
		copy_register_mision_vivienda = tk.Label(item,
			image=pointGreen if self.data['copy_register_mision_vivienda'] else pointRed)
		copy_register_mision_vivienda.place(x=300,y=60)
		copy_register_mision_vivienda.image=pointGreen if self.data['copy_register_mision_vivienda'] else pointRed
		tk.Label(item, text="Copia del registro Gran Misíon Vivienda",
			font="Helvetica 10 normal", fg="#474747").place(x=320,y=60)

	def tracing(self):
		# ------------
		top = tk.Frame(self.top, width=700, height=70, background="#DDD")
		top.pack(side=tk.TOP, pady=10, padx=15)
		top.pack_propagate(0)
		# last time
		last_time = tk.Frame(top, background="#DDD")
		last_time.pack(side=tk.RIGHT, pady=10, padx=15)
		tk.Label(last_time, text="Ultima Vez", font="Roboto 12 normal",
			fg="#474747", bg="#DDD").pack(anchor=tk.SE, padx=5)
		# ------
		tk.Label(last_time, text="27/12/2015", font="Roboto 22 normal",
			fg="#474747", bg="#DDD").pack(side=tk.RIGHT)

		# Numbers of times
		numbers_times = tk.Frame(top, background="#DDD")
		numbers_times.pack(side=tk.LEFT, pady=10, padx=15)
		tk.Label(numbers_times, text="Veces", font="Roboto 12 normal",
			fg="#474747", bg="#DDD").pack()
		# ------
		tk.Label(numbers_times, text="20", font="Roboto 22 normal",
			fg="#474747", bg="#DDD").pack()
		
		# scroll
		root = VerticalScrolledFrame(self.top, width=500)
		root.pack(expand=True, fill=tk.BOTH, pady=15, padx=15)
		root.pack_propagate(0)

		t = SimpleTable(root.interior, 20,3)
		t.pack(side="top", fill="x")

		t.set(0,0,"Día")
		t.set(0,1,"Mes")
		t.set(0,2,"Año")
		for x in xrange(1,20):
			t.set(x,0,"Martes 13")
			t.set(x,1,"Septiembre")
			t.set(x,2,"2016")

