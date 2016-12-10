#!/usr/bin/python
# -*- coding: utf-8 -*-

import Tkinter as tk
import ttk
from utils import validate
from utils.methods import Methods
from views.forms.user import login
from views.generic.successes import SuccessesView
from database.main import UserModel

class RegisterForm(tk.Frame, Methods):
	def __init__(self, root, **kwargs):
		tk.Frame.__init__(self, root)
		self.root = root
		self.db = UserModel()

		self.user = {}
		self.passwd = None
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

		self.form()

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

	def form(self):
		div = tk.Frame(self.root, height=550, background="grey", relief=tk.RAISED)
		div.pack(expand=True, fill=tk.X)
		div.pack_propagate(0)

		form = tk.Frame(div, width=650, relief=tk.RAISED)
		form.pack(expand=True, fill=tk.Y)
		form.pack_propagate(0)

		# Title of the Form
		tk.Label(form, text="Iniciar Sesion", font="Helvetica 16 bold",
			fg="blue").pack(pady=20)

		# Entry of the username
		tk.Label(form, text="Nombre de usuario:", font="Helvetica 10",
			fg="#474747").place(x=83,y=78)

		self.username=validate.MaxLengthEntry(form, maxlength=40,
			value=self.user['username'] if self.user else '',
			width=27, font="Helvetica 13",justify="left")
		self.username.focus()
		self.username.pack(pady=8)

		# Entry of the first_name
		tk.Label(form, text="Nombre:", font="Helvetica 10",
			fg="#474747").place(x=145,y=118)

		self.first_name=validate.MaxLengthEntry(form, maxlength=40,
			value=self.user['first_name'] if self.user else '',
			width=27, font="Helvetica 13",justify="left")
		self.first_name.pack(pady=8)

		# Entry of the last_name
		tk.Label(form, text="Apellido:", font="Helvetica 10",
			fg="#474747").place(x=140,y=158)

		self.last_name=validate.MaxLengthEntry(form, maxlength=40,
			value=self.user['last_name'] if self.user else '',
			width=27, font="Helvetica 13",justify="left")
		self.last_name.pack(pady=8)

		# Entry of the cedula
		tk.Label(form, text="CI:", font="Helvetica 10",
			fg="#474747").place(x=176,y=198)

		self.ci=validate.IntegerEntry(form,
			value=self.user['cedula'] if self.user else 0,
			width=27, font="Helvetica 13",justify="left")
		self.ci.pack(pady=8)

		# Entrada de texto para permissions
		tk.Label(form, text="Permisos:", font="Helvetica 10",
			fg="#474747").place(x=135,y=239)
		self.permissions=tk.StringVar(form,
			value=self.user['permission'] if self.user else '')
		fieldPermissions = ttk.Combobox(form, state='readonly',
			textvariable=self.permissions, font="Helvetica 13",
			justify="left",background="#1E6FBA", width=25)
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

		# Entry of the password
		tk.Label(form, text="Contraseña:", font="Helvetica 10",
			fg="#474747").place(x=125,y=320)

		self.password=validate.MaxLengthEntry(form, show="*", maxlength=40,
			value=self.passwd if self.passwd else '',
			width=27, font="Helvetica 13",justify="left")
		self.password.pack(pady=8)

		# Entry of the password repeat
		tk.Label(form, text="Repita Contraseña:", font="Helvetica 10",
			fg="#474747").place(x=83,y=360)

		self.password2=validate.MaxLengthEntry(form, show="*", maxlength=40,
			value=self.passwd if self.passwd else '',
			width=27, font="Helvetica 13",justify="left")
		self.password2.pack(pady=8)

		# Buttons of actions
		buttons = tk.Frame(form,  relief=tk.RAISED)
		buttons.pack(pady=8)
		# buttons.pack_propagate(0)
		# Create Account
		ttk.Button(buttons, command=self.save, text="Crear Cuenta",
			width=13).pack(padx=8)

