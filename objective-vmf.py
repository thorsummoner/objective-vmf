#!/usr/bin/python3
import sys, os
# User our projects 'lib' path.
sys.path.append(os.path.realpath(os.path.join(os.path.dirname(__file__), 'lib')))
try:
	from gi.repository import Gtk, Gdk, Gio
	import obj
except ImportError as err:
	# Wrap any specific, common, import shortfalls here.
	# EG. Common missing dependencies.
	raise err;
	sys.exit()

# help(Gtk.ApplicationWindow);sys.exit()

def main(argv):
	if argv != [__file__]:
		print('[Application] CLI Mode')
		#TODO: implement cli 
		return
	print('[Application] Graphical Mode')
	class ObjectiveVmfWindow(Gtk.ApplicationWindow):
		def __init__(self, app):
			print('[Application] initializing ... ')
			Gtk.Window.__init__(self, application=app)
			self.set_title('Objective Vmf')
			self.set_icon_from_file('asset/objective-vmf_128x128.png')
			# self.set_default_size(400, 200)

			grid = Gtk.Grid()
			self.add(grid)
			grid.show()

			ui_element_main = Gtk.Builder()
			ui_element_main.add_from_file('asset/objective-vmf-main.glade')

			grid.attach(ui_element_main.get_object('main'), 0, 0, 1, 1)

			print('[Application] initialized')
		def do_delete_event(self, event):
			print('[Application] exit')
			# Gtk.ApplicationWindow.do_delete_event(self, event)
			sys.exit()


	class ObjectiveVmfApplication(Gtk.Application):
		def __init__(self):
			Gtk.Application.__init__(self)

		def do_activate(self):
			win = ObjectiveVmfWindow(self)
			win.show()

		def do_startup(self):
			Gtk.Application.do_startup(self)


	app = ObjectiveVmfApplication()
	sys.exit(app.run(sys.argv))

	return


	# class ObjectiveVmf(Gtk.Builder):
	# 	def __init__(self):
	# 		print('[Application] initializing')
	# 		super(ObjectiveVmf, self).__init__()
	# 		self.add_from_file('asset/objective-vmf-main.glade')
	# 		self.connect_signals(self)

	# 		window = self.get_object('main')

	# 		print('[Application] initialized')
	# 		window.show_all()

	# 	def test(self, widget):
	# 		print('test')
	# 		self.exit(self)

	# 	def exit(self, args=None, kwargs=None):
	# 		print('[Application] exit')
	# 		Gtk.main_quit(self, args, kwargs)

	# ObjectiveVmf();
	# # application = ObjectiveVmf();

	# # builder = Gtk.Builder()
	# # builder.add_from_file("asset/objective-vmf-main.glade")
	# # builder.connect_signals(application)

	# # window = builder.get_object("main")
	# # window.show_all()

	# # # try:
	# # Gtk.main()
	# # # except KeyboardInterrupt:
	# # # 	application.exit()


if __name__ == "__main__":
	try:
		main(sys.argv)
	except KeyboardInterrupt:
		pass
