#!/usr/bin/python3
"""
sends a POST request to the passed URL with the email as a parameter
and finally displays the body of the response.
"""

import requests
from sys import argv


def request_post_email(url, email):
    """defining the function to fetch url"""

    r = requests.post(url, data={'email': email})
    print(r.text)


if __name__ == "__main__":
    request_post_email(argv[1], argv[2])
