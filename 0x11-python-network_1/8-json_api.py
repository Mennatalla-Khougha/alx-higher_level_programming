#!/usr/bin/python3
""" script that takes in a letter and sends a POST request"""
import requests
from sys import argv


if __name__ == "__main__":
    letter = {"q": argv[1] if len(argv) > 1 else ""}
    html = requests.post('http://0.0.0.0:5000/search_user', letter)
    try:
        response = html.json()
        if response:
            print(f'[{response.get("id")}] {response.get("name")}')
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
