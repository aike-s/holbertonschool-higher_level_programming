#!/bin/bash
# displays only the status code of the response
curl -o -I -L -s -w "%{http_code}" "$1"
