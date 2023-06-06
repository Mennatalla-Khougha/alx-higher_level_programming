#!/usr/bin/python3
i = 122
while i > 64:
    if i == 65:
        print(chr(i), end='')
        break
    if i > 96:
        print(chr(i), end='')
        i -= 33
    else:
        print(chr(i), end='')
        i += 31
