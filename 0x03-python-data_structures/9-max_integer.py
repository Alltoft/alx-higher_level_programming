#!/usr/bin/python3
def max_integer(my_list=[]):
    is_very_big = my_list[0]
    for i in my_list:
        if i > is_very_big:
            is_very_big = i
    return is_very_big
