#!/usr/bin/python3
"""a Python script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays the body of
the response (decoded in utf-8)"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    dict = {'email': sys.argv[2]}
    data = requests.api(dict).encoding('utf-8')
    req = requests.request(url, data)
    resp = requests.get(req)
    rd = resp.text
    print(rd)
