#!/usr/bin/python3
"""script that takes your GitHub credentials"""
import requests
from sys import argv


if __name__ == "__main__":
    git_api = 'https://api.github.com/user'
    data = (argv[1], argv[2])
    user = requests.get(git_api, auth=data).json()
    print(user.get("id"))
