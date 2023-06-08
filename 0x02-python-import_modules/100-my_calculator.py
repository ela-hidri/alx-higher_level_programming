#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        o = argv[2]
        op = ["+", "-", "*", "/"]
        if o not in op:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
        a = int(argv[1])
        b = int(argv[3])
        if o == "+":
            print("{} + {} = {}".format(a, b, add(a, b)))
        elif o == "-":
            print("{} - {} = {}".format(a, b, sub(a, b)))
        elif o == "*":
            print("{} * {} = {}".format(a, b, mul(a, b)))
        elif o == "/":
            print("{} / {} = {}".format(a, b, div(a, b)))
