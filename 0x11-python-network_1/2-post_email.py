#!/usr/bin/python3
"""
sends a POST request to the passed URL with the email as a parameter
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    info = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(info).encode()
    post_request = urllib.request.Request(url, data=data)

    with urllib.request.urlopen(post_request) as response:
        html = response.read().decode('utf-8')
        print(html)
