# this program will periodically scan nearby wifi networks and geolocate and print the gps coordinates

import helpers, os
import json
from time import sleep

SCAN_INTERVAL = 5

fieldLengths = {
    "Latitude": 9,
    "Longitude": 9,
}

errors = {
	"dailyLimitExceeded": "Daily limit exceeded. The Program will try again shortly.",
	"keyInvalid": "Invalid API Key. The Program will try again shortly.",
	"userRateLimitExceeded": "Exceeded the request per second per user limit configured by you",
	"notFound": "Wifi Access Point not geolocated. The Program will try again shortly.",
	"parseError": "Request body is not valid JSON. The Program will try again shortly."
}

def __main__():
    while True:
        # scan the wifi networks
        networks = helpers.scanWifi()

        # get the gps location
        gps = helpers.getGps()
        
        gps_check = json.loads(gps)
        
        # if the geolocation was not successful, try again from the beginning
      	if str(gps_check['error']['errors'][0]['reason'])=='dailyLimitExceeded':
      		helpers.displayError(errors["dailyLimitExceeded"])
      		sleep(SCAN_INTERVAL)
      		continue
      	elif str(gps_check['error']['errors'][0]['reason'])=='keyInvalid':
      		helpers.displayError(errors["keyInvalid"])
      		sleep(SCAN_INTERVAL)
      		continue
      	elif str(gps_check['error']['errors'][0]['reason'])=='userRateLimitExceeded':
      		helpers.displayError(errors["userRateLimitExceeded"])
      		sleep(SCAN_INTERVAL)
      		continue
      	elif str(gps_check['error']['errors'][0]['reason'])=='notFound':
      		helpers.displayError(errors["notFound"])
      		sleep(SCAN_INTERVAL)
      		continue
      	else:
      		helpers.displayError(errors["parseError"])
      		sleep(SCAN_INTERVAL)
      		continue
      		
      	# write to screen
        
        helpers.displayLocation(
			gps,
			fieldLengths
		)

        # sleep
        sleep(SCAN_INTERVAL)
        
if __name__ == '__main__':
    __main__()
