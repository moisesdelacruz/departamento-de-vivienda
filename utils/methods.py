import os
import Tkinter as tk
import ttk
import tkFont
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

	def _format_user(self, data):
		return ({
			"user_id": data[0],
			"username": data[1],
			"first_name": data[2],
			"last_name": data[3],
			"full_name": ' '.join([data[2], data[3]]),
			"cedula": data[4],
			"is_superuser": data[5],
			"permission": data[6],
			"password": data[7],
		})

	def _format_family(self, data):
		return ({
			"id": int(data[0]),
			"viviendo_id": int(data[1]),
			"ci": int(data[2]),
			"first_name": data[3],
			"last_name": data[4],
			"full_name": ' '.join([data[3], data[4]]),
			"birthday": data[5],
			"work": bool(data[6]),
			"birth_state": data[7],
			"entry": float(data[8]),
			"discapacity": bool(data[9]),
			"discapacity_desc": str(data[10]),
			"old_age": bool(data[11])
		})

	def style(self):
		# Fonts
		self.microsoft_10 = tkFont.Font(
			family="Microsoft New Tai Lue",size=10,weight="normal")
		self.microsoft_12 = tkFont.Font(
			family="Microsoft New Tai Lue",size=12,weight="normal")
		self.microsoft_12_bold = tkFont.Font(
			family="Microsoft New Tai Lue",size=12,weight="bold")
		self.microsoft_14 = tkFont.Font(
			family="Microsoft New Tai Lue",size=14,weight="normal")
		self.microsoft_16 = tkFont.Font(
			family="Microsoft New Tai Lue",size=16,weight="normal")
		self.microsoft_18 = tkFont.Font(
			family="Microsoft New Tai Lue",size=18,weight="normal")
		self.microsoft_22 = tkFont.Font(
			family="Microsoft New Tai Lue",size=22,weight="normal")
		self.microsoft_62 = tkFont.Font(
			family="Microsoft Yi Baiti",size=62)

		# styles forms
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

		# Entry White
		s.configure('White.TEntry', padding=5)

		# Combobox
		s.configure('TCombobox', padding=6)

		# Checkbutton
		s.configure('TCheckbutton', background="#012D5A", foreground='white')

		# Button
		s.configure('Kim.TButton', foreground='#6F767E',
			fieldbackground="#00162D")

		# Frame
		s.configure('Kim.TFrame', background="#012D5A")
		# item list
		s.configure('Item.TFrame', background="#00162D")
		# frame white
		s.configure('White.TFrame', background="#FFF")
		# frame grey
		s.configure('Grey.TFrame', background="#f0f0f0")

		# Label
		s.configure('Title.TLabel', foreground='#FFF',
			background="#012D5A", font=self.microsoft_22)

		# title black
		s.configure('Black.TLabel', foreground='#000',
			background='#f0f0f0', font=self.microsoft_16)
		# title back 22
		s.configure('Black22.TLabel', foreground='#000',
			background='#FFF', font=self.microsoft_22)

		s.configure('Text.TLabel', foreground='#FFF',
			background="#012D5A", font=self.microsoft_12, justify="left")

		s.configure('Text_bold.TLabel', foreground='#FFF',
			background="#012D5A", font=self.microsoft_12_bold, justify="left")

		s.configure('Black12.TLabel', foreground='#000',
			background="#FFF", font=self.microsoft_12, justify="left")

		s.configure('Black12_bold.TLabel', foreground='#000',
			background="#FFF", font=self.microsoft_12_bold, justify="left")

		# background grey foreground black
		s.configure('Grey12.TLabel', foreground='#000',
			background="#f0f0f0", font=self.microsoft_12, justify="left")

		s.configure('Grey10.TLabel', foreground='#000',
			background="#f0f0f0", font=self.microsoft_10, justify="left")

		s.configure('TLabel', foreground='#FFF',
			background="#012D5A", font=self.microsoft_10, justify="left")
		# label white
		s.configure('Black.TLabel', foreground='#000',
			background="#FFF", font=self.microsoft_10, justify="left")

		# text item list
		s.configure('Item.TLabel', foreground='#FFF',
			background="#00162D", font=self.microsoft_12, justify="left")

		# hour
		s.configure('Hour.TLabel', foreground='#000',
			background="#FFF", font=self.microsoft_62, justify="left")

		# messages of errors
		s.configure('Error.TLabel', foreground='#FFF',
			background="#FF0000", font=self.microsoft_18, justify="left")