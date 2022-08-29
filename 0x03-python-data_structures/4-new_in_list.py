#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    length_of_list = len(my_list) - 1
    if (idx < 0 or idx > length_of_list):
        return (my_list)
    else:
        new_list = my_list[:]
        new_list[idx] = element
        return (new_list)
