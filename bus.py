# How long do we need to wait for the 22 bus at Dearborn & Madison?
#
# ---------------------------------------------------------------
# This file is NOT runnable as-is.
#
# But you can copy and paste each line, one at a time,
# into your Python interactive interpreter.
#
# (Even better is to type it in yourelf without copy/pasting!)
# ---------------------------------------------------------------
#
import urllib.request
from xml.etree.ElementTree import parse
url = "http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop=1882&route=22"
html_page = urllib.request.urlopen(url)
doc = parse(html_page)
for pt in doc.findall('.//pt'):
    print(pt.text)
