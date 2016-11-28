#!/usr/bin/python
# -*- coding: utf-8 -*-

import Tkinter as tk
import ttk
from utils import validate
from utils.methods import Methods
from views.forms.user import login
from database.main import UserModel

class RegisterForm(tk.Frame, Methods):
	def __init__(self, root):
		tk.Frame.__init__(self, root)
		self.root = root
		self.db = UserModel()
		self.form()

	def save(self):
		if self.password.get() == self.password2.get():
			data = ({
				"username": self.username.get(),
				"first_name": self.first_name.get(),
				"last_name": self.last_name.get(),
				"cedula": int(self.ci.get()),
				"permission": self.permissions.get(),
				"password": self.password.get()
			})
			print data
			self.db.create(data)
		else:
			print "Password does not match"

	def login(self):
		self.clean(self.root)
		login.LoginForm(self.root)

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
			width=22, bd=0, font="Helvetica 14 normal",justify="left",
			bg="white",fg="#6b6a6a", highlightbackground="black",
			highlightcolor="red", highlightthickness=0)
		self.username.pack(pady=8)

		# Entry of the first_name
		tk.Label(form, text="Nombre:", font="Helvetica 10",
			fg="#474747").place(x=145,y=118)

		self.first_name=validate.MaxLengthEntry(form, maxlength=40,
			width=22, bd=0, font="Helvetica 14 normal",justify="left",
			bg="white",fg="#6b6a6a", highlightbackground="black",
			highlightcolor="red", highlightthickness=0)
		self.first_name.pack(pady=8)

		# Entry of the last_name
		tk.Label(form, text="Apellido:", font="Helvetica 10",
			fg="#474747").place(x=140,y=158)

		self.last_name=validate.MaxLengthEntry(form, maxlength=40,
			width=22, bd=0, font="Helvetica 14 normal",justify="left",
			bg="white",fg="#6b6a6a", highlightbackground="black",
			highlightcolor="red", highlightthickness=0)
		self.last_name.pack(pady=8)

		# Entry of the cedula
		tk.Label(form, text="CI:", font="Helvetica 10",
			fg="#474747").place(x=176,y=198)

		self.ci=validate.IntegerEntry(form,
			width=22, bd=0, font="Helvetica 14 normal",justify="left",
			bg="white",fg="#6b6a6a", highlightbackground="black",
			highlightcolor="red", highlightthickness=0)
		self.ci.pack(pady=8)

		# Entrada de texto para permissions
		tk.Label(form, text="Permisos:", font="Helvetica 10",
			fg="#474747").place(x=135,y=239)
		self.permissions=tk.StringVar(form)
		fieldPermissions = ttk.Combobox(form, state='readonly',
			textvariable=self.permissions, font="Helvetica 13",
			justify="left",background="#1E6FBA", width=25)
		fieldPermissions['values'] = self.selectPermissions()
		fieldPermissions.current(0)
		for (x, item) in enumerate(fieldPermissions['values']):
			if item == self.permissions.get():
				fieldPermissions.current(int(x))
		fieldPermissions.pack(pady=8)

		# Entry of the password
		tk.Label(form, text="Contraseña:", font="Helvetica 10",
			fg="#474747").place(x=125,y=280)

		self.password=validate.MaxLengthEntry(form, maxlength=40,
			width=22, bd=0, font="Helvetica 14 normal",justify="left",
			bg="white",fg="#6b6a6a", highlightbackground="black",
			highlightcolor="red", highlightthickness=0)
		self.password.pack(pady=8)

		# Entry of the password repeat
		tk.Label(form, text="Repita Contraseña:", font="Helvetica 10",
			fg="#474747").place(x=83,y=320)

		self.password2=validate.MaxLengthEntry(form, maxlength=40,
			width=22, bd=0, font="Helvetica 14 normal",justify="left",
			bg="white",fg="#6b6a6a", highlightbackground="black",
			highlightcolor="red", highlightthickness=0)
		self.password2.pack(pady=8)

		# Buttons of actions
		buttons = tk.Frame(form,  relief=tk.RAISED)
		buttons.pack(side=tk.RIGHT, pady=8)
		# buttons.pack_propagate(0)
		# Create Account
		tk.Button(buttons, command=self.save, text="Crear Cuenta",
			font="Helvetica 12 bold", bd=0, activebackground="red",
			activeforeground="blue", bg="green", fg="white", width=13,
			height=2).pack(side=tk.LEFT, padx=8)

		# Login
		tk.Button(buttons, command=self.login, text="Iniciar Sesion",
			font="Helvetica 12 bold", bd=0, activebackground="red",
			activeforeground="blue", bg="grey", fg="white", width=13,
			height=2).pack(side=tk.LEFT, padx=8)

