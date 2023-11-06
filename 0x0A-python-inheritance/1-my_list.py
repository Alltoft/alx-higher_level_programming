#!/usr/bin/python3
"""
a class MyList that inherits from list
"""


class MyList(list):
    """Public instance method: def print_sorted(self): that prints
the list, but sorted (ascending sort)
You can assume that all the elements of the list will be of type int
You are not allowed to import any module"""
    def print_sorted(self):
        sor_list = sorted(self)
        print(sor_list)
