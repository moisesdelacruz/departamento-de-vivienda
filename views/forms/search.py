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

		if kwargs.get('session'):
			self.session = kwargs.get('session')

		# Data base
		class DB(object): pass
		self.db = DB()
		self.db.viviendo = ViviendoModel()
		self.db.tracing = TracingModel()

		# contents
		div = ttk.Frame(self.root, height=550, style='Kim.TFrame')
		div.pack(expand=True, fill=tk.X)
		div.pack_propagate(0)

		self._view = ttk.Frame(div, width=650, padding=50, style='White.TFrame')
		self._view.pack(expand=True, fill=tk.Y)
		self._view.pack_propagate(0)

		self.message = ttk.Frame(self._view, style='White.TFrame')
		self.message.pack(side=tk.BOTTOM)

		# Init view
		self.form()

	def searchdb(self):

		if len(self.search.get()) >= 7:
			self.result = self.db.viviendo.retrive(int(self.search.get()), field='ci')

			if self.result:
				# set time
				self.db.tracing.create({"viviendo_id": self.result[0][0]})
				# clean content
				self.clean(self.root)
				# render view
				self.detail = ViviendoDetail(self.root, session=self.session, viviendo=self.result)
			else:
				message = 'Viviendo '+self.search.get()+' no existe'
				self.error(message)
		else:
			message = 'Debes introducir una Cedula de Identidad valida'
			self.error(message)

	def form(self):
		view=self._view

		# Logo
		logoImage = self.getImage(
			"views/images/Gran-Mision-Vivienda-Venezuela.png", 520, 240)
		logo = ttk.Label(view, image=logoImage, style='Black.TLabel')
		logo.pack()
		logo.image = logoImage

		# form
		# Entry Cedula de Identidad
		form = ttk.Frame(view, style='Kim.TFrame')
		form.pack()

		self.search=validate.IntegerEntry(form,
			style="White.TEntry", width=51, font="Helvetica 13",
			justify="left")
		self.search.focus()
		self.search.pack(side=tk.LEFT)
		# btn -----------
		img_send = self.getImage("views/images/send.png")
		ok=tk.Button(form, command=self.searchdb, bd=0, 
			bg="#325678", width=50, image=img_send,
			activebackground="#012D5A")
		ok.image = img_send
		ok.pack(side=tk.LEFT)
		

	def error(self, message):
		self.clean(self.message)
		# message of error
		ttk.Label(self.message, text=message,
			style='Error.TLabel').pack()