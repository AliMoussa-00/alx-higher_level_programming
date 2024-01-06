#!//usr/bin/python3
"""a Python script that fetches https://alx-intranet.hbtn.io/status"""

# from urllib.request import Request, urlopen
import urllib.request


def fetch_url(url):
    """defining the function to fetch url"""

    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        body = response.read()

        print("Body response:")

        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")

        t = 'OK' if response.info().get_content_charset() == "utf-8" else 'NO'
        print(f"\t- utf8 content: {t}")


if __name__ == "__main__":
    fetch_url("https://alx-intranet.hbtn.io/status")
