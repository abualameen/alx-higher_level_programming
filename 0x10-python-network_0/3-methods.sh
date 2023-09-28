#!/bin/bash
# check the methods supported
curl -s -I --request OPTIONS "$1" | grep "Allow" | sed 's/Allow: //'
