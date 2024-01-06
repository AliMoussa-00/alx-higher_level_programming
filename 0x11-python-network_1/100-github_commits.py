#!/usr/bin/python3
"""
Please list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
"""

import requests
from sys import argv


def request_github_commits(repo, owner):
    """defining the function"""

    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    r = requests.get(url)
    try:
        data = r.json()

        # print(data[0])

        for i in range(10):
            sha = data[i].get('sha')
            author = data[i].get('commit').get('author').get('name')
            print(f"{sha}: {author}")

    except (requests.exceptions.JSONDecodeError, Exception):
        pass


if __name__ == "__main__":
    request_github_commits(argv[1], argv[2])
