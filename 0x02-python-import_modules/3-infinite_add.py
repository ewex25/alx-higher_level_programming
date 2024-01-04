#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum_of_all_args = 0
    n = 0
    for a in sys.argv:
        if n > 0:
            sum_of_all_args += int(a)
        n += 1
    print(sum_of_all_args)
