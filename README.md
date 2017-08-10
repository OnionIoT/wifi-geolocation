# wifi-geolocation
WiFi geolocation using WiFi Accesspoints
Requires Omega2 Plus, Omega expansion dock and Omega Oled expansion.

# Installation
1. Generate your google API Key to use with the application by following the link :
https://developers.google.com/maps/documentation/geolocation/get-api-key

1. Install the required software packages:
    ```
    opkg update
    opkg install python-light pyOledExp python-urllib3
    ```

1. Edit the file helper.py to add the generated API Key and save the file

1. Install cURL package
    ```
    opkg update
    opkg install curl
    ```

1. Run the following command:
* `python /root/wifi-geolocation/main.py &`

The program will now scan for wifi and display the gps location based on that.
