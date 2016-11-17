#!/usr/bin/python
# -*- coding: utf-8 -*-

import Tkinter as tk
from views.utils._calendar import CalendarDialog

class ViviendoForm(tk.Frame):

    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.root = root
        self.form()

    def getDate(self):
        cd = CalendarDialog(self)
        result = cd.result
        try:
            self.birthday.set(result.strftime("%d/%m/%Y"))
        except AttributeError, e:
            self.birthday.set(self.birthday.get())

    def form(self):
        # Title of the Form
        tk.Label(self.root,text="Registro de Viviendo", font="Helvetica 16 bold",
            fg="blue").place(x=310,y=60)

        # Entry of the cedula
        tk.Label(self.root,text="CI:", font="Helvetica 12",
            fg="#474747").place(x=70,y=130)
        ci=tk.StringVar(self.root, value='0')
        tk.Entry(self.root,textvariable=ci, width=20, bd=0,
            font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
            highlightbackground="black",highlightcolor="red",
            highlightthickness=1).place(x=100,y=130)

        # Entrada de texto para Nombre
        tk.Label(self.root,text="Nombre:", font="Helvetica 12",
            fg="#474747").place(x=27,y=165)
        first_name=tk.StringVar()
        tk.Entry(self.root,textvariable=first_name, width=20, bd=0,
            font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
            disabledbackground="#1E6FBA",disabledforeground="yellow",
            highlightbackground="black",highlightcolor="red",
            highlightthickness=1).place(x=100,y=165)

        # Entrada de texto para Apellido
        tk.Label(self.root,text="Apellido:", font="Helvetica 12",
            fg="#474747").place(x=26,y=200)
        last_name=tk.StringVar()
        tk.Entry(self.root,textvariable=last_name, width=20, bd=0,
            font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
            disabledbackground="#1E6FBA",disabledforeground="yellow",
            highlightbackground="black",highlightcolor="red",
            highlightthickness=1).place(x=100,y=200)

        # Entrada de texto para direction
        tk.Label(self.root,text="Fecha de Nacimiento:", font="Helvetica 12",
            fg="#474747").place(x=10,y=235)
        self.birthday=tk.StringVar()
        # select date
        tk.Button(self.root, text="Cal", bg="#1E6FBA", fg="yellow",
            command=self.getDate).place(x=295,y=235)
        tk.Entry(self.root,textvariable=self.birthday, width=10, bd=0,
            font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
            disabledbackground="#1E6FBA",disabledforeground="yellow",
            highlightbackground="black",highlightcolor="red",
            highlightthickness=1).place(x=170,y=235)


        # Fields right
        # Entrada de texto para Fecha de Nacimiento
        tk.Label(self.root,text="Dirección:", font="Helvetica 12",
            fg="#474747").place(x=420,y=130)
        direction=tk.StringVar()
        tk.Entry(self.root,textvariable=direction, width=27, bd=0,
            font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
            disabledbackground="#1E6FBA",disabledforeground="yellow",
            highlightbackground="black",highlightcolor="red",
            highlightthickness=1).place(x=500,y=130)

        # Entrada de texto para estado_civil
        tk.Label(self.root,text="Estado Civil:", font="Helvetica 12",
            fg="#474747").place(x=400,y=165)
        estado_civil=tk.StringVar()
        tk.Entry(self.root,textvariable=estado_civil, width=27, bd=0,
            font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
            disabledbackground="#1E6FBA",disabledforeground="yellow",
            highlightbackground="black",highlightcolor="red",
            highlightthickness=1).place(x=500,y=165)

        # Entrada de texto para work BOOLEAN
        tk.Label(self.root,text="Trabaja:", font="Helvetica 12",
            fg="#474747").place(x=430,y=200)
        work=tk.BooleanVar(self.root, value=False)
        tk.Checkbutton(self.root,textvariable=work, font="Helvetica 14 normal",
            bd=0, bg="#1E6FBA", fg="black", highlightbackground="black",
            highlightcolor="red").place(x=500,y=200)

        # Entrada de texto para Ingresos
        tk.Label(self.root,text="Ingresos:", font="Helvetica 12",
            fg="#474747").place(x=425,y=235)
        estado_civil=tk.StringVar()
        tk.Entry(self.root,textvariable=estado_civil, width=27, bd=0,
            font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
            disabledbackground="#1E6FBA",disabledforeground="yellow",
            highlightbackground="black",highlightcolor="red",
            highlightthickness=1).place(x=500,y=235)

        # Entrada de texto para postulation
        tk.Label(self.root,text="Postulación:", font="Helvetica 12",
            fg="#474747").place(x=401,y=270)
        postulation=tk.StringVar()
        tk.Entry(self.root,textvariable=postulation, width=27, bd=0,
            font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
            disabledbackground="#1E6FBA",disabledforeground="yellow",
            highlightbackground="black",highlightcolor="red",
            highlightthickness=1).place(x=500,y=270)

        # Entrada de texto para discapacity BOOLEAN
        tk.Label(self.root,text="Discapacidad:", font="Helvetica 12",
            fg="#474747").place(x=390,y=305)
        discapacity=tk.BooleanVar(self.root, value=False)
        tk.Checkbutton(self.root,textvariable=discapacity, font="Helvetica 14 normal",
            bd=0, bg="#1E6FBA", fg="black", highlightbackground="black",
            highlightcolor="red").place(x=500,y=305)

        # Entrada de texto para discapacity Description
        tk.Label(self.root,text="Describa Discapacidad:", font="Helvetica 12",
            fg="#474747").place(x=320,y=340)
        discapacity_desc=tk.StringVar()
        tk.Text(self.root, width=30, height=4, bd=0,
            font="Helvetica 12 normal",bg="#1E6FBA",fg="yellow",
            highlightbackground="black",highlightcolor="red",
            highlightthickness=1).place(x=500,y=340)