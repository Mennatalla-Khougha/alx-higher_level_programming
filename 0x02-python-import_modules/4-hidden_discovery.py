#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4

    names = dir(hidden_4)
    for c in names:
        if c[:2]:
            continue
        print(c)
