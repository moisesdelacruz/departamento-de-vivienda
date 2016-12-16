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
	def __init__(self, root, controller, viviendo_id, **kwargs):
		tk.Frame.__init__(self, root)
		self.root = root
		self.controller = controller

		self.viviendo_id = viviendo_id

		self.render()


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
		view = Grupo_familiarDetail(self.root, self.controller, self.viviendo_id)


	def render(self):
		# boxs------
		div = ttk.Frame(self.root, height=550, style='Kim.TFrame')
		div.pack(expand=True, fill=tk.X)
		div.pack_propagate(0)

		self._form = ttk.Frame(div, width=650, padding=20, style='White.TFrame')
		self._form.pack(expand=True, fill=tk.Y)
		self._form.pack_propagate(0)

		self.form()

	def form(self):
		form=self._form

		# Title of the Form
		ttk.Label(form, text="Registrar Familiar",
			style='Black22.TLabel').pack(anchor=tk.NW)

		ttk.Label(form, text="Sera redirigido automaticamente"+
			"a un panel de administracion personalizado,"+
			"\nAl Presionar \"Guardar\".",
			style="Black12.TLabel").pack(anchor=tk.NW, pady=15)

		# Entry of the cedula
		ttk.Label(form,text="CI",
			style='Black.TLabel').place(x=0,y=135)
		self.ci=validate.IntegerEntry(form, style='White.TEntry',
			width=27, font="Helvetica 13",
			justify="left")
		self.ci.focus()
		self.ci.pack(pady=8)

		# Entry of first_name
		ttk.Label(form,text="Nombre",
			style='Black.TLabel').place(x=0,y=185)
		self.first_name=validate.MaxLengthEntry(form,
			style='White.TEntry', maxlength=30,width=27,
			font="Helvetica 13",justify="left")
		self.first_name.pack(pady=8)

		# Entry of last_name
		ttk.Label(form,text="Apellido",
			style='Black.TLabel').place(x=0,y=235)
		self.last_name=validate.MaxLengthEntry(form,
			style='White.TEntry', maxlength=30, width=27,
			font="Helvetica 13", justify="left")
		self.last_name.pack(pady=8)

		# Entry birthday
		ttk.Label(form, text="Fecha de Nacimiento",
			style='Black.TLabel').place(x=0,y=280)

		self.birthday=entrydate.DateEntry(form,
			style='White.TEntry', font="Helvetica 13")
		self.birthday.pack(pady=8)

		# Entry birth_state
		ttk.Label(form,text="Estado de Nacimiento",
			style='Black.TLabel').place(x=0,y=330)
		self.birth_state=validate.MaxLengthEntry(form,
			style='White.TEntry', maxlength=30, width=27,
			font="Helvetica 13", justify="left")
		self.birth_state.pack(pady=8)

		# Booleans Fields
		# Content BOOLEANS
		booleans = ttk.Frame(form, style='White.TFrame')
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
			command=lambda : self.textDialog(self.discapacity_desc)
			).pack(side=tk.LEFT, padx=5, pady=8)

		# Boolean of work
		self.value=0
		self.work=tk.BooleanVar(booleans, value=False)
		ttk.Checkbutton(booleans, text='Trabaja', variable=self.work,
			onvalue=True, offvalue=False,
			command=lambda : self.entry(self.value)
			).pack(side=tk.LEFT, padx=5, pady=8)

		# Buttons of actions
		buttons = ttk.Frame(form, style='White.TFrame')
		buttons.pack(pady=8)
		# Guardar
		ttk.Button(buttons,
			text="Cancelar").pack(side=tk.LEFT, padx=8)

		# Cancelar
		ttk.Button(buttons, command=self.save,
			text="Guardar").pack(side=tk.LEFT, padx=8)