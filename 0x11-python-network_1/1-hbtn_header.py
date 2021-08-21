#!/usr/bin/python3
"""
sends a request to the URL and displays the value of the X-Request-Id
"""
import urllib.request
import sys
if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        request_id = response.info().get('X-Request-Id')
        print(request_id)
