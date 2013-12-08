#!/usr/bin/python3
import sys
try:
	from Tkinter import *
	import ttk
	import obj
# Not explicit, This catches missing py-tk stacktrace and instruct corrective actions.
except ImportError as err:
	try:
		missing_package = err.__str__().split()[7];
		print '\033[2m{0}\033[0m'.format(err)
		print ("The program '{0}' is currently not installed. You can install it by typing:\n"\
			+ "sudo apt-get install {0}").format(err.__str__().split()[7])
	except IndexError:
		raise err
	sys.exit()


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
