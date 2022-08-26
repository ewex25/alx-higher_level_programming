#!/usr/bin/python3
tmp_str = ""
for i in reversed(range(97, 123)):
    if (i % 2) == 0:
        tmp_str += chr(i)
    else:
        tmp_str += chr(i-32)
print("{}".format(tmp_str), end="")
