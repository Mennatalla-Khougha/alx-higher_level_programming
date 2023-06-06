#!/usr/bin/python3
def uppercase(str):
    for c in str:
        char = ord(c)
        if char > 96 and char < 123:
            char -= 32
        print("{}".format(char), end='')
    print("\n")
