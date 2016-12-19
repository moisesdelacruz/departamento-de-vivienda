#!/usr/bin/python
# -*- coding: utf-8 -*-

from database.main import UserModel
from utils.methods import Methods
import getpass

class CreateSuperUser(Methods):
	def __init__(self):
		self.db = UserModel()
		self.form()

	def save(self):
		if self.password1 == self.password2:
			password_encrypt = self.encrypt(self.password1)
			data = ({
				"username": str(self.username),
				"first_name": '',
				"last_name": '',
				"cedula": int(self.cedula),
				"permission": str('Lectura y Escritura'),
				"is_superuser": bool(True),
				"password": str(password_encrypt)
			})
			self.db.create(data)
		else: print "Passwords do not match."

	def form(self):
		self.username = raw_input("Nombre de Usuario: ")
		self.cedula = raw_input("Cedula de Identidad: ")
		self.password1 = getpass.getpass("Contraseña: ")
		self.password2 = getpass.getpass("Confirme Contraseña: ")
		self.save()