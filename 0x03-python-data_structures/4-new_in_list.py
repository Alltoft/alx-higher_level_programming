#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return my_list
    rep_list = my_list.copy()
    rep_list[idx] = element
    return rep_list
