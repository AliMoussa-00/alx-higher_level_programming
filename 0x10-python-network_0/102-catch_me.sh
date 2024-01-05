#!/bin/bash
# a request that causes the server to respond with a message containing You got me!
curl -sX PUT -L "0.0.0.0:5000/catch_me_2"
