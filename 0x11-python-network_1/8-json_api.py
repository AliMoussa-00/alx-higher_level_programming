#!/usr/bin/python3
"""
sends a POST request to url with the letter as a parameter.
"""

import requests
from sys import argv


def request_json(url, letter):
    """defining the function to fetch url"""

    r = requests.post(url, data={'q': letter})

    try:
        data = r.json()
        if len(data) > 0:

            print(f"[{data.get('id')}] {data.get('name')}")
        else:
            print("No result")

    except requests.exceptions.JSONDecodeError:
        print("Not a valid JSON")


if __name__ == "__main__":

    letter = argv[1] if len(argv) > 1 else ''
    request_json("http://0.0.0.0:5000/search_user", letter)
