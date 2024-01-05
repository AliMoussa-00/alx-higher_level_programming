#!/bin/bash
# send a file with json content in POST request
curl -X POST -H "Content-Type: application/json" -d "@$2" "$1"
