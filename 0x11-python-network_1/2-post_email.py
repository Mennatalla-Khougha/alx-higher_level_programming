#!/usr/bin/python3
""" script that takes in a URL and an email, sends a POST request """
from urllib.request import urlopen
from urllib.parse import urlencode
from sys import argv

if __name__ == "__main__":
    mail = {"email": argv[2]}
    mail = urlencode(mail).encode('utf-8')
    with urlopen(argv[1], data=mail) as response:
        print(response.read().decode('utf-8'))
