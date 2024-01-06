#!//usr/bin/python3
"""
a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to display your id
"""

import requests
from sys import argv


def request_github_id(username, token):
    """defining the function to fetch url"""

    url = "https://api.github.com/user"

    r = requests.get(url, auth=(username, token))
    try:
        data = r.json()

        print(data.get('id'))

    except requests.exceptions.JSONDecodeError:
        print(None)


if __name__ == "__main__":
    request_github_id(argv[1], argv[2])
