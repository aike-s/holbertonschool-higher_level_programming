#!/usr/bin/python3
"""
sends a request to the URL and displays the body of the response
"""
import urllib.error
import urllib.request
import sys
if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf-8')
            print(html)
    except urllib.error.HTTPError as response:
        print("Error code: {}".format(response.code))
