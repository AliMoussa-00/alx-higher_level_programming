#!//usr/bin/python3
"""
script that takes in a URL, sends a request to the URL
and displays the body of the response.
-   If the HTTP status code is greater than or equal to 400,
    print: Error code: followed by the value of the HTTP status code
"""

import requests
from sys import argv


def request_error(url):
    """defining the function to fetch url"""

    r = requests.get(url)

    if r.status_code >= 400:
        print(f"Error code: {r.status_code}")
    else:
        print(r.text)


if __name__ == "__main__":
    request_error(argv[1])
