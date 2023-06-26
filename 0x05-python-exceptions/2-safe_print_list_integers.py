#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    val = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[x]))
            val += 1
        except (TypeError, ValueError):
            break
        return val
