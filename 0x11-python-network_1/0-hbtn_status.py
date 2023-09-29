#!/usr/bin/python3
"""script that fetches https://alx-intranet.hbtn.io/status"""
from urllib.request import urlopen


with urlopen('https://alx-intranet.hbtn.io/status') as response:
    html = response.read()
    print("Body response:")
    print(f'    - type: {type(html)}')
    print(f'    - content: {html}')
    print(f'    - utf8 content: {html.decode("utf-8")}')
