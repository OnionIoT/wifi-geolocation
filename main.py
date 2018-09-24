# this program will periodically scan nearby wifi networks and geolocate and print the gps coordinates

import json, os, sys
import geolocation
from time import sleep

# find the directory of the script
dirName = os.path.dirname(os.path.abspath(__file__))

# defines & global vars
DEFAULT_SCAN_INTERVAL = 5
CONFIG_FILE = 'config.json'


config = {}


# read configuration file
def readConfigFile():
	global config
	filepath = '/'.join([dirName, CONFIG_FILE])
	with open( filepath ) as f:
		try:
			config = json.load(f)
		except:
			print("ERROR: expecting JSON file")
			return False
		if 'apiKey' not in config:
			print("ERROR: expecting config file to have 'apiKey' member")
			return False
		if 'scanInterval' not in config:
			config['scanInterval'] = DEFAULT_SCAN_INTERVAL
		print('> Successfully read config file')
		# print(config)
		return True

def __main__():
	global config
	if not readConfigFile():
		sys.exit()

	while True:
		# scan the wifi networks, and get geolocation data from API
		data = geolocation.getGeolocation(config['apiKey'])
		# display the data
		geolocation.displayGeolocation(data)

		# sleep
		sleep(config['scanInterval'])

if __name__ == '__main__':
	__main__()
