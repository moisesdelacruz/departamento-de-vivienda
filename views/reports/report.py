#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.lib.pagesizes import A4, cm
from reportlab.lib.utils import ImageReader
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table,TableStyle
from reportlab.lib.enums import TA_CENTER

# imports locals moduls
from utils.methods import Methods
from database.main import FamilyModel, ViviendoModel

class ReportsModule(Methods):
	def __init__(self, **kwargs):
		# instance from database
		class DB(object): pass
		self.db = DB()
		self.db.family = FamilyModel()
		self.db.viviendo = ViviendoModel()

		# kwargs
		if kwargs.get('viviendo'):
			self.viviendo = kwargs.get('viviendo')
		elif kwargs.get('viviendo_id'):
			query = self.db.viviendo.retrive(
				kwargs.get('viviendo_id'), field='viviendo_id')
			self.viviendo = self._format_viviendo(query[0])
		else:
			ValueError("This Module require a field 'viviendo' or 'viviendo_id'")
			
		# date actually
		self.date = '%s-%s-%s' %(datetime.now().year,
			datetime.now().month,
			datetime.now().day)
		self.actually=datetime.strptime(str(self.date), '%Y-%m-%d')
		# path to route
		self.path='reportes/'+str(self.viviendo.get('ci'))
		if not os.path.exists(self.path):
			os.makedirs(self.path)

	def _viviendo(self):
		# view PDF
		header = ImageReader("views/images/header.jpg")
		c = canvas.Canvas(self.path+"/viviendo.pdf", pagesize=A4)
		# Header
		c.drawImage(header, 10, 760)

		# date
		c.setFont('Helvetica-Bold', 12)
		c.drawString(507, 700, self.actually.strftime('%d/%m/%Y'))
		c.line(507, 697, 567, 697)

		# Datos del Grupo Familiar
		c.setFont('Helvetica-Bold', 14)
		c.drawString(200, 650, 'Datos del Grupo Familiar')

		c.setFont('Helvetica-Bold', 10)
		c.drawString(30, 620, 'Fecha de Registro:')
		c.drawString(30, 600, 'Telefono de Contacto:')
		c.drawString(30, 580, 'Clasificacion de la Familia:')
		c.drawString(30, 560, 'Ingresos Mensuales:')
		# data
		c.setFont('Helvetica', 10)
		c.drawString(122, 620, str(self.viviendo.get('created_at')))
		c.drawString(137, 600, '0416-3658717')
		c.drawString(160, 580, '0800')
		c.drawString(132, 560, str(self.viviendo.get('entry')))

		# Grupo Familiar
		c.setFont('Helvetica-Bold', 12)
		c.drawString(240, 495, 'Grupo Familiar')

		# box gray
		black30transparent = colors.Color( 0, 0, 0, alpha=0.1)
		c.setFillColor(black30transparent)
		c.rect(30,375,535,110, fill=True, stroke=False)

		# LEFT
		c.setFillColor(colors.black)
		c.setFont('Helvetica-Bold', 8)
		c.drawString(32, 470, 'Cedula:')
		c.drawString(32, 450, 'Apellidos:')
		c.drawString(32, 430, 'Sexo:')
		c.drawString(32, 410, 'Niv. Instruccional:')
		c.drawString(32, 390, 'Ocupacion:')
		# RIGHT
		c.drawString(302, 470, 'Nombres:')
		c.drawString(302, 450, 'Fecha de Nacimiento:')
		c.drawString(302, 430, 'Rol:')
		c.drawString(302, 410, 'Discamacidad:')
		c.drawString(302, 390, 'Institucion:')
		# data
		# LEFT
		c.setFont('Helvetica', 8)
		c.drawString(64, 470, str(self.viviendo.get('ci')))
		c.drawString(73, 450, str(self.viviendo.get('last_name')))
		c.drawString(57, 430, str(self.viviendo.get('sex')))
		c.drawString(104, 410, str(self.viviendo.get('instructional_level')))
		c.drawString(78, 390, str(self.viviendo.get('occupation')))
		# RIGHT
		c.drawString(342, 470, str(self.viviendo.get('first_name')))
		c.drawString(387, 450, str(self.viviendo.get('birthday')))
		c.drawString(321, 430, 'Jefe(a)')
		c.drawString(361, 410, str(self.viviendo.get('discapacity_desc')))
		c.drawString(348, 390, str(self.viviendo.get('institution')))

		# Direccion de Origen
		c.setFont('Helvetica-Bold', 14)
		c.drawString(215, 330, 'Direccion de Origen')

		# LEFT
		c.setFont('Helvetica-Bold', 10)
		c.drawString(30, 300, 'Estado:')
		c.drawString(30, 280, 'Parroquia:')
		c.drawString(30, 260, 'Titularidad de Vivienda:')
		# RIGHT
		c.drawString(300, 300, 'Municipio:')
		c.drawString(300, 280, 'Condicion Vivienda:')
		c.drawString(300, 260, 'Direccion:')

		# data
		c.setFont('Helvetica', 10)
		# LEFT
		c.drawString(71, 300, 'Portuguesa')
		c.drawString(83, 280, 'Guanare')
		c.drawString(145, 260, 'N/A')
		# RIGHT
		c.drawString(355, 300, 'Guanare')
		c.drawString(400, 280, 'N/A')
		c.drawString(353, 260, str(self.viviendo.get('direction')))

		# save
		c.showPage()
		c.save()
		# open folder
		self.open_folder(['reportes', str(self.viviendo.get('ci'))])

	def _family_group(self):
		# view PDF
		header = ImageReader("views/images/header.jpg")
		c = canvas.Canvas(self.path+"/grupo_familiar.pdf", pagesize=A4)
		# Header
		c.drawImage(header, 10, 760)

		# Jefe de Familia
		c.setFont('Helvetica-Bold', 12)
		c.drawString(30, 700, 'Jefe(a) de Familia:')
		c.setFont('Helvetica', 12)
		c.drawString(30, 680, self.viviendo.get('full_name'))

		# date
		c.setFont('Helvetica-Bold', 12)
		c.drawString(507, 700, self.actually.strftime('%d/%m/%Y'))
		c.line(507, 697, 567, 697)

		# Title
		c.setFont('Helvetica-Bold', 14)
		c.drawString(240, 550, 'Grupo Familiar')

		# Table Family Group
		# header table > style
		styles = getSampleStyleSheet()
		styleBH = styles["Normal"]
		styleBH.alignment = TA_CENTER
		styleBH.fontSize = 10
		# header table fileds
		number = Paragraph('''#''',styleBH)
		ci = Paragraph('''CI''',styleBH)
		full_name = Paragraph('''Nomber Completo''',styleBH)
		birthday = Paragraph('''Fecha de Nacimiento''',styleBH)
		sex = Paragraph('''Sexo''',styleBH)

		# line list
		data =[]
		data.append([number, ci, full_name, birthday, sex])

		# items table > styles
		styleN = styles["BodyText"]
		styleN.alignment = TA_CENTER
		styleN.fontSize = 7

		high = 520
		# query to database
		query = self.db.family.list(
			viviendo_id=self.viviendo.get('id'))
		# iterator and format
		for (i, item) in enumerate(query):
			format_item = self._format_family(item)
			this_family = [i+1, format_item['ci'], format_item['full_name'],
				format_item['birthday'], format_item['sex']]
			data.append(this_family)
			high -= 18

		# table size
		width, height = A4
		table = Table(data,
			colWidths=[1.1 * cm, 2 * cm, 9 * cm, 4 * cm, 2.9 * cm])
		table.setStyle(TableStyle([
			# table styles
			('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black),
			('BOX', (0, 0), (-1, -1), 0.25, colors.black), ]))
		# pdf size
		table.wrapOn(c, width, height)
		table.drawOn(c, 30, high)

		# save
		c.showPage()
		c.save()
		# open folder
		self.open_folder(['reportes', str(self.viviendo.get('ci'))])


	def _family(self, family):
		# view PDF
		header = ImageReader("views/images/header.jpg")
		c = canvas.Canvas(self.path+"/familiar-"+str(family.get('ci'))+".pdf", pagesize=A4)
		# Header
		c.drawImage(header, 10, 760)

		# date
		c.setFont('Helvetica-Bold', 12)
		c.drawString(507, 700, self.actually.strftime('%d/%m/%Y'))
		c.line(507, 697, 567, 697)

		# Datos del Grupo Familiar
		c.setFont('Helvetica-Bold', 14)
		c.drawString(200, 650, 'Datos del Grupo Familiar')

		c.setFont('Helvetica-Bold', 10)
		c.drawString(30, 620, 'Fecha de Registro:')
		c.drawString(30, 600, 'Telefono de Contacto:')
		c.drawString(30, 580, 'Clasificacion de la Familia:')
		c.drawString(30, 560, 'Ingresos Mensuales:')
		# data
		c.setFont('Helvetica', 10)
		c.drawString(122, 620, str(family.get('created_at')))
		c.drawString(137, 600, '0416-3658717')
		c.drawString(160, 580, '0800')
		c.drawString(132, 560, str(family.get('entry')))

		# Grupo Familiar
		c.setFont('Helvetica-Bold', 12)
		c.drawString(240, 495, 'Grupo Familiar')

		# box gray
		black30transparent = colors.Color( 0, 0, 0, alpha=0.1)
		c.setFillColor(black30transparent)
		c.rect(30,375,535,110, fill=True, stroke=False)

		# LEFT
		c.setFillColor(colors.black)
		c.setFont('Helvetica-Bold', 8)
		c.drawString(32, 470, 'Cedula:')
		c.drawString(32, 450, 'Apellidos:')
		c.drawString(32, 430, 'Sexo:')
		c.drawString(32, 410, 'Niv. Instruccional:')
		c.drawString(32, 390, 'Ocupacion:')
		# RIGHT
		c.drawString(302, 470, 'Nombres:')
		c.drawString(302, 450, 'Fecha de Nacimiento:')
		c.drawString(302, 430, 'Rol:')
		c.drawString(302, 410, 'Discamacidad:')
		c.drawString(302, 390, 'Institucion:')
		# data
		# LEFT
		c.setFont('Helvetica', 8)
		c.drawString(64, 470, str(family.get('ci')))
		c.drawString(73, 450, str(family.get('last_name')))
		c.drawString(57, 430, str(family.get('sex')))
		c.drawString(104, 410, str(family.get('instructional_level')))
		c.drawString(78, 390, str(family.get('occupation')))
		# RIGHT
		c.drawString(342, 470, str(family.get('first_name')))
		c.drawString(387, 450, str(family.get('birthday')))
		c.drawString(321, 430, 'N/A')
		c.drawString(361, 410, str(family.get('discapacity_desc')))
		c.drawString(348, 390, str(family.get('institution')))

		# Direccion de Origen
		c.setFont('Helvetica-Bold', 14)
		c.drawString(215, 330, 'Direccion de Origen')

		# LEFT
		c.setFont('Helvetica-Bold', 10)
		c.drawString(30, 300, 'Estado:')
		c.drawString(30, 280, 'Parroquia:')
		c.drawString(30, 260, 'Titularidad de Vivienda:')
		# RIGHT
		c.drawString(300, 300, 'Municipio:')
		c.drawString(300, 280, 'Condicion Vivienda:')
		c.drawString(300, 260, 'Direccion:')

		# data
		c.setFont('Helvetica', 10)
		# LEFT
		c.drawString(71, 300, 'Portuguesa')
		c.drawString(83, 280, 'Guanare')
		c.drawString(145, 260, 'N/A')
		# RIGHT
		c.drawString(355, 300, 'Guanare')
		c.drawString(400, 280, 'N/A')
		c.drawString(353, 260, str(self.viviendo.get('direction')))

		# save
		c.showPage()
		c.save()
		# open folder
		self.open_folder(['reportes', str(self.viviendo.get('ci'))])