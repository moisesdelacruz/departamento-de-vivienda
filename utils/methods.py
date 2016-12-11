import os
import Tkinter as tk
import ttk
import tkMessageBox
import tkSimpleDialog
import base64

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

	def entry(self, value):
		var = FloatDialog(self.root, 'Ingresos', 'Ingresos Mensuales', value)
		self.value = var.result if var.result != None else value

	def textDialog(self, value):
		dialog = TextDialog(self.root, 'Descapacidad', 'Describa descapacidad', value)
		self.discapacity_desc = dialog.result if dialog.result else value

	def select_civil_status(self):
		return ('Soltero(a)', 'Casado(a)', 'Divorciado(a)', 'Concubino(a)')

	def select_sex(self):
		return ('Hombre', 'Mujer')

	def selectPermissions(self):
		return ('Lectura', 'Lectura y Escritura')

	def encrypt(self, password):
		return base64.b64encode(password)

	def decrypt(self, password):
		return base64.b64decode(password)

	def alert(self, title='Alert', message=''):
		tkMessageBox.showwarning(title=title, message=message)

	def style(self):
		s = ttk.Style()
		s.element_create("plain.field", "from", "clam")
		s.layout("Kim.TEntry",
                   [('Entry.plain.field', {'children': [(
                       'Entry.background', {'children': [(
                           'Entry.padding', {'children': [(
                               'Entry.textarea', {'sticky': 'nswe'})],
                      'sticky': 'nswe'})], 'sticky': 'nswe'})],
                      'border':'2', 'sticky': 'nswe'})])
		s.configure('Kim.TEntry', foreground='#6F767E',
			fieldbackground="#00162D", padding=5)

		# Button
		s.configure('Kim.TButton', foreground='#6F767E',
			fieldbackground="#00162D")

		# Frame
		s.configure('Kim.TFrame', background="#012D5A")