#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import Tkinter as tk
import ttk

from datetime import datetime
from utils.methods import Methods
from utils import validate, entrydate
from database.main import FamilyModel
from views import detail

class Grupo_familiarForm(tk.Frame, Methods):
	def __init__(self, root, controller, viviendo_id, **kwargs):
		tk.Frame.__init__(self, root)
		self.root = root
		self.controller = controller
		# id from viviendo
		self.viviendo_id = viviendo_id
		# instance database
		self.db = FamilyModel()
		# data actually
		self.data = ({})
		# edit mode unavailable
		self.edit = False
		# state actual of the form
		self.form_actually = 1

		if kwargs.get('action'):
			self.action = kwargs.get('action')
			self._actions(kwargs)

		self.show()


	def _actions(self, kwargs):
		if self.action == 'edit':
			if not kwargs.get('data'):
				raise ValueError("This action requires a 'data' attribute")
			# title of window
			self.controller.parent.title('Editar Familiar')
			self.data = kwargs.get('data')
			self.data_id = self.data.get('id')
			# edit mode available
			self.edit = True

		# action unknown
		else:
			raise ValueError(' '.join([self.action,
				'This action is not valid.']))


	def save(self):
		data = self._format()

		if not self.edit:
			self.db.create(data)
			# clean
			self.clean(self.root)
			# clean render
			view = detail.grupo_familiar.Grupo_familiarDetail(self.root,
				self.controller, self.viviendo_id)
		elif self.edit:
			data['id'] = self.data_id
			self.db.update(data)
			# clean
			self.clean(self.root)
			# render view
			view = detail.grupo_familiar.Grupo_familiarDetail(self.root,
				self.controller, self.viviendo_id)

	def _format(self):
		fields = [{'int': 'viviendo_id'}, {'str': 'nationality'}, {'int': 'ci'},
			{'str': 'first_name'}, {'str': 'last_name'}, {'str': 'birthday'},
			{'str': 'sex'}, {'str': 'estado_civil'}, {'str': 'instructional_level'},
			{'bool': 'work'}, {'str': 'occupation'}, {'str': 'institution'},
			{'float': 'entry'}, {'str': 'birth_state'}, {'bool': 'discapacity'},
			{'str': 'discapacity_desc'}, {'bool': 'old_age'}]

		data = ({})
		for field in fields:
			for key, value in field.items():
				if (value != 'viviendo_id' and value != 'entry'
					and value != 'discapacity_desc'):
					data[value] = eval(
						key+'(self.'+value+'.get())') if hasattr(
						self, value) else self.data.get(value)
				else:
					data[value] = eval(
						key+'(self.'+value+')') if hasattr(
						self, value) else self.data.get(value)
		return data

	def state_data(self):
		self.data = self._format()

	def validate(self):
		required_list = [{'Nacionalidad': 'nationality'}, {'Cedula': 'ci'},
			{'Nombre': 'first_name'}, {'Apellido': 'last_name'}, {'Sexo': 'sex'}]
		for field in required_list:
			for message, name in field.items():
				if hasattr(self, name):
					if not bool(eval('self.%s.get()' %(name))):
						self.set_error('%s es requerido para continuar' %(message))
						return False
						break
					if name == 'ci' and len(self.ci.get()) < 7:
						self.set_error('%s debe tener al menos siete digitos para continuar' %(message))
						return False
						break
				else: pass
		return True

	def change_form(self, action):
		if action == 'next' and self.validate():
			self.form_actually += 1
			self.state_data()
			self.render()
		elif action == 'back' and self.validate():
			self.form_actually -= 1
			self.state_data()
			self.render()
		elif action == 'render':
			self.render()

	def set_error(self, err):
		self.clean(self.content_message)
		ttk.Label(self.content_message,
			text=err, style='Error.TLabel').pack()

	def render(self):
		# clean content form
		self.clean(self.content_form)

		if hasattr(self, eval("'form%s'" %(str(self.form_actually)))):
			# Title of the Form
			ttk.Label(self.content_form,
				text="Editar Familiar" if self.edit else "Registrar Familiar",
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

	def show(self):
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
		form=self.content_form

		# Nacionalidad
		ttk.Label(form, text='Nacionalidad',
			style='Black.TLabel').place(x=0, y=130)
		self.nationality = tk.StringVar(form,
			value=self.data.get('nationality')
				if self.data.get('nationality') else '')
		fieldNationality = ttk.Combobox(form, state='readonly',
			textvariable=self.nationality, font="Helvetica 13", justify="left",
			background="#1E6FBA", width=25)
		fieldNationality['values'] = self.select_nationality()
		for (x, item) in enumerate(fieldNationality['values']):
			if item == self.nationality.get():
				fieldNationality.current(int(x))
		fieldNationality.focus()
		fieldNationality.pack(pady=8)

		# Entry of the cedula
		ttk.Label(form,text="CI",
			style='Black.TLabel').place(x=0,y=180)
		self.ci=validate.IntegerEntry(form, value=self.data.get('ci')
				if self.data.get('ci') else 0, maxlength=9,
			style='White.TEntry', width=27,
			font="Helvetica 13", justify="left")
		self.ci.pack(pady=8)

		# Entry of first_name
		ttk.Label(form,text="Nombre",
			style='Black.TLabel').place(x=0,y=230)
		self.first_name=validate.MaxLengthEntry(form,
			value=self.data.get('first_name')
				if self.data.get('first_name') else '',
			style='White.TEntry', maxlength=30,width=27,
			font="Helvetica 13",justify="left")
		self.first_name.pack(pady=8)

		# Entry of last_name
		ttk.Label(form,text="Apellido",
			style='Black.TLabel').place(x=0,y=275)
		self.last_name=validate.MaxLengthEntry(form,
			value=self.data.get('last_name')
				if self.data.get('last_name') else '',
			style='White.TEntry', maxlength=30, width=27,
			font="Helvetica 13", justify="left")
		self.last_name.pack(pady=8)

		# Entry birthday
		ttk.Label(form, text="Fecha de Nacimiento",
			style='Black.TLabel').place(x=0,y=330)

		actually = (self.data.get('birthday')
			if self.data.get('birthday') else None)

		self.birthday=entrydate.DateEntry(form, actually=actually,
			style='White.TEntry', font="Helvetica 13")
		self.birthday.pack(pady=8)

		# Sex
		ttk.Label(form, text="Sexo:",
			style='Black.TLabel').place(x=0,y=380)
		self.sex = tk.StringVar(form,
			value=self.data.get('sex') if self.data.get('sex') else '')
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
		# back
		ttk.Button(buttons,
			text="Cancelar").pack(side=tk.LEFT, padx=8)

		# next
		ttk.Button(buttons, command=lambda : self.change_form('next'),
			text="Siguiente").pack(side=tk.LEFT, padx=8)

	def form2(self):
		form = self.content_form

		# Entrada de texto para estado_civil
		ttk.Label(form, text="Estado Civil:",
			style='Black.TLabel').place(x=0,y=135)
		self.estado_civil=tk.StringVar(form,
			value=self.data.get('estado_civil')
				if self.data.get('estado_civil') else '')
		fieldState_civil = ttk.Combobox(form, state='readonly',
			textvariable=self.estado_civil, font="Helvetica 13",
			justify="left",background="#1E6FBA", width=25)
		fieldState_civil['values'] = self.select_civil_status()
		for (x, item) in enumerate(fieldState_civil['values']):
			if item == self.estado_civil.get():
				fieldState_civil.current(int(x))
		fieldState_civil.pack(pady=8)

		# instructional_level
		ttk.Label(form, text="Niv. Instruccional:",
			style='Black.TLabel').place(x=0,y=185)
		self.instructional_level = tk.StringVar(form,
			value=self.data.get('instructional_level')
				if self.data.get('instructional_level') else '')
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
			style='Black.TLabel').place(x=0,y=230)
		self.occupation=validate.MaxLengthEntry(form, style='White.TEntry',
			value=self.data.get('occupation')
				if self.data.get('occupation') else '',
			maxlength=40, width=27, font="Helvetica 13",justify="left")
		self.occupation.pack(pady=8)

		# Entry Text For institution
		ttk.Label(form, text="Institucion:",
			style='Black.TLabel').place(x=0,y=280)
		self.institution=validate.MaxLengthEntry(form, style='White.TEntry',
			value=self.data.get('institution')
				if self.data.get('institution') else '',
			maxlength=40, width=27, font="Helvetica 13",justify="left")
		self.institution.pack(pady=8)

		# Entry birth_state
		ttk.Label(form,text="Estado de Nacimiento",
			style='Black.TLabel').place(x=0,y=335)
		self.birth_state=validate.MaxLengthEntry(form,
			value=self.data.get('birth_state')
				if self.data.get('birth_state') else '',
			style='White.TEntry', maxlength=30, width=27,
			font="Helvetica 13", justify="left")
		self.birth_state.pack(pady=8)

		# Booleans Fields
		# Content BOOLEANS
		booleans = ttk.Frame(form, style='White.TFrame')
		booleans.pack(pady=2)

		# Entry of tercera edad
		self.old_age=tk.BooleanVar(booleans,
			value=self.data.get('old_age') if self.data.get('old_age') else False)
		ttk.Checkbutton(booleans, text='Tercera edad', variable=self.old_age,
			onvalue=True, offvalue=False).pack(side=tk.LEFT, padx=5, pady=8)

		# Entry of discapacity
		self.discapacity_desc=(self.data.get('discapacity_desc')
			if self.data.get('discapacity_desc') else '')
		self.discapacity=tk.BooleanVar(booleans,
			value=self.data.get('discapacity')
				if self.data.get('discapacity') else False)
		ttk.Checkbutton(booleans, text='Discapacidad', variable=self.discapacity,
			onvalue=True, offvalue=False,
			command=lambda : self.textDialog(self.discapacity_desc)
			).pack(side=tk.LEFT, padx=5, pady=8)

		# Boolean of work
		self.entry=self.data.get('entry') if self.data.get('entry') else 0
		self.work=tk.BooleanVar(booleans,
			value=self.data.get('work') if self.data.get('work') else False)
		ttk.Checkbutton(booleans, text='Trabaja', variable=self.work,
			onvalue=True, offvalue=False,
			command=lambda : self.floatDialog(self.entry)
			).pack(side=tk.LEFT, padx=5, pady=8)

		# Buttons of actions
		buttons = ttk.Frame(form, style='White.TFrame')
		buttons.pack(pady=8)
		# Guardar
		ttk.Button(buttons, command=lambda : self.change_form('back'),
			text="Atras").pack(side=tk.LEFT, padx=8)

		# Cancelar
		ttk.Button(buttons, command=self.save,
			text="Guardar Cambios" if self.edit else "Guardar"
			).pack(side=tk.LEFT, padx=8)
