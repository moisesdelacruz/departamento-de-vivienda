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
		# edit mode unavailable
		self.edit = False
		# state actual of the form
		self.form_actually = 1

		if kwargs.get('action'):
			self.action = kwargs.get('action')
			self._actions(kwargs)

		self.render()


	def _actions(self, kwargs):
		if self.action == 'edit':
			if not kwargs.get('data'):
				raise ValueError("This action requires a 'data' attribute")
			# title of window
			self.controller.parent.title('Editar Familiar')
			self.data = kwargs.get('data')
			# edit mode available
			self.edit = True

		# action unknown
		else:
			raise ValueError(' '.join([self.action,
				'This action is not valid.']))


	def save(self):
		data = ({
			"viviendo_id": int(self.viviendo_id),
			"nationality": self.nationality.get(),
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
			"entry": float(self.entry),
			"birth_state": self.birth_state.get(),
			"discapacity": bool(self.discapacity.get()),
			"discapacity_desc": str(self.discapacity_desc),
			"old_age": bool(self.old_age.get())
		})

		if not self.edit:
			self.db.create(data)
			# clean
			self.clean(self.root)
			# clean render
			view = detail.grupo_familiar.Grupo_familiarDetail(self.root,
				self.controller, self.viviendo_id)
		elif self.edit:
			data['id'] = self.data.get('id')
			self.db.update(data)
			# clean
			self.clean(self.root)
			# render view
			view = detail.grupo_familiar.Grupo_familiarDetail(self.root,
				self.controller, self.viviendo_id)

	def change_form(self, action):
		self.clean(self._form)
		if action == 'next':
			self.form_actually += 1
		elif action == 'back':
			self.form_actually -= 1
		elif action == 'render':
			pass

		if hasattr(self, eval("'form%s'" %(str(self.form_actually)))):
			# Title of the Form
			ttk.Label(self._form,
				text="Editar Familiar" if self.edit else "Registrar Familiar",
				style='Black22.TLabel').pack(anchor=tk.NW)

			ttk.Label(self._form, text="Sera redirigido automaticamente"+
				"a un panel de administracion personalizado,"+
				"\nAl Presionar \"Guardar\".",
				style="Black12.TLabel").pack(anchor=tk.NW, pady=15)
			# render form
			eval('self.form%s()' %(str(self.form_actually)))
			# content message
			self.content_message = ttk.Frame(self._form,
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

		self._form = ttk.Frame(div, width=650, padding=20, style='White.TFrame')
		self._form.pack(expand=True, fill=tk.Y)
		self._form.pack_propagate(0)

		# call form1
		self.change_form('render')

	def form1(self):
		form=self._form

		# Nacionalidad
		ttk.Label(form, text='Nacionalidad',
			style='Black.TLabel').place(x=0, y=130)
		self.nationality = tk.StringVar(form,
			value=self.data.get('nationality') if self.edit else '')
		fieldNationality = ttk.Combobox(form, state='readonly',
			textvariable=self.nationality, font="Helvetica 13", justify="left",
			background="#1E6FBA", width=25)
		fieldNationality['values'] = self.select_nationality()
		for (x, item) in enumerate(fieldNationality['values']):
			if item == self.nationality.get():
				fieldNationality.current(int(x))
		fieldNationality.pack(pady=8)

		# Entry of the cedula
		ttk.Label(form,text="CI",
			style='Black.TLabel').place(x=0,y=180)
		self.ci=validate.IntegerEntry(form, value=self.data.get('ci')
				if self.edit else 0, maxlength=9,
			style='White.TEntry', width=27,
			font="Helvetica 13", justify="left")
		self.ci.focus()
		self.ci.pack(pady=8)

		# Entry of first_name
		ttk.Label(form,text="Nombre",
			style='Black.TLabel').place(x=0,y=230)
		self.first_name=validate.MaxLengthEntry(form,
			value=self.data.get('first_name') if self.edit else '',
			style='White.TEntry', maxlength=30,width=27,
			font="Helvetica 13",justify="left")
		self.first_name.pack(pady=8)

		# Entry of last_name
		ttk.Label(form,text="Apellido",
			style='Black.TLabel').place(x=0,y=275)
		self.last_name=validate.MaxLengthEntry(form,
			value=self.data.get('last_name') if self.edit else '',
			style='White.TEntry', maxlength=30, width=27,
			font="Helvetica 13", justify="left")
		self.last_name.pack(pady=8)

		# Entry birthday
		ttk.Label(form, text="Fecha de Nacimiento",
			style='Black.TLabel').place(x=0,y=330)

		actually = self.data.get('birthday') if self.edit else None

		self.birthday=entrydate.DateEntry(form, actually=actually,
			style='White.TEntry', font="Helvetica 13")
		self.birthday.pack(pady=8)

		# Sex
		ttk.Label(form, text="Sexo:",
			style='Black.TLabel').place(x=0,y=380)
		self.sex = tk.StringVar(form,
			value=self.data.get('sex') if self.edit else '')
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
		form = self._form

		# Entrada de texto para estado_civil
		ttk.Label(form, text="Estado Civil:",
			style='Black.TLabel').place(x=0,y=135)
		self.estado_civil=tk.StringVar(form,
			value=self.data.get('estado_civil') if self.edit else '')
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
			value=self.data.get('instructional_level') if self.edit else '')
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
			value=self.data.get('occupation') if self.edit else '',
			maxlength=40, width=27, font="Helvetica 13",justify="left")
		self.occupation.pack(pady=8)

		# Entry Text For institution
		ttk.Label(form, text="Institucion:",
			style='Black.TLabel').place(x=0,y=280)
		self.institution=validate.MaxLengthEntry(form, style='White.TEntry',
			value=self.data.get('institution') if self.edit else '',
			maxlength=40, width=27, font="Helvetica 13",justify="left")
		self.institution.pack(pady=8)

		# Entry birth_state
		ttk.Label(form,text="Estado de Nacimiento",
			style='Black.TLabel').place(x=0,y=335)
		self.birth_state=validate.MaxLengthEntry(form,
			value=self.data.get('birth_state') if self.edit else '',
			style='White.TEntry', maxlength=30, width=27,
			font="Helvetica 13", justify="left")
		self.birth_state.pack(pady=8)

		# Booleans Fields
		# Content BOOLEANS
		booleans = ttk.Frame(form, style='White.TFrame')
		booleans.pack(pady=2)

		# Entry of tercera edad
		self.old_age=tk.BooleanVar(booleans,
			value=self.data.get('old_age') if self.edit else False)
		ttk.Checkbutton(booleans, text='Tercera edad', variable=self.old_age,
			onvalue=True, offvalue=False).pack(side=tk.LEFT, padx=5, pady=8)

		# Entry of discapacity
		self.discapacity_desc=self.data.get('discapacity_desc') if self.edit else ''
		self.discapacity=tk.BooleanVar(booleans,
			value=self.data.get('discapacity') if self.edit else False)
		ttk.Checkbutton(booleans, text='Discapacidad', variable=self.discapacity,
			onvalue=True, offvalue=False,
			command=lambda : self.textDialog(self.discapacity_desc)
			).pack(side=tk.LEFT, padx=5, pady=8)

		# Boolean of work
		self.entry=self.data.get('entry') if self.edit else 0
		self.work=tk.BooleanVar(booleans,
			value=self.data.get('work') if self.edit else False)
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
