import os
import Tkinter as tk
import tkSimpleDialog

from PIL import Image, ImageTk
from utils.asktext import TextDialog

class Methods(object):

	def getImage(self, image, sizeY=30, sizeX=30):
		self.img = Image.open(image)
		self.img = self.img.resize((sizeY, sizeX), Image.ANTIALIAS)
		return ImageTk.PhotoImage(self.img)

	def clean(self, div):
		for child in div.winfo_children():
			child.destroy()

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

	def entry(self):
		self.value = tkSimpleDialog.askfloat('Ingresos', 'Ingresos Mensuales')

	def textDialog(self):
		dialog = TextDialog(self.root, 'Descapacidad', 'Describa descapacidad')
		self.discapacity_desc = dialog.result