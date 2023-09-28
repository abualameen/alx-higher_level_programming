#!/bin/bash
# Sends a GET requuest
curl -siL "$1" | tail -n +13
