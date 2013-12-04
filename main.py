#!/usr/bin/python2
import sys
from Tkinter import *
import ttk
import obj

def main(argv):
	class Application(Frame):
		def __init__(self, master=None):
			print('[Application] initializing')
			self.master = master
			Frame.__init__(self, master)
			self.pack()
			self.createWidgets()
			master.protocol("WM_DELETE_WINDOW", self.exit)
			print('[Application] initialized')

		def createWidgets(self):
			self.quitButton = ttk.Button(self, text='Quit', command=self.quit)
			self.quitButton.grid()

			self.testButton = ttk.Button(self, text='Test', command=obj.load)
			self.testButton.grid()

		def exit(self):
			print('[Application] exit')
			self.master.destroy()
			self.master.quit()

	root = Tk()
	app = Application(master=root)
	app.mainloop()

if __name__ == "__main__":
	main(sys.argv)
