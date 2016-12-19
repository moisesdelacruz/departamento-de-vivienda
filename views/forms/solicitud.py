#!/usr/bin/python
# -*- coding: utf-8 -*-

import Tkinter as tk
import ttk
from database.main import SolicitudModel
from utils.methods import Methods
from utils import validate
from views.detail.status import StatusDetail

class SolicitudForm(tk.Frame, Methods):
	def __init__(self, root, controller, viviendo, **kwargs):
		tk.Frame.__init__(self, root)
		self.root = root
		self.controller = controller

		self.viviendo = viviendo
		self.viviendo_id = viviendo.get('id')
		self.db = SolicitudModel()

		# get data from database
		self.data = self.db.retrive(self.viviendo_id)
		
		# render view
		self.render()


	def save(self):
		data = ({
			"viviendo_id": self.viviendo_id,
			"housing_conditions": self.housing_conditions.get(),
			"housing_direction": str(self.housing_direction.get('0.0',tk.END)),
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
		show = StatusDetail(self.root, self.controller, self.viviendo)


	def render(self):
		# Content Horizontal
		div = ttk.Frame(self.root, height=550, style='Kim.TFrame')
		div.pack(expand=True, fill=tk.X)
		div.pack_propagate(0)
		# Content Vertical
		self._form = ttk.Frame(div, width=650, padding=20,
			style='White.TFrame')
		self._form.pack(expand=True, fill=tk.Y)
		self._form.pack_propagate(0)
		
		self.form()


	def form(self):
		form = self._form
		data = self.data

		# Title of the Form
		ttk.Label(form, text="Solicitud de Vivienda",
			style='Black22.TLabel').pack(anchor=tk.NW)

		ttk.Label(form, text="Sera redirigido automaticamente"+
			"a un panel de administracion personalizado,"+
			"\nAl Presionar \"Guardar\".",
			style="Black12.TLabel").pack(anchor=tk.NW, pady=15)

		# Entry housing_conditions
		ttk.Label(form,text="Condicion Habitacional",
			style='Black.TLabel').place(x=0,y=130)
		housing_conditions = tk.StringVar(form,
			value=data[0][2]) if data else tk.StringVar()
		self.housing_conditions=validate.MaxLengthEntry(form, style='White.TEntry',
			value=housing_conditions.get(), maxlength=45, width=27,
			font="Helvetica 13",justify="left")
		self.housing_conditions.focus()
		self.housing_conditions.pack(pady=8)

		# Entry housing_direction
		ttk.Label(form,text="Dirección Habitacional",
			style='Black.TLabel').place(x=0,y=185)
		self.housing_direction=tk.Text(form, width=28, height=3, bd=0,
			font="Helvetica 12 normal",bg="white",fg="#6b6a6a",
			highlightbackground="grey",highlightcolor="#4FC2EB",
			highlightthickness=1)
		self.housing_direction.insert(tk.INSERT,
			data[0][3] if data else '')
		self.housing_direction.pack(pady=8)
		
		# Entry phone_number
		ttk.Label(form,text="Numero de Telefono",
			style='Black.TLabel').place(x=0,y=255)
		phone_number = tk.IntVar(form,
			value=data[0][4]) if data else tk.IntVar()
		self.phone_number=validate.IntegerEntry(form,
			value=phone_number.get(), maxlength=11,
			width=27, font="Helvetica 13", style='White.TEntry',
			justify="left")
		self.phone_number.pack(pady=8)

		# Fields Booleans 1
		booleans = ttk.Frame(form, style='White.TFrame')
		booleans.pack(pady=2)

		# Entry residence_constancia
		self.residence_constancia = tk.BooleanVar(booleans,
			value=data[0][5]) if data else tk.BooleanVar(booleans, value=False)
		ttk.Checkbutton(booleans,
			text='Constancia de residencia',
			variable=self.residence_constancia,
			onvalue=True, offvalue=False
			).pack(side=tk.LEFT, padx=5, pady=8)

		# Entry copy_ci
		self.copy_ci = tk.BooleanVar(booleans,
			value=data[0][6]) if data else tk.BooleanVar(booleans, value=False)
		ttk.Checkbutton(booleans, text='Copia de cedula', variable=self.copy_ci,
			onvalue=True, offvalue=False).pack(side=tk.LEFT, padx=5, pady=8)

		# Entry medical_reports
		self.medical_reports = tk.BooleanVar(booleans,
			value=data[0][7]) if data else tk.BooleanVar(booleans, value=False)
		ttk.Checkbutton(booleans,
			text='Informes medicos', variable=self.medical_reports,
			onvalue=True, offvalue=False).pack(side=tk.LEFT, padx=5, pady=8)

		# Fields Booleans 2
		booleans2 = ttk.Frame(form, style='White.TFrame')
		booleans2.pack(pady=2)

		# Right
		# Entry housing_in_risk
		self.housing_in_risk = tk.BooleanVar(booleans2,
			value=data[0][8]) if data else tk.BooleanVar(booleans2, value=False)
		ttk.Checkbutton(booleans2,
			text='Riesgos en el hogar', variable=self.housing_in_risk,
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
		buttons = ttk.Frame(form, style='White.TFrame')
		buttons.pack(pady=8)
		# Guardar
		ttk.Button(buttons,
			text="Cancelar").pack(side=tk.LEFT, padx=8)

		# Cancelar
		ttk.Button(buttons, command=self.save,
			text="Guardar").pack(side=tk.LEFT, padx=8)