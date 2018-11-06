# Who's in space?
#
# Tip: Install the JSONFormatter extension for Chrome.

import json
from urllib.request import urlopen

astros_url = "http://api.open-notify.org/astros.json"

webservice = urlopen(astros_url)
encoded_data = webservice.read()
decoded_data = encoded_data.decode("utf8")
data = json.loads(decoded_data)

# TO DO: Print the names of the people in space right now.
