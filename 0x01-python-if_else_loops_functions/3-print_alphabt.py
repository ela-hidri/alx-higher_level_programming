#!/usr/bin/python3
for n in range(ord('a'), ord("z")+1):
    if n is not ord('q') and n is not ord('e'):
        print("{:s}".format(chr(n).lower()), end="")
