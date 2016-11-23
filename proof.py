#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
# from Tkinter import *
# import ttk
# from utils.methods import Methods
 
# # Calcula coste de viaje con validación y cálculo inmediato
 
# class Aplicacion(Methods):
#     def __init__(self):
#         self.raiz = Tk()
#         self.raiz.title("Alta Velocidad")
		 
#         # Declara variables de control
									
#         self.num_via = IntVar(value=1)
#         self.ida_vue = BooleanVar()        
#         self.clase   = StringVar(value='t')
#         self.km = IntVar(value=1)        
#         self.precio = DoubleVar(value=0.10)
#         self.total = DoubleVar(value=0.0)
		 
#         # Define trazas con la variables de control de los widgets Entry()
#         # para detectar cambios en los datos. Si se producen cambios
#         # se llama a la función 'self.calcular' para validación y para
#         # calcular importe a pagar
		 
#         self.km.trace('w', self.calcular)
#         self.precio.trace('w', self.calcular)
		 
#         # Llama a función para validar y calcular
		 
#         self.calcular()
		 
#         # Carga imagen para asociar a widget Label()
				 
#         tren = self.getImage('tren-128x64.png', 128, 64)  
		 
#         # Declara widgets de la ventana
#         # En los widgets de tipo Spinbox, Checkbutton y Radiobutton
#         # se utiliza la opción 'command' para llamar a la función 
#         # 'self.calcular' para validar datos y calcular importe a 
#         # pagar de forma inmediata
			   
#         self.imagen1 = ttk.Label(self.raiz, image=tren, anchor="center")
#         self.etiq1 = ttk.Label(self.raiz, text="Viajeros:")                               
#         self.viaje = Spinbox(self.raiz, from_=1, to=20, wrap=True,
#                              textvariable=self.num_via, state='readonly',
#                              command=self.calcular)                                                              
#         self.idavue = ttk.Checkbutton(self.raiz, text='Ida y vuelta', 
#                                       variable=self.ida_vue, 
#                                       onvalue=True, offvalue=False, 
#                                       command=self.calcular)
#         self.etiq2 = ttk.Label(self.raiz, text="Clase:")
#         self.clase1 = ttk.Radiobutton(self.raiz, text='Turista', 
#                                       variable=self.clase, value='t',
#                                       command=self.calcular)
#         self.clase2 = ttk.Radiobutton(self.raiz, text='Primera', 
#                                       variable=self.clase, value='p',
#                                       command=self.calcular)
#         self.clase3 = ttk.Radiobutton(self.raiz, text='Lujo', 
#                                       variable=self.clase, value='l',
#                                       command=self.calcular)        
#         self.etiq3 = ttk.Label(self.raiz, text="Distancia (Kilómetros):")                                                                                                   
#         self.dist = ttk.Entry(self.raiz, textvariable=self.km, width=10)                
#         self.etiq4 = ttk.Label(self.raiz, text="Precio:")
#         self.coste = ttk.Entry(self.raiz, textvariable=self.precio, width=10)        
#         self.etiq5 = ttk.Label(self.raiz, text="A Pagar (euros):")        
#         self.etiq6 = ttk.Label(self.raiz, textvariable=self.total,
#                                foreground="yellow", background="black",
#                                borderwidth=5, anchor="e")                                
#         self.separ1 = ttk.Separator(self.raiz, orient=HORIZONTAL)
				 
#         self.boton1 = ttk.Button(self.raiz, text="Salir", 
#                                  command=quit)                                 
													  
