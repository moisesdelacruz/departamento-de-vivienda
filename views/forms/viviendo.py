#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import *
# import ttkcalendar

class ViviendoForm(Frame):

    def __init__(self, root):
        Frame.__init__(self, root)
        self.root = root
        self.form()

    def form(self):
        # Title of the Form
        Label(self.root,text="Registro de Viviendo", font="Helvetica 16 bold",
            fg="blue").place(x=310,y=60)

        # Entry of the cedula
        Label(self.root,text="CI:", font="Helvetica 12",
            fg="#474747").place(x=70,y=130)
        ci=StringVar(self.root, value='0')
        Entry(self.root,textvariable=ci, width=20, bd=0,
            font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
            highlightbackground="black",highlightcolor="red",
            highlightthickness=1).place(x=100,y=130)

        # Entrada de texto para Nombre
        Label(self.root,text="Nombre:", font="Helvetica 12",
            fg="#474747").place(x=27,y=165)
        first_name=StringVar()
        Entry(self.root,textvariable=first_name, width=20, bd=0,
            font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
            disabledbackground="#1E6FBA",disabledforeground="yellow",
            highlightbackground="black",highlightcolor="red",
            highlightthickness=1).place(x=100,y=165)

        # Entrada de texto para Apellido
        Label(self.root,text="Apellido:", font="Helvetica 12",
            fg="#474747").place(x=26,y=200)
        last_name=StringVar()
        Entry(self.root,textvariable=last_name, width=20, bd=0,
            font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
            disabledbackground="#1E6FBA",disabledforeground="yellow",
            highlightbackground="black",highlightcolor="red",
            highlightthickness=1).place(x=100,y=200)

        # Entrada de texto para direction
        Label(self.root,text="Fecha de Nacimiento:", font="Helvetica 12",
            fg="#474747").place(x=20,y=235)
        birthday=StringVar()
        # ttkcalendar.Calendar(self.root).pack()
        Entry(self.root,textvariable=birthday, width=12, bd=0,
            font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
            disabledbackground="#1E6FBA",disabledforeground="yellow",
            highlightbackground="black",highlightcolor="red",
            highlightthickness=1).place(x=181,y=235)


        # Fields right
        # Entrada de texto para Fecha de Nacimiento
        Label(self.root,text="Dirección:", font="Helvetica 12",
            fg="#474747").place(x=420,y=130)
        direction=StringVar()
        Entry(self.root,textvariable=direction, width=27, bd=0,
            font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
            disabledbackground="#1E6FBA",disabledforeground="yellow",
            highlightbackground="black",highlightcolor="red",
            highlightthickness=1).place(x=500,y=130)

        # Entrada de texto para estado_civil
        Label(self.root,text="Estado Civil:", font="Helvetica 12",
            fg="#474747").place(x=400,y=165)
        estado_civil=StringVar()
        Entry(self.root,textvariable=estado_civil, width=27, bd=0,
            font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
            disabledbackground="#1E6FBA",disabledforeground="yellow",
            highlightbackground="black",highlightcolor="red",
            highlightthickness=1).place(x=500,y=165)

        # Entrada de texto para work BOOLEAN
        Label(self.root,text="Trabaja:", font="Helvetica 12",
            fg="#474747").place(x=430,y=200)
        work=BooleanVar(self.root, value=False)
        Checkbutton(self.root,textvariable=work, font="Helvetica 14 normal",
            bd=0, bg="#1E6FBA", fg="black", highlightbackground="black",
            highlightcolor="red").place(x=500,y=200)

        # Entrada de texto para Ingresos
        Label(self.root,text="Ingresos:", font="Helvetica 12",
            fg="#474747").place(x=425,y=235)
        estado_civil=StringVar()
        Entry(self.root,textvariable=estado_civil, width=27, bd=0,
            font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
            disabledbackground="#1E6FBA",disabledforeground="yellow",
            highlightbackground="black",highlightcolor="red",
            highlightthickness=1).place(x=500,y=235)

        # Entrada de texto para postulation
        Label(self.root,text="Postulación:", font="Helvetica 12",
            fg="#474747").place(x=401,y=270)
        postulation=StringVar()
        Entry(self.root,textvariable=postulation, width=27, bd=0,
            font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
            disabledbackground="#1E6FBA",disabledforeground="yellow",
            highlightbackground="black",highlightcolor="red",
            highlightthickness=1).place(x=500,y=270)

        # Entrada de texto para discapacity BOOLEAN
        Label(self.root,text="Discapacidad:", font="Helvetica 12",
            fg="#474747").place(x=390,y=305)
        discapacity=BooleanVar(self.root, value=False)
        Checkbutton(self.root,textvariable=discapacity, font="Helvetica 14 normal",
            bd=0, bg="#1E6FBA", fg="black", highlightbackground="black",
            highlightcolor="red").place(x=500,y=305)

        # Entrada de texto para discapacity Description
        Label(self.root,text="Describa Discapacidad:", font="Helvetica 12",
            fg="#474747").place(x=320,y=340)
        discapacity_desc=StringVar()
        Text(self.root, width=30, height=4, bd=0,
            font="Helvetica 12 normal",bg="#1E6FBA",fg="yellow",
            highlightbackground="black",highlightcolor="red",
            highlightthickness=1).place(x=500,y=340)