#!/usr/bin/python3
def common_elements(set_1, set_2):
    lis = []
    for n in set_1:
        if n in set_2:
            lis.append(n)
    return lis
