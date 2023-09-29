#!/usr/bin/python3
""" script that takes in a URL, sends a request to the URL"""
from urllib.request import urlopen
from sys import argv


with urlopen(argv[1]) as response:
    print(response.getheader('X-Request-Id'))
