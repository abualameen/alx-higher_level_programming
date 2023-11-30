#!/bin/bash
# this script that sends a request to a URL passed
curl -s -o /dev/null -w "%{http_code}" "$1"
