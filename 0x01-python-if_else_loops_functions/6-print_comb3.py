#!/usr/bin/python3
for num1 in range(0, 10):
    for num2 in range(0, 10):
        s_num = ((num1 * 10) + num2)
        if s_num == 89:
            print("{:d}".format(89))
        elif num1 < num2:
            print("{:d}{:d}, ".format(num1, num2), end='')
