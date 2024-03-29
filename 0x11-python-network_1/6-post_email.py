#!/usr/bin/python3
"""urllib to fetch data"""

import requests
from sys import argv

if __name__ == "__main__":
    data = {'email': argv[2]}
    req = requests.post(argv[1], data=data)
    print(req.text)
