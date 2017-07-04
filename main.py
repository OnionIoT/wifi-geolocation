# this program will periodically scan nearby wifi networks and geolocate and print the gps coordinates

import helpers, os
from time import sleep

SCAN_INTERVAL = 5

fieldLengths = {
    "Latitude": 9,
    "Longitude": 9,
}

errors = {
	"gpsNotLocated": "Wifi Access Point not geolocated. The Program will try again shortly."
}

def __main__():
    while True:
        # scan the wifi networks
        networks = helpers.scanWifi()

        # get the gps location
        gps = helpers.getGps()
       
        # if the geolocation was not successful, try again from the beginning
      	if not gps:
      		helpers.displayError(errors["gpsNotLocated"])
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
