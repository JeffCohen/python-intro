# Geocoding
# https://developers.google.com/maps/documentation/geocoding/intro

# Here is an example of how to get the coordinates of Millenium Park.
# Your job is to modify this code to display the coordinates to the screen.

import json
from urllib.request import urlopen

url = "https://maps.googleapis.com/maps/api/geocode/json?address=Millenium+Park,+Chicago,+IL&key=AIzaSyDttiQ5XjbJAombW2oliPDujDtBw6XZD7Q"
webservice = urlopen(url)
encoded_data = webservice.read()
decoded_data = encoded_data.decode("utf8")
data = json.loads(decoded_data)

latitude = 0.0       # use the data to get the latitude
longitude = 0.0      # use the data to get the longitude

print(f"Millenium Park is at latitude {latitude} and longitude {longitude}")
