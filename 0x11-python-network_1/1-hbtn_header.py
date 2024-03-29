#!/usr/bin/python3
"""urlib to get header"""


import urllib.request as ul
from sys import argv

url = argv[1]

with ul.urlopen(url) as response:
    header = response.getheader('X-Request-Id')
    print(header)
