import os
import Tkinter as tk
import tkSimpleDialog

from PIL import Image, ImageTk
from utils.asktext import TextDialog
from utils.askfloat import FloatDialog
from utils._calendar import CalendarDialog

class Methods(object):

	def getImage(self, image, sizeY=30, sizeX=30):
		self.img = Image.open(image)
		self.img = self.img.resize((sizeY, sizeX), Image.ANTIALIAS)
		return ImageTk.PhotoImage(self.img)

	def getDate(self):
		cd = CalendarDialog(self)
		result = cd.result
		try:
			self.birthday.set(result.strftime("%Y-%m-%d"))
		except AttributeError, e:
			self.birthday.set(self.birthday.get())


	def clean(self, div):
		for child in div.winfo_children():
			child.destroy()

	def entry(self, value):
		var = FloatDialog(self.root, 'Ingresos', 'Ingresos Mensuales', value)
		self.value = var.result

	def textDialog(self, value):
		dialog = TextDialog(self.root, 'Descapacidad', 'Describa descapacidad', value)
		self.discapacity_desc = dialog.result