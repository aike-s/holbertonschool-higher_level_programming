#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    div_num = []
    for i in range(0, list_length):
        try:
            div_num.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            div_num.append(0)
            print('division by 0')
        except TypeError:
            div_num.append(0)
            print('wrong type')
        except IndexError:
            div_num.append(0)
            print('out of range')
        finally:
            pass
    return div_num
