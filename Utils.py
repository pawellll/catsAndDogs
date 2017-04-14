import os
from os import listdir, makedirs
from os.path import isfile, join, exists
from time import gmtime, strftime

class Utils:
	def __init__(self):
		pass

	@staticmethod
	def files_in_path(path):
		return [f for f in listdir(path) if isfile(join(path, f))]

	@staticmethod
	def maybe_create_directory(directory):
		if not os.path.exists(directory):
			os.makedirs(directory)
			