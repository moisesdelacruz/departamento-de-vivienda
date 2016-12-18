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
		# title of the window
		self.control.parent.title('Iniciar Sesion')
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
						"full_name": ' '.join([query[0][2], query[0][3]]),
						"cedula": query[0][4],
						"is_superuser": query[0][5],
						"permission": query[0][6],
						"password": query[0][7],
						"last_login": query[0][8],
					})
					self.control.set_session(self.session)
					self.db.update_last_login(self.session.get('user_id'))
				else: self.alert('Alerta Contraseña',
					'contraseña no coincide con el nombre de usuario')
			else: self.alert('Alerta Contraseña',
				'debe ingresar una contraseña')
		else: self.alert('Alerta Contraseña',
			'nombre de usuario no existe')


	def form(self):
		div = ttk.Frame(self.root, height=550, padding=50, style='Kim.TFrame')
		div.pack(expand=True, fill=tk.X)
		div.pack_propagate(0)

		form = ttk.Frame(div, width=650, style='Kim.TFrame')
		form.pack(expand=True, fill=tk.Y)
		form.pack_propagate(0)

		# Image
		img = self.getImage("views/images/user.png", 200, 200)
		image = tk.Label(form, image=img, fg="blue", background="#012D5A")
		image.image = img
		image.pack(pady=10)
		# Title of the Form
		tk.Label(form, text="Iniciar Sesion", fg="white", bg="#012D5A",
			font="Candara 28").pack(pady=10)

		# Entry of the username
		ttk.Label(form, text="Usuario",
			style="TLabel").place(x=90,y=310)

		self.username=validate.MaxLengthEntry(form, maxlength=40,
			value="moisesdelacruz", style="Kim.TEntry", font="Helvetica 14",
			width=25, justify="left")
		# self.username.focus()
		self.username.pack(pady=8)

		# Entry of the password
		ttk.Label(form, text="Contraseña",
			style="TLabel").place(x=90,y=365)

		password = tk.Frame(form, background="#325678", relief=tk.RAISED)
		password.pack(pady=8)
		# password.pack_propagate(0)
		self.password=validate.MaxLengthEntry(password, show="*", maxlength=40,
			value="demilovato", style="Kim.TEntry",
			width=22, font="Helvetica 14",justify="left")
		self.password.pack(side=tk.LEFT)
		# Login
		img_send = self.getImage("views/images/send.png")
		ok=tk.Button(password, command=self.login, bd=0,
			bg="#325678", image=img_send, activebackground="#012D5A")
		ok.focus()
		ok.image = img_send
		ok.pack(side=tk.LEFT)
