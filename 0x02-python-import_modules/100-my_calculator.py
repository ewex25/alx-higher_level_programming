#!/usr/bin/python3

def new_cal():
    ops = {"+": add, "-": sub, "*": mul, "/": div}
    length = len(argv) - 1
    if (length < 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    oprtr = argv[2]

    if oprtr not in ops:
        print("Unknown operator. available operators: +, -, *, /")
        exit(1)
    result = ops[oprtr](a, b)
    print("{} {} {} = {}".format(a, oprtr, b, result))


if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    new_cal()
