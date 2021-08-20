#!/bin/bash
# Displays the size of the body of the response
curl -s -I "$1" | grep -i "Content-length:" | awk '{print$2}'