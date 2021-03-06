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
from ttk import *

class ValidatingEntry(Entry):
	# base class for validating entry widgets

	def __init__(self, master, value="", maxlength=None, **kw):
		Entry.__init__(self, master, **kw)
		self.__value = value
		self.__variable = StringVar()
		self.__variable.set(value)
		self.__variable.trace("w", self.__callback)
		self.config(textvariable=self.__variable)
		self.results = StringVar()
		self.maxlength = maxlength
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
	
	def get(self):
		result = self.results.get()
		return self.getresults(result)

	def set(self, value):
		self.__variable.set(value)

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
			if self.maxlength is None or len(value) <= self.maxlength:
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
		ValidatingEntry.__init__(self, master, value=value, **kw)

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
		ValidatingEntry.__init__(self, master, value=value, **kw)

	def getresults(self, value):
		if self.maxlength:
				if len(value) > self.maxlength:
						value = value[:self.maxlength]
						self.results.set(value)
		return self.results.get()


class StringEntry(ValidatingEntry):
		#same as ValidatingEntry; nothing extra
		pass