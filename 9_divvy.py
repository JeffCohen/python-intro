# Find the Nearest Divvy Station
#

import json
import urllib.request

# 1. Use your browser to determine your current coordinates.
# 2. use the following webservice url to find the nearest Divvy station.

webservice_url = "https://feeds.divvybikes.com/stations/stations.json"

# 3. Print the name of the station and the number of available bikes there.

# HINTS:
# ------
#   The "JSON Formatter" extension for Chrome is very helpful when viewing
#   JSON results in a browser.
#
#   To measure distance, you can treat latitudes and longitudes
#   like simple x and y coordinates, assume the earth is flat,
#   and use the Pythagorean theorem.
