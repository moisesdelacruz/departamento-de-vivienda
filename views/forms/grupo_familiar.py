#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import Tkinter as tk
import ttk

from datetime import datetime
from utils.methods import Methods
from utils import validate, entrydate
from database.main import FamilyModel
from views.detail.grupo_familiar import Grupo_familiarDetail 

class Grupo_familiarForm(tk.Frame, Methods):
	def __init__(self, root, viviendo_id, **kwargs):
		tk.Frame.__init__(self, root)
		self.root = root
		# get session
		if kwargs.get('session'):
			self.session = kwargs.get('session')

		self.viviendo_id = viviendo_id
		self.form()

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
		view = Grupo_familiarDetail(self.root, self.viviendo_id, session=self.session)

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
		self.ci=validate.IntegerEntry(form,
			width=22, bd=0, font="Helvetica 14 normal",
			justify="left",bg="white",fg="#6b6a6a",
			highlightbackground="black",highlightcolor="red",
			highlightthickness=0)
		self.ci.pack(pady=8)

		# Entry of first_name
		tk.Label(form,text="Nombre:", font="Helvetica 10",
			fg="#474747").place(x=143,y=120)
		self.first_name=validate.MaxLengthEntry(form,
			maxlength=30,width=22, bd=0,
			font="Helvetica 14 normal",justify="left",bg="white",
			fg="#6b6a6a", highlightbackground="black",
			highlightcolor="red", highlightthickness=0)
		self.first_name.pack(pady=8)

		# Entry of last_name
		tk.Label(form,text="Apellido:", font="Helvetica 10",
			fg="#474747").place(x=142,y=162)
		self.last_name=validate.MaxLengthEntry(form,
			maxlength=30, width=22, bd=0, font="Helvetica 14 normal",
			justify="left",bg="white",fg="#6b6a6a",
			highlightbackground="black",highlightcolor="red",
			highlightthickness=0)
		self.last_name.pack(pady=8)

		# Entry birthday
		tk.Label(form, text="Fecha de Nacimiento:", font="Helvetica 10",
			fg="#474747").place(x=65,y=204)
		date = tk.Frame(form, background="grey", relief=tk.RAISED)
		date.pack(pady=8)

		self.birthday=entrydate.DateEntry(date, bd=0, font="Helvetica 14 normal")
		self.birthday.pack(side=tk.LEFT)

		# Entry birth_state
		tk.Label(form,text="Estado de Nacimiento:", font="Helvetica 10",
			fg="#474747").place(x=63,y=248)
		self.birth_state=validate.MaxLengthEntry(form, 
			maxlength=30, width=22, bd=0, font="Helvetica 14 normal",
			justify="left",bg="white",fg="#6b6a6a", 
			highlightbackground="black",highlightcolor="red", 
			highlightthickness=0)
		self.birth_state.pack(pady=8)

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
		self.value=0
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