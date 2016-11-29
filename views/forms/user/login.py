#!/usr/bin/python
# -*- coding: utf-8 -*-

import Tkinter as tk
import ttk
from utils import validate
from utils.methods import Methods
from views.forms import user
from database.main import UserModel

class LoginForm(tk.Frame, Methods):
	def __init__(self, root, control):
		tk.Frame.__init__(self, root)
		self.root = root
		self.control = control
		self.db = UserModel()
		self.session = []
		self.form()

	def login(self):
		query = self.db.retrive(str(self.username.get()), field='username')
		if query:
			if self.password.get():
				password_decrypt = self.decrypt(query[0][7])
				if password_decrypt == self.password.get():
					self.session = ({
						"user_id": query[0][0],
						"username": query[0][1],
						"first_name": query[0][2],
						"last_name": query[0][3],
						"cedula": query[0][4],
						"is_superuser": query[0][5],
						"permission": query[0][6]
					})
					print self.session
					self.control.set(self.session)
				else: print 'password does not match with username'
			else: print 'debe ingresar una contraseña'
		else: print 'username no exist'
		

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

		# Entry of the password
		tk.Label(form, text="Contraseña:", font="Helvetica 10",
			fg="#474747").place(x=125,y=118)

		self.password=validate.MaxLengthEntry(form, show="*", maxlength=40,
			width=22, bd=0, font="Helvetica 14 normal",justify="left",
			bg="white",fg="#6b6a6a", highlightbackground="black",
			highlightcolor="red", highlightthickness=0)
		self.password.pack(pady=8)

		# Buttons of actions
		buttons = tk.Frame(form,  relief=tk.RAISED)
		buttons.pack(pady=8)
		# buttons.pack_propagate(0)
		# Login
		tk.Button(buttons, command=self.login, text="Iniciar Sesion",
			font="Helvetica 12 bold", bd=0, activebackground="red",
			activeforeground="blue", bg="green", fg="white", width=13,
			height=2).pack(side=tk.LEFT, padx=8)