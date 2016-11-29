import Tkinter as tk
import validate
import calendar

from datetime import datetime


class DateEntry(tk.Frame):
	def __init__(self, master, frame_look={}, actually="", **look):
		args = dict(relief=tk.SUNKEN, border=1)
		args.update(frame_look)
		tk.Frame.__init__(self, master, **args)

		self.actually = actually if actually else '%s-%s-%s' %(
											datetime.now().year,
											datetime.now().month,
											datetime.now().day)
		self.result=datetime.strptime(str(self.actually), '%Y-%m-%d')

		args = {'relief': tk.FLAT}
		args.update(look)


		self.entry_1 = validate.IntegerEntry(self, width=3, **args)
		self.label_1 = tk.Label(self, text='/', **args)
		self.entry_2 = validate.IntegerEntry(self, width=3, **args)
		self.label_2 = tk.Label(self, text='/', **args)
		self.entry_3 = validate.IntegerEntry(self, width=6, **args)
		self.ac=tk.Label(self, text=self.result.strftime('%Y/%m/%d'), font="Helvetica 12 normal", fg="#757575")

		if actually:
			self.entry_1.set(self.result.strftime('%d'))
			self.entry_2.set(self.result.strftime('%m'))
			self.entry_3.set(self.result.strftime('%Y'))

		self.entry_3.pack(side=tk.LEFT)
		self.label_1.pack(side=tk.LEFT)
		self.entry_2.pack(side=tk.LEFT)
		self.label_2.pack(side=tk.LEFT)
		self.entry_1.pack(side=tk.LEFT)
		self.ac.pack(side=tk.RIGHT)

		self.entry_3.bind('<KeyRelease>', self._e3_check)
		self.entry_2.bind('<KeyRelease>', self._e2_check)
		self.entry_1.bind('<KeyRelease>', self._e1_check)

	def _backspace(self, entry):
		cont = entry.get()
		entry.delete(0, tk.END)
		entry.insert(0, cont[:-1])

	def _e1_check(self, e):
		cont = self.entry_1.get()
		if not self.entry_1.get(): self.entry_1.set(01)
		if not self.entry_2.get(): self.entry_2.set(datetime.now().month)
		if not self.entry_3.get(): self.entry_3.set(datetime.now().year)
		month = calendar.monthrange(int(self.entry_3.get()),int(self.entry_2.get()))
		if cont and int(cont) <= month[1]:
			if len(cont) > 2 or not cont[-1].isdigit():
				self._backspace(self.entry_1)
				self.entry_1.focus()
		else: self.entry_1.set(value=month[1])

	def _e2_check(self, e):
		cont = self.entry_2.get()
		if cont and int(cont) <= 12:
			if len(cont) >= 2:
				self.entry_1.focus()
			if len(cont) > 2 or not cont[-1].isdigit():
				self._backspace(self.entry_2)
				self.entry_2.focus()
		else: self.entry_2.set(value=12)

	def _e3_check(self, e):
		cont = self.entry_3.get()
		if cont:
			if len(cont) >= 4:
				self.entry_2.focus()
			if len(cont) > 4 or not cont[-1].isdigit():
				self._backspace(self.entry_3)

	def get(self):
		date = '%s-%s-%s' %(self.entry_3.get(), self.entry_2.get(), self.entry_1.get())
		self.result = date if date != '--' else self.result
		return self.result