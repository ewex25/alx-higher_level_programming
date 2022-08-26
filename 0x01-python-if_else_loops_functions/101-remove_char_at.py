#!/usr/bin/python3
def remove_char_at(str, n):
    tmp_str = ""
    cont = 0
    for c in str:
        if cont == n:
            pass
        else:
            tmp_str += c
        cont += 1
    return tmp_str
