#!/usr/bin/python3
""" script that takes in a URL, sends a request to the URL"""
import requests
from sys import argv


if __name__ == "__main__":
    try:
        html = requests.get(argv[1])
        html.raise_for_status()
        print(html.text)
    except requests.RequestException as e:
        print(f'Error code: {html.status_code}')
