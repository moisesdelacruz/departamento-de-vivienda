#!/usr/bin/python
# -*- coding: utf-8 -*-

import Tkinter as tk
import ttk
from utils import validate
from utils.methods import Methods
from views.forms.user import login
from views.generic.successes import SuccessesView
from views.detail import user 
from database.main import UserModel

class RegisterForm(tk.Frame, Methods):
	def __init__(self, root, **kwargs):
		tk.Frame.__init__(self, root)
		self.root = root
		self.db = UserModel()

		self.user = {}
		self.passwd = None

		# contents
		div = ttk.Frame(self.root, height=550, padding=20,
			style='Kim.TFrame')
		div.pack(expand=True, fill=tk.X)
		div.pack_propagate(0)

		self._form = ttk.Frame(div, width=650,
			style="Kim.TFrame")
		self._form.pack(expand=True, fill=tk.Y)
		self._form.pack_propagate(0)

		# edit
		if kwargs.get('user'):
			# user_wof = user without format
			user_wof = kwargs.get('user')
			self.user = self.format_list(user_wof)
			self.passwd = self.decrypt(user_wof[7])
		elif kwargs.get('session'):
			self.session = kwargs.get('session')
			self.user = self.session.content_session
			self.passwd = self.decrypt(self.user.get('password'))

		self.form1()

	def format_list(self, data):
		return ({
			"user_id": data[0],
			"username": data[1],
			"first_name": data[2],
			"last_name": data[3],
			"full_name": ' '.join([data[2], data[3]]),
			"cedula": data[4],
			"is_superuser": data[5],
			"permission": data[6],
			"password": data[7],
		})

	def save(self):
		if self.password.get() == self.password2.get():
			password_encrypt = self.encrypt(self.password.get())
			data = ({
				"username": self.username.get(),
				"first_name": self.first_name.get(),
				"last_name": self.last_name.get(),
				"cedula": int(self.ci.get()),
				"permission": self.permissions.get(),
				"is_superuser": bool(self.is_superuser.get()),
				"password": password_encrypt
			})

			if not self.user:
				self.db.create(data)
				successes = SuccessesView(self.root, message='Usuario Creado')
			else:
				data['user_id'] = self.user['user_id']
				self.db.update(data)
				if hasattr(self, 'session'):
					query = self.db.retrive(int(self.user['user_id']), field='user_id')
					user = self.format_list(query[0])
					self.session.content_session = user

				successes = SuccessesView(self.root, message='Usuario Editado')


		else:
			self.alert('Alerta Contraseña', 'Contraseñas no coinciden')

	def next(self):
		self.clean(self._form)
		self.form2()

	def back(self):
		self.clean(self._form)
		self.form1()

	def cancel(self):
		if hasattr(self, 'session'):
			self.clean(self.root)
			user.profile.ProfileView(self.root, session=self.session)

	def form1(self):
		form = self._form

		# Title of the Form
		ttk.Label(form, text="Editar Usuario" if self.user else "Nuevo Usuario",
			style="Title.TLabel").pack(anchor=tk.NW)
		# message about password
		ttk.Label(form, text="Elija una contraseña que sea fácil de recordar pero difícil de adivinar.\nSi te olvidas, mostraremos la pista",
			style="Text.TLabel").pack(anchor=tk.NW, pady=15)

		# Entry of the username
		ttk.Label(form, text="Nombre de usuario",
			style="TLabel").place(x=0,y=130)

		self.username=validate.MaxLengthEntry(form, maxlength=40,
			value=self.user['username'] if self.user else '',
			style="Kim.TEntry", width=22, font="Helvetica 14",
			justify="left")
		self.username.focus()
		self.username.pack(pady=8)

		# Entry of the first_name
		ttk.Label(form, text="Nombre", style="TLabel").place(x=0,y=185)

		self.first_name=validate.MaxLengthEntry(form, maxlength=40,
			value=self.user['first_name'] if self.user else '',
			style="Kim.TEntry", width=22, font="Helvetica 14",
			justify="left")
		self.first_name.pack(pady=8)

		# Entry of the last_name
		ttk.Label(form, text="Apellido", style="TLabel").place(x=0,y=240)

		self.last_name=validate.MaxLengthEntry(form, maxlength=40,
			value=self.user['last_name'] if self.user else '',
			style="Kim.TEntry", width=22, font="Helvetica 14",
			justify="left")
		self.last_name.pack(pady=8)

		# Entry of the cedula
		ttk.Label(form, text="Cedula de Identidad",
			style="TLabel").place(x=0,y=295)

		self.ci=validate.IntegerEntry(form,
			value=self.user['cedula'] if self.user else 0,
			style="Kim.TEntry", width=22, font="Helvetica 14",
			justify="left")
		self.ci.pack(pady=8)

		# Entrada de texto para permissions
		ttk.Label(form, text="Permisos",
			style="TLabel").place(x=0,y=345)
		self.permissions=tk.StringVar(form,
			value=self.user['permission'] if self.user else '')
		fieldPermissions = ttk.Combobox(form, state='readonly',
			textvariable=self.permissions, font="Helvetica 14",
			style="TCombobox",
			justify="left",background="#1E6FBA", width=21)
		fieldPermissions['values'] = self.selectPermissions()
		for (x, item) in enumerate(fieldPermissions['values']):
			if item == self.permissions.get():
				fieldPermissions.current(int(x))
		fieldPermissions.pack(pady=8)

		# is superuser
		self.is_superuser = tk.BooleanVar(form,
			value=self.user['is_superuser'] if self.user else False)
		ttk.Checkbutton(form, text='Superusuario', variable=self.is_superuser,
			onvalue=True, offvalue=False).pack(pady=8)

		# Buttons of actions
		buttons = tk.Frame(form, background="#012D5A", relief=tk.RAISED)
		buttons.pack(pady=8)
		# buttons.pack_propagate(0)
		# Create Account
		ttk.Button(buttons, command=self.cancel, text="Cancelar",
			width=13).pack(side=tk.LEFT, padx=10)

		ttk.Button(buttons, command=self.next, text="Siguiente",
			width=13).pack(side=tk.LEFT, padx=10)


	def form2(self):
		form = self._form

		# Title of the Form
		ttk.Label(form, text="Nuevo Usuario", style="Title.TLabel").pack(anchor=tk.NW)
		# message about password
		ttk.Label(form, text="Elija una contraseña que sea fácil de recordar pero difícil de adivinar.\nSi te olvidas, mostraremos la pista",
			style="Text.TLabel").pack(anchor=tk.NW, pady=15)

		# Entry of the password
		ttk.Label(form, text="Contraseña", style="TLabel").place(x=0,y=130)

		self.password=validate.MaxLengthEntry(form, show="*", maxlength=40,
			value=self.passwd if self.passwd else '',
			style="Kim.TEntry", width=22, font="Helvetica 14",
			justify="left")
		self.password.pack(pady=8)

		# Entry of the password repeat
		ttk.Label(form, text="Repita Contraseña",
			style="TLabel").place(x=0,y=185)

		self.password2=validate.MaxLengthEntry(form, show="*", maxlength=40,
			value=self.passwd if self.passwd else '',
			style="Kim.TEntry", width=22, font="Helvetica 14",
			justify="left")
		self.password2.pack(pady=8)

		# Buttons of actions
		buttons = tk.Frame(form, background="#012D5A", relief=tk.RAISED)
		buttons.pack(pady=8)
		# buttons.pack_propagate(0)
		# Create Account
		ttk.Button(buttons, command=self.back, text="Atras",
			width=13).pack(side=tk.LEFT, padx=10)

		ttk.Button(buttons, command=self.save, text="Guardas",
			width=13).pack(side=tk.LEFT, padx=10)