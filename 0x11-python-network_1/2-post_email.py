#!/usr/bin/python3
"""a Python script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays the body of
the response (decoded in utf-8)"""
import sys
from urllib import request
if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    req = request.Request(url, email)
    with request.urlopen(req) as resp:
        print('Your email is: {}'.format(req))
