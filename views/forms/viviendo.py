from Tkinter import *

class FormViviendo(object):

    def __init__(self, root):
        self.root = root
        self.form()

    def form(self):
        # Entrada de texto para CI
        textlabel2=Label(self.root,text="CI:").place(x=100,y=80)
        ci=StringVar(self.root, value='0')
        entry=Entry(self.root,textvariable=ci, width=37).place(x=205,y=80)

        # Entrada de texto para Nombre
        textlabel2=Label(self.root,text="First_name:").place(x=100,y=110)
        first_name=StringVar()
        entry=Entry(self.root,textvariable=first_name, width=37).place(x=205,y=110)

        # Entrada de texto para Aprellido
        textlabel2=Label(self.root,text="Last_name:").place(x=100,y=140)
        last_name=StringVar()
        entry=Entry(self.root,textvariable=last_name, width=37).place(x=205,y=140)

        # Entrada de texto para direction
        textlabel2=Label(self.root,text="Direccion:").place(x=100,y=170)
        direction=StringVar()
        entry=Entry(self.root,textvariable=direction, width=37).place(x=205,y=170)

        # Entrada de texto para Fecha de Nacimiento
        textlabel2=Label(self.root,text="Fecha de Nacimiento:").place(x=100,y=200)
        birthday=StringVar()
        entry=Entry(self.root,textvariable=birthday, width=37).place(x=205,y=200)

        # Entrada de texto para estado_civil
        textlabel2=Label(self.root,text="Estado Civil:").place(x=100,y=230)
        estado_civil=StringVar()
        entry=Entry(self.root,textvariable=estado_civil, width=37).place(x=205,y=230)
