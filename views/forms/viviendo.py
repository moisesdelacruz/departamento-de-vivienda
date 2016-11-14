from Tkinter import *

class FormViviendo(object):

    def __init__(self, root):
        self.root = root
        self.form()

    def form(self):
        # Entrada de texto para CI
        Label(self.root,text="CI:").place(x=20,y=83)
        ci=StringVar(self.root, value='0')
        Entry(self.root,textvariable=ci, width=18, bd=0,
            font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
            highlightbackground="black",highlightcolor="red",
            highlightthickness=1).place(x=50,y=80)

        # Entrada de texto para Nombre
        Label(self.root,text="First_name:").place(x=20,y=110)
        first_name=StringVar()
        Entry(self.root,textvariable=first_name, width=37, bd=0,
            font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
            disabledbackground="#1E6FBA",disabledforeground="yellow",
            highlightbackground="black",highlightcolor="red",
            highlightthickness=1).place(x=205,y=110)

        # Entrada de texto para Aprellido
        Label(self.root,text="Last_name:").place(x=20,y=140)
        last_name=StringVar()
        Entry(self.root,textvariable=last_name, width=37, bd=0,
            font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
            disabledbackground="#1E6FBA",disabledforeground="yellow",
            highlightbackground="black",highlightcolor="red",
            highlightthickness=1).place(x=205,y=140)

        # Entrada de texto para direction
        Label(self.root,text="Direccion:").place(x=20,y=170)
        direction=StringVar()
        Entry(self.root,textvariable=direction, width=37, bd=0,
            font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
            disabledbackground="#1E6FBA",disabledforeground="yellow",
            highlightbackground="black",highlightcolor="red",
            highlightthickness=1).place(x=205,y=170)

        # Entrada de texto para Fecha de Nacimiento
        Label(self.root,text="Fecha de Nacimiento:").place(x=20,y=200)
        birthday=StringVar()
        Entry(self.root,textvariable=birthday, width=37, bd=0,
            font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
            disabledbackground="#1E6FBA",disabledforeground="yellow",
            highlightbackground="black",highlightcolor="red",
            highlightthickness=1).place(x=205,y=200)

        # Entrada de texto para estado_civil
        Label(self.root,text="Estado Civil:").place(x=20,y=230)
        estado_civil=StringVar()
        Entry(self.root,textvariable=estado_civil, width=37, bd=0,
            font="Helvetica 14 normal",justify="left",bg="#1E6FBA",fg="yellow",
            disabledbackground="#1E6FBA",disabledforeground="yellow",
            highlightbackground="black",highlightcolor="red",
            highlightthickness=1).place(x=205,y=230)
