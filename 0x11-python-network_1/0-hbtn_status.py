#!/usr/bin/python3
"""
fetches https://intranet.hbtn.io/status
"""
import urllib.request
if __name__ == "__main__":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        data = response.read()
        body_response = ("Body response:\n\t- type: {}".format(type(data)) +
                         "\n\t- content: {}".format(data) +
                         "\n\t- utf8 content: {}".format(data.decode('utf-8')))
        print(body_response)
