#!/usr/bin/python
# -*- coding: utf-8 -*-

import Tkinter as tk
from utils.methods import Methods

class SuccessesView(tk.Frame, Methods):
	def __init__(self, root, **kwargs):
		tk.Frame.__init__(self, root)
		self.root = root
		self.clean(self.root)
		if kwargs.get('message'):
			self.message = kwargs.get('message')
		else: self.message = 'Successes'
		self.view()

	def view(self):
		div = tk.Frame(self.root, height=60, relief=tk.RAISED)
		div.pack(expand=True, fill=tk.X)
		div.pack_propagate(0)

		view = tk.Frame(div, bd=1, bg="green")

		tk.Label(view, text=self.message,
			fg="green", font="Helvetica 32 normal").pack()
		view.pack(anchor=tk.CENTER)