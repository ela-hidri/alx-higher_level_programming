#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dic = dict(a_dictionary)
    for i in dic:
        dic[i] *= 2
    return dic
