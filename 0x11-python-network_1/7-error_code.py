#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8)"""
import sys
import requests


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        resp = requests.get(url)
        resp.raise_for_status()
        print(resp.text)
    except requests.exceptions.HTTPError as error:
        print('Error code: {}'.format(error.response.status_code))
