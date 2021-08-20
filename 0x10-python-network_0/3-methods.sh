#!/bin/bash
# displays all HTTP methods the server will accept
curl -i --request-target "*" -X OPTIONS "$1"
