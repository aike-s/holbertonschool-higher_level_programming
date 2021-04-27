#!/usr/bin/python3
for letter in range(97, 123):
    if letter == 101:
        continue
    elif letter == 113:
        continue
    else:
        print("{:s}".format(chr(letter)), end='')
