#!/usr/bin/python
import Tkinter as tk
import ttk, sys, obj
obj.load('monkey_vector')
sys.exit()

class Application(tk.Frame):
	def __init__(self, master=None):
		print('initializing')
		tk.Frame.__init__(self, master)
		self.master.title('Application')
		self.grid()
		self.createWidgets()
	def createWidgets(self):
		self.quitButton = ttk.Button(self, text='Quit', command=self.quit)
		self.quitButton.grid()

		self.testButton = ttk.Button(self, text='Test', command=obj.load)
		self.testButton.grid()
	def quit(self):
		print('terminating')
		sys.exit()

Application().mainloop()