#         self.imagen1.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
#         self.etiq1.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
#         self.viaje.pack(side=TOP, fill=X, expand=True, padx=20, pady=5)
#         self.idavue.pack(side=TOP, fill=X, expand=True, padx=20, pady=5)
#         self.etiq2.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
#         self.clase1.pack(side=TOP, fill=BOTH, expand=True, padx=20, pady=5)
#         self.clase2.pack(side=TOP, fill=BOTH, expand=True, padx=20, pady=5)
#         self.clase3.pack(side=TOP, fill=BOTH, expand=True, padx=20, pady=5)
#         self.etiq3.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
#         self.dist.pack(side=TOP, fill=X, expand=True, padx=20, pady=5)
#         self.etiq4.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
#         self.coste.pack(side=TOP, fill=X, expand=True, padx=20, pady=5)
#         self.etiq5.pack(side=TOP, fill=BOTH, expand=True, padx=10, pady=5)
#         self.etiq6.pack(side=TOP, fill=BOTH, expand=True, padx=20, pady=5)        
#         self.separ1.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
#         self.boton1.pack(side=RIGHT, fill=BOTH, expand=True, padx=10, pady=10)
#         self.raiz.mainloop()
		 
#     def calcular(self, *args):
		 
#         # Función para validar datos y calcular importe a pagar
		 
#         error_dato = False
#         total = 0
#         try:
#             km = int(self.km.get())
#             precio = float(self.precio.get())
#         except:
#             error_dato = True   
#         if not error_dato:
#             total =  self.num_via.get() * km * precio
#             if self.ida_vue.get():
#                 total = total * 1.5
#             if self.clase.get() == 'p':
#                 total = total * 1.2
#             elif self.clase.get() == 'l':
#                 total = total * 2
#             self.total.set(total)                
#         else:
#             self.total.set("¡ERROR!")
			 
# def main():
#     mi_app = Aplicacion()
#     return 0
 
# if __name__ == '__main__':
#     main()


# import Tkinter as tk

# class Example(tk.Frame):
# 	def __init__(self, root):

# 		tk.Frame.__init__(self, root)
# 		self.canvas = tk.Canvas(root, borderwidth=0, background="#ffffff")
# 		self.frame = tk.Frame(self.canvas, background="#ffffff")
# 		self.vsb = tk.Scrollbar(root, orient="vertical", command=self.canvas.yview)
# 		self.canvas.configure(yscrollcommand=self.vsb.set)

# 		self.vsb.pack(side="right", fill="y")
# 		self.canvas.pack(side=tk.LEFT)
# 		self.canvas.create_window((4,4), window=self.frame, anchor="nw", 
# 								  tags="self.frame")

# 		self.frame.bind("<Configure>", self.onFrameConfigure)

# 		self.populate()

# 	def populate(self):
# 		'''Put in some fake data'''
# 		for row in range(100):
# 			tk.Label(self.frame, text="%s" % row, width=3, borderwidth="1", 
# 					 relief="solid").grid(row=row, column=0)
# 			t="this is the second column for row %s" %row
# 			tk.Label(self.frame, text=t).grid(row=row, column=1)

# 	def onFrameConfigure(self, event):
# 		'''Reset the scroll region to encompass the inner frame'''
# 		self.canvas.configure(scrollregion=self.canvas.bbox("all"))

# if __name__ == "__main__":
# 	root=tk.Tk()
# 	Example(root).pack(side="top", fill="both", expand=True)
# 	root.mainloop()



# ----------------------


'''
Info by Fredrik Lundh:
This module implements a validating version of the Tkinter Entry widget.
It uses the textvariable option to attach a StringVar to the widget,
and uses the variable trace function to keep track of what's going on (in real time, as the user types the input).
To specify how validation is to be done, override the validate method.
Note that the constructor takes a parent widget, and also allows you to use the value option to specify the initial contents.
All other options are passed on to the Entry widget itself.
'''

from Tkinter import *

class ValidatingEntry(Entry):
	# base class for validating entry widgets

	def __init__(self, master, value="", **kw):
		Entry.__init__(self, master, **kw)
		self.__value = value
		self.__variable = StringVar()
		self.__variable.set(value)
		self.__variable.trace("w", self.__callback)
		self.config(textvariable=self.__variable)
		self.results = StringVar()
		if self.__value is None: self.results.set(None)
		else:
				self.results.set(self.__value)

	def __callback(self, *dummy):
		value = self.__variable.get()
		newvalue = self.validate(value)
		if newvalue is None:
			self.__variable.set(self.__value)
		elif newvalue != value:
			self.__value = newvalue
			self.__variable.set(newvalue)
		else:
			self.__value = value

	def validate(self, value):
		# override: return value, new value, or None if invalid
		self.results.set(value)
		return value

	def getresults(self, value):
		# override: return value, or chopped value in the case of ChopLengthEntry
		return self.results.get()

