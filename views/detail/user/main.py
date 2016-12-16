#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import ttk
import Tkinter as tk

from utils.methods import Methods
from views.detail.user.profile import ProfileView
from views.detail.user.users_list import UsersListDetail
from views.forms.user.register import RegisterForm
from views import detail


class ConfigView(tk.Frame, Methods):
	def __init__(self, root, controller, **kwargs):
		tk.Frame.__init__(self, root)
		self.root = root
		self.controller = controller

		self._menu = tk.Frame(self.root, width=300, bd=1,
			background="white")
		self._menu.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
		self._menu.pack_propagate(0)

		self._body = ttk.Frame(self.root, width=2000, style='Kim.TFrame')
		self._body.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
		self._body.pack_propagate(0)

		self.methods = ['my_profile', 'edit_user',
			'user_list', 'new_user', 'exit']

		# init view
		self.menu()

		if kwargs.get('view'):
			view=kwargs.get('view')
			for item in self.methods:
				if view == item:
					eval('self.'+item+'()')
		else: self.my_profile()


	def menu(self):

		iconConfig = self.getImage("views/images/config.png", 30,30)
		t=ttk.Label(self._menu, text=" Configuracion",
			image=iconConfig, style="Text.TLabel",
			padding=10, compound=tk.LEFT)
		t.image = iconConfig
		t.pack(anchor=tk.NW, padx=2, pady=1, fill=tk.BOTH)

		# options------
		for x in xrange(1,6):
			locals()['icon'+str(x)]=self.getImage(
				"views/images/config_btn_"+str(x)+".png", 320, 55)
			locals()['btn'+str(x)]=tk.Button(self._menu,
				image=locals()['icon'+str(x)], bd=0,
				justify=tk.LEFT, command=eval('self.'+self.methods[x-1]))
			locals()['btn'+str(x)].image=locals()['icon'+str(x)]
			locals()['btn'+str(x)].pack(anchor=tk.NW, padx=2, pady=1, fill=tk.BOTH)



	def my_profile(self):
		self.clean(self._body)
		ProfileView(self._body, self.controller)

	def user_list(self):
		self.clean(self._body)
		UsersListDetail(self._body, self.controller)

	def new_user(self):
		self.clean(self._body)
		RegisterForm(self._body, self.controller)

	def edit_user(self):
		self.clean(self._body)
		RegisterForm(self._body, self.controller, action='edit_me')

	def exit(self):
		self.clean(self.root)
		detail.home.HomeView(self.root, self.controller)