#!/usr/bin/python3
""" a Python script that fetches https://alx-intranet.hbtn.io/status"""
from urllib import request

if __name__ == '__main__':
    with request.urlopen('https://alx-intranet.hbtn.io/status') as resp:
        disp = resp.read()
        print(('Body response:\n\t- type: {}\n\t- content: {}\n\t\
- utf8 content: {}').format(type(disp), disp, disp.decode('utf-8')))
