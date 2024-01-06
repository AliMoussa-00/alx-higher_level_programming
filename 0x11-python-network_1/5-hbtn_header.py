#!//usr/bin/python3
"""
sends a request to the URL and
displays the value of the variable X-Request-Id
"""

import requests
from sys import argv


def request_id(url):
    """defining the function to fetch url"""

    r = requests.get(url)
    print(r.headers.get('X-Request-Id'))


if __name__ == "__main__":
    request_id(argv[1])
