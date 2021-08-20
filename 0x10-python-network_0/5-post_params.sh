#!/bin/bash
# sends a POST request to the passed URL
curl -sL --data "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
