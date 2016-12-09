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
			font="Helvetica 22 normal").pack(pady=20)

		box = tk.Frame(view)
		box.pack(side=tk.LEFT, anchor=tk.N)


		# last inicio of session
		box5 = tk.Frame(view)
		box5.pack(side=tk.BOTTOM, anchor=tk.SE)
		tk.Label(box5, text="Ultimo Inicio de Sesión:",
			font="Helvetica 12 normal", fg="#6b6a6a").pack(pady=10, side=tk.LEFT)
		tk.Label(box5, text="13/12/1989",
			font="Helvetica 12 normal", fg="blue").pack(pady=10, side=tk.LEFT)
