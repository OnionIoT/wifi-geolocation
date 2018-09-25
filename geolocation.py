import ubusHelper as ubus
import oledHelper as oled
import datetime
import json
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

errors = {
	"dailyLimitExceeded": "Daily limit exceeded. The Program will try again shortly.",
	"keyInvalid": "Invalid API Key. The Program will try again shortly.",
	"userRateLimitExceeded": "Exceeded the request per second per user limit configured by you",
	"notFound": "Wifi Access Point not geolocated. The Program will try again shortly.",
	"parseError": "Request body is not valid JSON. The Program will try again shortly."
}

fieldLengths = {
	"Latitude": 9,
	"Longitude": 9,
}

#### ALL IN ONE FUNCTIONS ####
# scan environment wifi networks and use API to get location
# returns dictionary of longitude and latitude
def getGeolocation(apiKey):
    # scan the wifi networks
    networks = scanWifi()

    # get the geo location data from the API
    data = getGps(networks, apiKey)

    return json.loads(data)

# performs error checking and displays data on OLED Expansion
#   displays the GPS coordinates if succesful, error message if not
def displayGeolocation(apiData):
    # check if received valid data
    errorCheck = gpsErrorCheck(apiData)
    if errorCheck is False:
        print('Successfully retrieved geolocation data')
        print(apiData)
        # write to screen
        displayLocation(
            apiData,
            fieldLengths
        )
    else:
        # geolocation not successful, print the error
        print('Geolocation not successful: ' + errorCheck)
        displayError(errorCheck)


#### HELPER FUNCTIONS ####

# scan wifi networks in range
# returns a list of wifi dictionaries
def scanWifi():
    device = json.dumps({"device": "ra0"})
    args = ["onion", "wifi-scan", device]

    # perform wifi scan
    networks = ubus.call(args)["results"]

    # format the data to hold only what's needed by the API
    formattedNetworks = {}
    formattedNetworks["results"] = []

    new_json_list=[]
    for data in networks:
    	new_data = {}
    	new_data["macAddress"] = data["bssid"]
    	new_data["signalStrength"] = int(data["rssi"])
    	formattedNetworks["results"].append(new_data)

    return formattedNetworks

# returns a dictionary with gps info
def getGps(networks, apiKey):
    http = urllib3.PoolManager()
    url = "https://www.googleapis.com/geolocation/v1/geolocate?key="+apiKey
    payload = json.dumps(networks)
    headers = {'content-Type': 'application/json', 'Accept-Charset': 'UTF-8'}
    r = http.request(
    	'POST',
    	url,
    	headers=headers,
    	body=payload
    )
    return r.data.decode('utf-8')

# check for error in API data
def gpsErrorCheck(apiData):
    errorDetected = False
    if 'error' in apiData:
        if str(apiData['error']['errors'][0]['reason'])=='dailyLimitExceeded':
            errorDetected = errors["dailyLimitExceeded"]
        elif str(apiData['error']['errors'][0]['reason'])=='keyInvalid':
            errorDetected = errors["keyInvalid"]
        elif str(apiData['error']['errors'][0]['reason'])=='userRateLimitExceeded':
            errorDetected = errors["userRateLimitExceeded"]
        elif str(apiData['error']['errors'][0]['reason'])=='notFound':
            errorDetected = errors["notFound"]
        else:
            errorDetected = errors["parseError"]
    return errorDetected

# build a date time header for the top of the screen
# returns a string
def buildDateTimeHeader():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d   %X")

# print to the display
# no return value
def displayLocation(apiData, fieldLengths):
    # build a time header at the top of the screen
    timeHeader = buildDateTimeHeader()

    #build gps location data
    data = {}
    data["latitude"] = format(apiData['location']['lat'], '.6f')
    data["longitude"] = format(apiData['location']['lng'], '.6f')

    # build header
    header = {}
    header['lat'] = "latitude  "
    header['lng'] = "longitude  "

    # create a list of rows of text
    # include gps data on 2nd line
    screenOutput = [
        timeHeader,
        " ",
        header['lat'] + data["latitude"].rjust(oled.getMaxCharacters() - len(header['lat'])),
        header['lng'] + data["longitude"].rjust(oled.getMaxCharacters() - len(header['lng']))
    ]

    oled.clear()
    oled.writeLines(screenOutput)



# write error message
def displayError(message):
    screenOutput = ["ERROR", message]
    oled.clear()
    oled.writeLines(screenOutput)
