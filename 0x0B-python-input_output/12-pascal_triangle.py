#!/usr/bin/python3
"""
define function
"""


def pascal_triangle(n):
    """
    define function that returns a list of lists of integers representing
    the Pascal’s triangle of n
    """
    if n <= 0:
        return []
    li = [[1]]
    while (len(li) != n):
        tt = li[-1]
        tm = [1]
        for o in range(len(tt) - 1):
            tm.append(tt[o] + tt[o + 1])
        tm.append(1)
        li.append(tm)
    return li
