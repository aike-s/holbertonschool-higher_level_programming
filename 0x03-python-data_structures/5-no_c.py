def no_c(my_string):
    bad_c = ['c', 'C']
    my_string = ''.join(i for i in my_string if not i in bad_c)
    return my_string
