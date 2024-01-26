#!/usr/bin/python3
"""a Python script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays the body of
the response (decoded in utf-8)"""
import sys
import requests


if __name__ == "__main__":
    if sys.argv[1] != None:
        dict = {'q': sys.argv[1]}
    else:
        q=""
        dict = {'q': q}
    data = requests.post('http://0.0.0.0:5000/search_user', data=dict)
    resp = data.json
    if resp == None:
        print('No result')
    else:
        print(resp)
