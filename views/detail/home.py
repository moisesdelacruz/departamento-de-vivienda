#!/usr/bin/python
# -*- coding: utf-8 -*-

import Tkinter as tk
import ttk

from utils.methods import Methods
from utils.clock import Clock
from views.forms.search import SearchForm
from views.detail.user.main import ConfigView

class HomeView(tk.Frame, Methods):
	def __init__(self, root, **kwargs):
		tk.Frame.__init__(self, root)
		self.root = root
		if kwargs.get('session'):
			self.session = kwargs.get('session')
			self.account = self.session.content_session
		self.view()

	def viviendo(self):
		self.clean(self.root)
		SearchForm(self.root, session=self.session)

	def config(self):
		self.clean(self.root)
		ConfigView(self.root, session=self.session)


	def view(self):
		div = ttk.Frame(self.root, height=550, style='Kim.TFrame')
		div.pack(expand=True, fill=tk.X)
		div.pack_propagate(0)

		view = ttk.Frame(div, width=650, style='White.TFrame')
		view.pack(expand=True, fill=tk.Y)
		view.pack_propagate(0)

		ttk.Label(view, text=' '.join(['Bienvenido',
			self.account.get('first_name'),
			self.account.get('last_name')]),
			style='Black22.TLabel').pack(pady=20)

		box_time=ttk.Frame(view, style='White.TFrame', padding=32)
		box_time.pack(anchor=tk.NW)

		# time=ttk.Label(box_time, text='', style='Hour.TLabel')
		# time.pack()
		Clock(box_time)


		# ------box-------
		box = ttk.Frame(view, style='White.TFrame')
		box.pack(anchor=tk.CENTER)
		# boxs----------
		# option config
		config=ttk.Frame(box, width=250, height=120, style='Kim.TFrame')
		config.pack(side=tk.LEFT, padx=15, pady=30)
		icon_config=self.getImage("views/images/btn-config.png", 276, 129)
		btn_config=tk.Button(config, bd=0, image=icon_config, command=self.config)
		btn_config.image=icon_config
		btn_config.pack(pady=10)

		# option viviendo
		viviendo=ttk.Frame(box, width=250, height=120, style='Item.TFrame')
		viviendo.pack(side=tk.LEFT, padx=15, pady=30)
		icon_viviendo=self.getImage("views/images/btn_viviendo.png", 276, 129)
		btn_viviendo=tk.Button(viviendo, bd=0, image=icon_viviendo, command=self.viviendo)
		btn_viviendo.image=icon_viviendo
		btn_viviendo.pack(pady=10)


		# last inicio of session
		box5 = tk.Frame(view)
		box5.pack(side=tk.BOTTOM, anchor=tk.SE)
		tk.Label(box5, text="Ultimo Inicio de Sesión:",
			font="Helvetica 12 normal", fg="#6b6a6a").pack(pady=10, side=tk.LEFT)
		tk.Label(box5, text="13/12/1989 08:27 a.m.",
			font="Helvetica 12 normal", fg="blue").pack(pady=10, side=tk.LEFT)
