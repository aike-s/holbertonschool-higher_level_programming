#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    divide = 0
    total = 0
    for element in my_list:
        total += int(element[0] * element[1])
        divide += int(element[1])
    return total / divide
