#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for jump, j in enumerate(i):
            print("{:d}".format(j), end="")
            if (jump < len(i) - 1):
                print("{}".format(" "), end="")
        print()
