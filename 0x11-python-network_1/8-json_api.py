#!/usr/bin/python3
"""a Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""
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
