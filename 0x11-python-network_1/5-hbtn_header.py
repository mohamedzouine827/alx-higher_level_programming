#!/usr/bin/python3
"""urllib to fetch data"""

import requests
from sys import argv

url = "https://alx-intranet.hbtn.io/status"
if __name__ == "__main__":
    text = requests.get(url=argv[1])
    texts = text.headers.get("X-Request-Id")
    print(texts)
