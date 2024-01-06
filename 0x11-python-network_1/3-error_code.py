#!/usr/bin/python3
"""
sends a request to the URL and displays the body of the response
manage urllib.error.HTTPError exceptions and print: Error code
"""

from urllib.request import Request, urlopen
from urllib.error import HTTPError
from sys import argv


def request_exception(url):
    """defining the function"""

    try:
        with urlopen(url) as response:
            print(response.read().decode('utf-8'))

    except HTTPError as e:
        print(f'Error code: {e.code}')


if __name__ == "__main__":
    request_exception(argv[1])
