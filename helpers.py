import ubusHelper as ubus
# TMP:
#import oledHelper as oled
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

# scan wifi networks in range
# returns a list of wifi dictionaries
def scanWifi():
    device = json.dumps({"device": "ra0"})
    args = ["onion", "wifi-scan", device]

    # perform wifi scan
    #networks = ubus.call(args)["results"]
    # tmp:
    networks = json.loads('{"results": [{"channel": "1","ssid": "Oboo-Clock-56BE","bssid": "40:a3:6b:c2:56:be","cipher": "AES","encryptionString": "WPA2PSK","encryption": "psk2","signalStrength": "55","wirelessMode": "11b\/g\/n","ext-ch": "NONE","rssi": "-68"},{"channel": "1","ssid": "BELL614","bssid": "00:26:50:9e:3e:09","cipher": "WEP","encryptionString": "WEP","encryption": "wep","signalStrength": "24","wirelessMode": "11b\/g","ext-ch": "NONE","rssi": "-80"},{"channel": "1","ssid": "HardGrotesqueVolume","bssid": "ac:84:c9:f1:fe:6e","cipher": "AES","encryptionString": "WPA2PSK","encryption": "psk2","signalStrength": "42","wirelessMode": "11b\/g\/n","ext-ch": "ABOVE","rssi": "-73"},{"channel": "1","ssid": "BELL552","bssid": "58:90:43:be:51:fa","cipher": "AES","encryptionString": "WPA2PSK","encryption": "psk2","signalStrength": "0","wirelessMode": "11b\/g\/n","ext-ch": "NONE","rssi": "-95"},{"channel": "1","ssid": "flattop","bssid": "08:60:6e:bb:fa:80","cipher": "AES","encryptionString": "WPA2PSK","encryption": "psk2","signalStrength": "100","wirelessMode": "11b\/g\/n","ext-ch": "NONE","rssi": "-50"},{"channel": "4","ssid": "Rogers27119","bssid": "84:94:8c:37:44:68","cipher": "TKIPAES","encryptionString": "WPA1PSKWPA2PSK","encryption": "psk2","signalStrength": "0","wirelessMode": "11b\/g\/n","ext-ch": "NONE","rssi": "-96"},{"channel": "6","ssid": "La","bssid": "bc:14:01:54:02:f8","cipher": "AES","encryptionString": "WPA2PSK","encryption": "psk2","signalStrength": "0","wirelessMode": "11b\/g\/n","ext-ch": "NONE","rssi": "-91"},{"channel": "6","ssid": "","bssid": "bc:14:01:54:02:f9","cipher": "AES","encryptionString": "WPA2PSK","encryption": "psk2","signalStrength": "0","wirelessMode": "11b\/g\/n","ext-ch": "NONE","rssi": "-91"},{"channel": "6","ssid": "ShinyFish","bssid": "bc:4d:fb:9f:d0:e8","cipher": "AES","encryptionString": "WPA1PSKWPA2PSK","encryption": "psk2","signalStrength": "23","wirelessMode": "11b\/g\/n","ext-ch": "NONE","rssi": "-81"},{"channel": "6","ssid": "BELL565","bssid": "f8:ab:05:52:99:6e","cipher": "AES","encryptionString": "WPA2PSK","encryption": "psk2","signalStrength": "0","wirelessMode": "11b\/g\/n","ext-ch": "BELOW","rssi": "-96"},{"channel": "6","ssid": "BELL400","bssid": "b8:d9:4d:f0:5d:66","cipher": "AES","encryptionString": "WPA2PSK","encryption": "psk2","signalStrength": "0","wirelessMode": "11b\/g\/n","ext-ch": "BELOW","rssi": "-92"},{"channel": "6","ssid": "RogersB6717","bssid": "00:fc:8d:35:7c:38","cipher": "TKIPAES","encryptionString": "WPA1PSKWPA2PSK","encryption": "psk2","signalStrength": "2","wirelessMode": "11b\/g\/n","ext-ch": "NONE","rssi": "-89"},{"channel": "6","ssid": "Brenda11","bssid": "f0:f2:49:5e:96:98","cipher": "TKIPAES","encryptionString": "WPA1PSKWPA2PSK","encryption": "psk2","signalStrength": "26","wirelessMode": "11b\/g\/n","ext-ch": "NONE","rssi": "-79"},{"channel": "7","ssid": "A Nice Name","bssid": "28:c6:8e:77:59:ab","cipher": "AES","encryptionString": "WPA2PSK","encryption": "psk2","signalStrength": "0","wirelessMode": "11b\/g\/n","ext-ch": "NONE","rssi": "-90"},{"channel": "9","ssid": "CGN3-B890","bssid": "78:8d:f7:e3:b8:98","cipher": "TKIPAES","encryptionString": "WPA1PSKWPA2PSK","encryption": "psk2","signalStrength": "0","wirelessMode": "11b\/g\/n","ext-ch": "NONE","rssi": "-94"},{"channel": "9","ssid": "CIK1000M_AC2.4G_4055","bssid": "8c:68:c8:a7:49:3c","cipher": "AES","encryptionString": "WPA2PSK","encryption": "psk2","signalStrength": "29","wirelessMode": "11b\/g\/n","ext-ch": "NONE","rssi": "-78"},{"channel": "9","ssid": "","bssid": "fa:8f:ca:63:e4:52","cipher": "NONE","encryptionString": "NONE","encryption": "none","signalStrength": "44","wirelessMode": "11b\/g\/n","ext-ch": "NONE","rssi": "-72"},{"channel": "10","ssid": "The LAN Before Time","bssid": "88:dc:96:65:61:ba","cipher": "AES","encryptionString": "WPA2PSK","encryption": "psk2","signalStrength": "0","wirelessMode": "11b\/g\/n","ext-ch": "NONE","rssi": "-95"},{"channel": "11","ssid": "WHATWHAT","bssid": "b8:ee:0e:b1:4e:0a","cipher": "AES","encryptionString": "WPA2PSK","encryption": "psk2","signalStrength": "0","wirelessMode": "11b\/g\/n","ext-ch": "NONE","rssi": "-96"},{"channel": "11","ssid": "","bssid": "00:fc:8d:e1:33:3a","cipher": "TKIPAES","encryptionString": "WPA1PSKWPA2PSK","encryption": "psk2","signalStrength": "10","wirelessMode": "11b\/g\/n","ext-ch": "NONE","rssi": "-86"},{"channel": "11","ssid": "georgina","bssid": "bc:14:01:ea:ec:78","cipher": "TKIPAES","encryptionString": "WPA1PSKWPA2PSK","encryption": "psk2","signalStrength": "0","wirelessMode": "11b\/g\/n","ext-ch": "NONE","rssi": "-90"},{"channel": "11","ssid": "","bssid": "bc:14:01:ea:ec:79","cipher": "AES","encryptionString": "WPA2PSK","encryption": "psk2","signalStrength": "0","wirelessMode": "11b\/g\/n","ext-ch": "NONE","rssi": "-90"},{"channel": "11","ssid": "Lizalipe","bssid": "64:77:7d:57:f4:28","cipher": "TKIPAES","encryptionString": "WPA1PSKWPA2PSK","encryption": "psk2","signalStrength": "31","wirelessMode": "11b\/g\/n","ext-ch": "NONE","rssi": "-77"},{"channel": "11","ssid": "","bssid": "00:fc:8d:40:f4:8a","cipher": "TKIPAES","encryptionString": "WPA1PSKWPA2PSK","encryption": "psk2","signalStrength": "0","wirelessMode": "11b\/g\/n","ext-ch": "NONE","rssi": "-96"}]}')

    # format the data to hold only what's needed by the API
    formattedNetworks = {}
    formattedNetworks["results"] = []

    new_json_list=[]
    for data in networks["results"]:
    	new_data = {}
    	new_data["macAddress"] = data["bssid"]
        # TODO: look into using RSSI
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
    print(apiData)
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
        "latitude  " + data["latitude"].ljust(fieldLengths["Latitude"]),
        "longitude  " + data["longitude"].ljust(fieldLengths["Longitude"])
    ]

    # TMP:
    #oled.clear()
    #oled.writeLines(screenOutput)



# write error message
def displayError(message):
    screenOutput = ["ERROR", message]
    # TMP:
    #oled.clear()
    #oled.writeLines(screenOutput)
