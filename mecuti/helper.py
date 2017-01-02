from datetime import datetime
import os

class Helper:

	def __init__(self):
		self.today = datetime.now()

	def generate_dir_saved(self):
		pathSaved = 'crawled'

		year = self.today.strftime('%Y_%m')
		day = self.today.strftime('%d_%H%M%S')
		# hms = self.today.strftime('%H%M%S')

		finalPath = '{}/{}/{}'.format(pathSaved, year, day)

		try:
			os.makedirs(finalPath)
			return finalPath
		except Exception as e:
			return pathSaved