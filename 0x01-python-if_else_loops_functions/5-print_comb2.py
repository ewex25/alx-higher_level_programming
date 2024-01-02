#!/usr/bin/python3
sprtr = ", "
for i in range(0, 100):
    if i < 10:
        print("{}{}".format(0, i), end=sprtr)
    else:
        if i == 99:
            sprtr = "\n"
        print(i, end=sprtr)
