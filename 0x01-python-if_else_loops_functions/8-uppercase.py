#!/usr/bin/python3
def uppercase(str):
    tmp_str = ""
    for a in str:
        if ord(a) > 96 and ord(a) < 123:
            tmp_str += chr(ord(a)-32)
        else:
            tmp_str += a
    print("{}".format(tmp_str))
