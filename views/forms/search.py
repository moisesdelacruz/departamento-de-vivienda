#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import Tkinter as tk

from database.main import ViviendoModel
from database.main import TracingModel
from utils.methods import Methods
from utils import validate
from views.detail.viviendo import ViviendoDetail

class SearchForm(tk.Frame, Methods):
	def __init__(self, root, **kwargs):
		tk.Frame.__init__(self, root)
		self.root = root

		# Data base
		class DB(object): pass
		self.db = DB()
		self.db.viviendo = ViviendoModel()
		self.db.tracing = TracingModel()

		if kwargs.get('session'):
			self.session = kwargs.get('session')
		self.form()

	def searchdb(self):
		if hasattr(self, 'message'):
			self.empty.destroy()

		self.result = self.db.viviendo.retrive(int(self.search.get()), field='ci')

		if self.result:
			# set time
			self.db.tracing.create({"viviendo_id": self.result[0][0]})
			# clean content
			self.clean(self.root)
			# render view
			self.detail = ViviendoDetail(self.root, session=self.session, viviendo=self.result)
		else:
			self.message = 'no se encontro resultado'
			self.noResult()

	def form(self):
		# Content Horizontal
		div = tk.Frame(self.root, height=500, background="grey", relief=tk.RAISED)
		div.pack(expand=True, fill=tk.X)
		div.pack_propagate(0)
		# Content Vertical
		hor = tk.Frame(div, width=650, relief=tk.RAISED)
		hor.pack(expand=True, fill=tk.Y)
		hor.pack_propagate(0)

		# Logo
		logoImage = self.getImage("views/images/Gran-Mision-Vivienda-Venezuela.png", 520, 240)
		logo = tk.Label(hor, image=logoImage)
		logo.pack()
		logo.image = logoImage

		# form
		# Entry Cedula de Identidad
		form = tk.Frame(hor, background="grey", relief=tk.RAISED)
		form.pack()
		self.search=validate.IntegerEntry(form,
			width=34, font="Helvetica 18 normal",justify="left")
		self.search.focus()
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