#!/usr/bin/python
# -*- coding: utf-8 -*-

import Tkinter as tk
from utils.methods import Methods

class AboutView(tk.Frame, Methods):
	def __init__(self, root):
		tk.Frame.__init__(self, root)
		self.root = root
		self.view()

	def view(self):
		div = tk.Frame(self.root, height=60, relief=tk.RAISED)
		div.pack(expand=True, fill=tk.X)
		div.pack_propagate(0)

		view = tk.Frame(div, bd=1, bg="grey")

		tk.Label(view, text='Universidad UPTP',
			fg="grey", font="Helvetica 26 normal").pack()
		view.pack(anchor=tk.CENTER)