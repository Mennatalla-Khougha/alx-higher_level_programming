#!/usr/bin/python3
"""script that takes your GitHub credentials"""
import requests
from sys import argv


if __name__ == "__main__":
    git_api = f'https://api.github.com/repos/{argv[2]}/{argv[1]}/commits'
    commits = requests.get(git_api).json()[:10]
    for commit in commits:
        name = commit.get("commit").get("author").get("name")
        print(f'{commit.get("sha")}: {name}')
