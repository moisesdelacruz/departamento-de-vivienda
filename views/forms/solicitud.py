#!/usr/bin/python
# -*- coding: utf-8 -*-

import Tkinter as tk

class SolicitudForm(tk.Frame):
	def __init__(self, root):
		tk.Frame.__init__(self, root)
		self.root = root
		self.form()

	def form(self):
		tk.Label(self.root, text="Solicitud de Vivienda", font="Helvetica 16 bold",
			fg="red").place(x=310,y=60)

		# Entry housing_conditions
		tk.Label(self.root,text="Condicion Habitacional:", font="Helvetica 12",
            fg="#474747").place(x=10,y=130)
		housing_conditions = tk.StringVar
		tk.Entry(self.root,textvariable=housing_conditions, width=20, bd=0,
            font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
            highlightbackground="black",highlightcolor="red",
            highlightthickness=1).place(x=185,y=130)

		# Entry housing_direction
		tk.Label(self.root,text="Dirección Habitacional:", font="Helvetica 12",
            fg="#474747").place(x=11,y=165)
		housing_direction = tk.StringVar
		tk.Entry(self.root,textvariable=housing_direction, width=20, bd=0,
            font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
            highlightbackground="black",highlightcolor="red",
            highlightthickness=1).place(x=185,y=165)
		
		# Entry phone_number
		tk.Label(self.root,text="Numero de Telefono:", font="Helvetica 12",
            fg="#474747").place(x=30,y=200)
		phone_number = tk.StringVar
		tk.Entry(self.root,textvariable=phone_number, width=20, bd=0,
            font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
            highlightbackground="black",highlightcolor="red",
            highlightthickness=1).place(x=185,y=200)

		# Entry residence_constancia
		tk.Label(self.root,text="Constancia de Residencia:", font="Helvetica 12",
            fg="#474747").place(x=10,y=235)
		residence_constancia = tk.BooleanVar(self.root, value=False)
		tk.Checkbutton(self.root, textvariable=residence_constancia, font="Helvetica 14 normal",
            bd=0, bg="#1E6FBA", fg="black", highlightbackground="black",
            highlightcolor="red").place(x=205,y=235)

		# Entry copy_ci
		tk.Label(self.root,text="Copia de Cedula:", font="Helvetica 12",
			fg="#474747").place(x=70,y=270)
		copy_ci = tk.BooleanVar(self.root, value=False)
		tk.Checkbutton(self.root,textvariable=copy_ci, font="Helvetica 14 normal",
            bd=0, bg="#1E6FBA", fg="black", highlightbackground="black",
            highlightcolor="red").place(x=205,y=270)

		# Entry housing_in_risk
		tk.Label(self.root,text="Vivienda en Riesgo?:", font="Helvetica 12",
            fg="#474747").place(x=595,y=130)
		housing_in_risk = tk.BooleanVar(self.root, value=False)
		tk.Checkbutton(self.root,textvariable=housing_in_risk, font="Helvetica 14 normal",
            bd=0, bg="#1E6FBA", fg="black", highlightbackground="black",
            highlightcolor="red").place(x=750,y=130)

        # Entry firefighters_constancy
		tk.Label(self.root,text="Constancia de los Bomberos:", font="Helvetica 12",
            fg="#474747").place(x=538,y=165)
		firefighters_constancy = tk.BooleanVar(self.root, value=False)
		tk.Checkbutton(self.root,textvariable=firefighters_constancy, font="Helvetica 14 normal",
            bd=0, bg="#1E6FBA", fg="black", highlightbackground="black",
            highlightcolor="red").place(x=750,y=165)

        # Entry health_case
		tk.Label(self.root,text="Caso de Salud:", font="Helvetica 12",
            fg="#474747").place(x=632,y=200)
		health_case = tk.BooleanVar(self.root, value=False)
		tk.Checkbutton(self.root,textvariable=health_case, font="Helvetica 14 normal",
            bd=0, bg="#1E6FBA", fg="black", highlightbackground="black",
            highlightcolor="red").place(x=750,y=200)

        # Entry medical_reports
		tk.Label(self.root,text="Informes Medicos:", font="Helvetica 12",
            fg="#474747").place(x=612,y=235)
		medical_reports = tk.BooleanVar(self.root, value=False)
		tk.Checkbutton(self.root,textvariable=medical_reports, font="Helvetica 14 normal",
            bd=0, bg="#1E6FBA", fg="black", highlightbackground="black",
            highlightcolor="red").place(x=750,y=235)

		# Entry copy_register_of_the_big_mision_vivienda
		tk.Label(self.root,text="Copia del Registro de la Gran Misíon Vivienda Venezuela:", font="Helvetica 12",
            fg="#474747").place(x=340,y=270)
		copy_register_of_the_big_mision_vivienda = tk.BooleanVar(self.root, value=False)
		tk.Checkbutton(self.root,textvariable=copy_register_of_the_big_mision_vivienda, font="Helvetica 14 normal",
            bd=0, bg="#1E6FBA", fg="black", highlightbackground="black",
            highlightcolor="red").place(x=750,y=270)