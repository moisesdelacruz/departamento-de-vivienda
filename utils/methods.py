import os
import platform
import subprocess

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

	def floatDialog(self, value):
		var = FloatDialog(self.root, 'Ingresos', 'Ingresos Mensuales', value)
		self.entry = var.result if var.result != None else value

	def textDialog(self, value):
		dialog = TextDialog(self.root, 'Descapacidad', 'Describa descapacidad', value)
		self.discapacity_desc = dialog.result if dialog.result else value

	def select_civil_status(self):
		return ('Soltero(a)', 'Casado(a)', 'Divorciado(a)', 'Concubino(a)')

	def select_sex(self):
		return ('Hombre', 'Mujer')

	def select_instruccion_level(self):
		return ('Basica','Bachiller','Tecnico Medio','Tecnico Superior',
			'Universitario(a)','Post Grado')

	def selectPermissions(self):
		return ('Lectura', 'Lectura y Escritura')

	def select_postulations(self):
		return ('Institucional', 'Salud', 'Riesgo')

	def select_nationality(self):
		return ('V', 'E')

	def encrypt(self, password):
		return base64.b64encode(password)

	def decrypt(self, password):
		return base64.b64decode(password)

	def alert(self, title='Alert', message=''):
		tkMessageBox.showwarning(title=title, message=message)

	def open_folder(self, arr):
		path = ''
		for item in arr:
			path+=item+'/'

		if platform.system() == "Windows":
			path = ''
			for item in arr:
				path+=item+'\\'
			subprocess.Popen(r'explorer "%s"' %(path))
		elif platform.system() == "Darwin":
			subprocess.Popen(["open", path])
		else:
			subprocess.Popen(["xdg-open", path])

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
			"last_login": data[8],
		})

	def _format_family(self, data):
		return ({
			"id": int(data[0]),
			"viviendo_id": int(data[1]),
			"nationality": data[2],
			"ci": int(data[3]),
			"first_name": data[4],
			"last_name": data[5],
			"full_name": ' '.join([data[4], data[5]]),
			"birthday": data[6],
			"sex": data[7],
			"estado_civil": data[8],
			"instructional_level": data[9],
			"work": bool(data[10]),
			"occupation": data[11],
			"institution": data[12],
			"entry": float(data[13]),
			"birth_state": data[14],
			"discapacity": bool(data[15]),
			"discapacity_desc": str(data[16]),
			"old_age": bool(data[17]),
			"created_at": data[18]
		})

	def _format_viviendo(self, data):
		return ({
			"id": data[0],
			"nationality": data[1],
			"ci": data[2],
			"full_name": ' '.join([data[3], data[4]]),
			"first_name": data[3],
			"last_name": data[4],
			"birthday": data[5],
			"sex": data[6],
			"estado_civil": data[7],
			"instructional_level": data[8],
			"work": data[9],
			"occupation": data[10],
			"institution": data[11],
			"entry": data[12],
			"direction": data[13],
			"postulation": data[14],
			"discapacity": data[15],
			"discapacity_desc": data[16],
			"created_at": data[17]
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
		self.hour_62 = tkFont.Font(
			family="Raleway Thin",size=62)

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
		# Entry
		s.configure('Kim.TEntry', foreground='#6F767E',
			fieldbackground="#00162D", padding=5)

		# Entry White
		s.configure('White.TEntry', padding=5)

		# Combobox
		s.configure('TCombobox', padding=6)

		# Checkbutton
		s.configure('TCheckbutton', background="#FFF", foreground='black')

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
			background="#FFF", font=self.hour_62, justify="left")

		# messages of errors
		s.configure('Error.TLabel', foreground='#FFF',
			background="#FF0000", font=self.microsoft_12, justify="left")
