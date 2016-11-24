#!/usr/bin/python
# -*- coding: utf-8 -*-

import Tkinter as tk
import ttk
from database.main import SolicitudModel
from utils.methods import Methods
from utils import validate
from views.detail.status import StatusDetail

class SolicitudForm(tk.Frame, Methods):
	def __init__(self, root, viviendo_id):
		tk.Frame.__init__(self, root)
		self.root = root
		self.viviendo_id = viviendo_id
		self.db = SolicitudModel()
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
		# clean content
		self.clean(self.root)
		# render view status
		show = StatusDetail(self.root, self.viviendo_id)

	def form(self):
		# Content Horizontal
		div = tk.Frame(self.root, height=500, background="grey", relief=tk.RAISED)
		div.pack(expand=True, fill=tk.X)
		div.pack_propagate(0)
		# Content Vertical
		form = tk.Frame(div, width=650, relief=tk.RAISED)
		form.pack(expand=True, fill=tk.Y)
		form.pack_propagate(0)

		# get data from database
		data = self.db.retrive(self.viviendo_id)

		tk.Label(form, text="Solicitud de Vivienda", font="Helvetica 16 bold",
			fg="red").pack(pady=20)

		# Entry housing_conditions
		tk.Label(form,text="Condicion Habitacional:", font="Helvetica 10",
			fg="#474747").place(x=59,y=77)
		housing_conditions = tk.StringVar(form,
			value=data[0][2]) if data else tk.StringVar()
		self.housing_conditions=validate.MaxLengthEntry(form,
			value=housing_conditions.get(), maxlength=45, width=22, bd=0,
			font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
			highlightbackground="black",highlightcolor="red",
			highlightthickness=1)
		self.housing_conditions.pack(pady=8)

		# Entry housing_direction
		tk.Label(form,text="Dirección Habitacional:", font="Helvetica 10",
			fg="#474747").place(x=60,y=120)
		housing_direction = tk.StringVar(form,
			value=data[0][3]) if data else tk.StringVar()
		self.housing_direction=validate.MaxLengthEntry(form,
			value=housing_direction.get(), maxlength=45, width=22, bd=0,
			font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
			highlightbackground="black",highlightcolor="red",
			highlightthickness=1)
		self.housing_direction.pack(pady=8)
		
		# Entry phone_number
		tk.Label(form,text="Numero de Telefono:", font="Helvetica 10",
			fg="#474747").place(x=72,y=162)
		phone_number = tk.IntVar(form,
			value=data[0][4]) if data else tk.IntVar()
		self.phone_number=validate.IntegerEntry(form, value=phone_number.get(),
			width=22, bd=0, font="Helvetica 14 normal",
			justify="left",bg="#1E6FBA",fg="yellow",
			highlightbackground="black",highlightcolor="red",
			highlightthickness=1)
		self.phone_number.pack(pady=8)

		# Fields Booleans 1
		booleans = tk.Frame(form,  relief=tk.RAISED)
		booleans.pack(pady=2)

		# Entry residence_constancia
		self.residence_constancia = tk.BooleanVar(booleans,
			value=data[0][5]) if data else tk.BooleanVar(booleans, value=False)
		ttk.Checkbutton(booleans, text='Constancia de residencia', variable=self.residence_constancia,
			onvalue=True, offvalue=False).pack(side=tk.LEFT, padx=5, pady=8)

		# Entry copy_ci
		self.copy_ci = tk.BooleanVar(booleans,
			value=data[0][6]) if data else tk.BooleanVar(booleans, value=False)
		ttk.Checkbutton(booleans, text='Copia de cedula', variable=self.copy_ci,
			onvalue=True, offvalue=False).pack(side=tk.LEFT, padx=5, pady=8)

		# Entry medical_reports
		self.medical_reports = tk.BooleanVar(booleans,
			value=data[0][7]) if data else tk.BooleanVar(booleans, value=False)
		ttk.Checkbutton(booleans, text='Informes medicos', variable=self.medical_reports,
			onvalue=True, offvalue=False).pack(side=tk.LEFT, padx=5, pady=8)

		# Fields Booleans 2
		booleans2 = tk.Frame(form,  relief=tk.RAISED)
		booleans2.pack(pady=2)

		# Right
		# Entry housing_in_risk
		self.housing_in_risk = tk.BooleanVar(booleans2,
			value=data[0][8]) if data else tk.BooleanVar(booleans2, value=False)
		ttk.Checkbutton(booleans2, text='Riesgos en el hogar', variable=self.housing_in_risk,
			onvalue=True, offvalue=False).pack(side=tk.LEFT, padx=5, pady=8)

		# Entry firefighters_constancy
		self.firefighters_constancy = tk.BooleanVar(booleans2,
			value=data[0][9]) if data else tk.BooleanVar(booleans2, value=False)
		ttk.Checkbutton(booleans2, text='Constancia de los Bomberos',
			variable=self.firefighters_constancy,
			onvalue=True, offvalue=False).pack(side=tk.LEFT, padx=5, pady=8)

		# Entry health_case
		self.health_case = tk.BooleanVar(booleans2,
			value=data[0][10]) if data else tk.BooleanVar(booleans2, value=False)
		ttk.Checkbutton(booleans2, text='Caso de Salud',
			variable=self.health_case,
			onvalue=True, offvalue=False).pack(side=tk.LEFT, padx=5, pady=8)

		# Entry copy_register_of_the_big_mision_vivienda
		self.copy_register_of_the_big_mision_vivienda = tk.BooleanVar(booleans,
			value=data[0][11]) if data else tk.BooleanVar(booleans, value=False)
		ttk.Checkbutton(form, text='Copia Registro de la Gran Misíon Vivienda',
			variable=self.copy_register_of_the_big_mision_vivienda,
			onvalue=True, offvalue=False).pack(pady=8)

		# Buttons of actions
		buttons = tk.Frame(form,  relief=tk.RAISED)
		buttons.pack(pady=8)
		# buttons.pack_propagate(0)
		# Guardar
		tk.Button(buttons, command=self.save, text="Guardar",
			font="Helvetica 12 bold", bd=0, activebackground="red",
			activeforeground="blue", bg="green", fg="white", width=10,
			height=2).pack(side=tk.LEFT, padx=8)

		# Cancelar
		tk.Button(buttons, command=self.save, text="Cancelar",
			font="Helvetica 12 bold", bd=0, activebackground="red",
			activeforeground="blue", bg="grey", fg="white", width=10,
			height=2).pack(side=tk.LEFT, padx=8)