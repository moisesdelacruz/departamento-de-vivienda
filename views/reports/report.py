#!/usr/bin/python
# -*- coding: utf-8 -*-

from xhtml2pdf import pisa
import codecs

class ReportsModule(object):

	def viviendo(self, model):
		sourceHTML = """
			<!DOCTYPE html>
			<html>
			<head>
				<meta charset="utf-8"/>
			</head>
			<body>
				<h2>A quién corresponda</h2>
				<h3>H. Consejo</h3>
				<p>
					Announcing the New Heroku CLI: Performance and Readability Enhancements 
					Learn how to take advantage of the CLI’s faster performance and new usability features.

					Apache Kafka, Data Pipelines, and Functional Reactive Programming with Node.js 
					Chris Castle shows you how pairing Kafka with Node.js simplifies the handling of event streams and lets you create fast, reliable, and scalable data processing pipelines.

					PostgreSQL 9.6 Now Generally Available on Heroku 
					Learn how parallelism in PostgreSQL 9.6 can help you speed up sequential scans for faster analytics applications, create indexes without blocking writes on tables in production apps, and much more.

					RubyConf 2016 Session Videos Now Available 
					If you weren’t able to make it to RubyConf in Cincinnati, you can still be part of the experience by watching the Heroku session recordings from this year’s event, including Matz’s keynote as well as talks on speech recognition with Ruby, Ruby 3 concurrency, and more.

					A Few Postgres Essentials 
					Postgres is our favorite database - it’s reliable and powerful. Check out these essential tips that can help you use Postgres more efficiently.
				</p>
				<h1>"""+model.get('full_name')+"""</h1>
			</html>
		"""
		 
		outFilename = "test.pdf"
		outFile = open(outFilename, "w+b")
		pisaStatus = pisa.CreatePDF(sourceHTML, dest=outFile)
		outFile.close()
		if pisaStatus.err:
			print pisaStatus.err