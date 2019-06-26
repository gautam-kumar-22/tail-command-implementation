"""

Tail command implementation Python
Usage:
tail.py filename linenumbers

"""
import sys

class TailImplementation(object):
	"""docstring for TailImplementation"""
	def __init__(self, *args, **kwargs):
		super(TailImplementation, self).__init__()
		self.filename = args[0]
		self.linenumbers = -int(args[1])
		print(args[0])

	def help(self):
		"""Help command"""		
		print("Help")

	def tailcommand(self):
		"""Tail command implementation"""
		file = open(self.filename, 'r')
		content = file.read().splitlines()[self.linenumbers::]
		print(content)
		file.close()


if __name__ == '__main__':
	if len(sys.argv) < 3 or len(sys.argv) > 3:
		print(""""Error:  Usage:
		tail.py filename linenumbers""")
		exit()
	file_name = sys.argv[1]
	linenumbers = sys.argv[2]
	tail = TailImplementation(file_name, linenumbers)
	tail.tailcommand()
