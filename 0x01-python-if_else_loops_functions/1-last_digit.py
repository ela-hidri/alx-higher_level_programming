#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lstdegit = abs(number) % 10
if number < 0:
    lstdegit *= -1
if lstdegit > 5:
    print("Last digit of {:d} is {:d} and is greater than 5"
          .format(number, lstdegit))
elif lstdegit == 0:
    print("Last digit of {:d} is {:d} and is 0"
          .format(number, lstdegit))
elif lstdegit < 6:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, lstdegit))
