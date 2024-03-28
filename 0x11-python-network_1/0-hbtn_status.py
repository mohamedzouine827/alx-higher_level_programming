#!/usr/bin/python3
"""urllib to fetch data"""

import urllib.request as ul

url = "https://alx-intranet.hbtn.io/status"
with ul.urlopen(url) as response:
    html = response.read()
    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html.decode('utf-8')))
