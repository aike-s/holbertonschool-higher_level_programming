#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        num_print = 0
        for i in range(0, x):
            if type(my_list[i]) == int:
                print("{:d}".format(my_list[i]), end='')
                num_print += 1
        print('')
        return num_print
    except:
        raise IndexError('list index out of range')
