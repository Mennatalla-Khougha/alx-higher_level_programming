#!/usr/bin/python3
"""This module read stdin and compute metrics"""
import sys


file_size = 0
status_count = {}
codes = [200, 301, 400, 401, 403, 404, 405, 500]
line_count = 0

for line in sys.stdin:
    if line_count % 10 == 0 or KeyboardInterrupt:
        print("File size: {}".format(file_size))
        for code in sorted(status_count.keys()):
            if status_count[code] > 0:
                print("{}: {}".format(code, status_count[code]))
    line_count += 1
    parts = line.split()
    try:
        file_size += int(parts[-1])
    except (ValueError, IndexError):
        pass
    try:
        status_code = int(parts[-2])
        if status_code in codes:
            if status_count.get(status_code, -1) == -1:
                status_count[status_code] = 1
            else:
                status_count[status_code] += 1
    except IndexError:
        pass
    print("File size: {}".format(file_size))
    for code in sorted(status_count.keys()):
        if status_count[code] > 0:
            print("{}: {}".format(code, status_count[code]))
