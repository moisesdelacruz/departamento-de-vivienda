#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import Tkinter as tk
import ttk

from datetime import datetime
from utils.methods import Methods
from utils import validate, entrydate
from database.main import ViviendoModel
from views.detail.viviendo import ViviendoDetail

class ViviendoForm(tk.Frame, Methods):

	def __init__(self, root, controller, **kwargs):
		tk.Frame.__init__(self, root)
		self.root = root
		self.controller = controller
		# instance from database
		self.db = ViviendoModel()
		# state actual of the form
		self.form_actually = 1

		# default title of window
		self.controller.parent.title('Nuevo Viviendo')

		self.viviendo = {}
		if kwargs.get('viviendo'):
			self.viviendo = kwargs.get('viviendo')
			# change title of window
			self.controller.parent.title(self.viviendo.get('full_name'))

		# render view
		self.render()


	def save(self):
		data = ({
			"ci": int(self.ci.get()),
			"first_name": self.first_name.get(),
			"last_name": self.last_name.get(),
			"birthday": self.birthday.get(),
			"sex": self.sex.get(),
			"estado_civil": self.estado_civil.get(),
			"instructional_level": self.instructional_level.get(),
			"work": bool(self.work.get()),
			"occupation": self.occupation.get(),
			"institution": self.institution.get(),
			"entry": float(self.value),
			"direction": str(self.new_direction),
			"postulation": self.postulation.get(),
			"discapacity": bool(self.discapacity.get()),
			"discapacity_desc": str(self.discapacity_desc)
		})

		if self.viviendo:
			data['id'] = self.viviendo.get('id')
			self.db.update(data)
			# Content main.
			parent = self.root._nametowidget(self.root.winfo_parent())
			self.clean(parent)
			ViviendoDetail(parent, self.controller,
				viviendo_id=self.viviendo.get('id'))
		else:
			self.db.create(data)
			# View Vivivendo Detail
			self.clean(self.root)
			view = ViviendoDetail(self.root, self.controller,
				ci=data.get('ci'))
			view.pack()

	def change_form(self, action):
		self.clean(self.content_form)
		if action == 'next':
			self.form_actually += 1
		elif action == 'back':
			self.form_actually -= 1
		elif action == 'render':
			pass

		if hasattr(self, eval("'form%s'" %(str(self.form_actually)))):
			# Title of the Form
			ttk.Label(self.content_form, text="Editar Viviendo"
					if self.viviendo else "Registro de Viviendo",
				style='Black22.TLabel').pack(anchor=tk.NW)

			ttk.Label(self.content_form, text="Sera redirigido automaticamente"+
				"a un panel de administracion personalizado,"+
				"\nAl Presionar \"Guardar\".",
				style="Black12.TLabel").pack(anchor=tk.NW, pady=15)
			# render form
			eval('self.form%s()' %(str(self.form_actually)))
			# content message
			self.content_message = ttk.Frame(self.content_form,
				style='Kim.TFrame')
			self.content_message.pack(pady=8)

	def set_error(self, err):
		self.clean(self.content_message)
		ttk.Label(self.content_message,
			text=err, style='Error.TLabel').pack()

	def render(self):
		# boxs------
		div = ttk.Frame(self.root, height=550, style='Kim.TFrame')
		div.pack(expand=True, fill=tk.X)
		div.pack_propagate(0)

		self.content_form = ttk.Frame(div, width=650, padding=20, style='White.TFrame')
		self.content_form.pack(expand=True, fill=tk.Y)
		self.content_form.pack_propagate(0)
		# call form1
		self.change_form('render')


	def form1(self):
		form = self.content_form

		# Entry of the cedula
		ttk.Label(form, text="CI:",
			style='Black.TLabel').place(x=0,y=130)

		self.ci=validate.IntegerEntry(form, style='White.TEntry', maxlength=9,
			value=self.viviendo.get('ci') if self.viviendo else 0,
			width=27,justify="left", font="Helvetica 13")
		self.ci.focus()
		self.ci.pack(pady=8)

		# Entrada de texto para Nombre
		ttk.Label(form, text="Nombre:",
			style='Black.TLabel').place(x=0,y=185)
		self.first_name=validate.MaxLengthEntry(form, style='White.TEntry',
			value=self.viviendo.get('first_name') if self.viviendo else '',
			maxlength=40, width=27, font="Helvetica 13",justify="left")
		self.first_name.pack(pady=8)

		# Entrada de texto para Apellido
		ttk.Label(form, text="Apellido:",
			style='Black.TLabel').place(x=0,y=235)
		self.last_name=validate.MaxLengthEntry(form, style='White.TEntry',
			value=self.viviendo.get('last_name') if self.viviendo else '',
			maxlength=40, width=27, font="Helvetica 13",justify="left")
		self.last_name.pack(pady=8)

		# Entry birthday
		ttk.Label(form, text="Fecha de Nacimiento:",
			style='Black.TLabel').place(x=0,y=285)
		date = tk.Frame(form, background="grey", relief=tk.RAISED)
		date.pack(pady=8)

		actually = self.viviendo.get('birthday') if self.viviendo else None

		self.birthday=entrydate.DateEntry(date, actually=actually,
			style='White.TEntry', font="Helvetica 13")
		self.birthday.pack(side=tk.LEFT)

		# Sex
		ttk.Label(form, text="Sexo:",
			style='Black.TLabel').place(x=0,y=330)
		self.sex = tk.StringVar(form,
			value=self.viviendo.get('sex') if self.viviendo else '')
		fieldSex = ttk.Combobox(form, state='readonly', textvariable=self.sex,
			font="Helvetica 13", justify="left",background="#1E6FBA", width=25)
		fieldSex['values'] = self.select_sex()
		for (x, item) in enumerate(fieldSex['values']):
			if item == self.sex.get():
				fieldSex.current(int(x))
		fieldSex.pack(pady=8)


		# Buttons of actions
		buttons = ttk.Frame(form, style='White.TFrame')
		buttons.pack(pady=8)
		# buttons.pack_propagate(0)
		# Guardar
		ttk.Button(buttons, command=self.save,
			text="Cancelar").pack(side=tk.LEFT, padx=8)

		# Cancelar
		ttk.Button(buttons, command=lambda : self.change_form('next'),
			text="Siguiente").pack(side=tk.LEFT, padx=8)

	def form2(self):
		form = self.content_form

		# Entrada de texto para estado_civil
		ttk.Label(form, text="Estado Civil:",
			style='Black.TLabel').place(x=0,y=130)
		self.estado_civil=tk.StringVar(form,
			value=self.viviendo.get('estado_civil') if self.viviendo else '')
		fieldState_civil = ttk.Combobox(form, state='readonly',
			textvariable=self.estado_civil, font="Helvetica 13",
			justify="left",background="#1E6FBA", width=25)
		fieldState_civil['values'] = self.select_civil_status()
		for (x, item) in enumerate(fieldState_civil['values']):
			if item == self.estado_civil.get():
				fieldState_civil.current(int(x))
		fieldState_civil.pack(pady=8)

		# Entrada de texto para postulation
		ttk.Label(form, text="Postulacion:",
			style='Black.TLabel').place(x=0,y=185)
		self.postulation=validate.MaxLengthEntry(form, style='White.TEntry',
			value=self.viviendo.get('postulation') if self.viviendo else '',
			maxlength=40, width=27, font="Helvetica 13",justify="left")
		self.postulation.pack(pady=8)

		# Entrada de texto para Direccion
		ttk.Label(form, text="Dirección:",
			style='Black.TLabel').place(x=0,y=235)
		self.direction=tk.Text(form, width=28, height=3, bd=0,
			font="Helvetica 12 normal",bg="white",fg="#6b6a6a",
			highlightbackground="grey",highlightcolor="#4FC2EB",
			highlightthickness=1)
		self.direction.insert(tk.INSERT,
			self.viviendo.get('direction') if self.viviendo else '')
		self.direction.pack(pady=8)

		self.new_direction = self.direction.get('0.0', tk.INSERT)

		# Content BOOLEANS
		booleans = ttk.Frame(form, style='White.TFrame')
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
		self.discapacity_desc = self.viviendo.get('discapacity_desc') if self.viviendo else ''
		ttk.Checkbutton(booleans, text='Discapacidad', variable=self.discapacity,
			onvalue=True, offvalue=False,
			command=lambda : self.textDialog(self.discapacity_desc)
			).pack(side=tk.LEFT, padx=5, pady=8)

		# Buttons of actions
		buttons = ttk.Frame(form, style='White.TFrame')
		buttons.pack(pady=8)
		# buttons.pack_propagate(0)
		# Guardar
		ttk.Button(buttons, command=lambda : self.change_form('back'),
			text="Atras").pack(side=tk.LEFT, padx=8)

		# Cancelar
		ttk.Button(buttons, command=lambda : self.change_form('next'),
			text="Siguiente").pack(side=tk.LEFT, padx=8)


	def form3(self):
		form = self.content_form

		# instructional_level
		ttk.Label(form, text="Niv. Instruccional:",
			style='Black.TLabel').place(x=0,y=130)
		self.instructional_level = tk.StringVar(form,
			value=self.viviendo.get('instructional_level') if self.viviendo else '')
		fieldNiv_Inst = ttk.Combobox(form, state='readonly',
		textvariable=self.instructional_level,
			font="Helvetica 13", justify="left",background="#1E6FBA", width=25)
		fieldNiv_Inst['values'] = self.select_instruccion_level()
		for (x, item) in enumerate(fieldNiv_Inst['values']):
			if item == self.instructional_level.get():
				fieldNiv_Inst.current(int(x))
		fieldNiv_Inst.pack(pady=8)

		# Entry Text For occupation
		ttk.Label(form, text="Occupacion:",
			style='Black.TLabel').place(x=0,y=185)
		self.occupation=validate.MaxLengthEntry(form, style='White.TEntry',
			value=self.viviendo.get('occupation') if self.viviendo else '',
			maxlength=40, width=27, font="Helvetica 13",justify="left")
		self.occupation.pack(pady=8)

		# Entry Text For institution
		ttk.Label(form, text="Institucion:",
			style='Black.TLabel').place(x=0,y=235)
		self.institution=validate.MaxLengthEntry(form, style='White.TEntry',
			value=self.viviendo.get('institution') if self.viviendo else '',
			maxlength=40, width=27, font="Helvetica 13",justify="left")
		self.institution.pack(pady=8)

		# Buttons of actions
		buttons = ttk.Frame(form, style='White.TFrame')
		buttons.pack(pady=8)
		# buttons.pack_propagate(0)
		# Guardar
		ttk.Button(buttons, command=lambda : self.change_form('back'),
			text="Atras").pack(side=tk.LEFT, padx=8)

		# Cancelar
		ttk.Button(buttons, command=self.save,
			text="Guardar").pack(side=tk.LEFT, padx=8)
