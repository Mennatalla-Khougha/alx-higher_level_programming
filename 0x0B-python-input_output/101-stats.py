#!/usr/bin/python3
"""This module read stdin and compute metrics"""
import sys


def print_stats(size, status_codes):
    """Print accumulated metrics.

    Args:
        size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))


file_size = 0
status_count = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        try:
            file_size += int(parts[-1])
        except (IndexError, ValueError):
            pass
        status_code = int(parts[-2])
        if status_code in status_count:
            status_count[status_code] += 1
        if line_count % 10 == 0:
            print_stats(file_size, status_count)
except KeyboardInterrupt:
    print_stats(file_size, status_count)
    raise
