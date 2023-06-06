#!/usr/bin/python3
i = 122
while i > 64:
    char = chr(i)
    print("{}".format(char), end='')
    if i % 2 == 0:
        i -= 33
    else:
        i += 31
