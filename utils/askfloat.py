import Tkinter as tk
from lib import tkSimpleDialog
import validate


class FloatDialog(tkSimpleDialog.Dialog):
	"""Dialog box that displays a text fields and return it"""
	def body(self, master, message, value):
		tk.Label(master, text=message,
			font="Helvetica 12 normal").pack(side=tk.TOP, pady=10)

		self.value=validate.FloatEntry(master,
			width=12, font="Helvetica 14 normal",
			justify="left")
		if value: self.value.set(value)
		self.value.pack(pady=8)

	def apply(self):
		try:
			v = float(self.value.get())
			self.result = v
		except ValueError:
			self.result = float(0)
