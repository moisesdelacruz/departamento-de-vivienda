#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import Tkinter as tk
import ttk

from utils._calendar import CalendarDialog
from utils.methods import Methods
from utils import validate
from database.main import ViviendoModel
# from views.detail.viviendo import ViviendoDetail

class ViviendoForm(tk.Frame, Methods):

	def __init__(self, root, **kwargs):
		tk.Frame.__init__(self, root)
		self.root = root
		self.db = ViviendoModel()
		self.viviendo = {}
		if kwargs.get('viviendoDetail'):
			self.viviendoDetail = kwargs.get('viviendoDetail')
		if kwargs.get('viviendo'):
			self.viviendo = kwargs.get('viviendo')
		self.form()

	def save(self):
		data = ({
			"ci": int(self.ci.get()),
			"first_name": self.first_name.get(),
			"last_name": self.last_name.get(),
			"direction": str(self.direction.get('0.0',tk.END)),
			"birthday": self.birthday.get(),
			"estado_civil": self.estado_civil.get(),
			"work": bool(self.work.get()),
			"entry": float(self.value),
			"postulation": self.postulation.get(),
			"discapacity": bool(self.discapacity.get()),
			"discapacity_desc": str(self.discapacity_desc)
		})

		if self.viviendo:
			data['id'] = self.viviendo.get('id')
			self.db.update(data)
			parent = self.root._nametowidget(self.root.winfo_parent())
			self.clean(parent)
			render = self.viviendoDetail.__init__(parent, viviendo_id=self.viviendo.get('id'))
		else:
			self.db.create(data)

	def form(self):
		div = tk.Frame(self.root, height=500, background="grey", relief=tk.RAISED)
		div.pack(expand=True, fill=tk.X)
		div.pack_propagate(0)

		form = tk.Frame(div, width=650, relief=tk.RAISED)
		form.pack(expand=True, fill=tk.Y)
		form.pack_propagate(0)

		# Title of the Form
		tk.Label(form, text="Registro de Viviendo", font="Helvetica 16 bold",
			fg="blue").pack(pady=20)

		# Entry of the cedula
		tk.Label(form, text="CI:", font="Helvetica 10",
			fg="#474747").place(x=176,y=78)

		self.ci=validate.IntegerEntry(form,
			value=self.viviendo.get('ci') if self.viviendo else 0,
			width=22, bd=0, font="Helvetica 14 normal",justify="left",
			bg="#1E6FBA",fg="yellow", highlightbackground="black",
			highlightcolor="red", highlightthickness=1)
		self.ci.pack(pady=8)

		# Entrada de texto para Nombre
		tk.Label(form, text="Nombre:", font="Helvetica 10",
			fg="#474747").place(x=143,y=120)
		self.first_name=validate.MaxLengthEntry(form,
			value=self.viviendo.get('first_name') if self.viviendo else '',
			maxlength=40, width=22, bd=0,
			font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
			disabledbackground="#1E6FBA",disabledforeground="yellow",
			highlightbackground="black",highlightcolor="red",
			highlightthickness=1)
		self.first_name.pack(pady=8)

		# Entrada de texto para Apellido
		tk.Label(form, text="Apellido:", font="Helvetica 10",
			fg="#474747").place(x=142,y=162)
		self.last_name=validate.MaxLengthEntry(form,
			value=self.viviendo.get('last_name') if self.viviendo else '',
			maxlength=40, width=22, bd=0,
			font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
			disabledbackground="#1E6FBA",disabledforeground="yellow",
			highlightbackground="black",highlightcolor="red",
			highlightthickness=1)
		self.last_name.pack(pady=8)

		# Entry birthday
		tk.Label(form, text="Fecha de Nacimiento:", font="Helvetica 10",
			fg="#474747").place(x=65,y=204)
		self.birthday=tk.StringVar(form,
			value=self.viviendo.get('birthday') if self.viviendo else 'YY-mm-dd')
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

		# Entrada de texto para estado_civil
		tk.Label(form, text="Estado Civil:", font="Helvetica 10",
			fg="#474747").place(x=120,y=246)
		self.estado_civil=validate.MaxLengthEntry(form,
			value=self.viviendo.get('estado_civil') if self.viviendo else '',
			maxlength=40, width=22, bd=0,
			font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
			disabledbackground="#1E6FBA",disabledforeground="yellow",
			highlightbackground="black",highlightcolor="red",
			highlightthickness=1)
		self.estado_civil.pack(pady=8)

		# Entrada de texto para postulation
		tk.Label(form, text="Postulacion:", font="Helvetica 10",
			fg="#474747").place(x=120,y=288)
		self.postulation=validate.MaxLengthEntry(form,
			value=self.viviendo.get('postulation') if self.viviendo else '',
			maxlength=40, width=22, bd=0,
			font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
			disabledbackground="#1E6FBA",disabledforeground="yellow",
			highlightbackground="black",highlightcolor="red",
			highlightthickness=1)
		self.postulation.pack(pady=8)

		# Entrada de texto para Direccion
		tk.Label(form, text="Dirección:", font="Helvetica 10",
			fg="#474747").place(x=135,y=330)
		self.direction=tk.Text(form, width=27, height=3, bd=1,
			font="Helvetica 12 normal",bg="#1E6FBA",fg="yellow",
			highlightbackground="black",highlightcolor="red",
			highlightthickness=1)
		self.direction.insert(tk.INSERT,
			self.viviendo.get('direction') if self.viviendo else '')
		self.direction.pack(pady=8)

		# Content BOOLEANS
		booleans = tk.Frame(form,  relief=tk.RAISED)
		booleans.pack(pady=2)
		# Entrada de texto para work BOOLEAN
		self.work=tk.BooleanVar(booleans, 
			value=self.viviendo.get('work') if self.viviendo else False)
		self.value = self.viviendo.get('entry') if self.viviendo else 0
		ttk.Checkbutton(booleans, text='Trabaja', variable=self.work,
			onvalue=True, offvalue=False,
			command=lambda : self.entry(self.value)).pack(side=tk.LEFT, padx=5, pady=8)

		# Entrada de texto para discapacity BOOLEAN
		self.discapacity=tk.BooleanVar(booleans, 
			value=self.viviendo.get('discapacity') if self.viviendo else False)
		self.discapacity_desc = self.viviendo.get('discapacity') if self.viviendo else ''
		ttk.Checkbutton(booleans, text='Discapacidad', variable=self.discapacity,
			onvalue=True, offvalue=False,
			command=lambda : self.textDialog(self.discapacity_desc)
			).pack(side=tk.LEFT, padx=5, pady=8)

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