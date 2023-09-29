#!/usr/bin/python3
""" script that takes in a URL, sends a request to the URL"""
import requests
from sys import argv

if __name__ == "__main__":
    html = requests.get(argv[1])
    print(html.headers.get('X-Request-Id'))
