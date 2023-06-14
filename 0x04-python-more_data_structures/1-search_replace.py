#!/usr/bin/python3
def exist(x, s, rep):
    if x == s:
        return rep
    else:
        return x


def search_replace(my_list, search, replace):
    listt = my_list[:]
    for x in range(0, len(listt)):
        listt[x] = exist(listt[x], search, replace)
    return listt
