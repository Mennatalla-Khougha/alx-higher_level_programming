#!/usr/bin/python3
import requests
from sys import argv

if __name__ == "__main__":
    print(requests.get(argv[1]).getheader('X-Request-Id'))
