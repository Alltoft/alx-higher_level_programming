#!/usr/bin/python3
"""a Python script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays the body of
the response (decoded in utf-8)"""
import sys
from urllib import parse
from urllib import request
if __name__ == "__main__":
    url = sys.argv[1]
    dict = {'email': sys.argv[2]}
    data = parse.urlencode(dict).encode('utf-8')
    req = request.Request(url, data)
    with request.urlopen(req) as resp:
        print('Your email is: {}'.format(resp.content))
