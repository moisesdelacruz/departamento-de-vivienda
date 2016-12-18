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
	def __init__(self, root, controller, **kwargs):
		tk.Frame.__init__(self, root)
		self.root = root
		self.controller = controller
		self.kwargs = kwargs
		# instance database
		self.db = UserModel()

		# set default title
		self.controller.parent.title('Nuevo Usuario')

		self.data = {}
		self.passwd = None

		if self.kwargs.get('action'):
			self.action = self.kwargs.get('action')
			self._actions()

		self.render()


	def _actions(self):
		# edit user
		if self.action == 'edit_user':
			if not self.kwargs.get('data'):
				raise ValueError("This action requires a 'data' attribute")
			# title of window
			self.controller.parent.title('Editar Usuario')
			# data = data without format. self.data = data with format.
			self.data = self.kwargs.get('data')
			self.passwd = self.decrypt(self.data.get('password'))
		# edit my user
		elif self.action == 'edit_me':
			# title of the window
			self.controller.parent.title('Editar Mi Perfil')
			# instance of dates
			self.data = self.controller.content_session
			self.passwd = self.decrypt(self.data.get('password'))
		# action unknown
		else:
			raise ValueError(self.action+'This action is not valid.')


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

			if not hasattr(self, 'action'):
				self.db.create(data)
				successes = SuccessesView(self.root, message='Usuario Creado')
			else:
				data['user_id'] = self.data.get('user_id')
				self.db.update(data)
				if self.action == 'edit_me':
					self.controller.update_session()
				successes = SuccessesView(self.root, message='Usuario Editado')

		else:
			self.alert('Alerta Contraseña', 'Contraseñas no coinciden')

	def next(self):
		self.clean(self.content_form)
		self.form2()

	def back(self):
		self.clean(self.content_form)
		self.form1()

	def cancel(self):
		if hasattr(self, 'action'):
			if self.action == 'edit_me':
				self.clean(self.root)
				user.profile.ProfileView(self.root, self.controller)

	def render(self):
		# contents
		div = ttk.Frame(self.root, height=550, padding=20,
			style='Kim.TFrame')
		div.pack(expand=True, fill=tk.X)
		div.pack_propagate(0)

		self.content_form = ttk.Frame(div, width=650,
			style="Kim.TFrame")
		self.content_form.pack(expand=True, fill=tk.Y)
		self.content_form.pack_propagate(0)

		self.form1()

	def form1(self):
		form = self.content_form

		# Title of the Form
		ttk.Label(form, text="Editar Usuario" if self.data else "Nuevo Usuario",
			style="Title.TLabel").pack(anchor=tk.NW)
		# message about password
		ttk.Label(form, text="Elija una contraseña que sea fácil"+
				"de recordar pero difícil de adivinar."+
				"\nSi te olvidas, mostraremos la pista",
			style="Text.TLabel").pack(anchor=tk.NW, pady=15)

		# Entry of the username
		ttk.Label(form, text="Nombre de usuario",
			style="TLabel").place(x=0,y=130)

		self.username=validate.MaxLengthEntry(form, maxlength=40,
			value=self.data.get('username') if self.data else '',
			style="Kim.TEntry", width=22, font="Helvetica 14",
			justify="left")
		self.username.focus()
		self.username.pack(pady=8)

		# Entry of the first_name
		ttk.Label(form, text="Nombre", style="TLabel").place(x=0,y=185)

		self.first_name=validate.MaxLengthEntry(form, maxlength=40,
			value=self.data.get('first_name') if self.data else '',
			style="Kim.TEntry", width=22, font="Helvetica 14",
			justify="left")
		self.first_name.pack(pady=8)

		# Entry of the last_name
		ttk.Label(form, text="Apellido", style="TLabel").place(x=0,y=240)

		self.last_name=validate.MaxLengthEntry(form, maxlength=40,
			value=self.data.get('last_name') if self.data else '',
			style="Kim.TEntry", width=22, font="Helvetica 14",
			justify="left")
		self.last_name.pack(pady=8)

		# Entry of the cedula
		ttk.Label(form, text="Cedula de Identidad",
			style="TLabel").place(x=0,y=295)

		self.ci=validate.IntegerEntry(form,
			value=self.data.get('cedula') if self.data else 0,
			style="Kim.TEntry", width=22, font="Helvetica 14",
			justify="left")
		self.ci.pack(pady=8)

		# permissions fields
		self.permissions=tk.StringVar(form,
			value=self.data.get('permission') if self.data else '')
		# is superuser
		self.is_superuser = tk.BooleanVar(form,
			value=self.data.get('is_superuser') if self.data else False)
		# if is superuser pass
		if self.controller.get_session().get('is_superuser'):
			# Entrada de texto para permissions
			ttk.Label(form, text="Permisos",
				style="TLabel").place(x=0,y=345)
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
		form = self.content_form

		# Title of the Form
		ttk.Label(form, text="Editar Usuario", style="Title.TLabel").pack(anchor=tk.NW)
		# message about password
		ttk.Label(form, text="Elija una contraseña que sea fácil"+
				"de recordar pero difícil de adivinar."+
				"\nSi te olvidas, mostraremos la pista",
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
