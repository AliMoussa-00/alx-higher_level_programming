#!/bin/bash
# a script that takes in a URL, sends a request to that URL, and get the size of responde
curl -s -w "%{size_download}\n"  -o /dev/null  "$1"
