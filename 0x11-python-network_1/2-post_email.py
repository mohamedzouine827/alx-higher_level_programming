#!/usr/bin/python3
"""post request with urlib"""


from sys import argv
from urllib.request import Request, urlopen
from urllib.parse import urlencode

if __name__ == "__main__":
    email = argv[2]
    url = argv[1]

    data = {"email": email}

    values = urlencode(data)
    values = values.encode('ascii')

    req = Request(url, data)
    with urlopen(req) as response:
        html = response.read()

    print(html.read().decode('utf-8'))
