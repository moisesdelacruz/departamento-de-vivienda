#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, cm
from reportlab.lib.utils import ImageReader
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, Table,TableStyle
from reportlab.lib.enums import TA_CENTER

# imports locals moduls
from utils.methods import Methods
from database.main import FamilyModel

class ReportsModule(Methods):
	def __init__(self, viviendo):
		# database instances
		self.viviendo = viviendo
		# instance from database
		self.db = FamilyModel()
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

		# Viviendo
		c.setFont('Helvetica-Bold', 15)
		c.drawString(430, 650, 'Viviendo')
		c.line(427, 647, 495, 647)
		c.setFont('Helvetica', 13)
		c.drawString(420, 635, self.viviendo.get('full_name'))

		# Title
		c.setFont('Helvetica-Bold', 18)
		c.drawString(240, 550, 'Viviendo')
		c.line(238, 545, 355, 545)

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

		# Viviendo
		c.setFont('Helvetica-Bold', 15)
		c.drawString(430, 650, 'Viviendo')
		c.line(427, 647, 495, 647)
		c.setFont('Helvetica', 13)
		c.drawString(420, 635, self.viviendo.get('full_name'))

		# Title
		c.setFont('Helvetica-Bold', 18)
		c.drawString(240, 550, 'Grupo Familiar')
		c.line(238, 545, 360, 545)

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
		query = self.db.list(
			viviendo_id=self.viviendo.get('id'))
		# iterator and format
		for (i, item) in enumerate(query):
			format_item = self._format_family(item)
			this_family = [i+1, format_item['ci'], format_item['full_name'],
				format_item['birthday'], 'N/A']
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
