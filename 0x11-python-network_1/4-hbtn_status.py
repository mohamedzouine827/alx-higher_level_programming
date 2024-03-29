#!/usr/bin/python3
"""urllib to fetch data"""

import requests

url = "https://alx-intranet.hbtn.io/status"
if __name__ == "__main__":
    text = requests.get(url=url)
    texts = text.text
    print("Body response:")
    print("\t- type: {}".format(type(texts)))
    print("\t- content: {}".format(texts))
