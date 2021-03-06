#!/usr/bin/python
# -*- coding: utf-8 -*-

import Tkinter as tk
import ttk
from utils import validate
from utils.methods import Methods
from views.forms import user
from database.main import UserModel

class LoginForm(tk.Frame, Methods):
	def __init__(self, root, controller):
		tk.Frame.__init__(self, root)
		self.root = root
		self.controller = controller
		self.db = UserModel()
		self.session = []
		# title of the window
		self.controller.parent.title('Iniciar Sesion')
		# render
		self.render()

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
					self.controller.set_session(self.session)
					self.db.update_last_login(self.session.get('user_id'))
				else: self.set_error('contraseña no coincide con el nombre de usuario')
			else: self.set_error('debe ingresar una contraseña')
		else: self.set_error('nombre de usuario no existe')

	def set_error(self, err):
		self.clean(self.content_message)
		ttk.Label(self.content_message, text=err, style='Error.TLabel').pack()


	def render(self):
		div = ttk.Frame(self.root, height=550, padding=50, style='Kim.TFrame')
		div.pack(expand=True, fill=tk.X)
		div.pack_propagate(0)

		self.content_form = ttk.Frame(div, width=650, style='Kim.TFrame')
		# self.content_form.bind_class("<Return>", (lambda event: self.login()))
		self.content_form.pack(expand=True, fill=tk.Y)
		self.content_form.pack_propagate(0)

		self.content_message = ttk.Frame(self.content_form, style='Kim.TFrame')
		self.content_message.pack(pady=8, side=tk.BOTTOM)

		# render form
		self.form()

	def form(self):

		# Image
		img = self.getImage("views/images/user.png", 200, 200)
		image = tk.Label(self.content_form, image=img, fg="blue", background="#012D5A")
		image.image = img
		image.pack(pady=10)
		# Title of the Form
		tk.Label(self.content_form, text="Iniciar Sesion", fg="white", bg="#012D5A",
			font="Candara 28").pack(pady=10)

		# Entry of the username
		ttk.Label(self.content_form, text="Usuario",
			style="TLabel").place(x=90,y=310)

		self.username=validate.MaxLengthEntry(self.content_form, maxlength=40,
			value="", style="Kim.TEntry", font="Helvetica 14",
			width=25, justify="left")
		self.username.focus()
		self.username.pack(pady=8)

		# Entry of the password
		ttk.Label(self.content_form, text="Contraseña",
			style="TLabel").place(x=90,y=365)

		password = tk.Frame(self.content_form, background="#325678", relief=tk.RAISED)
		password.pack(pady=8)
		# password.pack_propagate(0)
		self.password=validate.MaxLengthEntry(password, show="*", maxlength=40,
			value="", style="Kim.TEntry",
			width=22, font="Helvetica 14",justify="left")
		self.password.pack(side=tk.LEFT)
		# Login
		img_send = self.getImage("views/images/send.png")
		ok=tk.Button(password, command=self.login, bd=0,
			bg="#325678", image=img_send, activebackground="#012D5A")
		ok.image = img_send
		ok.pack(side=tk.LEFT)
