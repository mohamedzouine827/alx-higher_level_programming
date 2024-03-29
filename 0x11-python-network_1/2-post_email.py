#!/usr/bin/python3
"""post request with urlib"""


from sys import argv
from urllib.request import Request, urlopen
from urllib.parse import urlencode
import urllib

if __name__ == "__main__":
    email = argv[2]
    url = argv[1]

    data = {"email": email}

    values = urlencode(data)
    values = values.encode('ascii')

    with urllib.request.urlopen(url, values) as response:
        print(response.read().decode('utf-8'))
