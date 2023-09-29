#!/usr/bin/python3
""" script that takes in a URL, sends a request to the URL"""
from urllib.request import urlopen
from urllib.error import HTTPError
from sys import argv


if __name__ == "__main__":
    try:
        with urlopen(argv[1]) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print(f'Error code: {e.code}')
