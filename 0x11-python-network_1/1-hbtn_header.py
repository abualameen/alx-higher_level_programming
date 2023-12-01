#!/usr/bin/python3
"""
The script take a URL as a command line argument, sends a request
to the URL and fetch the value of the X-Request-Id variable found in the header
of the response.

"""


import urllib.request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        x_request_id = response.getheader('X-Request-Id')
        print(x_request_id)
