import Tkinter as tk
from lib import tkSimpleDialog
import validate


class FloatDialog(tkSimpleDialog.Dialog):
	"""Dialog box that displays a text fields and return it"""
	def body(self, master, message, value):
		tk.Label(master, text=message,
			font="Helvetica 12 normal").pack(side=tk.TOP, pady=10)

		self.value=validate.FloatEntry(master, value=value,
			width=12, bd=0, font="Helvetica 14 normal",
			justify="left",bg="#1E6FBA",fg="yellow",
			highlightbackground="black",highlightcolor="red",
			highlightthickness=1)
		self.value.pack(pady=8)

	def apply(self):
		self.result = float(self.value.get())
