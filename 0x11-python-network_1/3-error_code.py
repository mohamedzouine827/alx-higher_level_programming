#!/usr/bin/python3
"""urlib to get header"""


import urllib.request as ul
from sys import argv
import urllib.error as error

if __name__ == "__main__":
    url = argv[1]
    try:
        with ul.urlopen(url) as response:
            print(response.read().decode("utf-8"))
    except error.HTTPError as err:
        print("Error code: ", err.code)
