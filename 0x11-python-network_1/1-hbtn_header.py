#!/usr/bin/python3
"""sends a request to the URL and displays the value of the X-Request-Id"""

from urllib.request import Request, urlopen
from sys import argv


def fetch_Request_Id(url):
    """defining the function"""

    with urlopen(url) as response:
        print(response.getheader('X-Request-Id'))


if __name__ == "__main__":
    fetch_Request_Id(argv[1])
