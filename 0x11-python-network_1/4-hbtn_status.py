#!/usr/bin/python3
""" a Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests

if __name__ == '__main__':
    resp = requests.get('https://alx-intranet.hbtn.io/status')
    res = resp.text
    print('Body response:')
    print('\t- type: {}'.format(type(res)))
    print('\t- content: {}'.format(res))
