#!/usr/bin/python3
"""
sends a request to the URL and displays the value of the X-Request-Id
"""
import urllib.request
import sys
if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        response_info = str(response.info()).split('X-Request-Id: ')
        request_id = response_info[1].split('\n')
        print(request_id[0])
