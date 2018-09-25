# wifi-geolocation
WiFi geolocation using WiFi Accesspoints
Requires Omega2 Plus, Omega expansion dock and Omega Oled expansion.

# Installation
1. Generate your google API Key to use with the application by following the link :
https://developers.google.com/maps/documentation/geolocation/get-api-key

1. Install the required software packages:

Python2:

    ```
    opkg update
    opkg install python-light pyOledExp python-urllib3
    ```

Python3:

```
opkg update
opkg install python3-light python3-oled-exp python3-pip
pip3 install urllib3
```

1. Edit the `config.json` file to add the generated API Key and save the file

1. Run the following command:
* `python /root/wifi-geolocation/main.py`

The program will now scan the surroundings for WiFi networks, use the Google Maps API to find the GPS location, and display the GPS coordinates
