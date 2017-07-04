# ubus driver for python

import shellHelper
import json

# basics of running a command
# returns a dict as ubus functions return json objects
def runCommand(command):
    output, err = shellHelper.runCommand(command)
    responseDict = json.loads(output)
    
    all_data = responseDict["results"]
    new_json={}
    new_json_list=[]
    for data in all_data:
    	new_data = {}
    	new_data["macAddress"] = data["bssid"]
    	new_data["signalStrength"] = int(data["signalStrength"])/2-100
    	new_json_list.append(new_data)
    new_json["results"] = new_json_list
    with open('data.json', 'w') as outfile:
    	json.dump(new_json, outfile)
    return responseDict

# often used commands
# add more if you need
def call(args):
    command = ["ubus", "call"]
    command.extend(args)
    return runCommand(command)
