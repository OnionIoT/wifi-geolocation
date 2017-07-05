import ubusHelper as ubus
import oledHelper as oled
import datetime
import json
import urllib3

#get your google api key from here : 
#https://developers.google.com/maps/documentation/geolocation/get-api-key
API_KEY = "Your_API_Key"


# scan wifi networks in range
# returns a list of wifi dictionaries
def scanWifi():
    device = json.dumps({"device": "ra0"})
    args = ["onion", "wifi-scan", device]
    return ubus.call(args)["results"]

# returns a dictionary with gps info
def getGps():
    http = urllib3.PoolManager()
    url = "https://www.googleapis.com/geolocation/v1/geolocate?key="+API_KEY
    payload = open("data.json")
    headers = {'content-Type': 'application/json', 'Accept-Charset': 'UTF-8'}
    r = http.request(
    	'POST',
    	url,
    	headers=headers,
    	body=payload
    )
    return r.data.decode('utf-8')

# build a date time header for the top of the screen
# returns a string
def buildDateTimeHeader():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d : %X")

# print to the display
# no return value
def displayLocation(gps, fieldLengths):
    # build a time header at the top of the screen
    timeHeader = buildDateTimeHeader()
    
    #build gps location data
    gps_json = json.loads(gps)
    data = {}
    data["latitude"] = str(gps_json['location']['lat'])
    data["longitude"] = str(gps_json['location']['lng'])
    
    # create a list of rows of text
    # include gps data on 2nd line
    screenOutput = [
        timeHeader,
        "latittude  " + data["latitude"].ljust(fieldLengths["Latitude"]), 
        "longitude  " + data["longitude"].ljust(fieldLengths["Longitude"])
    ]
    
    oled.clear()    
    oled.writeLines(screenOutput)
    
    

# write error message
def displayError(message):
    screenOutput = ["ERROR", message]
    oled.clear()
    oled.writeLines(screenOutput)
