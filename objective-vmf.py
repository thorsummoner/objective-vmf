#!/usr/bin/python3
import os, sys
# User our projects 'lib' path.
sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), 'lib')))
# Give actionable messages on dependency errors.
try:
	import tkinter
	from tkinter import ttk
	import obj
except ImportError as err:
	err.msg_list = err.msg.split()
	# If this error is not Exactly the one I expect, keep throwing it.
	if len(err.msg_list) == 9 and\
		err.msg_list[3] == "'_tkinter'," and\
		err.msg_list[7] == 'python-tk':
		print('\033[2m{0}\033[0m'.format(err))
		print(str("The program '{0}' is currently not installed. You can install it by typing:\n"\
				+ "sudo apt-get install {0} --yes").format('python3-tk'))
		sys.exit()
	raise err
	sys.exit()


def main(argv):
	if argv != [__file__]:
		#TODO: implement cli 
		sys.exit()
	root = tkinter.Tk()

# DEMO CODE
	# style = ttk.Style()
	# style.theme_settings("default", {
	#    "TCombobox": {
	#        "configure": {"padding": 5},
	#        "map": {
	#            "background": [("active", "green2"),
	#                           ("!disabled", "green4")],
	#            "fieldbackground": [("!disabled", "green3")],
	#            "foreground": [("focus", "OliveDrab1"),
	#                           ("!disabled", "OliveDrab2")]
	#        }
	#    }
	# })

	# # print(style.theme_names())
	# # style.theme_use('classic')

	# combo = ttk.Combobox().pack()

	# root.mainloop()
# OLD APPLICATION
	# class Application(Frame):
# 		def __init__(self, master=None):
# 			print('[Application] initializing')
# 			self.master = master
# 			Frame.__init__(self, master)
# 			self.pack()
# 			self.createWidgets()
# 			master.protocol("WM_DELETE_WINDOW", self.exit)
# 			print('[Application] initialized')

# 		def createWidgets(self):
# 			self.quitButton = ttk.Button(self, text='Quit', command=self.quit)
# 			self.quitButton.grid()

# 			self.testButton = ttk.Button(self, text='Test', command=obj.load)
# 			self.testButton.grid()

# 		def exit(self):
# 			print('[Application] exit')
# 			self.master.destroy()
# 			self.master.quit()

# 	root = Tk()
# 	app = Application(master=root)
# 	app.mainloop()

if __name__ == "__main__":
	main(sys.argv)
