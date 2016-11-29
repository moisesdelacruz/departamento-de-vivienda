#!/usr/bin/python
# -*- coding: utf-8 -*-

from database.main import UserModel

class CreateSuperUser(object):
	def __init__(self):
		self.db = UserModel()
		self.form()

	def save(self):
		if self.password1 == self.password2:
			data = ({
				"username": str(self.username),
				"first_name": '',
				"last_name": '',
				"cedula": 0,
				"permission": str('Lectura y Escritura'),
				"is_superuser": bool(True),
				"password": str(self.password1)
			})
			print data
			self.db.create(data)

	def form(self):
		self.username = raw_input("Nombre de Usuario: ")
		self.password1 = raw_input("Contraseña: ")
		self.password2 = raw_input("Confirme Contraseña: ")
		self.save()