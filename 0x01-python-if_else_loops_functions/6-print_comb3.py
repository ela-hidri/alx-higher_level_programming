#!/usr/bin/python3
for n in range(10):
    for j in range(10):
        if n < j and n != j and n != 9 and j != 9:
            print("{:d}{:d} ,".format(n, j), end="")
print("{:d}{:d}".format(n, j))
