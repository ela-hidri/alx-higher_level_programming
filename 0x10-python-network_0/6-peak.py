#!/usr/bin/python3
""" 
define a function
"""


def find_peak(list_of_integers):
    """ 
    defining a function that finds a peak
    """
    if len(list_of_integers) == 0 or list_of_integers is None:
        return None
    s, e = 0,  len(list_of_integers) - 1

    while s < e:
        m = s + (e - s) // 2
        if (list_of_integers[m] > list_of_integers[m - 1] and
            list_of_integers[m] > list_of_integers[m + 1] ):
               return list_of_integers[m]
        if list_of_integers[m - 1] > list_of_integers[m + 1]:
            e = m
        else:
            s = m + 1
    return list_of_integers[s]
