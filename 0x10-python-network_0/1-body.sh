#!/bin/bash
# a script that takes in a URL, sends a request to that URL, and Display only body of a 200 status code response
curl -sL "$1"
