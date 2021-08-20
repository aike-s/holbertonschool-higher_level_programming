#!/usr/bin/python3
"""
sends a request to the URL and displays the value of the variable X-Request-Id
"""
import requests
import sys

from requests.api import patch
if __name__ == "__main__":
    url = sys.argv[1]

    req = requests.get(url)
    req_header = dict(req.headers)
    print(req_header['X-Request-Id'])
