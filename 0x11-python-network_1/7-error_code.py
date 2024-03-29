#!/usr/bin/python3
"""urllib to fetch data"""

import requests
from sys import argv

if __name__ == "__main__":
    text = requests.get(url=argv[1])
    code = text.status_code
    if code >= 400:
        print("Error code: ".format(code))
    else:
        print(text.text)
