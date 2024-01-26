#!/usr/bin/python3
"""a Python script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays the body of
the response (decoded in utf-8)"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    if sys.argv[2] != None:
        dict = {'q': sys.argv[2]}
    else:
        q=""
        dict = {'q': q}
    data = requests.post(url, data=dict)
    resp = data.json
    if resp == None:
        print('No result')
    else:
        print(resp)
