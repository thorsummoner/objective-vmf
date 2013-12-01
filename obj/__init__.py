#obj
import os
def load(fname):
	fullyQualifiedName = fname
	# Try all file name corrections until file exists
	from pprint import pprint
	pprint(
		os.path.exists(fullyQualifiedName),
	)
	pprint(
		os.path.dirname(os.path.realpath(__file__)) + '\\obj_sample\\' + fname
	)
	# Open file
	#instantiate obj class on file content
	#return obj.

class obj:
	def __init__(self):
		pass
