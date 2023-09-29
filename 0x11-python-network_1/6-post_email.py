#!/usr/bin/python3
""" script that takes in a URL and an email, sends a POST request """
import requests
from sys import argv


if __name__ == "__main__":
    mail = {"email": argv[2]}
    html = requests.post(argv[1], mail)
    print(html.text)
