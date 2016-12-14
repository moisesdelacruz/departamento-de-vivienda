#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import Tkinter as tk
import ttk

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
		div = ttk.Frame(self.root, height=550, style='Kim.TFrame')
		div.pack(expand=True, fill=tk.X)
		div.pack_propagate(0)

		view = ttk.Frame(div, width=650, padding=50, style='White.TFrame')
		view.pack(expand=True, fill=tk.Y)
		view.pack_propagate(0)

		# Logo
		logoImage = self.getImage("views/images/Gran-Mision-Vivienda-Venezuela.png", 520, 240)
		logo = ttk.Label(view, image=logoImage, style='Black.TLabel')
		logo.pack()
		logo.image = logoImage

		# form
		# Entry Cedula de Identidad
		form = ttk.Frame(view, style='Kim.TFrame')
		form.pack()

		self.search=validate.MaxLengthEntry(form, maxlength=40,
			style="White.TEntry", width=51, font="Helvetica 13",
			justify="left")
		self.search.focus()
		self.search.pack(side=tk.LEFT)
		# btn -----------
		img_send = self.getImage("views/images/send.png")
		ok=tk.Button(form, command=self.searchdb, bd=0, 
			bg="#325678", width=50, image=img_send)
		ok.image = img_send
		ok.pack(side=tk.LEFT)
		

	def noResult(self):
		self.empty = tk.Frame(self.root, bd=1, bg="red")

		tk.Label(self.empty, text=self.message,
			fg="red", font="Helvetica 14 normal").pack()
		self.empty.pack(side=tk.TOP)