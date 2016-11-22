import Tkinter as tk
from lib import tkSimpleDialog


class TextDialog(tkSimpleDialog.Dialog):
	"""Dialog box that displays a text fields and return it"""
	def body(self, master, message):
		tk.Label(master, text=message,
			font="Helvetica 12 normal").pack(side=tk.TOP, pady=10)

		self.value = tk.Text(master, width=30, height=6, bd=1,
			font="Helvetica 12 normal",bg="white",fg="black",
			highlightbackground="black",highlightcolor="red",
			highlightthickness=1)
		self.value.pack(side=tk.TOP)

	def apply(self):
		self.result = str(self.value.get('0.0',tk.END))
