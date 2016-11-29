#!/usr/bin/python
# -*- coding: utf-8 -*-

import Tkinter as tk

class HomeView(tk.Frame):
	def __init__(self, root, account):
		tk.Frame.__init__(self, root)
		self.root = root
		self.account = account
		self.view()

	def view(self):
		div = tk.Frame(self.root, height=550, background="grey", relief=tk.RAISED)
		div.pack(expand=True, fill=tk.X)
		div.pack_propagate(0)

		view = tk.Frame(div, width=650, relief=tk.RAISED)
		view.pack(expand=True, fill=tk.Y)
		view.pack_propagate(0)

		tk.Label(view, text=' '.join(['Bienvenido',
			self.account.get('first_name'),
			self.account.get('last_name')]),
			font="Helvetica 24 normal").pack(pady=20)

		box = tk.Frame(view)
		box.pack(side=tk.LEFT, anchor=tk.N)
		# username
		box1 = tk.Frame(box)
		box1.pack(anchor=tk.NW)
		tk.Label(box1, text="Nombre de Usuario:",
			font="Helvetica 14 normal", fg="#6b6a6a").pack(pady=10, side=tk.LEFT)
		tk.Label(box1, text=self.account.get('username'),
			font="Helvetica 14 normal", fg="red").pack(pady=10, side=tk.LEFT)

		# cedula
		box2 = tk.Frame(box)
		box2.pack(anchor=tk.NW)
		tk.Label(box2, text="Cedula de Identidad:",
			font="Helvetica 14 normal", fg="#6b6a6a").pack(pady=10, side=tk.LEFT)
		tk.Label(box2, text=self.account.get('cedula'),
			font="Helvetica 14 normal", fg="green").pack(pady=10, side=tk.LEFT)

		# permission
		box3 = tk.Frame(box)
		box3.pack(anchor=tk.NW)
		tk.Label(box3, text="Permisos:",
			font="Helvetica 14 normal", fg="#6b6a6a").pack(pady=10, side=tk.LEFT)
		tk.Label(box3, text=self.account.get('permission'),
			font="Helvetica 14 normal", fg="blue").pack(pady=10, side=tk.LEFT)

		# is_superuser
		box4 = tk.Frame(box)
		box4.pack(anchor=tk.NW)
		tk.Label(box4, text="Superusuario:",
			font="Helvetica 14 normal", fg="#6b6a6a").pack(pady=10, side=tk.LEFT)
		tk.Label(box4, text="SI" if self.account.get('is_superuser') else "NO",
			font="Helvetica 14 normal", fg="blue").pack(pady=10, side=tk.LEFT)

		# last inicio of session
		box5 = tk.Frame(view)
		box5.pack(side=tk.BOTTOM, anchor=tk.SE)
		tk.Label(box5, text="Ultimo Inicio de Sesión:",
			font="Helvetica 12 normal", fg="#6b6a6a").pack(pady=10, side=tk.LEFT)
		tk.Label(box5, text="13/12/1989",
			font="Helvetica 12 normal", fg="blue").pack(pady=10, side=tk.LEFT)
