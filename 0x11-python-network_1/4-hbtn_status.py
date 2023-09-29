#!/usr/bin/python3
"""
This script fetches a site

"""


import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    texts = response.text.split()
    for tex in texts:
        print("Body response:")
        print("\t- type", type(response.text))
        print("\t- content:", tex)

