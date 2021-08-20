#!/usr/bin/python3
"""
fetches https://intranet.hbtn.io/status
"""
import requests
if __name__ == "__main__":
    req = requests.get('https://intranet.hbtn.io/status')
    data = req.text
    body_response = ("Body response:\n\t- type: {}".format(type(data)) +
                     "\n\t- content: {}".format(data))
    print(body_response)