'''
The first two examples are subclasses that check that the input is a valid Python integer or float, respectively.
The validate method simply tries to convert the value to an object of the right kind, and returns None (reject) if that fails.
'''

class IntegerEntry(ValidatingEntry):
	def validate(self, value):
		try:
			if value:
				v = int(value)
				self.results.set(value)
			return value
		except ValueError:
			return None


class FloatEntry(ValidatingEntry):
	def validate(self, value):
		try:
			if value:
				v = float(value)
				self.results.set(value)
			return value
		except ValueError:
			return None


class MaxLengthEntry(ValidatingEntry):
	'''MaxLength is a subclass that restricts the length of the input to a given max length.
	   The getresults method is provided only to deal with a situation where a too-long
	   initial value is provided, and the user accepts it without editing.
	   Also if a too-long initial value is provided, it must be truncated to at least one char
	   less than the max length, or else the user will be unable to even edit it
	   (since the Del or BS key would cause the length to exceed the maxlength, they would be ignored)'''
	def __init__(self, master, value="", maxlength=None, **kw):
		if len(value) > maxlength-1:
				value = value[:maxlength-1]
		self.maxlength = maxlength
		ValidatingEntry.__init__(self, master, value=value)

	def validate(self, value):
		if self.maxlength is None or len(value) <= self.maxlength:
				self.results.set(value)
				return value
		return None # new value too long

	def getresults(self, value):
		if self.maxlength:
				if len(value) > self.maxlength:
						value = value[:self.maxlength]
						self.results.set(value)
		return self.results.get()

class ChopLengthEntry(ValidatingEntry):
	'''ChopLengthEntry accepts all entries, but chops them when the results are called for'''
	def __init__(self, master, value="", maxlength=None, **kw):
		self.maxlength = maxlength
		ValidatingEntry.__init__(self, master, value=value)

	def getresults(self, value):
		if self.maxlength:
				if len(value) > self.maxlength:
						value = value[:self.maxlength]
						self.results.set(value)
		return self.results.get()


class StringEntry(ValidatingEntry):
		#same as ValidatingEntry; nothing extra
		pass

if __name__ == '__main__':
		labelString = ['Integer','Float','String','MaxLength','ChopLength']
		limitString = ['MaxLength','ChopLength']
		initial     = [123, 456.789, '"hello, world!"', '"long text"', '"Please don\'t cut me!"']
		num = len(labelString)

		entry = [None]*num; value = [None]*num

		def results():
				resultsList = []
				for i in range(num):
						value[i] = entry[i].results.get()
						value[i] = entry[i].getresults(value[i])
						if value[i] is not None:
								resultsList.append( value[i] )
				for x,y in zip(labelString, resultsList):
						print "validated %s entry is: %s" % (x, y)
				root.destroy()

		root = Tk()
		lab = []; but = []; entry = []
		#if we put the names of the various widget into a list, we can create instances
		#  using a for loop. Note that we need to handle
		#  the special case that 2 of them have a 2nd argument, while the others don't
		# (alternatively, could have re-defined the widgets to all take a (sometimes unneeded) 2nd argument)
		for i in range(num):
				but.append(None)
				lab.append(Label(text = 'please enter a '+labelString[i]))
				lab[-1].pack(side='top')
				if labelString[i] in limitString:
						entry.append(eval(labelString[i] + 'Entry')(root, value=initial[i], maxlength=10))
				else:
						entry.append(eval(labelString[i] + 'Entry')(root, value=initial[i]))
				entry[-1].pack()

		bt = Button(text = 'Ok', command = results)
		bt.pack(side='left')
		cn = Button(text = 'Cancel', command = root.destroy)
		cn.pack(side='left')
		mainloop()