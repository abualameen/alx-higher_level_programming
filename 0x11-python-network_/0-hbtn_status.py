#!/usr/bin/python3
"""
This script fetches content using urllib.request from a give url

"""


import urllib.request

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        content = response.read()
        encoded_content = content.decode('utf-8')
    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
    print("\t- utf8 content:", encoded_content)
