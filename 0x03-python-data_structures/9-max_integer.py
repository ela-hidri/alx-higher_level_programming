#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    maxv = my_list[0]
    for i in range(1, len(my_list)):
        if maxv < my_list[i]:
            maxv = my_list[i]
    return maxv
