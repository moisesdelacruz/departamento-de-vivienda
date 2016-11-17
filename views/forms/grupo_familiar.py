#!/usr/bin/python
# -*- coding: utf-8 -*-

import Tkinter as tk

class Grupo_familiarForm(tk.Frame):
	def __init__(self, root):
		tk.Frame.__init__(self, root)
		self.root = root
		self.form()


	def form(self):
		# Title
		tk.Label(self.root, text="Registrar Grupo Familiar",
			font="Helvetica 16 bold", fg="green").place(x=290,y=60)

		# Entry of the cedula
		tk.Label(self.root,text="CI:", font="Helvetica 12",
			fg="#474747").place(x=130,y=130)
		ci=tk.StringVar(self.root, value='0')
		tk.Entry(self.root,textvariable=ci, width=20, bd=0,
			font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
			highlightbackground="black",highlightcolor="red",
			highlightthickness=1).place(x=160,y=130)

		# Entry of first_name
		tk.Label(self.root,text="Nombre:", font="Helvetica 12",
			fg="#474747").place(x=93,y=165)
		first_name=tk.StringVar()
		tk.Entry(self.root,textvariable=first_name, width=20, bd=0,
			font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
			highlightbackground="black",highlightcolor="red",
			highlightthickness=1).place(x=160,y=165)

		# Entry of last_name
		tk.Label(self.root,text="Apellido:", font="Helvetica 12",
			fg="#474747").place(x=90,y=200)
		last_name=tk.StringVar()
		tk.Entry(self.root,textvariable=last_name, width=20, bd=0,
			font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
			highlightbackground="black",highlightcolor="red",
			highlightthickness=1).place(x=160,y=200)

		# Entry of birthday
		tk.Label(self.root,text="Fecha de Nacimiento:", font="Helvetica 12",
			fg="#474747").place(x=20,y=235)
		birthday=tk.StringVar()
		# ttkcalendar.Calendar(self.root).pack()
		tk.Entry(self.root,textvariable=birthday, width=12, bd=0,
			font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
			disabledbackground="#1E6FBA",disabledforeground="yellow",
			highlightbackground="black",highlightcolor="red",
			highlightthickness=1).place(x=181,y=235)

		# Entry birth_state
		tk.Label(self.root,text="Estado de Nacimiento:", font="Helvetica 12",
			fg="#474747").place(x=12,y=270)
		birth_state=tk.StringVar()
		tk.Entry(self.root,textvariable=birth_state, width=18, bd=0,
			font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
			highlightbackground="black",highlightcolor="red",
			highlightthickness=1).place(x=181,y=270)

		# Entry of tercera edad
		tk.Label(self.root,text="Tercera Edad?:", font="Helvetica 12",
			fg="#474747").place(x=60,y=305)
		old_age=tk.BooleanVar(self.root, value=False)
		tk.Checkbutton(self.root,textvariable=old_age, font="Helvetica 14 normal",
			bd=0, bg="#1E6FBA", fg="black", highlightbackground="black",
			highlightcolor="red").place(x=181,y=305)

		# Entry of discapacity
		tk.Label(self.root,text="Discapacidad?:", font="Helvetica 12",
			fg="#474747").place(x=57,y=340)
		discapacity=tk.BooleanVar(self.root, value=False)
		tk.Checkbutton(self.root,textvariable=discapacity, font="Helvetica 14 normal",
			bd=0, bg="#1E6FBA", fg="black", highlightbackground="black",
			highlightcolor="red").place(x=181,y=340)

		# Entry of discapacity description
		tk.Label(self.root,text="Describa Discapacidad:", font="Helvetica 12",
			fg="#474747").place(x=5,y=375)
		discapacity_desc=tk.StringVar()
		tk.Text(self.root, width=22, height=4, bd=0,
			font="Helvetica 12 normal",bg="#1E6FBA",fg="yellow",
			highlightbackground="black",highlightcolor="red",
			highlightthickness=1).place(x=180,y=375)

		# Right Fields
		# Entry of work
		tk.Label(self.root,text="Trabaja?:", font="Helvetica 12",
			fg="#474747").place(x=425,y=130)
		work=tk.BooleanVar(self.root, value=False)
		tk.Checkbutton(self.root,textvariable=work, font="Helvetica 14 normal",
			bd=0, bg="#1E6FBA", fg="black", highlightbackground="black",
			highlightcolor="red").place(x=500,y=130)

		# Entry of Entry > Ingresos
		tk.Label(self.root,text="Ingresos:", font="Helvetica 12",
			fg="#474747").place(x=430,y=165)
		entry=tk.StringVar()
		tk.Entry(self.root,textvariable=entry, width=20, bd=0,
			font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
			highlightbackground="black",highlightcolor="red",
			highlightthickness=1).place(x=500,y=165)