#!/usr/bin/python3
sprtr = ", "
for i in range(0, 100):
    num2 = i % 10
    num1 = i / 10
    if i < 10 and num1 < num2:
        print("{}{}".format(0, i), end=sprtr)
    elif num1 < num2:
        if i == 89:
            sprtr = "\n"
        print(i, end=sprtr)
