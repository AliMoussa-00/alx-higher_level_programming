#!/usr/bin/python3
"""sends a POST request to the passed URL with the email as a parameter"""

from urllib.request import Request, urlopen
from urllib.parse import urlencode
from sys import argv


def post_email(url, email):
    """defining the function"""

    params = urlencode({'email': email})
    params = params.encode("ascii")

    req = Request(url, params)
    with urlopen(req) as response:
        print(response.read().decode('utf-8'))


if __name__ == "__main__":
    post_email(argv[1], argv[2])
