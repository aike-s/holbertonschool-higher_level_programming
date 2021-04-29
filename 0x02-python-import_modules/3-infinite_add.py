#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    i = 0
    sys.argv.pop(0)
    # Eliminates the first argument
    num_list = list(map(int, sys.argv))
    # Converts all the arguments into integers
    length = len(num_list)
    if length < 1:
        print("{}".format(0))
        quit()
    total = num_list[0]
    for x in range(1, length):
        i += 1
        total += num_list[i]
    print("{:d}".format(total))
