#!/usr/bin/python
# -*- coding: utf-8 -*-

import Tkinter as tk
import  ttk
from datetime import datetime
from database.main import SolicitudModel
from database.main import TracingModel
from utils.methods import Methods
from utils.verticalScrolled import VerticalScrolledFrame
from utils.table import SimpleTable

class StatusDetail(tk.Frame, Methods):
	def __init__(self, root, controller, viviendo_id):
		tk.Frame.__init__(self, root)
		self.root = root
		self.controller = controller

		# Data base
		class DB(object): pass
		self.db = DB()
		self.db.solicitud = SolicitudModel()
		self.db.tracing = TracingModel()

		# viviendo id
		self.viviendo_id = viviendo_id
		# query to data base
		self.solicitud = self.db.solicitud.retrive(self.viviendo_id)
		# Query to database
		self.dates = self.db.tracing.list(viviendo_id=self.viviendo_id)
		
		# render view
		self.render()
		

	def render(self):
		div = ttk.Frame(self.root, height=550, style='Kim.TFrame')
		div.pack(expand=True, fill=tk.X)
		div.pack_propagate(0)

		view = ttk.Frame(div, width=650, padding=10, style='White.TFrame')
		view.pack(expand=True, fill=tk.Y)
		view.pack_propagate(0)

		# TOP content
		self.top = ttk.Frame(view, padding=10, style='White.TFrame')
		self.top.pack(side=tk.TOP, expand=True, fill=tk.BOTH)
		self.top.pack_propagate(0)

		# BOTTOM content
		self.bottom = ttk.Frame(view, padding=10, style='White.TFrame')
		self.bottom.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH)
		self.bottom.pack_propagate(0)

		if self.solicitud and self.dates:
			self.data = {
				"residence_constancia": self.solicitud[0][5],
				"copy_ci": self.solicitud[0][6],
				"medical_reports": self.solicitud[0][7],
				"housing_in_risk": self.solicitud[0][8],
				"firefighters_constancy": self.solicitud[0][9],
				"health_case": self.solicitud[0][10],
				"copy_register_mision_vivienda": self.solicitud[0][11]
			}
			self.tracing()
			self.status()

	def status(self):
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
		pointGreen = self.getImage("views/images/true.png", 15, 15)

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
		result = self.dates
		# ------------
		top = ttk.Frame(self.top, width=700, height=80, style='White.TFrame')
		top.pack(side=tk.TOP)
		top.pack_propagate(0)
		# last time
		last_time = ttk.Frame(top, style='White.TFrame')
		last_time.pack(side=tk.RIGHT, pady=10, padx=15)
		ttk.Label(last_time, text="Ultima Vez",
			style='Black12.TLabel').pack(anchor=tk.SE, padx=5)
		# ------
		date=datetime.strptime(str(result[-1][2]),
			'%Y-%m-%d %H:%M:%S.%f').strftime('%Y/%m/%d')
		ttk.Label(last_time, text=date,
			style='Black22.TLabel').pack(side=tk.RIGHT)

		# Numbers of times
		numbers_times = ttk.Frame(top, style='White.TFrame')
		numbers_times.pack(side=tk.LEFT, pady=10, padx=15)
		ttk.Label(numbers_times, text="Veces",
			style='Black12.TLabel').pack()
		# ------
		ttk.Label(numbers_times, text=len(result), style='Black22.TLabel').pack()
		
		# scroll
		root = VerticalScrolledFrame(self.top, width=500)
		root.pack(expand=True, fill=tk.BOTH)
		root.pack_propagate(0)

		# inverse list
		list_inverse = []
		for i in xrange(len(result)-1+1):
			list_inverse.insert(0, result[i])

		# table of dates
		t = SimpleTable(root.interior, len(list_inverse)+1,4)
		t.pack(side="top", fill="x")

		t.set(0,0,"Día")
		t.set(0,1,"Mes")
		t.set(0,2,"Año")
		t.set(0,3,"Hora")
		for (i, item) in enumerate(list_inverse):
			date = datetime.strptime(str(item[2]), '%Y-%m-%d %H:%M:%S.%f')
			t.set(int(i)+1,0,date.strftime('%d'))
			t.set(int(i)+1,1,date.strftime('%B'))
			t.set(int(i)+1,2,date.strftime('%Y'))
			t.set(int(i)+1,3,date.strftime('%H:%M:%S'))

