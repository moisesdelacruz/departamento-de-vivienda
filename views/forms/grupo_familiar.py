#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import Tkinter as tk
import ttk
from utils._calendar import CalendarDialog
from utils.methods import Methods
from database.main import FamilyModel
from views.detail.grupo_familiar import Grupo_familiarDetail 

class Grupo_familiarForm(tk.Frame, Methods):
	def __init__(self, root, viviendo_id):
		tk.Frame.__init__(self, root)
		self.root = root
		self.viviendo_id = viviendo_id
		self.validate_number = (self.root.register(self.validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
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
			"entry": float(self.value),
			"discapacity": bool(self.discapacity.get()),
			"discapacity_desc": str(self.discapacity_desc),
			"old_age": bool(self.old_age.get())
		})
		db = FamilyModel()
		db.create(data)
		self.clean(self.root)
		view = Grupo_familiarDetail(self.root, self.viviendo_id)

	def form(self):
		# Content Horizontal
		div = tk.Frame(self.root, height=500, background="grey", relief=tk.RAISED)
		div.pack(expand=True, fill=tk.X)
		div.pack_propagate(0)
		# Content Vertical
		form = tk.Frame(div, width=650, relief=tk.RAISED)
		form.pack(expand=True, fill=tk.Y)
		form.pack_propagate(0)

		# Title
		tk.Label(form, text="Registrar Grupo Familiar",
			font="Helvetica 16 bold", fg="green").pack(pady=20)

		# Entry of the cedula
		tk.Label(form,text="CI:", font="Helvetica 10",
			fg="#474747").place(x=176,y=78)
		self.ci=tk.IntVar()
		tk.Entry(form,textvariable=self.ci, width=22, bd=0,
			validate='key', validatecommand=self.validate_number,
			font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
			highlightbackground="black",highlightcolor="red",
			highlightthickness=1).pack(pady=8)

		# Entry of first_name
		tk.Label(form,text="Nombre:", font="Helvetica 10",
			fg="#474747").place(x=143,y=120)
		self.first_name=tk.StringVar()
		tk.Entry(form,textvariable=self.first_name, width=22, bd=0,
			font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
			highlightbackground="black",highlightcolor="red",
			highlightthickness=1).pack(pady=8)

		# Entry of last_name
		tk.Label(form,text="Apellido:", font="Helvetica 10",
			fg="#474747").place(x=142,y=162)
		self.last_name=tk.StringVar()
		tk.Entry(form,textvariable=self.last_name, width=22, bd=0,
			font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
			highlightbackground="black",highlightcolor="red",
			highlightthickness=1).pack(pady=8)

		# Entry of birthday
		tk.Label(form, text="Fecha de Nacimiento:", font="Helvetica 10",
			fg="#474747").place(x=65,y=204)
		self.birthday=tk.StringVar()
		# select date
		date = tk.Frame(form, background="blue", relief=tk.RAISED)
		date.pack(pady=8)

		iconCalendar = self.getImage("views/images/calendar.png", 20, 20)

		calendarButton = tk.Button(date, image=iconCalendar,
			command=self.getDate, bg="#1E6FBA", fg="yellow",)
		calendarButton.pack(side=tk.RIGHT)
		calendarButton.image = iconCalendar

		tk.Entry(date,textvariable=self.birthday, width=20, bd=0,
			font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
			disabledbackground="#1E6FBA",disabledforeground="yellow",
			highlightbackground="black",highlightcolor="red",
			highlightthickness=1).pack(side=tk.RIGHT)

		# Entry birth_state
		tk.Label(form,text="Estado de Nacimiento:", font="Helvetica 10",
			fg="#474747").place(x=63,y=248)
		self.birth_state=tk.StringVar()
		tk.Entry(form,textvariable=self.birth_state, width=22, bd=0,
			font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
			highlightbackground="black",highlightcolor="red",
			highlightthickness=1).pack(pady=8)

		# Booleans Fields
		# Content BOOLEANS
		booleans = tk.Frame(form,  relief=tk.RAISED)
		booleans.pack(pady=2)

		# Entry of tercera edad
		self.old_age=tk.BooleanVar(booleans, value=False)
		ttk.Checkbutton(booleans, text='Tercera edad', variable=self.old_age,
			onvalue=True, offvalue=False).pack(side=tk.LEFT, padx=5, pady=8)

		# Entry of discapacity
		self.discapacity_desc=''
		self.discapacity=tk.BooleanVar(booleans, value=False)
		ttk.Checkbutton(booleans, text='Discapacidad', variable=self.discapacity,
			onvalue=True, offvalue=False,
			command=self.textDialog).pack(side=tk.LEFT, padx=5, pady=8)

		# Boolean of work
		self.value=tk.StringVar()
		self.work=tk.BooleanVar(booleans, value=False)
		ttk.Checkbutton(booleans, text='Trabaja', variable=self.work,
			onvalue=True, offvalue=False,
			command=self.entry).pack(side=tk.LEFT, padx=5, pady=8)

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