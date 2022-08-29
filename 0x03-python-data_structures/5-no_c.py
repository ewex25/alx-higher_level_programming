#!/usr/bin/python3
def no_c(my_string):
    fresh_string = ''
    for c in my_string:
        if (c not in ('c', 'C')):
            fresh_string += c
    return fresh_string
