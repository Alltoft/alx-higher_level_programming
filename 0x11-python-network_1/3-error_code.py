#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8)"""
import sys
from urllib import parse
from urllib import request


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        with request.urlopen(url) as resp:
            rd = resp.read()
            print(rd.decode('utf-8'))
    except Exception as error:
        print('Error code: {}'.format(error))
