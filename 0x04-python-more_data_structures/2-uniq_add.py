#!/usr/bin/python3
def uniq_add(mylist=[]):
    from functools import reduce
    my_set = set(my_list)
    new_list = list(my_set)
    result = reduce(lambda x, y: x + y, new_list)
    return result
