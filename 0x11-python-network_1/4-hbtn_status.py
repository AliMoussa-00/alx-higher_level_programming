#!//usr/bin/python3
"""
a Python script that fetches https://alx-intranet.hbtn.io/status
using the package 'requests'
"""

import requests


def request_url(url):
    """defining the function to fetch url"""

    r = requests.get(url)

    print("Body response:")
    print(f"\t- type: {type(r.text)}")
    print(f"\t- content: {r.text}")


if __name__ == "__main__":
    request_url("https://alx-intranet.hbtn.io/status")
