#obj
import os
def load(fname='monkey_vector.obj', directory='obj_sample'):
	fileExists = False;
	from pprint import pprint
	# Try all file name corrections until file exists
	fullyQualifiedName = fname
	#TODO: write a debug print class that can be turned off in production releases
	#pprint(fullyQualifiedName)
	#pprint(os.path.exists(fullyQualifiedName))
	fileExists = fileExists or os.path.exists(fullyQualifiedName)

	fullyQualifiedName = directory + fname
	#pprint(fullyQualifiedName)
	#pprint(os.path.exists(fullyQualifiedName))
	fileExists = fileExists or os.path.exists(fullyQualifiedName)

	fullyQualifiedName = directory + '/' + fname
	#pprint(fullyQualifiedName)
	#pprint(os.path.exists(fullyQualifiedName))
	fileExists = fileExists or os.path.exists(fullyQualifiedName)

	fullyQualifiedName = os.path.dirname(os.path.realpath(__file__)) + '/' + directory + '/' + fname
	#pprint(fullyQualifiedName)
	#pprint(os.path.exists(fullyQualifiedName))
	fileExists = fileExists or os.path.exists(fullyQualifiedName)

	fullyQualifiedName += '.obj'
	#pprint(fullyQualifiedName)
	#pprint(os.path.exists(fullyQualifiedName))
	fileExists = fileExists or os.path.exists(fullyQualifiedName)

	#pprint(fileExists)
	#TODO: Collapse ^this into a loop, control tables? or file open library maybe?
	if True != fileExists:
		return False #TODO: write a application failure class to handle these

	try:
		with open(fullyQualifiedName, 'r', 0) as fileHandle:
			model = obj(fileHandle)

	except IOError:
		return False #TODO: write a application failure class to handle these

	return None
class obj:
	modelRaw = {
		'#':  [None],
		'v':  [None],
		'l':  [None],
		'vt': [None],
		'vn': [None],
		'vp': [None],
		'f':  [None],
		'o':  [None],
		'g':  [None],
		's':  [None],
	}

	def __init__(self, reference):
		from pprint import pprint
		controlTable = {
			file: '_parseFromFileHandle',
			str : '_parseFromPlainText',
		}
		for dataType, method in controlTable.iteritems():
			if not isinstance(reference, dataType):
				continue
			parsedModel = getattr(self, method)(reference)
			# pprint(parsedModel)
			# pprint(self.modelRaw['#'])

	def _parseLine(self, line):
		from pprint import pprint
		lineParts = line.split()
		lineKey   = lineParts.pop(0)
		try:
			self.modelRaw[lineKey]
		except KeyError:
			subParseMethod = '_subParse' + lineKey[0].upper() + lineKey[1:]
			try:
				getattr(self, subParseMethod)(line) #TODO: write built in type extensions for additional string methods like 'ucfrist'
			except AttributeError:
				print('Sub parse method not defined: ' + subParseMethod)

	def _parseFromFileHandle(self, fileHandle):
		for line in fileHandle:
			self._parseLine(line)
	def _parseFromPlainText(self, raw):
		return 'text banana'
