#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import Tkinter as tk
from utils._calendar import CalendarDialog
from utils.methods import Methods
from database.main import ViviendoModel

class ViviendoForm(tk.Frame, Methods):

    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.root = root
        self.validate_number = (self.root.register(self.validate),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        self.form()

    def getDate(self):
        cd = CalendarDialog(self)
        result = cd.result
        try:
            self.birthday.set(result.strftime("%d/%m/%Y"))
        except AttributeError, e:
            self.birthday.set(self.birthday.get())

    def save(self):
        data = ({
            "ci": int(self.ci.get()),
            "first_name": self.first_name.get(),
            "last_name": self.last_name.get(),
            "direction": self.direction.get(),
            "birthday": self.birthday.get(),
            "estado_civil": self.estado_civil.get(),
            "work": bool(self.work.get()),
            "entry": float(self.entry.get()),
            "postulation": bool(self.postulation.get()),
            "discapacity": bool(self.discapacity.get()),
            "discapacity_desc": str(self.discapacity_desc.get('0.0',tk.END))
        })
        db = ViviendoModel()
        db.create(data)

    def form(self):
        # Title of the Form
        tk.Label(self.root,text="Registro de Viviendo", font="Helvetica 16 bold",
            fg="blue").place(x=310,y=60)

        # Entry of the cedula
        tk.Label(self.root,text="CI:", font="Helvetica 12",
            fg="#474747").place(x=70,y=130)
        self.ci=tk.StringVar()
        tk.Entry(self.root,textvariable=self.ci, validate='key',
            validatecommand=self.validate_number,
            width=20, bd=0, font="Helvetica 14 normal",justify="left",
            bg="#1E6FBA",fg="yellow", highlightbackground="black",
            highlightcolor="red", highlightthickness=1).place(x=100,y=130)

        # Entrada de texto para Nombre
        tk.Label(self.root,text="Nombre:", font="Helvetica 12",
            fg="#474747").place(x=27,y=165)
        self.first_name=tk.StringVar()
        tk.Entry(self.root,textvariable=self.first_name, width=20, bd=0,
            font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
            disabledbackground="#1E6FBA",disabledforeground="yellow",
            highlightbackground="black",highlightcolor="red",
            highlightthickness=1).place(x=100,y=165)

        # Entrada de texto para Apellido
        tk.Label(self.root,text="Apellido:", font="Helvetica 12",
            fg="#474747").place(x=26,y=200)
        self.last_name=tk.StringVar()
        tk.Entry(self.root,textvariable=self.last_name, width=20, bd=0,
            font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
            disabledbackground="#1E6FBA",disabledforeground="yellow",
            highlightbackground="black",highlightcolor="red",
            highlightthickness=1).place(x=100,y=200)

        # Entrada de texto para direction
        tk.Label(self.root,text="Fecha de Nacimiento:", font="Helvetica 12",
            fg="#474747").place(x=10,y=235)
        self.birthday=tk.StringVar()
        # select date
        iconCalendar = self.getImage("views/images/calendar.png", 20, 20)

        calendarButton = tk.Button(self.root, image=iconCalendar,
            command=self.getDate, bg="#1E6FBA", fg="yellow",)
        calendarButton.place(x=295,y=235)
        calendarButton.image = iconCalendar

        tk.Entry(self.root,textvariable=self.birthday, width=10, bd=0,
            font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
            disabledbackground="#1E6FBA",disabledforeground="yellow",
            highlightbackground="black",highlightcolor="red",
            highlightthickness=1).place(x=170,y=235)


        # Fields right
        # Entrada de texto para Fecha de Nacimiento
        tk.Label(self.root,text="Dirección:", font="Helvetica 12",
            fg="#474747").place(x=420,y=130)
        self.direction=tk.StringVar()
        tk.Entry(self.root,textvariable=self.direction, width=27, bd=0,
            font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
            disabledbackground="#1E6FBA",disabledforeground="yellow",
            highlightbackground="black",highlightcolor="red",
            highlightthickness=1).place(x=500,y=130)

        # Entrada de texto para estado_civil
        tk.Label(self.root,text="Estado Civil:", font="Helvetica 12",
            fg="#474747").place(x=400,y=165)
        self.estado_civil=tk.StringVar()
        tk.Entry(self.root,textvariable=self.estado_civil, width=27, bd=0,
            font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
            disabledbackground="#1E6FBA",disabledforeground="yellow",
            highlightbackground="black",highlightcolor="red",
            highlightthickness=1).place(x=500,y=165)

        # Entrada de texto para work BOOLEAN
        tk.Label(self.root,text="Trabaja:", font="Helvetica 12",
            fg="#474747").place(x=430,y=200)
        self.work=tk.BooleanVar(self.root, value=False)
        tk.Checkbutton(self.root, variable=self.work, font="Helvetica 14 normal",
            bd=0, bg="#1E6FBA", fg="black", highlightbackground="black",
            highlightcolor="red").place(x=500,y=200)

        # Entrada de texto para Ingresos
        tk.Label(self.root,text="Ingresos:", font="Helvetica 12",
            fg="#474747").place(x=425,y=235)
        self.entry=tk.StringVar()
        tk.Entry(self.root,textvariable=self.entry, validate='key',
            validatecommand=self.validate_number, width=27, bd=0,
            font="Helvetica 14 normal",justify="left",bg="#1E6FBA",
            fg="yellow", disabledbackground="#1E6FBA",
            disabledforeground="yellow", highlightbackground="black",
            highlightcolor="red", highlightthickness=1).place(x=500,y=235)

        # Entrada de texto para postulation
        tk.Label(self.root,text="Postulación:", font="Helvetica 12",
            fg="#474747").place(x=401,y=270)
        self.postulation=tk.BooleanVar(self.root, value=False)
        tk.Checkbutton(self.root, variable=self.postulation, font="Helvetica 14 normal",
            bd=0, bg="#1E6FBA", fg="black", highlightbackground="black",
            highlightcolor="red").place(x=500,y=270)

        # Entrada de texto para discapacity BOOLEAN
        tk.Label(self.root,text="Discapacidad:", font="Helvetica 12",
            fg="#474747").place(x=390,y=305)
        self.discapacity=tk.BooleanVar(self.root, value=False)
        tk.Checkbutton(self.root, variable=self.discapacity, font="Helvetica 14 normal",
            bd=0, bg="#1E6FBA", fg="black", highlightbackground="black",
            highlightcolor="red").place(x=500,y=305)

        # Entrada de texto para discapacity Description
        tk.Label(self.root,text="Describa Discapacidad:", font="Helvetica 12",
            fg="#474747").place(x=320,y=340)
        self.discapacity_desc=tk.Text(self.root, width=30, height=4, bd=0,
            font="Helvetica 12 normal",bg="#1E6FBA",fg="yellow",
            highlightbackground="black",highlightcolor="red",
            highlightthickness=1)
        self.discapacity_desc.place(x=500,y=340)

        # Buttons of actions
        # Guardar
        tk.Button(self.root, command=self.save, text="Guardar", font="Helvetica 14 normal", bd=0,
            activebackground="red", activeforeground="blue",
            bg="green", fg="white", width=12, height=2).place(x=500,y=500)