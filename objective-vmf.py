#!/usr/bin/python3
import os, sys
# User our projects 'lib' path.
sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), 'lib')))
try:
	from gi.repository import Gtk
	import obj
except ImportError as err:
	raise err;
	sys.exit()

def main(argv):
	if argv != [__file__]:
		#TODO: implement cli 
		sys.exit()

	class ObjectiveVmf(Gtk.Window):
		def __init__(self):
			print('[Application] initializing')
			Gtk.Window.__init__(self, title="Objective Vmf")

			self.button = Gtk.Button(label="Test")
			self.button.connect("clicked", self.test)
			self.add(self.button)

			print('[Application] initialized')

		def test(self, widget):
			print('test')
			self.exit(self)

		def exit(self, args=None, kwargs=None):
			print('[Application] exit')
			Gtk.main_quit(self, args, kwargs)


	win = ObjectiveVmf()
	win.connect("delete-event", win.exit)
	win.show_all()
	Gtk.main()

if __name__ == "__main__":
	main(sys.argv)
