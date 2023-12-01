#!/usr/bin/python3
"""
this module script that takes in a URL, sends a

"""


import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    if 'X-Request-Id' in response.headers:
        x_req_id = response.headers['X-Request-Id']
     print(x_req_id)
