#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    Old_tuple = tuple_a + (0, 0)
    Older_tuple = tuple_b + (0, 0)
    resault_tuple = (Old_tuple[0] + Older_tuple[0], Older_tuple[1] + Old_tuple[1])
    return resault_tuple