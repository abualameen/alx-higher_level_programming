#!/usr/bin/python3
# this script that takes in a URL
curl -sI "$1" | grep -i 'content-length' | awk '{print $2}'
