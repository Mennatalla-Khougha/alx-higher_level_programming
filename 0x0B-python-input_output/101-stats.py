#!/usr/bin/python3
"""This module read stdin and compute metrics"""
import sys


file_size = 0
status_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        file_size += int(parts[-1])
        status_code = int(parts[-2])
        if status_code in status_count:
            status_count[status_code] += 1
        if line_count % 10 == 0:
            print("File size: {}".format(file_size))
            for code in sorted(status_count.keys()):
                if status_count[code] > 0:
                    print("{}: {}".format(code, status_count[code]))
except KeyboardInterrupt:
    print("File size: {}".format(file_size))
    for code in sorted(status_count.keys()):
        if status_count[code] > 0:
            print("{}: {}".format(code, status_count[code]))
