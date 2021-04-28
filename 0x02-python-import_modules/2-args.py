#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 0
    length = len(sys.argv) - 1
    if length == 0:
        print("{:d} arguments.".format(length))
    else:
        if length == 1:
            print("{:d} argument:".format(length))
        else:
            print("{:d} arguments:".format(length))
    for num in range(1, length + 1):
        i += 1
        print("{:d}: {:s}".format(num, sys.argv[i]))
