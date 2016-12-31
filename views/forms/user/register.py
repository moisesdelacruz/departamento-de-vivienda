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
		self.form_actually = 1

		if self.kwargs.get('action'):
			self.action = self.kwargs.get('action')
			self._actions()

		# show contents
		self.show()

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
			self.data = self.controller.get_session()
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
				self.clean(self.root)
				user.users_list.UsersListDetail(self.root, self.controller)
			else:
				data['user_id'] = self.data.get('user_id')
				self.db.update(data)
				self.clean(self.root)
				if self.action == 'edit_me':
					# if action is edit my profile, then update the session
					self.controller.update_session()
					self.data = self.controller.get_session()
					user.profile.ProfileView(self.root, self.controller)
				else:
					user.users_list.UsersListDetail(self.root, self.controller)

		else:
			self.set_error('Contraseñas no coinciden')


	# def _format(self):
	# 	return ({
	# 		"username": self.username.get(),
	# 		"first_name": self.first_name.get(),
	# 		"last_name": self.last_name.get(),
	# 		"cedula": int(self.ci.get()),
	# 		"permission": self.permissions.get(),
	# 		"is_superuser": bool(self.is_superuser.get())
	# 	})


	# def data_state(self):
	# 	self.data = self._format()


	def validate(self):
		required_list = ['username', 'ci', 'permissions',
			'password', 'password2']
		for item in required_list:
			if hasattr(self, item):
				if not len(eval('self.%s.get()' %(item))) > 3:
					self.set_error('%s es requerido para continuar' %(item))
					return False
					break
			else: pass
		return True

	def change_form(self, action):
		if action == 'next' and self.validate():
			self.form_actually += 1
			self.render()
		elif action == 'back' and self.validate():
			self.form_actually -= 1
			self.render()
		elif action == 'render':
			self.render()

	def show(self):
		# contents
		div = ttk.Frame(self.root, height=550, padding=20,
			style='Kim.TFrame')
		div.pack(expand=True, fill=tk.X)
		div.pack_propagate(0)

		self.content_form = ttk.Frame(div, width=650,
			style="Kim.TFrame")
		self.content_form.pack(expand=True, fill=tk.Y)
		self.content_form.pack_propagate(0)

		# render form
		self.change_form('render')

	def render(self):
		self.clean(self.content_form)
		if hasattr(self, eval("'form%s'" %(str(self.form_actually)))):
			# Title of the Form
			ttk.Label(self.content_form, text="Editar Usuario",
				style="Title.TLabel").pack(anchor=tk.NW)
			# message about password
			ttk.Label(self.content_form,
				text="Elija una contraseña que sea fácil"+
					"de recordar pero difícil de adivinar."+
					"\nSi te olvidas, mostraremos la pista",
				style="Text.TLabel").pack(anchor=tk.NW, pady=15)
			# render form
			eval('self.form%s()' %(str(self.form_actually)))
			# content message
			self.content_message = ttk.Frame(self.content_form,
				style='Kim.TFrame')
			self.content_message.pack(pady=8)

	def cancel(self):
		if hasattr(self, 'action'):
			if self.action == 'edit_me':
				self.clean(self.root)
				user.profile.ProfileView(self.root, self.controller)

	def set_error(self, err):
		self.clean(self.content_message)
		ttk.Label(self.content_message,
			text=err, style='Error.TLabel').pack()


	def form1(self):

		# Entry of the username
		ttk.Label(self.content_form, text="Nombre de usuario",
			style="TLabel").place(x=0,y=130)

		self.username=validate.MaxLengthEntry(
			self.content_form, maxlength=40, justify="left",
			value=self.data.get('username') if self.data else '',
			style="Kim.TEntry", width=22, font="Helvetica 14")
		self.username.focus()
		self.username.pack(pady=8)

		# Entry of the first_name
		ttk.Label(self.content_form, text="Nombre",
			style="TLabel").place(x=0,y=185)

		self.first_name=validate.MaxLengthEntry(
			self.content_form, maxlength=40, justify="left",
			value=self.data.get('first_name') if self.data else '',
			style="Kim.TEntry", width=22, font="Helvetica 14")
		self.first_name.pack(pady=8)

		# Entry of the last_name
		ttk.Label(self.content_form,
			text="Apellido", style="TLabel").place(x=0,y=240)

		self.last_name=validate.MaxLengthEntry(
			self.content_form, maxlength=40, justify="left",
			value=self.data.get('last_name') if self.data else '',
			style="Kim.TEntry", width=22, font="Helvetica 14")
		self.last_name.pack(pady=8)

		# Entry of the cedula
		ttk.Label(self.content_form, text="Cedula de Identidad",
			style="TLabel").place(x=0,y=295)

		self.ci=validate.IntegerEntry(self.content_form, maxlength=9,
			value=self.data.get('cedula') if self.data else 0,
			style="Kim.TEntry", width=22, font="Helvetica 14",
			justify="left")
		self.ci.pack(pady=8)

		# permissions fields
		self.permissions=tk.StringVar(self.content_form,
			value=self.data.get('permission') if self.data else '')
		# is superuser
		self.is_superuser = tk.BooleanVar(self.content_form,
			value=self.data.get('is_superuser') if self.data else False)
		# if is superuser pass
		if self.controller.get_session().get('is_superuser'):
			# Entrada de texto para permissions
			ttk.Label(self.content_form, text="Permisos",
				style="TLabel").place(x=0,y=345)
			fieldPermissions = ttk.Combobox(
				self.content_form, state='readonly', style="TCombobox",
				textvariable=self.permissions, font="Helvetica 14",
				justify="left",background="#1E6FBA", width=21)
			fieldPermissions['values'] = self.selectPermissions()
			for (x, item) in enumerate(fieldPermissions['values']):
				if item == self.permissions.get():
					fieldPermissions.current(int(x))
			fieldPermissions.pack(pady=8)

			# is superuser
			ttk.Checkbutton(self.content_form, text='Superusuario',
				variable=self.is_superuser, onvalue=True,
				offvalue=False).pack(pady=8)

		# Buttons of actions
		buttons = tk.Frame(self.content_form,
			background="#012D5A", relief=tk.RAISED)
		buttons.pack(pady=8)
		# Create Account
		ttk.Button(buttons, command=self.cancel, text="Cancelar",
			width=13).pack(side=tk.LEFT, padx=10)

		ttk.Button(buttons,
			command=lambda : self.change_form('next'), text="Siguiente",
			width=13).pack(side=tk.LEFT, padx=10)


	def form2(self):

		# Entry of the password
		ttk.Label(self.content_form, text="Contraseña",
			style="TLabel").place(x=0,y=130)

		self.password=validate.MaxLengthEntry(
			self.content_form, show="*", maxlength=40,
			value=self.passwd if self.passwd else '',
			style="Kim.TEntry", width=22, font="Helvetica 14",
			justify="left")
		self.password.pack(pady=8)

		# Entry of the password repeat
		ttk.Label(self.content_form, text="Repita Contraseña",
			style="TLabel").place(x=0,y=185)

		self.password2=validate.MaxLengthEntry(
			self.content_form, show="*", maxlength=40,
			value=self.passwd if self.passwd else '',
			style="Kim.TEntry", width=22, font="Helvetica 14",
			justify="left")
		self.password2.pack(pady=8)

		# Buttons of actions
		buttons = tk.Frame(self.content_form,
			background="#012D5A", relief=tk.RAISED)
		buttons.pack(pady=8)
		# Create Account
		ttk.Button(buttons,
			command=lambda : self.change_form('back'), text="Atras",
			width=13).pack(side=tk.LEFT, padx=10)

		ttk.Button(buttons, command=self.save, text="Guardas",
			width=13).pack(side=tk.LEFT, padx=10)
