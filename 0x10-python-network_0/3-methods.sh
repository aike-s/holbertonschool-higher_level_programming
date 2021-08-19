#!/bin/bash
# displays all HTTP methods the server will accept
curl -s -X OPTIONS "$1"