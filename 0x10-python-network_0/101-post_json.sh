#!/bin/bash
# this script sends a JSON POST request to a URL passed
curl -s -H "Content-Type: application/json" -X POST -d @"$2" "$1"
