#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    if idx < 0:
        return new_list
    i = 0
    for x in new_list:
        if i == idx:
            new_list[idx] = element
        i += 1
    return new_list
