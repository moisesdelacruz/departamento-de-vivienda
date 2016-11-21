#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import Tkinter as tk
from utils._calendar import CalendarDialog
from utils.methods import Methods
from database.main import FamilyModel
from views.detail.grupo_familiar import Grupo_familiarDetail 

class Grupo_familiarForm(tk.Frame, Methods):
	def __init__(self, root, viviendo_id):
		tk.Frame.__init__(self, root)
		self.root = root
		self.viviendo_id = viviendo_id
		self.form()

	def getDate(self):
		cd = CalendarDialog(self)
		result = cd.result
		try:
			self.birthday.set(result.strftime("%d/%m/%Y"))
		except AttributeError, e:
			self.birthday.set(self.birthday.get())

	def save(self):
		data = ({
			"viviendo_id": int(self.viviendo_id),
			"ci": int(self.ci.get()),
			"first_name": self.first_name.get(),
			"last_name": self.last_name.get(),
			"birthday": self.birthday.get(),
			"work": bool(self.work.get()),
			"birth_state": self.birth_state.get(),
			"entry": float(self.entry.get()),
			"discapacity": bool(self.discapacity.get()),
			"discapacity_desc": str(self.discapacity_desc.get('0.0',tk.END)),
			"old_age": bool(self.old_age.get())
		})
		db = FamilyModel()
		db.create(data)
		self.clean(self.root)
		view = Grupo_familiarDetail(self.root, self.viviendo_id)

	def form(self):
		# Title
		tk.Label(self.root, text="Registrar Grupo Familiar",
			font="Helvetica 16 bold", fg="green").place(x=100,y=10)

		# Entry of the cedula
		tk.Label(self.root,text="CI:", font="Helvetica 12",
			fg="#474747").place(x=60,y=90)
		self.ci=tk.StringVar(self.root, value='0')
		tk.Entry(self.root,textvariable=self.ci, width=20, bd=0,
			font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
			highlightbackground="black",highlightcolor="red",
			highlightthickness=1).place(x=90,y=90)

		# Entry of first_name
		tk.Label(self.root,text="Nombre:", font="Helvetica 12",
			fg="#474747").place(x=16,y=125)
		self.first_name=tk.StringVar()
		tk.Entry(self.root,textvariable=self.first_name, width=20, bd=0,
			font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
			highlightbackground="black",highlightcolor="red",
			highlightthickness=1).place(x=90,y=125)

		# Entry of last_name
		tk.Label(self.root,text="Apellido:", font="Helvetica 12",
			fg="#474747").place(x=15,y=160)
		self.last_name=tk.StringVar()
		tk.Entry(self.root,textvariable=self.last_name, width=20, bd=0,
			font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
			highlightbackground="black",highlightcolor="red",
			highlightthickness=1).place(x=90,y=160)

		# Entry of birthday
		tk.Label(self.root,text="Fecha de Nacimiento:", font="Helvetica 10",
			fg="#474747").place(x=10,y=205)
		self.birthday=tk.StringVar()
		# select date
		iconCalendar = self.getImage("views/images/calendar.png", 20, 20)

		calendarButton = tk.Button(self.root, image=iconCalendar,
			command=self.getDate, bg="#1E6FBA", fg="yellow",)
		calendarButton.place(x=264,y=205)
		calendarButton.image = iconCalendar

		tk.Entry(self.root,textvariable=self.birthday, width=10, bd=0,
			font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
			disabledbackground="#1E6FBA",disabledforeground="yellow",
			highlightbackground="black",highlightcolor="red",
			highlightthickness=1).place(x=145,y=205)

		# Entry birth_state
		tk.Label(self.root,text="Estado de Nacimiento:", font="Helvetica 10",
			fg="#474747").place(x=8,y=240)
		self.birth_state=tk.StringVar()
		tk.Entry(self.root,textvariable=self.birth_state, width=13, bd=0,
			font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
			highlightbackground="black",highlightcolor="red",
			highlightthickness=1).place(x=145,y=240)

		# Right Fields
		# Entry of tercera edad
		tk.Label(self.root,text="Tercera Edad?:", font="Helvetica 10 normal",
			fg="#474747").place(x=305,y=205)
		self.old_age=tk.BooleanVar(self.root, value=False)
		tk.Checkbutton(self.root, variable=self.old_age, font="Helvetica 14 normal",
			bd=0, bg="#1E6FBA", fg="black", highlightbackground="black",
			highlightcolor="red").place(x=400,y=205)

		# Entry of discapacity
		tk.Label(self.root,text="Discapacidad?:", font="Helvetica 10 normal",
			fg="#474747").place(x=305,y=240)
		self.discapacity=tk.BooleanVar(self.root, value=False)
		tk.Checkbutton(self.root, variable=self.discapacity, font="Helvetica 14 normal",
			bd=0, bg="#1E6FBA", fg="black", highlightbackground="black",
			highlightcolor="red").place(x=400,y=240)

		# LEFT Field
		# Entry of discapacity description
		tk.Label(self.root,text="Describa Discapacidad:", font="Helvetica 10 normal",
			fg="#474747").place(x=4,y=280)
		self.discapacity_desc=tk.Text(self.root, width=43, height=4, bd=0,
			font="Helvetica 12 normal",bg="#1E6FBA",fg="yellow",
			highlightbackground="black",highlightcolor="red",
			highlightthickness=1)
		self.discapacity_desc.place(x=145,y=280)

		# Right Fields
		# Entry of work
		tk.Label(self.root,text="Trabaja?:", font="Helvetica 12",
			fg="#474747").place(x=324,y=90)
		self.work=tk.BooleanVar(self.root, value=False)
		tk.Checkbutton(self.root, variable=self.work, font="Helvetica 14 normal",
			bd=0, bg="#1E6FBA", fg="black", highlightbackground="black",
			highlightcolor="red").place(x=400,y=90)

		# Entry of Entry > Ingresos
		tk.Label(self.root,text="Ingresos:", font="Helvetica 12",
			fg="#474747").place(x=327,y=125)
		self.entry=tk.StringVar()
		tk.Entry(self.root,textvariable=self.entry, width=12, bd=0,
			font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
			highlightbackground="black",highlightcolor="red",
			highlightthickness=1).place(x=400,y=125)

		# Button
		tk.Button(self.root, text="Guardar", font="Helvetica 14 normal", bd=0,
			command=self.save, bg="#1E6FBA", fg="white").place(x=450,y=400)