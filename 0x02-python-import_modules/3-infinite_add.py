#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    args = sys.argv
    result = 0;
    for i, c in enumerate(args):
        if i == 0:
            continue
        result += int(c)
    print(f"{result:d}")
