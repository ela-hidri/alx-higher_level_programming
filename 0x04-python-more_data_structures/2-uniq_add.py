#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    lis = []
    for i in range(0, len(my_list)):
        if my_list[i] not in lis:
            sum += my_list[i]
            lis.append(my_list[i])
    return sum
