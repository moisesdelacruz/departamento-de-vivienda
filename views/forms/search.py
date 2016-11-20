#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import Tkinter as tk
from database.main import ViviendoModel
from views.utils.methods import Methods
from views.forms.viviendoDetail import ViviendoDetail

class SearchForm(tk.Frame, Methods):
	def __init__(self, root):
		tk.Frame.__init__(self, root)
		self.root = root
		self.validate_number = (self.root.register(self.validate),
				'%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
		self.form()

	def searchdb(self):
		if hasattr(self, 'message'):
			self.empty.destroy()

		tb = ViviendoModel()
		self.result = tb.retrive(int(self.search.get()))

		if self.result != []:
			print self.result
			self.clean(self.root)
			self.detail = ViviendoDetail(self.root, self.result)
		else:
			self.message = 'no se encontro resultado'
			self.noResult()

	def form(self):
		# Logo
		logoImage = self.getImage("views/images/Gran-Mision-Vivienda-Venezuela.jpg", 520, 240)
		logo = tk.Label(self.root, image=logoImage)
		logo.place(x=160,y=110)
		logo.image = logoImage

		# form
		# Entry Cedula de Identidad
		self.search=tk.StringVar()
		tk.Entry(self.root,textvariable=self.search,
			validate='key', validatecommand=self.validate_number,
			width=33, bd=0, font="Helvetica 18 normal",justify="left",
			bg="white",fg="black", highlightbackground="black",
			highlightcolor="red", highlightthickness=1).place(x=161,y=320)
		iconSearch = self.getImage("views/images/search-icon.png")
		searchButton = tk.Button(self.root, command=self.searchdb,
			image=iconSearch, width=82, bd=0,
			bg="#4285f4", activebackground="#1E6FBA")
		searchButton.place(x=598,y=320)
		searchButton.image = iconSearch

	def noResult(self):
		self.empty = tk.Frame(self.root, bd=1, bg="red")

		tk.Label(self.empty, text=self.message,
			fg="red", font="Helvetica 14 normal").pack()
		self.empty.pack(side=tk.TOP)