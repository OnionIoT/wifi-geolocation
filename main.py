# this program will periodically scan nearby wifi networks and geolocate and print the gps coordinates

import json, os, sys
import helpers
from time import sleep

# find the directory of the script
dirName = os.path.dirname(os.path.abspath(__file__))

# defines & global vars
DEFAULT_SCAN_INTERVAL = 5
CONFIG_FILE = 'config.json'

fieldLengths = {
	"Latitude": 9,
	"Longitude": 9,
}

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
		print(config)
		return True

def __main__():
	global config
	if not readConfigFile():
		sys.exit()

	while True:
		# scan the wifi networks
		networks = helpers.scanWifi()

		# get the gps location
		gps = helpers.getGps(networks, config['apiKey'])
		print('got gps result:')
		print(gps)

		# check if received valid data
		errorCheck = helpers.gpsErrorCheck(json.loads(gps))
		if errorCheck is False:
			print('Successfully retrieved geolocation data')
			# write to screen
			helpers.displayLocation(
				gps,
				fieldLengths
			)
		else:
			# geolocation not successful, print the error
			print('Geolocation not successful: ' + errorCheck)
			helpers.displayError(errorCheck)

		# sleep
		sleep(config['scanInterval'])

if __name__ == '__main__':
	__main__()
