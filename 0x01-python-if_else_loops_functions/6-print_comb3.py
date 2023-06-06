#!/usr/bin/python3
for n in range(10):
    for j in range(10):
        if n < j and n != j:
            if n == 8 and j == 9:
                print("{:d}{:d}".format(n, j))
            else:
                print("{:d}{:d} ,".format(n, j), end="")
