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
			justify="left",bg="white",fg="#6b6a6a",
			highlightthickness=0)
		self.value.pack(pady=8)

	def apply(self):
		self.result = float(self.value.get())
