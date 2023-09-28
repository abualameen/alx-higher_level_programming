#!/bin/bash


if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

curl -sI "$1" | grep -i 'content-length' | awk '{print $2}'#!/bin/bash

