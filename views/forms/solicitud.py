#!/usr/bin/python
# -*- coding: utf-8 -*-

import Tkinter as tk
from database.main import SolicitudModel
from utils.methods import Methods

class SolicitudForm(tk.Frame, Methods):
	def __init__(self, root, viviendo_id):
		tk.Frame.__init__(self, root)
		self.root = root
		self.viviendo_id = viviendo_id
		self.db = SolicitudModel()
		self.validate_number = (self.root.register(self.validate),
				'%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
		self.form()

	def save(self):
		data = ({
			"viviendo_id": self.viviendo_id,
			"housing_conditions": self.housing_conditions.get(),
			"housing_direction": self.housing_direction.get(),
			"phone_number": int(self.phone_number.get()),
			"residence_constancia": bool(self.residence_constancia.get()),
			"copy_ci": bool(self.copy_ci.get()),
			"copy_register_of_the_big_mision_vivienda": bool(self.copy_register_of_the_big_mision_vivienda.get()),
			"housing_in_risk": bool(self.housing_in_risk.get()),
			"firefighters_constancy": bool(self.firefighters_constancy.get()),
			"health_case": bool(self.health_case.get()),
			"medical_reports": bool(self.medical_reports.get())
		})
		self.db.createOrUpdate(data)

	def form(self):
		# get data from database
		data = self.db.retrive(self.viviendo_id)

		tk.Label(self.root, text="Solicitud de Vivienda", font="Helvetica 16 bold",
			fg="red").place(x=160,y=10)

		# Entry housing_conditions
		tk.Label(self.root,text="Condicion Habitacional:", font="Helvetica 10",
			fg="#474747").place(x=7,y=90)
		self.housing_conditions = tk.StringVar(self.root,
			value=data[0][2]) if data else tk.StringVar()
		tk.Entry(self.root,textvariable=self.housing_conditions, width=22, bd=0,
			font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
			highlightbackground="black",highlightcolor="red",
			highlightthickness=1).place(x=150,y=90)

		# Entry housing_direction
		tk.Label(self.root,text="Dirección Habitacional:", font="Helvetica 10",
			fg="#474747").place(x=10,y=125)
		self.housing_direction = tk.StringVar(self.root,
			value=data[0][3]) if data else tk.StringVar()
		tk.Entry(self.root,textvariable=self.housing_direction, width=22, bd=0,
			font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
			highlightbackground="black",highlightcolor="red",
			highlightthickness=1).place(x=150,y=125)
		
		# Entry phone_number
		tk.Label(self.root,text="Numero de Telefono:", font="Helvetica 10",
			fg="#474747").place(x=23,y=160)
		self.phone_number = tk.StringVar(self.root,
			value=data[0][4]) if data else tk.StringVar()
		tk.Entry(self.root,textvariable=self.phone_number, validate='key',
			validatecommand=self.validate_number, width=22, bd=0,
			font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
			highlightbackground="black",highlightcolor="red",
			highlightthickness=1).place(x=150,y=160)

		# Entry residence_constancia
		tk.Label(self.root,text="Constancia Residencia:", font="Helvetica 10",
			fg="#474747").place(x=7,y=195)
		self.residence_constancia = tk.BooleanVar(self.root,
			value=data[0][5]) if data else tk.BooleanVar(self.root, value=False)
		tk.Checkbutton(self.root, variable=self.residence_constancia, font="Helvetica 14 normal",
			bd=0, bg="#1E6FBA", fg="black", highlightbackground="black",
			highlightcolor="red").place(x=150,y=195)

		# Entry copy_ci
		tk.Label(self.root,text="Copia de Cedula:", font="Helvetica 10",
			fg="#474747").place(x=45,y=235)
		self.copy_ci = tk.BooleanVar(self.root,
			value=data[0][6]) if data else tk.BooleanVar(self.root, value=False)
		tk.Checkbutton(self.root,variable=self.copy_ci, font="Helvetica 14 normal",
			bd=0, bg="#1E6FBA", fg="black", highlightbackground="black",
			highlightcolor="red").place(x=150,y=235)

		# Entry medical_reports
		tk.Label(self.root,text="Informes Medicos:", font="Helvetica 10 normal",
			fg="#474747").place(x=40,y=275)
		self.medical_reports = tk.BooleanVar(self.root,
			value=data[0][7]) if data else tk.BooleanVar(self.root, value=False)
		tk.Checkbutton(self.root,variable=self.medical_reports, font="Helvetica 14 normal",
			bd=0, bg="#1E6FBA", fg="black", highlightbackground="black",
			highlightcolor="red").place(x=150,y=275)

		# Right
		# Entry housing_in_risk
		tk.Label(self.root,text="Vivienda en Riesgo?:", font="Helvetica 10",
			fg="#474747").place(x=243,y=195)
		self.housing_in_risk = tk.BooleanVar(self.root,
			value=data[0][8]) if data else tk.BooleanVar(self.root, value=False)
		tk.Checkbutton(self.root,variable=self.housing_in_risk, font="Helvetica 14 normal",
			bd=0, bg="#1E6FBA", fg="black", highlightbackground="black",
			highlightcolor="red").place(x=370,y=195)

		# Entry firefighters_constancy
		tk.Label(self.root,text="Constancia de los Bomberos:", font="Helvetica 10",
			fg="#474747").place(x=193,y=235)
		self.firefighters_constancy = tk.BooleanVar(self.root,
			value=data[0][9]) if data else tk.BooleanVar(self.root, value=False)
		tk.Checkbutton(self.root,variable=self.firefighters_constancy, font="Helvetica 14 normal",
			bd=0, bg="#1E6FBA", fg="black", highlightbackground="black",
			highlightcolor="red").place(x=370,y=235)

		# Entry health_case
		tk.Label(self.root,text="Caso de Salud:", font="Helvetica 10",
			fg="#474747").place(x=275,y=270)
		self.health_case = tk.BooleanVar(self.root,
			value=data[0][10]) if data else tk.BooleanVar(self.root, value=False)
		tk.Checkbutton(self.root, variable=self.health_case, font="Helvetica 14 normal",
			bd=0, bg="#1E6FBA", fg="black", highlightbackground="black",
			highlightcolor="red").place(x=370,y=270)

		# Entry copy_register_of_the_big_mision_vivienda
		tk.Label(self.root,text="Copia del Registro de la Gran Misíon Vivienda Venezuela:",
			font="Helvetica 9", fg="#474747").place(x=48,y=310)
		self.copy_register_of_the_big_mision_vivienda = tk.BooleanVar(self.root,
			value=data[0][11]) if data else tk.BooleanVar(self.root, value=False)
		tk.Checkbutton(self.root,variable=self.copy_register_of_the_big_mision_vivienda,
			font="Helvetica 14 normal", bd=0, bg="#1E6FBA", fg="black",
			highlightbackground="black", highlightcolor="red").place(x=370,y=305)

		# Button
		tk.Button(self.root, text="Guardar", font="Helvetica 14 normal", bd=0,
			command=self.save, bg="#1E6FBA", fg="white").place(x=300,y=400)