import os
import Tkinter as tk
import tkSimpleDialog

from PIL import Image, ImageTk
from utils.asktext import TextDialog
from utils.askfloat import FloatDialog

class Methods(object):

	def getImage(self, image, sizeY=30, sizeX=30):
		self.img = Image.open(image)
		self.img = self.img.resize((sizeY, sizeX), Image.ANTIALIAS)
		return ImageTk.PhotoImage(self.img)

	def clean(self, div):
		for child in div.winfo_children():
			child.destroy()

	def entry(self):
		var = FloatDialog(self.root, 'Ingresos', 'Ingresos Mensuales')
		self.value = var.result

	def textDialog(self):
		dialog = TextDialog(self.root, 'Descapacidad', 'Describa descapacidad')
		self.discapacity_desc = dialog.result