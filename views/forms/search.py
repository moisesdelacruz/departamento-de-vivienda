#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import Tkinter as tk
from PIL import Image, ImageTk
from database.main import ViviendoModel
from views.forms.viviendoDetail import ViviendoDetail

class SearchForm(tk.Frame):
	def __init__(self, root, toolbar):
		tk.Frame.__init__(self, root)
		self.root = root
		self.toolbar = toolbar
		self.validate_number = (self.root.register(self.validate),
				'%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
		self.form()

	def getImage(self, image, sizeY=30, sizeX=30):
		self.img = Image.open(image)
		self.img = self.img.resize((sizeY, sizeX), Image.ANTIALIAS)
		return ImageTk.PhotoImage(self.img)

	def validate(self, action, index, value_if_allowed,
					   prior_value, text, validation_type, trigger_type, widget_name):
		if text in '0123456789.-+':
			try:
				float(value_if_allowed)
				return True
			except ValueError:
				return False
		else:
			return False

	def cleanWindow(self):
		for child in self.root.winfo_children():
			child.destroy()
		self.toolbar.__init__(self.root)

	def searchdb(self):
		if hasattr(self, 'message'):
			self.newRoot.destroy()

		tb = ViviendoModel()
		self.result = tb.retrive(int(self.search.get()))

		if self.result != []:
			print self.result
			self.cleanWindow()
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
		self.newRoot = tk.Frame(self.root, bd=1, bg="red")

		tk.Label(self.newRoot, text=self.message,
			fg="red", font="Helvetica 14 normal").pack()
		self.newRoot.pack(side=tk.TOP)