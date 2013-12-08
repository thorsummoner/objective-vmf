#!/usr/bin/python3
import os, sys
# User our projects 'lib' path.
sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), 'lib')))
try:
	from gi.repository import Gtk
	import obj
except ImportError as err:
	# Wrap any specific, common, import shortfalls here.
	raise err;
	sys.exit()

def main(argv):
	if argv != [__file__]:
		#TODO: implement cli 
		sys.exit()

	class ObjectiveVmf(Gtk.Window):
		def __init__(self):
			print('[Application] initializing')

			print('[Application] initialized')

		def test(self, widget):
			print('test')
			self.exit(self)

		def exit(self, args=None, kwargs=None):
			print('[Application] exit')
			Gtk.main_quit(self, args, kwargs)

	application = ObjectiveVmf();

	builder = Gtk.Builder()
	builder.add_from_file("asset/objective-vmf-main.glade")
	builder.connect_signals(application)

	window = builder.get_object("main")
	window.show_all()

	# try:
	Gtk.main()
	# except KeyboardInterrupt:
	# 	application.exit()


if __name__ == "__main__":
	main(sys.argv)
