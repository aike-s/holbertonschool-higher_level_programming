#!/usr/bin/python3
def uppercase(str):
    for character in str:
        n_char = ord(character)
        if n_char >= 97 and n_char <= 122:
            n_char -= 32
        print("{:s}".format(chr(n_char)), end='')
    print('\n', end='')
