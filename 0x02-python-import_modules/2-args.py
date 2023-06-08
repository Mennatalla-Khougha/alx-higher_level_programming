#!/usr/bin/python3
if __name__ == '__main__':
    import sys

    args = sys.argv
    argc = len(args)

    if argc == 1:
        print('0 arguments.')
    else:
        print(f"{argc - 1} arguments:")
        for i, c in enumerate(args):
            if i == 0:
                continue
            print(f"{i:d}: {c}")
