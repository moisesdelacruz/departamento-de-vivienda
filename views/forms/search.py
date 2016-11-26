#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import Tkinter as tk
from database.main import ViviendoModel
from utils.methods import Methods
from utils import validate
from views.detail.viviendo import ViviendoDetail

class SearchForm(tk.Frame, Methods):
	def __init__(self, root):
		tk.Frame.__init__(self, root)
		self.root = root
		self.form()

	def searchdb(self):
		if hasattr(self, 'message'):
			self.empty.destroy()

		tb = ViviendoModel()
		self.result = tb.retrive(int(self.search.get()), field='ci')

		if self.result:
			self.clean(self.root)
			self.detail = ViviendoDetail(self.root, viviendo=self.result)
		else:
			self.message = 'no se encontro resultado'
			self.noResult()

	def form(self):
		# Content
		div = tk.Frame(self.root, width=650, height=300,
			background="grey", relief=tk.RAISED)
		div.pack(side=tk.TOP, expand=True, fill=tk.X)
		div.pack_propagate(0)

		# Logo
		logoImage = self.getImage("views/images/Gran-Mision-Vivienda-Venezuela.jpg", 520, 240)
		logo = tk.Label(div, image=logoImage)
		logo.pack()
		logo.image = logoImage

		# form
		# Entry Cedula de Identidad
		form = tk.Frame(div, background="violet", relief=tk.RAISED)
		form.pack()
		self.search=validate.IntegerEntry(form,
			width=34, bd=0, font="Helvetica 18 normal",justify="left",
			bg="white",fg="black", highlightbackground="black",
			highlightcolor="red", highlightthickness=1)
		self.search.pack(side=tk.LEFT)
		iconSearch = self.getImage("views/images/search-icon.png")
		searchButton = tk.Button(form, command=self.searchdb,
			image=iconSearch, width=77, bd=0,
			bg="#4285f4", activebackground="#1E6FBA")
		searchButton.pack(side=tk.RIGHT)
		searchButton.image = iconSearch

	def noResult(self):
		self.empty = tk.Frame(self.root, bd=1, bg="red")

		tk.Label(self.empty, text=self.message,
			fg="red", font="Helvetica 14 normal").pack()
		self.empty.pack(side=tk.TOP)