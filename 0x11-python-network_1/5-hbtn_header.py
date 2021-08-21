#!/usr/bin/python3
"""
sends a request to the URL and displays the value of the variable X-Request-Id
"""
import requests
import sys

if __name__ == "__main__":

    url = sys.argv[1]

    req = requests.get(url)
    req_header = req.headers['X-Request-Id']
    print(req_header)
